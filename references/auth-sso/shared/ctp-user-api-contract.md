# ctp-user-api 5.3.351 完整契约包 [FACT ✅ jar 反编译]

> 来源：ctp-user-api-5.3.351.jar 反编译，所有签名均为 FACT 级别。

---

## 1. SPI 接口（入口点）

### 1.1 CtpSsoAvoidLoginBaseService（基类）

```java
package com.seeyon.ctp.user.api;

public interface CtpSsoAvoidLoginBaseService {
    String TAG = "[avoid]";
    @CtpUserComment("返回客户端标识，双方约定的唯一 type")
    String getClientId();
}
```

### 1.2 CtpUserSsoAuthProviderService（模式 A：V8 认证登录）

```java
package com.seeyon.ctp.user.api.sso;

// 实现类需要增加 @CtpUserChannelRouter 注解
public interface CtpUserSsoAuthProviderService {

    // === 必须实现 ===
    String getRequestParaKey();  // request 中 code/ticket 的 key 名
    String getSsoLoginUrl(HttpServletRequest request, String redirectUrl);  // 三方 SSO 登录地址
    CtpUserSpiLoginUserInfoDto getUserLoginInfo(HttpServletRequest request, String redirectUrl)
        throws CtpUserSpiSsoException, SpiAuthContinueException;  // 核心：获取用户信息

    // === 可选实现（有默认值）===
    default void setServerEnv(CtpUserSpiServerEnvDto dto) {}
    default Boolean sendVerifyCode(String mobile) { return null; }
    default ShortLinkModeEnum shortLinkMode() { return null; }
    default String getEncodeLogoutRedirectUrl() { return null; }
    default void thirdSsoLogout(HttpServletRequest request, String thirdUserInfoJson) {}
    default CtpUserSpiLoginUserInfoDto getUserLoginInfoForMobile(
        String userLoginName, Map<String, Object> extData,
        CtpUserSpiAuthTokenEnum authTypeEnum) throws CtpUserSpiSsoException { return null; }
    default boolean tokenExpiredSetNull() { return false; }
    default Long rebuildCtpUserDtoList(List<CtpUserSpiUserDto> list) {
        return CollectionUtils.isEmpty(list) ? null : list.get(0).getId();
    }
    default CtpUserSpiThirdTokenDto refreshThirdTokenByConfig(
        String thirdToken, Map<String, Object> configMap) { return null; }
    default String get4aTokenKey() { return null; }
    default String getTidCode() { return null; }
    default Map<String, CtpUserSpiAuthTokenEnum[]> mapSupportsAuthTokenEnum() {
        Map<String, CtpUserSpiAuthTokenEnum[]> map = new HashMap();
        map.put("WEB", new CtpUserSpiAuthTokenEnum[]{CtpUserSpiAuthTokenEnum.SPI_SSO});
        return map;
    }
    default CtpUserSpiAuthTokenEnum getSuccessAuthTokenEnum() {
        return CtpUserSpiAuthTokenEnum.USERNAME_PASSWORD;
    }
    default CtpUserSpiThirdLogoutDto getThirdLogoutParams(Map<String, Object> thirdLogoutMap) {
        return null;
    }

    // === 已废弃 ===
    @Deprecated default void setServerDomain(String serverDomain) {}
    @Deprecated default Boolean isRedirectShortLink() { return false; }
    @Deprecated default CtpUserSpiThirdTokenDto refreshThirdToken(String thirdToken, long expired) { return null; }
}
```

### 1.3 CtpAvoidLoginClientModeProviderService（模式 B：三方→V8 免登，无中间页）

```java
package com.seeyon.ctp.user.api.avoidlogin;

public interface CtpAvoidLoginClientModeProviderService extends CtpSsoAvoidLoginBaseService {
    void preCheck(CtpUserSpiAvoidLoginClientModeDto dto) throws CtpUserSpiSsoException;
    CtpAvoidLoginUserInfoDto getUserInfo(CtpUserSpiAvoidLoginClientModeDto dto);
}
```

### 1.4 CtpAvoidLoginMiddlePageProviderService（模式 B：三方→V8 免登，有中间页）

```java
package com.seeyon.ctp.user.api.avoidlogin;

public interface CtpAvoidLoginMiddlePageProviderService extends CtpSsoAvoidLoginBaseService {
    default CtpAvoidLoginUserInfoDto getUserInfo(String code, Map<String, String> extData) { return null; }
    default Object getCtpUserInfo(String code, Map<String, String> extData) { return null; }
    default Boolean isRefreshTokenCycle() { return false; }
    default CtpUserSpiThirdTokenDto doRefreshToken(ThirdTokenDto thirdTokenDto) { return null; }
    default SpiWebAuthenticationDetailInfo getSpiWebAuthenticationDetailInfo() { return null; }
}
```

