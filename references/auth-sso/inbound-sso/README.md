# 三方→V8 免登 / CtpAvoidLogin*ProviderService

> Evidence: FACT ✅ from `references/auth-sso/avoid-login/README.md`（已沉淀完整接口定义）。语雀 `0109-三方单点到V8` 为 OBSERVATION。

## 场景

三方系统携带用户身份令牌访问 V8 免登中间页，V8 通过 SPI 回调识别真实用户。

## 三种模式

| 模式 | 接口 | 适用场景 |
|------|------|----------|
| 中间页免登 | `CtpAvoidLoginMiddlePageProviderService` | 无自定义参数，code 换用户 |
| 客户端免登 | `CtpAvoidLoginClientModeProviderService` | 携带签名/加密数据 |
| 后端免登 | `CtpAvoidLoginBackendProviderService` | 后端 ticket 直连 |

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>ctp-user-api</artifactId>
  <version>3.8.211</version>
</dependency>
```

## 接口一：CtpAvoidLoginMiddlePageProviderService [FACT ✅]

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

## 接口二：CtpAvoidLoginClientModeProviderService [FACT ✅]

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
public interface CtpSsoAvoidLoginBaseService {
    String getClientId();
}
```

## 返回值：CtpAvoidLoginUserInfoDto [FACT ✅]

```java
// 5 个用户标识字段，有且只有一个赋值即可：
//   thirdUserId      → 三方用户 ID
//   thirdUserCode    → 三方用户编码（人员编号/工号）
//   thirdMobile      → 三方用户手机号
//   thirdLoginName   → 三方用户登录名
//   thirdUserEmail   → 三方用户邮箱

CtpAvoidLoginUserInfoDto result = CtpAvoidLoginUserInfoDto.builder()
    .thirdUserCode("人员编号")
    .ctpUserSpiRedirectUrlDto(
        CtpUserSpiRedirectUrlDto.builder()
            .webRedirectUrl("/main/portal")
            .mobileRedirectUrl("/main-mobile/portal")
            .build()
    )
    .build();
```

## 入参：CtpUserSpiAvoidLoginClientModeDto（ClientMode 专用）

```java
dto.getExtData()    // Map<String, String> 自定义参数
dto.getCode()       // String code
dto.getThirdType()  // String 三方标识（对应 URL c）
dto.getTimestamp()  // String 时间戳（对应 URL t）
dto.getSign()       // String 签名（对应 URL s）
dto.getWebUrl()     // String PC 端跳转（对应 URL w）
dto.getMobileUrl()  // String 移动端跳转（对应 URL m）
dto.getEncryptData()// String 加密数据（对应 URL d）
```

## 免登地址格式

### 新版（优先）

```text
{V8域名}/oauth/home?
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

### 旧版（仅在现场明确使用时采用）

```text
{V8域名}/seeyon/reportLogin.do?sytype={third_type}&syid={标识}&{自定义参数}
```

## Nacos 配置

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
    encryptKey: CHANGE_ME_IN_NACOS
  avoid:
    clearCookieTypes:    # 多账号切换
      - {third_type_a}
      - {third_type_b}
```

## spring.factories

```properties
# 中间页免登
com.seeyon.ctp.user.api.avoidlogin.CtpAvoidLoginMiddlePageProviderService=\
com.seeyon.extend.spi.{project_id}.{Prefix}AvoidLoginService

# 客户端免登
com.seeyon.ctp.user.api.avoidlogin.CtpAvoidLoginClientModeProviderService=\
com.seeyon.extend.spi.{project_id}.{Prefix}AvoidLoginClientService
```

## 代码骨架（MiddlePage）

```java
package com.seeyon.extend.spi.{project_id};

import com.seeyon.ctp.user.api.avoidlogin.CtpAvoidLoginMiddlePageProviderService;
import com.seeyon.ctp.user.dto.*;
import com.seeyon.ctp.user.exception.CtpUserSpiSsoException;
import com.seeyon.ctp.user.util.CtpUserSpiUtils;
import lombok.extern.slf4j.Slf4j;

import java.util.Map;

/**
 * {project_name_cn} 中间页免登
 *
 * 场景：三方系统登录后跳转 V8，通过 code 换取用户信息
 * V8 调用时机：用户访问免登 URL 时，框架调用 getUserInfo
 * 三方系统：{third_system_name}
 * 返回语义：CtpAvoidLoginUserInfoDto 包含 V8 可匹配的用户标识（五字段唯一）
 */
@Slf4j
public class {Prefix}AvoidLoginService implements CtpAvoidLoginMiddlePageProviderService {

    @Override
    public String getClientId() {
        return "{third_type}";  // 必须等于免登地址 type 参数
    }

    @Override
    public CtpAvoidLoginUserInfoDto getUserInfo(String code, Map<String, String> extData) {
        try {
            log.info("[avoid] {project_name_cn} 免登, code 长度: {}, extData: {}", 
                     code != null ? code.length() : 0, extData);

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

            // 3. 构建返回（五字段唯一，这里用 thirdUserCode）
            return CtpAvoidLoginUserInfoDto.builder()
                .thirdUserCode(memberId)
                .ctpUserSpiRedirectUrlDto(CtpUserSpiRedirectUrlDto.builder()
                    .webRedirectUrl("/main/portal")
                    .mobileRedirectUrl("/main-mobile/portal")
                    .build())
                .build();

        } catch (CtpUserSpiSsoException e) {
            throw e;
        } catch (Exception e) {
            log.error("[avoid] {project_name_cn} 免登处理异常", e);
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
        // TODO: 调用三方接口或 V8 OpenAPI 查询用户
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

## 代码骨架（ClientMode）

```java
package com.seeyon.extend.spi.{project_id};

