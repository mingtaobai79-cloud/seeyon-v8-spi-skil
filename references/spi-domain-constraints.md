# SPI 域公共约束 / Domain Constraints

> 所有 SPI 子域（auth-sso、crypto、file-storage、datasource 等）生成代码、沉淀文档、做交付验证时，必须先读本文件。域独有约束在各域 `constraints.md` 中补充，不得与本文件冲突。

## 1. 证据标注

所有关键判断必须同时标明 Contract Source、Evidence、Locator。

| 等级 | 标记 | 定义 |
|------|------|------|
| FACT | ✅ | 源码/jar/反编译结果/官方 OpenAPI exact match |
| OBSERVATION | ⚠️ | 语雀 rendered-md、历史样例、项目观察 |
| HYPOTHESIS | ❓ | 版本矩阵、经验推断、AI 推断，必须提示待验证 |

关键接口、DTO、method signature 不能只靠 HYPOTHESIS 生成最终代码。

## 2. 代码规范

### 2.1 JavaDoc

- 类级 JavaDoc：说明场景、V8 调用时机、三方系统、返回语义。
- 方法 JavaDoc：逐个解释参数、返回值、异常。
- 参数字段：说明来源（V8 平台传入 / 三方系统 / Nacos 配置）。

### 2.2 日志

- 使用 `org.slf4j.Logger`（`@Slf4j` 或手动 `LoggerFactory`）。
- SPI 入口必须打关键日志：clientId / thirdType / traceId / requestId。
- 关键分支、成功、失败都要有日志。
- 脱敏：token / secret / sign / code / mobile / email 不得明文落日志。
- 日志前缀按域统一：`[avoid]`、`[mobile-app]`、`[qrcode]`、`[crypto]` 等。

### 2.3 禁止项

- 禁止 `@Autowired`、`@Service`、`@Component` 等 Spring 注解（SPI 不走 Spring 容器扫描）。
- 禁止默认套 Hutool `StrUtil`；除非 POM/Contract 明确证明可用。
- 禁止 `lib/` 目录、`systemPath`。
- 禁止在 `spi-common` 放 `spring.factories` / `spi_info.json`。
- 禁止把不同业务域硬塞同一实现类。
- SM3 是摘要不可解密；用户说"SM3 解密"时必须纠正。

### 2.4 配置读取 / Request 获取

- 通用配置读取优先使用平台 boot 能力：`Apps.getEnvironment().getProperty(...)` 或 `EnvironmentHolder.get().getProperty(...)`。
- Bean 获取优先使用平台 boot 能力：`Apps.getBeanFactory().getBean(...)` / `Apps.getApplicationContext().getBean(...)`。
- Servlet request/response 只有确需 Web 上下文时使用 `HttpServletRequestContext.getRequest()` / `getResponse()`。
- `CtpUserSpiUtils`、`CipConnectorSpiUtils` 等只属于对应子域契约包的能力；不得写入全局公共约束，必须在目标子域 contract 已 FACT 后才可使用。

## 3. Nacos 配置规范

每个 SPI 场景必须给出 Nacos 样例和参数说明。格式：

```yaml
# {服务名} 微服务 Nacos 配置
seeyon:
  {domain}:
    {module}:
      key: value
```

每个 key 在 `docs/API_AND_CONFIG.md` 中标明：

| Key | Required | Sensitive | Default | Example | 说明 |
|-----|----------|-----------|---------|---------|------|

敏感字段（secret/key/token）必须标 `CHANGE_ME_IN_NACOS`。

## 4. 注册文件

### 4.1 spring.factories

```properties
<扩展接口FQCN>=<实现类FQCN>
```

- key 必须是目标版本真实接口 FQCN。
- value 必须是实现类 FQCN。
- 一个 jar 可注册多个 SPI，但不同业务域不共用实现类。

### 4.2 spi_info.json（Super SPI 才需要）

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["{scope}"]
}
```

旧 SPI / 5.6 以下版本不默认生成 `spi_info.json`；只有目标页面明确需要时才加。

## 5. 部署规范

### 5.1 重启服务

每个 SPI 必须标明重启哪些服务（ctp-user / cip-connector / portal / 全部）。

### 5.2 插件加载方式（旧 SPI）

三种方式，以现场为准：

```yaml
# Maven 私服
seeyon:
  spi:
    enable: true
    spi-plugins:
    - maven:groupId,artifactId,version

