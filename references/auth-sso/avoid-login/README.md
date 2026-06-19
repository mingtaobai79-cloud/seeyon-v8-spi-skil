# 模式 B：三方 → V8 免登 — SPI 接口完整定义

> **Evidence: FACT ✅** — 接口签名、DTO 来自 `ctp-user-api-5.3.351.jar` 反编译。
> 完整契约包：`../shared/ctp-user-api-contract.md`

## 接口一：CtpAvoidLoginMiddlePageProviderService（中间页免登，无自定义参数）

```java
package com.seeyon.ctp.user.api.avoidlogin;

@CtpUserComment("中间页进行免登")
public interface CtpAvoidLoginMiddlePageProviderService extends CtpSsoAvoidLoginBaseService {

    @CtpUserComment("定制化处理-从请求中提取参数并获取用户信息")
    default CtpAvoidLoginUserInfoDto getUserInfo(String code, Map<String, String> extData) {
        return null;
    }

    @CtpUserComment("自定义查询获取 CtpUser 对象, 通过反射查询用户信息, 返回的必须是 CtpUser 对象")
    default Object getCtpUserInfo(String code, Map<String, String> extData) {
        return null;
    }

    @CtpUserComment("是否周期性刷新 token")
    default Boolean isRefreshTokenCycle() { return false; }

    @CtpUserComment("刷新三方 token")
    default CtpUserSpiThirdTokenDto doRefreshToken(ThirdTokenDto thirdTokenDto) {
        return null;
    }

    @CtpUserComment("扩展信息替换")
    default SpiWebAuthenticationDetailInfo getSpiWebAuthenticationDetailInfo() {
        return null;
    }
}
```

## 接口二：CtpAvoidLoginClientModeProviderService（客户端免登，携带自定义参数）

```java
package com.seeyon.ctp.user.api.avoidlogin;

@CtpUserComment("客户端直接免登")
public interface CtpAvoidLoginClientModeProviderService extends CtpSsoAvoidLoginBaseService {

    @CtpUserComment("参数验证, 如果验证失败，抛出 CtpUserSpiSsoException 异常")
    void preCheck(CtpUserSpiAvoidLoginClientModeDto dto) throws CtpUserSpiSsoException;

    @CtpUserComment("获取用户信息")
    CtpAvoidLoginUserInfoDto getUserInfo(CtpUserSpiAvoidLoginClientModeDto dto);
}
```

## 基类：CtpSsoAvoidLoginBaseService

```java
// 基类提供 getClientId() 方法，子类必须实现
public interface CtpSsoAvoidLoginBaseService {
    String getClientId();
}
```

## 返回值：CtpAvoidLoginUserInfoDto [FACT ✅ jar 反编译]

```java
// 5 个用户标识字段，有且只有一个赋值即可：
//   thirdUserId      → 三方用户 ID
//   thirdUserCode    → 三方用户编码（人员编号/工号）
//   thirdMobile      → 三方用户手机号
//   thirdLoginName   → 三方用户登录名
//   thirdUserEmail   → 三方用户邮箱

// 使用 Builder 模式构建
CtpAvoidLoginUserInfoDto result = CtpAvoidLoginUserInfoDto.builder()
    .thirdUserCode("人员编号")              // 人员编号/工号 → thirdUserCode
    // .thirdUserId("三方用户ID")           // 三方系统内部 ID → thirdUserId
    // .thirdMobile("手机号")               // 手机号 → thirdMobile
    // .thirdLoginName("登录名")            // 登录名 → thirdLoginName
    // .thirdUserEmail("邮箱")              // 邮箱 → thirdUserEmail
    .ctpUserSpiRedirectUrlDto(
        CtpUserSpiRedirectUrlDto.builder()
            .webRedirectUrl("/main/portal")        // PC 端跳转
            .mobileRedirectUrl("/main-mobile/portal") // 移动端跳转
            .build()
    )
    .build();
```

