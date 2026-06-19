# 系统变量 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 域特有规则

1. 🧊 **冻结**：接口 FQCN 未确认，代码无法编译。
2. SystemVariableSPIService 是标记接口，无抽象方法。
3. 通过 @SPISystemVariable 注解标记方法为系统变量。
4. SPISystemVariableType 枚举决定变量数据类型。

## 禁止项

- 禁止在 SPI 方法中做数据库查询（公式引擎高频调用）。
- 禁止返回 null（应返回默认值）。

## 索取清单

```
P0（阻塞）:
1. ❌ SystemVariableSPIService 完整包名 — 5.3.313 不存在
2. ❌ @SPISystemVariable 完整包名 — 5.3.313 不存在
3. ❌ SPISystemVariableType 完整包名 + 全部枚举值 — 5.3.313 不存在

P1:
4. ✅ SystemVariableKeyEnum → com.seeyon.boot.starter.systemvariable.enums.SystemVariableKeyEnum（FACT）
5. ✅ SystemVariableItems → com.seeyon.boot.starter.formula.dto.preset.SystemVariableItems（FACT）
6. ✅ ExpressionService → com.seeyon.boot.starter.formula.domain.service.ExpressionService（FACT）
7. 需要更高版本 jar 或独立 SPI artifact
```
