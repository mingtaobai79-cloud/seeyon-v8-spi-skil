# System Variable Jar Analysis (2026-06-17)

> 状态：域已冻结，等待确认 SPI 接口所在 jar。

## 已检查的 jar

### boot-starter-systemvariable-5.3.313.jar（34 entries，仅 4 个类）

```
com.seeyon.boot.starter.systemvariable.engine.functions.env.EnvFunction
com.seeyon.boot.starter.systemvariable.enums.SystemVariableKeyEnum
com.seeyon.boot.starter.systemvariable.service.SystemVariableService
com.seeyon.boot.starter.systemvariable.util.SystemVariableUtils
```

**不含** SystemVariableSPIService / @SPISystemVariable / SPISystemVariableType。

metadata/starter_info.json:
```json
{"name":"boot-starter-systemvariable","basePackage":"com.seeyon.boot.starter.systemvariable","type":"1"}
```

### boot-starter-formula-5.3.313.jar（326 entries）

含 ExpressionService 但**不含** SPI 接口。SPI/Variable 相关类：
```
ExprSystemConstant
VariableCheckFilter
SystemPresetVariableDto / SystemVariableItems
SystemVariable (parser/ast)
SystemVariableExpressionScriptBuilder
VariableValidator
```

## 已确认的 FQCN（FACT ✅）

| 短名 | FQCN | 来源 |
|------|------|------|
| Apps | `com.seeyon.boot.context.Apps` | boot-core（用户贴的反编译） |
| ExpressionService | `com.seeyon.boot.starter.formula.domain.service.ExpressionService` | boot-starter-formula-5.3.313.jar |
| RequestContext | `com.seeyon.boot.context.RequestContext` | Apps 源码中引用 |

## 未确认的 FQCN（仍阻塞）

| 短名 | 状态 |
|------|------|
| SystemVariableSPIService | ❌ 不在上述两个 jar 中 |
| @SPISystemVariable | ❌ 不在上述两个 jar 中 |
| SPISystemVariableType | ❌ 不在上述两个 jar 中 |

## 下一步

在 IntelliJ 中 Ctrl+N 搜索 `SystemVariableSPIService`，确认它属于哪个 artifact/jar。
可能在 `boot-starter-spi-api`、`boot-starter-spi-systemvariable` 或类似 SPI 注解包中。

## organization.json 内置变量摘要

boot-starter-systemvariable jar 中 `META-INF/system/organization.json` 定义了 80+ 个内置系统变量。
关键模式：
- type: "SYSTEM"
- name: "system.{variableName}"
- functionName: 对应 @Function 注册名
- resultType: "BIGINTEGER" / "STRING" / "ARRAY" / "INTEGER"
- relationEntity: 组织模型实体 fullName（仅组织模型类型有）

示例：
```json
{"name":"system.currentUserId","functionName":"currentUserId","resultType":"BIGINTEGER",
 "relationEntity":"com.seeyon.organization.domain.core.entity.OrgMember"}
```

SystemVariableKeyEnum 枚举值（多维组织相关）：
```
CURRENT_MULTI_ORG, CURRENT_MULTI_ORG_DEPARTMENT, CURRENT_MULTI_ORG_DEPARTMENT_PARENT,
CURRENT_MULTI_ORG_DEPARTMENT_FIRST, CURRENT_MULTI_ORG_RESPONSIBLE, CURRENT_MULTI_ORG_DIVIDE,
CURRENT_MULTI_ORG_RESPONSIBLE_DEPARTMENT, CURRENT_MULTI_ORG_DIVIDE_DEPARTMENT,
CURRENT_ALL_PARENT_ORG
```
