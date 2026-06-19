# V8 版本兼容矩阵

> ⚠️ **本文件所有数据均来自项目观察，非官方文档。confidence 标注可信度。**
> **如果用户提供 jar 文件，优先走 Contract Discovery，不依赖本文件。**

## 版本映射表

### 5.2.x

```yaml
parent.boot.version: 5.2.1
platform.version: 5.2.1
ctp-user-api: 5.2.4
cip-connector-api: 5.2.4

confidence: medium
source:
  - 项目观察 B parent pom.xml (boot 5.2.1)
  - 项目观察 B spi-avoid-ca pom.xml (platform.version 5.2.4)
  - 项目观察 B spi-sso pom.xml (platform.version 5.2.4)

notes:
  - ctp-user-api 在模块中直接用 ${platform.version}，不需要 system scope
  - platform.version 与 boot.version 不同（5.2.1 vs 5.2.4）

verify_required: true
```

### 5.3.x（≤5.3.200）

```yaml
parent.boot.version: 5.3.200  # 推测
platform.version: 3.10.1
ctp-user-api: 5.3.200  # 推测
cip-connector-api: 3.10.1

confidence: low
source:
  - 无直接项目证据
  - 从 5.3.293 行反推

notes:
  - platform.version 从 5.x 跳到 3.x（原因不明）
  - 具体版本号需要实际项目验证

verify_required: true
```

### 5.3.x（>5.3.200，含 SP1/SP2）

```yaml
parent.boot.version: 5.3.293
platform.version: 3.10.1
ctp-user-api: 5.3.351
cip-connector-api: 3.10.1

confidence: high
source:
  - custom-backend-1.0.zip parent pom.xml (boot 5.3.293, platform 3.10.1)
  - 项目观察 A pom.xml (历史观察：ctp-user-api 5.3.351 曾用 system scope)
  - 用户提供的 ctp-user-api-5.3.351.jar

notes:
  - 这是目前证据最充分的版本行
  - 新生成工程统一使用 Maven 仓库/私服依赖；不再生成 lib/ 或独立 system-scope 项目
  - cip-connector-api 用 ${platform.version}

verify_required: false
```

### 5.3 SP3 / SP4

```yaml
parent.boot.version: 待确认
platform.version: 待确认
ctp-user-api: 待确认
cip-connector-api: 待确认

confidence: none
source: []

notes:
  - 无任何项目证据
  - 必须用户提供具体版本号或 jar 文件

verify_required: true
```

## 接口变更观察记录

> 以下均为观察结果，非官方 changelog。

### innerUserLoginName 修复

```yaml
observed_in: 5.3.293+
description: |
  低版本 innerUserLoginName 与 innerUserCODE 值相同（bug）。
  5.3.330 版本已修复（来源：DOCX 文档中 SsoService 接口注释）。
confidence: medium
source:
  - DOCX 知识库中 SsoService 接口注释原文：
    "innerUserLoginName: 内部用户登录名(低版本有bug，低版本这个值和innerUserCODE是一样的，26年330版本已经修复)"
verify_required: false
```

### refreshThirdTokenByConfig 方法

```yaml
observed_in: ctp-user-api-5.3.351.jar
description: |
  CtpUserSsoAuthProviderService 接口中存在此方法（default 实现）。
  旧版本可能只有 refreshThirdToken（已 @Deprecated）。
confidence: high
source:
  - paste_1_111544.txt（ctp-user-api-5.3.351.jar 反编译结果）
  - 接口原文：
    @Deprecated default CtpUserSpiThirdTokenDto refreshThirdToken(...)
    default CtpUserSpiThirdTokenDto refreshThirdTokenByConfig(...)
verify_required: false
```

### CtpAvoidLoginUserInfoDto Builder 模式

```yaml
observed_in: 5.3.x 项目代码
description: |
  CtpAvoidLoginUserInfoDto.builder() 在项目观察 B中使用。
  5.2.x 项目未使用（可能不支持）。
confidence: medium
source:
  - 中核 spi-avoid-xrtx: XrtxSsoAvoidMiddlePageProviderService.java
    使用 CtpAvoidLoginUserInfoDto.builder().thirdUserId(...).build()
  - 中核 spi-avoid-ca: CaSsoAvoidMiddlePageProviderService.java
    同样使用 builder 模式
verify_required: true  # 5.2.x 是否支持未确认
```

### CtpUserSpiUtils.getInstance() / getPropertyByName()

```yaml
observed_in: 所有项目
description: |
  SPI 代码中获取 Bean 和 Nacos 配置的标准方式。
  所有观察到的项目都使用此方式，无例外。
confidence: high
source:
  - 项目观察 A: CHNsSsoAuthConstants.java
  - 项目观察 B: CaSsoAvoidConstants.java, XrtxSsoAvoidConstants.java
  - DOCX 知识库多处提及
verify_required: false
```

## POM 生成规则

### Super SPI 模块项目（唯一生成格式）

```xml
<!-- 模式 A/B: ctp-user-api -->
<dependency>
    <groupId>com.seeyon</groupId>
    <artifactId>ctp-user-api</artifactId>
    <version>${platform.version}</version>
</dependency>

<!-- 模式 C: cip-connector-api -->
<dependency>
    <groupId>com.seeyon</groupId>
    <artifactId>cip-connector-api</artifactId>
    <version>${platform.version}</version>
</dependency>
```

### 禁止生成的格式

不再生成独立 `lib/` + `systemPath` 项目。即使用户提供本地 API jar，也只用于 Contract Discovery；代码工程仍按 Super SPI Maven 多模块输出。

## 版本验证清单

生成代码后检查：

- [ ] parent.boot.version 与用户提供的 V8 版本匹配（或 jar 文件名匹配）
- [ ] platform.version 与版本矩阵一致（注意 confidence 级别）
- [ ] 如果 confidence: low/none，在代码注释中标注"版本号需验证"
- [ ] 如果用户提供了 jar，优先用 jar 中的接口签名（Contract Discovery）
