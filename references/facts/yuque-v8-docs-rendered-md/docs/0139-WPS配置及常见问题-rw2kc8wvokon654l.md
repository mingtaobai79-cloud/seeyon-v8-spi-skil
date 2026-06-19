---
title: "WPS配置及常见问题"
source: "https://www.yuque.com/seeyonkk/v8/rw2kc8wvokon654l"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# WPS配置及常见问题

> Source: https://www.yuque.com/seeyonkk/v8/rw2kc8wvokon654l

作者：潘峰
最后更新：2026-06-09

# wps配置

wps配置分为v8侧和wps侧两部分，两者进行互相调用实现文档的相关能力。

# V8配置

### A01、入口

<img src="https://cdn.nlark.com/yuque/0/2026/png/68956708/1780809980392-f0082023-282a-4b56-8535-a601a5b53275.png" width="2879">

<img src="https://cdn.nlark.com/yuque/0/2026/png/68956708/1780809980537-3aa6522d-c0bc-450d-bef0-8fefb544fad5.png" width="2789">

### A02、通道设置为wps

<img src="https://cdn.nlark.com/yuque/0/2026/png/68956708/1780809980413-fcd6589e-88e5-4254-8d60-0cdbabe3d43b.png" width="2869">

### A03、参数设置

●
appId,appKey参考wps中台配置的P02章节

●
apiUrl:{wps中台域名}/open

●
domain:{v8域名}/open以上4个参数必须配置，其他参数看业务上需要

●
expandJson:扩展的一些参数，尤其默认的空白文档，尤其重要，参考下面文档中的1.1001008章节 https://docs.qq.com/doc/DZmdORldsVmd5cFdq?nlc=1

# wps中台配置

如果能够登录wps中台，那么参考如下配置

### P01、登录系统后，先关注一下是否过期

<img width="1553">

### P02、集成应用

<img width="2859">

<img width="2741">

<img width="2437">

●
回调地址：就是**{V8域名}/service/cip-capability/doc/wps**，所有功能的都是这么配置，都要检查一遍，尤其是在线预览和书签处理

●
白名单设置，将v8域名设置到白名单中

# 常见问题

●
1、公文拟文正文打开失败，原因可能是
1）空白文档设置不对，尤其是项目上一些迁移或者重装的环境，默认空白文档已经失效，参考A03章节
2）回调地址不对，或者网络不通。参考P02章节中的回调地址。

●
2、V8有ip和域名两个地址，跟wps中台配置的是ip地址，模板的文档打开失败，上传文档正常。
一般下面两种方式之一可解决：
1）wps中台和v8域名网络不通
2）5.30版本以上，如果wps中台和v8域名网络不通，通过配置参数filePathPrefixJson进行映射

●
3、预览时一直在转圈
1）回调地址不对，或者网络不通。参考P02章节中的回调地址。
2）白名单问题，参考P02章节中的白名单。
