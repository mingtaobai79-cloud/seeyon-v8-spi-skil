# Contract Normalization（接口契约归一化）

> **将不同命名、不同风格的 SPI 接口统一归一化为标准结构，使 Strategy 层只面对统一模型。**

## 为什么需要 Normalization

不同厂商、不同版本的 SPI 接口命名差异巨大：

```java
// 厂商 A
User login(String token);

// 厂商 B
AuthInfo auth(HttpServletRequest request);

// 厂商 C
Result<UserDTO> authenticate(Map<String,Object> params);
```

如果 Strategy 层直接面对原始接口，每增加一个厂商就要写一套适配。
归一化后，Strategy 只面对统一结构。

## 归一化模型（Normalized Contract）

```yaml
normalized_contract:

  # 认证方法（统一命名）
  auth_method:
    name: authenticate          # 统一名称
    original_name: getUserLoginInfo  # 原始方法名
    original_interface: CtpUserSsoAuthProviderService

  # 输入（统一分类）
  input:
    type: http_request          # http_request | token_string | credential_pair | encrypted_param | config_map
    original_params:
      - name: request
        type: HttpServletRequest
      - name: encodeRedirectUrl
        type: String

  # 输出（统一分类）
  output:
    type: user_info             # user_info | redirect_url | token_string | void
    original_return: CtpUserSpiLoginUserInfoDto
    user_fields:                # 输出中可用于匹配用户的字段
      - loginName
      - userId
      - code

  # 异常（统一分类）
  exception:
    type: auth_exception        # auth_exception | validation_exception | system_exception
    original_class: CtpUserSpiSsoException
    supports_error_page: true   # 是否支持自定义错误页

  # 注册（统一分类）
  registration:
    type: spring_factories      # spring_factories | spi_descriptor | annotation_scan
    factory_key: com.seeyon.ctp.user.api.sso.CtpUserSsoAuthProviderService

  # 配置（统一分类）
  config:
    type: nacos                 # nacos | properties | yaml | env
    keys: []                    # 运行时填充
```

## 归一化规则

### Input Type 判定

| 原始参数模式 | 归一化为 |
|-------------|---------|
| `HttpServletRequest` + `String` | `http_request` |
| `String token` / `String code` | `token_string` |
| `String username, String password` | `credential_pair` |
| `Map<String, Object>` | `config_map` |
| DTO 对象（如 `CtpUserSpiAvoidLoginClientModeDto`） | `dto_wrapper`（内部字段再分析） |

### Output Type 判定

| 原始返回类型 | 归一化为 |
|-------------|---------|
| 包含 user/login/member 字段的 DTO | `user_info` |
| `String`（URL） | `redirect_url` |
| `String`（token） | `token_string` |
| `void` | `void` |
| `Map<String, Object>` | `config_map` |

### Exception Type 判定

| 原始异常 | 归一化为 |
|---------|---------|
| 名称含 Sso/Auth/Login | `auth_exception` |
| 名称含 Valid/Check/Pre | `validation_exception` |
| 其他 | `system_exception` |

## 归一化流程

```
Raw Contract (from Discovery)
    ↓
1. 提取所有 required 方法
    ↓
2. 对每个方法：
   a. 分析参数 → 判定 input.type
   b. 分析返回值 → 判定 output.type
   c. 分析 throws → 判定 exception.type
    ↓
3. 识别"核心认证方法"（通常是返回 user_info 的那个）
    ↓
4. 填充 normalized_contract
    ↓
5. Strategy 层基于 normalized_contract 生成代码
```

## 核心认证方法识别

从多个 required 方法中识别"核心认证方法"的规则：

1. 返回类型包含 user/login/member 信息 → 优先
2. 参数包含 HttpServletRequest → 优先（说明需要从请求中提取信息）
3. 方法名包含 login/auth/getUser → 优先
4. 如果多个方法都匹配，取参数最多的那个

## 归一化示例

### V8 模式 A

```yaml
# 原始
interface: CtpUserSsoAuthProviderService
required_methods:
  - getRequestParaKey(): String
  - getSsoLoginUrl(HttpServletRequest, String): String
  - getUserLoginInfo(HttpServletRequest, String): CtpUserSpiLoginUserInfoDto

# 归一化
normalized_contract:
  auth_method:
    name: authenticate
    original_name: getUserLoginInfo
  input:
    type: http_request
  output:
    type: user_info
    original_return: CtpUserSpiLoginUserInfoDto
    user_fields: [loginName, userId, code]
  exception:
    type: auth_exception
    original_class: CtpUserSpiSsoException
    supports_error_page: true
  auxiliary_methods:
    - name: get_request_key
      original_name: getRequestParaKey
      purpose: 声明 token 参数名
    - name: build_login_url
      original_name: getSsoLoginUrl
      purpose: 构建三方登录 URL
```

### V8 模式 B（ClientMode）

```yaml
# 原始
interface: CtpAvoidLoginClientModeProviderService
required_methods:
  - getClientId(): String
  - preCheck(CtpUserSpiAvoidLoginClientModeDto): void
  - getUserInfo(CtpUserSpiAvoidLoginClientModeDto): CtpAvoidLoginUserInfoDto

# 归一化
normalized_contract:
  auth_method:
    name: authenticate
    original_name: getUserInfo
  input:
    type: dto_wrapper
    dto_class: CtpUserSpiAvoidLoginClientModeDto
    dto_fields: [extData, code]
  output:
    type: user_info
    original_return: CtpAvoidLoginUserInfoDto
    user_fields: [thirdUserId]
  exception:
    type: auth_exception
    original_class: CtpUserSpiSsoException
    supports_error_page: true
  auxiliary_methods:
    - name: get_client_id
      original_name: getClientId
      purpose: 声明免登标识
    - name: validate
      original_name: preCheck
      purpose: 参数预校验
```

### V8 模式 C

```yaml
# 原始
interface: SsoService
required_methods:
  - getName(): String
  - getTypeCaption(): String
  - login(String, String, Map, SsoClientTypeEnum, Map): String
  - check(String): void
  - getPageJson(): String
  - getSortNo(): Integer
  - needUserBind(): boolean

# 归一化
normalized_contract:
  auth_method:
    name: authenticate
    original_name: login
  input:
    type: config_map
    original_params:
      - { name: url, type: String }
      - { name: json, type: String }
      - { name: userMap, type: "Map<String,Object>" }
      - { name: clientType, type: SsoClientTypeEnum }
      - { name: extendParams, type: "Map<String,Object>" }
  output:
    type: redirect_url
    original_return: String
  exception:
    type: system_exception
    original_class: RuntimeException
    supports_error_page: false
  auxiliary_methods:
    - name: get_name
      original_name: getName
      purpose: 唯一标识
    - name: get_caption
      original_name: getTypeCaption
      purpose: 中文名称
    - name: validate_config
      original_name: check
      purpose: 配置校验
    - name: get_page_json
      original_name: getPageJson
      purpose: 前端配置页面
    - name: need_user_bind
      original_name: needUserBind
      purpose: 是否需要用户绑定
```

## Strategy 层如何使用 Normalized Contract

Strategy 不再关心原始接口叫什么，只关心：

```
normalized_contract.input.type  → 决定如何获取认证凭据
normalized_contract.output.type → 决定如何构建返回值
normalized_contract.exception   → 决定如何处理错误
```

这样新增厂商时，只需：
1. Discovery 提取原始 Contract
2. Normalization 归一化
3. Strategy 基于归一化结果生成代码

不需要为每个厂商写一套适配。
