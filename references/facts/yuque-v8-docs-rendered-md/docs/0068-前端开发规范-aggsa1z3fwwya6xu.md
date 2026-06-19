---
title: "前端开发规范"
source: "https://www.yuque.com/seeyonkk/v8/aggsa1z3fwwya6xu"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 前端开发规范

> Source: https://www.yuque.com/seeyonkk/v8/aggsa1z3fwwya6xu

V8平台前端技术采用微前端架构和组件化开发模式，基于React技术栈开发，并采用前后端分离方案，实现前端工程独立开发、独立部署、独立扩展。

前端技术栈以react为主，采用react、redux、typescript、graphql、node.js 等技术

### 1
架构图：

REACT/APOLLOCLIENT/TYPESCRIPTLESS/SASS
ELECTRON/C++/OBJECTC/SWIFT/AVA/KOTLIN
A9移动客户端/微信/钉钉WELINK/...
JSBRIDGE桥接器/HYBRID混合框架
1111111111122222042720420100204202022021221211
移动设备IOS/ANDROID
IE11+/SAFARI/CHROME
WINDOWS/MAC/国产
APP性能基线
INNA-H-AOAOOOOONOCCOOCOR
前端组件
路由管理
开发工具
业务组件
基础组件
基础组件
原生技术
扩展组件
44--44000074477277000774014444422244-444
APP热修复
发文档
硬件API
安全防护
化系统
流量控制
发布规范
HYBRIDAPP
行为式验证码
原生组件/API
A组件
WEBAPP
微前端理念
用户鉴权
SPRINGBOOT
开发规范
设计规范
应用包管理
前端应用
性能检测
WEB组件
消息推送
XSS防护
WEB技术
安全加固
日志元录
研发支持
GRAPHQL
CSRF防
前端框架
平台安全
NODE服务
用户理点
PC电脑
部署发布
RESTAPL
应用沙少盒
/DEMO
开发支撑
GIT托管
刘览器
自动化测
前端服务
NPM
MOCK
工程理念
终端
工具
网关
脚手架
MDM
调试
移动
----
-----------------
开发
设计
式
----------二-----

支持多端适配的通用组件,
复用的组件和模块,可避
预置开箱即用的脚手架,
提升公司整体技术能力,退
统一的接口规范或者框架,
免重复性技术研究和频繁造
对业务代码进行有效的评估
免陷入一个人的能力决定-
节约人力成本
统一的U交互标准;
便于系统集成,应用之间
进行技术沉淀
采用同一开发架构后,方便
提升产品质量
保证开发出来的产品干人
减少网络原因导致的各种
代码复用性和可维护性高;
社区和相关扩展插件比较
互联网最流行的静态资源
将代码提交至私有化NPM
统一脚手架:私有化NPM
统一构建工具:WEBPACL
按需构建,减少前流量
统一技术栈:REACT
虚拟DOM性能好速度快;
有效管理和考核
问题,提升开发效率
服务器端的潼染,便于搜
预处理机制,支持多种语
好处:
具有统一,高复用,易调
各应用具备独立开发,构
制定标准化的技术规范
项目结构更加清晰,利于
统一前端组件
一切皆组件,更模块化,
面,利于质量提升
统一的
维护和问题排查
中,保证代码安全
不存在依赖关系;
子的局面
建和运行能力
素引擎优化
模块化打包器
轻应用
言的转换
台O
和考量
用等特点
个项目
西

统一WEBSOCKT通信
统一页签管理(WEB端
MAIN/APP
独立开发与运行
统一静态资源加载与管理
MAIN/APP1
MAIN/APP1
主应用
子应用
统一状态管理
APPN.
统一路由管理
访问
APP1
APP2
MAIN

备注：采用“主子应用”的技术构架，主应用main或main-mobile统一进行资源、数据、通信等管理，子应用只关心自身的业务

### 2
开发注意事项

1
代码中禁止显式使用 antd antd-mobile  , 只能使用 @seeyon/ui @seeyon/mui (使用方式与 antd 一致)

2
所有 NPM 包必须写固定版本号

3
NPM包黑名单（禁止使用的包）

4
无需显式安装的NPM 包

以下 NPM 包 已经使用 Webpack   external 挂载到全局

5
组件目录结构

6.    平台预置三方组件已包含可参考此链接（https://docs.qq.com/sheet/DQ2RISEdBQ29UeFhE?tab=re0r1f），也可以通过window.SeeyonGlobal.dynamicImport引用

### 3
前端UI组件库

地址：http://ui.seeyonv8.com/dev/pc

### 4
备注

"业务组件"是指在前端应用中，专门用于处理业务逻辑、展示业务数据和与业务相关的交互的组件。

这些组件通常是在应用程序中具有特定业务目的的可重用部分，有助于将代码进行模块化，提高可维护性和可复用性

在一个典型的前端应用中，可能会有许多业务组件，例如公文应用组件、流程图组件、流程意见框组件等
