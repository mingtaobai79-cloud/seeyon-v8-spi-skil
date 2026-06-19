# 公文扩展 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 域特有规则

1. 🧊 **冻结**：接口定义不完整，代码无法编写。
2. 该接口只能通过泛化调用方式扩展，不是传统 SPI 注册。
3. 包名中包含数字 ID `335172694483814428`，是公文应用的唯一标识。
4. 涉及大量 DTO 和 Service，需 16KB 附件确认完整定义。

## 禁止项

- 禁止使用传统 SPI 注册方式（spring.factories）。
- 禁止硬编码数字 ID（应从配置或元数据获取）。

## 索取清单

```
P0（阻塞）:
1. ❌ 公文应用 artifact — 仓库中未找到
2. ❌ EdocProjectPublicService 完整接口定义 — 需 16KB 附件
3. ❌ 大量 DTO 和 Service 完整字段 — 需 16KB 附件
4. ❌ 泛化调用方式的具体示例代码 — 需文档补充

P1:
5. 数字 ID `335172694483814428` 是否环境相关
6. AppServiceReliableInvoker 使用示例
7. 公文应用版本号确认
```
