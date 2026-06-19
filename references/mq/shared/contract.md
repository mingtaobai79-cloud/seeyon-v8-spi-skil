# MQMessageSpi Contract / MessageDto 契约

> 来源：用户提供的 IntelliJ IDEA / Fernflower 反编译代码：
> - `com.seeyon.boot.starter.mq.spi.MQMessageSpi`
> - `com.seeyon.boot.starter.mq.support.dto.MessageDto`
>
> Evidence：FACT ✅（来自目标类反编译代码）。
> 注意：版本不同，Contract 仍需以现场实际反编译代码为准；本文记录当前已知 MQ 子域核心契约，生成工程时优先使用这里的 FQN / method signature / DTO 字段。

## 1. 核心 SPI 接口 [FACT ✅]

```java
package com.seeyon.boot.starter.mq.spi;

import com.seeyon.boot.starter.mq.support.dto.MessageDto;
import java.util.List;

public interface MQMessageSpi {
    default boolean send(MessageDto messageDto) {
        return true;
    }

    default boolean sendBatch(List<MessageDto> messageDtoList) {
        return true;
    }

    default boolean subscribeTopic(String topic) {
        return true;
    }

    default boolean unSubscribeTopic(String topic) {
        return true;
    }
}
```

### 方法契约

| 方法 | 参数 | 返回 | 语义 |
|---|---|---|---|
| `send` | `MessageDto messageDto` | `boolean` | 发送单条消息 |
| `sendBatch` | `List<MessageDto> messageDtoList` | `boolean` | 批量发送；目标 MQ client 不支持原生 batch 时可循环调用 `send` |
| `subscribeTopic` | `String topic` | `boolean` | 动态订阅 topic |
| `unSubscribeTopic` | `String topic` | `boolean` | 动态取消订阅 topic；若目标 MQ client 不支持，必须在交付报告标注能力缺口 |

### 生成约束

1. 实现类必须 `implements MQMessageSpi`。
2. 必须 import 精确 FQN：`com.seeyon.boot.starter.mq.support.dto.MessageDto`。
3. 四个方法都应显式 override，不依赖 interface default `true`，否则容易形成“看似支持、实际无效”的假实现。
4. `sendBatch` 如果循环调用 `send`，不能吞掉失败：任一发送失败应返回 `false` 或记录失败并按现场策略处理。

## 2. MessageDto DTO 契约 [FACT ✅]

FQN：

```java
com.seeyon.boot.starter.mq.support.dto.MessageDto
```

注解：

```java
@DtoInfo("mq组件消息包装类")
public class MessageDto implements Serializable
```

字段：

| 字段 | 类型 | 约束/说明 |
|---|---|---|
| `fromApp` | `String` | 消息来源应用 |
| `transferRequestContext` | `TransferRequestContext` | 上下文透传对象 |
| `traceId` | `String` | traceId；为空时可由 `Ids.gidString()` 生成 |
| `secretLevel` | `Integer` | 密级；接收时为空会记录错误日志 |
| `tenantId` | `Long` | `@NotNull`；发送前 `RequestContext.tenantId` 为空会抛 `BootException` |
| `grayTag` | `String` | 灰度标记 |
| `topic` | `String` | `@NotNull @Length(min=1,max=64)` |
| `msgId` | `String` | `@NotNull`；通常可作为 MQ key / message id |
| `partition` | `Integer` | 分区 |
| `executeTime` | `Long` | 执行时间 / 延迟投递相关字段，具体语义看目标 MQ 实现 |
| `data` | `Object` | `@NotNull`；业务消息体 |
| `customPassThrough` | `Map<String,String>` | 自定义透传上下文 |
| `createTime` | `Long` | 创建时间 |
| `dataFullName` | `String` | `data` 类型全名，反序列化/消费方类型匹配时有意义 |

## 3. MessageDto 方法语义 [FACT ✅]

### `check()`

```java
public void check() {
    Validators.assertjsr303(this, new Class[0]);
}
```

