---
title: "nacos开关"
source: "https://www.yuque.com/seeyonkk/v8/lw1x44oiovko3ybv"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# nacos开关

> Source: https://www.yuque.com/seeyonkk/v8/lw1x44oiovko3ybv

作者：杨颜华、陈晓东、李阳CD

●
时间：2025-11-17

## 1、第三方应用集成配置的接口修改超时时间

配置方式：nacos中添加 seeyon connector httpTimeOut 参数后设置超时时间，cip-connector服务默认超时时间是10秒

INMANGMUQUANLI5255129282792932340泛化调用NUL]接日CORM:SEEY
ICEZHUSHUJUPINGTA.GETESTDATA超时超时时间[5000]毫
3津B间2025062422:31:05
成用启动完成2025-09-0220:35:20
CLIENTCREDENTIAL
分类:默认分类
应用启动成功
营销管理系统
清除应用数据
WEB黄移动瑞
求居类型:APPLICA
测试启动完成
主数据及企业服务总
认证清求:否
清求方式:POST
名称:查询主步
主数据模型的主题名称
2025-09-02203520
是否异步:否
南运数球租务项用
P活金的出健列表
设计版本V1.0
请求参数
沙箱准备成功
显示名称
日数环婚环下标
用时5分24秒
ERSIONNAME
2025-08-0220
描:12
V基础信息
页面调试(BETA)
主数据模型名称
USERNAME
SOURCEFROM
北扣口减限运行日志
制全部信息
信息详情
LVAIDATESTRUECOANRA
检查贝国
节守类型
住别同中物册
执行状态全
质号机
消管理系剂1口
加理环山)
执行时用
SOURCEIP
微程运行日志
2025-0B-0220
发布版本
导第信租
CGMSEEYONCIPCONNECTORDYNARMIC.APPSER
执行先败
运行日志
202508-0220
PASSWORD
BOY
节点名称
页面测试
人出参
沙箱试
128.G7G
执行吃功
HEADER
接口
应用X
欧计日志
执行成功
更多
图
事件
20978
计数唯环
规运行日志
信息交换亲允
依赖口年
队列
关闭
荣单
QUERY
029.878
品品
立用
0
测试
打
口
包量物西
早
准新力中清引会
出参
目
社E中
4
应用
万点61
迎
AREL完

请球地E:HTTP://192.168.17.63/W2/API/GETENTITYDATA..
请求据类型:APPLICATIONJSO
主数据及企业服务总线平台
返回据类型:APPLICATIONISON
是否启用:是
YTECYFN日
名称:查询主数据数据
主数据模型的主题名称
分类:默认分类
猫述:12
方法名:GETESTDATA
NTITYNAME
出择数据源:-
CIENCREDENTAL
请求方式:POST
携带签名/秘铜:关闭
悬数类型
最示名称
MODELNAME
0参数显示
认证请求:否
是否异步:否
主数据模型名称
LIENTCREDENTAL
SOURCELP
参数名
SOURCELP
PASSWORD
SOURCEFROM
PATH(URD
请求参数
USERNAME
USERNAME
SOURCEFROM
PASSWORD
192.168.17.122
是否显示
AWARE][完
异常信息
基础信息
接口
数居
QUEY
文本
HEADER
是香必填
YTHC
BODY
置查
队列
默认值
接口
文杰
文本
文本
文本
123456
对象
应用
事件
文杰
迎
3
0
百
目
G
口
习
日走
豆
同步
设量
雪

DATABASE:CIP_CONNECTOR_DEV
:83185CAB05A3E820153AB671DFC491C7
配置详情
HTTPTIMEOUT:5OOOE
CIP-CONNECTOR
命名空间SEEYON-DE
DATASOURCE:
更多高级选项
CONNECTOR
DETAID
配置内容
SEEYON:
SEEYON
GROUP
MD5:831
描述

## 2、dubbo接口超时配置

配置方式，nacos的public下面找到dubbo配置下面的timeout，默认是5s

MD5:CE356983B17E464FC43B1978B5D9D6D5
PROVIDER-1OG:TRU
MAX-THREADS:1OOO
CONSUMER-1OG:TRU
MOCK-ENABLE:FALSE
命名空间SEEYON-DE
ENABLE-NACOS:TRUE
ELASTICSEARCH:
CORE-THREADS:1OE
REGISTER:TRUE
P0RT:20880
TIMEOUT:5OO0
PPOIC十ON.十PLE
多高级选顶
DISABLE:TRUE
MONITOR:
ENABLE:TRUE
配置内容
DUBBO:
SEEYON
AUEUE:5OO
*GROUP
DATAID
PROVIDER:
PUBLIC
播述
2
39
5
59E1AS

## 3、给所有应用开起swagger接口

配置方式nacos的public下面添加

<img width="992.8">

## 4.PC端、M5桌面端、M5移动端默认的修改密码功能隐藏

在nasco配置里面添加passwordModify: false属性 ，重启portal服务就会生效

<img width="1536">

<img width="1152.8">

<img width="612">

## 5.关闭切换后台及超时锁屏的密码验证

在nacos的public配置文件中添加如下配置项，即可关闭切换后台时的密码验证：

如下图：

<img width="1330">

登录system-admin帐号，找到登录管理-登录及密码策略菜单，关闭“超时保护”选项，即可关闭长时间未操作时的密码验证。如下图：

<img width="983.3333333333334">
