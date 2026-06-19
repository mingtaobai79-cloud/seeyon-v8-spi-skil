---
title: "事件监听"
source: "https://www.yuque.com/seeyonkk/v8/ewvnzdah85uuwi5k"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 事件监听

> Source: https://www.yuque.com/seeyonkk/v8/ewvnzdah85uuwi5k

作者：陈晓东

时间：2025-08-15

##### 1、应用内事件监听

使用@EventHandler 、@EventSubscribe注解进行标注。具体监听哪个事件根据入参（消息体）:

AfterCreateEvent<com.seeyon.jichupeixun6416391523783754075.dto.PeixundibiaoDto> 来确认

```java
@Slf4j
@EventHandler
public class PeixunInnerEventListener {

    @EventSubscribe
    public void onAfterCreateEvent(AfterCreateEvent<com.seeyon.jichupeixun6416391523783754075.dto.PeixundibiaoDto> message){
        log.info("PeixunInnerEventListener.onAfterCreateEvent");
    }
}
```

##### 2、应用间事件监听

使用@Component、@MessageListener(topic= {})注解进行标注。具体监听事件根据方法入参（消息体）确认

```java
@Component
public class PeixunEventListener {
    /**
     * 监听事项变动事件
     * @param message 消息体
     */
    @MessageListener(topic = AffairOpenConstants.AFFAIR_TOPIC)
    public void affairListenerMethod(AffairMessageDto message) {
        log.info("基础培训监听到事件");
        log.info("参数：" + JsonUtils.toJson(message));
        //TODO 向第三方发送消息
    }

    /**
     * topic 为：UDC_应用编码_MQ,其中应用编码字母大写
     * @param message 消息体
     */
    @MessageListener(topic = "UDC_JICHUPEIXUN6416391523783754075_MQ")
    public void onSeeyonUdcTestEvent(com.seeyon.jichupeixun6416391523783754075.dto.ZichanxinxiluruPeixundibiao message) {
        log.info("基础培训监听到当前应用事件");
        log.info("参数：" + JsonUtils.toJson(message));
        //TODO 向第三方发送消息
    }
}
```

##### 3、注意事项

消息体的获取方式，后台管理-》集成平台-》开发平台-》事件管理  选中具体事件进行查看

##### 4、UDC预置事件

事件包路径com.seeyon.udc.common.event

TRANSACTIONSUCCESSCREATEBATCHEVENT
TRANSACTIONSUCCESSUPDATEBATCHEVEN
RANSACTIONSUCCESSUPDATEBVENT
TRANSACTIONSUCCESSCREATEEVENT
TRANSACTIONSUCCESSDELETEBATCHEVENT
FORMLOADSUCCESSEVENT
LRANSACTIONSUCCESSDELETEEVEN
BEFOREDELETEBATCHEVENT
AFTERUPDATEBATCHEVENT
AFTERBPMPROCESSEVENT
BEFOREUPDATEBATCHEVENT
AFTERDELETEBATCHEVE
AFTERCREATEBATCHEVENT
BEFOREDELETEEVENT
ABSTRACTBATCHEVENT
AFTERUPDATEEVENT
AFTERDELETEEVENT
BEFORECREATEEVENT
CHANGEEVENTDAT
BEFORECREATEBATCHEVENT
OBEFOREUPDATEEVE
AFTERCREATEEVENT
O
CAFTE
OBEF
OT
CF

##### 5、BPM、组织、人员监听示例

注意创建人员的时候会同步发送任职等消息，并非创建人员消息，具体类型可以参考

import com.seeyon.organization.message.core.OrgMessageConstants;
