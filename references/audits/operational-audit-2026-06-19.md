# seeyon-v8-spi Operational Audit Report

时间：2026-06-19 00:08:03
范围：`<skill-root>`（seeyon-v8-spi skill 根目录）

## 1. 审计目标

这次不是只看文档结构，而是按真实 Agent 使用路径压测：

1. 状态/冻结查询能否从入口正确路由到唯一状态源。
2. Super SPI 生成请求能否走到 domain/spi/workflow/validator/Maven 边界。
3. jar/source/Contract 证据升级请求能否优先进入 Contract Index，不回退到经验猜测。
4. 检查旧路径、断链、workflow/status 静态口径残留。

## 2. 压测用例结果

### Case A：状态 / 冻结 / 缺口查询

模拟问题：现在 seeyon-v8 SPI 状态、冻结项、还缺什么？

实际读取链路：

1. SKILL.md
2. references/index.md
3. references/status/frozen-artifacts.md
4. references/status/evidence-summary.md

结果：PASS

关键观察：

- references/status/evidence-summary.md 已经只做状态转发，不复制静态计数。
- references/index.md 是当前状态唯一主源。
- frozen-artifacts.md 的冻结语义清楚：冻结 = 停止推进，不修改冻结域。

风险：低。

### Case B：生成 Super SPI 工程路由

模拟问题：生成组织同步中间表 Super SPI 工程。

实际读取链路：

1. references/integration-sync/index.md
2. references/integration-sync/org-sync-middle-table/README.md
3. references/integration-sync/org-sync-middle-table/constraints.md
4. references/spi-domain-constraints.md
5. references/workflows/spi-generation-workflow.md
6. references/generation/maven-verification-notes.md
7. references/contract-index/tools/contract_index_status.py

结果：PASS

关键观察：

- org-sync-middle-table 的接口、回调服务、spring.factories、约束均能被路由到。
- 生成 workflow 明确要求先归一化输入、查 Contract Index、生成后运行 validator。
- Maven 编译边界正确：只作为现场增强验证，不作为 skill 默认交付。
- contract_index_status.py 当前返回 READY：已启用 1 个外部源，本地 jar index 0 条。

风险：低。

### Case C：jar/source/Contract 证据升级路由

模拟问题：提供更高版本 jar 后升级系统变量 SPI Evidence。

实际读取链路：

1. references/system-variable/index.md
2. references/system-variable/system-variable-spi/README.md
3. references/system-variable/system-variable-spi/constraints.md
4. references/contract-index/overview.md
5. references/contract-index/contract-discovery.md
6. references/workflows/evidence-upgrade-workflow.md
7. references/contract-index/tools/contract_index_status.py

结果：PASS

关键观察：

- 系统变量域冻结原因明确：5.3.313 的 boot-starter-systemvariable / boot-starter-formula 不含目标 SPI 接口类。
- Evidence 升级 workflow 明确要求 jar tf / 提取 / CFR / 更新 README / constraints / domain index / root index。
- Contract Index 策略正确：External/Local Index First，不是 Jar First；用户提供 jar 时才 targeted probe / decompile。

风险：低。

## 3. 发现并已修复的问题

### 3.1 旧路径残留 / 断链

修复文件：

- references/contract-index/contract-discovery.md
- references/contract-index/initialization.md
- references/contract-index/overview.md
- references/contract-index/jar-contract-indexing-plan.md
- references/mq/rocketmq-ons/README.md
- references/mq/rocketmq-ons/README.md（已归一化，示例事实不再单独作为默认加载文件）
- references/mq/shared/closeout.md
- references/mq/shared/deployment-guide.md
- references/mq/shared/health-check-rules.md
- references/infra-config-registry/index.md

修复内容：

- Contract Index 文档中的旧根路径已改为 root-relative（例如外部索引 / jar 索引 / source-types / capability-contract 均改到 references/contract-index/ 下）。
- MQ 下沉后的旧 flat-path 已改为 shared/ 或 rocketmq-ons/ 子目录下的新路径。
- infra-config-registry/index.md 中 config/README.md 链接被解析为 skill 根 config/README.md，已改为 ./config/README.md。
- contract-index/overview.md 中不存在的治理说明路径已改为当前模块入口。

### 3.2 未修复但刻意排除的项

- SKILL.full-archive.md：历史归档文件，不作为 active skill 路由源；断链扫描中排除。
- references/facts/yuque-v8-docs-rendered-md/：本地事实库原文/渲染文档，非 active workflow 路径；断链扫描中排除。
- 代码块中的占位符如 references/{domain}/...：属于模板，不按真实文件校验。

## 4. 当前结论

seeyon-v8-spi 当前可用性：PASS。

可以支撑三类真实任务：

1. 查询状态/冻结/缺口：从 SKILL.md → references/index.md → status 文档闭环。
2. 生成 Super SPI 工程：从 domain/spi → generation workflow → validator → Maven 边界闭环。
3. 证据升级：从 Contract Index → Evidence upgrade workflow → root/domain/spi 状态同步闭环。

剩余主要风险不是架构问题，而是资料本身的冻结项：缺更高版本 jar/source 的域仍不能 FACT 化，不应强行生成可部署代码。

## 5. 建议

短期不需要继续膨胀入口。后续维护只做两类动作：

1. 用户提供新 jar/source/sample 时，走 Contract Index + Evidence Upgrade，更新对应 domain/spi 文档。
2. 生成工程失败时，只回补 validator / workflow / domain constraints，不把现场 Maven/私服配置固化进 skill。
