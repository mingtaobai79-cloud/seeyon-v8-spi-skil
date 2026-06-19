# Jar Contract Indexing 方案草案

> 目标：把 jar 处理降级为“外部索引未命中后的本地事实补充”。默认不把大 jar、完整反编译源码塞进 skill；优先外部索引库（Swagger/OpenAPI/MCP/HTTP），再查本地轻量 jar index，最后才 targeted jar probe。


## 0. 定位调整：External Index First

Jar Contract Index 不是第一入口，而是外部契约索引未命中后的本地补充。

新的查询顺序：

```
External Contract Index（Swagger/OpenAPI/MCP/HTTP）
  → Local Jar Contract Index（轻量 JSONL/SQLite）
  → Targeted Jar Probe（单类/目标包）
  → Version Matrix / 手工推断
```

设计原则：

1. 几百 MB 的 jar 不默认整包反编译。
2. skill 不保存完整 jar、不保存完整反编译源码、不复制 Swagger 正文。
3. jar index 只保存可查询的轻量事实：symbols/methods/fields/meta。
4. 外部索引 exact match 命中时，禁止继续手搓接口。
5. 只有外部索引、本地索引都找不到，才对用户提供的 jar 做 targeted probe。

外部索引配置见：`config/external-indexes.yaml`
外部索引规则见：`references/contract-index/external-contract-index.md`

## 1. 问题定义

原 `references/contract-index/tools/decompile_jar.py` 是一次性流水线：

```
Jar → CFR → Decompiled Source → Contract Extract → stdout summary
```

问题：

1. 反编译结果没有结构化持久化。
2. 同一个 jar 每次都可能重复反编译。
3. Contract 不能按接口名、方法名、DTO、版本、scope 快速命中。
4. Version Matrix 仍然承担过多推断职责。
5. 初期已有 jar 不能统一导入形成索引库。

目标改成：

```
External query → local index query → jar fingerprint → targeted scan/probe → optional decompile → lightweight index
```

## 2. 总体设计

### 2.1 核心目录

建议在 skill 内新增：

```
references/facts/
└── jar-contracts/
    ├── registry.jsonl              # 每个 jar 一条记录
    ├── sqlite.db                   # 主查询索引，可选但推荐
    ├── by-sha256/
    │   └── {sha256}/
    │       ├── jar-meta.json
    │       ├── contracts.jsonl
    │       ├── symbols.jsonl
    │       ├── methods.jsonl
    │       ├── fields.jsonl
    │       ├── normalized-contract.json
    │       ├── contract.md
    │       └── decompiled/         # 可选缓存，体积大时可关闭
    └── aliases/
        ├── ctp-user-api-5.3.351.json
        └── cip-connector-api-3.10.1.json
```

说明：

- `registry.jsonl`：轻量、可 diff、可人工查看。
- `sqlite.db`：真正用于快速查询；支持接口名、方法名、包名、版本、jar 名、scope 检索。
- `by-sha256/{sha256}`：以内容哈希做唯一主键，避免同名不同 jar 或不同名同 jar。
- 默认不保存完整 jar / 完整 decompiled 源码；`decompiled/` 只在 `--keep-source` debug 时保留。
- `aliases/`：按常见 jar 名/版本建立别名，方便命中。

### 2.2 为什么不是只写 md

md 适合人读，不适合稳定命中：

- 搜索方法签名容易误命中。
- 无法快速按 DTO → 接口反查。
- 无法表达 jar 指纹和版本可信度。
- 无法判断缓存是否过期。

所以需要：

- JSONL/SQLite 做机器索引。
- contract.md 做人工摘要。

## 3. 数据模型

### 3.1 jar-meta.json

```json
{
  "sha256": "...",
  "file_name": "ctp-user-api-5.3.351.jar",
  "artifact_id": "ctp-user-api",
  "version": "5.3.351",
  "size": 1234567,
  "indexed_at": "2026-06-12T10:00:00+08:00",
  "decompiler": "cfr-0.152",
  "source": {
    "type": "local_file",
    "path": "C:/.../ctp-user-api-5.3.351.jar"
  },
  "evidence": "FACT"
}
```

### 3.2 contracts.jsonl

每个 class/interface/enum 一行：

```json
{
  "sha256": "...",
  "artifact_id": "ctp-user-api",
  "version": "5.3.351",
  "kind": "interface",
  "package": "com.seeyon.ctp.user.api.sso",
  "name": "CtpUserSsoAuthProviderService",
  "fqn": "com.seeyon.ctp.user.api.sso.CtpUserSsoAuthProviderService",
  "extends": [],
  "implements": [],
  "annotations": ["CtpUserComment"],
  "source_file": "decompiled/.../CtpUserSsoAuthProviderService.java",
  "domain_hint": "sso.unifiedauth"
}
```

