> 🧊 **冻结状态** — 缺少必要 jar 包，接口/DTO 均为 OBSERVATION，无法升级到 FACT。
> 待获取对应 jar 后解除冻结。

# 系统变量扩展 / SystemVariableSPIService

> Evidence: OBSERVATION ⚠️ — 语雀文档 + jar 反编译交叉验证。
> **jar 验证结果**：`boot-starter-systemvariable-5.3.313.jar` 和 `boot-starter-formula-5.3.313.jar` 中均未找到 `SystemVariableSPIService`、`@SPISystemVariable`、`SPISystemVariableType`。
> 这些 SPI 接口可能在更高版本或独立 artifact 中。

## 场景

在计算条件弹框组件中添加自定义系统变量。效果是在公式/条件配置时让业务人员能选择扩展变量。

适用版本：5.6.30 及以上版本。

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>boot-starter-systemvariable</artifactId>
  <version>5.3.313</version>
</dependency>
```

## 接口定义 [OBSERVATION ⚠️]

```java
// FQCN 待 jar 确认，短名：
public interface SystemVariableSPIService {
    // 标记接口，无抽象方法
    // 实现类中定义 public 方法 + @SPISystemVariable 注解即可注册为系统变量
}
```

## jar 反编译确认的类 [FACT ✅]

### SystemVariableKeyEnum（boot-starter-systemvariable-5.3.313）

```java
package com.seeyon.boot.starter.systemvariable.enums;

public enum SystemVariableKeyEnum {
    CURRENT_MULTI_ORG("system.currentMultiOrg", "当前人员所在的多维组织"),
    CURRENT_MULTI_ORG_DEPARTMENT("system.currentMultiOrgDepartment", "当前人员所在的多维组织部门"),
    CURRENT_MULTI_ORG_DEPARTMENT_PARENT("system.currentMultiOrgDepartmentParent", "多维组织部门的上级部门"),
    CURRENT_MULTI_ORG_DEPARTMENT_FIRST("system.currentMultiOrgDepartmentFirst", "多维组织部门的一级部门"),
    CURRENT_MULTI_ORG_RESPONSIBLE("system.currentMultiOrgDepartmentResponsible", "负责的多维组织"),
    CURRENT_MULTI_ORG_DIVIDE("system.currentMultiOrgDepartmentDivide", "分管的多维组织"),
    CURRENT_MULTI_ORG_RESPONSIBLE_DEPARTMENT("system.currentMultiOrgDepartmentResponsibleDepartment", "负责的多维组织部门"),
    CURRENT_MULTI_ORG_DIVIDE_DEPARTMENT("system.currentMultiOrgDepartmentDivideDepartment", "分管的多维组织部门"),
    CURRENT_ALL_PARENT_ORG("system.currentAllParentOrg", "人员主岗对应上级机构");

    // 每个枚举提供 getIdKey() / getCodeKey() / getNameKey()
}
```

### ExpressionService（boot-starter-formula-5.3.313）

```java
package com.seeyon.boot.starter.formula.domain.service;

// FQCN: com.seeyon.boot.starter.formula.domain.service.ExpressionService
// 公式引擎核心服务，非 SPI 接口
```

### SystemVariableItems（boot-starter-formula-5.3.313）

```java
package com.seeyon.boot.starter.formula.dto.preset;

@DtoInfo("变量项")
public class SystemVariableItems implements Serializable {
    String type;            // 操作符类型
    String name;            // 参数变量名
    String description;     // 显示名称
    String functionName;    // 对应函数名
    String resultType;      // 数据类型
    String relationEntity;  // 系统变量关联实体
    boolean hidden;         // 是否隐藏
}
```

## 代码骨架

```java
package com.seeyon.extend.spi.systemvariable;

// import com.seeyon.boot.starter.formula.spi.SystemVariableSPIService;  // FQCN 待确认
// import com.seeyon.boot.starter.formula.annotation.SPISystemVariable;   // FQCN 待确认
// import com.seeyon.boot.starter.formula.enums.SPISystemVariableType;   // FQCN 待确认

/**
 * 系统变量 SPI 实现
 * <p>🧊 冻结：接口 FQCN 未确认，代码无法编译</p>
 */
public class CustomSystemVariableService /* implements SystemVariableSPIService */ {

    // @SPISystemVariable(name = "customVar", description = "自定义变量", type = SPISystemVariableType.STRING)
    public String getCustomVariable() {
        // TODO: 返回自定义系统变量值
        return "custom-value";
    }
}
```

## Nacos 配置

本 SPI 不需要额外 Nacos 配置。

## spring.factories

```properties
# FQCN 待 jar 确认
# com.seeyon.boot.starter.formula.spi.SystemVariableSPIService=com.seeyon.extend.spi.systemvariable.CustomSystemVariableService
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["formula"]
}
```

## 重启服务

formula

## 阻塞项

1. `SystemVariableSPIService` 接口 FQCN — 5.3.313 jar 中不存在
2. `@SPISystemVariable` 注解 FQCN — 5.3.313 jar 中不存在
3. `SPISystemVariableType` 枚举 FQCN + 全部枚举值 — 5.3.313 jar 中不存在
4. 需要更高版本 jar 或独立 SPI artifact
