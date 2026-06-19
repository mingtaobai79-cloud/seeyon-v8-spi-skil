# 阿里云 RocketMQ / ONS MQMessageSpi 实现规则

> **核心 SPI 接口 Evidence: FACT ✅** — `MQMessageSpi`、`MessageDto`、`MQSerializer`、`MessageListenerService` 来自反编译，见 `../shared/contract.md`。
> **实现观察 Evidence: OBSERVATION ⚠️** — ONS 实现规则来自本地源码观察，非 jar 反编译；只能作为实现策略参考。

## 归一化实现观察 [OBSERVATION ⚠️]

来源工程结构仅作观察，不进入模板：

```text
ali-rocketmq/
├── pom.xml
├── .flattened-pom.xml
├── src/main/java/com/seeyon/ali/rocketmq/AliOnesMqService.java
└── src/main/resources/META-INF/spring.factories
```

观察到的实现类形态：

```java
com.seeyon.ali.rocketmq.AliOnesMqService implements MQMessageSpi
```

注册 key [FACT ✅]：

```properties
com.seeyon.boot.starter.mq.spi.MQMessageSpi=com.seeyon.ali.rocketmq.AliOnesMqService
```

> key `com.seeyon.boot.starter.mq.spi.MQMessageSpi` 与 `shared/contract.md` §1 接口 FQN 一致，已交叉验证。

三方依赖观察：

```xml
<dependency>
    <groupId>com.aliyun.openservices</groupId>
    <artifactId>ons-client</artifactId>
    <version>1.8.8.5.Final</version>
</dependency>
```

观察到的平台 MQ 依赖版本存在差异：源码 `pom.xml` 为 `5.0.0-DEV-SNAPSHOT`，`.flattened-pom.xml` 展开后为 `5.0.0-TEST-SNAPSHOT`。

生成新资料/新工程时，以现场 POM / 目标版本文档为准；当前 MQ 扩展文档记录版本为 `5.8.0`，但不能覆盖现场版本。

## 必保留的平台接入方式 [OBSERVATION ⚠️ — FQCN 已交叉验证 FACT ✅]

实现观察明确：

1. 注意序列化方式，尽量使用 `com.seeyon.boot.starter.mq.serializer.MQSerializer`。
2. 通过 `Apps.getBeanFactory().getBean(XXX.class)` 获取 bean。
3. 通过 `Apps.getEnvironment().getProperty("seeyon.xx.xx")` 获取 Nacos 配置。
4. 不支持任何 Spring 注解。
5. Topic 需要支持动态订阅和取消订阅；动态订阅必须支持，动态取消可不支持。
6. 收到消息后调用 `Apps.getBeanFactory().getBean(MessageListenerService.class).invoke(xxx)`。

## 发送逻辑

发送流程：

1. new `com.aliyun.openservices.ons.api.Message()`。
2. 必要时先执行 `messageDto.getContext()`，从 `RequestContext` 采集 `tenantId`、`traceId`、`secretLevel`、`customPassThrough`。
3. 必要时执行 `messageDto.check()`，校验 `tenantId`、`topic`、`msgId`、`data` 等 JSR-303 约束。
4. `message.setTopic(messageDto.getTopic())`。
5. `message.setBody(MQSerializer.serialize(messageDto))`。
6. `message.setMsgID(messageDto.getMsgId())`。
7. `message.setKey(messageDto.getMsgId())`。
8. `getProducer().send(message)`。
9. `SendResult.getMessageId() != null` 表示成功。

生成代码时注意：

- 不要手写 JSON 序列化 `MessageDto`。
- 不要只序列化 `messageDto.getData()`；样例强调 `messageDto` 和 `messageDto.data` 到接收方都要可反序列化且类型匹配。
- `MessageDto` 包含租户、trace、密级和透传上下文；只发送 `data` 会破坏平台消费链。

## 批量发送逻辑

若 `sendBatch` 循环调用单条 `send`：

```java
for (MessageDto dto : messageDtoList) {
    send(dto);
}
return true;
```

