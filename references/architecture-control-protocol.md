# Skill 架构治理

> 本文件合并了原 architecture-control-protocol.md、knowledge-organization.md、skill-architecture-health-check.md。

---

# Seeyon V8 SPI Skill 架构控制协议

> 目标：把 `seeyon-v8-spi` 控制成“可路由、可取证、可生成、可验证”的 skill，而不是不断堆资料的知识垃圾桶。

## 0. 总原则

`seeyon-v8-spi` 的核心价值不是“让 AI 知道很多”，而是：

1. 让 AI 知道该去哪里查。
2. 让 AI 知道什么能当事实。
3. 让 AI 不瞎编 Seeyon/V8 接口。
4. 让 AI 只在明确进入生成阶段时才写工程代码。
5. 让 AI 生成后必须验证。

入口只路由，不承载所有知识；事实只索引，不直接膨胀入口；模板只在可复制生成时存在。

## 1. 四层架构

### 第 1 层：Routing / 主入口

文件：`SKILL.md`

只干 5 件事：

1. 识别需求类型。
2. 路由到子域或模块。
3. 规定 Contract Source / Evidence 优先级。
4. 规定 Super SPI 生成边界。
5. 规定验证清单。

禁止放入：

- 大段接口正文。
- 大段 Java 代码。
- 某个子域的细节教程。
- 一次性排障记录。
- 未稳定的现场猜测。

### 第 2 层：Knowledge / 子域知识

目录：`references/`

职责：放人工沉淀后的领域知识。

推荐结构：

```text
references/auth-sso/
references/mq/
references/contract-index/
references/deployment/        # 未来部署公共化时再建
references/openapi-docs/      # OpenAPI 原始资料/文档集合
references/facts/             # 事实库/原始资料区
```

规则：

1. 子域知识必须先有入口：`references/<domain>/index.md` 或 `overview.md`。
2. 子域 reference 只写稳定结论、边界、触发词、验证规则。
3. 子域找不到信息时，先查 facts / Contract Source，不凭记忆补。
4. 查到的稳定结论可以回填 reference；原始长文不回填。

### 第 3 层：Tools / 工具层

目录：优先放在所属模块下，例如：

```text
references/contract-index/tools/
```

职责：给 AI 调用，不是给入口阅读。

当前工具：

- `references/contract-index/tools/contract_index_status.py`：Contract Index readiness 检查。
- `references/contract-index/tools/query_yuque_local_index.py`：查询本地语雀 rendered-md 事实库。
- `references/contract-index/tools/decompile_jar.py`：jar 轻量索引、查询、targeted probe、必要时反编译。
- `references/contract-index/tools/cfr.jar`：反编译依赖。
- `references/generation/tools/validate_generated_spi_project.py`：Super SPI 生成后静态结构验证。

规则：

1. 根目录不放 active `scripts/`。
2. 工具跟随模块走，避免全局脚本垃圾桶。
3. 工具测试放同模块 `tests/`。
4. 工具输出必须能给出 locator / source / evidence。

### 第 4 层：Templates / 生成器与模板层

目录：仅在真的有“可复制出去并修改”的生成模板时创建，例如：

```text
templates/super-spi/
templates/spi-sso/
templates/spi-mq/
templates/health-check/
templates/agent-prompts/
```

当前规则：

1. 不为了“看起来完整”创建空 templates。
2. 不把知识文档伪装成 templates。
3. 只有当模板可直接参与生成工程/报告/agent prompt 时才落盘。
4. 模板必须配验证方式，否则宁可继续放 reference。

## 2. Contract Source 统一抽象

Contract Source = AI 获取事实依据的来源。

所有接口、DTO、method signature、OpenAPI、MCP/HTTP、jar、语雀文档，都必须统一进入 Contract Source 体系，不各说各话。

优先级：

1. 用户提供的源码 / jar / 反编译结果。
2. 外部 Swagger / OpenAPI exact match。
3. MCP capability adapter。
4. HTTP capability adapter。
5. 本地语雀 rendered-md：`references/facts/yuque-v8-docs-rendered-md/`。
6. 本地 jar 轻量索引：`references/contract-index/jar-inventory-2026-06.md` 与 `references/contract-index/`。
7. 版本矩阵 / 历史经验。
8. AI 推断。

证据标签：

