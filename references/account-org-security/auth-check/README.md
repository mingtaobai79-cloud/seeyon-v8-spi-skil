> 🧊 **冻结状态** — 缺少必要 jar 包，接口/DTO 均为 OBSERVATION，无法升级到 FACT。
> 待获取对应 jar 后解除冻结。

# 登录人数控制 / AbstractAuthenticationCheckService

> Evidence: OBSERVATION ⚠️ — 语雀文档 + jar 反编译交叉验证。
> **jar 验证结果**：`ctp-user-api-5.3.429.jar` 中未找到 `AbstractAuthenticationCheckService` 和 `MaxOnlineUserExceedException`。
> 这些类可能在更高版本或独立 artifact 中。

## 场景

自定义租户、机构登录人数控制。客户有一个专门维护租户级/机构级的登录人数控制底表，在登录、切换租户、切换机构时进行校验。

适用版本：5.30 及以上版本。

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>ctp-user-api</artifactId>
  <version>5.3.429</version>
</dependency>
```

## 接口定义 [OBSERVATION ⚠️]

```java
// FQCN 待 jar 确认，短名：
public abstract class AbstractAuthenticationCheckService {
    /**
     * 处理租户或者机构已经达到最大的用户数的用户
     * @param users 用户列表
     * @return 过滤掉超过最大用户数的用户，返回剩余的用户
     */
    public abstract List<BaseDto> handleMaxOnlineUser(List<BaseDto> users);
}
```

## jar 反编译确认的类 [FACT ✅]

### PasswordCheckService（ctp-user-api-5.3.429）

```java
package com.seeyon.ctp.user.api.passwordCheck;

public interface PasswordCheckService {
    Boolean checkPasswordStrength(String var1);
}
```

## 代码骨架

```java
package com.seeyon.extend.spi.auth;

// import com.seeyon.ctp.user.api.authentication.AbstractAuthenticationCheckService;  // FQCN 待确认
// import com.seeyon.ctp.user.exception.MaxOnlineUserExceedException;                // FQCN 待确认
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.List;

/**
 * 登录人数控制 SPI 实现
 * <p>🧊 冻结：接口 FQCN 未确认，代码无法编译</p>
 */
public class CustomAuthenticationCheckService /* extends AbstractAuthenticationCheckService */ {

    private static final Logger log = LoggerFactory.getLogger(CustomAuthenticationCheckService.class);

    // @Override
    public /* List<BaseDto> */ Object handleMaxOnlineUser(/* List<BaseDto> */ Object users) {
        log.debug("[auth-check] handleMaxOnlineUser called");
        // TODO: 实现租户/机构登录人数控制逻辑
        // 1. 查询租户/机构的最大在线用户数配置
        // 2. 查询当前在线用户数
        // 3. 如果超过限制，抛出 MaxOnlineUserExceedException
        // 4. 返回过滤后的用户列表
        return users;
    }
}
```

## Nacos 配置

本 SPI 不需要额外 Nacos 配置。

## spring.factories

```properties
# FQCN 待 jar 确认
# com.seeyon.ctp.user.api.authentication.AbstractAuthenticationCheckService=com.seeyon.extend.spi.auth.CustomAuthenticationCheckService
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

## 阻塞项

1. `AbstractAuthenticationCheckService` 接口 FQCN — 5.3.429 jar 中不存在
2. `MaxOnlineUserExceedException` 异常类 FQCN — 5.3.429 jar 中不存在
3. `BaseDto` 完整字段 — 5.3.429 jar 中未找到
4. 需要更高版本 jar 或独立 artifact