生成发送逻辑时建议在入 MQ 前调用 `messageDto.check()` 或至少保证必填字段完整：`tenantId`、`topic`、`msgId`、`data`。

### `getContext()`：发送前采集上下文

关键行为：

1. `transferRequestContext = TransferRequestContext.get()`。
2. `traceId = RequestContext.get().getTraceId()`；为空时用 `Ids.gidString()`。
3. 从 `RequestContext` 获取 `tenantId`；为空时抛：
   `BootException.throwIt("BOOT_3000", "发送mq時上下文中的tenantId為空，不允许发送mq，请检查请求来源是否合法")`。
4. 从 `RequestContext` 获取 `secretLevel`；为空只打错误日志，仍允许发送。
5. 复制 `customPassThrough`。

生成发送代码时的含义：

- 不要自己伪造租户上下文。
- 如果上游没有 RequestContext，需要在调用 MQ SPI 前先建立合法上下文，否则 `tenantId` 可能为空。
- `secretLevel` 为空不是硬失败，但下游若依赖密级会出错，应在日志/报告提示。

### `setContext()`：消费时恢复上下文

关键行为：

1. 如果 `transferRequestContext != null`，调用 `transferRequestContext.setAll()`。
2. 否则设置：
   - `RequestContext.tenantId = tenantId`
   - `traceId` 为空则生成 `Ids.gidString()`
   - `RequestContext.traceId = traceId`
   - `RequestContext.secretLevel = secretLevel`
3. 如果 `customPassThrough` 非空，设置到 `RequestContext`。
4. 如果最终 `RequestContext.secretLevel == null`，记录错误日志。

消费实现的含义：

- 消费端反序列化得到 `MessageDto` 后，应确保进入平台 listener 前上下文能被恢复。
- 样例通过 `MessageListenerService.invoke(messageDto)` 进入平台消费链；不要只处理 `messageDto.getData()`。
- 自己实现消费转发时不得丢弃 `MessageDto` 包装层，否则 `tenantId`、`traceId`、`secretLevel`、`customPassThrough` 会丢。

## 4. 依赖来源 [FACT ✅ / 待现场版本确认]

反编译代码显示 `MessageDto` 依赖以下平台类：

```java
com.seeyon.boot.annotation.DtoInfo
com.seeyon.boot.context.RequestContext
com.seeyon.boot.context.TransferRequestContext
com.seeyon.boot.exception.BootException
com.seeyon.boot.util.ToStringUtils
com.seeyon.boot.util.id.Ids
com.seeyon.boot.util.validate.Validators
```

第三方/标准依赖：

```java
java.io.Serializable
java.util.Map
java.util.List
javax.validation.constraints.NotNull
org.hibernate.validator.constraints.Length
org.apache.commons.collections4.MapUtils
org.slf4j.Logger
org.slf4j.LoggerFactory
```

平台 Maven 坐标当前入口记录为：

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>boot-starter-mq</artifactId>
  <version>5.8.0</version>