# OSS / 摆渡桶
    - oss:groupId,artifactId,version

# 本地文件
    - file:/absolute/path/to/spi.jar
```

### 5.3 Super SPI 部署

Super SPI 走客开管理式打包，不需要 `seeyon.spi.spi-plugins`。

## 6. 测试规范

"真实测试"不是文件存在检查。测试要构造真实接口 DTO 并调用实现方法。

最低要求：

- happy path 返回 DTO。
- 缺必填参数抛错。
- 签名/票据/加密失败路径。
- 配置字段解析。
- 域特有校验（如免登五字段唯一）。

如果平台 API jar 不在本机，允许先做静态质量验证，但必须明确写出：完整 `mvn test` 依赖现场提供 Maven 坐标或 jar。

## 7. 交付物清单

每个 SPI module 至少包含：

| 文件 | 必须 | 说明 |
|------|------|------|
| `src/main/java/.../*Impl.java` | ✅ | 实现类 |
| `src/main/resources/META-INF/spring.factories` | ✅ | SPI 注册 |
| `src/main/resources/metadata/spi_info.json` | Super SPI | 旧 SPI 不必须 |
| `src/main/resources/nacos/*.yaml` | ✅ | Nacos 配置样例 |
| `docs/API_AND_CONFIG.md` | ✅ | 接口与配置说明 |
| `src/test/java/.../*Test.java` | ✅ | 真实测试 |
| `README.md` | ✅ | 场景说明 |

## 8. 索取清单模板

每个域启动时，向用户输出标准索取清单：

```
P0（阻塞生成）:
1. {接口FQCN} 完整反编译源码（方法签名、泛型、异常、注解）
2. {DTO FQCN} 完整反编译源码（字段、父类、枚举）
3. spring.factories 注册示例

P1（影响质量）:
4. 示例实现类（官方 demo 或现场已跑通代码）
5. Nacos 配置 key 和示例值
6. POM 依赖坐标和版本

P2（影响部署）:
7. 重启服务范围
8. 私服类型（minio/nexus）和 jar 上传状态
9. 目标环境版本号
```

## 9. 文档结构规范

每个域目录结构：

```
{domain}/
├── index.md           ← 纯导航：子场景路由表 + scope + 重启服务
├── constraints.md     ← 域独有约束（注解、DTO 规则、禁止项）
├── {scene-1}.md       ← 子场景 1（完整接口 + 代码骨架 + Nacos + 注册）
├── {scene-2}.md       ← 子场景 2
└── ...
```

`index.md` 只做路由，不塞实现细节。具体知识在子场景文件中。

## 10. 生成器规则

1. 缺业务信息不阻塞模板生成；在报告里列为"业务待填配置"。
2. 业务差异做成可配置模板，不写死单一业务。
3. 不确定字段不要编；标 `TODO` 或 `CHANGE_ME`。
4. 生成后必须跑静态验证。


---

## 附录：官方 SPI 开发与部署规范

> 来源：致远 V8 SPI 开发说明文档（已并入公共约束附录）

# SPI 开发与部署规范 [FACT ✅ 官方文档]

> 来源：致远 V8 SPI 开发说明文档

---

## 1. spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["spi-app-name"]
}
```

- `name`: 固定值 `boot-starter-spi-customized`，请勿修改
- `scopes`: SPI 组件的适配范围
  - `ALL` — 针对所有应用
  - `ctp-user` — 仅 ctp-user 微服务（模式 A/B）
  - `cip-connector` — 仅 cip-connector 微服务（模式 C）
  - 其他具体应用 code

**多模块项目：** module 会被编译成一个 SPI jar，spi_info.json 只需 scopes：
```json
{
  "scopes": ["spi-app-name"]
}
```

## 2. spring.factories

```
com.seeyon.cip.connector.api.sso.SsoService=\
com.seeyon.extend.spi.sso.TemplateSsoServiceImpl
```

格式：`api包里面的接口全路径=手写实现代码的全路径`

### 各模式对应的接口全路径

| 模式 | 接口全路径 |
|------|-----------|
| A: V8认证 | `com.seeyon.ctp.user.api.sso.CtpUserSsoAuthProviderService` |
| B: 三方→V8 无中间页 | `com.seeyon.ctp.user.api.avoidlogin.CtpAvoidLoginClientModeProviderService` |
| B: 三方→V8 有中间页 | `com.seeyon.ctp.user.api.avoidlogin.CtpAvoidLoginMiddlePageProviderService` |
| B: 后端直接免登 | `com.seeyon.ctp.user.api.avoidlogin.CtpAvoidLoginBackendProviderService` |
| C: V8→三方 | `com.seeyon.cip.connector.api.sso.SsoService` |

## 3. 三方 jar 依赖

三方依赖统一走 Maven dependency。

- Maven/私服已有：直接在对应模块 POM 写 `<dependency>`
- 只有 jar 文件：统一放到根目录 `/third-jar` 暂存，然后执行 `mvn install:install-file` 或 deploy 到私服，最后仍用 Maven 坐标引用
- 禁止生成 `/lib` 目录
- 默认禁止 `systemPath`；只有客开平台或客户环境强制要求 jar 随包时，才允许对模块 root `third-jar/` 例外引用，并在 Health Check 标 WARN

示例：
```bash
mvn install:install-file \
  -Dfile=third-jar/vendor-sdk-1.0.0.jar \
  -DgroupId=com.vendor \
  -DartifactId=vendor-sdk \
  -Dversion=1.0.0 \
  -Dpackaging=jar
```

```xml
<dependency>
    <groupId>com.vendor</groupId>
    <artifactId>vendor-sdk</artifactId>
    <version>1.0.0</version>
</dependency>
```

## 4. 多模块项目

一个 Super SPI 工程可以包含多个 SPI 子域 module，每个业务 module 编译成独立 SPI jar；公共代码统一进入 `spi-common`。

```
custom-backend/
├── pom.xml                    # 父 POM (packaging: pom)
├── third-jar/                 # 本地/私有三方 jar 暂存区
├── spi-common/                # 公共模块，不注册 SPI
│   ├── pom.xml
│   └── src/main/java/...
├── spi-sso/                   # SSO/统一认证模块，融合模式 A/B/C
│   ├── pom.xml
│   ├── src/main/java/...
│   └── src/main/resources/
│       ├── META-INF/spring.factories
│       └── metadata/spi_info.json
└── spi-{domain}/              # 其他 SPI 子域
    ├── pom.xml
    └── ...
```

父 POM 模板：
```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.seeyon</groupId>
        <artifactId>boot</artifactId>
        <version>{v8_version}</version>
    </parent>
    <artifactId>boot-starter-spi-customized</artifactId>
    <version>1.0.0-TEST-SNAPSHOT</version>
    <packaging>pom</packaging>
    <name>custom-backend</name>
    <modules>
        <module>spi-common</module>
        <module>spi-sso</module>
        <module>spi-{domain}</module>
    </modules>
    <properties>
        <platform.version>{platform_version}</platform.version>
    </properties>
</project>
```

## 5. 客开 SPI 限制

### 文件 SPI 扩展

**当前客开通路不支持文件 SPI 扩展。** 文件存储 SPI 需要走独立通路：

#### 方式一：磁盘部署

1. 本地构建打包 jar
2. 上传 jar 到服务器磁盘
3. 修改对应服务的 Nacos 配置：

```yaml
seeyon:
  spi:
    enable: true
  file:
    storage-type: spi
    spiPlugins: 
    - file: /xxx/xxx/xxx.jar
```

4. 重启对应服务

#### 方式二：Nexus Maven 仓库部署

1. 本地构建打包 jar
2. 上传到 Nexus 仓库
3. 修改对应服务的 Nacos 配置：

```yaml
seeyon:
  spi:
    enable: true
  file:
    storage-type: spi
    spiPlugins: 
    - maven:com.seeyon,boot-starter-file-spi,1.0.0
  dynamic:
    loader:
      type: maven
      maven:
        releaseUrl: http://ip:端口/repository/maven-releases/
        snapshotUrl: http://ip:端口/repository/maven-snapshots/
        username: 账号
        password: 密码
```

4. 重启对应服务

## 6. 部署检查清单

### 标准客开通路部署（模式 A/B/C 通用）

1. ✅ 代码打包为 zip（含父 pom.xml、spi-common、业务 spi-*、root third-jar）
2. ✅ 上传到 V8 客开管理平台构建
3. ✅ 配置 Nacos（sm4Key / openApi 等）
4. ✅ 重启对应微服务（ctp-user 或 cip-connector）

### 文件 SPI 独立通路部署

1. ✅ 本地 `mvn clean package -DskipTests`
2. ✅ 上传 jar 到磁盘或 Nexus
3. ✅ 修改 Nacos 中 `seeyon.spi.enable: true` + `seeyon.file.spiPlugins`
4. ✅ 重启对应服务



---

## 附录 A：Auth/SSO 质量门禁

> 原 auth-sso-quality-gate.md

# Auth/SSO SPI 质量门禁：避免生成“玩具模板”

来源：一次 V8 SSO/SPI 模板生成被用户指出不可交付：注释缺失、接口参数没用、实现注解/日志缺失、Nacos 参数缺失、测试只是结构验证。以后凡是生成 Seeyon V8 认证/SSO/SPI 模板，必须把本门禁作为冻结条件。

## 触发场景

- 生成 `CtpAvoidLogin*ProviderService`、`CtpUserSsoAuthProviderService`、`Mobile*ProviderService`、`AbstractLoginQrCodeService` 等实现。
- 生成“一 SPI 一项目”父工程、交付 zip、客开模板、现场测试包。
- 用户要求“真实测试”“可交付”“不是玩具”。

## 必须补齐的交付面

每个 SPI module 至少包含：

1. `src/main/java/.../*ProviderService.java`
2. `src/main/resources/META-INF/spring.factories`
3. `src/main/resources/metadata/spi_info.json`
4. `src/main/resources/nacos/*.yaml`
5. `docs/API_AND_CONFIG.md`
6. `src/test/java/.../*Test.java`
7. `README.md`

`spi-common` 只放公共工具，不注册 SPI。

## 实现代码门禁

实现类必须有：

- 类级 JavaDoc：说明场景、V8 调用时机、三方系统、返回语义。
- 方法 JavaDoc：逐个解释参数、返回值、异常。
- 必要的实现注解/路由注解：例如 `@CtpUserChannelRouter`、`@ConnectorChannelRouter`、`@CtpUserComment`，以目标接口 FACT 为准，不能凭空加。
- SLF4J 日志：入口、关键分支、成功、失败。
- 脱敏：token / secret / sign / code / mobile / email 不得明文落日志。
- 真实使用接口 DTO 字段，而不是只返回空对象或只 set 一个字段。

## 免登 DTO 特别规则

`CtpAvoidLoginUserInfoDto` 的五个唯一匹配字段：

- `thirdUserId`
- `thirdUserCode`
- `thirdMobile`
- `thirdLoginName`
- `thirdUserEmail`

必须“有且只有一个”赋值。模板里应提供 `UserIdentityGuard` 或等价校验，并在测试里覆盖。

`CtpUserSpiAvoidLoginClientModeDto` 不能闲置字段：

- `thirdType` 对应前端 `c`
- `timestamp` 对应 `t`
- `sign` 对应 `s`
- `webUrl` 对应 `w`
- `mobileUrl` 对应 `m`
- `encryptData` 对应 `d`
- `extData` 承载 traceId、clientSecret、identityType、identityValue、tenant 等扩展

客户端直连免登至少测试：有效签名、错误签名、过期时间戳、用户唯一字段。

## Nacos / 配置门禁

每个 SPI 场景必须给出 Nacos 样例和参数说明。至少包含：

```yaml
auth-sso:
  module: example
  enabled: true
  client-id: example-client
  trace-log-enabled: true
  timeout-ms: 5000
  retry-times: 1
  token-url: https://third.example.com/oauth/token
  user-info-url: https://third.example.com/api/userinfo
  client-secret: CHANGE_ME_IN_NACOS
  aes-key: CHANGE_ME_IN_NACOS
  sign-secret: CHANGE_ME_IN_NACOS
  identity-type: thirdUserCode
  tenant-type: code
  tenant-data: default
```

同时在 `docs/API_AND_CONFIG.md` 标明：key、required、sensitive、example、说明。

## 测试门禁

“真实测试”不是文件存在检查。测试要构造真实接口 DTO 并调用实现方法。

最低要求：

- happy path 返回 DTO。
- 缺必填参数抛错。
- 签名/票据失败路径。
- token refresh 或 redirect/tenant 这种接口能力至少覆盖一个。
- Nacos/配置字段解析。
- `CtpAvoidLoginUserInfoDto` 唯一字段校验。

如果平台 API jar 不在本机，允许先做静态质量验证，但必须明确写出：完整 `mvn test` 依赖现场提供 `ctp-user-api` / `cip-connector-api` Maven 坐标或 jar。

## 冻结判断

可以冻结：

- 一 SPI 一 module 结构。
- spring.factories / metadata / nacos / docs / tests 交付形态。
- DTO 使用方式、日志脱敏标准、配置参数标准。

不能冻结：

- 现场 Maven 坐标。
- 真实三方 HTTP 协议字段。
- 未提供 FACT 的 DTO 字段填充。
- 登录前门户等预置 jar 的真实 Nacos key。

## 常见反模式

- 只生成类和 `spring.factories`，没有注释、日志、配置、测试。
- 参数 DTO 收到了但不用，例如不校验 `timestamp/sign/encryptData`。
- 只 set `thirdUserCode(code)`，忽略 tenant、redirect、third token。
- 把结构验证冒充业务测试。
- 因为缺 jar 就声称完成编译验证；正确做法是标明依赖缺口并提供静态门禁报告。


---

## 附录 B：运行模式定义

> 原 runtime-modes.md

# Runtime Modes（运行模式定义）[FACT ✅]

> Rule-003: Deployment Context First — 生成代码前必须先判定运行模式。

---

## 模式判定决策树

```
用户提到 SPI / 客开平台 / 上传 jar / spring.factories / spi_info.json？
  → SUPER_SPI

用户提到多个 SPI / 超级 SPI / 融合多个 SPI？
  → SUPER_SPI

用户提到 SSO / 单点登录 / 免登 / 统一认证？
  → SUPER_SPI + spi-sso

无法判断？
  → 追问
```

---

## SUPER_SPI（统一 SPI 插件工程）

### 运行环境
- 运行在已有 V8 微服务内部（ctp-user 或 cip-connector）
- 控制当前 custom-backend/Super SPI 工程 pom
- 依赖要收敛，避免与平台冲突

### 部署流程
```
开发 → 打包 SPI Jar → 上传客开平台 → Nacos 配置 → 服务动态加载
```

### 依赖来源
- **双查强制规则**：生成、改造或标注 SPI 方法时，两边都要查：子域契约负责 SPI 接口/DTO/枚举/scope；`references/platform-standard-library/index.md` + `references/platform-standard-library/decompiled/` 负责 boot 公共方法。
- **平台通用基础能力**：优先查 `references/platform-standard-library/index.md` 中的 boot FACT allowlist（boot-core / boot-starter-web / boot-starter-spi）。凡是 JSON、HTTP、加密、BeanCopy、Transport Response/Request、RequestContext、BusinessException 等公共 helper，先查这里。
- **子域 SPI 契约包**：如 `ctp-user-api`、`cip-connector-api`、`organization-api`，只放在对应 `spi-{domain}` 子模块中，不作为 `spi-common` 公共方法来源。
- **三方依赖**：优先 Maven 坐标；本地/私有 jar 只作为 `third-jar/` 暂存，install/deploy 后再按 dependency 引用。

### 禁止
- `@Autowired` / `@Component` / `@Service` / `@Configuration`（不在 Spring 容器）
- `@RestController`（不是独立服务）
- `java.sql.*` / `javax.persistence.*`（不允许直接操作数据库）
- `org.springframework.data.redis.*`（不允许直接操作 Redis）
- `com.seeyon.ctp.user.service/dao/mapper.*`（不允许访问内部层）
- 把 `ctp-user-api` / `cip-connector-api` 的 helper 当成全局公共 helper 写进 `spi-common`

### 允许（按证据边界）
- boot 通用能力：按 `references/platform-standard-library/index.md` 的 FACT 签名使用。
- 子域契约能力：只在目标子域 README/contract 已 FACT 时使用，例如 SSO 模块里的 ctp-user 相关接口/工具；不得提升为全局规则。

### 文件结构
```
custom-backend/
├── pom.xml
├── third-jar/
├── spi-common/
│   ├── pom.xml
│   └── src/main/java/...
├── spi-sso/
│   ├── pom.xml
│   ├── src/main/java/...
│   └── src/main/resources/
│       ├── META-INF/spring.factories
│       └── metadata/spi_info.json
└── spi-{domain}/
```

### 谨慎使用的依赖
- guava（可能和平台版本冲突）
- fastjson（可能和平台版本冲突）
- jackson 新版（可能和平台版本冲突）

---

## CUSTOM_BRAND / 独立服务

当前 skill 不生成独立 Spring Boot 服务。用户明确要独立服务时，应说明这不属于本 Super SPI 生成格式，除非后续另建 skill/项目。

---

## 模式对比表

| 特性 | SUPER_SPI 统一格式 |
|------|-------------------|
| 运行环境 | V8 微服务内部 |
| 依赖管理 | Maven dependency；root `third-jar/` 仅作本地/私有 jar 暂存 |
| Spring 注解 | 禁止 @Autowired 等 |
| 工具类 | boot FACT allowlist 优先；子域契约 helper 只在对应子域 FACT 后使用 |
| 配置文件 | Nacos |
| 部署方式 | 上传客开平台或 SPI jar 部署 |
| spring.factories | 业务 SPI 模块必须；spi-common 禁止 |
| spi_info.json | 业务 SPI 模块必须；spi-common 禁止 |
| 重启服务 | ctp-user / cip-connector / 对应 scope 服务 |

---

## SSO 场景下的模式选择

| SSO 模式 | 运行模式 | 说明 |
|----------|---------|------|
| A: 统一认证 / V8 认证登录 | SUPER_SPI + `spi-sso/unifiedauth` | 实现 CtpUserSsoAuthProviderService |
| B: 三方→V8 免登 | SUPER_SPI + `spi-sso/avoidlogin` | 实现 CtpAvoidLogin*ProviderService |
| C: V8→三方单点 | SUPER_SPI + `spi-sso/connector` | 实现 SsoService |
| 多 SPI 融合 | SUPER_SPI | `spi-common` + 多个 `spi-*` 模块 |

**注意：** 当前 skill 以 SSO 为首个子域，但生成格式始终是 SUPER_SPI：
- 模式 A/B/C → 全部进入 `spi-sso` 分包；统一认证固定放 `spi-sso/unifiedauth`
- 公共能力 → `spi-common`
- 如果用户明确说"独立部署" → 不使用本 skill 生成，说明需另建独立 Spring Boot 项目


---

## 附录 C：SPI 开发准备

> 原 spi-development-preparation.md

# SPI 开发准备 / 客开工程前置规则

> 来源：语雀 rendered-md `0002-开发准备-fqdmdrodt7x7p6no.md`。
> Source: https://www.yuque.com/seeyonkk/v8/fqdmdrodt7x7p6no
> Evidence：OBSERVATION ⚠️（语雀 rendered-md）。
>
> 用途：所有 SPI 开发/生成/改造前先读本文，确认工程结构、注册文件、scope、三方依赖、构建与重启规则。接口/方法签名仍以现场源码、jar、反编译结果为 FACT。

## 1. 触发条件

任一场景涉及 SPI 开发时，先加载本文件：

- 生成新的 `custom-backend` / Super SPI 工程
- 新增 `spi-sso` / `spi-mq` / `spi-system-variable` / 其他 SPI 子模块
- 修改已有 SPI 工程
- 处理 `spring.factories` / `spi_info.json` / `third-jar` / Maven 依赖
- 讨论构建、部署、重启、生效范围

## 2. 后端 SPI 工程来源

语雀“开发准备”描述的入口：

```text
开发环境 -> system-admin 登录后台 -> 系统管理 -> 客开管理
```

在客开管理中获取：

- GitLab 工程名称
- GitLab 工程地址
- Maven `settings.xml`
- 构建入口/构建日志

## 3. 标准工程结构观察

语雀截图/OCR 中的后端扩展工程要点：

```text
custom-backend/
├── pom.xml                 # 后端代码父级工程
├── third-jar/              # 第三方 jar 暂存位置，不是 lib/
├── spi-sso/
├── spi-workflow/
├── spi-file/
├── spi-mobile/
└── ...                     # 一个 module 对应一个 SPI 子工程
```

子模块典型结构：

```text
spi-xxx/
├── pom.xml
└── src/main/resources/
    ├── META-INF/spring.factories
    └── metadata/spi_info.json
```

工程规则：

1. 一个 module 对应一个 SPI 子域/子工程。
2. 新增 SPI 子工程必须加入父级 POM `<modules>`。
3. 第三方 JAR 可放 `third-jar/` 作为现场暂存/上传材料；生成默认 POM 不使用 `scope=system` / `systemPath`。只有用户明确要求兼容旧现场格式时才保留，并在交付报告中标为部署风险；若现场已给 Maven 坐标或私服可用，必须优先 Maven dependency。
4. `spi-common` 这类公共模块不是 SPI，不放 `spring.factories` 和 `spi_info.json`。

## 4. `spi_info.json` 规则

语雀示例：

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["announcement1492794990099121396", "kekaiguanli7996550270124641378"]
}
```

字段规则：

- `name`：固定值，通常为 `boot-starter-spi-customized`，不要随意修改。
- `scopes`：SPI 生效服务范围。
  - 指定服务：如 `["ctp-user", "kekaiguanli7996550270124641378"]`
  - 所有服务：`["ALL"]`

生成/修改工程时必须根据子域判断 scope：

- MQ：官方文档已沉淀为全系统生效，通常 `scopes: ["ALL"]`，并且部署后重启所有服务。
- SSO/系统变量等：按具体子域部署文档或现场要求确认。

## 5. `spring.factories` 规则

语雀描述：

```text
格式：api包里面的接口全路径=手写实现代码的全路径
```

示例：

```properties
com.seeyon.boot.starter.mq.spi.MQMessageSpi=com.seeyon.ali.rocketmq.AliOnesMqService
```

多行续写可用 properties 标准反斜杠：

```properties
com.seeyon.boot.starter.mq.spi.MQMessageSpi=com.seeyon.ali.rocketmq.AliOnesMqService
```

生成校验：

1. key 必须是 SPI 接口 FQN。
2. value 必须是实现类 FQN。
3. 实现类必须在 Java 源码中存在。
4. 不要把多个不相关 SPI 混到错误子模块。

## 6. 三方依赖与 Maven settings

开发准备文档要求在客开管理下载 Maven `settings.xml` 并在 IDEA 中配置。

生成/交付时要区分：

- `pom.xml` 依赖坐标：工程应声明真实 dependency。
- `settings.xml` / 私服：属于现场构建环境，不应硬编码进 skill。
- `third-jar/`：用于现场三方 JAR 暂存；不等同于推荐 `lib/` 或 `systemPath`。

## 7. 构建与验证

构建入口：

```text
开发环境 -> system-admin -> 系统管理 -> 客开管理 -> 构建
```

验证规则：

1. 后端 SPI 构建好以后，需要重启对应 scope 内的服务才能验证。
2. 如果 `scopes == ["ALL"]`，按全系统影响处理，通常需要重启所有服务。
3. 当前方式不支持文件操作的 `StorageSpi`；文件操作 SPI 需要打成 jar 后在 Nacos 中配置。
4. SPI 代码中不能使用 `@Autowired`。
5. 获取 bean 只能通过类似 `Apps.getBeanFactory().getBean(...)` 的方式；具体 FQN/方法以现场 Contract 为准。

## 8. 生产环境导入

语雀描述：

```text
生产环境 -> system-admin -> 系统管理 -> 客开管理
```

注意：

- 导入后端扩展后，需要重启 SPI 作用域内的服务才能验证。
- 导入前端扩展后，通常导入成功、前台刷新即可生效。

## 9. 对生成器/Agent 的硬约束

1. 所有 SPI 生成任务先确认：接口 FQN、实现类 FQN、`spring.factories`、`spi_info.json`、父 POM module。
2. 所有 SPI 代码禁止默认使用 `@Autowired` / `@Service` / `@Component`。
3. 所有三方依赖优先走 Maven 坐标；仅现场明确时使用 `third-jar/`。
4. 所有部署说明必须写清楚 scope 与重启范围。
5. 语雀开发准备是 OBSERVATION，不覆盖现场源码/jar/反编译 FACT。


---

## 附录 D：Super SPI 统一工程结构

> 统一 Super SPI 工程结构附录

# Super SPI 统一工程结构

> 生成格式唯一来源。SSO 只是 `spi-sso` 子域，未来多个 SPI 通过 `spi-common` 融合。

## 唯一目录结构

可见模板目录：``。

```
custom-backend/
├── pom.xml
├── README.md
├── third-jar/
│   └── README.md
├── spi-common/
│   ├── pom.xml
│   └── src/main/java/com/seeyon/extend/spi/common/
│       ├── config/
│       ├── crypto/
│       ├── http/
│       ├── json/
│       └── util/
├── spi-sso/
│   ├── pom.xml
│   ├── src/main/java/com/seeyon/extend/spi/sso/
│   │   ├── unifiedauth/    # 统一认证 / 登录页接统一认证中心（模式 A）
│   │   ├── avoidlogin/     # 三方 → V8 免登（模式 B）
│   │   ├── connector/      # V8 → 三方单点（模式 C）
│   │   └── support/
│   └── src/main/resources/
│       ├── META-INF/spring.factories
│       └── metadata/spi_info.json
└── spi-{domain}/
```

## 模块职责

SSO 详细导航见：`references/auth-sso/index.md`。

- `spi-common`: 公共代码模块，不注册 SPI，不放 `spring.factories`，不放 `spi_info.json`。
- `spi-sso`: SSO/统一认证唯一落点，模式 A/B/C 在模块内分包。
  - `unifiedauth/`: 统一认证，登录页接统一认证中心，V8 认证登录扩展。
  - `avoidlogin/`: 三方系统登录后免登进入 V8。
  - `connector/`: V8 菜单/入口单点到三方系统。
- `spi-{domain}`: 后续新增其他 SPI 子域，如移动端、连接器扩展、消息等。
- `third-jar`: 本地/私有三方 jar 暂存区，不是 `lib/`。优先 install/deploy 成 Maven 坐标后在 POM 引用；若现场语雀/客开工程明确要求，可按 `scope=system` + `systemPath=${project.basedir}/../third-jar/XXXX.jar` 引用，必须保持 jar 放在根 `third-jar/`。

## 禁止

- 禁止生成 `lib/`。
- 禁止生成独立 system-scope 平台 API 项目。
- 禁止把 SSO/统一认证拆成多个 `spi-sso-*` 模块。
- 禁止在 `spi-common` 中注册 SPI。

## 依赖规则

- 父 POM 放平台通用依赖/公共运行时能力（例如目标版本 FACT 存在的 `boot-starter-web`、`boot-starter-spi`）。
- 子 SPI 模块只放对应 SPI 域契约包（例如 SSO 模块的 `ctp-user-api`）和本工程模块依赖（例如 `spi-common`）。
- 平台 boot parent 版本、平台通用 starter 版本、SPI 契约包版本可能不同，必须分别参数化；不要把 boot 版本强行套给 `ctp-user-api` / `cip-connector-api` 等契约包。
- 不要凭名称臆造 starter。已验证反例：本地仓库存在 `boot-starter-spi`，但没有命中 `boot-starter-spi-common` 时，应改用真实存在的 starter。
- 如果 `boot-core` 已提供公共工具（如 `com.seeyon.boot.util.http.HttpClientUtil`、`com.seeyon.boot.util.encrypt.SM4Utils`），优先复用平台 FACT，避免在 SPI 工程里额外引入 Hutool HTTP/crypto、BouncyCastle、Lombok 等可冲突依赖。
- 平台 API: `ctp-user-api` / `cip-connector-api` 通过 Maven dependency 引用。
- 公共代码: 业务模块依赖 `spi-common`。
- 私有 jar: 先 `mvn install:install-file` 或 deploy 到私服，再按坐标引用。

