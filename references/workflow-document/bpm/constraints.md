# BPM 流程扩展 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 域特有规则

1. 两个 SPI 必须配合实现，才能完整覆盖场景。
2. mergeNodePermission 合并权限后，checkNodePermission 负责校验。
3. forwardAffair 返回重定向事项 ID，平台据此打开对应事项。
4. BpmCheckNodePermissionResp 有三个校验维度：操作合法、意见必填、意见长度。

## 禁止项

- 禁止只实现一个 SPI（场景画不圆）。
- 禁止 forwardAffair 返回 null（应返回 BpmForwardResp 对象）。

## 索取清单

```
P0:
1. ✅ BpmDetailViewSpi FQCN → com.seeyon.bpm.spi.BpmDetailViewSpi（FACT）
2. ✅ BpmOperationSpi FQCN → com.seeyon.bpm.spi.BpmOperationSpi（FACT）
3. ✅ BpmForwardReq/Resp → com.seeyon.bpm.spi.dto.detail.*（FACT）
4. ✅ BpmNodePermissionMergeReq/Resp → com.seeyon.bpm.spi.dto.detail.*（FACT）
5. ✅ BpmCheckNodePermissionReq/Resp → com.seeyon.bpm.spi.dto.operation.*（FACT）

P1:
6. BpmNodePermissionOperationSimpleDto 完整字段
7. BpmCommentDto 完整字段
8. 示例实现类
```
