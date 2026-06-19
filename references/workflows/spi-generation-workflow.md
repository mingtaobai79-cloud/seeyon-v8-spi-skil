# SPI Generation Workflow 闭环

> 目标：把 `seeyon-v8-spi` 从“清楚可用的 skill”推进到“能跑闭环的工程型 skill”。本文件只定义 workflow，不堆接口资料，不替代 `references/auth-sso/`、`references/mq/`、`references/contract-index/`。

## 0. 适用范围

当用户明确提出以下诉求时，进入本 workflow：

- 生成 Super SPI 工程。
- 基于 SSO / MQ / 某个 SPI 子域写代码。
- 根据 jar / OpenAPI / MCP / HTTP / 语雀文档生成 SPI 实现。
- 对已有 SPI 工程补模块、改模块、做验证。

不适用：

- 只是问概念、查资料、整理文档：只读/更新 reference，不生成工程。
- 只是新增事实库资料：走 `references/facts/`，不进入生成。
- 只是定义 skill 架构：走 `references/architecture-control-protocol.md`。

## 1. 输入格式

### 1.1 最小输入

```yaml
task_type: generate | modify | validate | investigate
domain: sso | mq | openapi | custom
scenario: <用户业务场景，如 统一认证 / 三方免登 / RocketMQ ONS>
target_project: <新工程输出路径或已有工程路径>
seeyon_version: <V8 版本，可空>
constraints:
  - <现场限制，如不能加数据库、只能 Maven 依赖、必须兼容某 jar>
contract_sources:
  - type: source | jar | openapi | mcp | http | yuque | local-jar-index | none
    locator: <路径/URL/配置名/说明>
delivery:
  generate_code: true | false
  package_zip: true | false
  run_maven: auto | true | false
```

### 1.2 用户自然语言输入时的归一化

用户可能不会给 YAML。Agent 必须先把自然语言归一化成上述字段，并在输出中显式列出假设。

缺失字段处理：

- `task_type` 不明确：按“资料沉淀/调查”处理，不写工程。
- `domain` 不明确：从触发词路由；仍不明确则停下来问。
- `target_project` 缺失且要生成代码：停下来问输出目录。
- `contract_sources` 缺失：先跑 Contract Index 状态；若无法取得 FACT，进入降级规则。

## 2. 路由规则

### 2.1 主路由

| 用户意图 / 触发词 | 路由 | 首读文档 |
|---|---|---|
| 统一认证、登录页接认证中心、V8 用第三方认证登录 | SSO unified-auth | `references/auth-sso/index.md`、`references/auth-sso/unified-auth/README.md` |
| 三方免登 V8、外部系统跳 V8、从门户进 V8 | SSO avoid-login | `references/auth-sso/index.md`、`references/auth-sso/avoid-login/README.md` |
| V8 到三方单点、V8 菜单跳 ERP/第三方 | SSO sso-connector | `references/auth-sso/index.md`、`references/auth-sso/sso-connector/README.md` |
| MQ、RocketMQ、ONS、消息中间件扩展 | MQ | `references/mq/index.md` |
| 系统变量扩展、系统变量 SPI、`SystemVariableSPIService`、`@SPISystemVariable`、计算条件弹框添加系统变量 | System Variable | `references/system-variable/index.md`、`references/system-variable/shared/README.md` |
| OpenAPI、Swagger、接口契约、DTO、method signature | Contract Index | `references/contract-index/overview.md`、`references/contract-index/source-types.md` |
| Super SPI、多模块、工程结构、打包部署 | Super SPI | `references/spi-domain-constraints.md`（附录：官方 SPI 开发与部署规范、Super SPI 统一工程结构） |
| 生成后检查、验收、静态结构验证 | Validation | 本文档 + `references/generation/tools/validate_generated_spi_project.py` |

### 2.2 生成边界

只有用户明确要求以下动作，才写工程：

- “生成工程 / 写代码 / 改这个项目 / 补模块 / 打包 / 验证这个工程”。

否则只做：

- 路由判断。
- Contract Source 查询。
- reference 沉淀。
- 风险和缺口报告。

## 3. Contract Source 查询顺序

所有涉及接口、DTO、method signature、配置键、SPI 注册类名的判断，必须走 Contract Source。

顺序：

1. 用户提供的源码 / jar / 反编译结果。
2. 外部 Swagger / OpenAPI exact match。
3. MCP capability adapter。
4. HTTP capability adapter。
5. 本地语雀 rendered-md：`references/facts/yuque-v8-docs-rendered-md/`。
6. 本地 jar 轻量索引：`references/contract-index/jar-inventory-2026-06.md` 与 `references/contract-index/`。
7. 版本矩阵 / 历史经验。
8. AI 推断。

执行要求：

1. 先运行：
   ```bash
   python references/contract-index/tools/contract_index_status.py
   ```
2. `READY`：先查 external/local contract index。
3. `CONFIG_NEEDED`：输出 A/B/C 分支，不直接猜。
4. 用户提供 jar 但 index 未命中：优先 targeted probe，不默认整包反编译。
5. 语雀 rendered-md 命中最多是 OBSERVATION，不能单独升级为 FACT。

