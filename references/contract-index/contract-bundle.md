# Contract Bundle（完整契约包）

> **SPI 不止有接口。Contract Discovery 应该提取完整的开发契约，包括资源文件、配置项、注解、依赖、启动钩子。**

## Bundle 结构

```yaml
contract_bundle:

  # 1. 接口层
  interfaces:
    - fqn: com.seeyon.ctp.user.api.sso.CtpUserSsoAuthProviderService
      type: spi_interface
      methods: [...]

  # 2. DTO / 数据对象
  dtos:
    - fqn: com.seeyon.ctp.user.dto.CtpUserSpiLoginUserInfoDto
      fields: [ctpUserSpiUserDtoList, thirdToken, thirdTokenConfigMap]
    - fqn: com.seeyon.ctp.user.dto.CtpUserSpiUserDto
      fields: [id, loginName, code, name]
    - fqn: com.seeyon.ctp.user.dto.CtpUserSpiServerEnvDto
      fields: [serverDomain, frontBaseRoute]

  # 3. 枚举
  enums:
    - fqn: com.seeyon.ctp.user.enums.CtpUserSpiAuthTokenEnum
      values: [USERNAME_PASSWORD, SPI_SSO, ...]
    - fqn: com.seeyon.ctp.user.enums.ShortLinkModeEnum
      values: [...]

  # 4. 异常
  exceptions:
    - fqn: com.seeyon.ctp.user.exception.CtpUserSpiSsoException
      constructors:
        - (String message)
        - (String message, String errorPageUrl)
      supports_error_page: true
    - fqn: com.seeyon.ctp.user.exception.SpiAuthContinueException
      purpose: 认证继续（多步认证场景）

  # 5. 注解
  annotations:
    - fqn: com.seeyon.ctp.user.annotation.CtpUserChannelRouter
      target: TYPE
      value: String  # 认证渠道标识
      required_for: [模式 A]
    - fqn: com.seeyon.ctp.user.annotation.CtpUserComment
      target: [METHOD, TYPE]
      value: String  # 方法说明
      required_for: []  # 可选

  # 6. 工具类（平台提供，SPI 代码可直接使用）
  utilities:
    - fqn: com.seeyon.ctp.user.util.CtpUserSpiUtils
      methods:
        - name: getInstance
          signature: "<T> T getInstance(Class<T> clazz)"
          purpose: 获取 Bean 实例（替代 @Autowired）
        - name: getRequest
          signature: "HttpServletRequest getRequest()"
          purpose: 获取当前 HTTP 请求
        - name: getPropertyByName
          signature: "String getPropertyByName(String key)"
          purpose: 获取 Nacos 配置值

  # 7. 资源文件
  resources:
    - path: META-INF/spring.factories
      format: properties
      template: |
        {interface_fqn}=\
        {impl_fqn}
      required: true

    - path: metadata/spi_info.json
      format: json
      template: |
        {
          "name": "boot-starter-spi-customized",
          "scopes": ["{scope}"]
        }
      required: true
      notes:
        - name 字段固定值，不可修改
        - scopes 决定 SPI 作用范围

  # 8. 配置项（Nacos）
  config_keys:
    mode_a:
      required:
        - key: seeyon.auth.type
          value: spisso
          purpose: 开启 SPI 认证（固定值）
        - key: seeyon.thirdauth.type
          value: "{channel_type}"
          purpose: 对应 @CtpUserChannelRouter 值
      optional:
        - key: seeyon.{project_id}.clientId
          purpose: 三方应用 ID
        - key: seeyon.{project_id}.clientSecret
          purpose: 三方应用密钥

    mode_b:
      required: []
      optional:
        - key: seeyon.thirdauth.clientId
          purpose: 三方认证 clientId
        - key: seeyon.thirdauth.clientSecret
          purpose: 三方认证 clientSecret
        - key: seeyon.openApi.appKey
          purpose: V8 OpenAPI appKey
        - key: seeyon.openApi.appSecret
          purpose: V8 OpenAPI appSecret
        - key: seeyon.openApi.domain
          purpose: V8 OpenAPI 域名
        - key: seeyon.system.domain
          purpose: V8 域名
        - key: seeyon.system.protocol
          purpose: V8 协议（http/https）
        - key: seeyon.avoid.clearCookieTypes
          purpose: 多账号切换 cookie 类型

    mode_c:
      required: []
      optional:
        - key: seeyon.{project_id}.*
          purpose: 项目特有配置（如 RSA 公钥）

  # 9. 依赖
  dependencies:
    mode_a:
      - groupId: com.seeyon
        artifactId: ctp-user-api
        version: "${platform.version}"
        scope: compile  # 或 system
      - groupId: com.seeyon
        artifactId: ctp-user-facade
        version: "3.8.13"
        confidence: medium
        source: [项目观察 A pom.xml]
    mode_b:
      - groupId: com.seeyon
        artifactId: ctp-user-api
        version: "${platform.version}"
    mode_c:
      - groupId: com.seeyon
        artifactId: cip-connector-api
        version: "${platform.version}"
    common:
      - groupId: org.projectlombok
        artifactId: lombok
        version: "1.18.36"
        scope: provided
      - groupId: cn.hutool
        artifactId: hutool-all
        version: "5.8.28"
        confidence: medium
        source: [项目观察 A pom.xml]
      - groupId: javax.servlet
        artifactId: javax.servlet-api
        version: "4.0.1"
        scope: provided

  # 10. 启动钩子 / 生命周期
  startup_hooks:
    - event: spi_loaded
      description: SPI jar 被加载时
      action: 重启对应微服务（ctp-user 或 cip-connector）
    - event: setServerEnv_called
      description: 模式 A 中平台调用 setServerEnv
      action: 保存 serverDomain 和 frontBaseRoute
    - event: build_complete
      description: 构建完成后
      action: 通过客开管理平台部署或手动上传 jar

  # 11. 限制 / 约束
  constraints:
    - id: no_autowired
      description: SPI 代码中不能使用 @Autowired
      reason: SPI 类不在 Spring 容器管理范围内
      alternative: CtpUserSpiUtils.getInstance() 或 App.getFactory().getBean()
    - id: no_file_spi
      description: 客开 SPI 通路不支持文件 SPI 扩展
      alternative: 文件 SPI 需要打 jar 在 Nacos 中配置
    - id: restart_required
      description: 构建后必须重启对应微服务
      reason: SPI 在启动时加载，热部署不支持
    - id: max_description_length
      description: spi_info.json 中 name 固定为 boot-starter-spi-customized
      reason: 平台硬编码检查
```

## Bundle 提取流程

```
输入: jar 文件 / 源码目录
    ↓
1. 扫描 interfaces（api 包下的 Service 接口）
    ↓
2. 扫描 dtos（dto 包下的数据类）
    ↓
3. 扫描 enums（enums 包下的枚举）
    ↓
4. 扫描 exceptions（exception 包下的异常类）
    ↓
5. 扫描 annotations（annotation 包下的注解）
    ↓
6. 扫描 utilities（util 包下的工具类）
    ↓
7. 从项目模板推断 resources / config_keys / dependencies
    ↓
8. 从文档/经验推断 startup_hooks / constraints
    ↓
输出: contract_bundle (YAML)
```

## Bundle 与 Normalization 的关系

```
Contract Discovery
    ↓ 提取
Contract Bundle（完整契约包）
    ↓ 归一化
Normalized Contract（统一模型）
    ↓ 匹配
Strategy（认证策略）
    ↓ 生成
Code + Config + Deploy Guide
```

Bundle 是"全量信息"，Normalization 是"核心抽象"。
Strategy 用 Normalization 做决策，用 Bundle 填充细节。
