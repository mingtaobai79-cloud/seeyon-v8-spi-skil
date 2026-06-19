---
title: "在线文档"
source: "https://www.yuque.com/seeyonkk/v8/hnoy0cnu8t5rl97o"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 在线文档

> Source: https://www.yuque.com/seeyonkk/v8/hnoy0cnu8t5rl97o

作者：陈晓东

时间：2026.1.5

###### 1、使用场景

提供文档在线预览、在线编辑、在线转版、套红、文字/图片水印等文档能力

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
com.seeyon.cip.provider.api.doc.DocOnlineProviderService
```

3、接口定义

​
Java
运行代码
复制代码

###### 3、示例demo

WPS集成：

WpsOnlineServiceImpl.java
(57 KB)

###### 4、使用配置

代码提交构建以后，在能力配置页面切换到对应的通道，如下图，切换到对应通道配置好参数，重启cip-connector服务后即可使用

HTTPS//DEV-XTCV8.SEEYONCLOUD.COM/SERVICE
提供文档当在线预览,在线编辑,在线转版,套红,文字/
日志列表用量统
HTTP://10.1.101.30/OPEN
YKUDGXCYMBBPPKY
海之韵DEMO简称
在线文档
协同运营平台
当前通道:WPS-服务
路三方应用集成
页能力配置
切换通道
基出能力接入
文档通-服务
础出信息
盛基础设置
豆开放平台
服务参数配置
永中-服务
应用通道管理
数科-服务
APPKEY
联想-服务
关闭全部
能力配置
停用
APIURL
OCIP
黑默认值
WPS-服务
DOMAIN
未启用
APPLD
理首页
测试-服务
已启用
6昌
已启用
编
参数名
已启用
元