**字段选择指南（⚠️ 必须根据实际用户标识类型选对字段）：**
- 人员编号/工号 → `thirdUserCode`
- 三方系统内部 ID → `thirdUserId`
- 手机号 → `thirdMobile`
- 登录名/账号 → `thirdLoginName`
- 邮箱 → `thirdUserEmail`

## 入参：CtpUserSpiAvoidLoginClientModeDto（ClientMode 专用）

```java
// 可获取的数据
dto.getExtData()    // Map<String, String> 自定义参数
dto.getCode()       // String code
```

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>ctp-user-api</artifactId>
  <version>5.3.351</version>
</dependency>
```

## spring.factories

```properties
com.seeyon.ctp.user.api.avoidlogin.CtpAvoidLoginMiddlePageProviderService=com.seeyon.extend.authsso.avoid.YourAvoidLoginMiddlePageService
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["ctp-user"]
}
```

## 重启服务

ctp-user

## 方法说明

### CtpAvoidLoginMiddlePageProviderService（中间页模式）

| 方法 | 参数 | 返回 | 语义 |
|------|------|------|------|
| getClientId | 无 | `String` | 客户端标识（继承自 CtpSsoAvoidLoginBaseService） |
| getUserInfo | `String code, Map extData` | `CtpAvoidLoginUserInfoDto` | 中间页免登获取用户信息 |
| getCtpUserInfo | `String code, Map extData` | `Object` | 获取用户信息（可选） |
| isRefreshTokenCycle | 无 | `Boolean` | 是否循环刷新 token |
| doRefreshToken | `ThirdTokenDto` | `CtpUserSpiThirdTokenDto` | 刷新 token |
| getSpiWebAuthenticationDetailInfo | 无 | `SpiWebAuthenticationDetailInfo` | 认证详情 |

### CtpAvoidLoginClientModeProviderService（客户端模式）

| 方法 | 参数 | 返回 | 语义 |
|------|------|------|------|
| getClientId | 无 | `String` | 客户端标识 |
| preCheck | `CtpUserSpiAvoidLoginClientModeDto` | void | 预校验（签名/时间戳等） |
| getUserInfo | `CtpUserSpiAvoidLoginClientModeDto` | `CtpAvoidLoginUserInfoDto` | 获取用户信息 |

### CtpAvoidLoginBackendProviderService（后端直接免登）

| 方法 | 参数 | 返回 | 语义 |
|------|------|------|------|
| getClientId | 无 | `String` | 客户端标识 |
| avoidLoginBackend | `HttpServletRequest, HttpServletResponse` | `Object` | 后端直接免登逻辑 |

## 代码骨架（MiddlePage）

```java
package com.seeyon.extend.spi.{project_id};

import com.seeyon.ctp.user.api.avoidlogin.CtpAvoidLoginMiddlePageProviderService;
import com.seeyon.ctp.user.dto.*;
import com.seeyon.ctp.user.exception.CtpUserSpiSsoException;
import com.seeyon.ctp.user.util.CtpUserSpiUtils;
import lombok.extern.slf4j.Slf4j;

import java.util.Map;

@Slf4j
public class {Prefix}AvoidLoginService implements CtpAvoidLoginMiddlePageProviderService {

    @Override
    public String getClientId() {
        return "{third_type}";
    }

