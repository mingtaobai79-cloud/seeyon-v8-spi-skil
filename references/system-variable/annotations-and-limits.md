# 系统变量注解与使用限制

> 来源：语雀《系统变量扩展》rendered-md。Evidence：OBSERVATION。

## @SPISystemVariable 属性

| 属性名 | 描述 | 用法 |
| --- | --- | --- |
| `type` | 系统变量类型 | 目前系统变量只支持日期、组织模型两种类型。 |
| `description` | 系统变量描述 | 可以直接写描述，也可以写国际化词条；若写国际化词条，需要在后台管理中设置对应词条信息。 |
| `relationEntity` | 关联实体 fullName | 如果返回值是关联实体，比如人员 ID、机构 ID 等，需要写明对应关联实体 fullName。文档示例：`com.seeyon.organization.domain.core.entity.OrgMember`。 |
| `sort` | 排序 | SPI 扩展的系统变量默认排在预制系统变量后面；这里控制所有 SPI 系统变量之间按 `sort` 从小到大排序。 |
| `hidden` | 是否隐藏 | 某些扩展变量后续不想让用户选择，但直接去掉会影响在途数据时，可以隐藏。 |

## 方法限制

1. 方法必须是 `public`。
2. 可以是静态方法，也可以是实例方法。
3. 方法必须添加 `@SPISystemVariable` 注解。
4. 方法返回值类型只支持基本类型和基本类型集合。
5. 不支持复杂 DTO 对象返回。
6. 系统变量方法不支持参数。

## 文档示例抽象

```java
public class DemoSPISystemVariableService implements SystemVariableSPIService {
    @SPISystemVariable(
        type = SPISystemVariableType.ORGANIZATION,
        description = "SPI登录人id系统变量静态",
        relationEntity = "com.seeyon.organization.domain.core.entity.OrgMember")
    public static Long getCustomLoginUserId(){
        return Apps.getRequestContext().getUserId();
    }
}
```

文档还展示了实例方法形态：

```java
public Long getCustomLoginUserIdInstance(){
    ExpressionService expressionService = Apps.getApplicationContext().getBean(ExpressionService.class);
    return (Long) expressionService.getSystemVariableResultByName("currentUserId");
}
```

## 生成代码前必须确认

- `SystemVariableSPIService` full qualified name。
- `SPISystemVariable` full qualified name。
- `SPISystemVariableType` full qualified name 与枚举值，比如 `ORGANIZATION`、日期类型对应枚举值。
- `Apps` full qualified name。
- `ExpressionService` full qualified name。
- 目标 V8 版本是否兼容 `boot-starter-formula:5.30.6`。

没有 jar/source/Contract Index 证据时，只能把这些作为 OBSERVATION/HYPOTHESIS 写入交付报告，不能宣称 FACT。
