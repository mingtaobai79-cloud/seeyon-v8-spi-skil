# Health Check Rules（健康检查规则）

> 生成代码后自动校验，输出 PASS/FAIL 报告。

## 规则列表

### Rule-001: SPI 接口实现正确

**检查项：**
- 模式 A：实现类 implements `CtpUserSsoAuthProviderService`
- 模式 B（MiddlePage）：实现类 implements `CtpAvoidLoginMiddlePageProviderService`
- 模式 B（ClientMode）：实现类 implements `CtpAvoidLoginClientModeProviderService`
- 模式 C：实现类 implements `SsoService`

**验证方法：** 检查 Java 文件的 implements 子句

---

### Rule-002: spring.factories 存在且路径正确

**检查项：**
- 文件存在于 `src/main/resources/META-INF/spring.factories`
- 接口全路径与模式匹配：
  - 模式 A: `com.seeyon.ctp.user.api.sso.CtpUserSsoAuthProviderService`
  - 模式 B: `com.seeyon.ctp.user.api.avoidlogin.CtpAvoidLogin{MiddlePage/ClientMode}ProviderService`
  - 模式 C: `com.seeyon.cip.connector.api.sso.SsoService`
- 实现类全路径与实际类名一致

**验证方法：** 读取 spring.factories，比对接口路径和实现类路径

---

### Rule-003: spi_info.json scopes 匹配

**检查项：**
- 文件存在于 `src/main/resources/metadata/spi_info.json`
- `name` 字段为 `"boot-starter-spi-customized"`
- `scopes` 数组包含正确的作用域：
  - 模式 A/B: `["ctp-user"]`
  - 模式 C: `["cip-connector"]` 或 `["{应用编码}"]`

**验证方法：** 解析 JSON，检查 name 和 scopes

**注意：** 每个实际业务 SPI 模块都需要 spi_info.json；`spi-common` 不注册 SPI，禁止放 spi_info.json。

---

### Rule-004: 返回值类型正确

**检查项：**
- 模式 A：`getUserLoginInfo()` 返回 `CtpUserSpiLoginUserInfoDto`
- 模式 B：`getUserInfo()` 返回 `CtpAvoidLoginUserInfoDto`
- 模式 C：`login()` 返回 `String`（URL）

**验证方法：** 检查方法签名的返回类型

---

### Rule-005: V8 版本兼容

**检查项：**
- 父 POM 的 `parent.version` 与用户提供的 V8 版本匹配
- `platform.version` 与版本矩阵一致
- 依赖的 API jar 版本正确
- 如果使用了 Builder 模式，确认版本 ≥ 5.3

**验证方法：** 解析 POM，比对版本矩阵

---

### Rule-006: 异常处理完整

**检查项：**
- 模式 A/B：认证失败使用 `CtpUserSpiSsoException`（不是 RuntimeException）
- 模式 A/B：有 catch 块处理异常
- 模式 C：login 方法有 try-catch

**验证方法：** 搜索 `throw new CtpUserSpiSsoException` 和 `catch` 块

---

### Rule-007: 无 @Autowired 使用

**检查项：**
- 整个工程中不存在 `@Autowired` 注解
- 获取 Bean 使用 `CtpUserSpiUtils.getInstance()` 或 `App.getFactory().getBean()`

**验证方法：** 搜索 `@Autowired`

---

### Rule-008: POM 依赖版本匹配

**检查项：**
- 模式 A/B：依赖 `ctp-user-api`
- 模式 C：依赖 `cip-connector-api`
- 版本号与 platform.version 一致
- 平台 API 与可解析三方库使用 Maven dependency；禁止生成 lib/；默认禁止 systemPath
- 本地/私有三方 jar 位于根目录 third-jar/ 且已给出 install/deploy 到 Maven 的说明

**验证方法：** 解析 POM dependencies

---

### Rule-009: 模式 A 注解正确

**检查项（仅模式 A）：**
- 实现类有 `@CtpUserChannelRouter` 注解
- 注解值与 Nacos 配置的 `thirdauth.type` 一致

**验证方法：** 检查类注解。注意注解值可能是字面量或常量引用：
- `@CtpUserChannelRouter("HNJWT")` → 直接比对字面量
- `@CtpUserChannelRouter(Constants.THIRD_TYPE)` → 需进一步检查常量类中 THIRD_TYPE 的值

**常见 false negative：** 如果只检查字面量，常量引用会被误判为 FAIL。必须同时检查两种形式。

---

### Rule-010: 模式 C 命名一致

**检查项（仅模式 C）：**
- `getName()` 返回值 + "SsoServiceImpl" = 类名
- `getTypeCaption()` 返回非空中文字符串

**验证方法：** 检查 getName() 返回值与类名的关系

---

### Rule-011: Nacos 配置完整

**检查项：**
- 常量类中引用的 Nacos key 在 nacos.yaml 中都有对应配置
- 模式 A：包含 `seeyon.auth.type: spisso` 和 `seeyon.thirdauth.type`
- 模式 B：包含 `seeyon.thirdauth` 或项目特有配置

**验证方法：** 提取 `CtpUserSpiUtils.getPropertyByName("xxx")` 中的 key，比对 nacos.yaml

---

### Rule-012: 日志完整

