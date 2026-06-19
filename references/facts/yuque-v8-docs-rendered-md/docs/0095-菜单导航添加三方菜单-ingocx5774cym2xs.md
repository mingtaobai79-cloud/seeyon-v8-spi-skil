---
title: "菜单导航添加三方菜单"
source: "https://www.yuque.com/seeyonkk/v8/ingocx5774cym2xs"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 菜单导航添加三方菜单

> Source: https://www.yuque.com/seeyonkk/v8/ingocx5774cym2xs

作者：陈晓东

时间：2026.5.27

适用版本：3.12及以上版本

场景：将三方系统中的菜单集成到V8导航中

# 1、SPI开发

SPI开发规范，参考：
开发准备

# 2、添加依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>ctp-user-api</artifactId>
  <version>3.12.1</version>
</dependency>
```

# 3、客开实现方法

实现spi接口说明：com.seeyon.ctp.user.api.menu.AbstractThirdMenuService

```
/**
* 三方菜单接入
*
* @author liu xiong
* @date 2024/6/11
*/
public abstract class AbstractThirdMenuService {
    /**
  * 位置, head - 头部， tail -尾部
  */
    public MenuPositionEnum position() {
        return MenuPositionEnum.TAIL;
    }
    /**
  * 获取三方菜单
  *
  * @param paramDto  请求参数
  * @return  返回三方菜单
  */
    public abstract List<CtpUserThirdNavFrontDto> selectThirdMenu(ThirdMenuParamDto paramDto);
}
```

入参说明：

```java
/**
* 三方菜单请求参数
*
* @author liu xiong
* @date 2024/7/16
*/
@Getter
@Setter
@DtoInfo(value = "三方菜单请求参数")
public class ThirdMenuParamDto extends BaseDto {
 private static final long serialVersionUID = -1487542722299819207L;
 @DtoAttribute(value = "每次查询菜单大小", example = "20")
 private Integer size;
 @DtoAttribute(value = "开始的索引", example = "0")
 private Integer startIndex;
 @DtoAttribute(value = "机构id", example = "343543")
 private Long orgId;
 @DtoAttribute(value = "用户id", example = "343543")
 private Long userId;
 @DtoAttribute(value = "是否是门户新样式", example = "false")
 private Boolean isNewStyle = false;
}
```

返回参数说明：

```java
/**
* 前端用户导航栏用到的dto
*
* @author 敬磊
* @version 1.0
* @date 2022/9/21 14:44
*/
@Setter
@Getter
@DtoInfo(value = "前端用户导航栏用到的dto")
public class CtpUserThirdNavFrontDto extends BaseDto {
 private static final long serialVersionUID = 7020235073887850881L;
 @DtoAttribute(value = "菜单Id", example = "123456", hidden = true)
 private Long id;
 @DtoAttribute(value = "名称", example = "资源名称")
 private String title;
 @DtoAttribute(value = "图标", example = "icon")
 private String icon = "";
 @DtoAttribute(value = "跳转链接", example = "/demo-order/order-info")
 private String url;
 @DtoAttribute(value = "打开方式:WORKSPACE,NEWWINDOW,MAIN", example = "WORKSPACE")
 private String openType = "";
 @DtoAttribute(value = "所属应用", example = "portal")
 private String appId;
 @Valid
 @DtoAttribute(value = "子节点")
 private List<CtpUserThirdNavFrontDto> children = Lists.newArrayList();
 @DtoAttribute(value = "父菜单id", example = "26565685986454")
 private Long parentId;
 @DtoAttribute(value = "数据型资源的类型", example = "BIZ_HOME")
 private String dataType;
}
```

# 4、重启服务

重启ctp-user服务
