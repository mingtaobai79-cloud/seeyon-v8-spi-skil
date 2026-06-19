# 模式 A：V8 认证登录 — SPI 接口完整定义

> **Evidence: FACT ✅** — 接口签名、DTO、枚举、工具类均来自 `ctp-user-api-5.3.351.jar` 反编译。
> 完整契约包：`../shared/ctp-user-api-contract.md`

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>ctp-user-api</artifactId>
  <version>5.3.351</version>
</dependency>
```

## 接口：CtpUserSsoAuthProviderService [FACT ✅]

```java
package com.seeyon.ctp.user.api.sso;

@CtpUserComment("统一三方认证 SPI 扩展接口, 实现类需要增加 @CtpUserChannelRouter 注解")
public interface CtpUserSsoAuthProviderService {

    // ===== 必须实现 =====

    @CtpUserComment("从 request 中获取临时 code 或 ticket 的 key")
    String getRequestParaKey();

    @CtpUserComment("三方认证 sso 登录地址")
    String getSsoLoginUrl(HttpServletRequest request, String encodeRedirectUrl);

    @CtpUserComment("从三方认证接口中获取用户信息")
    CtpUserSpiLoginUserInfoDto getUserLoginInfo(HttpServletRequest request, String encodeRedirectUrl)
        throws CtpUserSpiSsoException, SpiAuthContinueException;

    // ===== 按需实现 =====

    @CtpUserComment("设置服务环境配置信息")
    default void setServerEnv(CtpUserSpiServerEnvDto dto) {}

    @CtpUserComment("三方认证发送短信验证码")
    default Boolean sendVerifyCode(String mobile) { return null; }

    @CtpUserComment("登录三方成功后的重定向地址是否使用短链接及短链接模式")
    default ShortLinkModeEnum shortLinkMode() { return null; }

    @CtpUserComment("三方登出重定向地址")
    default String getEncodeLogoutRedirectUrl() { return null; }

    @CtpUserComment("三方认证 sso 登出逻辑")
    default void thirdSsoLogout(HttpServletRequest request, String thirdUserInfoJson) {}

    @CtpUserComment("手机端登录使用")
    default CtpUserSpiLoginUserInfoDto getUserLoginInfoForMobile(
        String userLoginName, Map<String, Object> extData,
        CtpUserSpiAuthTokenEnum authTokenEnum) throws CtpUserSpiSsoException { return null; }

    @CtpUserComment("如果 v8 token 过期，则赋值空")
    default boolean tokenExpiredSetNull() { return false; }

    @CtpUserComment("如果获取到多个用户，则业务方判断取哪个")
    default Long rebuildCtpUserDtoList(List<CtpUserSpiUserDto> list) {
        return CollectionUtils.isEmpty(list) ? null : list.get(0).getId();
    }

    @CtpUserComment("刷新三方 token")
    default CtpUserSpiThirdTokenDto refreshThirdTokenByConfig(
        String thirdToken, Map<String, Object> configMap) { return null; }

    @CtpUserComment("如果需要缓存 4a token，则返回 key")
    default String get4aTokenKey() { return null; }

    @CtpUserComment("为上下文租户赋值")
    default String getTidCode() { return null; }

    @CtpUserComment("登录认证条件")
    default Map<String, CtpUserSpiAuthTokenEnum[]> mapSupportsAuthTokenEnum() {
        Map<String, CtpUserSpiAuthTokenEnum[]> map = new HashMap<>();
        map.put("WEB", new CtpUserSpiAuthTokenEnum[]{CtpUserSpiAuthTokenEnum.SPI_SSO});
        return map;
    }

    @CtpUserComment("默认返回 USERNAME_PASSWORD")
    default CtpUserSpiAuthTokenEnum getSuccessAuthTokenEnum() {
        return CtpUserSpiAuthTokenEnum.USERNAME_PASSWORD;
    }

