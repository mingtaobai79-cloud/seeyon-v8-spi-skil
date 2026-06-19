---
name: seeyon-v8-spi
description: "Seeyon V8 SPI/Super SPI 统一入口。入口只负责路由、证据规则、工程边界；子域知识下沉到 references/<domain>/ 独立目录，每个域按 SPI 类型拆分为独立文件夹。"
version: 8.1.3-pass-with-frozen-boundary
owners: [白明涛]
metadata:
  hermes:
    tags: [seeyon, v8, sso, spi, java, code-generation, generator, deployment]
    related_skills: []
---

# Seeyon V8 SPI / Super SPI 统一入口

本文件只做三件事：路由、证据规则、工程边界。

具体接口、DTO、代码骨架、审计流程、冻结状态、坑位，不放入口；按下面路径下沉读取。语雀全量文档不内置，只保留 SPI 子集；非 SPI / 指定 URL 走 `references/facts/yuque-v8-docs-rendered-md/tools/yuque_fetch.py` 在线查 `https://www.yuque.com/seeyonkk/v8`。

## 0. Runtime Requirements

本 skill 的默认任务以文档路由、证据归档、契约发现和工程生成校验为主；不要把当前机器环境误写成客户部署要求。

- Python：推荐 Python >= 3.11。核心脚本主要使用标准库；`references/contract-index/tools/contract_index_status.py` 需要 `PyYAML`；`references/facts/yuque-v8-docs-rendered-md/tools/yuque_fetch.py` 使用标准库；旧 rendered-md CDP 复制工具若重抓才需要 `websocket-client`。
- Java/JDK：只有 jar 契约发现、`javap`、CFR 反编译、生成工程编译验证时需要可用 `java` / `jar` / `javap`。当前运行 JDK 版本不等于客户现场部署版本；生成工程的 source/target 按现场 V8 要求或用户参数确定。
- CFR：走 `references/contract-index/cfr-decompile-workflow.md` 时才需要 CFR jar 路径；不要默认假设已存在。
- Maven：不是 skill 默认交付要求。只有用户明确要求 Maven validate/compile 时，先按 `references/generation/maven-verification-notes.md` 收集 Maven executable、settings.xml、localRepository、私服与版本信息，再执行。
- OS/路径：skill 文档保持跨平台；本机 Windows/Git Bash 事实只能作为当次执行环境，不固化为通用样例。

## 0. 必读顺序

任何 Seeyon V8 SPI 任务，按顺序读：

1. `references/architecture-control-protocol.md` — 证据、架构、知识治理总协议
2. `references/spi-domain-constraints.md` — 所有域公共约束
3. `references/<domain>/index.md` — 进入对应域
4. `references/<domain>/<spi>/README.md` — 接口契约、DTO、代码骨架
5. `references/<domain>/<spi>/constraints.md` — 独有约束、禁止项、缺口
6. 生成/修改工程时：`references/workflows/spi-generation-workflow.md`
7. 生成后验证：`references/generation/tools/validate_generated_spi_project.py`
8. Maven 编译闭环和私有仓库排障：`references/generation/maven-verification-notes.md`

如果任务涉及 jar、源码、反编译、接口契约，先进入 Contract Index：

- `references/contract-index/overview.md`
- `references/contract-index/contract-discovery.md`
- `references/contract-index/cfr-decompile-workflow.md`

## 1. 最高优先级规则

### Rule-000: Contract First

用户提供 jar、源码、反编译接口、示例工程时，优先从真实 artifact 提取 Contract。

禁止靠经验猜接口、DTO、方法签名、注解、scope。

触发后读取：

- `references/contract-index/overview.md`
- `references/contract-index/contract-discovery.md`
- `references/contract-index/contract-bundle.md`
- `references/contract-index/contract-normalization.md`
- `references/contract-index/source-types.md`

### Rule-001: Evidence First

关键判断必须标明 Evidence。

Contract Source 优先级：

1. 用户提供源码 / jar / 反编译结果
2. 外部 Swagger / OpenAPI exact match
3. MCP capability adapter
4. HTTP capability adapter
5. 语雀 V8：本地 SPI 子集 rendered-md `references/facts/yuque-v8-docs-rendered-md/`；全量/指定 URL 用 `references/facts/yuque-v8-docs-rendered-md/tools/yuque_fetch.py` 查 `https://www.yuque.com/seeyonkk/v8`
6. 本地 jar 轻量索引：`references/contract-index/jar-inventory-2026-06.md`
7. 版本矩阵 / 历史经验
8. AI 推断

