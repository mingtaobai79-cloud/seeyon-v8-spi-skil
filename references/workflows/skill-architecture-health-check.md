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

## 结构审计补充：完成态不能只看断链

当用户问“除了冻结是不是都完成了 / 入口有没有问题 / 有没有重复和错误文件”时，必须额外检查以下三类问题；断链 0 不等于结构 PASS：

1. **状态表算术一致性**
   - 核对 `references/index.md` 的域表数量与“总计”是否相等。
   - Capability Channel 按 28 个能力文件夹计入 SPI 数量；不要沿用旧聚合目录时期的总数。

2. **域 root 与 shared/SPI 子目录重复**
   - 对每个业务域检查 root 下除 `index.md` 外的 `.md`。
   - 如果同名或同主题文档同时存在于 `references/<domain>/` 与 `references/<domain>/shared/` 或 `references/<domain>/<spi>/`，判为迁移残留风险。
   - 处理顺序：先查 active 引用，再确认 shared/SPI 子目录承接，最后将 root legacy 文件移出 active tree。
   - 典型形态：`deployment-guide.md`、`health-check-rules.md`、`generated-project-validation.md` 在 root/shared 双份并存。

3. **冻结 README banner 一致性**
   - `references/status/frozen-artifacts.md` 中列出的冻结 SPI，其 `README.md` 头部必须有 🧊/冻结 banner。
   - 内容里写了 jar 缺失或 OBSERVATION 还不够；没有头部 banner 会导致后续 agent 误判为可推进。

报告口径：
- 断链 0 + 顶层 md 合规 + Contract READY，但存在总数错误、root/shared 双份、冻结 banner 缺失时，结论是 `PARTIAL`，不是 PASS。
- “除了冻结都完成了”可以给基本肯定，但必须把上述结构债列为收口前必修项。

4. **运行时配置 / 模板漂移**
   - 对比 `config/external-indexes.yaml` 与 `config/external-indexes.template.yaml` 的 `query_order`、enabled sources、capability mapping。
   - runtime 已启用但 template 缺失的来源（例如 `local_doc_index` / 语雀本地索引）判为漂移风险：后续按 template 重置会丢能力。
   - template 不应写死本机绝对路径；用“skill root 下的相对路径”描述 source of truth。
   - `local_jar_index.enabled=true` 时，如果 registry 文件不存在或 entries=0，报告里必须区分“预留能力”与“已有 FACT jar index”，避免把 READY 误报成 FACT-ready。

5. **active tree 污染与验证副产物**
   - 扫描 `__pycache__/`、`.pyc`、`dist/`、一次性 zip/report/json；这些不应留在 active skill tree。
   - 注意：运行 py_compile / tests 后会重新生成 `__pycache__`，收口前必须二次清理。
   - 空 `__init__.py` 精确重复可接受；`.pyc` 精确重复/副产物不可接受。

6. **旧 stop point / 内嵌重复治理文档**
   - 检查 `architecture-control-protocol.md` 的稳定目录树是否与真实 active tree 一致；旧 `sso/` 应为 `auth-sso/`，不要保留旧目录名作为 stop point。
   - 如果 `architecture-control-protocol.md` 内嵌了与 `workflows/knowledge-organization.md` 大段重复的治理规则，判为 drift 风险；总协议只保留摘要与转发，细则归 workflow。
   - 示例路径如 `templates/super-spi/source/...` 必须明确标注“未来示例，不代表当前 active path”，否则 raw path 审计会产生歧义。

7. **语雀索引职责分离**
   - `references/yuque-local-index.md` 应是检索策略入口。
   - `references/facts/yuque-v8-docs-rendered-md/outline.md` 应是本地 SPI 子集清单。
   - 两者标题/职责不要完全重复，否则后续 agent 会混淆“策略入口”和“事实清单”。

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