    @CtpUserComment("三方退出参数处理")
    default CtpUserSpiThirdLogoutDto getThirdLogoutParams(Map<String, Object> thirdLogoutMap) {
        return null;
    }
}
```

## 返回值：CtpUserSpiLoginUserInfoDto [FACT ✅]

```java
// 关键字段（构建返回对象时使用）
CtpUserSpiLoginUserInfoDto dto = new CtpUserSpiLoginUserInfoDto();
dto.setCtpUserSpiUserDtoList(userDtoList);  // 用户列表
dto.setThirdToken("xxx");                    // 三方 token（可选，用于刷新）
dto.setThirdTokenConfigMap(configMap);       // token 配置（可选）
```

## 用户对象：CtpUserSpiUserDto [FACT ✅]

```java
CtpUserSpiUserDto userDto = new CtpUserSpiUserDto();
userDto.setId(memberId);           // V8 用户 ID（Long）
userDto.setLoginName("xxx");       // 登录名
userDto.setCode("xxx");            // 用户编号
userDto.setName("xxx");            // 用户姓名
```

## 方法说明

| 方法 | 必须 | 参数 | 返回 | 语义 |
|------|------|------|------|------|
| getRequestParaKey | ✅ | 无 | `String` | request 中 code/ticket 的 key 名 |
| getSsoLoginUrl | ✅ | `HttpServletRequest, String` | `String` | 三方 SSO 登录地址 |
| getUserLoginInfo | ✅ | `HttpServletRequest, String` | `CtpUserSpiLoginUserInfoDto` | 核心：获取用户信息 |
| setServerEnv | 可选 | `CtpUserSpiServerEnvDto` | void | 设置服务环境配置 |
| sendVerifyCode | 可选 | `String mobile` | `Boolean` | 发送短信验证码 |
| shortLinkMode | 可选 | 无 | `ShortLinkModeEnum` | 短链接模式 |
| getEncodeLogoutRedirectUrl | 可选 | 无 | `String` | 三方登出重定向地址 |
| thirdSsoLogout | 可选 | `HttpServletRequest, String` | void | 三方登出逻辑 |
| getUserLoginInfoForMobile | 可选 | `String, Map, CtpUserSpiAuthTokenEnum` | `CtpUserSpiLoginUserInfoDto` | 手机端登录 |
| tokenExpiredSetNull | 可选 | 无 | `boolean` | token 过期返回空 |
| rebuildCtpUserDtoList | 可选 | `List<CtpUserSpiUserDto>` | `Long` | 多用户时选择哪个 |
| refreshThirdTokenByConfig | 可选 | `String, Map` | `CtpUserSpiThirdTokenDto` | 刷新三方 token |
| get4aTokenKey | 可选 | 无 | `String` | 缓存 4a token 的 key |
| getTidCode | 可选 | 无 | `String` | 上下文租户赋值 |
| mapSupportsAuthTokenEnum | 可选 | 无 | `Map<String, CtpUserSpiAuthTokenEnum[]>` | 登录认证条件 |
| getSuccessAuthTokenEnum | 可选 | 无 | `CtpUserSpiAuthTokenEnum` | 默认 USERNAME_PASSWORD |
| getThirdLogoutParams | 可选 | `Map` | `CtpUserSpiThirdLogoutDto` | 三方退出参数 |

## 代码骨架

```java
package com.seeyon.extend.spi.sso.{project_id};

import com.seeyon.ctp.user.annotation.CtpUserChannelRouter;
import com.seeyon.ctp.user.api.sso.CtpUserSsoAuthProviderService;
import com.seeyon.ctp.user.dto.*;
import com.seeyon.ctp.user.enums.CtpUserSpiAuthTokenEnum;
import com.seeyon.ctp.user.exception.CtpUserSpiSsoException;
import com.seeyon.ctp.user.util.CtpUserSpiUtils;
import lombok.extern.slf4j.Slf4j;

import javax.servlet.http.HttpServletRequest;
import java.util.*;

@Slf4j
@CtpUserChannelRouter("{channel_type}")
public class {Prefix}SsoAuthProviderService implements CtpUserSsoAuthProviderService {

    private CtpUserSpiServerEnvDto serverEnv;

    @Override
    public void setServerEnv(CtpUserSpiServerEnvDto dto) {
        this.serverEnv = dto;
        log.info("{project_name_cn} SSO 初始化, 域名: {}", dto.getServerDomain());
    }

    @Override
    public String getRequestParaKey() {
        return "{code_param_name}"; // 如 "code" 或 "ticket"
    }

