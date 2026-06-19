# ticket 返回人员信息自定义 / CustomUserInfoService

> Evidence: FACT ✅ 用户提供的反编译接口源码。语雀 `0096-ticket认证返回人员信息自定义-pazygl1cot73gavl.md` 为 OBSERVATION。

## 场景

ticket 认证返回人员信息自定义，对 ticket 换取的用户信息 map 进行过滤/包装/脱敏/增强。

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>ctp-user-api</artifactId>
  <version>5.0.3</version>
</dependency>
```

## 接口定义 [FACT ✅]

```java
package com.seeyon.ctp.user.api.user;

public interface CustomUserInfoService {
    /**
     * 过滤/自定义 ticket 认证返回的人员信息
     * @param map ticket 认证返回的原始用户信息 map
     * @return 处理后的用户信息 map
     */
    Map<String, Object> filterCustomUserInfo(Map<String, Object> map);
}
```

## 方法说明

| 方法 | 作用 |
|------|------|
| `filterCustomUserInfo(Map<String, Object> map)` | 对 ticket 认证返回的用户信息 map 进行过滤/包装/脱敏/增强 |

## Nacos 配置

```yaml
# ctp-user 微服务 Nacos 配置
seeyon:
  ticket-custom:
    enabled: true
    # 需要脱敏的字段（逗号分隔）
    desensitize-fields: mobile,email
    # 需要额外添加的字段（JSON 格式）
    extra-fields: ""
    # 需要移除的字段（逗号分隔）
    remove-fields: ""
```

## spring.factories

```properties
com.seeyon.ctp.user.api.user.CustomUserInfoService=\
com.seeyon.extend.spi.{project_id}.{Prefix}CustomUserInfoService
```

## 代码骨架

```java
package com.seeyon.extend.spi.{project_id};

import com.seeyon.ctp.user.api.user.CustomUserInfoService;
import com.seeyon.ctp.user.util.CtpUserSpiUtils;
import lombok.extern.slf4j.Slf4j;

import java.util.LinkedHashMap;
import java.util.Map;

/**
 * {project_name_cn} ticket 返回人员信息自定义
 *
 * 场景：ticket 认证返回人员信息时，对原始 map 进行过滤/包装/脱敏/增强
 * V8 调用时机：ticket 换取用户信息后，框架调用 filterCustomUserInfo 处理返回结果
 * 返回语义：处理后的用户信息 map
 *
 * 默认行为：原样返回 map，不做任何修改。
 * 现场明确 ticket 返回字段后，再补充包装/脱敏/增强逻辑。
 */
@Slf4j
public class {Prefix}CustomUserInfoService implements CustomUserInfoService {

    @Override
    public Map<String, Object> filterCustomUserInfo(Map<String, Object> map) {
        if (map == null) {
            log.warn("[ticket] filterCustomUserInfo 收到 null map");
            return null;
        }

        log.info("[ticket] filterCustomUserInfo, 原始字段数: {}", map.size());

        // 默认不假设 ticket 返回字段，原样返回 map。
        // 现场明确字段后，再在这里做包装/脱敏/增强。
        //
        // 示例扩展点：
        //
        // 1. 脱敏手机号：
        //    String mobile = (String) map.get("mobile");
        //    if (mobile != null && mobile.length() == 11) {
        //        map.put("mobile", mobile.substring(0, 3) + "****" + mobile.substring(7));
        //    }
        //
        // 2. 添加额外字段：
        //    map.put("customField", "customValue");
        //
        // 3. 移除敏感字段：
        //    map.remove("idCard");
        //
        // 4. 包装返回结构：
        //    Map<String, Object> wrapped = new LinkedHashMap<>();
        //    wrapped.put("userInfo", map);
        //    wrapped.put("timestamp", System.currentTimeMillis());
        //    return wrapped;

        return map;
    }
}
```

## 字段包装/脱敏扩展指南

现场明确 ticket 返回 map 字段后，按以下模式扩展：

1. **脱敏**：手机号、邮箱、身份证号等敏感字段做掩码处理。
2. **增强**：添加三方系统特有的字段（如部门名称、角色标识）。
3. **过滤**：移除不需要的字段，减少返回数据量。
4. **包装**：将原始 map 嵌套到更大的返回结构中。

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["ctp-user"]
}
```

## 重启服务

`ctp-user`
