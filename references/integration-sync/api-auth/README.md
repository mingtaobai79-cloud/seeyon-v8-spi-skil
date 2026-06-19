# 集成接口鉴权 / LinkerSecurityService

> Evidence: FACT ✅ 用户提供的反编译接口源码。语雀 `0112-集成接口鉴权-nks3s8agdgi1im3z.md` 为 OBSERVATION。

## 场景

在配置集成应用接口时，有些业务接口通过标品无法成功配置时，可以通过扩展 SPI 方式来完成接口鉴权（通过扩展代码调用接口方式来完成相关 header、body、query 参数设置）。

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>cip-connector-api</artifactId>
  <version>3.8.211</version>
</dependency>
```

## 接口定义 [FACT ✅]

```java
package com.seeyon.cip.connector.api.authentication;

import com.seeyon.cip.connector.annotation.CipConnectorComment;
import com.seeyon.cip.connector.dto.authentication.AuthEventDto;
import com.seeyon.cip.connector.dto.authentication.AuthenticationDto;
import com.seeyon.cip.connector.enums.AuthInfoModeEnum;
import java.util.Map;

public interface LinkerSecurityService {
    @CipConnectorComment("认证类型名称")
    String getName();

    @CipConnectorComment("认证类型中文名称")
    String getTypeCaption();

    @CipConnectorComment("获取安全模式")
    AuthInfoModeEnum getMode();

    @CipConnectorComment("认证请求")
    Map<String, Object> doAuthentication(AuthenticationDto var1) throws Exception;

    @CipConnectorComment("回调解密json : 认证信息dto json串")
    AuthEventDto doDecode(String var1, AuthEventDto var2) throws Exception;

    @CipConnectorComment("获取页面json语句")
    String getPageJson();

    @CipConnectorComment("排序")
    Integer getSortNo();

    @CipConnectorComment("jsr303校验")
    void jsonCheck(String var1);

    @CipConnectorComment("校验执行动作最终结果")
    default Boolean doVerification(AuthenticationDto authenticationDto) {
        return null;
    }
}
```

## 方法说明

| 方法 | 参数 | 返回 | 语义 |
|------|------|------|------|
| `getName` | - | `String` | 认证类型名称（英文标识） |
| `getTypeCaption` | - | `String` | 认证类型中文名称 |
| `getMode` | - | `AuthInfoModeEnum` | 获取安全模式（ANONYMOUS/TENANT/USER） |
| `doAuthentication` | `AuthenticationDto` | `Map<String, Object>` | 执行认证请求，返回认证结果参数 |
| `doDecode` | `String`, `AuthEventDto` | `AuthEventDto` | 回调解密，处理认证信息 DTO JSON 串 |
| `getPageJson` | - | `String` | 获取前端配置页面 JSON |
| `getSortNo` | - | `Integer` | 排序号 |
| `jsonCheck` | `String` | `void` | JSR303 校验配置 JSON |
| `doVerification` | `AuthenticationDto` | `Boolean` | 校验执行动作最终结果（可选） |

## DTO 定义 [FACT ✅]

### AuthenticationDto（认证请求）

```java
package com.seeyon.cip.connector.dto.authentication;

public class AuthenticationDto extends BaseDto {
    private Long authId;
    private Long detailId;
    private String json;
    private Map<String, Object> params;
    private AuthenticationUserDto user;
}
```

### AuthEventDto（认证事件）

```java
package com.seeyon.cip.connector.dto.authentication;

@DtoInfo("认证事件dto")
public class AuthEventDto extends BaseDto {
    private String name;
    private Map<String, Object> data;
    private Long authId;
}
```

### AuthInfoModeEnum（安全模式）

```java
package com.seeyon.cip.connector.enums;

public enum AuthInfoModeEnum implements Messageable {
    ANONYMOUS(0),  // 匿名模式
    TENANT(1),     // 租户模式
    USER(2);       // 用户模式

    private int code;
}
```

## Nacos 配置

```yaml
# cip-connector 微服务 Nacos 配置
seeyon:
  connector:
    auth:
      {auth_type}:
        enabled: true
        client-id: CHANGE_ME_IN_NACOS
        client-secret: CHANGE_ME_IN_NACOS
        token-url: https://third.example.com/oauth/token
        refresh-url: https://third.example.com/oauth/refresh
        timeout-ms: 5000
