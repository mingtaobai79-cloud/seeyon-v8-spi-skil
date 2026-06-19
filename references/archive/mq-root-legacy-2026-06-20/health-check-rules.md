# MQ SPI Health Check / 验证规则

## 文档/知识库校验

当用户处于“第二子域 MQ 资料沉淀”阶段时，只检查 skill reference：

- [ ] `references/mq/index.md` 存在
- [ ] `references/mq/rocketmq-ons.md` 存在
- [ ] `references/mq/deployment-guide.md` 存在
- [ ] `references/mq/health-check-rules.md` 存在
- [ ] `SKILL.md` 路由决策树能路由到 `references/mq/index.md`
- [ ] `SKILL.md` References 列出 MQ 子域入口

## 生成代码后的静态校验

只有用户明确要求生成/修改工程代码后，才检查：

- [ ] 父 POM 有 `<module>spi-mq</module>`
- [ ] `spi-mq/pom.xml` XML well-formed
- [ ] `boot-starter-mq` 版本为 `5.8.0`，除非现场指定其他版本
- [ ] Java 实现 `implements MQMessageSpi`
- [ ] 四个方法都存在：`send` / `sendBatch` / `subscribeTopic` / `unSubscribeTopic`
- [ ] `spring.factories` 注册 `com.seeyon.boot.starter.mq.spi.MQMessageSpi`
- [ ] `spi_info.json` JSON well-formed，`scopes` 为 `["ALL"]`
- [ ] 没有 `@Autowired` / `@Service` / `@Component`
- [ ] 发送使用 `MQSerializer.serialize(messageDto)`
- [ ] 消费使用 `MQSerializer.deserialize(message.getBody())`
- [ ] 消费后调用 `MessageListenerService.invoke(...)`

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
2. 误把 `boot-starter-mq:5.0.0-DEV-SNAPSHOT` 当新版本：样例旧，用户文档新版本是 `5.8.0`。
3. 使用 Spring 注解：样例明确“不支持任何 spring 注解”。
4. 手写序列化：应使用平台 `MQSerializer`。
5. 动态订阅未实现：`subscribeTopic` 必须支持动态订阅。
6. 把 MQ 补进 SSO 工程/文档：MQ 是第二子域，知识进 `references/mq/`，代码进 `spi-mq`。
