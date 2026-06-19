---
title: "电子邮件"
source: "https://www.yuque.com/seeyonkk/v8/lonl0sev2do5sswq"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 电子邮件

> Source: https://www.yuque.com/seeyonkk/v8/lonl0sev2do5sswq

作者：陈晓东

时间：2026.1.4

###### 1、使用场景

集成三方电子邮件系统，基础邮件服务，提供邮件消息、邮箱登录、自定义邮件模板等能力

###### 2、操作步骤

SPI开发规则，参考：
开发准备

1、工程中加入maven依赖

```xml
<dependency>
    <groupId>com.seeyon</groupId>
    <artifactId>cip-connector-api</artifactId>
    <version>${platform.version}</version>
</dependency>
```

2、实现SPI接口

```
com.seeyon.cip.provider.api.email.EmailProviderService
```

3、切换能力通道

切换到自己集成的对应通道，设置好对应的基础信息

描述基础邮件服务,提供邮件消息,邮箱登录,自定义邮件模
模板管理日志列表限流设置用量统
账户名:2660555181@QQ.COM
邮箱账户:2660555181@QQ.COR
SMTP服务器:SMTP.QGCON
协同运营平台
电子邮件
台海之韵DEMO简称
切换通道
邮件设置
当前通道:SMTP-服务
SMTP-服务
用通道管理
三方应用集成
8关闭全部
书基础设置
能力配置
基础能力接
测试-服务
能力配置
理首页
停用
开放平台
当前通道
已启用
基础信息
密码:OOO
OCIP
未启用
09

###### 3、参考demo

SmtpEmailProviderServiceImpl.java
(21 KB)