### 1.5 CtpAvoidLoginBackendProviderService（模式 B：后端直接免登）

```java
package com.seeyon.ctp.user.api.avoidlogin;

public interface CtpAvoidLoginBackendProviderService extends CtpSsoAvoidLoginBaseService {
    @Deprecated default Map<String, Object> doExecuteAvoidLoginBackend(
        HttpServletRequest request, HttpServletResponse response) { return null; }
    default Object avoidLoginBackend(HttpServletRequest request, HttpServletResponse response) { return null; }
}
```

### 1.6 其他 SPI 接口

```java
// 自定义用户信息
package com.seeyon.ctp.user.api.user;
public interface CustomUserInfoService {
    Map<String, Object> filterCustomUserInfo(Map<String, Object> var1);
}

// 密码强度校验
package com.seeyon.ctp.user.api.passwordCheck;
public interface PasswordCheckService {
    Boolean checkPasswordStrength(String var1);
}

// 三方菜单
package com.seeyon.ctp.user.api.menu;
public abstract class AbstractThirdMenuService {
    public MenuPositionEnum position() { return MenuPositionEnum.TAIL; }
    public abstract List<CtpUserThirdNavFrontDto> selectThirdMenu(ThirdMenuParamDto var1);
}

// 扫码登录
package com.seeyon.ctp.user.api.qrcode;
public abstract class AbstractLoginQrCodeService {
    public abstract String getQrCodeAuthenticationType();
    public abstract CtpLoginQrCodeDto generateQrCode();
    public abstract QrcodeResultDto roundScanResult(String var1);
}
```

---

## 2. DTO（数据传输对象）

### 2.1 CtpAvoidLoginUserInfoDto（模式 B 返回值）

```java
package com.seeyon.ctp.user.dto;

// Builder 模式
public class CtpAvoidLoginUserInfoDto implements Serializable {
    // 5 个用户标识字段，有且只有一个赋值即可：
    String thirdUserId;       // 三方用户 ID
    String thirdUserCode;     // 三方用户编码（人员编号/工号）
    String thirdMobile;       // 三方用户手机号
    String thirdLoginName;    // 三方用户登录名
    String thirdUserEmail;    // 三方用户邮箱

    String tenantType;        // 租户数据类型：code / id
    String tenantData;        // 租户数据值
    CtpUserSpiThirdTokenDto ctpUserSpiThirdTokenDto;  // 三方认证 token
    CtpUserSpiRedirectUrlDto ctpUserSpiRedirectUrlDto; // 免登成功后重定向地址
    String clientType;        // WEB/PC/MOBILE/PAD/THIRD
}
```

### 2.2 CtpUserSpiLoginUserInfoDto（模式 A 返回值）

```java
package com.seeyon.ctp.user.dto;

// Builder 模式
public class CtpUserSpiLoginUserInfoDto implements Serializable {
    // 5 个用户标识字段，有且只有一个赋值即可：
    String thirdUserId;
    String thirdUserCode;
    String thirdMobile;
    String thirdLoginName;
    String thirdUserEmail;

    String tenantType;
    String tenantData;
    String thirdUserInfoJson;  // 待缓存的三方用户信息 JSON（模式 A 特有）
    CtpUserSpiThirdTokenDto ctpUserSpiThirdTokenDto;
    String clientType;         // WEB/PC/MOBILE/PAD/THIRD
}
```

### 2.3 CtpUserSpiAvoidLoginClientModeDto（ClientMode 入参）

```java
package com.seeyon.ctp.user.dto;

public class CtpUserSpiAvoidLoginClientModeDto implements Serializable {
    String thirdType;              // 第三方类型，对应前端入参 'c'
    String clientType;             // 客户端类型，前端自动赋值 WEB|MOBILE
    public String timestamp;       // 时间戳_毫秒，对应前端入参 't'
    public String sign;            // 签名，对应前端入参 's'
    public String webUrl;          // web端登录地址，对应前端入参 'w'
    public String mobileUrl;       // 手机端登录地址，对应前端入参 'm'
    public String encryptData;     // 加密后的业务数据，对应前端入参 'd'
    Map<String, String> extData;   // 扩展数据
}
```

