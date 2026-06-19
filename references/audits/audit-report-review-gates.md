# 审计报告复审 Gate（PASS / PARTIAL / FAIL）

用于复审 `seeyon-v8-spi` 的只读审计报告、生成准备度报告、hygiene 扫描报告。目标不是重复报告结论，而是判断它是否真的验证了红线。

## 1. 先判报告类型

复审前先区分：

| 报告类型 | 可以要求 | 不应要求 |
|---|---|---|
| 只读准备度审计 | Evidence locator、缺口口径、冻结域 STOP、污染扫描分类、断链/卫生扫描规则 | 必须跑生成物 validator |
| 生成交付审计 | 工程结构、`spi-common` 污染、`spring.factories` / `spi_info.json`、validator 输出、手工补充检查项 | 只说“准备度可生成”就算通过 |

规则：没生成工程时，不跑 `validate_generated_spi_project.py` 不算违规；但也不能宣称 `spi-common` / 生成结构 / validator 已通过。

## 2. READY 必须分层，不要一句 READY 混过去

输出 READY 时拆成：

- `READY_FACT`：接口、DTO、注册 key、scope 等已有源码 / jar / 反编译 / exact locator。
- `READY_OBSERVATION`：实现策略来自样例、语雀、项目观察，可参考但不能当平台 Contract。
- `PARAM_REQUIRED`：现场参数，例如 project_id、endpoint、accessKey、secretKey、topic/group、Nacos key 命名、目标版本。
- `SKELETON_READY_ONLY`：入口接口足够生成骨架，但 DTO/回调/表结构/版本仍缺，不能宣称完整落地。
- `STOP_FROZEN`：冻结域，停止生成和修改。

典型 MQ 口径：接口/DTO/注册 key 为 `READY_FACT`；ONS client 版本、配置 key、endpoint/accessKey/secretKey 为 `PARAM_REQUIRED`；ONS 实现链路为 `READY_OBSERVATION`。

## 3. 案例污染扫描必须分类

不要只报“命中 N 条”。至少分四类：

| 分类 | 含义 | 处理 |
|---|---|---|
| `ACTIVE_REFERENCE_POLLUTION` | active reference 中真实客户名、真实域名、真实 secret、不可泛化案例值 | 必修清理 |
| `LEGAL_CONTRACT_FIELD` | `clientSecret` / `appSecret` 作为接口字段、参数、契约名 | 保留 |
| `PLACEHOLDER_OK` | `CHANGE_ME_IN_NACOS`、`{project_id}`、`C:/path/to/...` 示例路径 | 保留或弱提示 |
| `FACTS_RAW_SAMPLE` | `references/facts/` 原始语雀/文档样例，例如 `ncoa` | 不直接清理；只避免回流到 active reference |

关键原则：`facts/` 是原始证据区，不等同 active skill 污染。清理前先确认是否会破坏证据链。

## 4. 断链 / hygiene 结论必须可复验

“断链 0”“顶层 md 符合 hygiene”这类结论需要说明扫描规则：

- 扫描范围。
- 忽略规则：`http/https/mailto/data`、纯锚点、代码块是否忽略。
- 是否解析 anchor。
- 是否支持目录链接。
- root-relative `references/...` 路径如何处理。
- 脚本或命令入口。

没有扫描规则时，只能判为“声称已扫”，不要强 PASS。

## 5. 红线复审清单

逐项给 PASS / PARTIAL / FAIL：

1. 冻结域是否继续生成或修改。
2. 是否把 AI 推断接口签名升为 FACT。
3. 是否把案例污染从样例/facts 回流到 active reference 或模板。
4. 是否存在 `spi-common` 注册 `spring.factories` / 放 `spi_info.json`。
5. 生成交付是否跑 validator；validator 覆盖不到的项是否列手工检查，不得伪装成通过。

## 6. 推荐输出格式

```text
结论：PASS / PARTIAL / FAIL
原因：一句话

覆盖检查：
1. <检查项>：PASS/PARTIAL/FAIL — <证据 locator / 问题>
...

必修问题：最多 4 条
可延后问题：最多 3 条
下一步测试语句：给一条能压出红线的完整 prompt
```

判定口径：主判断正确但验证强度不足，通常是 `PARTIAL`，不是 PASS。