### 3.3 methods.jsonl

每个方法一行：

```json
{
  "sha256": "...",
  "owner_fqn": "com.seeyon.ctp.user.api.sso.CtpUserSsoAuthProviderService",
  "method_name": "getUserLoginInfo",
  "return_type": "CtpUserSpiLoginUserInfoDto",
  "params": [
    {"type": "HttpServletRequest", "name": "request"},
    {"type": "String", "name": "encodeRedirectUrl"}
  ],
  "throws": ["CtpUserSpiSsoException", "SpiAuthContinueException"],
  "default": false,
  "static": false,
  "comment": "从三方认证接口中获取用户信息",
  "signature": "CtpUserSpiLoginUserInfoDto getUserLoginInfo(HttpServletRequest request, String encodeRedirectUrl) throws ..."
}
```

### 3.4 fields.jsonl

每个 DTO 字段一行：

```json
{
  "sha256": "...",
  "owner_fqn": "com.seeyon.ctp.user.dto.CtpAvoidLoginUserInfoDto",
  "field_name": "thirdUserCode",
  "field_type": "String",
  "comment": "三方用户编码"
}
```

### 3.5 normalized-contract.json

面向生成器的归一化结果：

```json
{
  "domains": {
    "sso.unifiedauth": {
      "interfaces": ["com.seeyon.ctp.user.api.sso.CtpUserSsoAuthProviderService"],
      "required_methods": [...],
      "optional_methods": [...],
      "dto": [...],
      "exceptions": [...],
      "annotations": [...],
      "resources": ["spring.factories", "spi_info.json"]
    },
    "sso.avoidlogin": {...},
    "sso.connector": {...}
  }
}
```

## 4. 查询能力

脚本需要支持：

```bash
# 导入一个 jar
python references/contract-index/tools/decompile_jar.py index C:/path/ctp-user-api-5.3.351.jar

# 批量导入目录下所有 jar
python references/contract-index/tools/decompile_jar.py index-dir C:/path/jars --pattern "*.jar"

# 查询接口
python references/contract-index/tools/decompile_jar.py query --symbol CtpUserSsoAuthProviderService

# 查询 FQN
python references/contract-index/tools/decompile_jar.py query --fqn com.seeyon.ctp.user.api.sso.CtpUserSsoAuthProviderService

# 查询方法
python references/contract-index/tools/decompile_jar.py query --method getUserLoginInfo

# 按领域查询
python references/contract-index/tools/decompile_jar.py query --domain sso.unifiedauth

# 输出某个 jar 的 contract.md
python references/contract-index/tools/decompile_jar.py export --sha256 xxx --format md

# 验证索引状态
python references/contract-index/tools/decompile_jar.py status
```

## 5. 命中策略

### 5.1 有 jar 时

1. 先查 external index；如果 exact match，直接返回 FACT。
2. 计算 sha256。
3. 查 `registry.jsonl` / sqlite：
   - 命中 sha256：直接使用已有 Contract Index。
   - 未命中且 jar 很大：先 targeted scan/probe 目标 class/method。
   - 只有确实需要完整 Contract Bundle 时，才反编译并写入轻量索引。
4. 生成代码时标注：`Contract Source: external-index / jar index sha256=... / targeted-probe`。

### 5.2 没 jar 但有版本号时

1. 用 artifact_id + version 查 aliases。
2. 命中：使用索引，但标注：
   - 如果用户版本和索引版本完全一致：FACT ✅ indexed jar
   - 如果只命中相邻版本：OBSERVATION/WARN，要求用户提供 jar 验证
3. 不命中：降级到 `references/auth-sso/shared/version-matrix.md`。

### 5.3 没 jar 也没版本号

1. 先问用户 V8 版本或 jar。
2. 如果必须继续，使用最低置信度推断。
3. 生成报告中明确：`Contract confidence: low`。

## 6. 初期批量导入

建议初期收集并导入：

```
ctp-user-api-5.2.x.jar
ctp-user-api-5.3.293.jar
ctp-user-api-5.3.351.jar
cip-connector-api-3.10.1.jar
cip-connector-api-5.3.x.jar（如存在）
```

导入命令：

```bash
python references/contract-index/tools/decompile_jar.py index-dir C:/path/to/initial-jars --pattern "*.jar"
python references/contract-index/tools/decompile_jar.py status
```

导入后生成：