证据等级：

| 等级 | 标记 | 定义 |
|------|------|------|
| FACT | ✅ | 源码 / jar / 反编译 / 官方 OpenAPI exact match |
| OBSERVATION | ⚠️ | 语雀文档、历史样例、项目观察 |
| HYPOTHESIS | ❓ | 版本矩阵、经验推断、AI 推断；必须提示待验证 |

### Rule-002: Closed-world Code Generation

生成代码只能使用白名单依赖。

禁止默认使用：

- 数据库直连
- Redis
- 内部 service/dao/mapper
- 未证实的 `@Autowired`
- 未证实的 Hutool / Guava / Fastjson / Jackson API
- 未证实的 V8 内部类

### Rule-003: Super SPI Only

默认工程形态只有一种：Super SPI Maven 多模块。

公共能力进 `spi-common`；具体 SPI 进对应 `spi-{domain}` module。

禁止：

- `lib/`
- `systemPath`
- `spi-common` 注册 `spring.factories`
- `spi-common` 放 `spi_info.json`
- 未经用户要求创建孤立单模块工程

### Rule-004: Frozen Means Stop

冻结 = 停止推进，不修改冻结域，不“顺手修”。

冻结清单见：

- `references/status/frozen-artifacts.md`
- `references/index.md`

### Rule-005: 缺口口径

不要把现场业务参数误报为知识库缺口。

不算缺口：URL、ticket、客户标识、跳转协议、业务字段、运行时配置、示例业务 util。

只算缺口：会影响 FACT 化或编译正确性的 SPI 接口、DTO、jar、示例源码、表结构。

详细口径见：`references/spi-domain-constraints.md`。

### Rule-006: Status, Workflow, and Active-tree Hygiene

维护本 skill 时，workflow/status 文档不要保留旧静态口径或已下沉文件路径。

- `references/status/evidence-summary.md` 只做状态转发；当前状态以 `references/index.md` 为唯一来源。
- workflow 中引用 skill 内文档时，使用从 skill 根目录出发的 `references/...` 路径，不使用相对当前 workflow 文件夹的隐式路径。
- 已下沉的历史结构/部署文档不要继续按旧文件名引用；统一以 `references/spi-domain-constraints.md` 附录为准；系统变量注解/限制以 `references/system-variable/shared/README.md` 为准。
- 修改 workflow 后，复扫旧路径残留，避免外部 agent 按不存在路径执行。
- skill 根目录不得保留 full dump、old 入口或 root 级历史快照；确认已由 active 文档承接后，直接移出 active skill tree，不在上传版中保留。
- `references/` 顶层 `.md` hygiene 目标为 6 个以内；审计/closeout/pattern 类文档应下沉到 `references/audits/` 或 `references/workflows/`，不要长期留在顶层。

### Rule-008: Active Skill Tree Is Not Session Storage

`seeyon-v8-spi` 的 active tree 只保留可复用的入口、规范、事实索引、工具和生成/验证流程；不要把一次性过程材料当知识库资产长期挂在 active 路由上。

清理口径：

- 不保留 root/active 评测目录、一次性评测 JSON、临时压测结果；这类材料不进入 release 版。
- 发布/上传前必须额外扫描并清零：`备份`、`恢复`、`backups`、`trash`、`restore`、`rollback`、本机备份路径、会话过程说明。OpenAPI/Yuque 等资料只保留“证据边界/使用规则”，不记录本轮移动、恢复、备份位置。
- 不保留带日期的一次性审计报告作为 active 文档，例如 `*-audit-YYYY-MM-DD.md`、`operational-audit-*`、`skill-architecture-audit-*`、`non-frozen-domain-audit-*`。稳定规则沉淀到 class-level workflow / audit gate；会话报告移出 active tree。
- 不保留带日期的历史旧目录。若其中内容已由当前 domain/workflow 承接，整目录移出 active tree；若未承接，先抽取稳定规则再移出 active tree。
- 语雀事实库采用“两层索引”：`references/facts/yuque-v8-docs-rendered-md/docs/` 只留 SPI 子集；`manifest.json` / `outline.md` 只说明 local_file ↔ remote_url 与本地/远程查询规则；本地无命中或非 SPI 文档，走 `references/facts/yuque-v8-docs-rendered-md/tools/yuque_fetch.py` 查远程语雀。
- 旧的 Chrome CDP rendered copy 工具（如旧 CDP 单页抓取脚本、旧 CDP 批量抓取脚本）属于重抓过程工具；当前策略下不留 active tree。若未来确需重抓，放到临时工作区执行，稳定后再按维护入口引入。
- OpenAPI `.docx` 是 contract/external evidence 输入，必须保留在 `references/openapi-docs/`；不要和语雀瘦身一起误删。