| Evidence | 来源 |
|---|---|
| FACT | 源码、jar、反编译结果、官方 OpenAPI/Swagger exact match、带明确 locator 的外部 contract exact match |
| OBSERVATION | 语雀 rendered-md、历史样例、项目观察、非 exact 的外部搜索摘要 |
| HYPOTHESIS | 版本矩阵、经验推断、AI 推断 |

硬规则：

1. 关键接口不能靠 HYPOTHESIS 直接生成最终代码。
2. OBSERVATION 可以指导方向，但涉及签名/DTO 时必须继续找 FACT。
3. FACT 也要输出 locator：文件路径、URL、SHA256、artifact version、class/method。
4. 找不到 FACT 时可以继续，但必须显式降级，并告诉用户风险。

## 3. 防垃圾桶规则

新增资料前先判断类型：

| 内容类型 | 放哪里 | 不放哪里 |
|---|---|---|
| 主路由/铁律/执行顺序 | `SKILL.md` | 子域长文、facts |
| 子域稳定知识 | `references/<domain>/` | `SKILL.md` |
| 原始文档/事实库 | `references/facts/` 或 `references/openapi-docs/` | `SKILL.md` |
| 可调用脚本 | 所属模块 `tools/` | 根 `scripts/` |
| 工具测试 | 所属模块 `tests/` | 根 `tests/` |
| 可复制生成模板 | `templates/` | reference/facts |
| 一次性过程记录 | 不进入 skill，必要时会话即可 | 任意 active 目录 |

新增任何目录必须满足：

1. 有入口说明。
2. 有触发条件。
3. 有证据边界。
4. 有验证方式。
5. 已在 `SKILL.md` 或对应上级 index 注册。

不满足就不要建。

## 4. 默认执行协议

1. 先读 `SKILL.md` 判断任务类型。
2. 进入对应 reference / module。
3. 如果涉及契约，先走 Contract Source，不靠记忆写接口。
4. 如果 reference 找不到，查 facts；facts 只给 OBSERVATION，不能自动升 FACT。
5. 用户明确要求生成/修改工程时，才进入 Super SPI 生成边界。
6. 生成后必须跑结构/静态/契约验证。
7. 输出时标明：路由、Contract Source、Evidence、生成/未生成、验证结果。

## 5. 稳定 stop point

当前稳定架构是：

```text
seeyon-v8-spi/
├── SKILL.md                         # Routing / 总入口，只做路由、证据规则、工程边界
├── config/
│   ├── external-indexes.yaml         # runtime Contract Source 配置，脚本读取它
│   └── external-indexes.template.yaml# bootstrap/reset 模板，不作为运行时事实源
├── references/                       # Knowledge + facts + tools modules
│   ├── index.md                      # 全域索引、状态、冻结清单
│   ├── architecture-control-protocol.md
│   ├── spi-domain-constraints.md
│   ├── workflows/
│   ├── audits/
│   ├── status/
│   ├── contract-index/
│   │   ├── overview.md
│   │   ├── tools/
│   │   └── tests/
│   ├── generation/
│   │   └── tools/
│   │       └── validate_generated_spi_project.py
│   ├── facts/
│   │   └── yuque-v8-docs-rendered-md/
│   │       ├── docs/                 # 本地 SPI 子集，不代表语雀全量
│   │       ├── manifest.json
│   │       ├── outline.md
│   │       └── tools/yuque_fetch.py   # 非本地/指定 URL 远程查询
│   ├── openapi-docs/
│   ├── auth-sso/
│   ├── mq/
│   ├── integration-sync/
│   ├── system-variable/
│   ├── account-org-security/
│   ├── capability-channel/
│   ├── crypto/
│   ├── datasource/
│   ├── entry-menu-mobile/
│   ├── file-storage/
│   ├── infra-config-registry/
│   └── workflow-document/
└── templates/                        # 仅在有真实生成模板时创建；不存在不算问题
```

这个 stop point 的含义：

- 入口不继续堆资料；新增知识必须下沉到对应 `references/<domain>/`、`references/workflows/`、`references/audits/` 或事实库。
- 可以继续补子域，但必须同步注册到 `SKILL.md` 路由表与 `references/index.md`。
- 可以继续补工具，但必须归属模块，且配 `tests/` / `py_compile` / 可复验命令。
- 可以继续补模板，但必须可生成、可验证；空模板目录不是目标。
- active tree 不保留历史目录、`dist/`、`__pycache__/`、带日期一次性审计、root full dump、旧 CDP 抓取工具。
- Contract Source 运行时配置以 `config/external-indexes.yaml` 为准；template 只用于 bootstrap/reset。