    @Override
    public CtpAvoidLoginUserInfoDto getUserInfo(String code, Map<String, String> extData) {
        try {
            log.info("{project_name_cn} 免登, code: {}, extData: {}", code, extData);

            if (code == null || code.isEmpty()) {
                throw new CtpUserSpiSsoException("未获取到认证码",
                    getErrorUrl("CODE_NULL", "未获取到认证码"));
            }

            // 1. 解密/验证 code（如需要）
            String realCode = decryptCode(code);

            // 2. 通过 code 查询用户标识
            String memberId = queryMemberId(realCode);
            if (memberId == null || memberId.isEmpty()) {
                throw new CtpUserSpiSsoException("用户不存在",
                    getErrorUrl("USER_NOT_EXIST", "用户不存在"));
            }

            // 3. 构建返回
            return CtpAvoidLoginUserInfoDto.builder()
                .thirdUserId(memberId)
                .ctpUserSpiRedirectUrlDto(CtpUserSpiRedirectUrlDto.builder()
                    .webRedirectUrl("/main/portal")
                    .mobileRedirectUrl("/main-mobile/portal")
                    .build())
                .build();

        } catch (CtpUserSpiSsoException e) {
            throw e;
        } catch (Exception e) {
            log.error("{project_name_cn} 免登处理异常", e);
            throw new CtpUserSpiSsoException(e.getMessage(),
                getErrorUrl("UNKNOWN_ERROR", "未知错误"));
        }
    }

    private String decryptCode(String code) {
        // TODO: 根据加密方式解密
        // SM2: SM2Utils.decrypt(privateKey, code)
        // AES: AESUtil.decrypt(code, key)
        // RSA: RSAUtil.decrypt(code, privateKey)
        return code;
    }

    private String queryMemberId(String code) {
        // TODO: 调用 V8 OpenAPI 查询用户
        return null;
    }

    private String getErrorUrl(String errorCode, String errorMsg) {
        String domain = CtpUserSpiUtils.getPropertyByName("seeyon.system.protocol")
            + "://" + CtpUserSpiUtils.getPropertyByName("seeyon.system.domain");
        try {
            java.util.HashMap<String, String> map = new java.util.HashMap<>();
            map.put("errorCode", errorCode);
            map.put("errorMsg", errorMsg);
            String encodeParam = java.net.URLEncoder.encode(
                com.seeyon.boot.util.JsonUtils.toJson(map), "UTF-8");
            return domain + "/custom-pages/ssoError.html?error=" + encodeParam;
        } catch (Exception e) {
            return domain + "/custom-pages/ssoError.html";
        }
    }
}
```

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>ctp-user-api</artifactId>
  <version>5.3.351</version>
</dependency>
```

## spring.factories

```properties
com.seeyon.ctp.user.api.avoidlogin.CtpAvoidLoginMiddlePageProviderService=com.seeyon.extend.authsso.avoid.YourAvoidLoginMiddlePageService
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["ctp-user"]
}
```

## 重启服务

ctp-user

## 方法说明

### CtpAvoidLoginMiddlePageProviderService（中间页模式）

| 方法 | 参数 | 返回 | 语义 |
|------|------|------|------|
| getClientId | 无 | `String` | 客户端标识（继承自 CtpSsoAvoidLoginBaseService） |
| getUserInfo | `String code, Map extData` | `CtpAvoidLoginUserInfoDto` | 中间页免登获取用户信息 |
| getCtpUserInfo | `String code, Map extData` | `Object` | 获取用户信息（可选） |
| isRefreshTokenCycle | 无 | `Boolean` | 是否循环刷新 token |
| doRefreshToken | `ThirdTokenDto` | `CtpUserSpiThirdTokenDto` | 刷新 token |
| getSpiWebAuthenticationDetailInfo | 无 | `SpiWebAuthenticationDetailInfo` | 认证详情 |

### CtpAvoidLoginClientModeProviderService（客户端模式）

| 方法 | 参数 | 返回 | 语义 |
|------|------|------|------|
| getClientId | 无 | `String` | 客户端标识 |
| preCheck | `CtpUserSpiAvoidLoginClientModeDto` | void | 预校验（签名/时间戳等） |
| getUserInfo | `CtpUserSpiAvoidLoginClientModeDto` | `CtpAvoidLoginUserInfoDto` | 获取用户信息 |

### CtpAvoidLoginBackendProviderService（后端直接免登）

| 方法 | 参数 | 返回 | 语义 |
|------|------|------|------|
| getClientId | 无 | `String` | 客户端标识 |
| avoidLoginBackend | `HttpServletRequest, HttpServletResponse` | `Object` | 后端直接免登逻辑 |