- registry.jsonl
- sqlite.db
- 每个 jar 的 contract.md
- 每个 jar 的 normalized-contract.json

## 7. 脚本改造计划

### Phase 1：兼容旧命令 + 建索引

保留旧用法：

```bash
python references/contract-index/tools/decompile_jar.py <jar_path> <output_dir>
```

新增子命令：

```bash
python references/contract-index/tools/decompile_jar.py index <jar_path>
python references/contract-index/tools/decompile_jar.py query --symbol Xxx
python references/contract-index/tools/decompile_jar.py status
```

实现：

- argparse 子命令。
- sha256 指纹。
- jar 文件名解析 artifact/version。
- CFR 输出缓存。
- JSONL 写入。
- contract.md 生成。

### Phase 2：SQLite 查询

新增 sqlite 表：

```sql
CREATE TABLE jars (
  sha256 TEXT PRIMARY KEY,
  file_name TEXT,
  artifact_id TEXT,
  version TEXT,
  size INTEGER,
  indexed_at TEXT,
  decompiler TEXT
);

CREATE TABLE symbols (
  id INTEGER PRIMARY KEY,
  sha256 TEXT,
  kind TEXT,
  package TEXT,
  name TEXT,
  fqn TEXT,
  domain_hint TEXT
);

CREATE TABLE methods (
  id INTEGER PRIMARY KEY,
  sha256 TEXT,
  owner_fqn TEXT,
  method_name TEXT,
  return_type TEXT,
  params_json TEXT,
  throws_json TEXT,
  is_default INTEGER,
  signature TEXT,
  comment TEXT
);

CREATE TABLE fields (
  id INTEGER PRIMARY KEY,
  sha256 TEXT,
  owner_fqn TEXT,
  field_name TEXT,
  field_type TEXT,
  comment TEXT
);

CREATE INDEX idx_symbols_name ON symbols(name);
CREATE INDEX idx_symbols_fqn ON symbols(fqn);
CREATE INDEX idx_methods_name ON methods(method_name);
CREATE INDEX idx_methods_owner ON methods(owner_fqn);
```

### Phase 3：领域归类

用规则把 Contract 自动归类：

| 规则 | domain_hint |
|------|-------------|
| FQN contains `.api.sso.` + `CtpUserSsoAuthProviderService` | `sso.unifiedauth` |
| FQN contains `.api.avoidlogin.` | `sso.avoidlogin` |
| FQN contains `cip.connector.api.sso.SsoService` | `sso.connector` |
| DTO package contains `ctp.user.dto` and referenced by SSO interface | `sso.dto` |
| Exception package contains `ctp.user.exception` | `sso.exception` |

未来其他 SPI 增加自己的 domain rules，不污染 SSO。

### Phase 4：生成器接入

生成代码前：

1. 先查 index。
2. 找到 exact contract。
3. 把 contract bundle 注入生成上下文。
4. Health Check 校验代码方法签名和 index 一致。

## 8. 版本与证据策略

- jar sha256 命中：FACT ✅
- artifact_id + version 命中：FACT ✅ if exact version + known sha256
- 只命中相邻版本：OBSERVATION ⚠️
- Version Matrix 推断：HYPOTHESIS ❓

生成报告必须显示：

```text
Contract Source: indexed jar
Artifact: ctp-user-api
Version: 5.3.351
SHA256: xxxx
Evidence: FACT ✅
```

## 9. 注意事项

1. 索引是“事实缓存”，不是猜测缓存。
2. 同名 jar 不可信，sha256 才是主键。
3. 用户提供的新 jar 即使文件名版本相同，也要按 sha256 判断是否新契约。
4. decompiled/ 目录可选保留，JSONL/SQLite 必须保留。
5. auth-sso 域文档是人工知识；`references/contract-index/` 是机器事实索引，两者不要混放。
6. OpenAPI 文档索引仍走 `references/contract-index/external-contract-index.md`，不要塞进 jar contract index。

## 10. 待确认点

1. 索引目录是否放 skill 内：`references/contract-index/`，还是放 Hermes 全局缓存目录？
   - 建议：skill 内保存可复用事实索引；大文件 decompiled 可配置是否保留。
2. 是否默认保留 decompiled 源码？
   - 建议：默认保留 contract JSON/MD，不保留完整 decompiled；需要 debug 时加 `--keep-source`。
3. 初期 jar 来源目录由谁提供？
   - 建议用户提供一个 `initial-jars/` 目录，脚本批量导入。
4. 是否把 SQLite 作为必选？
   - 建议必选。Python stdlib 自带 sqlite3，无额外依赖。