收口后必须复验：

1. 旧散目录、带日期 audit、legacy history、旧 CDP 抓取工具在 active tree 中不存在。
2. `yuque_fetch.py` 位于 `references/facts/yuque-v8-docs-rendered-md/tools/`，且 SKILL/config/workflow/query 脚本无旧路径引用。
3. `outline.md` / `manifest.json` 表达本地 SPI 子集 + 远程语雀，而不是全量抓取流水账。
4. `config/external-indexes.yaml` 是 runtime source of truth；`config/external-indexes.template.yaml` 只用于 bootstrap/reset。改 runtime 能力（如 `local_doc_index` / Yuque adapter）后，必须同步 template 并用 YAML 语义 equality 验证，不能只看文本 diff。
5. py_compile、Markdown 断链、Contract Index status、本地语雀查询、OpenAPI 文件数、发布包内容全部复验。
6. 注意 py_compile / unittest 会重新生成 `__pycache__`；所有验证跑完后必须二次移出 active tree，并最终断言 `__pycache__` / 历史目录 / `dist` 为 0。

## 2. 路由表

先识别用户场景，再进入对应域。

| 用户场景 | 入口 |
|----------|------|
| 总览、状态、冻结、缺口 | `references/index.md` |
| 统一认证、免登、SSO、登录扩展、三方 App 登录 | `references/auth-sso/index.md` |
| 帆软 / FineReport / 决策平台单点（V8→帆软） | `references/auth-sso/index.md` → `references/auth-sso/sso-connector/README.md`；外部接口观察见 `references/auth-sso/fanruan-finereport-sso.md` |
| MQ、RocketMQ、阿里云 ONS | `references/mq/index.md` |
| 三方待办、接口鉴权、组织同步中间表 | `references/integration-sync/index.md` |
| 系统变量扩展 | `references/system-variable/index.md` |
| 通讯录脱敏、登录人数、密码策略 | `references/account-org-security/index.md` |
| 能力通道 ProviderService | `references/capability-channel/index.md` |
| 加密/摘要/对称加密 | `references/crypto/index.md` |
| 数据源扩展 | `references/datasource/index.md` |
| 三方菜单、移动插件 | `references/entry-menu-mobile/index.md` |
| 文件存储、上传下载拦截 | `references/file-storage/index.md` |
| 注册中心、配置中心 | `references/infra-config-registry/index.md` |
| BPM、流程、公文 | `references/workflow-document/index.md` |
| jar、反编译、契约发现 | `references/contract-index/overview.md` |
| 全 SPI / 能力项 Super SPI 大工程生成 | `references/workflows/spi-generation-workflow.md`（覆盖多域/能力项生成流程；冻结项只生成 audit skeleton；validator PASS 不等于 Maven compile） |
| 生成 Super SPI 工程 | `references/workflows/spi-generation-workflow.md` |
| 生成工程 Maven 验证 / 私有依赖判定 | `references/generation/maven-verification-notes.md` |
| 审计 Evidence / 非冻结域 | `references/workflows/evidence-audit-workflow.md` / `references/workflows/non-frozen-audit-workflow.md` |
| 复审审计报告 / PASS-PARTIAL-FAIL gate | `references/audits/audit-report-review-gates.md`（区分只读准备度审计 vs 生成交付审计；READY 分层、污染分类、断链可复验、validator 口径） |
| MQ-only Super SPI 生成物审计 | `references/audits/generated-mq-super-spi-audit-notes.md`（先验目录存在，再查注册边界/FACT 契约/污染/validator） |
| 知识库瘦身 / hygiene | `references/workflows/knowledge-hygiene-workflow.md` |
| OpenAPI / 语雀打包瘦身回归门 | `references/workflows/openapi-yuque-packaging-hygiene.md` |
| Skill 架构收口审计 / closeout gate | `references/audits/architecture-closeout-gate.md` |
| Skill 可用态收敛 / closeout | `references/workflows/skill-closeout-checklist.md` |
| Closeout hygiene 小收敛 patch | `references/workflows/closeout-hygiene-patch-pattern.md` |

## 3. 域目录标准

