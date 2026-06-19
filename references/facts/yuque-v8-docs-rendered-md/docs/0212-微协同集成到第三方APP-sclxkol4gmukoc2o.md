---
title: "微协同集成到第三方APP"
source: "https://www.yuque.com/seeyonkk/v8/sclxkol4gmukoc2o"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 微协同集成到第三方APP

> Source: https://www.yuque.com/seeyonkk/v8/sclxkol4gmukoc2o

## 1.应用场景

V8 应用运行在三方 APP 的时候，不可避免的需要调用三方 APP 提供的底层 API 来触发与三方 APP 里面功能

例如：第三方APP集成的微协同H5页面，协同或公文处理时一直转圈，无法关闭或返回上一个页面或者访问微协同页面时执行的返回操作，页面出现返回异常或混乱等操作，需要适配第三方APP的关闭webView; 比如适配分享链接、打开通讯录等等。因此 V8 平台统一封装了 @seeyon/js-sdk, 来抹平各个三方APP的调用方式差异(方法名称，入参，出参)，给上层业务一个统一的接口， 主要支持钉钉，M5，微信，企业微信，飞书等应用

本手册的扩展能力主要解决以下问题：

1
打通V8系统与三方APP的交互能力

2
提供三方APP定制化JSSDK能力

## 2.开发步骤

比如：适配返回方法

### 2.1 拉取前端扩展工程，开发环境搭建  参考 
开发准备

### 2.2 开发入口：extend-js-sdk

