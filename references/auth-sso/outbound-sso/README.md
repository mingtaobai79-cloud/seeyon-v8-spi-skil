# V8→三方单点 / SsoService

> Evidence: FACT ✅ from `references/auth-sso/sso-connector/README.md`（已沉淀完整接口定义）。语雀 `0110-V8单点到三方` 为 OBSERVATION。

## 场景

V8 菜单/磁贴/流程/待办跳转三方系统时，通过 SPI 生成三方系统登录 URL。

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
package com.seeyon.cip.connector.api.sso;

public interface SsoService {

    /**
     * 获取唯一标识（全英文）
     * 类名 = name + "SsoServiceImpl"
     */
    String getName();

    /**
     * 获取中文名称
     */
    String getTypeCaption();

    /**
     * 单点登录（核心方法）
     * @param url          外部跳转地址或标识
     * @param json         前端页面传递的配置数据
     * @param userMap      用户信息 map（needUserBind=true 时才有数据）
     * @param clientType   客户端类型（PC/移动端）
     * @param extendParams 扩展参数
     * @return 最终的单点登录跳转地址
     */
    String login(String url, String json, Map<String, Object> userMap,
                 SsoClientTypeEnum clientType, Map<String, Object> extendParams);

    /**
     * 校验前端配置参数
     */
    void check(String config);

    /**
     * 获取前端配置页面 JSON
     */
    String getPageJson();

    /**
     * 排序号
     */
    Integer getSortNo();

    /**
     * 是否需要用户绑定操作
     * 返回 true 时 login 的 userMap 才有用户数据
     */
    boolean needUserBind();
}
```

## 方法说明

| 方法 | 作用 |
|------|------|
| `getName()` | 英文唯一标识；类名必须等于 `getName() + "SsoServiceImpl"` |
| `getTypeCaption()` | 前端显示的中文名称 |
| `login(url, json, userMap, clientType, extendParams)` | 核心方法：生成三方系统最终登录 URL |
| `check(config)` | 保存配置时校验参数 |
| `getPageJson()` | 定义 V8 前端配置表单 |
| `getSortNo()` | 前端排序 |
| `needUserBind()` | 是否需要用户绑定；true 时 `userMap` 才有绑定用户数据 |

## userMap 字段说明

| Key | 说明 |
|-----|------|
| innerUserId | 内部用户 ID |
| innerUserName | 内部用户名称 |
| innerUserCODE | 内部用户编号 |
| innerUserLoginName | 内部用户登录名 |
| outerUser | 外部用户账户 |
| outerUserId | 外部用户 ID |
| innerUserEmail | 内部用户邮箱 |
| innerUserPhone | 内部用户手机号 |
| innerUserOfficeNumber | 内部用户办公电话 |
| innerUserBankAccount | 内部用户银行账户 |
| innerUserOrgId | 内部用户组织编号 |

## getPageJson 格式

```json
{
    "caption": "认证类型中文名",
    "type": "认证类型英文标识",
    "extensionProperties": [
        {
            "colProps": { "span": 12 },
            "componentType": "Input",
            "componentProps": { "placeholder": "请输入" },
            "validateFirst": true,
            "rules": [
                { "required": true, "message": "请输入xxx" },
                { "pattern": "^[^\\s]*$", "message": "禁止输入空格" },
                { "type": "string", "max": 255, "message": "最多255个字符" }
            ],
            "caption": "字段中文名",
            "defaultValue": "",
            "name": "字段英文标识"
        }
    ]
}
```

## Nacos 配置

```yaml
# cip-connector 微服务 Nacos 配置
seeyon:
  {project_id}:
    defaultJumpUrl: https://third.example.com/sso/login
    secretKey: CHANGE_ME_IN_NACOS
    encryptType: RSA  # RSA / AES / MD5 / DIRECT
```

## spring.factories

```properties
com.seeyon.cip.connector.api.sso.SsoService=\
com.seeyon.extend.spi.{project_id}.{Prefix}SsoServiceImpl
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["cip-connector"]
}
```

或指定应用编码：

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["{应用编码}"]
}
```

## 代码骨架