## 4. 证据不足时如何降级

### 4.1 Evidence 定义

| Evidence | 可用于什么 | 不能用于什么 |
|---|---|---|
| FACT | 关键接口签名、DTO 字段、注册类名、依赖坐标、生成代码 | 仍需标 locator，不可无来源引用 |
| OBSERVATION | 方向判断、文档说明、候选实现路径、待验证设计 | 不能单独锁死 method signature / DTO |
| HYPOTHESIS | 提醒用户可能方案、生成草稿/伪代码 | 不能当最终可部署代码依据 |

### 4.2 降级动作

1. FACT 不足，OBSERVATION 充分：
   - 可以生成带 TODO / guard 的草稿。
   - 报告中必须标“不可直接部署”。
   - 下一步必须列出获取 FACT 的最小动作。

2. 只有 HYPOTHESIS：
   - 不生成最终工程。
   - 只输出设计假设、缺口、需要用户提供的 jar/source/OpenAPI。

3. 用户明确要求“先按假设生成”：
   - 可以继续，但每个假设点必须写入 `VALIDATION.md` / 交付报告。
   - 关键接口处必须做隔离，避免伪 FACT 扩散。

## 5. 生成 Super SPI 的步骤

### 5.1 生成前

1. 归一化输入。
2. 路由到子域 reference。
3. 跑 Contract Index 状态检查。
4. 双查契约与公共方法：先读目标子域 `README.md` / `constraints.md` / `shared/*contract*` 锁定 SPI 接口、DTO、枚举、scope、spring.factories；同时读取 `references/platform-standard-library/index.md` 和 `references/platform-standard-library/decompiled/`，检查 boot 平台标准库 allowlist。能复用 `boot-core` / `boot-starter-web` / `boot-starter-spi` 中已 FACT 的 JSON/HTTP/Crypto/Request/Config/DTO-copy/Transport Response/Request 能力时，不在 `spi-common` 重造 helper。`ctp-user-api` / `cip-connector-api` 只作为子域契约包进入对应 `spi-{domain}` 模块，不能提升为全局公共方法。
5. 平台公共能力版本判定：
   - 能取得现场 boot jar：用现场 jar targeted probe，标 `FACT(site-jar:<version>)`。
   - 取不到现场 boot jar：按 `references/platform-standard-library/decompiled/` 初始化，标 `BASELINE(boot:5.3.358)`；后续拿到现场 jar 再补差异。
   - 注意：baseline 只兜底 boot 公共能力，不兜底子域 SPI 契约包接口/DTO。
6. 收集 Contract Source 与 Evidence。
7. 决定模块：
   - SSO → `spi-sso`
   - MQ → `spi-mq`
   - 系统变量扩展 → `spi-system-variable`
   - 公共能力 → `spi-common`
   - 新域 → `spi-{domain}`，必须先在 `SKILL.md` 路由表和 `references/index.md` 注册子域
7. 明确输出目录。

### 5.2 工程结构

必须符合 `references/spi-domain-constraints.md` 中“附录 D：Super SPI 统一工程结构”：

```text
custom-backend/
├── pom.xml
├── third-jar/
├── spi-common/
│   └── pom.xml
├── spi-sso/ or spi-mq/ or spi-system-variable/ or spi-{domain}/
│   ├── pom.xml
│   └── src/main/
│       ├── java/
│       └── resources/
│           ├── META-INF/spring.factories
│           └── metadata/spi_info.json
└── VALIDATION.md
```

禁止：

- `lib/`。
- 默认 `systemPath`。
- `spi-common` 注册 SPI。
- 默认使用 Spring 注解：`@Autowired`、`@Service`、`@Component`。
- 无证据使用 Hutool / 内部 service / dao / mapper。

### 5.3 生成中

1. 父 POM 注册所有模块。
2. 每个子模块 POM XML well-formed。
3. `spi-common` 只放公共工具，不放 `spring.factories` / `spi_info.json`。
4. 业务 SPI 模块写 `META-INF/spring.factories`。
5. 业务 SPI 模块写 `metadata/spi_info.json`。
6. 关键接口实现必须可追溯到 FACT 或显式降级。
7. 每个降级点写入交付报告。

## 6. 生成后验证清单

最小验证必须执行：

```bash
python references/generation/tools/validate_generated_spi_project.py <project-root>
```

检查项：

1. 项目根目录存在。
2. 根 `pom.xml` 存在且 XML well-formed。
3. 根 POM modules 与实际模块目录一致。
4. 不存在 `lib/`。
5. 不存在默认 `systemPath`。
6. `spi-common` 不包含 `spring.factories` / `metadata/spi_info.json`。
7. 业务 SPI 模块包含 `spring.factories`。
8. 业务 SPI 模块包含 `metadata/spi_info.json` 且 JSON well-formed。
9. Java 源码不包含禁止 Spring 注解。
10. MQ 模块额外检查：`MQMessageSpi`、`send`、`sendBatch`、`subscribeTopic`、`unSubscribeTopic`、`MQSerializer`、`MessageListenerService.invoke`。
11. SSO 模块额外检查：至少命中 unifiedauth / avoidlogin / connector 中一个场景包或实现类，并带 SPI 注册。
12. Auth-SSO 域包额外检查：如果交付物声称覆盖完整 `auth-sso/` 域，按 `references/auth-sso/index.md` 核验子场景顺序、生成/文档边界、`spring.factories` 注册和 `spi_info.json` scopes。
13. 本机存在 Maven 且用户明确要求编译验证时，可尝试 `mvn validate -DskipTests` / `mvn compile -DskipTests`；Maven 可执行文件、settings.xml、本地仓库、私服地址都视为用户现场输入，不写死到 skill、模板或默认样例。Maven 缺失或私服依赖不可达只记为环境状态，不覆盖静态结构结论。

