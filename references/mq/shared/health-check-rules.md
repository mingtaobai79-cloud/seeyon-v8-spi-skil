# MQ SPI Health Check / 验证规则

## 文档/知识库校验

当用户处于“第二子域 MQ 资料沉淀”阶段时，只检查 skill reference：

- [ ] `references/mq/index.md` 存在
- [ ] `references/mq/rocketmq-ons/README.md` 存在
- [ ] `references/mq/shared/contract.md` 存在，且记录 `MQMessageSpi` / `MessageDto` FQN、方法签名、字段约束
- [ ] `references/mq/shared/deployment-guide.md` 存在
- [ ] `references/mq/shared/health-check-rules.md` 存在
- [ ] `SKILL.md` 路由决策树能路由到 `references/mq/index.md`
- [ ] `SKILL.md` References 列出 MQ 子域入口

## 生成代码后的静态校验

只有用户明确要求生成/修改工程代码后，才检查：

- [ ] 父 POM 有 `<module>spi-mq</module>`
- [ ] `spi-mq/pom.xml` XML well-formed
- [ ] `boot-starter-mq` 版本为 `5.8.0`，除非现场指定其他版本
- [ ] Java 实现 `implements MQMessageSpi`
- [ ] 四个方法都存在：`send` / `sendBatch` / `subscribeTopic` / `unSubscribeTopic`
- [ ] import 精确 DTO：`com.seeyon.boot.starter.mq.support.dto.MessageDto`
- [ ] 没有依赖 `MQMessageSpi` default 方法形成假实现；四个方法均有明确实现逻辑或能力缺口说明
- [ ] `spring.factories` 注册 `com.seeyon.boot.starter.mq.spi.MQMessageSpi`
- [ ] `spi_info.json` JSON well-formed，`scopes` 为 `["ALL"]`
- [ ] 没有 `@Autowired` / `@Service` / `@Component`
- [ ] 发送使用 `MQSerializer.serialize(messageDto)`
- [ ] 发送前确保 `MessageDto` 必填字段完整：`tenantId` / `topic` / `msgId` / `data`
- [ ] 发送前有 `messageDto.getContext()` / 等价上下文采集策略，或报告说明调用方已设置完整上下文
- [ ] 消费使用 `MQSerializer.deserialize(message.getBody())`
- [ ] 消费后调用 `MessageListenerService.invoke(...)`
- [ ] 说明 topic 是否受 `TopicConverter` 动态分区/环境前缀影响
- [ ] 如果使用灰度消息，说明 `grayTag` 与实例灰度标记匹配策略
- [ ] `MQSerializer.deserialize(...)` 后有 null 保护或明确重试/失败策略
- [ ] 没有只序列化或只消费 `messageDto.getData()`
- [ ] `sendBatch` 聚合失败结果，不是循环发送后无条件 `return true`

## 现场验证

- [ ] MQ 连接配置真实可用
- [ ] Producer 初始化成功
- [ ] Consumer 初始化成功
- [ ] 可发送单条消息
- [ ] 可批量发送或循环发送多条消息
- [ ] 可动态订阅 Topic
- [ ] 可取消订阅 Topic（若目标 MQ client 支持）
- [ ] 消费消息后进入平台 `MessageListenerService`
- [ ] 所有服务已重启

## 常见风险

1. 只重启单服务：MQ 生效范围是全系统，必须重启所有服务。
2. 误把观察到的旧 `boot-starter-mq` 版本当新版本：版本以现场 POM / 目标平台文档为准。
3. 使用 Spring 注解：MQ SPI 实现规则明确不支持 Spring 注解。
4. 手写序列化：应使用平台 `MQSerializer`。
5. 只序列化 `messageDto.getData()`：会丢 `tenantId`、`traceId`、`secretLevel`、`customPassThrough`，并绕过 `MessageListenerService` 的 topic 转换/去重/监听器匹配链路。
6. 默认方法假实现：`MQMessageSpi` 的 default 方法都返回 `true`，生成类不能靠 default 伪装成功。
7. `sendBatch` 假成功：循环发送时吞掉单条失败会导致上游误判。
8. 动态订阅未实现：`subscribeTopic` 必须支持动态订阅。
9. 把 MQ 补进 SSO 工程/文档：MQ 是第二子域，知识进 `references/mq/`，代码进 `spi-mq`。
