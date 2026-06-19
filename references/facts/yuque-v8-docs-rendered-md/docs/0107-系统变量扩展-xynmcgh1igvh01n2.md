---
title: "系统变量扩展"
source: "https://www.yuque.com/seeyonkk/v8/xynmcgh1igvh01n2"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 系统变量扩展

> Source: https://www.yuque.com/seeyonkk/v8/xynmcgh1igvh01n2

作者：陈晓东

时间：2025.12.31

支持版本：5.6.30及以上版本

使用场景：在计算条件弹框组件中添加系统变量

实现SystemVariableSPIService接口

# 1、SPI开发

SPI开发规范，参考：开发准备

# 2、添加依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>boot-starter-formula</artifactId>
  <version>5.30.6</version>
</dependency>
```

# 3、示例代码

```java
public class DemoSPISystemVariableService implements SystemVariableSPIService {
    @SPISystemVariable(
        type = SPISystemVariableType.ORGANIZATION ,
        description = "SPI登录人id系统变量静态",
        relationEntity = "com.seeyon.organization.domain.core.entity.OrgMember")
    public static Long getCustomLoginUserId(){
        //演示: 静态方法扩展系统变量
        Long userId = Apps.getRequestContext().getUserId();;
        return userId;
    }
    @SPISystemVariable(
        type = SPISystemVariableType.ORGANIZATION ,
        description = "SPI登录人id系统变量实例方法",
        relationEntity = "com.seeyon.organization.domain.core.entity.OrgMember")
    public Long getCustomLoginUserIdInstance(){
        //演示 1.实例方法注册系统变量  2.在SPI系统变量方法中获取平台组件中bean，也可以获取其他SPI实现类
        ExpressionService expressionService = Apps.getApplicationContext().getBean(ExpressionService.class);
        return (Long)expressionService.getSystemVariableResultByName("currentUserId");
    }
    @SPISystemVariable(
        type = SPISystemVariableType.ORGANIZATION ,
        description = "SPI登录人id系统变量实例方法2",
        relationEntity = "com.seeyon.organization.domain.core.entity.OrgMember")
    public Long getCustomLoginUserIdInstance2(){
        //演示 1.实例方法注册系统变量  2.获取请求上下文信息
        return Apps.getRequestContext().getUserId();
    }
}
```

# 4、SPISystemVariable注解属性描述：

| 属性名 | 描述 | 用法 |
| --- | --- | --- |
| type | 系统变量类型 | 目前系统变量只支持日期、组织模型两种类型 |
| description | 系统变量描述 | 可以直接写描述，也可以写国际化词条，但是需要在后台管理中设置对应词条信息 |
| relationEntity | 关联实体fullName | 如果返回值是关联实体比如人员ID、机构ID等数据，需要在relationEntity中写明对应关联实体的fullName, 比如下面demo中获取人员ID，relationEntity需要标明: com.seeyon.organization.domain.core.entity.OrgMember |
| sort | 排序 | SPI扩展的系统变量默认都是排在预制系统变量后面，这里是指所有SPI系统变量中的排序(按sort从小到大顺序)。 |
| hidden | 是否隐藏 | 如果某些扩展的SPI系统变量后续不想让用户选择了，但是直接去掉又会影响在途数据，可以隐藏掉。 |

# 5、使用限制

1.方法必须是public的，可以是静态方法，也可以是实例方法

2.方法必须添加@SPISystemVariable注解修饰

3.方法返回值类型只支持基本类型和基本类型集合，不支持复杂DTO对象

4.系统变量方法不支持参数

# 6、效果图

<img src="https://cdn.nlark.com/yuque/0/2025/png/55453183/1767158849948-88aeb2d6-0eb9-41d7-a29b-db2f66aacf23.png" width="1215">

# 7、服务重启

重启UDC应用对应的服务
