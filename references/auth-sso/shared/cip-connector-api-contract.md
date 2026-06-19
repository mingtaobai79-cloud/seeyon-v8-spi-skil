# cip-connector-api 完整契约包 [FACT ✅ CFR 反编译]

> 来源：cip-connector-api-decompiled（CFR 0.152 反编译），所有签名均为 FACT 级别。

---

## 1. SSO 接口（模式 C：V8→三方单点）

### 1.1 SsoService

```java
package com.seeyon.cip.connector.api.sso;

public interface SsoService {
    @CipConnectorComment("获取名称")
    String getName();

    @CipConnectorComment("获取描述")
    String getTypeCaption();

    @CipConnectorComment("登录 url, 登录信息json串, 用户信息map, 客户端类型, 扩展字段")
    String login(String url, String json, Map<String, Object> userMap,
                 SsoClientTypeEnum clientType, Map<String, Object> extendParams);

    @CipConnectorComment("jsr303校验")
    void check(String config);

    @CipConnectorComment("获取页面json语句")
    String getPageJson();

    @CipConnectorComment("排序")
    Integer getSortNo();

    @CipConnectorComment("是否需要用户绑定操作")
    boolean needUserBind();
}
```

**login() 参数说明：**
- `url` — 跳转地址（V8 后台配置的三方 URL）
- `json` — 前端页面传递的配置数据（getPageJson 定义的字段）
- `userMap` — 用户信息 map（needUserBind()=true 时有数据）
  - `innerUserLoginName` — 登录名
  - `innerUserName` — 用户名称
  - `innerUserCODE` — 用户编码
  - `innerUserPhone` — 手机号
  - `innerUserEmail` — 邮箱
  - `innerUserId` — 用户 ID
  - `innerMemberId` — 人员 ID
- `clientType` — 客户端类型（PC / PHONE）
- `extendParams` — 扩展字段

### 1.2 SsoClientTypeEnum

```java
package com.seeyon.cip.connector.enums;

public enum SsoClientTypeEnum {
    PC(0),
    PHONE(1);
}
```

---

## 2. 注解

### 2.1 ConnectorChannelRouter

```java
package com.seeyon.cip.connector.annotation;

@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Indexed
public @interface ConnectorChannelRouter {
    String[] value();
    String desc() default "";
}
```

### 2.2 CipConnectorComment

```java
package com.seeyon.cip.connector.annotation;

@Target({ElementType.TYPE, ElementType.METHOD, ElementType.FIELD})
@Retention(RetentionPolicy.RUNTIME)
@Indexed
public @interface CipConnectorComment {
    String value() default "";
    String example() default "";
}
```

---

## 3. 工具类

### 3.1 CipConnectorSpiUtils

```java
package com.seeyon.cip.connector.common;

public class CipConnectorSpiUtils {
    // 获取指定类的单例实例（SPI 内部缓存）
    static <T> T getInstance(Class<T> clazz);

    // 获取 Spring Bean
    static <T> T getBean(Class<T> clazz);
    static <T> T getBean(String beanName, Class<T> requiredType);

    // 调用 Spring Bean 的指定方法（反射）
    static <T> T invokeBean(String beanName, String methodName, Object... params);

    // 获取 Nacos/yaml 配置
    static String getPropertyByName(String key);
}
```

**注意：** CipConnectorSpiUtils 没有 getRequest() 方法（与 CtpUserSpiUtils 不同）。

---

## 4. SSO 相关 DTO

### 4.1 MobileSsoUserDto（三方平台免登用户信息）

```java
package com.seeyon.cip.connector.dto.mobile.sso;

public class MobileSsoUserDto extends BaseDto {
    Long tid;                        // 租户 ID
    String thirdUserId;              // 三方用户 ID
    String thirdUserCode;            // 三方用户编码
    String thirdMobile;              // 三方用户手机号
    String thirdLoginName;           // 三方用户登录名
    String thirdUserEmail;           // 三方用户邮箱
    String bingMappingId;            // 需要绑定的三方用户 ID
    Map<String, String> extData;     // 扩展信息
}
```

### 4.2 MobileSsoUserRequestDto（查询单点登录信息）

```java
package com.seeyon.cip.connector.dto.mobile.sso;

// Builder 模式
public class MobileSsoUserRequestDto extends BaseDto {
    String type;                     // 插件类型（如 FeiShu）
    String appId;                    // 应用 ID
    String code;                     // 一次性随机 code
    String agentId;                  // agentId
    Map<String, String> extData;     // 扩展数据
}
```

---

## 5. 其他枚举

### 5.1 AccessModeEnum / AuthInfoModeEnum / ClientScopeEnum / ConfigModeEnum

```java
package com.seeyon.cip.connector.enums;

// 均为简单枚举，code 值从 jar 提取
```

---

## 6. 模式 C 代码生成约束

### spring.factories 格式
```
com.seeyon.cip.connector.api.sso.SsoService=\
com.seeyon.extend.spi.sso.{project}.XxxSsoServiceImpl
```

### spi_info.json
```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["cip-connector"]
}
```

### 重启服务
**cip-connector**（非 ctp-user）

### 命名规则
- `getName()` 返回值 + "SsoServiceImpl" = 类名
- 例：`getName()` 返回 "hospital" → 类名 `HospitalSsoServiceImpl`

### userMap 字段（needUserBind=true 时可用）
| key | 说明 |
|-----|------|
| innerUserLoginName | 登录名 |
| innerUserName | 用户名称 |
| innerUserCODE | 用户编码 |
| innerUserPhone | 手机号 |
| innerUserEmail | 邮箱 |
| innerUserId | 用户 ID |
| innerMemberId | 人员 ID |
