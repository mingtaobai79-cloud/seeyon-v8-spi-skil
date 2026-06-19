# 系统变量扩展域共享资源

> Source snapshot: `references/facts/yuque-v8-docs-rendered-md/docs/0107-系统变量扩展-xynmcgh1igvh01n2.md`
> Evidence: OBSERVATION。

## 域概述

系统变量扩展用于在"计算条件弹框组件"中添加自定义系统变量。

- 推荐模块名：`spi-system-variable`
- 核心接口短名：`SystemVariableSPIService`
- 核心注解短名：`@SPISystemVariable`
- 类型枚举短名：`SPISystemVariableType`
- 文档标注支持版本：`5.6.30 及以上版本`
- 文档示例依赖：`com.seeyon:boot-starter-systemvariable:5.3.313`
- 生效验证入口：计算条件弹框组件
- 部署影响：重启 UDC 应用对应服务

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>boot-starter-systemvariable</artifactId>
  <version>5.3.313</version>
</dependency>
```

注意：版本号是文档示例，不等于所有 V8 版本通用。生成工程时优先使用现场父 POM / 私服 BOM / 已有依赖版本，不要盲目固定 `5.3.313`。

## `@SPISystemVariable` 注解属性

| 属性名 | 描述 | 生成/使用规则 |
| --- | --- | --- |
| `type` | 系统变量类型 | 文档写明目前只支持"日期、组织模型"两种。示例只出现 `SPISystemVariableType.ORGANIZATION`。日期枚举值未在文档中出现，生成前必须由 jar/source 确认。 |
| `description` | 系统变量描述 | 可直接写中文描述，也可写国际化词条；如果写国际化词条，需要在后台管理中维护对应词条。 |
| `relationEntity` | 关联实体 fullName | 返回人员 ID、机构 ID 等组织模型关联数据时填写对应实体 fullName。文档示例：`com.seeyon.organization.domain.core.entity.OrgMember`。 |
| `sort` | 排序 | SPI 扩展变量默认排在预制系统变量后；多个 SPI 扩展变量之间按 `sort` 从小到大排序。 |
| `hidden` | 是否隐藏 | 后续不想让用户继续选择某变量，但删除会影响在途数据时，使用隐藏。 |

## 类型规则

### 组织模型类型

```java
type = SPISystemVariableType.ORGANIZATION
```

返回人员 ID 时：

```java
relationEntity = "com.seeyon.organization.domain.core.entity.OrgMember"
```

生成器约束：
- 如果变量语义是"当前登录人/发起人/部门/机构/岗位"等组织模型对象，应优先按组织模型类型处理。
- 如果返回的是关联实体 ID，必须补 `relationEntity`。
- `relationEntity` 值必须是平台实体 fullName，不是 Java 类短名，也不是表名。

### 日期类型

文档只说支持日期类型，但没有给出日期枚举值和示例。

生成器约束：
- 未确认枚举前，不要凭空写 `DATE`、`DATETIME`、`TIME`。
- 可以在交付报告中标注"日期类型待目标版本 jar/source 确认"。

## 方法限制

文档明确：

1. 方法必须是 `public`。
2. 方法可以是静态方法，也可以是实例方法。
3. 方法必须添加 `@SPISystemVariable` 注解。
4. 方法返回值类型只支持基本类型和基本类型集合。
5. 不支持复杂 DTO 对象。
6. 系统变量方法不支持参数。

生成器强校验：

```text
public ✓
public static ✓
private/protected ✗
参数个数 == 0 ✓
参数个数 > 0 ✗
返回基本类型 / 包装类型 / String / 基本类型集合 ✓
返回业务 DTO / Map<String,Object> / 自定义对象 ✗
```

推荐只生成：`String`、`Long`、`Integer`、`Boolean`、`Double`、`List<String>`、`List<Long>`。

## 命名建议

```text
getCurrentUserId        -> 当前登录人ID
getCurrentLoginOrgId    -> 当前登录部门ID
getCurrentUserName      -> 当前登录人姓名
getCurrentDate          -> 当前日期
```

不要用 `test1`、`demoVar` 这种无法维护的名字。

## 删除与隐藏策略

已发布过的系统变量不要轻易删除方法或改返回类型，因为在途表单/规则/条件可能仍引用旧变量。

推荐策略：
1. 废弃但保留兼容：保留方法，`hidden=true`。
2. 变更展示名：优先调整 `description` 或国际化词条。

## 部署指南

### 推荐模块落点

```text
custom-backend/
├── pom.xml
└── spi-system-variable/
    ├── pom.xml
    ├── src/main/java/com/seeyon/extend/spi/systemvariable/CustomSystemVariableService.java
    └── src/main/resources/
        ├── META-INF/spring.factories
        └── metadata/spi_info.json