每个域固定结构：

```text
references/<domain>/
├── index.md                    # 纯导航；不放实现细节
├── shared/                     # 跨 SPI 共享资源
├── <spi-name>/
│   ├── README.md               # 场景、接口、DTO、代码骨架、Nacos、spring.factories
│   └── constraints.md          # 独有约束、禁止项、索取清单
└── ...
```

`index.md` 只做路由：SPI 文件夹索引、scope、重启服务、Evidence 状态。

实现细节必须进 SPI 文件夹或 shared。

## 4. 默认执行流程

1. 识别场景，确定 domain/spi。
2. 读 `references/architecture-control-protocol.md` 和公共约束。
3. 读 domain `index.md`。
4. 读目标 SPI 的 `README.md` + `constraints.md`。
5. 判断 Evidence 是否足够；不足则走 Contract Index 或标明缺口。
6. 若用户给 jar/源码/示例工程，先抽取事实，再更新对应 reference。
7. 若生成代码，进入 `spi-generation-workflow.md`。
8. 生成后运行 validator。
9. 若用户明确要求 Java 工程编译验证，按 `references/generation/maven-verification-notes.md` 收集 Maven executable / settings.xml / localRepository / 私服信息后再跑 Maven validate / compile；不要把 Maven 编译作为 skill 默认交付，也不要把用户本地仓库配置固化为通用样例。
10. 报告必须区分：已 FACT、仍缺口、冻结项、假设项。
11. 如果发现入口/文档膨胀，按 hygiene workflow 下沉，不继续往入口塞。

## 5. 生成红线

- 不许 AI 推断接口签名。
- 不许跳过 Contract Source。
- 不许修改冻结域。
- 不许把现场参数当知识库缺口。
- 不许在 `index.md` 塞实现细节。
- 不许生成后不验证。
- 不许把示例业务 util 沉淀成通用 SPI 约束。
- 不许默认套 Hutool `StrUtil`。
- 不许把 SM3 当可解密算法；SM3 是摘要。
- 不许让 `spi-common` 注册 SPI。
- 生成代码中的禁止注解检查是 token 级静态扫描：JavaDoc/注释里也不要直接写 `@Autowired` / `@Service` / `@Component`，否则 validator 会判 FAIL。交付文档需要说明禁止项时，用“Spring stereotype/injection annotations”或放到非 Java 文档，并明确这只是文档描述。
- 用户要求“如果 validator 不支持某域特定检查，必须列手工检查项”时，即使 validator 已支持该域，也要在 `VALIDATION.md` 追加一张手工约束检查表，逐条覆盖用户显式要求（配置参数化、兼容观察、scope、注册文件、FACT 契约、禁止注解、序列化/消费链路等），避免把静态 PASS 冒充为业务全验。

## 6. Capability Channel governance

能力通道按 28 项具体能力拆分，不保留 `provider-service/` 这种长期总账目录，也不为每个 jar 版本沉淀全量反编译索引。这个规则是用户明确纠正后的金标准：SSO 没有版本总账目录，能力通道也不要开这个口子；否则所有 SPI 域都会膨胀成版本仓库。

执行口径：

1. 入口只读 `references/capability-channel/index.md`，再路由到具体能力文件夹（如 `sms/`、`email/`、`doc-online/`、`pay/`）。
2. 每个能力文件夹至少包含 `README.md`（场景、接口、方法表、Maven、spring.factories、spi_info、重启服务、代码骨架、Evidence 摘要）和 `constraints.md`（独有约束、生成器规则、索取清单、禁止项）。
3. 若用户提供实际 jar/source 或指定目标版本，先走 Contract First，从该 artifact 抽取接口 FQCN、方法签名、DTO、枚举、required/default，再只更新受影响的能力文件夹。
4. 临时反编译产物属于过程材料，不进入 active skill；稳定结论才回填到对应能力文档。
5. 禁止新增 `provider-service/`、`contract-facts-<version>.md`、`*-facts-<version>.md` 这类长期版本总账；如确需保留过程材料，放到临时目录或会话产物，不挂 active skill 路由。
6. 若用户口头说 `cip-provider-api`，但给出 `cip-capability-api-*.jar`，先读取 `META-INF/MANIFEST.MF` 和 `META-INF/maven/**/pom.properties|pom.xml` 确认真实 Maven 坐标，禁止按历史名猜。
7. 用户要求“28 个能力每个都生成、放在一个大的项目里面”时，默认生成一个 Super SPI 大工程 + 一个业务模块 `spi-capability-channel`，在该模块内放 28 个 `Custom*ProviderService` 实现，并用同一个 `META-INF/spring.factories` 注册 28 条接口映射；不要膨胀成 28 个 Maven 子模块，除非用户明确要求按能力拆模块。
8. Capability Channel 的 `spi_info.json` scope 应为 `cip-capability`。通用 validator 可能对非 `ALL` scope 给 WARN；这是能力通道域的正确 scope 提示，不要为了消 WARN 改成 `ALL`。交付报告中说明该 WARN 是域特定可接受项。
9. 没有现场 `cip-capability-api` jar / CapabilityEnum 反编译 FACT 时，`getCapabilityEnum()` 不要猜枚举值；保留 TODO/隔离点并在 `VALIDATION.md` 标为需现场补齐。供应商 SDK/HTTP API 未提供时，required 方法可以作为结构模板占位返回，但必须标明“不可直接生产调用”。