    @Override
    public String getSsoLoginUrl(HttpServletRequest request, String encodeRedirectUrl) {
        // 拼接三方认证中心登录地址
        // 示例：{auth_login_url}?client_id={clientId}&redirect_uri={encodeRedirectUrl}&response_type=code
        String clientId = CtpUserSpiUtils.getPropertyByName("{client_id_nacos_key}");
        String loginUrl = "{auth_login_url}"
            + "?client_id=" + clientId
            + "&redirect_uri=" + encodeRedirectUrl
            + "&response_type=code";
        log.info("{project_name_cn} SSO 登录地址: {}", loginUrl);
        return loginUrl;
    }

    @Override
    public CtpUserSpiLoginUserInfoDto getUserLoginInfo(
            HttpServletRequest request, String encodeRedirectUrl)
            throws CtpUserSpiSsoException {
        try {
            // 1. 从 request 获取 code
            String code = request.getParameter(getRequestParaKey());
            if (code == null || code.isEmpty()) {
                throw new CtpUserSpiSsoException("未获取到认证码");
            }

            // 2. 用 code 换取 token
            String token = fetchToken(code);

            // 3. 用 token 获取用户信息
            String thirdUserId = fetchUserInfo(token);

            // 4. 匹配 V8 用户
            CtpUserSpiUserDto userDto = matchV8User(thirdUserId);
            if (userDto == null) {
                throw new CtpUserSpiSsoException("用户不存在或未绑定");
            }

            // 5. 构建返回
            CtpUserSpiLoginUserInfoDto result = new CtpUserSpiLoginUserInfoDto();
            result.setCtpUserSpiUserDtoList(Collections.singletonList(userDto));
            return result;

        } catch (CtpUserSpiSsoException e) {
            throw e;
        } catch (Exception e) {
            log.error("{project_name_cn} SSO 认证失败", e);
            throw new CtpUserSpiSsoException("认证失败: " + e.getMessage());
        }
    }

    @Override
    public String getEncodeLogoutRedirectUrl() {
        // 返回三方登出地址（URLEncode 后）
        try {
            String logoutUrl = CtpUserSpiUtils.getPropertyByName("{logout_url_nacos_key}");
            return java.net.URLEncoder.encode(logoutUrl, "UTF-8");
        } catch (Exception e) {
            log.error("{project_name_cn} SSO 登出地址编码失败", e);
            return null;
        }
    }

    @Override
    public Map<String, CtpUserSpiAuthTokenEnum[]> mapSupportsAuthTokenEnum() {
        Map<String, CtpUserSpiAuthTokenEnum[]> map = new HashMap<>();
        map.put("WEB", new CtpUserSpiAuthTokenEnum[]{CtpUserSpiAuthTokenEnum.SPI_SSO});
        // 如需移动端支持：
        // map.put("MOBILE", new CtpUserSpiAuthTokenEnum[]{CtpUserSpiAuthTokenEnum.SPI_SSO});
        return map;
    }

    // ===== 私有方法 =====

    private String fetchToken(String code) {
        // TODO: 调用三方 token 接口
        // 使用 hutool HttpUtil 或 RestTemplate
        return "";
    }

    private String fetchUserInfo(String token) {
        // TODO: 调用三方用户信息接口
        return "";
    }

    private CtpUserSpiUserDto matchV8User(String thirdUserId) {
        // TODO: 通过 OpenAPI 查询 V8 用户
        // 常用 API：
        //   /organization/member/code — 通过编号查
        //   /organization/base/member/selectMemberListByCondition — 条件查
        return null;
    }
}
```

## spring.factories

```properties
com.seeyon.ctp.user.api.sso.CtpUserSsoAuthProviderService=com.seeyon.extend.authsso.unified.YourUnifiedAuthProviderService
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["ctp-user"]
}
```

## Nacos 配置模板

```yaml
# ctp-user 微服务 Nacos 配置
seeyon:
  auth:
    type: spisso          # 固定值，开启 SPI 认证
  thirdauth:
    type: {channel_type}  # 对应 @CtpUserChannelRouter 的值
  {project_id}:
    clientId: {third_auth_client_id}         # 三方应用 ID
    clientSecret: CHANGE_ME_IN_NACOS  # 三方应用密钥
    loginUrl: {third_login_url}         # 三方登录地址
    tokenUrl: {third_token_url}         # token 接口地址
    userInfoUrl: {third_user_info_url}      # 用户信息接口地址
    logoutUrl: {third_logout_url}        # 三方登出地址
```


## 重启服务

ctp-user
