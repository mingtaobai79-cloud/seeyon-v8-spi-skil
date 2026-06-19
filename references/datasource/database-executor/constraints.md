# 数据源扩展 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 域特有规则

1. 无额外 Nacos 配置，所有连接信息通过 DatabaseInfoApiDto 传入。
2. executeDetail 和 executeDetailForCount 是核心方法，必须实现。
3. getDbTypeEnum 返回值决定平台匹配哪个数据库插件。
4. ExecutorResultApiDto 的 exception 字段用于传递执行异常。

## 禁止项

- 禁止硬编码数据库连接信息（必须从 DatabaseInfoApiDto 获取）。
- 禁止吞掉 SQL 异常（必须包装到 ExecutorResultApiDto.exception）。

## 索取清单

```
P0:
1. ✅ DataBaseExecutorService FQCN → com.seeyon.cip.connector.api.db.DataBaseExecutorService（FACT）
2. ✅ DatabaseInfoApiDto → com.seeyon.cip.connector.dto.db.DatabaseInfoApiDto（FACT）
3. ✅ ExecutorResultApiDto → com.seeyon.cip.connector.dto.db.ExecutorResultApiDto（FACT）
4. ✅ DbTypeEnum → com.seeyon.cip.connector.enums.DbTypeEnum（FACT）

P1:
5. LinkerDetailApiDto 完整字段（较大，含 SQL 结构化配置）
6. OracleSpiDataBaseExecutorService 示例代码
7. 完整接口方法列表（jar 反编译截断了部分方法）
```
