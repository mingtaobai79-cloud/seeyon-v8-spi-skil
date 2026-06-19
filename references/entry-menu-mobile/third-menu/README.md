# 三方菜单 / AbstractThirdMenuService

> **Evidence: FACT ✅** — 接口签名、DTO、枚举来自 `ctp-user-api-5.3.351.jar` CFR 反编译。
> Source: jar 反编译 + 语雀 0095

## 场景

将三方系统中的菜单集成到 V8 导航中。

适用版本：3.12 及以上版本。

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
package com.seeyon.ctp.user.api.menu;

import com.seeyon.ctp.user.dto.menu.CtpUserThirdNavFrontDto;
import com.seeyon.ctp.user.dto.menu.ThirdMenuParamDto;
import com.seeyon.ctp.user.enums.MenuPositionEnum;
import java.util.List;

public abstract class AbstractThirdMenuService {
    public MenuPositionEnum position() {
        return MenuPositionEnum.TAIL;
    }
    public abstract List<CtpUserThirdNavFrontDto> selectThirdMenu(ThirdMenuParamDto var1);
}
```

## 方法说明

| 方法 | 参数 | 返回 | 语义 |
|------|------|------|------|
| position | 无 | `MenuPositionEnum` | 菜单位置（HEAD/TAIL），默认 TAIL |
| selectThirdMenu | `ThirdMenuParamDto` | `List<CtpUserThirdNavFrontDto>` | 返回三方菜单列表（abstract，必须实现） |

## DTO 定义 [FACT ✅]

### ThirdMenuParamDto（入参）

```java
package com.seeyon.ctp.user.dto.menu;

@DtoInfo("三方菜单请求参数")
public class ThirdMenuParamDto extends BaseDto {
    Integer size;           // 每次查询菜单大小
    Integer startIndex;     // 开始的索引
    Long orgId;             // 机构 ID
    Long userId;            // 用户 ID
    Boolean isNewStyle;     // 是否是门户新样式，默认 false
}
```

### CtpUserThirdNavFrontDto（返回）

```java
package com.seeyon.ctp.user.dto.menu;

@DtoInfo("前端用户导航栏用到的dto")
public class CtpUserThirdNavFrontDto extends BaseDto {
    Long id;                // 菜单 ID
    String title;           // 名称
    String icon;            // 图标，默认 ""
    String url;             // 跳转链接
    String openType;        // 打开方式: WORKSPACE/NEWWINDOW/MAIN，默认 ""
    String appId;           // 所属应用
    @Valid List<CtpUserThirdNavFrontDto> children;  // 子节点，默认空 List
    Long parentId;          // 父菜单 ID
    String dataType;        // 数据型资源的类型
}
```

### MenuPositionEnum [FACT ✅]

```java
package com.seeyon.ctp.user.enums;

public enum MenuPositionEnum implements Messageable {
    HEAD(0),
    TAIL(2);
}
```

## 代码骨架

```java
package com.seeyon.extend.spi.menu;

import com.seeyon.ctp.user.api.menu.AbstractThirdMenuService;
import com.seeyon.ctp.user.dto.menu.CtpUserThirdNavFrontDto;
import com.seeyon.ctp.user.dto.menu.ThirdMenuParamDto;
import com.seeyon.ctp.user.enums.MenuPositionEnum;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.ArrayList;
import java.util.List;

/**
 * 三方菜单 SPI 实现
 * <p>将三方系统菜单集成到 V8 导航。</p>
 */
public class CustomThirdMenuService extends AbstractThirdMenuService {

    private static final Logger log = LoggerFactory.getLogger(CustomThirdMenuService.class);

    @Override
    public MenuPositionEnum position() {
        return MenuPositionEnum.TAIL;
    }

    @Override
    public List<CtpUserThirdNavFrontDto> selectThirdMenu(ThirdMenuParamDto paramDto) {
        log.debug("[third-menu] selectThirdMenu called, userId={}, orgId={}",
            paramDto.getUserId(), paramDto.getOrgId());
        List<CtpUserThirdNavFrontDto> menus = new ArrayList<>();
        // TODO: 从三方系统获取菜单列表
        // 示例：
        // CtpUserThirdNavFrontDto menu = new CtpUserThirdNavFrontDto();
        // menu.setTitle("三方系统");
        // menu.setUrl("https://third-party.example.com");
        // menu.setOpenType("NEWWINDOW");
        // menus.add(menu);
        return menus;
    }
}
```

## spring.factories

```properties
com.seeyon.ctp.user.api.menu.AbstractThirdMenuService=com.seeyon.extend.spi.menu.CustomThirdMenuService
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["ctp-user"]
}
```

## Nacos 配置

本 SPI 不需要额外 Nacos 配置。如果业务逻辑需要读取配置，通过 `CtpUserSpiUtils.getPropertyByName(...)` 获取。

## 重启服务

ctp-user
