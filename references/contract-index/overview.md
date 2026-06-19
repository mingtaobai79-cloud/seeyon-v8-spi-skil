
# Seeyon Contract Index 模块入口

## Overview

本文件是 `seeyon-v8-spi` 的 Contract Index 模块入口。主流程以路径读取 `references/contract-index/` 为准，不依赖 nested skill loader 行为。

它不负责生成 SSO 代码，也不保存大 jar / Swagger 正文 / 反编译源码；它只负责：

1. 检查外部索引配置是否可用。
2. 决定本次是否走外部契约索引。
3. 把用户的查询意图归一成通用 capability。
4. 按顺序查询：OpenAPI/Swagger → MCP adapter → HTTP adapter → 事实库 rendered-md 文档索引 → 本地 jar index → targeted jar probe → Version Matrix。
5. 输出带 evidence/source/locator 的 Contract 查询结果。

核心原则：

```text
Contract First，但不是 Jar First。
外部索引能命中，就不手搓、不反编译。
MCP 是 adapter，不是统一工具名假设。
```

## When to Use

使用场景：

- 用户要生成/修改 Seeyon V8 SPI/SSO 代码。
- 用户提到 jar、接口契约、Swagger、OpenAPI、MCP、HTTP 文档索引、外部契约索引。
- 生成代码前需要确认接口、DTO、method signature、operationId、path、schema。
- 用户问“这个方法有没有”“这个接口在哪个版本”“有没有索引命中”。

不要用于：

- 纯业务方案讨论，不涉及接口契约。
- 已经有明确源码/接口定义，且用户要求直接按源码改。
- 用户明确说“跳过索引/不要查外部”。

## Mandatory Startup Check

每次被 `seeyon-v8-spi` 主入口路由到 Contract Index 模块时，先做状态检查。推荐从 `seeyon-v8-spi` 根目录执行：

```bash
python references/contract-index/tools/contract_index_status.py
```

状态分三类：

| 状态 | 含义 | 下一步 |
|------|------|--------|
| `READY` | 有 enabled 外部源，或本地 jar index 有数据 | 先查索引 |
| `CONFIG_NEEDED` | 配置存在但没有 enabled source，且本地 index 为空 | 提示用户配置或选择跳过 |
| `SKIP_REQUESTED` | 用户明确要求跳过索引 | 不查索引，继续主流程 |

## User Options

如果状态是 `CONFIG_NEEDED`，给用户三个选项，不要硬继续反编译：

1. 配置外部索引：提供 Swagger/OpenAPI/MCP/HTTP 地址。
2. 导入本地 jar index：提供 jar 目录，只做轻量索引或 targeted probe。
3. 跳过契约索引：继续当前任务，但 evidence 降级为 HYPOTHESIS/待验证。

提示模板：

```text
当前 Contract Index 未配置/无命中。你可以选：
A. 配置外部 Swagger/OpenAPI/MCP/HTTP 地址
B. 提供 jar 目录，建立轻量本地索引
C. 跳过索引，继续生成，但接口契约标记为 HYPOTHESIS
```

## 模块定位

```text
主目录：references/contract-index/
兼容入口：references/contract-index/overview.md
治理说明：references/contract-index/overview.md
主流程依赖：路径读取，不依赖 nested skill loader
```

## Configuration Files

唯一运行时配置文件：

```text
../../config/external-indexes.yaml
```

从 `seeyon-v8-spi` 根目录看就是：

```text
config/external-indexes.yaml
```

模块里的 YAML 只允许作为模板：

```text
config/external-indexes.template.yaml
```

规则：

1. Agent / 脚本读取配置时，只读 `seeyon-v8-spi/config/external-indexes.yaml`。
2. `config/external-indexes.template.yaml` 只用于初始化/重置，不是运行时配置。
3. 修改客户 Swagger/OpenAPI/MCP/HTTP 地址，只改外层 `config/external-indexes.yaml`。
4. 配置只放链接、开关、认证环境变量名、capability 映射，不放 token 明文、不放大文档正文。

初始化说明：

```text
references/contract-index/initialization.md
```

## Source Types

详细分类见 `references/contract-index/source-types.md`。当前来源分 6 类：

| Source | Source Type | 作用 |
|--------|-------------|------|
| `external-index` | `openapi` / `swagger` | 标准 REST 契约、operationId、path、method、schema |
| `external-index` | `mcp` | 通过 capability mapping 适配不同 MCP 工具集 |
| `external-index` | `http` | 企业内部文档索引 / 搜索接口 |
| `local-jar-index` | `jar` | 本地 jar 轻量索引，按 symbol/method/class 查 |
| `targeted-jar-probe` | `javap` | 已知目标 class/method 时做定点探测 |
| `version-matrix` | `hypothesis` | 兜底推断，只能给 OBSERVATION/HYPOTHESIS |

