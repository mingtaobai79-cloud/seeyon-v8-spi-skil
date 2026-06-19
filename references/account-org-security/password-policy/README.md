# 密码强度/默认密码 / PasswordCheckService

> **Evidence: 混合** — 接口 FQCN FACT ✅（jar 反编译），扩展方法 OBSERVATION ⚠️（语雀文档，jar 中未包含）。
> Source: `ctp-user-api-5.3.351.jar` CFR 反编译 + 语雀 0097

## 场景

1. 系统密码强度不满足需求时，通过 SPI 自定义密码强度校验。
2. 系统默认密码不符合要求时，通过 SPI 自定义初始化密码。

适用版本：自定义密码强度 5.0.3+，自定义默认密码 5.3.0+。

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>ctp-user-api</artifactId>
  <version>5.3.351</version>
</dependency>
```

## 接口定义

### 5.3.351 版本 [FACT ✅ jar 反编译]

```java
package com.seeyon.ctp.user.api.passwordCheck;

public interface PasswordCheckService {
    Boolean checkPasswordStrength(String var1);
}
```

**注意：** 5.3.351 jar 中只有 `checkPasswordStrength` 一个方法。语雀文档提到的 `getMethodType()` 和 `customInitPassword()` 方法在 5.3.351 中不存在，可能在更高版本（5.0.3+ / 5.3.0+）中新增。

### 语雀文档版本 [OBSERVATION ⚠️]

```java
public interface PasswordCheckService {
    default List<PasswordMethodTypeEnum> getMethodType() {
        return Lists.newArrayList(PasswordMethodTypeEnum.CHECK_STRENGTH);
    }
    default Boolean checkPasswordStrength(String password) {
        return Boolean.TRUE;
    }
    default String customInitPassword(CtpUserSpiUserDto userDto, String password) {
        return password;
    }
}
```

**版本差异：** `getMethodType()`、`customInitPassword()`、`PasswordMethodTypeEnum` 在 5.3.351 jar 中均未找到。如果现场版本高于 5.3.351，需要重新反编译确认。

## 方法说明

| 方法 | 参数 | 返回 | Evidence | 语义 |
|------|------|------|----------|------|
| checkPasswordStrength | `String` | `Boolean` | FACT ✅ | 密码强度校验，true=通过 |
| getMethodType | 无 | `List<PasswordMethodTypeEnum>` | OBSERVATION ⚠️ | 控制执行哪些功能 |
| customInitPassword | `CtpUserSpiUserDto, String` | `String` | OBSERVATION ⚠️ | 返回自定义初始化密码 |

## 代码骨架

### 最小可用版（5.3.351 确认）

```java
package com.seeyon.extend.spi.user;

import com.seeyon.ctp.user.api.passwordCheck.PasswordCheckService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * 密码强度校验 SPI 实现
 * <p>注意：一旦配置自定义密码规则，系统管理员配置的密码规则不再生效。</p>
 */
public class CustomPasswordCheckService implements PasswordCheckService {

    private static final Logger log = LoggerFactory.getLogger(CustomPasswordCheckService.class);

    @Override
    public Boolean checkPasswordStrength(String password) {
        log.debug("[password-policy] checkPasswordStrength called");
        // TODO: 实现客户自定义密码规则
        // 示例：至少8位，包含大小写字母和数字
        // if (password == null || password.length() < 8) return false;
        // return password.matches(".*[A-Z].*") && password.matches(".*[a-z].*") && password.matches(".*\d.*");
        return Boolean.TRUE;
    }
}
```

### 完整版（需更高版本 jar 确认）

```java
    // 以下方法需要确认现场 ctp-user-api 版本是否包含
    // @Override
    // public List<PasswordMethodTypeEnum> getMethodType() {
    //     return Lists.newArrayList(
    //         PasswordMethodTypeEnum.CHECK_STRENGTH,
    //         PasswordMethodTypeEnum.INIT_PASS);
    // }
    //
    // @Override
    // public String customInitPassword(CtpUserSpiUserDto userDto, String password) {
    //     return "Custom@123"; // 自定义初始化密码
    // }
```

## spring.factories

```properties
com.seeyon.ctp.user.api.passwordCheck.PasswordCheckService=com.seeyon.extend.spi.user.CustomPasswordCheckService
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["ctp-user"]
}
```

## Nacos 配置

本 SPI 不需要额外 Nacos 配置。

## 重启服务

ctp-user
