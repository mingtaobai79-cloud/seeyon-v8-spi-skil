---
title: "自定义设计器组件"
source: "https://www.yuque.com/seeyonkk/v8/pz65zwbngxlat9kg"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 自定义设计器组件

> Source: https://www.yuque.com/seeyonkk/v8/pz65zwbngxlat9kg

适用版本：3.12以上版本

作者：杨颜华
最后更新：2025-04-08

## 1. 应用场景

标品的UDC页面设计器组件不满足客户场景 ，可以新增一个自定义的udc组件替换标准组件

## 2. 开发步骤

环境搭建详见：开发准备-前端代码开发

### 2.1 开发步骤

实现逻辑：参考标品组件的代码结构，新增一个udc自定义组件，编写组件的设计态和运行态业务逻辑，并提交到扩展工程的1.0分支进行构建验证

SCHEMAMODULE":"./SRC/SCHEMA/INDEX.TS"
DESIGNMODULE":"./SRC/COMPONENTS/DESIGN.T
JSWEBPACK-OVERTIDES-CUSTOMJSEXTEND-COMPONE
TYPE":KKDEMOCOMPONENTCA1E
RUNTIMEMODULE":"./SRC/INDEX.TSX"
SYCONFIGJSONCUSTOMFRONTEND-VISUALSTUDIO
XSY.CONFIGJSONEXTEND-COMPONENTSLDEMO-C..M
@KKDEMO-COMPONENT-CA1ENDAR1,
DESCRIPTION":"日历-日历测试"
CUSTOM-FRONTENI
ICON":"LINEDCALENDAR"
BIZCATEGORY":"CUSTOM,
JSWEBPACK-OVERRIDES-CUSTOMJS
TERMINA1TYPE":"PC,
SYCONFIGJSON
}SYCONFIGJSONMX
MXJSWEBPACK-OVERRIDES-CUSTOMJS
TSAPI.TSEXTEND-JS-SDKLLIB
GREADME.MD
VEXTEND-COMPONENTS
>EXTEND-FONTS
>NODEMODULE
"APPLICATION",
PACKAGENAME":@KKD
>EXTEND-JS-SDK
"日历测试",
VDEMO-CALENDAR
>EXTEND-ICONS
OPENEDITORS
>EXAMPLE
CONTROLS:
FILEEDITSELECTIO
GROUP":
"NAME"
>EXTEND-HTML
EXTEND-CSS
>EXTENDJS
ORUNTERMINAL
.GITIGNORE
EXPLORER
SRC
STATIC
TSAPI.TS
房
ALHELP
16
DLIST
15
TIONVIEWG
12
安
10
M
三
13
包
17
O
14
日A
UALSTUDIOCODE
11
9
8

备注：sy.config.json里面的属性说明具体参考该工程下README.md

### 2.2 提交代码并构建

### 2.3 扩展工程构建成功后对应的udc应用所需的组件 添加依赖

组件依赖

@SEEYONMBIZUDC-IFRAME
/DEV.SEEYONV8.COM/MAIN/CHILD-FRAME/UDC/APP-DESIGN/APP
测试自定义组件流程
GOLANG教程LT营凶GOLANG教程GO语言.
SEEYON/BIZ-UDCFRAME
@SEEYONBIZ-UDC-IFRAME
202504101103:31
SEEYONMBZ-QRCODE
@SEEYONBIZ-QRCODE
创建时间2025-04-1011:03:31
度.口商品搜索REACTLT营
025-04-1011:03:3
P-DESIGN/APP-BASIC-INFO/DEPENDENTCMP?APPL
025-04-1011:03:31
025-04-1011:03:31
02504-1011:03:3
测试自定义组件流程(1.0)
2025041011:03:3
@SEEYONMBIZ-REPOR
表单助手检查页
2025-04-1011:03:31
添加依赖批量删除依赖
页面调试BETA)试更多
WEB端移动端O测试式失败
@SEEYONBIZ-REPORT
计版本:V1.0
其他收藏
..0REACT学习视频-百度..
.OPYTHON教程-廖雪..
移动端
更新时间
组件依赖
依赖组件
团队设置
动端
@SEEYONMBIZ-CONTE
P?APPLD=46377337101305832
)Q点点此搜索
赖设置
应用主题
发布版本
应用依赖
FRAME
移动端
职业培训.0虎课网-原创PS视频.
移动端
页面视试
WEB端
后端组件
二维码
报表
中
二维码
WEB端
少箱测
WEB端
终端
总组代
报表
编辑
包名
正文

S视频.PYTHON教程-廖雪.腾讯课堂职业培LL.虎课网-原创PS视频.
O表单助手2检查页面调试(BETI)
@KKDEMO-COMPONEN-CALENDAR1
CHILD-FRAME/UDC/APP-DESIGN/APP-BASIC-INFO/DEPENDENTG
EB端移动端D测试失败
创建时间:2025-04-1011:03:31
KKLTGJCALENDAR
-百度..口商品搜索REACTLT营
日历-日历测试
试自定义组件流程
GOLANG教程T营色
频..REACT学习视频-百度..L
北量删除依赖
择依赖组件
2门其他收藏
日历测试
设计版本:V1.0
<1>10条/顶
ETA测试更多
EB端移动
组件衣
消定
沙少箱测试
依赖设置
页面测试
发布版本
应用依赖
包名
编辑
东
日历测试
WEB端
图标
用主题
自
二
队设置
Q点此搜索
试自定义组件流程
名称
X
取消

### 2.4 组件依赖添加成功后，可在控件左侧区域看到新增的UDC组件

<img width="1920">

### 2.5 运行态就可以看到拖到页面上的组件

<img width="1911">

### 2.6 本地环境代理调试

<img width="1380">

<img width="1528">

<img width="1512">

<img width="1536">

<img width="1535.2">

<img width="1524">

备注：调试前需要先新增的自定义设计器组件代码提交到扩展工程并进行构建成功，再代理调试。若是组件已经引入进去，运行态逻辑进行调整 需要修改package.json文件的version字段（发布版本号，用于运行态版本控制, 在发布该工程时需要调整该版本号）

<img width="1208">

扩展工程 每个目录存放什么功能 ，具体细看README.md

<img width="1508">

## 3.demo例子

extend-components.zip
(30 KB)

## 4.现有组件清单

https://docs.qq.com/sheet/DQ2RISEdBQ29UeFhE?tab=BB08J2