mobile.ts 是入口文件，用来加载jssk文件   
!注意:在PC浏览器调试时上方参数需直接设置为TRUE,不然浏览器不会使用自定义JSSDK的方法
RETURN/ANDROIDBLACKOERYJIENOBILEJPADLIPHONELIPODLOPERAMIRILVEBOSLPOBOILENINIPOGRAM/I.TEST(NAVIGETOR,USER4G
/如果没有线上地址N可以将JSSDK的JS拷贝至当前目录下的SD水K文件夹中,构建打包后DIST目录下的所有JS文件均需放到OSS.
//CONSTISTHIRDAPP=/LANXIN/I,TEST(WANDOW,NAVIGATOR.USERAGENT)&&SDKHELPER.IS/OBILE();
CONSOLE.LOG(已进入自定义API方法',ISTHIRDAPP);
/获取JSSD授权信息,如果不JSSDKAPI不需要投权则不加该参数,该位置为统一建权,如果需要调用时才建权可以在AP
复SDK法O.ASA.::...
CONSTISTHIRDAPP=SDKHELPER?.ISMOBI1E()ISNOBI1E();
{JSYCONFIGJSONTSAPITSUTSMOBILETSMXJSWEBPACKOVEDESJSM
MOBILETS-CUSTOM-FRONTEND-VISUALSTUDIOCOD
(WINDOWASANY).SYJSSDKCUSTOMFLAG
月7可而买7凹己前PTGE日肚一NTTT叫不I小A调天W月W正
//AWAITSDKHELPER,LOADSCRIPT('//G.ALICDN.COM/DINGDING/DINGTAL
//引入三方JS,如果有线上地址可以直接使用线上地址
CONSTGETCIIENTSDK=ASYNC
AWAITIMPORT('./UTI1S/ESN.MIN");
LAG=ISTHIRDAPP?GETCLIENTSDK:NUL
!检查是否成功挂载到WINDOW
ALERT(开始加载JSSDK");
//AWAITAUTH()
JSWEBPACK-OVERRIDESJSEXAMPLE
/CONSTISTHIRDAPP三TRUE
//如果不在三方APP中则不进行赋值
INDEX.TSXEXTEND-COMPONENTSNEW-..
TSY.CONFIGJSONEXTEND-COMPONENTSLNEW
BCATCH(ERROR}
CONSTISMOBILE=(E>
>JOWMEWERROR('YYESNBRIDGE加载失败)
>EXTEND-COMPONENTS
XTSMOBILE.TSEXTEND-JS-SDK
TSAPI.TSEXTEND-JS-SDKLIB
CUSTOM-FRONTEND
API:GETAPI(),
LCUSTOM-FRONTEND.Z
PACKAGE.JSON
EXTEND-IS-SDJK
EXTEND-HTML
RETURN
>NODE_MODULES
>EXTEND-CSS
OPENEDITORS
>EXTEND-ICONS
OREADMEMG
>EXTEND-FONTS
SGLOBALDLTS
>EXTENDJS
Y
GITIGNORE
VMRC
JIDEA
INDEX.TSXM
MNPMRC
TSMOBILE.TS
EXPLORER
包
OUTLINE
>UIS
EDITSELECTION
>EXAMPLE
TSPGTS
福
DIST
8
23
>心
SAIC
人
UNTERMINAL
8
说
美
品
21
X母INDEXTS
NN
片:.:日下的所有S文件均需放到9SS上
),..AR,,RIUUO可RU法采妆
13C
调用时才建权可以在API方法中去使用
14
M

项目中最好使用下面这种方式来判断是否在三方app中，app标识可以找三方对接的开发同事获取；

首先需要判断当前环境是否在三方APP中,判断条件可根据实际情况调整
CONST ISTHIRDAPP 三/APP标识/I.TEST(WINDOW.NAVIGATOR.USERAGENT)

因为如果M5加载了三方的jssdk进入M5就会报错：获取前端工程列表异常，请重新登录

<img src="https://cdn.nlark.com/yuque/0/2026/png/58875573/1777353933252-a518451d-3960-4e76-add9-202ec4993f32.png" width="722">

根据业务需求，覆写jssdk里面的对应的api方法，api.ts文件就是方法覆写文件

如图：覆写router.back和router.close方法，如果需要覆写关闭操作，最好back和close方法都覆写

<img width="1296">

auth.ts文件是鉴权文件，有的三方app调用关闭的时候需要鉴权，鉴权的一般步骤是：1.调用后端提供的鉴权接口，拿到鉴权参数；2.将参数设置到扩展的jssdk配置里面。例如：

<img width="1532">

## 3 已支持的 API 汇总

http://10.255.1.230:9082/-/web/detail/@seeyon/js-sdk 的 README.MD 中

// 设备类
'device.scan',
'device.getSystemInfo',
'device.getNetworkType',
'device.vibrate',
'device.setClipboard',
'device.getClipboard',
'device.sendMessage',
'device.call',
'device.savePhoneNumber',
'device.isM5',
// 媒体类
'media.takePicture',
'media.saveImage',
'media.chooseImage',
'media.previewImage',
'media.takeVideo',
'media.saveVideo',
'media.chooseVideo',
'media.startRecord',
'media.onRecordEnd',
'media.stopRecord',
'media.playAudio',
'media.pauseAudio',
'media.resumeAudio',
'media.stopAudio',
'media.onAudioPlayEnd',
'media.translateVoice',
// 地图
'map.getLocation',
'map.openLocation',
// 导航
'router.push',
'router.back',
'router.setNavLeftBtn',
'router.setNavRightBtns',
'router.setNavTitle',
'router.overrideBack',
'router.overrideClose',
'router.close',

JSSDK 生成后会挂在 window.jsSdk 变量上，部分暴露api如下

<img width="982">

备注：覆写获取wifi信息Api:window.jsSdk.device.getWifiInfo

当  @seeyon/js-sdk 的 API 不满足需求， 还支持对 @seeyon/js-sdk 进行扩展和覆写

JSSDK可复写方法汇总
腾讯文档-在线表格
https://docs.qq.com/sheet/DQ2xqb1ZqRGJOQmpq?no_promotion=1&tab=BB08J2

## 4.@seeyon/js-sdk 实现流程

<img width="1211">

1
JSSDK将在进入v8页面后首先被初始化

2
JSSDK 采用了分层结构的设计思路：一般app会有两侧

a
三方app sdk层：拿飞书举例，会定义关闭webview，打开相机，分享等，这些api的底层实现是飞书app特有的，也是每个三方app需要实现的。

b
默认H5层：这一层可以理解为H5原生层或者业务层，主要实现了一些普通H5的方法以及一些业务定制的方法

3
当业务代码调用了router.push 的时候，首先会看三方app层是否存在router.push方法，如果有，则调用三方app的router.push 进行页面跳转，否则查看H5层。如果都不存在，则会报错

## 5.demo

extend-js-sdk.zip
(5 KB)