如果目标 MQ client 支持真正批量发送，可以替换成原生批量 API；否则保守循环发送。

生成代码时不要无脑 `return true`。循环发送时至少应聚合失败结果：任一 `send(dto)` 返回 `false` 时整体返回 `false`，或记录失败明细并按现场策略处理。

## 消费与订阅逻辑

消费 listener：

```java
MessageDto messageDto = MQSerializer.deserialize(message.getBody());
if (messageDto == null) {
    // deserialize 可能 Jackson/JSON fallback 均失败；生成代码应记录日志并按目标 MQ 重试/失败策略返回
    return Action.ReconsumeLater;
}
getListenerService().invoke(messageDto);
return Action.CommitMessage;
```

消费侧要点：

- 反序列化对象必须是完整 `MessageDto`。
- 不要只把 `messageDto.getData()` 交给业务代码。
- 平台 listener 链路通过 `MessageListenerService.invoke(messageDto)` 处理上下文恢复、topic 转换、动态分区、灰度判断、去重、监听器匹配、MDC/RequestContext 清理；若自行绕过，必须证明等价。
- `MQSerializer.deserialize(byte[])` 可能返回 `null`，消费回调要显式处理，避免 `invoke(null)`。

订阅：

```java
getConsumer().subscribe(topic, SubscriptionData.SUB_ALL, listener);
```

取消订阅：

```java
getConsumer().unsubscribe(topic);
```

## Producer / Consumer 初始化

可采用 lazy init：

- `ONSFactory.createProducer(properties)` 后调用 `producer.start()`。
- `ONSFactory.createConsumer(properties)` 后调用 `consumer.start()`。
- Consumer 设置集群模式：`PropertyValueConst.CLUSTERING`，避免多节点重复消费。

GroupId 生成方式观察：

```java
SystemEnvironment.getEnv().toUpperCase() + "_Producer_" + Apps.getAppName()
SystemEnvironment.getEnv().toUpperCase() + "_Consumer_" + Apps.getAppName()
```

## 配置键边界 [OBSERVATION ⚠️ — 非平台标准]

观察到的自定义配置键：

```text
seeyon.ones.accessKey
seeyon.ones.secretKey
seeyon.ones.send-time-out
seeyon.ones.server
```

这些 key 带 `ones` 业务名，只能作为非标准观察；生成新工程时必须按现场命名策略确认，不得把 `ones` 当平台标准。

## 生成新工程时的配置命名 [HYPOTHESIS ❓]

如果用户没有要求沿用现场既有配置名，可使用参数化命名：

```yaml
seeyon:
  mq:
    aliyun:
      accessKey: "${ALIYUN_ROCKETMQ_ACCESS_KEY}"
      secretKey: "${ALIYUN_ROCKETMQ_SECRET_KEY}"
      nameSrvAddr: "{aliyun_rocketmq_name_srv_addr}"
      sendTimeoutMillis: "3000"
```

但这属于生成策略，不是官方 Contract。输出时应标为建议，或向用户确认是否沿用 `seeyon.ones.*`。

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["ALL"]
}
```

## 方法说明

| 方法 | 参数 | 返回 | 语义 |
|------|------|------|------|
| send | `MessageDto` | `boolean` | 发送单条消息 |
| sendBatch | `List<MessageDto>` | `boolean` | 批量发送（可循环调用 send） |
| subscribeTopic | `String topic` | `boolean` | 动态订阅 topic（必须支持） |
| unSubscribeTopic | `String topic` | `boolean` | 动态取消订阅（可不支持但需标注） |

## 重启服务

全部服务（MQ 生效范围是全系统）

## Scope

`scopes: ["ALL"]` — MQ 扩展全系统生效。

## 禁止项

- 禁止使用 `@Autowired`、`@Service`、`@Component` 等 Spring 注解。
- 禁止绕过 `MQSerializer` 手工序列化消息。
- 禁止消费后不调用 `MessageListenerService.invoke(...)`。
- 禁止把样例里的 `.idea/`、`target/`、`.flattened-pom.xml` 当模板复制。
