# External Contract Index（外部契约索引库）

> 目标：不要把所有 jar、Swagger/OpenAPI、厂商文档都塞进 skill。本 skill 只保存“路由规则 + 索引配置 + 查询协议”，事实数据优先放外部索引库或远端 MCP/API。

## 1. 核心判断

大 jar / 多版本 jar 不能默认整包反编译入 skill。

原因：

1. jar 动辄几百 MB，skill 会迅速臃肿。
2. 同一客户/版本的 jar 可能包含大量与当前 SPI 无关的 class。
3. 反编译产物不适合长期塞在知识库里。
4. Swagger/OpenAPI、厂商接口平台、内部文档系统本身就是更好的事实源。

正确形态：

```text
用户需求
  ↓
External Contract Index（Swagger/OpenAPI/MCP/HTTP/文档索引）
  ↓ 未命中
Local Contract Index（已索引 jar 的轻量 JSONL/SQLite）
  ↓ 未命中
Targeted Jar Probe（只查目标 class/method，不整包）
  ↓ 未命中
Version Matrix / 手工推断（最低置信度）
```

## 2. 证据优先级

| 优先级 | 来源 | 证据等级 | 说明 |
|--------|------|----------|------|
| P0 | 用户本次提供的源码 / jar 精确 class | FACT ✅ | 当前项目真实契约 |
| P1 | 外部索引库 exact match：Swagger/OpenAPI/MCP/官方接口平台 | FACT ✅ | 可访问、可追溯 URL/接口返回 |
| P2 | 本地 jar contract index sha256 exact match | FACT ✅ | 已入库 jar 的结构化事实 |
| P3 | 本地 jar targeted probe：`jar tf` / `javap` 单类 | FACT ✅ | 不整包反编译，只验证目标 |
| P4 | 外部索引相邻版本 / 历史样例 | OBSERVATION ⚠️ | 只能辅助，不可当最终契约 |
| P5 | Version Matrix / 经验推断 | HYPOTHESIS ❓ | 最后兜底，必须提示待验证 |

## 3. 外部索引库配置

配置文件建议放：

```text
config/external-indexes.yaml
```

此文件只放“链接和查询方式”，不放大文档正文。

示例：

```yaml
version: 1

sources:
  - id: seeyon-v8-openapi-local
    type: openapi
    enabled: true
    base_url: "http://127.0.0.1:8080"
    specs:
      - name: user-center
        url: "http://127.0.0.1:8080/v3/api-docs/user-center"
      - name: org-model
        url: "http://127.0.0.1:8080/v3/api-docs/org-model"
    auth:
      type: none

  - id: customer-swagger
    type: swagger
    enabled: false
    specs:
      - name: default
        url: "https://example.com/swagger/v1/swagger.json"
    auth:
      type: bearer
      token_env: "CUSTOMER_SWAGGER_TOKEN"

  - id: seeyon-contract-mcp
    type: mcp
    enabled: false
    server_name: "seeyon_contract"
    tools:
      search_symbol: "mcp_seeyon_contract_search_symbol"
      search_method: "mcp_seeyon_contract_search_method"
      get_openapi: "mcp_seeyon_contract_get_openapi"

  - id: internal-doc-index
    type: http
    enabled: false
    base_url: "https://docs.example.com/api/search"
    auth:
      type: bearer
      token_env: "DOC_INDEX_TOKEN"
```

## 4. MCP 接入形态

如果外部系统已经有接口平台、Swagger 聚合、文档搜索、Maven 仓库索引，推荐外接 MCP。

Hermes 侧配置在 `~/.hermes/config.yaml`：

```yaml
mcp_servers:
  seeyon_contract:
    url: "https://contract-index.example.com/mcp"
    headers:
      Authorization: "Bearer ${SEEYON_CONTRACT_TOKEN}"
    timeout: 180
    connect_timeout: 30
```

MCP 工具建议提供：

```text
search_symbol(symbol, artifact?, version?, domain?)
search_method(method, owner?, artifact?, version?, domain?)
get_openapi(source_id, path_or_operation_id)
resolve_artifact(artifact_id, version)
probe_class(artifact_id, version, class_name)
```

