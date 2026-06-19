# RocketMQ / ONS SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`
> 共享契约：`../shared/contract.md`

## 平台接入方式（必须保留）

1. 序列化方式尽量使用 `com.seeyon.boot.starter.mq.serializer.MQSerializer`。
2. 通过 `Apps.getBeanFactory().getBean(XXX.class)` 获取 bean。
3. 通过 `Apps.getEnvironment().getProperty("seeyon.xx.xx")` 获取 Nacos 配置。
4. 不支持任何 Spring 注解。
5. Topic 需要支持动态订阅和取消订阅；动态订阅必须支持，动态取消可不支持。
6. 收到消息后调用 `Apps.getBeanFactory().getBean(MessageListenerService.class).invoke(xxx)`。

## 禁止项

- 禁止绕过 `MQSerializer` 手工序列化消息。
- 禁止消费后不调用 `MessageListenerService.invoke(...)`。
- 禁止使用 `@Autowired`、`@Service`、`@Component` 等 Spring 注解。
- 禁止只序列化 `messageDto.getData()`；必须保留完整 `MessageDto`。

## 部署

- 生效范围：全系统
- 重启：所有服务
- 旧 SPI 走 `seeyon.spi.spi-plugins`，Super SPI 走客开管理式打包

## 索取清单

```
P0:
1. ✅ MQMessageSpi 完整反编译源码 → shared/contract.md §1 (FACT)
2. ✅ MessageDto 字段、序列化约定 → shared/contract.md §2-3 (FACT)
3. ✅ spring.factories 注册示例 → key=com.seeyon.boot.starter.mq.spi.MQMessageSpi (FACT)

P1:
4. ✅ 消费监听相关接口 → shared/contract.md §4 MessageListenerService (FACT)
5. ⚠️ 阿里云 RocketMQ / ONS 实现观察 → README.md 已归一化记录；不保留独立案例文件
6. ✅ 部署/重启口径按现有文档执行：MQ 生效范围全系统，重启所有服务；旧 SPI 走 `seeyon.spi.spi-plugins`，Super SPI 走客开管理式打包
7. ✅ boot-starter-mq / POM 片段当前不再作为阻塞索取项：按 `README.md`、`shared/contract.md`、`shared/deployment-guide.md` 既有文档生成；版本差异仅在现场最终构建时复核
```

## 域特有规则

1. 四个方法都应显式 override，不依赖 interface default `true`。
2. `sendBatch` 如果循环调用 `send`，不能吞掉失败。
3. 序列化必须使用 `MQSerializer`，不能手写 JSON。
4. 消费后必须调用 `MessageListenerService.invoke(messageDto)`。
5. Topic 动态订阅必须支持，动态取消可不支持但需在交付报告标注。