## 6.1 可选 Maven 编译验证边界

Maven 编译不是 skill 的核心产物，只是用户现场允许时的增强验证。

执行原则：

1. 不把用户本地 Maven 路径、本地仓库路径、私服 id、一次性依赖版本写入全局样例或默认模板。
2. 需要编译时，先向用户索取或从目标工程配置中发现：
   - Maven 可执行文件。
   - settings.xml。
   - localRepository。
   - 私服 repository id / URL。
   - 是否允许联网或只走离线仓库。
3. 编译失败要区分：
   - SPI 工程结构失败。
   - Java 代码/接口签名失败。
   - Maven 环境/私服依赖解析失败。
4. 私有依赖解析经验只能沉淀为“通用处理模式”，不能沉淀为用户本地环境实例。

详细规则见 `references/generation/maven-verification-notes.md`。
## 6.2 最终收敛 / Closeout 清理

用户认为代码基本闭环、要求“最后收敛和清理”时，不再扩 scope，不新增业务能力，只做交付面闭环与反模式清扫：

1. 修正交付文档中的真实目标路径，避免遗留旧 demo / 临时目录。
2. 补齐或更新根 `README.md`：业务流程、关键文件、Nacos 最小配置、部署/重启、验证状态、未声明通过的边界。
3. 更新 `VALIDATION.md`：静态 validator 结果、WARN/SKIP 解释、Maven 编译/测试是否真实执行；不能把 `mvn not found` 或私服依赖缺失冒充为编译通过。
4. 再跑一次静态验证：
   ```bash
   python references/generation/tools/validate_generated_spi_project.py <project-root>
   ```
5. 扫描反模式并在最终回复中只报结论：
   - `@Autowired` / `@Service` / `@Component` / `@RestController`
   - `systemPath` / `lib/`
   - 无 FACT 的 Hutool / fastjson / 新依赖
   - `TODO` / 错拼字段 / 旧路径残留
6. 配置读取边界复核：全局 boot 配置优先用 `Apps.getEnvironment().getProperty(...)` 或 `EnvironmentHolder.get().getProperty(...)`；子域 helper（如 `CtpUserSpiUtils`）只用于该子域 FACT 能力，不要扩大成全局配置读取工具。
7. 只做可验证的小修；若发现需要改变 domain、接口、部署模式、依赖坐标，列为风险或现场待确认，不在 closeout 阶段硬改。

Closeout 最终回复格式要短：项目路径、清理项、验证结果、WARN 解释、现场下一步。不要重新长篇解释整个 SPI 原理。

## 7. 交付报告模板

## 1. Route
- Domain:
- Scenario:
- Workflow:
- Target Project:

## 2. Inputs Normalized
- task_type:
- seeyon_version:
- constraints:
- assumptions:

## 3. Contract Sources
| Item | Source Type | Evidence | Locator | Result |
|---|---|---|---|---|

## 4. Generation Summary
- Created/Modified modules:
- Public capabilities in spi-common:
- SPI modules:
- Files changed:

## 5. Validation
| Check | Result | Detail |
|---|---|---|

## 6. Downgrade / Risk
- FACT gaps:
- OBSERVATION-only decisions:
- HYPOTHESIS points:

## 7. Next Action
- User action needed:
- Suggested command:
```

## 8. 必须停下来问用户的情况

以下情况不要硬猜：

1. 用户要求生成代码，但没有目标输出目录。
2. `domain` 无法从输入判断，且不同 domain 会生成不同模块。
3. Contract Index `CONFIG_NEEDED`，且用户没有提供 jar/source/OpenAPI，也没有允许降级。
4. 关键接口只有 HYPOTHESIS，但用户要求“可部署最终代码”。
5. 需要访问外部私有系统、下载依赖、提交代码、发消息、公开内容。
6. 需要删除/覆盖已有工程文件，且用户未明确确认。
7. 发现已有工程结构与 Super SPI 边界冲突，例如根本不是 Maven 多模块或已有 `lib/`/`systemPath` 大量依赖。
8. 子域未注册，例如新 SPI 域没有 reference/index，也没有生成边界。

## 9. M1 完成定义

M1 不要求生成器自动写完整业务代码。M1 的完成标准是：

1. 有本 workflow 文档。
2. 有可运行 validator。
3. 主入口 `SKILL.md` 能路由到 workflow 和 validator。
4. 任一生成工程都能用统一报告格式交付。
5. 证据不足时不会悄悄伪装成 FACT。
