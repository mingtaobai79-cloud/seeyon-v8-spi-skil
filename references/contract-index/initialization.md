# Seeyon Contract Index 初始化说明

## 目标

让复用 `seeyon-v8-spi` 的人能真正启用契约索引，而不是只看到一套原则。

初始化后，查询顺序是：

```text
Swagger/OpenAPI → MCP capability adapter → HTTP capability adapter
  → 本地语雀 rendered-md 文档索引
  → 本地轻量 jar index
  → targeted jar probe
  → Version Matrix / 手工推断
```

Contract Index 的统一协议见：

- `references/contract-index/source-types.md` — source 分类与证据边界
- `references/contract-index/capability-contract.md` — capability mapping 与 Missing Capability 降级规则


## 配置文件边界

Contract Index 只有一个运行时配置源：

```text
<skill-root>/config/external-indexes.yaml
```

模块里的文件只是模板：

```text
config/external-indexes.template.yaml
```

规则：

- `contract_index_status.py` 和后续查询 adapter 只读外层 `config/external-indexes.yaml`。
- 首次初始化/重置时，可以从模块模板复制到外层 config。
- 日常改客户地址、Swagger/OpenAPI/MCP/HTTP source、capability mapping，只改外层 config。
- 不要在模块 templates 里维护客户现场配置。

## 1. 首次状态检查

在本 skill 目录执行：

```bash
cd <skill-root>/references/contract-index
python references/contract-index/tools/contract_index_status.py
```

或从 `seeyon-v8-spi` 根目录执行：

```bash
cd <skill-root>
python references/contract-index/tools/contract_index_status.py
```

可能输出：

```text
STATUS: READY
```

表示已有 enabled 外部源，或本地 jar index 有数据。

```text
STATUS: CONFIG_NEEDED
```

表示还没有可用索引，需要配置或选择跳过。

## 2. 配置外部 Swagger/OpenAPI

首次没有外层运行时配置时，才复制模板：

```bash
cd <skill-root>
cp config/external-indexes.template.yaml config/external-indexes.yaml
```

修改：

```yaml
sources:
  - id: customer-openapi
    type: openapi
    enabled: true
    specs:
      - name: default
        url: "https://your-host/v3/api-docs"
    auth:
      type: bearer
      token_env: "CUSTOMER_OPENAPI_TOKEN"
    capabilities:
      resolve_operation:
        supported: true
      resolve_schema:
        supported: true
      search_symbol:
        supported: true
```

如果不需要认证：

```yaml
auth:
  type: none
```

不要把 token 明文写进 yaml。只写环境变量名。

## 3. 配置 MCP 外部索引

Hermes MCP 配置在：

```text
~/.hermes/config.yaml
```

示例：

```yaml
mcp_servers:
  seeyon_contract:
    url: "https://contract-index.example.com/mcp"
    headers:
      Authorization: "Bearer ${SEEYON_CONTRACT_TOKEN}"
    timeout: 180
    connect_timeout: 30
```

然后在本 skill 配置里启用。注意这里配置的是 capability mapping，不是固定工具名清单：

```yaml
sources:
  - id: seeyon-contract-mcp
    type: mcp
    enabled: true
    server_name: "seeyon_contract"
    capabilities:
      search_symbol:
        tool: "mcp_seeyon_contract_search"
        args_map:
          symbol: "query"
      search_method:
        tool: "mcp_seeyon_contract_search"
        args_map:
          method: "query"
          class_name: "className"
      resolve_operation:
        unsupported: true
      probe_class:
        unsupported: true
```

规则：

- 每个 MCP 只声明自己真实支持的 capability。
- 不要求所有 MCP 都支持 `search_symbol/search_method/resolve_operation/resolve_schema/resolve_artifact/probe_class`。
- capability 缺失时，记录 `Missing Capability` 并降级到下一个 source。

注意：Hermes 新增 MCP server 后需要重启，工具才会被发现。

## 4. 配置 HTTP 文档索引

HTTP source 也使用 capability mapping：

```yaml
sources:
  - id: internal-doc-index
    type: http
    enabled: true
    base_url: "https://docs.example.com/api"
    auth:
      type: bearer
      token_env: "DOC_INDEX_TOKEN"
    capabilities:
      search_symbol:
        method: GET
        path: "/search"
        query_map:
          symbol: "q"
      search_method:
        method: GET
        path: "/search"
        query_map:
          method: "q"
      resolve_schema:
        unsupported: true
```

HTTP 搜索命中不自动等于 FACT；必须返回可定位 contract source，才能标 FACT。

## 5. 导入本地 jar 轻量索引

如果暂时没有外部索引，但有 API jar：

```bash
cd <skill-root>
python references/contract-index/tools/decompile_jar.py index-dir C:/path/to/jars --pattern "*.jar"
python references/contract-index/tools/decompile_jar.py status
```

规则：

- 默认只保存 JSONL/MD 轻量事实。
- 不保存完整 jar。
- 不默认保存完整 decompiled 源码。
- 大 jar 优先 targeted probe，不要全量反编译。

## 6. 修改地址

以后客户地址、Swagger/OpenAPI 地址、MCP 地址、HTTP 文档索引地址、capability mapping 变了，只改外层运行时配置：

```text
config/external-indexes.yaml
```

修改后重新跑：

```bash
python references/contract-index/tools/contract_index_status.py
```

如果改的是 Hermes MCP server 地址，还要同步改：

```text
~/.hermes/config.yaml
```

并重启 Hermes。

## 7. 跳过索引

如果用户明确说跳过：

```text
跳过契约索引
不查外部索引
不用 jar index
```

则当前任务可以继续，但生成结果必须标记：

```text
Contract Source: version-matrix / manual
Source Type: hypothesis
Evidence: HYPOTHESIS ❓
```

## 8. 最小复用流程

```text
1. 加载 seeyon-v8-spi
2. 涉及契约查询时进入 references/contract-index
3. 运行 contract_index_status.py
4. 把查询意图归一成 capability
5. READY → 按 query_order 查 source adapter
6. source 缺 capability → 记录 Missing Capability，继续降级
7. CONFIG_NEEDED → 让用户选 A 配外部 / B 导 jar / C 跳过
8. 生成代码前输出 Contract Source + Source Type + Capability + Evidence + Locator
```
