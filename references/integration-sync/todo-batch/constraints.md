# 批处理三方待办 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 域特有规则

1. **异常隔离**：每个事项的处理必须独立，单个事项失败不能影响其他事项处理。
2. **操作类型**：根据 `AffairBatchDto.getOperation()` 判断操作类型（如：同意、拒绝、转办等）。
3. **来源应用**：根据 `AffairBatchSubDto.getAppName()` 判断事项来源（如：`app_approval` 审批应用）。
4. **表单数据**：`formData` 只传节点权限 ID，其他表单数据由 UDC 查询过滤。
5. **意见信息**：`OpinionDto.content` 为用户填写的处理意见，可能为空。

## 禁止项

- 禁止在批处理循环中抛出未捕获异常导致整个批次中断。
- 禁止直接修改入参 `AffairBatchDto` 对象。
- 禁止在 SPI 实现中直接操作数据库，应通过三方 API 调用。

## 索取清单

```
P0:
1. AbstractThirdAffairService 完整反编译源码 ✅ 已有
2. AffairBatchDto / AffairBatchSubDto / OpinionDto / AffairBatchResponseDto ✅ 已有
3. spring.factories 注册示例 ✅ 已有

P1:
4. 示例实现类（如有；业务线 util 属实际项目代码，不作为通用 SPI 知识库输入）
5. Nacos 配置 key 和示例值（业务现场参数，不作为接口 FACT 化阻塞）
6. ctp-affair-facade 版本确认 ✅ 已确认：5.3.315
   - Locator: `repo_key:<project-repo>!/com/seeyon/ctp-affair-facade/5.3.315/ctp-affair-facade-5.3.315.jar`
   - 已核验类：AbstractThirdAffairService / AffairBatchDto / AffairBatchSubDto / OpinionDto / AffairBatchResponseDto
   - `<project-repo>` 必须在具体任务中由用户提供或从目标工程配置发现，不写死现场路径
```