import com.seeyon.ctp.user.api.avoidlogin.CtpAvoidLoginClientModeProviderService;
import com.seeyon.ctp.user.dto.*;
import com.seeyon.ctp.user.exception.CtpUserSpiSsoException;
import com.seeyon.ctp.user.util.CtpUserSpiUtils;
import lombok.extern.slf4j.Slf4j;

import javax.servlet.http.HttpServletRequest;

/**
 * {project_name_cn} 客户端免登
 *
 * 场景：客户端携带签名/加密数据直接免登 V8
 * V8 调用时机：用户访问免登 URL 时，框架先调用 preCheck 校验，再调用 getUserInfo
 * 三方系统：{third_system_name}
 * 返回语义：CtpAvoidLoginUserInfoDto 包含 V8 可匹配的用户标识（五字段唯一）
 */
@Slf4j
public class {Prefix}AvoidLoginClientService implements CtpAvoidLoginClientModeProviderService {

    @Override
    public String getClientId() {
        return "{third_type}";
    }

    @Override
    public void preCheck(CtpUserSpiAvoidLoginClientModeDto dto) throws CtpUserSpiSsoException {
        log.info("[avoid] {project_name_cn} 客户端免登 preCheck, thirdType: {}, timestamp: {}", 
                 dto.getThirdType(), dto.getTimestamp());

        // 1. 校验时间戳（防重放）
        String timestamp = dto.getTimestamp();
        if (timestamp == null || timestamp.isEmpty()) {
            throw new CtpUserSpiSsoException("缺少时间戳");
        }
        long ts = Long.parseLong(timestamp);
        long now = System.currentTimeMillis();
        if (Math.abs(now - ts) > 5 * 60 * 1000) {  // 5 分钟过期
            throw new CtpUserSpiSsoException("时间戳过期");
        }

        // 2. 校验签名
        String sign = dto.getSign();
        if (sign == null || sign.isEmpty()) {
            throw new CtpUserSpiSsoException("缺少签名");
        }
        String expectedSign = calculateSign(dto);
        if (!sign.equals(expectedSign)) {
            throw new CtpUserSpiSsoException("签名校验失败");
        }
    }

    @Override
    public CtpAvoidLoginUserInfoDto getUserInfo(CtpUserSpiAvoidLoginClientModeDto dto) {
        String webUrl = dto.getWebUrl() != null ? dto.getWebUrl() : "/main/portal";
        String mobileUrl = dto.getMobileUrl() != null ? dto.getMobileUrl() : "/main-mobile/portal";
        
        try {
            log.info("[avoid] {project_name_cn} 客户端免登, extData: {}", dto.getExtData());

            // 1. 从 extData 获取用户标识
            String userIdentity = dto.getExtData().get("{identity_field}");
            if (userIdentity == null || userIdentity.isEmpty()) {
                // 尝试从 encryptData 解密
                String encryptData = dto.getEncryptData();
                if (encryptData != null && !encryptData.isEmpty()) {
                    userIdentity = decryptData(encryptData);
                }
            }
            
            if (userIdentity == null || userIdentity.isEmpty()) {
                throw new CtpUserSpiSsoException("未获取到用户标识",
                    getErrorUrl("USER_IDENTITY_NULL", "未获取到用户标识"));
            }

            // 2. 构建返回（五字段唯一）
            return CtpAvoidLoginUserInfoDto.builder()
                .thirdUserCode(userIdentity)
                .ctpUserSpiRedirectUrlDto(CtpUserSpiRedirectUrlDto.builder()
                    .webRedirectUrl(webUrl)
                    .mobileRedirectUrl(mobileUrl)
                    .build())
                .build();

        } catch (CtpUserSpiSsoException e) {
            throw e;
        } catch (Exception e) {
            log.error("[avoid] {project_name_cn} 客户端免登处理异常", e);
            throw new CtpUserSpiSsoException(e.getMessage(),
                getErrorUrl("UNKNOWN_ERROR", "未知错误"));
        }
    }

    private String calculateSign(CtpUserSpiAvoidLoginClientModeDto dto) {
        // TODO: 实现签名计算
        // 常见方式：SHA256(thirdType + timestamp + secret)
        String secret = CtpUserSpiUtils.getPropertyByName("{project_id}.signSecret");
        String raw = dto.getThirdType() + dto.getTimestamp() + secret;
        // return DigestUtils.sha256Hex(raw);
        return "";
    }

    private String decryptData(String encryptData) {
        // TODO: 实现解密逻辑
        // AES / SM4 / RSA
        return "";
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

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["ctp-user"]
}
```

## 方法说明

| 接口 | 方法 | 参数 | 返回 | 语义 |
|------|------|------|------|------|
| MiddlePage | getUserInfo | `String code, Map extData` | `CtpAvoidLoginUserInfoDto` | 中间页免登获取用户 |
| MiddlePage | getCtpUserInfo | `String code, Map extData` | `Object` | 获取用户信息 |
| ClientMode | preCheck | `CtpUserSpiAvoidLoginClientModeDto` | void | 客户端模式预校验 |
| ClientMode | getUserInfo | `CtpUserSpiAvoidLoginClientModeDto` | `CtpAvoidLoginUserInfoDto` | 客户端模式获取用户 |
| Backend | avoidLoginBackend | `HttpServletRequest, HttpServletResponse` | `Object` | 后端直接免登 |

## 重启服务

`ctp-user`