返回必须带 evidence：

```json
{
  "evidence": "FACT",
  "source": {
    "type": "openapi",
    "source_id": "customer-swagger",
    "url": "https://example.com/swagger/v1/swagger.json",
    "fetched_at": "2026-06-12T10:00:00+08:00"
  },
  "matches": []
}
```

## 5. 查询决策流

### 5.1 查询接口 / DTO / 方法

```text
query_contract(symbol/method/domain)
  1. 读 config/external-indexes.yaml
  2. 查 enabled=true 的 external sources
     - openapi/swagger: 拉 spec 或读缓存，按 operationId/path/schema 搜索
     - mcp: 调用 MCP search_symbol/search_method
     - http: 调用外部搜索 API
  3. 若 exact match：返回 FACT，不再查 jar
  4. 若 external 未命中：查 local jar index
  5. 若 local 未命中但用户给了 jar：targeted probe 目标 class
  6. targeted probe 仍未命中：才允许手工推断
```

### 5.2 生成代码前

必须记录 Contract Source：

```text
Contract Source: external-index
Source Type: openapi/swagger/mcp/http/local-jar/targeted-jar-probe/version-matrix
Evidence: FACT/OBSERVATION/HYPOTHESIS
URL/SHA256/Artifact: ...
```

## 6. Jar 处理策略调整

### 不再默认整包反编译

大 jar 默认策略：

1. 先 `jar tf` 列 class。
2. 通过规则筛选目标包：
   - `*.api.*`
   - `*.spi.*`
   - `*.sso.*`
   - `*Service.class`
   - `*Provider.class`
   - `*Dto.class`
3. 只对命中的 class 做 `javap` 或单类 CFR。
4. 只有明确需要 DTO 字段/注解细节时，再小范围反编译。

### 本地 jar index 只存轻量事实

默认只保留：

```text
jar-meta.json
symbols.jsonl
methods.jsonl
fields.jsonl
contract.md
```

不默认保留：

```text
decompiled/
完整源码
完整 jar 副本
```

## 7. Skill 边界

本 skill 不应该变成：

- jar 仓库
- Swagger 文档仓库
- 反编译源码仓库
- 客户接口平台镜像

本 skill 只保留：

- 查询顺序
- 证据规则
- 配置模板
- 小型事实索引
- 必要的领域路由规则

## 8. 最小落地计划

### Phase E1：配置文件先行

新增：

```text
config/external-indexes.yaml
references/contract-index/external-contract-index.md
```

脚本新增命令规划：

```bash
python references/contract-index/tools/decompile_jar.py external-status
python references/contract-index/tools/decompile_jar.py external-query --symbol Xxx
python references/contract-index/tools/decompile_jar.py external-query --method methodName
```

### Phase E2：OpenAPI/Swagger 查询

实现：

- 读取 `external-indexes.yaml`
- 拉取 swagger/openapi JSON
- 本地缓存 spec fingerprint
- 按 operationId/path/schema 搜索

### Phase E3：MCP Adapter

不在脚本里硬编码 MCP 工具名，而从配置读取：

```yaml
server_name: seeyon_contract
tools:
  search_symbol: mcp_seeyon_contract_search_symbol
```

Hermes 启动后工具可用时，优先走 MCP；不可用时跳过，不阻塞本地 jar 查询。

### Phase E4：Targeted Jar Probe

为大 jar 增加：

```bash
python references/contract-index/tools/decompile_jar.py probe C:/path/big.jar --class com.xxx.Service
python references/contract-index/tools/decompile_jar.py scan C:/path/big.jar --include "*api*Service.class"
```

只输出目标 class/method，不整包入库。

## 9. 禁止项

1. 禁止把几百 MB jar 或完整反编译源码放进 skill。
2. 禁止外部索引能命中时继续手搓接口。
3. 禁止把 Swagger/OpenAPI 正文复制进 SKILL.md。
4. 禁止没有 evidence/source 的“看起来像接口”的手写契约。
5. 禁止把客户私有 URL/token 写死在 skill；只能通过配置文件和环境变量引用。