## 6. 知识结构治理规则

> 来源：会话纠偏。用户明确指出：这里治理的是 skill 知识库结构，不是生成项目的源码模板目录。

`seeyon-v8-spi` 是 Super SPI 的统一入口 skill。稳定四层：

1. `SKILL.md` = Routing / 主入口，只做需求识别、路由、证据优先级、生成边界、验证清单。
2. `references/` = Knowledge / 子域知识、事实库、工作流、审计 gate。
3. `references/<module>/tools/` = Tools / 可调用工具层，例如 Contract Index 工具。
4. `templates/` = Templates / 真实可复制、可生成、可验证的模板层。

硬边界：

- 顶层 `SKILL.md` 只做入口、路由、铁律、边界说明。
- 具体领域知识下沉到 `references/` 的子目录。
- SSO 是一个子域，所有 SSO 细节集中放在 `references/auth-sso/`。
- MQ 是一个子域，所有 MQ 细节集中放在 `references/mq/`。
- Contract Source / jar / OpenAPI / MCP / HTTP 统一进入 `references/contract-index/` 与 `config/external-indexes.yaml`。
- 不把统一认证、免登、单点登录、MQ、OpenAPI 或 jar 细节散落在顶层。
- 不继续把资料往主入口堆成知识垃圾桶。

## SSO 子域结构

```
references/auth-sso/
├── index.md
├── unified-auth/
├── avoid-login/
├── sso-connector/
├── inbound-sso/
├── outbound-sso/
├── auth-provider/
├── mobile-app/
├── qrcode-login/
├── ticket-custom-userinfo/
└── shared/
```

## 顶层 SKILL.md 职责

顶层只回答：

1. 当前请求属于哪个子域？
2. 应加载哪个 reference？
3. 有哪些全局铁律？
4. Contract Source / Evidence 优先级是什么？
5. Super SPI 的工程边界是什么？
6. 生成后如何验证？

顶层不应该长期堆积：

- 大段 Java 接口定义
- 完整代码骨架
- 某一模式的详细实现细节
- 单次会话产生的窄问题记录

这些应放入 `references/<domain>/<spi>/README.md`、`constraints.md` 或对应 `shared/`，不要放在入口。

## 不要误建 templates

只有“未来要复制出去并修改的真实 starter 文件”才放 `templates/`。

不要为了让用户“看见目录”而创建生成项目源码骨架，例如：

```
templates/super-spi/source/...
```

如果用户说“没看见文件/目录”，先确认他说的是 skill 知识目录还是生成项目模板。对于本 skill 的 SSO 导航诉求，正确动作是整理 `references/auth-sso/`，不是创建源码模板。

## 导航优先级

用户提到 SSO 相关时：

1. 先加载 `references/auth-sso/index.md`。
2. 再按场景加载：
   - 统一认证 → `references/auth-sso/unified-auth/README.md`
   - 三方免登 V8 → `references/auth-sso/avoid-login/README.md`
   - V8 到三方单点 → `references/auth-sso/sso-connector/README.md`
3. 涉及 OAuth2/CAS/SM2/SM4/RSA/AES/OIDC/SAML/JWT/LDAP 等，再加载 `references/auth-sso/shared/` 和目标 SPI 的 `constraints.md`。

## 维护规则

- references 根目录只放跨 SPI 公共语义/结构文档，例如：契约发现方法论、证据系统、Contract Bundle/Normalization、Super SPI 工程结构、OpenAPI 索引、架构控制协议。
- 某个 SPI 子域自己的约束、版本矩阵、Health Check、部署、依赖白名单、API Contract，必须放进该子域目录。SSO 的这些文件统一放 `references/auth-sso/`；MQ 的这些文件统一放 `references/mq/`。
- 不同 SPI 未来有不同约束，不要把某个子域的规则伪装成全局规则。
- 移动文件后必须全局更新旧路径引用。
- 删除误建/无用目录后，必须扫残留引用。

### 目录合并 / 清理规则

当用户要求检查 `indexes`、`subskills`、外部 Agent adapter、历史目录是否能合并/清理时，按下面顺序执行：

