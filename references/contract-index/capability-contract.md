# Contract Index Capability Contract

## 目标

定义 Contract Index 的统一查询协议，让 OpenAPI、MCP、HTTP、本地 jar index、targeted jar probe 都能接到同一套查询意图下。

关键判断：

```text
不要为每个 MCP 拆一个 skill。
MCP/HTTP/OpenAPI/local jar 都是 source adapter。
差异由 capability mapping 吸收。
```

## Capability 列表

| Capability | 输入 | 输出 | 典型来源 |
|------------|------|------|----------|
| `search_symbol` | symbol/class/interface/DTO 名 | 候选 contract + locator | MCP, HTTP, jar index, OpenAPI schema |
| `search_method` | method 名、可选 class、参数片段 | method signature / overload | MCP, HTTP, jar index, targeted probe |
| `resolve_operation` | path/method/operationId/关键词 | REST operation contract | OpenAPI, Swagger, MCP |
| `resolve_schema` | schema/DTO 名、字段名 | fields/types/required/enum | OpenAPI, Swagger, MCP |
| `resolve_artifact` | artifactId/groupId/version/类名 | jar 坐标、版本、SHA256 | MCP, HTTP, jar index |
| `probe_class` | jar 路径 + class 名 | javap/反射签名事实 | targeted jar probe, 特定 MCP |

## 标准输出 Envelope

任何 adapter 返回结果，都归一成：

```yaml
contract_source: external-index | local-jar-index | targeted-jar-probe | version-matrix
source_type: openapi | swagger | mcp | http | jar | javap | hypothesis
capability: search_symbol | search_method | resolve_operation | resolve_schema | resolve_artifact | probe_class
evidence: FACT | OBSERVATION | HYPOTHESIS
locator: <URL | server+tool | endpoint | SHA256 | artifact:version | class name>
missing_capability: []
result:
  summary: "human-readable contract summary"
  raw_ref: "do not inline large body; point to cache/path/url if needed"
```

## Capability Mapping 配置

外部 source 不直接假设工具名，统一写 capability mapping：

```yaml
sources:
  - id: seeyon-contract-mcp
    type: mcp
    enabled: true
    server_name: seeyon_contract
    capabilities:
      search_symbol:
        tool: mcp_seeyon_contract_search
        args_map:
          symbol: query
      search_method:
        tool: mcp_seeyon_contract_search
        args_map:
          method: query
          class_name: className
      resolve_operation:
        tool: mcp_seeyon_contract_openapi_lookup
        args_map:
          operation_id: operationId
      probe_class:
        unsupported: true
```

HTTP source 同理：

```yaml
sources:
  - id: internal-doc-index
    type: http
    enabled: true
    base_url: "https://docs.example.com/api/search"
    capabilities:
      search_symbol:
        method: GET
        path: "/search"
        query_map:
          symbol: q
      search_method:
        method: GET
        path: "/search"
        query_map:
          method: q
      resolve_schema:
        unsupported: true
```

OpenAPI/Swagger source 可以不显式声明所有 capability，但推荐写出 parser 能力：

```yaml
sources:
  - id: customer-openapi
    type: openapi
    enabled: true
    specs:
      - name: default
        url: "https://example.com/v3/api-docs"
    capabilities:
      resolve_operation:
        supported: true
      resolve_schema:
        supported: true
      search_symbol:
        supported: true
      probe_class:
        unsupported: true
```

## Missing Capability 规则

source 不支持 capability 时，不算失败，不要报错中断。必须输出降级记录：

```text
Contract Source: external-index
Source Type: mcp
Capability: probe_class
Evidence: HYPOTHESIS
Locator: seeyon_contract
Missing Capability: probe_class
Next: fallback to local_jar_index or targeted_jar_probe
```

使用规则：

1. 当前 source `enabled=false`：跳过，不输出 missing capability。
2. 当前 source `enabled=true` 但 capability 未声明：视为 unknown，除 OpenAPI/Swagger 默认 parser 能力外，不假设支持。
3. 当前 source 显式 `unsupported: true`：输出 Missing Capability，并降级。
4. 当前 source tool 调用失败：记录 error locator，但不要把未验证内容标 FACT。
5. 后续 source exact match 后，可停止继续查询。

## Evidence 判定

| 情况 | Evidence |
|------|----------|
| OpenAPI/Swagger operation/schema exact match | FACT |
| MCP 返回可定位官方/内部 contract source 且 exact match | FACT |
| MCP/HTTP 只返回搜索摘要或相似历史样例 | OBSERVATION |
| local jar SHA256/artifact exact match | FACT |
| targeted jar probe 输出目标 class/method | FACT，仅限 probe 范围 |
| version matrix / 手写推断 | HYPOTHESIS |

## Adapter 实现边界

- adapter 负责把 source-specific 输入输出映射到统一 envelope。
- adapter 不负责代码生成。
- adapter 不扩大证据范围。
- adapter 不把 token、完整 Swagger、完整 jar、完整反编译源码写入 skill。
- adapter 缺能力时只降级，不“脑补”结果。

## 查询决策伪流程

```text
for capability in requested_capabilities:
  for source in query_order:
    if source disabled:
      continue
    if source lacks capability:
      record Missing Capability
      continue
    result = call adapter
    if result exact FACT:
      return result
    if result observation:
      keep as fallback evidence
  return best observation or HYPOTHESIS
```

## 常见坑

1. 把 MCP tool 名当成统一协议。错，统一协议是 capability，不是 tool name。
2. 要求所有 MCP 都实现 search_symbol/search_method/get_openapi/probe_class。错，不同 MCP 支持不同能力。
3. capability 缺失就停止任务。错，应记录 Missing Capability 并降级。
4. HTTP 搜索命中标题就标 FACT。错，必须有可定位 contract source。
5. targeted probe 只查了一个 class，却把整个 jar 都标 FACT。错，FACT 只限 probe 范围。