```

## spring.factories

```properties
com.seeyon.cip.connector.api.authentication.LinkerSecurityService=\
com.seeyon.extend.spi.{project_id}.{Prefix}SecurityService
```

## 代码骨架

```java
package com.seeyon.extend.spi.{project_id};

import com.seeyon.boot.util.JsonUtils;
import com.seeyon.cip.connector.api.authentication.LinkerSecurityService;
import com.seeyon.cip.connector.dto.authentication.AuthEventDto;
import com.seeyon.cip.connector.dto.authentication.AuthenticationDto;
import com.seeyon.cip.connector.enums.AuthInfoModeEnum;
import lombok.extern.slf4j.Slf4j;

import java.util.HashMap;
import java.util.Map;

/**
 * {project_name_cn} 集成接口鉴权
 *
 * 场景：集成应用接口标品认证方式不满足时，通过 SPI 追加/生成 header、body、query 参数
 * V8 调用时机：集成应用调用三方接口前，框架调用 doAuthentication 获取认证参数
 * 三方系统：{third_system_name}
 * 返回语义：认证结果参数 Map（如 access_token、header 参数等）
 */
@Slf4j
public class {Prefix}SecurityService implements LinkerSecurityService {

    @Override
    public String getName() {
        return "{auth_type}";  // 认证类型英文标识
    }

    @Override
    public String getTypeCaption() {
        return "{auth_caption}";  // 认证类型中文名称
    }

    @Override
    public AuthInfoModeEnum getMode() {
        return AuthInfoModeEnum.USER;  // 根据实际场景选择
    }

    @Override
    public Map<String, Object> doAuthentication(AuthenticationDto authenticationDto) throws Exception {
        log.info("[api-auth] 执行认证, authId: {}, detailId: {}",
                 authenticationDto.getAuthId(),
                 authenticationDto.getDetailId());

        Map<String, Object> result = new HashMap<>();

        try {
            // 1. 解析配置 JSON
            String json = authenticationDto.getJson();
            Map<String, Object> config = JsonUtils.fromJson(json, Map.class);

            // 2. 获取认证参数
            String clientId = (String) config.get("clientId");
            String clientSecret = (String) config.get("clientSecret");
            String tokenUrl = (String) config.get("tokenUrl");

            // 3. 调用三方认证接口获取 token
            // TODO: 实现具体的认证逻辑
            // String accessToken = fetchAccessToken(tokenUrl, clientId, clientSecret);

            // 4. 构建返回结果
            // result.put("access_token", accessToken);
            // result.put("header_Authorization", "Bearer " + accessToken);

            log.info("[api-auth] 认证成功");

        } catch (Exception e) {
            log.error("[api-auth] 认证失败", e);
            throw e;
        }

        return result;
    }

    @Override
    public AuthEventDto doDecode(String json, AuthEventDto authEventDto) throws Exception {
        log.info("[api-auth] 回调解密, authId: {}", authEventDto.getAuthId());

        // TODO: 实现回调解密逻辑
        // 根据 json 参数解密认证信息，更新 authEventDto

        return authEventDto;
    }

    @Override
    public String getPageJson() {
        // 返回前端配置页面 JSON
        return "{\"fields\":[" +
               "{\"name\":\"clientId\",\"label\":\"客户端ID\",\"type\":\"input\",\"required\":true}," +
               "{\"name\":\"clientSecret\",\"label\":\"客户端密钥\",\"type\":\"password\",\"required\":true}," +
               "{\"name\":\"tokenUrl\",\"label\":\"Token接口地址\",\"type\":\"input\",\"required\":true}" +
               "]}";
    }

    @Override
    public Integer getSortNo() {
        return 100;
    }

    @Override
    public void jsonCheck(String json) {
        log.info("[api-auth] JSR303 校验配置 JSON");
        // TODO: 实现配置 JSON 校验逻辑
    }

    @Override
    public Boolean doVerification(AuthenticationDto authenticationDto) {
        log.info("[api-auth] 校验执行动作最终结果");
        // TODO: 实现最终结果校验逻辑
        return true;
    }
}
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["cip-connector"]
}
```

## 重启服务

`cip-connector`