</dependency>
```

版本注意：`5.8.0` 来自已沉淀的 MQ 扩展文档；实际项目版本必须以现场 POM / 反编译 jar 为准。

## 5. 代码生成时的最低字段要求

发送 `MessageDto` 前至少要能解释这些字段：

```text
topic     必填，1..64
msgId     必填，建议全局唯一，可作为 MQ key
data      必填，业务对象；必须保证消费端可反序列化/可识别
tenantId  必填，通常由 MessageDto.getContext() 从 RequestContext 获取
traceId   建议透传；为空可生成
secretLevel 建议透传；为空允许发送但有风险
```

推荐发送流程：

```java
messageDto.getContext();
messageDto.check();
byte[] body = MQSerializer.serialize(messageDto);
```

推荐消费流程：

```java
MessageDto messageDto = MQSerializer.deserialize(message.getBody());
MessageListenerService listener = Apps.getBeanFactory().getBean(MessageListenerService.class);
listener.invoke(messageDto);
```

## 6. 已知生成风险

1. **只序列化 `data` 是错的**：会丢 `tenantId`、`traceId`、`secretLevel`、`customPassThrough`。
2. **不设置/不恢复上下文是错的**：平台消费链依赖 `MessageDto` 包装层和 RequestContext。
3. **默认方法返回 true 不能当实现**：生成类必须真实实现发送/订阅逻辑。
4. **`sendBatch` 不能无脑 return true**：循环发送时至少要聚合失败结果。
5. **`unSubscribeTopic` 能力依赖目标 MQ client**：不支持时要明确标注，不要假装成功。
6. **版本敏感点**：字段、注解、平台工具类可能随 V8/boot-starter-mq 版本变化；遇到现场 jar/反编译代码，以现场为准更新本 contract。

## 7. MQSerializer 契约 [FACT ✅]

来源：用户提供 IntelliJ IDEA / Fernflower 反编译代码。

FQN：

```java
com.seeyon.boot.starter.mq.serializer.MQSerializer
```

方法签名：

```java
public static MessageDto deserialize(byte[] data)
public static byte[] serialize(MessageDto messageDto)
public static void setBigDataSize(int bigDataSize)
```

### `deserialize(byte[])`

反序列化流程：

1. 优先使用 `JacksonSerializer.deserialize(data, MessageDto.class)`。
2. 失败后降级为 `JsonUtils.fromJson(new String(data), MessageDto.class)`。
3. 再失败则记录 warn：`消息反序列化失败,改用String反序列化`。
4. 最终可能返回 `null`。

生成/消费代码约束：

- 调用 `MQSerializer.deserialize(message.getBody())` 后必须考虑返回 `null` 的风险。
- 外部 MQ client 回调中如果 `deserialize` 返回 `null`，不应继续调用 `MessageListenerService.invoke(null)`。
- 除非现场有特殊兼容要求，不要自己替换成 JSON 工具；平台已经内置 Jackson + JSON fallback。

### `serialize(MessageDto)`

序列化流程：

1. 使用 `JacksonSerializer.serialize(messageDto)`。
2. 如果序列化后字节长度 `> bigDataSize`：
   - 创建 `new LocalContext.Data(System.currentTimeMillis(), (long) bytes.length)`
   - 调用 `LocalContext.set(data)`
3. 返回 byte[]。

依赖类：

```java
com.seeyon.boot.starter.mq.context.LocalContext
com.seeyon.boot.starter.mq.support.dto.MessageDto
com.seeyon.boot.util.JsonUtils
com.seeyon.boot.util.serialize.JacksonSerializer
```

生成约束：

- 发送端必须序列化完整 `MessageDto`，不能只序列化 `data`。
- 大消息监控通过 `LocalContext` 记录，不要绕过 `MQSerializer`，否则可能丢失平台监控/上下文行为。
- `bigDataSize` 默认值来自静态字段，实际阈值可能由平台启动配置调用 `setBigDataSize` 设置；不要在 SPI 实现中随意改。

## 8. MessageListenerService 契约 [FACT ✅]

来源：用户提供 IntelliJ IDEA / Fernflower 反编译代码。

FQN：

```java
com.seeyon.boot.starter.mq.consumer.listener.MessageListenerService
```

核心方法签名：

```java
public void invoke(MessageDto messageDto)
public void invoke(List<MessageDto> messageDtoList) throws Throwable
public MessageListener addMessageListener(String topic, String processClassName, String processMethodName, String processParameterName)
public MessageListener addMessageListener(String topic, Object processBean, Method processMethod)
public MessageListener addMessageListener(String topic, Class messageProcessClass, String messageProcessMethodName)
public MessageListener removeMessageListener(String topic, String processClassName, String processMethodName, String processParameterName)
public boolean antiDuplicate(MessageDto messageDto)
public boolean topicMessageListenerIsEmpty(String topic)
public Map getAllMessageListener()
```

### `invoke(MessageDto)` 消费链路

关键流程：

1. `messageDto.setContext()`：恢复 `RequestContext` / trace / tenant / secretLevel / customPassThrough。
2. 设置 MDC：`appId`、`traceId`、`tenantId`。
3. 执行 `antiDuplicate(messageDto)`。
4. 计算 topicKey：
   - `DynamicMessageDto`：使用 `getInnerTopic()`。
   - 非 `eventbus` engine：通过 `TopicConverter` 做 env/topic 转换。
5. 记录 MQ 日志和耗时监控。
6. `processDelay(messageDto)`：非单体且 `executeTime != null` 时，会把 `data` 从 String 反序列化回对象。
7. 查找 `listenerMap.get(topicKey)`。
8. 遍历 listener，根据动态订阅/参数类型匹配决定是否 `messageListener.onMessage(messageDto)`。
9. finally 中固定执行 `MDC.clear()` 与 `RequestContext.clear()`。

生成/接入约束：

- 外部 MQ 消费回调应该把完整 `MessageDto` 交给 `MessageListenerService.invoke(messageDto)`，不要直接调用业务 bean。
- `invoke` 内部负责调用 `messageDto.setContext()`，因此示例消费侧不需要手工 setContext，但不能丢失 `MessageDto` 包装层。
- `invoke` 会清理 `RequestContext` 和 MDC；不要在调用后依赖当前线程上下文继续执行业务逻辑。
- 如果 `MQSerializer.deserialize` 返回 `null`，进入 `invoke(null)` 会 NPE；SPI 实现应加空判断并返回重试/失败策略。

### `invoke(List<MessageDto>)`

批量消费流程：

1. 对每条消息提交到 `getInvokeTaskPool()` 并行执行 `invoke(messageDto)`。
2. 使用 `CountDownLatch` 最多等待 3 分钟。
3. 超时抛 `BootException`：`<engine>消息消费超时`。
4. 收集异常列表，结束后抛第一个异常。

样例注释“批量 invoke 为并行(多线程)处理”对应这里。

### 去重逻辑 `antiDuplicate(MessageDto)`

关键行为：

- `rebalanceEnable` 开启时，用 Redis `setIfAbsent` 写入 key：
  `SystemEnvironment.getEnv() + ":mq:" + Apps.getAppName() + ":" + topic + "::" + msgId`，TTL 15 分钟。
- `mqProperties.getConsumer().isAntiDuplicate()` 开启时，使用 Redis ZSet 检查 `MQMessageCompUtils.getTopicRedisKey()` 中是否已有 msgId。

生成/运行提示：

- `msgId` 必须稳定且唯一，否则去重失效或误丢消息。
- 多节点/重平衡场景依赖 Redis；现场 Redis 异常可能影响消费去重。

### 监听器匹配规则

`invoke` 中会根据以下条件触发 listener：

- listener 是动态订阅；或
- `messageDto.getData().getClass().getName().equals(listener.getProcessParameterName())`；或
- listener 参数是 `MessageDto`；或
- listener 参数是 `DynamicMessageDto`；或
- listener method 第一个参数类型 `isAssignableFrom(messageDto.getData().getClass())`。

因此：

- `data` 必须能被正确反序列化为实际类型。
- `dataFullName` / 类型兼容性对消费匹配有实际意义。
- 如果只传 String/Map 导致类型不匹配，可能出现“消息消费到了但没有 listener 处理”。

### 平台内部 Spring 注解说明

`MessageListenerService` 自身是平台内部 `@Service`，并使用 `@Autowired` 注入 Redis/EventBus/Nacos 等。这不改变客开 SPI 约束：自定义 SPI 实现类仍禁止使用 `@Autowired` / `@Service` / `@Component`，应通过 `Apps.getBeanFactory().getBean(...)` 获取平台 bean。

## 9. MessageListener 注解与 MessageListenerImpl 契约 [FACT ✅]

来源：用户提供 IntelliJ IDEA / Fernflower 反编译代码。

### 9.1 监听方法注解

FQN：

```java
com.seeyon.boot.starter.mq.consumer.anotations.MessageListener
```

注意包名是 `anotations`，不是常见拼写 `annotations`。

注解定义：

```java
@Target({ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface MessageListener {
    String topic();
    boolean broadcast() default false;
}
```

含义：

- 标注在方法上。
- `topic()` 必填。
- `broadcast()` 默认 `false`。

### 9.2 MessageListenerImpl

FQN：

```java
com.seeyon.boot.starter.mq.consumer.listener.MessageListenerImpl
```

继承：

```java
public class MessageListenerImpl extends AbstractMessageListener
```

核心方法：

```java
public void onMessage(MessageDto message) throws Throwable
```

关键行为：

1. 检查 `RequestContext.traceId`，缺失时记录 warn。
2. 处理 `grayTag`：
   - 若消息带灰度标记，会结合 `NacosInstancesListener.hasGrayTag(grayTag)` 与 `SystemEnvironment.getGrayTag()` 判断当前实例是否允许消费。
   - 不匹配时抛 `RuntimeException("不能消费灰度消息")`。
   - 匹配后写入 `RequestContext.grayTag`。
3. 根据 `MqConstant.printLog(topic)` 与 `CommonLogProperties.getEnableMQ()` 决定是否打印完整消息体。
4. 如果 `message.getData() instanceof BaseMessageBodyDto`，会写入 `msgId`：
   `((BaseMessageBodyDto) message.getData()).setMsgId(message.getMsgId())`。
5. 动态订阅：
   - `dynamicSubscribe == true` 时，调用目标方法并传入完整 `MessageDto`。
6. 模块订阅：
   - 如果 `methodWrapper == null`，发布 `ModuleLoadEventPreInvoke`，尝试触发模块加载。
   - 如果监听方法参数是 `MessageDto` 或 `DynamicMessageDto`，传完整消息对象。
   - 否则按 `data` 类型传业务对象；类加载器不同则先 `JsonUtils.toJson/fromJson` 转成目标参数类型。
7. 普通订阅：
   - 直接调用监听方法，参数是 `message.getData()`。
8. finally 中记录 `StatisticsMonitor.recordExecution("MQ", listenerKey, cost, isFailure)`。

生成/排错结论：

- 如果业务监听方法参数是业务 DTO，平台最终传的是 `message.getData()`。
- 如果业务监听方法参数是 `MessageDto` / `DynamicMessageDto`，平台传完整消息包装。
- 动态订阅固定传完整 `MessageDto`。
- 类加载器不同场景会 JSON 二次转换，因此 `data` 类型必须可 JSON 序列化/反序列化。
- 灰度消息可能被非灰度实例拒绝消费；排查“消息到了但没处理”时要看 `grayTag` 与实例灰度标记。
- `BaseMessageBodyDto` 会被注入 `msgId`，业务 DTO 如继承该类可获得消息 ID。

## 10. TopicConverter / DynamicMessageDto 契约 [FACT ✅]

来源：用户提供 IntelliJ IDEA / Fernflower 反编译代码。

### 10.1 DynamicMessageDto

FQN：

```java
com.seeyon.boot.starter.mq.support.dto.DynamicMessageDto
```

定义：

```java
@DtoInfo("动态消息")
public class DynamicMessageDto extends MessageDto {
    @DtoAttribute("内部topic")
    private String innerTopic;
}
```

含义：

- 动态消息继承 `MessageDto`。
- 多一个 `innerTopic` 字段。
- `MessageListenerService.invoke` 遇到 `DynamicMessageDto` 时，会把 `messageDto.topic` 改成 `innerTopic`，并使用 `innerTopic` 作为 listenerMap key。

### 10.2 TopicConverter

FQN：

```java
com.seeyon.boot.starter.mq.converter.TopicConverter
```

核心字段：

```java
private static final String DYNAMIC_TOPIC_PREFIX = "DYNAMIC_";
private final Map<String, String> outerTopicMap = new ConcurrentHashMap();
private final Map<String, String> innerTopicMap = new ConcurrentHashMap();
```

核心方法：

```java
public void addTopicItem(String innerTopic)
public boolean containsInnerTopic(String innerTopic)
public String getInnerTopic(String outerTopic)
public String getOuterTopic(String innerTopic)
public String getTopicIncludeEnv(String outerTopic)
public String getTopicExcludeEnv(String topic)
public boolean isDynamicTopic(String innerTopic)
```

转换规则：

1. `addTopicItem(innerTopic)`：
   - 先转大写 outerTopic。
   - 如果不跳过转换，则 `generateOuterTopic(innerTopic)` 生成 `DYNAMIC_<partition>`。
   - 否则直接建立 outer/inner 映射。
2. `generateOuterTopic(innerTopic)`：
   - `partition = Math.abs(innerTopic.hashCode()) % mqProperties.getTopicPartitionLength()`
   - outer topic 为 `DYNAMIC_<partition>`。
3. `getTopicIncludeEnv(outerTopic)`：
   - 如果没有环境前缀，则加 `ENV_` 前缀，并把 `.` / `-` 替换为 `_`。
4. `getTopicExcludeEnv(topic)`：
   - 如果有环境前缀，则去掉 `ENV_`。
5. `isSkipTopicConvert(innerTopic)`：
   - 如果 `topicPartitionEnable == false`，跳过转换。
   - 否则只有 `UDC_` 或 `DYNAMIC_` 前缀会进入动态分区转换；其他 topic 跳过。

生成/排错结论：

- 外部 MQ topic 不一定等于业务 inner topic；平台可能按环境和动态分区转换。
- 非 `eventbus` engine 消费时，`MessageListenerService.invoke` 会通过 `TopicConverter` 把外部 topic 转回内部 topic。
- 生成 SPI 时不要自作主张改写 `messageDto.topic`；发送和订阅时应尊重平台转换链路。
- 如果出现“订阅 topic 和业务监听 topic 对不上”，优先检查 `topicPartitionEnable`、`topicPartitionLength`、环境前缀、`UDC_`/`DYNAMIC_` 前缀。

## 11. MQProperties 配置契约 [FACT ✅]

来源：用户提供 IntelliJ IDEA / Fernflower 反编译代码。

FQN：

```java
com.seeyon.boot.starter.mq.MQProperties
```

配置前缀：

```java
@ConfigurationProperties(prefix = "seeyon.mq")
public class MQProperties
```

顶层字段默认值：

| 配置 | 默认值 | 说明 |
|---|---:|---|
| `seeyon.mq.enable` | `false` | MQ 总开关 |
| `seeyon.mq.engine` | `rocketmq` | MQ 引擎；`MessageListenerService` 对 `kafka` 有特殊分支 |
| `seeyon.mq.servers` | null | 服务地址 |
| `seeyon.mq.userName` | null | 用户名 |
| `seeyon.mq.password` | null | 密码 |
| `seeyon.mq.bigDataSize` | `Integer.MAX_VALUE` | 大消息阈值，关联 `MQSerializer.setBigDataSize` / `LocalContext` |
| `seeyon.mq.topicPartitionEnable` | `true` | topic 动态分区开关 |
| `seeyon.mq.topicPartitionLength` | `8` | 动态 topic 分区数量 |
| `seeyon.mq.spiPlugins` | `[]` | SPI 插件列表 |

Producer 默认值：

| 配置 | 默认值 |
|---|---:|
| `seeyon.mq.producer.enable` | `false` |
| `seeyon.mq.producer.maxBatchSize` | `100` |
| `seeyon.mq.producer.maxMessageSize` | `8388608` |
| `seeyon.mq.producer.group` | `Provider_` + `Apps.getAppName()` |
| `seeyon.mq.producer.activeCommit` | `true` |

Consumer 默认值：

| 配置 | 默认值 |
|---|---:|
| `seeyon.mq.consumer.group` | `ENV_` + `Apps.getAppName()` |
| `seeyon.mq.consumer.broadcast` | `false` |
| `seeyon.mq.consumer.enable` | `true` |
| `seeyon.mq.consumer.batchSize` | `50` |
| `seeyon.mq.consumer.minThreads` | `10` |
| `seeyon.mq.consumer.maxThreads` | `50` |
| `seeyon.mq.consumer.queueCapacity` | `400` |
| `seeyon.mq.consumer.antiDuplicate` | `false` |
| `seeyon.mq.consumer.enableOffsetLog` | `true` |
| `seeyon.mq.consumer.enableConsumerLog` | `true` |

SSL 配置：

```text
seeyon.mq.ssl.truststoreLocation
seeyon.mq.ssl.truststorePassword
seeyon.mq.ssl.mechanism
seeyon.mq.ssl.protocol
```

生成/部署结论：

- 平台原生 MQ 配置前缀是 `seeyon.mq`。
- `ali-rocketmq` 示例里的 `seeyon.ones.*` 是示例 SPI 自己读取的三方 ONS 配置，不等同于平台原生 `seeyon.mq.*`。
- 生成通用 MQ SPI 时，应明确区分：平台 MQ 配置 `seeyon.mq.*` 与三方客户端配置 `seeyon.<custom>.*`。
- topic 动态分区默认开启，长度默认 8；跨环境/跨 topic 排错必须考虑转换规则。

## 12. AbstractMessageListener / MQMessageCompUtils / NacosInstancesListener / MqConstant 契约 [FACT ✅]

来源：用户提供 IntelliJ IDEA / Fernflower 反编译代码。

### 12.1 AbstractMessageListener

FQN：

```java
com.seeyon.boot.starter.mq.consumer.listener.AbstractMessageListener
```

注意：它实现的是平台消费 listener 接口：

```java
public abstract class AbstractMessageListener implements MessageListener
```

这里的 `MessageListener` 是 `com.seeyon.boot.starter.mq.consumer.listener.MessageListener`，不是注解 `com.seeyon.boot.starter.mq.consumer.anotations.MessageListener`。

核心字段：

```java
protected String topic;
protected boolean dynamicSubscribe = false;
protected MethodWrapper methodWrapper;
private String processClassName;
private String processMethodName;
private String processParameterName;
protected String moduleName;
```

listenerKey 规则：

```java
processClassName + "#" + processMethodName + "#" + processParameterName
```

模块订阅判断：

```java
StringUtils.isNotBlank(moduleName)
```

生成/排错结论：

- 同一 topic 下 listener 去重/查找依赖 `processClassName#processMethodName#processParameterName`。
- 如果监听方法参数类型不一致，即使类和方法名相同，也会形成不同 listenerKey。
- `moduleName` 非空即为模块订阅；模块订阅可能触发模块预加载。
- `clearMethodWrapper()` 会清空方法包装，但保留 listener 元数据。

### 12.2 MethodWrapper 契约 [FACT ✅]

来源：用户提供 IntelliJ IDEA / Fernflower 反编译代码。

FQN：

```java
com.seeyon.boot.starter.mq.consumer.wrapper.MethodWrapper
```

字段：

```java
private final Object bean;
private final Method method;
```

构造方法：

```java
public MethodWrapper(Object bean, Method method)
```

核心方法：

```java
public Object getBean()
public Method getMethod()
public String getMethodName()
```

`getMethodName()` 规则：

```java
method.getDeclaringClass().getName() + "#" + method.getName() + "#" + method.getParameterTypes()[0].getName()
```

结论：

- MQ listener 方法 key 与 `AbstractMessageListener` 的 listenerKey 规则一致，核心都是 `class#method#firstParameterType`。
- 监听方法必须至少有一个参数，否则 `getParameterTypes()[0]` 会越界。
- 参数类型是 listener 匹配和分发的关键：业务 DTO、`MessageDto`、`DynamicMessageDto` 会走不同分发路径。
- `bean` 和 `method` 都参与 equals/hashCode；同方法不同 bean 不是同一个 wrapper。
- 之前出现的 `com.alibaba.excel.support.cglib.core.MethodWrapper` 是 EasyExcel/cglib 内部类，不是 MQ wrapper，不能作为 MQ Contract。

### 12.3 MQMessageCompUtils

FQN：

```java
com.seeyon.boot.starter.mq.util.MQMessageCompUtils
```

核心方法：

```java
public static String getTopicRedisKey()
public static MQMessageSpi getMQMessageSpi(List<String> spiPlugins)
public static void initMQSpi(List<String> spiPlugins)
public static RedisTemplate buildRedisTemplate(MQProperties properties)
```

关键行为：

1. `getTopicRedisKey()`：
   - `CacheUtils.getCacheKeyWithoutTenantIdAndAppName(Apps.getAppName(), "topic")`
2. `getMQMessageSpi(spiPlugins)`：
   - 若缓存为空，先 `initMQSpi(spiPlugins)`。
   - 再从 Spring BeanFactory 获取 `MQMessageSpi.class` bean。
   - 找不到则抛 `BusinessException`：`沒有找到MQ SPI实现,请检查SPI代码`。
3. `initMQSpi(spiPlugins)`：
   - `spiPlugins` 非空时调用 `SPIJarLoader.loadSPIPlugins(spiPlugins, false)`。
   - 失败只记录 `MQ SPI加载失败` 日志，不直接抛出。
4. `buildRedisTemplate(MQProperties)`：
   - 如果 `properties.servers` 非空，按逗号判断 cluster，否则按 `host:port` 建 standalone。
   - 支持 username/password。
   - 默认 database = 0。
   - serializer：`JacksonRedisSerializer` + `StringRedisSerializer` key/hashKey。
   - 如果 `servers` 为空，使用平台默认 `redisTemplate` bean。

生成/部署结论：

- MQ SPI 能被平台发现，最终要能通过 `Apps.getBeanFactory().getBean(MQMessageSpi.class)` 拿到。
- `spring.factories` / SPI 插件加载 / `seeyon.mq.spiPlugins` 是发现链路的一部分。
- 如果报“沒有找到MQ SPI实现”，优先查：`spring.factories`、SPI jar 是否加载、`spiPlugins`、scope、服务重启。
- `seeyon.mq.servers` 可影响 MQ 去重 Redis 使用独立 Redis 还是平台默认 Redis。

### 12.4 NacosInstancesListener

FQN：

```java
com.seeyon.boot.starter.mq.listener.NacosInstancesListener
```

核心方法：

```java
public boolean hasGrayTag(String grayTag)
public void refresh()
public void run() throws Exception
```

关键行为：

- 启动时遍历 `Apps.getAppNames()`，从 `RegisterCenterService` 获取各应用实例。
- 读取实例 metadata 中的 `seeyon.gray.tag`，维护 `appGrayTagSet`。
- 对每个 appName 注册 Nacos 订阅，实例变化时刷新灰度 tag 集合。

生成/排错结论：

- `MessageListenerImpl` 的灰度消费判断依赖这里维护的全局灰度 tag 集合。
- 灰度消息消费失败时，要查 Nacos 实例 metadata：`seeyon.gray.tag`。
- 如果当前环境灰度标记与消息 `grayTag` 不匹配，平台会抛“不能消费灰度消息”。

### 12.5 MqConstant

FQN：

```java
com.seeyon.boot.starter.mq.common.MqConstant
```

常量：

```java
String ignoreLogTopic = SystemEnvironment.getEnv().toUpperCase() + "_AUDIT_LOG";
String CTP_MQ_SUBSCRIBE_KEY = SystemEnvironment.getEnv() + ":" + ":" + "ctp_mq_subscribe";
```

日志判断：

```java
static boolean printLog(String topic) {
    return !ignoreLogTopic.equals(topic);
}
```

结论：

- 审计日志 topic：`ENV_AUDIT_LOG` 不打印完整 MQ body 日志。
- 其他 topic 在 `CommonLogProperties.getEnableMQ()` 开启时可能打印 body；敏感消息要注意日志暴露风险。