1. 先盘点目录树、体积、文件清单、主动引用和脚本入口；不要凭目录名直接删。
2. `references/facts/` 是事实库数据区，和 `references/openapi-docs/` 一样归入 references；人工总结放子域 reference，原始/半结构化事实放 facts；旧索引根目录不再作为 active 入口。
3. 只有内部导航用途的旧 nested module 目录应优先 flatten 为 `references/<module>/` 模块；入口文件改名为 `overview.md`，工具脚本放对应模块 `tools/`，测试放对应模块 `tests/`，模板放 `config/*.template.yaml`。
4. 外部 Agent 适配层不要作为根目录常驻文件夹；合并到 `references/agent-portability.md`，把 CLAUDE.md / skill adapter / .mcp.json 作为可复制模板内联，避免 Hermes skill loader 误识别同名 skill。
5. 历史目录、`dist/`、`__pycache__/`、一次性生成包不留在 active skill tree；确认承接后移出 active tree。
6. 清理后必须验证：`skill_view` 可加载、状态/查询脚本可运行、相关模块 tests/py_compile 通过、旧路径残留 grep 为空、目录体积符合预期。
7. 运行验证生成的 `__pycache__` 也要二次移出 active tree，避免刚清完又污染。

## 阶段资料沉淀 vs 工程代码生成

用户按“第一步/第二域/下一步”推进 SPI 子域时，优先理解为 skill 知识库的领域资料沉淀，而不是立刻修改上一阶段生成的业务工程。

典型纠偏：用户给出 MQ 扩展文档和样例 zip，说“这是 mq 的 spi 扩展，我们往下一步走”，这里的正确动作是生成/更新 `references/mq/index.md`、`references/mq/rocketmq-ons/README.md` 或 `references/mq/shared/`，并在主 `SKILL.md` 注册 MQ 子域路由；不是把 `spi-mq` 源码补进上一阶段的 SSO 示例工程。

执行判据：

1. 用户说“信息 / 文档 / 下一域 / 第二域 / 按这个扩展看一下” → 写 reference md，维护知识结构。
2. 用户明确说“生成工程 / 写代码 / 改这个项目 / 补模块 / 打包” → 才修改业务工程或创建 `spi-{domain}` 模块。
3. 如果误改了业务工程，先撤销工程改动，再把知识沉淀到正确的 `references/<domain>/`。
4. 子域新增必须同步更新主入口 `SKILL.md` 的路由决策树与 References 列表。

## 主入口导航职责

`seeyon-v8-spi/SKILL.md` 不是普通说明文档，而是跨 agent 的导航 / 路由器 / 执行索引。

主入口必须说清楚：

1. 当前支持哪些 SPI 子域。
2. 每个子域的触发词是什么。
3. 每个子域入口文档在哪里。
4. 进入子域后第一步做什么。
5. 何时需要跑状态检查脚本。
6. 何时必须给 Evidence / Contract Source。
7. 哪些内容属于公共层，哪些内容必须下沉到子域 reference 或模块目录。

新增 SPI 子域时，不允许只新增目录或 reference；必须同步更新主入口的路由决策树。否则 Claude Code / Codex 这类只读入口文件的 agent 可能无法发现子域。

### 模块注册模板

```markdown
### N. <子域名>

触发词：<用户可能说法>
入口：`references/<domain>/index.md` 或 `references/<module>/overview.md`
第一步：<读取哪个文件 / 运行哪个脚本>
证据要求：<FACT / OBSERVATION / HYPOTHESIS 规则>
输出要求：<必须输出哪些字段>
```

### 跨 Agent 原则

- Hermes 可用 `skill_view` 是增强能力，不是唯一入口。
- Claude Code / Codex 只要读到主 `SKILL.md`，就必须能顺路径执行。
- nested skill 可发现时是兼容层；不可发现时仍要能通过路径读取执行。



---

# Seeyon V8 SPI Skill 架构健康检查

> 用于复查 `seeyon-v8-spi` 是否还是“可路由、可取证、可生成、可验证”的 skill，而不是退化成知识垃圾桶。

## 复查结论分层

复查时不要只说“清楚/不清楚”，按四个维度给判断：