## 代码骨架（ClientMode）

```java
package com.seeyon.extend.spi.{project_id};

import com.seeyon.ctp.user.api.avoidlogin.CtpAvoidLoginClientModeProviderService;
import com.seeyon.ctp.user.dto.*;
import com.seeyon.ctp.user.exception.CtpUserSpiSsoException;
import com.seeyon.ctp.user.util.CtpUserSpiUtils;
import lombok.extern.slf4j.Slf4j;

import javax.servlet.http.HttpServletRequest;

@Slf4j
public class {Prefix}AvoidLoginService implements CtpAvoidLoginClientModeProviderService {

    @Override
    public String getClientId() {
        return "{third_type}";
    }

    @Override
    public void preCheck(CtpUserSpiAvoidLoginClientModeDto dto) throws CtpUserSpiSsoException {
        // 参数验证
        if (dto.getExtData() == null || dto.getExtData().isEmpty()) {
            throw new CtpUserSpiSsoException("缺少必要参数");
        }
    }

    @Override
    public CtpAvoidLoginUserInfoDto getUserInfo(CtpUserSpiAvoidLoginClientModeDto dto) {
        String webUrl = "/main/portal";
        String mobileUrl = "/main-mobile/portal";
        try {
            HttpServletRequest request = CtpUserSpiUtils.getRequest();
            log.info("{project_name_cn} 免登, extData: {}", dto.getExtData());

            // 1. 从 extData 或 request 获取认证凭据
            String ticket = dto.getExtData().get("{token_param_name}");
            if (ticket == null || ticket.isEmpty()) {
                ticket = request.getParameter("{token_param_name}");
            }
            if (ticket == null || ticket.isEmpty()) {
                throw new CtpUserSpiSsoException("未获取到凭据",
                    getErrorUrl("TICKET_NULL", "未获取到凭据"));
            }

            // 2. 验证凭据
            String userIdentity = verifyTicket(ticket);

            // 3. 查询 V8 用户
            String loginName = queryLoginName(userIdentity);
            if (loginName == null || loginName.isEmpty()) {
                throw new CtpUserSpiSsoException("用户不存在",
                    getErrorUrl("USER_NOT_EXIST", "用户不存在"));
            }

            // 4. 获取自定义跳转地址（如有）
            String service = request.getParameter("service");
            if (service != null && !service.isEmpty()) {
                webUrl = service;
            }
            String redirectUrl = request.getParameter("redirectUrl");
            if (redirectUrl != null && !redirectUrl.isEmpty()) {
                mobileUrl = redirectUrl;
            }

            // 5. 构建返回
            return CtpAvoidLoginUserInfoDto.builder()
                .thirdUserId(loginName)
                .ctpUserSpiRedirectUrlDto(CtpUserSpiRedirectUrlDto.builder()
                    .webRedirectUrl(webUrl)
                    .mobileRedirectUrl(mobileUrl)
                    .build())
                .build();

        } catch (CtpUserSpiSsoException e) {
            throw e;
        } catch (Exception e) {
            log.error("{project_name_cn} 免登处理异常", e);
            throw new CtpUserSpiSsoException(e.getMessage(),
                getErrorUrl("UNKNOWN_ERROR", "未知错误"));
        }
    }

    private String verifyTicket(String ticket) {
        // TODO: 调用三方验证接口
        return "";
    }

    private String queryLoginName(String userIdentity) {
        // TODO: 调用 V8 OpenAPI 查询用户登录名
        return null;
    }

    private String getErrorUrl(String errorCode, String errorMsg) {
        String domain = CtpUserSpiUtils.getPropertyByName("seeyon.system.protocol")
            + "://" + CtpUserSpiUtils.getPropertyByName("seeyon.system.domain");
        try {
            java.util.HashMap<String, String> map = new java.util.HashMap<>();
            map.put("errorCode", errorCode);
            map.put("errorMsg", errorMsg);
            String encodeParam = java.net.URLEncoder.encode(
                com.seeyon.boot.util.JsonUtils.toJson(map), "UTF-8");
            return domain + "/custom-pages/ssoError.html?error=" + encodeParam;
        } catch (Exception e) {
            return domain + "/custom-pages/ssoError.html";
        }
    }
}
```