### 2.4 CtpUserSpiRedirectUrlDto（跳转地址）

```java
package com.seeyon.ctp.user.dto;

// Builder 模式
public class CtpUserSpiRedirectUrlDto implements Serializable {
    String webRedirectUrl;     // web 重定向地址
    String mobileRedirectUrl;  // mobile 重定向地址
}
```

### 2.5 CtpUserSpiThirdTokenDto（三方 token）

```java
package com.seeyon.ctp.user.dto;

// Builder 模式
public class CtpUserSpiThirdTokenDto implements Serializable {
    String thirdToken;              // 待缓存的三方 token
    Long expired;                   // 过期时间_秒
    Map<String, Object> extData;    // 扩展参数
}
```

### 2.6 CtpUserSpiServerEnvDto（服务环境配置）

```java
package com.seeyon.ctp.user.dto;

// Builder 模式
public class CtpUserSpiServerEnvDto implements Serializable {
    String serverDomain;    // 服务域名
    String frontBaseRoute;  // 前端地址路由
}
```

### 2.7 CtpUserSpiUserDto（用户信息）

```java
package com.seeyon.ctp.user.dto;

// Builder 模式, extends BaseDto
public class CtpUserSpiUserDto extends BaseDto {
    Long id;
    Long tenantId;
    String name;              // 用户名称
    String loginName;         // 登录名
    String password;
    Date expiredTime;
    String avatar;
    String phoneNumber;       // 手机号
    String email;
    Boolean admin;
    CtpUserSpiUserTypeEnum type;  // 默认 INTERNAL
    Long memberId;            // 人员ID
    Long orgId;               // 所属机构ID
    String orgName;
    List<Long> authOrgIdList;
    Boolean enabled;          // 默认 true
    String locale;
    Date effectiveTime;
    Date invalidTime;
    String lastLoginDevice;
    String lastLoginIp;
    Date lastLoginTime;
    Date createTime;
    Long memberPostId;        // 默认 -1L
    String clientLoginTime;
}
```

### 2.8 CtpUserSpiThirdLogoutDto（登出参数）

```java
package com.seeyon.ctp.user.dto;

public class CtpUserSpiThirdLogoutDto implements Serializable {
    String code;  // 人员编码
}
```

### 2.9 SpiWebAuthenticationDetailInfo（认证详情）

```java
package com.seeyon.ctp.user.dto;

// Builder 模式
public class SpiWebAuthenticationDetailInfo {
    String remoteAddress;  // 登录地址
}
```

### 2.10 ThirdTokenDto（token 刷新入参）

```java
package com.seeyon.ctp.user.dto;

// Builder 模式
public class ThirdTokenDto implements Serializable {
    String innerUserId;
    String thirdToken;
}
```

### 2.11 AvoidLoginConfigProperties（免登配置属性）

```java
package com.seeyon.ctp.user.dto;

public class AvoidLoginConfigProperties {
    String authType;
    String callbackUrl;
    String aesKey;
    String clientId = "v8sso";
    String clientSecret;
    String tokenUrl;
    String authorizeUrl;
    Boolean isEncrypt = false;
}
```

---

## 3. 枚举

### 3.1 CtpUserSpiAuthTokenEnum

```java
package com.seeyon.ctp.user.enums;

public enum CtpUserSpiAuthTokenEnum {
    SPI_SSO(0, "com.seeyon.ctp.user.security.authentication.SpiSsoAuthenticationToken"),
    USERNAME_PASSWORD(1, "com.seeyon.ctp.user.security.authentication.UsernamePasswordAuthenticationToken"),
    PHONE_VERIFY_CODE(2, "com.seeyon.ctp.user.security.authentication.PhoneNumberDynamicPasswordAuthenticationToken");
}
```

### 3.2 CtpUserSpiUserTypeEnum

```java
package com.seeyon.ctp.user.enums;

public enum CtpUserSpiUserTypeEnum {
    INTERNAL(0), EXTERNAL(1), VISITOR(2), DEVICE(3), ROBOT(4),
    ADMINISTRATOR(5), OPENAPI(6), OPS(7), CLOUD(8), NATURAL_MEMBER(9), GUEST(10);
}
```

### 3.3 ShortLinkModeEnum

```java
package com.seeyon.ctp.user.enums;

public enum ShortLinkModeEnum {
    COMPACT_MODE(1),   // domain/path/sl/xxx
    SPLICING_MODE(2);  // domain/path?mappingId=xxx
}
```

### 3.4 MenuPositionEnum

