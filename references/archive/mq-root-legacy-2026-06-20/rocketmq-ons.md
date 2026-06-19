# 阿里云 RocketMQ / ONS MQMessageSpi 样例抽象

> 来源：用户当次提供的 `ali-rocketmq.zip` 样例包中的 `AliOnesMqService.java`、`pom.xml`、`META-INF/spring.factories`；不要把本机绝对路径作为通用输入。

## 样例工程事实 [OBSERVATION ⚠️]

样例工程：

```text
ali-rocketmq/
├── pom.xml
├── src/main/java/com/seeyon/ali/rocketmq/AliOnesMqService.java
└── src/main/resources/META-INF/spring.factories
```

样例实现类：

```java
com.seeyon.ali.rocketmq.AliOnesMqService implements MQMessageSpi
```

样例注册：

```properties
com.seeyon.boot.starter.mq.spi.MQMessageSpi=com.seeyon.ali.rocketmq.AliOnesMqService
```

样例三方依赖：

```xml
<dependency>
    <groupId>com.aliyun.openservices</groupId>
    <artifactId>ons-client</artifactId>
    <version>1.8.8.5.Final</version>
</dependency>
```

样例里的平台 MQ 依赖版本是旧值：

```xml
<com.seeyon:boot-starter-mq:5.0.0-DEV-SNAPSHOT>
```

生成新资料/新工程时，以用户提供的官方文档版本 `5.8.0` 为准，除非现场另有指定。

## 必保留的平台接入方式 [OBSERVATION ⚠️]

样例注释明确：

1. 注意序列化方式，尽量使用 `com.seeyon.boot.starter.mq.serializer.MQSerializer`。
2. 通过 `Apps.getBeanFactory().getBean(XXX.class)` 获取 bean。
3. 通过 `Apps.getEnvironment().getProperty("seeyon.xx.xx")` 获取 Nacos 配置。
4. 不支持任何 Spring 注解。
5. Topic 需要支持动态订阅和取消订阅；动态订阅必须支持，动态取消可不支持。
6. 收到消息后调用 `Apps.getBeanFactory().getBean(MessageListenerService.class).invoke(xxx)`。

## 发送逻辑

样例发送流程：

1. new `com.aliyun.openservices.ons.api.Message()`。
2. `message.setTopic(messageDto.getTopic())`。
3. `message.setBody(MQSerializer.serialize(messageDto))`。
4. `message.setMsgID(messageDto.getMsgId())`。
5. `message.setKey(messageDto.getMsgId())`。
6. `getProducer().send(message)`。
7. `SendResult.getMessageId() != null` 表示成功。

生成代码时注意：

- 不要手写 JSON 序列化 `MessageDto`。
- 不要只序列化 `messageDto.getData()`；样例强调 `messageDto` 和 `messageDto.data` 到接收方都要可反序列化且类型匹配。

## 批量发送逻辑

样例中 `sendBatch` 是循环调用单条 `send`：

```java
for (MessageDto dto : messageDtoList) {
    send(dto);
}
return true;
```

如果目标 MQ client 支持真正批量发送，可以替换成原生批量 API；否则保守循环发送。

## 消费与订阅逻辑

样例 listener：

```java
MessageDto messageDto = MQSerializer.deserialize(message.getBody());
getListenerService().invoke(messageDto);
return Action.CommitMessage;
```

样例订阅：

```java
getConsumer().subscribe(topic, SubscriptionData.SUB_ALL, listener);
```

样例取消订阅：

```java
getConsumer().unsubscribe(topic);
```

## Producer / Consumer 初始化

样例用 lazy init：

- `ONSFactory.createProducer(properties)` 后调用 `producer.start()`。
- `ONSFactory.createConsumer(properties)` 后调用 `consumer.start()`。
- Consumer 设置集群模式：`PropertyValueConst.CLUSTERING`，避免多节点重复消费。

样例 GroupId：

```java
SystemEnvironment.getEnv().toUpperCase() + "_Producer_" + Apps.getAppName()
SystemEnvironment.getEnv().toUpperCase() + "_Consumer_" + Apps.getAppName()
```

## 样例配置键 [OBSERVATION ⚠️]

样例使用：

```text
seeyon.ones.accessKey
seeyon.ones.secretKey
seeyon.ones.send-time-out
seeyon.ones.server
```

这些 key 带 `ones` 业务名。沉淀为通用 MQ 子域时，应记录“样例如此”，但生成新工程时需按现场命名策略确认；不要擅自把 `ones` 当平台标准。

## 生成新工程时的建议命名 [HYPOTHESIS ❓]

如果用户没有要求沿用样例配置名，可用更通用的：

```yaml
seeyon:
  mq:
    aliyun:
      accessKey: "${ALIYUN_ROCKETMQ_ACCESS_KEY}"
      secretKey: "${ALIYUN_ROCKETMQ_SECRET_KEY}"
      nameSrvAddr: "xxx.aliyuncs.com:9876"
      sendTimeoutMillis: "3000"
```

但这属于生成策略，不是官方 Contract。输出时应标为建议，或向用户确认是否沿用 `seeyon.ones.*`。

## 禁止项

- 禁止使用 `@Autowired`、`@Service`、`@Component` 等 Spring 注解。
- 禁止绕过 `MQSerializer` 手工序列化消息。
- 禁止消费后不调用 `MessageListenerService.invoke(...)`。
- 禁止把样例里的 `.idea/`、`target/`、`.flattened-pom.xml` 当模板复制。
