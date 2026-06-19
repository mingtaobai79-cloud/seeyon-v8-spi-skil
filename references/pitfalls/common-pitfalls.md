# Seeyon V8 SPI 常见坑

> 从 SKILL.md 下沉。入口只保留灾难级红线，本文件保留详细坑位。

## 关键坑

0. 认证/SSO/免登/三方 App SPI 模板有专门质量门禁（已合并到 `references/spi-domain-constraints.md` 附录 A）。用户明确纠正过：只生成类、少注释、不用接口参数/注解/日志、没有 Nacos 参数、把结构验证当真实测试，都是"玩具"。
1. `spi-common` 不是 SPI，不注册 `spring.factories`，不放 `spi_info.json`。
2. `spi-sso` 是 SSO 唯一 module，统一认证/免登/单点登录只在内部按 package 分流。
3. 统一认证固定进 `spi-sso/unifiedauth`。
4. 三方免登固定进 `spi-sso/avoidlogin`。
5. V8 到三方单点固定进 `spi-sso/connector`。
6. 本地三方 jar 只能放 root `third-jar/` 暂存，优先 install/deploy 后 Maven dependency 引用。
7. 用户说"SM3 解密"时必须纠正：SM3 是摘要，不可解密；需确认是 SM2 还是 SM4。
8. 解密后的人员编号/工号如果就是 V8 loginName/code，可直接返回对应字段，不一定要 OpenAPI 二次查询。
9. 生成 SSO/SPI Java 代码时禁止默认套 Hutool `StrUtil`。除非 POM/Contract 明确证明可用。
10. Contract First ≠ Jar First。先走 Contract Index 状态检查。
11. 子域 reference 不是事实终点。找不到时搜索 `references/facts/yuque-v8-docs-rendered-md/docs/`。
12. MQ 是 SSO 后的第二子域。
13. Contract Index 保持一个内聚模块。
14. 外部 Agent 适配层统一沉淀到 `references/agent-portability.md`。
15. 生成示例工程后必须做静态结构验证。
16. 维护本 skill 结构时保持"子域 reference + facts 事实库 + 模块 tools/tests"三分法。
17. 查询语雀 rendered-md 时，跳过 bootstrap 巨长行。
18. 系统变量扩展文档只给短名和示例，full qualified name 必须经 jar/source 确认。
21. **system-variable SPI 接口不在预期 jar 中**：`boot-starter-systemvariable-5.3.313.jar`（仅 4 个类：EnvFunction、SystemVariableKeyEnum、SystemVariableService、SystemVariableUtils）和 `boot-starter-formula-5.3.313.jar`（有 ExpressionService 但无 SPI 接口）都不包含 `SystemVariableSPIService`、`@SPISystemVariable`、`SPISystemVariableType`。这三个 SPI 接口在一个尚未确认的 jar 中（可能是 `boot-starter-spi-api` 或类似 artifact）。
22. **已确认的 FQCN**（来自 jar 反编译 FACT）：`Apps` = `com.seeyon.boot.context.Apps`；`ExpressionService` = `com.seeyon.boot.starter.formula.domain.service.ExpressionService`。
23. **"冻结"语义**：用户说"去掉/除去/冻结"某个域时，意思是停止该域的工作推进，不是替换引用。不要主动修改已冻结域的文件内容。
19. 新增/重抓语雀 rendered-md 时，先查 manifest 避免重复。
20. **域合并规则**：auth-sso 域包含 Super SPI（unified-auth、avoid-login、sso-connector）和旧版本 SPI（auth-provider、inbound-sso、outbound-sso、mobile-app、ticket-custom-userinfo、qrcode-login、login-pre-portal），统一在 `references/auth-sso/` 下，不再分 legacy。MQ 同理，`references/mq/` 包含所有 MQ 内容。
21. **Frozen Skeleton 模式**：当 jar 不可用但用户要求"先做一个版本"时，不要阻塞。生成 frozen skeleton：(a) implements 接口注释掉，(b) @注解注释掉，(c) 平台 API 调用注释掉并加 `// placeholder` 返回值，(d) 文件头加 EVIDENCE STATUS 块列出所有待确认 FQCN，(e) spring.factories 用 PLACEHOLDER key。代码可编译（注释掉的代码不影响编译），拿到 jar 后 5 分钟内可激活。这是用户明确偏好的降级方式，不要反复确认。
22. **工程模块命名惯例**：auth-sso-spi-parent 项目中模块按 `spi-NN-{name}` 编号（spi-01 到 spi-16），新增模块取下一个编号。不要创建独立的 custom-backend/ 工程，除非用户明确要求。
