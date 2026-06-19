---
title: "MQ扩展"
source: "https://www.yuque.com/seeyonkk/v8/qii2f3ybtoq43pnz"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# MQ扩展

> Source: https://www.yuque.com/seeyonkk/v8/qii2f3ybtoq43pnz

文档待完善

更新时间：2026.1.14

###### 1、使用场景

其他类型MQ中间件扩展

###### 2、生效范围

全系统

###### 3、集成步骤

参考SPI的开发规则：
开发准备

1、引入maven坐标

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>boot-starter-mq</artifactId>
  <version>5.8.0</version>
</dependency>
```

2、需要实现的SPI接口

```
com.seeyon.boot.starter.mq.spi.MQMessageSpi
```

3、接口详情

```
public interface MQMessageSpi {
    //消息发送
    default boolean send(MessageDto messageDto) {
        return true;
    }
    //批量发送消息
    default boolean sendBatch(List<MessageDto> messageDtoList) {
        return true;
    }
    //消息订阅
    default boolean subscribeTopic(String topic) {
        return true;
    }
    //取消消息订阅
    default boolean unSubscribeTopic(String topic) {
        return true;
    }
}
```

###### 4、重启服务

需要重启所有服务

###### 5、示例代码

ali-rocketmq.zip
(19 KB)
