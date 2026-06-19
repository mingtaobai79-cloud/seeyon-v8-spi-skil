---
title: "启信宝"
source: "https://www.yuque.com/seeyonkk/v8/lf6ug4tttyywm7fg"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 启信宝

> Source: https://www.yuque.com/seeyonkk/v8/lf6ug4tttyywm7fg

作者：潘峰
最后更新：2026-06-09

# V8入口

后台登录→基础能力接入→企业征信→切换通道启信宝

扩展字段X:基础能力接)
7A7E21BC-F482-40E1-9B0D-6C4850CC068
当前通道:启信宝-服务
述:提供企业基础工商信息,工商股东
后台管理致远互联PRE
HTTP://API.GIXINCOR
RE.SEEYONV8.COM/SEEYON/MAI
8关闭全部
日志列表用量统
基础能力接)
三方应用集成
启信宝-服务
致远互联-服
服务参数配
SECRETKEY
,工商股东,融资信息,行政处罚,产品信息,行政许可等企业征信信息查询
企业征信
切换通道
应用通道管理
开放平台
测试-服务
管理首页
已启用
基础信息
基础设置
能力配置
APPKEY
豆运维监控
参数名
停用
默认值
已启用
APIURL
OCIP
O吕
已启用
OOOOOOO.
V

apiUrl：固定值 http://api.qixin.com

appkey和secretkey，从启信宝三方获取（详见下面章节），或者找客户问询

# 启信宝端

### 第1步：登录启信宝开放平台账号

后台地址：https://data.qixin.com/，登录账号。

<img src="https://cdn.nlark.com/yuque/0/2026/png/68956708/1780889466744-f5ff8518-cc00-4cf8-b678-e003505e15e4.png" width="1908">

### 第2步：获取授权信息

登陆后，点击右上角头像，选择「我的API」，再点击左侧菜单栏的「安全中心」-「APP KEY」，即可得到「appkey」和「appsecret」。然后对接口进行授权。

光
启信宝数据AP平台
请输入接口名称/接口ID
可视化测试
我的钱包
APIIP白名单
接口授权
我的API
AP列表
安全中心
充值中心
账号信息
我的钱包
安全退出
APPKEY
APPKEY
AP接口
帮助中心
我的发票
安全中心
重置密铝
我的AP
置密码
充值记录
3
空钥
显示KE
刘账单
豆制
KEY

# 问题排查

碰到调用启信宝异常、超时等情况，浏览器F12，录制调用启信宝的动作，如下图，获取到traceId

<img width="1338.5">

查询cip-capability服务的日志，按照traceId搜索，可以看到异常原因

<img width="1327.5">
