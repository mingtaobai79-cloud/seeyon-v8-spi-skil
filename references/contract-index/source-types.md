# Contract Index Source Types

## 目标

把 Contract Index 的来源分类讲清楚，避免把“来源类型”“查询能力”“证据等级”混在一起。

核心分层：

```text
用户查询意图 → capability → source adapter → evidence output
```

source 只说明“从哪里查”；capability 说明“能查什么”；evidence 说明“查到的东西可信到什么程度”。

## 1. OpenAPI / Swagger

| 字段 | 说明 |
|------|------|
| Contract Source | `external-index` |
| Source Type | `openapi` / `swagger` |
| 典型 capability | `resolve_operation`, `resolve_schema`, `search_symbol`, `search_method` |
| 强项 | REST path/method/operationId/schema/DTO fields |
| 弱项 | Java interface overload、jar artifact 内部类、非 REST SPI |
| FACT 条件 | spec URL 可定位，并且 operation/schema exact match |

适合查询：

- REST path 是否存在
- operationId 对应的 request/response schema
- DTO 字段、enum、required 字段
- method/path/status code/header contract

不要做：

- 把完整 spec 正文复制进 skill
- 只因 schema 名称相似就当 FACT
- 用 OpenAPI 推断 Java overload 签名，除非 spec 明确暴露

## 2. MCP

| 字段 | 说明 |
|------|------|
| Contract Source | `external-index` |
| Source Type | `mcp` |
| 典型 capability | 由 `capabilities` 映射声明，不能硬编码假设 |
| 强项 | 能统一包一层内部搜索、文档库、OpenAPI、jar probe |
| 弱项 | 每个 MCP server 支持的 tool set 可能完全不同 |
| FACT 条件 | MCP 返回可定位来源，且 capability 结果是 exact match |

MCP 是 adapter，不是固定接口标准。配置里只声明当前 MCP 实际支持的 capability：

```yaml
capabilities:
  search_symbol:
    tool: mcp_seeyon_contract_search
    args_map:
      symbol: query
  probe_class:
    unsupported: true
```

规则：

- 不要求每个 MCP 都有 `search_symbol/search_method/get_openapi/resolve_artifact/probe_class`。
- capability 缺失时输出 `Missing Capability`，然后降级到下一个 source。
- 如果 MCP 返回的是“历史样例/相邻版本”，最多 OBSERVATION，不能标 FACT。

## 3. HTTP 文档索引

| 字段 | 说明 |
|------|------|
| Contract Source | `external-index` |
| Source Type | `http` |
| 典型 capability | `search_symbol`, `search_method`, `resolve_artifact` |
| 强项 | 企业内部文档库、全文搜索、私有索引服务 |
| 弱项 | schema 结构化程度不稳定，返回格式因服务而异 |
| FACT 条件 | HTTP 返回明确 contract locator，且 exact match |

HTTP source 也走 capability mapping，不把 URL 直接等同于能力。一个 HTTP 搜索服务可能只支持 keyword search，不支持 schema resolve。

## 4. Local Jar Index

| 字段 | 说明 |
|------|------|
| Contract Source | `local-jar-index` |
| Source Type | `jar` |
| 典型 capability | `search_symbol`, `search_method`, `resolve_artifact` |
| 强项 | 本地 jar 已索引时快速确认 class/method/artifact |
| 弱项 | 只能覆盖已导入 jar；索引粒度取决于脚本 |
| FACT 条件 | jar SHA256 / artifact version exact match |

位置：

```text
references/contract-index/
```

规则：

- 只保存轻量 JSONL/MD 事实。
- 不保存完整 jar。
- 不保存完整反编译源码。
- 命中时必须输出 SHA256 或 artifact/version。

## 5. Targeted Jar Probe

| 字段 | 说明 |
|------|------|
| Contract Source | `targeted-jar-probe` |
| Source Type | `javap` |
| 典型 capability | `probe_class`, `search_method` |
| 强项 | 本地索引没命中但知道 class/method 时，定点确认签名 |
| 弱项 | 覆盖范围只限本次 probe 的目标 |
| FACT 条件 | javap/反射/定点输出明确目标 class/method |

规则：

- 先 targeted probe，不默认整包反编译。
- 只把本次 probe 范围标 FACT。
- 不把 probe 结果扩大推断到整个 jar。

## 6. Version Matrix

| 字段 | 说明 |
|------|------|
| Contract Source | `version-matrix` |
| Source Type | `hypothesis` |
| 典型 capability | 无真实 capability，只是兜底参考 |
| 强项 | 无索引、无 jar、无源码时提供方向 |
| 弱项 | 不能当事实生成关键契约 |
| Evidence | OBSERVATION 或 HYPOTHESIS，默认 HYPOTHESIS |

只有以下都失败时才用：

1. OpenAPI/Swagger 未命中
2. MCP 未命中或 capability 缺失
3. HTTP 未命中
4. local_doc_index / Yuque rendered-md 未命中或证据不足
5. local jar index 未命中
6. targeted jar probe 不可用或未命中

## 降级顺序

```text
OpenAPI/Swagger exact match
  → MCP capability adapter
  → HTTP capability adapter
  → local_doc_index / Yuque rendered-md (OBSERVATION)
  → local jar index
  → targeted jar probe
  → version matrix / manual hypothesis
```

## 证据边界

- exact external match：FACT。
- MCP/HTTP 只返回搜索摘要：OBSERVATION，除非有可定位 contract source。
- local_doc_index / Yuque rendered-md：OBSERVATION，不能单独升级为 FACT。
- local jar SHA256 exact match：FACT。
- targeted jar probe：FACT，但只限目标 class/method。
- version matrix：HYPOTHESIS，除非引用了可验证历史样例，才是 OBSERVATION。


## local_doc_index / Yuque rendered-md

- Path: `references/facts/yuque-v8-docs-rendered-md/docs/`
- Manifest: `references/facts/yuque-v8-docs-rendered-md/manifest.json`
- Source Type: `yuque-rendered-md`
- Capabilities: keyword-style `search_symbol`, `search_method`, `resolve_operation`, `resolve_schema`
- Evidence ceiling: OBSERVATION. Use jar/source/OpenAPI exact match to upgrade to FACT.
- Adapter: `references/contract-index/tools/query_yuque_local_index.py` from this module.