```java
package com.seeyon.extend.spi.{project_id};

import com.seeyon.boot.util.JsonUtils;
import com.seeyon.boot.util.StringUtils;
import com.seeyon.cip.connector.api.sso.SsoService;
import com.seeyon.cip.connector.enums.SsoClientTypeEnum;
import lombok.Getter;
import lombok.Setter;
import lombok.extern.slf4j.Slf4j;

import javax.validation.constraints.NotBlank;
import java.util.Map;

/**
 * {project_name_cn} 单点登录服务实现类
 *
 * 场景：V8 菜单/磁贴/流程/待办跳转三方系统
 * V8 调用时机：用户点击跳转链接时，框架调用 login 生成最终 URL
 * 三方系统：{third_system_name}
 * 返回语义：三方系统登录 URL（含加密/签名后的用户标识）
 */
@Slf4j
public class {Prefix}SsoServiceImpl implements SsoService {

    @Override
    public String getName() {
        return "{sso_name}";  // 类名必须等于 getName() + "SsoServiceImpl"
    }

    @Override
    public String getTypeCaption() {
        return "{sso_caption}";
    }

    @Override
    public String login(String url, String json, Map<String, Object> userMap,
                        SsoClientTypeEnum clientType, Map<String, Object> extendParams) {
        try {
            // 1. 解析前端配置
            {Prefix}SsoDto ssoConfig = JsonUtils.fromJson(json, {Prefix}SsoDto.class);

            // 2. 如果 url 为空，使用默认跳转地址
            if (StringUtils.isBlank(url)) {
                url = ssoConfig.getDefaultJumpUrl();
            }

            // 3. 获取用户信息
            String loginName = (String) userMap.get("innerUserLoginName");
            String userCode = (String) userMap.get("innerUserCODE");
            log.info("[outbound-sso] {project_name_cn} SSO, 用户: {}, URL: {}", loginName, url);

            // 4. 构建单点登录地址
            String ssoUrl = buildSsoUrl(url, loginName, userCode, ssoConfig);

            log.info("[outbound-sso] {project_name_cn} SSO 最终地址长度: {}", ssoUrl.length());
            return ssoUrl;

        } catch (Exception e) {
            log.error("[outbound-sso] {project_name_cn} SSO 失败", e);
            throw new RuntimeException("单点登录失败: " + e.getMessage(), e);
        }
    }

    @Override
    public void check(String config) {
        try {
            {Prefix}SsoDto ssoConfig = JsonUtils.fromJson(config, {Prefix}SsoDto.class);
            if (StringUtils.isBlank(ssoConfig.getDefaultJumpUrl())) {
                throw new RuntimeException("跳转地址不能为空");
            }
        } catch (Exception e) {
            throw new RuntimeException("配置参数校验失败: " + e.getMessage(), e);
        }
    }

    @Override
    public String getPageJson() {
        return "{\"caption\":\"{sso_caption}\",\"type\":\"{sso_name}\","
"
            + "\"extensionProperties\":[
"
            + "{\"colProps\":{\"span\":12},\"componentType\":\"Input\","
"
            + "\"componentProps\":{\"placeholder\":\"请输入\"},
"
            + "\"validateFirst\":true,
"
            + "\"rules\":[{\"required\":true,\"message\":\"请输入跳转地址\"}],
"
            + "\"caption\":\"跳转地址\",\"defaultValue\":\"\",\"name\":\"defaultJumpUrl\"}
"
            + "]}";
    }

    @Override
    public Integer getSortNo() {
        return 99;
    }

    @Override
    public boolean needUserBind() {
        return true;  // true 时 userMap 才有用户数据
    }

    // ===== 私有方法 =====

    private String buildSsoUrl(String url, String loginName, String userCode,
                                {Prefix}SsoDto config) {
        // TODO: 根据三方系统认证方式实现
        // 常见模式：
        //
        // 1. 直接拼接参数：
        //    return url + "?user=" + loginName + "&token=" + generateToken(loginName);
        //
        // 2. RSA 加密（帆软模式）：
        //    String payload = "{\"username\":\"" + loginName + "\",\"issueTime\":" + timestamp + "}";
        //    String encrypted = RSAEncrypt.encrypt(payload, publicKey);
        //    return url + "&ssoToken=" + URLEncoder.encode(encrypted, "UTF-8");
        //
        // 3. MD5 签名：
        //    String sign = md5(loginName + timestamp + secret);
        //    return url + "?user=" + loginName + "&timestamp=" + timestamp + "&sign=" + sign;
        //
        // 4. AES 加密：
        //    String encrypted = AESUtil.encrypt(loginName, key);
        //    return url + "?token=" + URLEncoder.encode(encrypted, "UTF-8");
        return url;
    }

    // ===== DTO =====

    @Getter
    @Setter
    public static class {Prefix}SsoDto {
        @NotBlank
        private String defaultJumpUrl;
        // 根据 page_json_fields 添加更多字段
    }
}
```

## 配置步骤（V8 管理后台）

1. **创建集成应用** → 获取应用编码
2. **单点登录设置** → 选择认证类型 → 填写配置参数
3. **配置菜单** → 绑定跳转地址
4. **发布应用**
5. **角色授权**

## 重启服务

`cip-connector`
