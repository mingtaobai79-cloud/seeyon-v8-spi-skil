---
title: "MQ消息规范"
source: "https://www.yuque.com/seeyonkk/v8/vdlfzwdaafl67yr9"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# MQ消息规范

> Source: https://www.yuque.com/seeyonkk/v8/vdlfzwdaafl67yr9

## MQ消息规范

1
【强制】topic只能包含大写字母数字和下划线。

2
【强制】topic命名请使用和业务有关名词,不要包含"topic"和"tag"字样。

3
【强制】topic不允许出现下划线以外的其他特殊字符。

4
【强制】topic长度不许超过50字符。

5
【强制】消息的定义方把topic定义为常量和消息体Dto一起放到facade层,方便其他应用订阅使用。

6
【强制】消息内容不允许超过1M