```java
package com.seeyon.ctp.user.enums;

public enum MenuPositionEnum {
    HEAD(0), TAIL(2);
}
```

---

## 4. 异常

### 4.1 CtpUserSpiSsoException

```java
package com.seeyon.ctp.user.exception;

public class CtpUserSpiSsoException extends RuntimeException {
    String errUrl;
    public CtpUserSpiSsoException(String message) { super(message); }
    public CtpUserSpiSsoException(String message, String errUrl) {
        super(message); this.errUrl = errUrl;
    }
}
```

### 4.2 SpiAuthContinueException

```java
package com.seeyon.ctp.user.exception;

public class SpiAuthContinueException extends BusinessException {
    public SpiAuthContinueException() {}
    public SpiAuthContinueException(String code) { super(code); }
    public SpiAuthContinueException(String code, String... params) { super(code, params); }
    public SpiAuthContinueException(String code, Throwable cause) { super(code, cause); }
}
```

---

## 5. 工具类

### 5.1 CtpUserSpiUtils

```java
package com.seeyon.ctp.user.util;

public class CtpUserSpiUtils {
    // 获取指定类的单例实例（SPI 内部缓存）
    static <T> T getInstance(Class<T> clazz);

    // 获取 Spring Bean
    static <T> T getBean(Class<T> clazz);
    static <T> T getBean(String beanName, Class<T> requiredType);

    // 调用 Spring Bean 的指定方法（反射）
    static <T> T invokeBean(String beanName, String methodName, Object... params);

    // 获取 Nacos/yaml 配置
    static String getPropertyByName(String key);

    // 获取当前 HttpServletRequest
    static HttpServletRequest getRequest();

    // 通过 SPI 登录信息获取 CtpUser（模式 A）
    static Object getCtpUserBySpiLogin(CtpUserSpiLoginUserInfoDto dto);

    // 通过免登信息获取 CtpUser（模式 B）
    static Object getCtpUserByAvoidLogin(CtpAvoidLoginUserInfoDto dto);
}
```

---

## 6. 常量

### 6.1 CtpUserSpiAvoidConstants

```java
package com.seeyon.ctp.user.constant;

public class CtpUserSpiAvoidConstants {
    public static class DataKey {
        public static final String USER_LOGIN_NAME = "l";  // 登录名
        public static final String USER_MOBILE = "m";      // 手机号
        public static final String USER_CODE = "c";        // 用户编码
    }
    public static class KeyMethodName {
        public static final String RSA = "RSA";
        public static final String AES = "AES";
        public static final String DES = "DES";
        public static final String MD5 = "MD5";
        public static final String SHA1 = "SHA1";
        public static final String SHA256 = "SHA256";
    }
}
```

### 6.2 CtpUserSpiConstants

```java
package com.seeyon.ctp.user.constant;

public class CtpUserSpiConstants {
    public static final String QR_CODE = "qrCode_";
    public static class ClientType {
        public static final String WEB = "WEB";
        public static final String PC = "PC";
        public static final String MOBILE = "MOBILE";
        public static final String PAD = "PAD";
        public static final String THIRD = "THIRD";
    }
}
```

---

## 7. 前端入参映射（ClientMode）

ClientMode 前端 URL 参数与 DTO 字段的映射关系：

| URL 参数 | DTO 字段 | 说明 |
|----------|----------|------|
| c | thirdType | 第三方类型 |
| t | timestamp | 时间戳_毫秒 |
| s | sign | 签名 |
| w | webUrl | web端登录地址 |
| m | mobileUrl | 手机端登录地址 |
| d | encryptData | 加密后的业务数据 |
| (自动) | clientType | 客户端类型 WEB/MOBILE |
| (自动) | extData | 扩展数据 Map |

## 8. 用户标识字段选择指南

CtpAvoidLoginUserInfoDto 和 CtpUserSpiLoginUserInfoDto 共享相同的 5 个用户标识字段：

| 字段 | 用途 | 匹配 V8 用户的条件 |
|------|------|-------------------|
| thirdUserId | 三方系统内部 ID | V8 用户表中的三方绑定 ID |
| thirdUserCode | 人员编号/工号 | V8 用户表中的 code 字段 |
| thirdMobile | 手机号 | V8 用户表中的 phoneNumber 字段 |
| thirdLoginName | 登录名/账号 | V8 用户表中的 loginName 字段 |
| thirdUserEmail | 邮箱 | V8 用户表中的 email 字段 |

**规则：有且只有一个赋值即可。**