1. 架构清晰度：主入口是否只做 Routing，子域知识是否下沉，tools/tests 是否归属模块。
2. 当前可用性：关键入口、配置、工具、事实库查询是否能跑。
3. 长期可维护性：新增子域/工具/模板是否有注册规则、证据边界、验证方式。
4. 端到端产品化程度：是否已能从需求自动到生成物、验证报告、交付说明。

建议分数口径：

- 8+：结构可继续演进，不需要推倒重来。
- 6-7：知识可用但闭环不足，优先补 workflow / validator。
- <6：入口或目录职责混乱，先做架构收敛，不继续堆资料。

## 必查项

### 1. 主入口

检查 `SKILL.md` 是否仍保持：

- 需求识别
- 子域路由
- Contract Source / Evidence 优先级
- Super SPI 工程边界
- 验证清单
- Pitfalls

禁止继续塞：

- 大段接口正文
- 大段 Java 代码
- 单次现场过程记录
- 具体子域教程全文

### 2. 四层架构

稳定目标：

```text
SKILL.md                          # Routing / 主入口
references/                       # Knowledge + facts
references/<module>/tools/        # Tools
references/<module>/tests/        # Tool tests
config/external-indexes.yaml      # 运行时 Contract Source 配置
templates/                        # 仅真实可复制、可生成、可验证模板
```

`templates/` 不存在不算问题；空模板目录反而是坏味道。只有有真实模板时再建。

### 3. Contract Source / Evidence

复查时重点看是否仍遵守：

- Contract Source 统一抽象 OpenAPI / MCP / HTTP / Yuque / jar / targeted probe。
- 语雀 rendered-md 上限是 OBSERVATION，不自动升 FACT。
- 关键接口、DTO、method signature 不能只靠 HYPOTHESIS 生成最终代码。
- 输出必须带 Contract Source / Source Type / Capability / Evidence / Locator / Missing Capability。

### 4. 工具验证

从 skill 根目录执行：

```bash
python references/contract-index/tools/contract_index_status.py
python references/contract-index/tools/decompile_jar.py status
python references/contract-index/tools/query_yuque_local_index.py "CtpAvoidLoginMiddlePageProviderService" --limit 3
python -m py_compile references/contract-index/tools/contract_index_status.py references/contract-index/tools/decompile_jar.py references/contract-index/tools/query_yuque_local_index.py
python -m unittest discover -s references/contract-index/tests -p "test*.py" -v
```

这些通过，说明“文档 + 工具”层可用；不代表生成工程已端到端闭环。

## 重要判断：READY 需要语义细分

如果 `contract_index_status.py` 因为 local_doc_index/Yuque enabled 而返回 READY，要在生成代码前继续区分：

- `READY_FACT`：有 OpenAPI exact match / jar index / targeted probe 等 FACT 级来源。
- `READY_OBSERVATION_ONLY`：只有语雀 rendered-md 或历史样例，只能给 OBSERVATION。
- `CONFIG_NEEDED`：没有可用来源。

当前若脚本尚未实现细分，Agent 输出中必须人工标明“READY 但只有 OBSERVATION 来源”或“READY with FACT source”。不要把语雀 READY 当成最终契约 FACT。

## 端到端闭环缺口

架构清楚后，不要继续堆资料。优先补两个能力：

1. Workflow 文档：`references/workflows/spi-generation-workflow.md`
   - 输入格式
   - 路由规则
   - Contract Source 查询顺序
   - 证据不足时降级策略
   - Super SPI 生成步骤
   - 生成后验证清单
   - 最终交付报告格式
   - 必须停下来问用户的条件

2. 生成物验证脚本：例如 `references/generation/tools/validate_generated_spi_project.py`
   - root `pom.xml` well-formed
   - modules 存在
   - `spi-common` 不含 `spring.factories` / `spi_info.json`
   - SPI module 有注册文件
   - 禁止 `lib/` / `systemPath`
   - 禁止无证据 `@Autowired` / 内部 service/dao/mapper
   - SSO/MQ 关键方法存在

## 复查输出格式

建议最终报告按：

```text
结论：清楚可用 / 清楚但闭环不足 / 需重构
评分：架构清晰度 / 当前可用性 / 长期可维护性 / 端到端产品化
已验证：列工具与结果
已修复：列本次 patch
主要缺口：最多 3 条
下一步：只给一个最高 ROI 动作
```

关键原则：