## 6. 常用工作流入口

| 工作流 | 路径 |
|--------|------|
| SPI 工程生成闭环 | `references/workflows/spi-generation-workflow.md` |
| Evidence 升级 | `references/workflows/evidence-upgrade-workflow.md` |
| Evidence 批量审计 | `references/workflows/evidence-audit-workflow.md` |
| 非冻结域审计 | `references/workflows/non-frozen-audit-workflow.md` |
| 知识库 hygiene | `references/workflows/knowledge-hygiene-workflow.md` |
| 案例污染 / 示例值污染清理 | `references/workflows/case-pollution-cleanup-checklist.md` |
| 入口瘦身 / workflow 去重 / 状态转发治理 | `references/workflows/entry-router-slimming-workflow.md` |
| Skill 架构收口审计 / closeout gate | `references/audits/architecture-closeout-gate.md` |
| Skill 可用态收敛 / closeout | `references/workflows/skill-closeout-checklist.md` |
| Closeout hygiene 小收敛 patch | `references/workflows/closeout-hygiene-patch-pattern.md` |
| 域升级到金标准 | `references/workflows/domain-upgrade-workflow.md` |
| CFR 反编译 / Jar 发现 | `references/contract-index/cfr-decompile-workflow.md` |
| 常见坑长列表 | `references/pitfalls/common-pitfalls.md` |
| 冻结 artifact 状态 | `references/status/frozen-artifacts.md` |
| Evidence 总览 | `references/status/evidence-summary.md` |

## 7. 核心文档

- `references/index.md` — 全域索引、状态、冻结清单
- `references/architecture-control-protocol.md` — 架构治理与 Evidence 协议
- `references/spi-domain-constraints.md` — 全局 SPI 约束
- `references/platform-standard-library/index.md` — 平台标准库 FACT 索引；生成前优先复用 boot 通用基础能力，避免重复造轮子；子域 API 只按 contract 引入
- `references/agent-portability.md` — 外部 Agent 适配
- `references/contract-index/` — 契约发现/反编译/归一化
- `references/facts/yuque-v8-docs-rendered-md/` — 语雀 SPI 子集 rendered-md 事实库（85 篇）；全量/指定 URL 用 `references/facts/yuque-v8-docs-rendered-md/tools/yuque_fetch.py`
- `references/generation/tools/validate_generated_spi_project.py` — 生成后验证器

## 8. 当前状态

状态不写死在入口。查看：

- `references/index.md` — 全域索引、FACT/冻结状态、缺口口径
- `references/status/frozen-artifacts.md` — 冻结 artifact 清单
- `references/status/evidence-summary.md` — 状态转发入口

## 9. Closeout 标记

**状态：✅ 可用态 / PASS-with-frozen-boundary closeout（2026-06-20）**

当前 skill 已完成 Super SPI 统一入口、子域路由、证据规则、生成边界、静态验证闭环和 root hygiene 收敛；冻结 SPI 保持 OBSERVATION/待 jar，不纳入 FACT 完成口径。后续维护原则：

1. 新现场 jar / 源码 / 反编译结果进入时，只升级对应子域 FACT 与 Contract Index，不回填大段实现到入口。
2. 新 SPI 域进入时，按 `references/<domain>/` 标准结构新增，并注册到 `references/index.md` 与入口路由表。
3. 冻结域默认不动；除非用户明确要求解冻或补 FACT。
4. 生成工程仍必须运行 `references/generation/tools/validate_generated_spi_project.py`，不能因 closeout 跳过验证。