## 生成器规则：业务差异不要硬问，做成可配置模板

免登生成任务不是为某一个业务写死代码，而是生成可复用模板。以下内容应做成配置项/策略项，不能在生成前反复追问：

1. `getClientId()` / URL `type`：使用参数占位（如 `{third_type}`），集中成常量或 Nacos 配置，业务改一个值即可；不要写具体业务默认值。
2. `dynamicField` / 凭据参数名：默认 `code`，生成代码要支持从 URL `dynamicField` 指定的参数名取值；取不到时再回退 `code` / `ticket` / `token`。
3. code 到用户标识的转换：生成默认策略链，不写死单一业务：
   - `DIRECT`：凭据本身就是用户标识。
   - `HTTP_EXCHANGE`：凭据调用三方接口换用户。
   - `AES` / `SM2` / `SM4` / `RSA`：凭据解密后得到用户标识。
   - `JWT` / `SIGNATURE`：验签/解析后得到用户标识。
4. V8 用户匹配字段：生成成配置项，例如 `matchField=thirdUserCode|thirdLoginName|thirdMobile|thirdUserEmail|thirdUserId`，默认 `thirdUserCode`，运行时按配置选择 DTO 字段；不要把某个业务字段写死在模板里。
5. code 校验：默认做基础校验（非空、长度上限、字符白名单/URL decode、可选时间戳/签名）；强校验按策略配置启用。
6. web/mobile redirect：从 URL 的 `web` / `mobile` 获取并 URL decode；默认只允许站内路径，防开放重定向；缺省回 `/main/portal` 和 `/main-mobile/portal`。

生成代码时，缺业务信息不应阻塞模板生成；只在报告里列为“业务待填配置”。

## SSO 地址组装格式

### 新版三方跳 V8 免登入口（用户现场/语雀示例，优先）

```text
{V8平台访问域名}/oauth/home?
  mobile={urlEncode(移动端重定向地址)}
  &web={urlEncode(Web端重定向地址)}
  &businessType=outsider
  &type={三方系统sso标识}
  &dynamicField={凭据参数名}
  &{凭据参数名}={三方追加的凭据值}
```

示例：

```text
{v8_domain}/oauth/home?mobile={urlEncoded_mobile_redirect}&web={urlEncoded_web_redirect}&businessType=outsider&type={third_type}&dynamicField={credential_param_name}&{credential_param_name}={credential_value}
```

字段对应：
- `type`：三方系统 SSO 标识，应与 `getClientId()` 返回值一致。
- `dynamicField`：追加凭据的参数名，例如 `code` / `ticket`。
- `{凭据参数名}`：三方追加的凭据值。
- `web` / `mobile`：URL encode 后的登录成功重定向地址。

### 旧/兼容免登入口（仅在现场明确使用时采用）

```text
{V8域名}/seeyon/reportLogin.do?sytype={third_type}&syid={标识}&{自定义参数}
```


## Nacos 配置模板

```yaml
# ctp-user 微服务 Nacos 配置
seeyon:
  thirdauth:
    clientId: {third_auth_client_id}
    clientSecret: CHANGE_ME_IN_NACOS
  openApi:
    appKey: {v8_openapi_app_key}
    appSecret: CHANGE_ME_IN_NACOS
    domain: {v8_openapi_domain}
  system:
    domain: {v8_domain}
    protocol: https
  {project_id}:
    # 项目特有配置
    encryptKey: CHANGE_ME_IN_NACOS
  avoid:
    clearCookieTypes:    # 多账号切换
      - {third_type_a}
      - {third_type_b}
```