**检查项：**
- 类有 `@Slf4j` 注解
- 核心方法（getUserLoginInfo / getUserInfo / login）有 `log.info` 入口日志
- catch 块有 `log.error`

**验证方法：** 搜索 `@Slf4j`、`log.info`、`log.error`

---

### Rule-013: Import 白名单检查（Rule-002 执行验证）

**检查项：**
- 所有 Java 文件的 import 语句必须在白名单内
- 白名单分层：Tier 0 (JDK) → Tier 1 (平台API) → Tier 2 (平台通用) → Tier 3 (常用三方) → Tier 4 (策略特有)
- 黑名单 import 不得出现（java.sql.*, javax.persistence.*, org.hibernate.*, redis, @Autowired 等）

**验证方法：** 正则提取所有 `import` 语句，逐条比对白名单前缀和黑名单前缀

---

### Rule-014: needUserBind() 返回值正确（仅模式 C）

**检查项：**
- 模式 C 实现类包含 `needUserBind()` 方法
- 返回值为 `true`（需要用户信息时）或 `false`（不需要时）
- 返回 `true` 时 userMap 参数才有数据

**验证方法：** 搜索 `needUserBind` 方法及其返回值

---

### Rule-015: userMap 字段使用正确（仅模式 C + needUserBind=true）

**检查项：**
- 使用标准 userMap 字段名：`innerUserLoginName`、`innerUserName`、`innerUserCODE`、`innerUserPhone`
- 不使用未文档化的字段名

**验证方法：** 搜索 `userMap.get(` 调用，检查 key 是否在已知字段列表中

---

### Rule-016: getPageJson() 返回有效配置（仅模式 C）

**检查项：**
- `getPageJson()` 方法存在且返回非空字符串
- 返回的 JSON 包含 `caption`、`type`、`extensionProperties` 字段
- `type` 值与 `getName()` 返回值一致

**验证方法：** 检查方法存在性和返回字符串关键字

---

### Rule-017: ssoToken URLEncode（仅模式 C）

**检查项：**
- 加密/签名后的 token 在拼接到 URL 前经过 `URLEncoder.encode()`
- 编码字符集为 `UTF-8`

**验证方法：** 搜索 `URLEncoder.encode` 调用

---

### Rule-013: Import 白名单检查（Rule-002 执行验证）

**检查项：**
- 所有 Java 文件的 import 语句必须在白名单内
- 白名单分层：Tier 0 (JDK) → Tier 1 (平台API) → Tier 2 (平台通用) → Tier 3 (常用三方) → Tier 4 (策略特有)
- 黑名单 import 不得出现（java.sql.*, javax.persistence.*, org.hibernate.*, redis, @Autowired 等）

**验证方法：** 正则提取所有 `import` 语句，逐条比对白名单前缀和黑名单前缀

---

### Rule-014: needUserBind() 返回值正确（仅模式 C）

**检查项：**
- 模式 C 实现类包含 `needUserBind()` 方法
- 返回值为 `true`（需要用户信息时）或 `false`（不需要时）
- 返回 `true` 时 userMap 参数才有数据

**验证方法：** 搜索 `needUserBind` 方法及其返回值

---

### Rule-015: userMap 字段使用正确（仅模式 C + needUserBind=true）

**检查项：**
- 使用标准 userMap 字段名：`innerUserLoginName`、`innerUserName`、`innerUserCODE`、`innerUserPhone`
- 不使用未文档化的字段名

**验证方法：** 搜索 `userMap.get(` 调用，检查 key 是否在已知字段列表中

---

### Rule-016: getPageJson() 返回有效配置（仅模式 C）

**检查项：**
- `getPageJson()` 方法存在且返回非空字符串
- 返回的 JSON 包含 `caption`、`type`、`extensionProperties` 字段
- `type` 值与 `getName()` 返回值一致

**验证方法：** 检查方法存在性和返回字符串关键字

---

### Rule-017: ssoToken URLEncode（仅模式 C）

**检查项：**
- 加密/签名后的 token 在拼接到 URL 前经过 `URLEncoder.encode()`
- 编码字符集为 `UTF-8`

**验证方法：** 搜索 `URLEncoder.encode` 调用

---

## 报告格式

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔍 SSO Project Health Check
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[PASS] Rule-001: SPI 接口实现正确 ({接口名})
[PASS] Rule-002: spring.factories 路径正确
[PASS] Rule-003: spi_info.json scopes={scopes}
[PASS] Rule-004: 返回值类型 {类型名}
[PASS] Rule-005: V8 版本 {版本号} 兼容
[PASS] Rule-006: 异常处理使用 CtpUserSpiSsoException
[PASS] Rule-007: 无 @Autowired
[PASS] Rule-008: POM 依赖版本匹配
[PASS] Rule-009: @CtpUserChannelRouter 注解正确（仅模式 A）
[PASS] Rule-010: getName() 命名一致（仅模式 C）
[PASS] Rule-011: Nacos 配置完整
[PASS] Rule-012: 日志完整

Result: PASS 12/12 ✅

⚠️ 注意事项：
- 构建后需重启 {服务名} 服务
- Nacos 配置需手动添加到 {微服务名} 下
```

如果有 FAIL：
```
[FAIL] Rule-007: 发现 @Autowired 使用
  → 位置: {文件名}:{行号}
  → 修复: 替换为 CtpUserSpiUtils.getInstance({类名}.class)
```