- 如果结构已经清楚，不要建议推倒重来。
- 如果工具能跑但生成未闭环，结论应是“知识/证据/路由可用，产品化闭环不足”。
- 下一步优先 workflow + validator，而不是继续扩资料。



---

## 附录：证据分级系统

> 原 evidence-system.md

# Evidence System（证据分级系统）

> **Rule-001: Skill 不允许把推测当事实。每条知识必须标注证据等级。**

## 证据等级

| 等级 | 标记 | 定义 | 来源 | 生成时行为 |
|------|------|------|------|-----------|
| FACT | ✅ | 可从 jar/源码直接验证 | 反编译结果、jar 文件名、POM 文件 | 直接使用 |
| OBSERVATION | ⚠️ | 从项目代码中观察到 | 具体项目的实现方式、配置值 | 使用但标注来源 |
| HYPOTHESIS | ❓ | 基于经验推断 | 类似项目类推、行业惯例 | 标注为待验证 |

## 标注格式

在 Skill 的所有 references 文件中，知识条目应标注证据等级：

```yaml
# FACT — 来自 jar 反编译
- statement: "CtpUserSsoAuthProviderService 有 getUserLoginInfo 方法"
  evidence: fact
  source: "ctp-user-api-5.3.351.jar 反编译 (paste_1_111544.txt)"

# OBSERVATION — 来自项目代码
- statement: "platform.version 在 5.3.x 中为 3.10.1"
  evidence: observation
  source: "custom-backend-1.0.zip parent pom.xml"

# HYPOTHESIS — 基于推断
- statement: "5.3 SP3 的 ctp-user-api 版本可能为 5.3.400+"
  evidence: hypothesis
  source: "版本号递增规律推断"
  verify_required: true
```

## 生成代码中的证据标注

生成的代码注释中应标注关键决策的证据来源：

```java
/**
 * Generated by seeyon-v8-spi skill v5.0
 *
 * Contract Source: ctp-user-api-5.3.351.jar [FACT ✅]
 * Version: 5.3.293 [OBSERVATION ⚠️ from custom-backend-1.0.zip]
 * Strategy: oauth2 [USER INPUT ✅]
 *
 * ⚠️ platform.version=3.10.1 来自项目观察，请确认与目标环境一致
 */
```

## 证据链追溯

每条知识应可追溯到原始证据：

```
知识: "SPI 代码不能用 @Autowired"
  ↓ 来源
DOCX 知识库原文: "SPI代码中不能使用@Autowired，获取bean只能通过App.getFactory.getBean()"
  ↓ 交叉验证
项目观察 A: 无 @Autowired 使用
项目观察 B: 无 @Autowired 使用
  ↓ 结论
evidence: fact (多源验证)
```

## 证据降级规则

| 情况 | 处理 |
|------|------|
| 只有一个项目观察到 | observation, confidence: low |
| 多个项目观察到相同模式 | observation, confidence: high |
| jar 中直接可见 | fact |
| 文档中声明但无法验证 | observation (文档可能过时) |
| 纯推断无任何项目证据 | hypothesis, verify_required: true |
| 用户口头声明 | observation, source: "user stated" |

## 证据冲突处理

当不同来源的证据冲突时：

1. **jar 反编译 > 项目代码 > 文档 > 推断**
2. 标注冲突，不静默覆盖
3. 生成代码时选择高可信度来源，注释中说明冲突

```yaml
conflict:
  statement: "ctp-user-api 版本号"
  sources:
    - value: "5.3.351"
      evidence: fact
      source: "用户提供的 jar 文件名"
    - value: "5.2.4"
      evidence: observation
      source: "项目观察 B pom.xml"
  resolution: "使用 5.3.351（FACT 优先于 OBSERVATION）"
  note: "项目观察 B可能使用旧版本"
```

## 在 Health Check 中使用证据等级

```
[PASS ✅] Rule-005: V8 版本兼容
  evidence: FACT (jar 文件名 ctp-user-api-5.3.351.jar)

[WARN ⚠️] Rule-005: V8 版本兼容
  evidence: OBSERVATION (custom-backend-1.0.zip pom.xml)
  note: platform.version=3.10.1 来自项目观察，请确认

[SKIP ❓] Rule-005: V8 版本兼容
  evidence: HYPOTHESIS (无 jar 无项目，仅用户口头版本号)
  note: 建议提供 jar 文件以验证
```

