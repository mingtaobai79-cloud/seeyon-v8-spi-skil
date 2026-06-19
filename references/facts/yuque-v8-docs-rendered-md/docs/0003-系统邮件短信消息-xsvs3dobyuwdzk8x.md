---
title: "系统邮件短信消息"
source: "https://www.yuque.com/seeyonkk/v8/xsvs3dobyuwdzk8x"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 系统邮件短信消息

> Source: https://www.yuque.com/seeyonkk/v8/xsvs3dobyuwdzk8x

作者：陈晓东

时间：2025年10月29日

###### 1、参考代码

```
MessageSend messageSend = new MessageSend();
MessageSendDto messageSendDto = new MessageSendDto();
List<UserDto> userDtos = new ArrayList<>();
//消息类型由MessageChannelEnum决定
List<MessageChannelEnum> messageChannelEnums = Arrays.asList(MessageChannelEnum.EMAIL);
for (Long id : personIds) {
    UserDto userDto = new UserDto();
    userDto.setUserId(id);
    userDtos.add(userDto);
}
messageSendDto.setMessageChannelList(messageChannelEnums);
messageSendDto.setUserDtoList(userDtos);
//todo 确认邮件内容
messageSendDto.setMessageSourceCode("kjzhglxt802852354613790726");
messageSendDto.setMessageTypeCode("default");
messageSendDto.setTitle("考勤异常处理");
messageSendDto.setContentJson("科室存在异常考勤数据，请尽快处理。");
messageSend.setData(messageSendDto);
messageProducer.send(messageSend);
```

###### 2、消息参数MessageSendDto详解

消息发送参数解释.txt
(3 KB)

###### 3、必填参数

提前在消息中心注册过的类型,如果没有注册可以填入"DEFAU1
此子列表为接收者ID,一条消息可以同时发给多个人,这里列表
如果不需要国际化的消息,这里直接填入消息的标题即可,长度
如果是系统消息发送者填八:COM,SEEYON.BOOT.COMMON.C
必须是提前在消息中心注册过的应用的APPNAME
如果想隐藏发送者填八:COM.SEEYON.BOOT,COMMON.CONST
MESSAGESOURCECODE消息来源
MESSAGETYPECODE消息类型码
DTO中必填字段解释
SENDERID发送者ID
发送USERID
USERDTO.USERID
接收者ID
标题
TITLE