## Capability Contract

详细协议见 `references/contract-index/capability-contract.md`。

Contract Index 不直接假设某个外部源的具体 API，而是把查询归一成 capability：

| Capability | 含义 |
|------------|------|
| `search_symbol` | 查 class/interface/DTO/常量名 |
| `search_method` | 查 method signature / overload |
| `resolve_operation` | 查 REST operation/path/method/operationId |
| `resolve_schema` | 查 DTO schema / field / enum |
| `resolve_artifact` | 查 artifact/version/jar 坐标 |
| `probe_class` | 对目标 class 做定点探测 |

MCP/HTTP/OpenAPI/local jar 都只是这些 capability 的 adapter。某个 source 不支持某项 capability 时，记录 `Missing Capability`，然后降级到下一个 source。

## Query Order

固定顺序：

```text
1. external_openapi / external_swagger
2. external_mcp
3. external_http
4. local_doc_index (Yuque rendered-md)
5. local_jar_index
6. targeted_jar_probe
7. version_matrix
```

命中规则：

- exact external match：FACT ✅，停止继续查询。
- local_doc_index / Yuque rendered-md：OBSERVATION ⚠️，不能替代 jar/源码/OpenAPI exact match。
- local jar sha256 exact match：FACT ✅。
- targeted jar probe：FACT ✅，但范围只限目标 class/method。
- 相邻版本/历史样例：OBSERVATION ⚠️。
- Version Matrix / 手写推断：HYPOTHESIS ❓。

## Required Output

任何查询结果必须输出：

```text
Contract Source: external-index | local-jar-index | targeted-jar-probe | version-matrix
Source Type: openapi | swagger | mcp | http | jar | javap | hypothesis
Capability: search_symbol | search_method | resolve_operation | resolve_schema | resolve_artifact | probe_class
Evidence: FACT | OBSERVATION | HYPOTHESIS
Locator: URL / MCP server+tool / HTTP endpoint / SHA256 / artifact:version / class name
Missing Capability: none | <capability list>
```

## Common Commands

```bash
# 检查索引配置状态
python references/contract-index/tools/contract_index_status.py

# 本地 jar index 状态
python references/contract-index/tools/decompile_jar.py status

# 查询本地 jar index
python references/contract-index/tools/decompile_jar.py query --symbol CtpUserSsoAuthProviderService
python references/contract-index/tools/decompile_jar.py query --method getUserLoginInfo

# 查询事实库 rendered-md 文档索引（OBSERVATION）
python references/contract-index/tools/query_yuque_local_index.py "MQMessageSpi"
python references/contract-index/tools/query_yuque_local_index.py "CtpAvoidLoginMiddlePageProviderService"
```

## Common Pitfalls

1. 不要把本文件当成独立产品边界；它是 `seeyon-v8-spi` 的内部模块，skill 可发现只是兼容层。
2. 主入口不要把 nested skill loader 写成前置依赖；应写成读取 `references/contract-index/` 内部文件。
3. 不要把大 jar 放进 skill。
4. 不要把 Swagger/OpenAPI 正文复制进 SKILL.md。
5. 不要把 token 写进运行时配置；用 `token_env`。
6. 外部索引 exact match 已命中时，不要继续手搓。
7. 本地 jar 未命中时，不要默认整包反编译几百 MB jar，先 targeted probe。
8. 没跑 startup check 就生成代码，属于证据链缺失。
9. 不要假设所有 MCP 都支持同一组工具名；MCP 必须走 capability mapping。
10. MCP 缺 capability 不是失败，是降级信号：记录 Missing Capability 后继续下一个 source。
11. 不要把 `config/external-indexes.template.yaml` 当运行时配置；它只是模板，真实配置永远在 `config/external-indexes.yaml`。
12. 事实库语雀索引只保留 `references/facts/yuque-v8-docs-rendered-md/`；旧 `yuque-v8-docs*assets*` 和早期 `yuque-v8-docs/` 已移出 active 查询路径，不再查询。

## Verification Checklist

- [ ] 已运行 `contract_index_status.py`
- [ ] 主入口以路径读取模块，不依赖 nested skill loader
- [ ] 已确认状态：READY / CONFIG_NEEDED / SKIP_REQUESTED
- [ ] 如果 READY，先查索引再生成
- [ ] 如果 CONFIG_NEEDED，给用户 A/B/C 选项
- [ ] 输出包含 Contract Source / Source Type / Capability / Evidence / Locator / Missing Capability
- [ ] 未把大文件、token、完整 Swagger 正文写入 skill
- [ ] MCP/HTTP 外部源使用 capability mapping，不写死固定全量工具名
