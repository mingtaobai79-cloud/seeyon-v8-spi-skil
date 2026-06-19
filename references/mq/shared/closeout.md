# MQ 子域收敛记录 / Closeout

> 状态：定格 / FROZEN
> Evidence：核心接口、DTO、序列化、消费链路、topic 转换、配置、SPI 加载、灰度、去重均来自用户提供反编译代码；ONS 实现规则只保留归一化观察。

## 范围

MQ 子域用于 V8 “其他类型 MQ 中间件扩展”，推荐生成到 `spi-mq` 模块。

已覆盖：

- `MQMessageSpi`
- `MessageDto`
- `MQSerializer`
- `MessageListenerService`
- `MessageListener` 注解
- `MessageListenerImpl`
- `TopicConverter`
- `DynamicMessageDto`
- `MQProperties`
- `AbstractMessageListener`
- `MethodWrapper`
- `MQMessageCompUtils`
- `NacosInstancesListener`
- `MqConstant`
- Aliyun RocketMQ / ONS 实现观察（已归一化，不保留独立案例文件）
- SPI 开发准备公共文档

## 核心文档

- `references/spi-domain-constraints.md` — 所有 SPI 开发/生成/改造公共前置入口
- `references/mq/index.md` — MQ 子域入口
- `references/mq/shared/contract.md` — MQ 平台契约，FACT 主文档
- `references/mq/rocketmq-ons/README.md` — 生成/实现策略
- `references/mq/shared/deployment-guide.md` — 工程落点、注册、配置、部署
- `references/mq/shared/health-check-rules.md` — 静态与现场校验
- `references/mq/shared/generated-project-validation.md` — 示例工程生成验证规则

## 收敛结论

1. MQ SPI 实现必须实现 `MQMessageSpi` 四个方法，不能依赖 default `true`。
2. 消息必须序列化完整 `MessageDto`，不能只传 `data`。
3. 消费必须进入 `MessageListenerService.invoke(messageDto)`，不能绕过平台链路。
4. `MQSerializer.deserialize` 可能返回 `null`，生成代码必须处理。
5. topic 可能受环境前缀、动态分区、`UDC_`/`DYNAMIC_` 规则影响。
6. listener 匹配依赖 `class#method#firstParameterType` 和 `data` 实际类型。
7. 灰度消息依赖 Nacos metadata `seeyon.gray.tag`。
8. 去重依赖 `msgId`、Redis、rebalance / antiDuplicate 配置。
9. 平台原生配置前缀是 `seeyon.mq.*`；示例 `seeyon.ones.*` 是 ONS SPI 自定义配置。
10. SPI 公共工程规则统一索引到 `references/spi-domain-constraints.md`。

## 冻结原则

MQ 子域当前停止继续扩资料。后续只有以下情况才解冻：

- 用户提供新版本现场反编译代码，与当前 Contract 冲突；
- 真实生成工程验证失败，需修正 health check / deployment / implementation rules；
- 新增非 RocketMQ/ONS 的 MQ client，需要新增独立实现策略文档。

否则不再追加零散资料，避免过度膨胀。

## 下一阶段输入

转入系统变量子域完善。优先需要：

- `SystemVariableSPIService` 反编译代码
- `@SPISystemVariable` 反编译代码
- `SPISystemVariableType` / 相关枚举
- 示例实现类
- 注册文件 / POM / 部署说明