```

父 POM 增加：

```xml
<module>spi-system-variable</module>
```

不要把系统变量实现类塞到 `spi-sso`、`spi-mq` 或 `spi-common`。

### spring.factories

SPI 注册格式：

```properties
<confirmed SystemVariableSPIService FQCN>=com.seeyon.extend.spi.systemvariable.CustomSystemVariableService
```

注意：rendered-md 只给出短名 `SystemVariableSPIService`，未给包名。未确认 FQCN 前，不能生成最终可部署的 `spring.factories`。

### spi_info.json

文档只说"重启 UDC 应用对应的服务"，没有给出 `spi_info.json` 示例。

保守模板：

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["ALL"]
}
```

`scopes: ["ALL"]` 是兜底，不是文档 FACT。如果知道 UDC 应用服务标识，应使用具体 scope。

### 部署步骤

1. 构建 `spi-system-variable` 模块。
2. 上传/导入后端 SPI 扩展。
3. 确认 `boot-starter-systemvariable` 在现场 Maven 私服可解析。
4. 重启 UDC 应用对应服务。
5. 打开计算条件弹框组件验证扩展变量出现。

### 验证清单

**静态检查：**
- 父 POM 包含 `<module>spi-system-variable</module>`
- 子模块 POM XML well-formed
- 子模块依赖包含或继承 `boot-starter-systemvariable`
- 存在 `META-INF/spring.factories`
- 存在 `metadata/spi_info.json`
- `spring.factories` key 是已确认的 `SystemVariableSPIService` FQCN
- 实现类实现 `SystemVariableSPIService`
- 每个变量方法 `public`、无参数、有 `@SPISystemVariable`
- 返回值不是复杂 DTO

**运行时验证：**
- 重启后无启动异常
- 计算条件弹框能看到变量
- `description` 展示正确
- `sort` 排序符合预期
- `hidden=true` 的变量不再可选
- 组织模型类型变量返回 ID 后能正确关联实体

### 常见失败点

1. 现场版本低于 `5.6.30`，接口不存在
2. 照抄文档依赖版本导致 Maven 解析失败
3. `SystemVariableSPIService` 包名未确认，`spring.factories` key 错
4. 日期类型枚举值凭空猜测，编译失败
5. 方法带参数，平台无法注册为系统变量
6. 返回复杂对象，计算条件弹框无法使用
7. 返回人员 ID 但没写 `relationEntity`，导致组织模型解析异常
8. 导入后未重启 UDC 应用对应服务

## 原文示例代码

```java
public class DemoSPISystemVariableService implements SystemVariableSPIService {
    @SPISystemVariable(
        type = SPISystemVariableType.ORGANIZATION ,
        description = "SPI登录人id系统变量静态",
        relationEntity = "com.seeyon.organization.domain.core.entity.OrgMember")
    public static Long getCustomLoginUserId(){
        Long userId = Apps.getRequestContext().getUserId();
        return userId;
    }
    @SPISystemVariable(
        type = SPISystemVariableType.ORGANIZATION ,
        description = "SPI登录人id系统变量实例方法",
        relationEntity = "com.seeyon.organization.domain.core.entity.OrgMember")
    public Long getCustomLoginUserIdInstance(){
        ExpressionService expressionService = Apps.getApplicationContext().getBean(ExpressionService.class);
        return (Long)expressionService.getSystemVariableResultByName("currentUserId");
    }
    @SPISystemVariable(
        type = SPISystemVariableType.ORGANIZATION ,
        description = "SPI登录人id系统变量实例方法2",
        relationEntity = "com.seeyon.organization.domain.core.entity.OrgMember")
    public Long getCustomLoginUserIdInstance2(){
        return Apps.getRequestContext().getUserId();
    }
}
```

## 原文未提供但落地必须确认的信息

- `SystemVariableSPIService` 的完整包名
- `@SPISystemVariable` 的完整包名
- `SPISystemVariableType` 的完整包名和完整枚举值
- 日期类型枚举值
- `Apps` 的完整包名
- `ExpressionService` 的完整包名
- `spring.factories` 的准确 key
- `spi_info.json` 的准确 scope
