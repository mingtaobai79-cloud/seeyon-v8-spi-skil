# 组织同步中间表 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 域特有规则

1. **同步阻塞执行**：`pullAll()` 和 `pullIncrement()` 必须同步阻塞执行，不能异步返回。
2. **全量 vs 增量**：
   - 全量拉取（`pullAll`）：必须调用 `markCallbackService.markComplete(linkerCode)` 标记完成
   - 增量拉取（`pullIncrement`）：**切勿调用** `markCallbackService`
3. **linkerCode 必填**：`ConfigInfoApiDto.getLinkerCode()` 是集成应用唯一标识，必须传递。
4. **数据维度**：支持机构/部门、岗位、职务、职级、人员五个维度的同步。
5. **被动接收完整性检测**：被动模式下，必须检测所有维度数据是否均已写入中间表后，才能触发同步。
6. **回调 URL 参数**：被动模式的回调 URL 中 `cipChannel=MIDORGSYNC` 是固定值。

## 禁止项

- 禁止在增量模式下调用 `markCallbackService.markComplete()`。
- 禁止在 SPI 实现中直接操作中间表数据库，必须通过回调服务写入。
- 禁止在被动模式下未检测完整性就触发同步。
- 禁止在 `pullAll()` 中异步执行后直接返回。

## 索取清单

```
P0:
1. MiddleTableOrgSyncSpiPullService 完整反编译源码 ✅ 已有
2. MiddleTableOrgSyncSpiListenerService 完整反编译源码 ✅ 已有
3. ConfigInfoApiDto / ConnectorCallbackRequestDto ✅ 已有

P1:
4. 示例代码 ✅ 已抽取核验
   - `sample_key:orgsync-pull-example`
   - `sample_key:orgsync-listener-example`
   - 已确认 `@MiddleTableChannelRouter`、`spring.factories`、POM、回调服务实际调用方法。
   - sample_key 对应的真实路径必须在具体任务中由用户提供或从目标工程配置发现，不写死到 skill。
5. MiddleTableOrgSyncDataCallbackService / MarkCallbackService / ExecuteCallbackService 完整接口（方法调用已由样例源码 FACT 化；接口源码仍待最终补齐）
6. 中间表数据库表结构（字段、状态值含义；影响数据落表精确说明）
7. cip-connector-api 版本确认（接口来源版本待最终标定；已有 ConfigInfoApiDto / ConnectorCallbackRequestDto 可用）
```

## 业务线边界

- 示例工程中的业务 util 属于实际业务场景，只用于理解样例业务线，不沉淀为通用 SPI 约束。
- 通用文档只保留组织同步中间表 SPI 调用链：主动/被动入口 → 回调服务写入中间表 → mark/execute 回调触发标准同步。
