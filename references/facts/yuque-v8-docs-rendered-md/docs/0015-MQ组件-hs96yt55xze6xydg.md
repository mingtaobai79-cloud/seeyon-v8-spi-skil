---
title: "MQ组件"
source: "https://www.yuque.com/seeyonkk/v8/hs96yt55xze6xydg"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# MQ组件

> Source: https://www.yuque.com/seeyonkk/v8/hs96yt55xze6xydg

作者：陈晓东

时间：2025-08-15

##### 1、组件介绍

MQ组件提供基于RocketMQ和Kafka的消息发布/订阅功能

##### 2、配置说明

```
seeyon:
  mq:
    enable: true #是否开启
    engine: rocketmq #可选 rocketmq|kafka 默认为：rocketmq
    servers: 127.0.0.1:9876 # rocket nameServer地址或者kafka服务地址，多个地址用逗号隔开
    producer:
      enable: false # 生产端是否开启
      group: Provider_Customer # 生产端分组标识,仅rocketmq生效
    consumer:
      enable: false # 消费端是否开启
      batch-size: 1 # 批量消费消息数
      min-threads: 10 # 最小线程数
      max-threads: 50 # 最大线程数
```

##### 3、组件使用

###### 3.1 Maven坐标

```xml
<dependency>
        <groupId>com.seeyon</groupId>
        <artifactId>boot-starter-mq</artifactId>
        <version>版本号</version>
    </dependency>
```

###### 3.2 消息发送

提供MessageProducer接口用于消息的发送。

消息发送接口定义如下：

```
public interface MessageProducer {
    /**
     * 发送消息到mq服务器,此方法消息发送和当前事务有关
     * 1.如果存在事务,则事务提交成功之后才发消息,异步发送,如果消息发送失败,不抛异常，定时重发;
     * 2.否则直接发送消息,同步发送,消息发送失败,不抛异常,定时重发;
     * @param message
     * @return 消息ID，如果需要修改和删除（只适用于延迟消息），则需应用回传，
     */
    String send(BaseMessage message);

    /**
     * 同步发送消息到mq服务器,此方法消息发送和事务无关,如果消息发送失败,抛异常,不定时重发
     *
     * @param message
     * @return
     */
    boolean sendDirectOneTime(BaseMessage message);
}
```

要发送mq消息首先要创建一个类继承BaseMessage类,并且指定泛型(泛型为实际的消息体类型,可以为任何Object类型)。

实现类上使用@MessageInfo注解标注该消息的元数据信息(必须描述,为了抽取mq消息元数据),topic,tags和description。

其中topic是主题；tags是标签。两者结合唯一确定一个Channel。

```java
//MessageInfo注解必须添加,不添加发送mq消息时会抛异常
@MessageInfo(topic = MetadataMessageConstants.MESSAGE_TOPIC, tags = MetadataMessageConstants.MESSAGE_TAG_ENTITY, value = "Entity元数据变动消息")
public class EntityMetadataChangeMessage extends BaseMessage<MetadataChangeMessage> {

}
```

定义好消息实现类之后就可以发送消息了。

发送的消息体对象可自定义，但需要实现Serializable接口,并使用swagger注解描述里边的字段(必须描述,为了抽取mq消息元数据)。

当发送消息在事务中执行时，会采用事务提交执行和补偿发送的策略；在非事务中执行时，直接发送消息。

```
private void sendMessage(){
    //MetadataChangeMessage要发送的实际的消息体对象
    MetadataChangeMessage msg = createChangeMessage();
    msg.set....
    EntityMetadataChangeMessage message = new EntityMetadataChangeMessage();
    if(message != null){
        message.setData(msg);
        messageProducer.send(message);
    }
}
```

###### 3.3 消息接收

```java
@Component
@Slf4j
public class OrderCreateMessageListener {

    @MessageListener(topic = MetadataMessageConstants.MESSAGE_TOPIC, tags= MetadataMessageConstants.MESSAGE_TAG_ENTITY)
    public void processChangeEntity(MetadataChangeMessage message) {
        log.info("received MQ中topic为{}的消息：{}","EntityChange", message);
    }
}
```

###### 3.4 消息消费端动态订阅

mq组件提供动态订阅消息的能力,调用MessageConsumer.dynamicSubscribe方法完成对指定通道的订阅,组件提供动态订阅持久化能力,应用启动后无需重新订阅.

MessageConsumer api

示例

###### 3.5 延迟消息

跟普通的MQ消息定义不同点就是延迟消息需要继承DelayBaseMessage，可以设置具体执行的时间，示例如下。

消息接收，跟普通的消息写法上一样

##### 4、特别说明

●
消息组件采用消息的补偿发送机制保证消息的可靠投递，也丧失了消息投递的有序性。

●
应用在使用消息组件构建业务时，不要依赖消息的有序性进行订阅消费，否则会导致不可预知的错误。
