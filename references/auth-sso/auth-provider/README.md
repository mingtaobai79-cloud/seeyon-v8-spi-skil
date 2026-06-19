# 登录扩展 / AbstractAuthenticationProvider

> **Evidence: FACT ✅** — 接口签名来自 `ctp-user-api-5.3.351.jar` CFR 反编译。

## 场景

账号密码或平台登录流程中扩展自定义认证方式。

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>ctp-user-api</artifactId>
  <version>5.3.351</version>
</dependency>
```

## 接口定义 [FACT ✅]

```java
package com.seeyon.ctp.user.security.authentication.provider;

import com.seeyon.ctp.user.security.authentication.Authentication;
import org.springframework.stereotype.Component;

@Component
public abstract class AbstractAuthenticationProvider {
    public abstract String getAuthenticationType();
    public abstract boolean supports(Class<?> var1);
    public abstract Authentication retrieveUser(Authentication var1);
    public abstract void preAuthenticationCheck(Authentication var1);
    public abstract void postAuthenticationCheck(Authentication var1);
    public abstract void additionalAuthenticationChecks(Authentication var1);
    public abstract Authentication createSuccessAuthentication(Object var1, Authentication var2);
}
```

### Authentication [FACT ✅]

```java
package com.seeyon.ctp.user.security.authentication;

import java.io.Serializable;
import java.security.Principal;

public interface Authentication extends Principal, Serializable {
    Object getCredentials();
    Object getDetails();
    Object getPrincipal();
}
```

### AbstractAuthenticationToken [FACT ✅]

```java
package com.seeyon.ctp.user.security.authentication;

public abstract class AbstractAuthenticationToken implements Authentication {
    private Object details;

    @Override
    public String getName() {
        return this.getPrincipal() == null ? "" : this.getPrincipal().toString();
    }

    @Override
    public Object getDetails() { return this.details; }
    public void setDetails(Object details) { this.details = details; }
}
```

## 方法说明

| 方法 | 参数 | 返回 | 语义 |
|------|------|------|------|
| getAuthenticationType | 无 | `String` | 返回认证类型标识 |
| supports | `Class<?>` | `boolean` | 是否支持该 Authentication 类型 |
| retrieveUser | `Authentication` | `Authentication` | 从认证请求中获取用户信息 |
| preAuthenticationCheck | `Authentication` | void | 认证前校验 |
| postAuthenticationCheck | `Authentication` | void | 认证后校验 |
| additionalAuthenticationChecks | `Authentication` | void | 额外认证检查 |
| createSuccessAuthentication | `Object, Authentication` | `Authentication` | 创建认证成功 Token |

## 代码骨架

```java
package com.seeyon.extend.spi.auth;

import com.seeyon.ctp.user.security.authentication.provider.AbstractAuthenticationProvider;
import com.seeyon.ctp.user.security.authentication.Authentication;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class CustomAuthenticationProvider extends AbstractAuthenticationProvider {

    private static final Logger log = LoggerFactory.getLogger(CustomAuthenticationProvider.class);

    @Override
    public String getAuthenticationType() {
        return "custom-auth";
    }

    @Override
    public boolean supports(Class<?> authentication) {
        // TODO: 判断是否支持该 Authentication 类型
        return false;
    }

    @Override
    public Authentication retrieveUser(Authentication authentication) {
        log.debug("[auth-provider] retrieveUser called");
        // TODO: 从认证请求中获取用户信息
        return authentication;
    }

    @Override
    public void preAuthenticationCheck(Authentication authentication) {
        log.debug("[auth-provider] preAuthenticationCheck called");
    }

    @Override
    public void postAuthenticationCheck(Authentication authentication) {
        log.debug("[auth-provider] postAuthenticationCheck called");
    }

    @Override
    public void additionalAuthenticationChecks(Authentication authentication) {
        log.debug("[auth-provider] additionalAuthenticationChecks called");
    }

    @Override
    public Authentication createSuccessAuthentication(Object principal, Authentication authentication) {
        log.debug("[auth-provider] createSuccessAuthentication called");
        // TODO: 创建认证成功 Token
        return authentication;
    }
}
```

## Nacos 配置

本 SPI 不需要额外 Nacos 配置。

## spring.factories

```properties
com.seeyon.ctp.user.security.authentication.provider.AbstractAuthenticationProvider=com.seeyon.extend.spi.auth.CustomAuthenticationProvider
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["user"]
}
```

## 重启服务

user
