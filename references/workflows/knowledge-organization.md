# Skill 知识结构治理规则

> 来源：会话纠偏。用户明确指出：这里治理的是 skill 知识库结构，不是生成项目的源码模板目录。

## 目标形态

`seeyon-v8-spi` 是 Super SPI 的统一入口 skill。

总控制协议见：`references/architecture-control-protocol.md`。

稳定四层：

1. `SKILL.md` = Routing / 主入口，只做需求识别、路由、证据优先级、生成边界、验证清单。
2. `references/` = Knowledge / 子域知识与事实库。
3. `references/<module>/tools/` = Tools / 可调用工具层，例如 Contract Index 工具。
4. `templates/` = Templates / 真实可复制、可生成、可验证的模板层。

硬边界：

- 顶层 `SKILL.md` 只做入口、路由、铁律、边界说明。
- 具体领域知识下沉到 `references/` 的子目录。
- Auth/SSO 是一个子域，所有认证与单点细节集中放在 `references/auth-sso/`。
- MQ 是一个子域，所有 MQ 细节集中放在 `references/mq/`。
- Contract Source / jar / OpenAPI / MCP / HTTP 统一进入 `references/contract-index/`。
- 不把统一认证、免登、单点登录、MQ、OpenAPI 或 jar 细节散落在顶层。
- 不继续把资料往主入口堆成知识垃圾桶。

## Auth/SSO 子域结构

```
references/auth-sso/
├── index.md                         # Auth/SSO 总导航
├── unified-auth/README.md           # 统一认证 / 登录页接统一认证中心
├── avoid-login/README.md            # 三方 → V8 免登
├── sso-connector/README.md          # V8 → 三方单点登录
├── inbound-sso/README.md            # 外部系统进 V8 的 SSO
├── outbound-sso/README.md           # V8 出站 SSO
└── shared/auth-strategies.md        # OAuth2/CAS/SM2/SM4/RSA/AES/OIDC/SAML/JWT/LDAP 等策略
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

这些应放入 `references/auth-sso/**/*.md` 或其他领域子目录。

## 不要误建 templates

只有“未来要复制出去并修改的真实 starter 文件”才放 `templates/`。

不要为了让用户“看见目录”而创建生成项目源码骨架，例如：

```
templates/super-spi/source/...
```

如果用户说“没看见文件/目录”，先确认他说的是 skill 知识目录还是生成项目模板。对于本 skill 的 Auth/SSO 导航诉求，正确动作是整理 `references/auth-sso/`，不是创建源码模板。

## 导航优先级

用户提到 Auth/SSO 相关时：

1. 先加载 `references/auth-sso/index.md`。
2. 再按场景加载：
   - 统一认证 → `references/auth-sso/unified-auth/README.md`
   - 三方免登 V8 → `references/auth-sso/avoid-login/README.md`
   - V8 到三方单点 → `references/auth-sso/sso-connector/README.md`
   - 外部系统进 V8 → `references/auth-sso/inbound-sso/README.md`
   - V8 出站 SSO → `references/auth-sso/outbound-sso/README.md`
3. 涉及 OAuth2/CAS/SM2/SM4/RSA/AES/OIDC/SAML/JWT/LDAP 等，再加载 `references/auth-sso/shared/auth-strategies.md`。

## 维护规则

- references 根目录只放跨 SPI 公共语义/结构文档，例如：入口索引、架构控制协议、全局约束、OpenAPI 总索引、Agent 适配；契约发现/证据/运行模式/部署等细节下沉到 `references/contract-index/`、`references/status/`、`references/workflows/`、`references/generation/`。
- 某个 SPI 子域自己的约束、版本矩阵、Health Check、部署、依赖白名单、API Contract，必须放进该子域目录。Auth/SSO 的这些文件统一放 `references/auth-sso/`；MQ 的这些文件统一放 `references/mq/`。
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

典型纠偏：用户给出 MQ 扩展文档和样例 zip，说“这是 mq 的 spi 扩展，我们往下一步走”，这里的正确动作是生成/更新 `references/mq/*.md`，并在主 `SKILL.md` 注册 MQ 子域路由；不是把 `spi-mq` 源码补进上一阶段的 SSO 示例工程。

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

