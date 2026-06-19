---
title: "前端依赖管理"
source: "https://www.yuque.com/seeyonkk/v8/kxm5mugeakq7i1uy"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 前端依赖管理

> Source: https://www.yuque.com/seeyonkk/v8/kxm5mugeakq7i1uy

为了保证系统整体的稳定性和安全性, UDC对于依赖管理有比较严格的限制，所有位于客户环境的前端客开工程在构建时都会受到沙箱环境限制（目前沙箱中只有node16），如网络环境，操作系统，资源配额等难以稳定安装NPM依赖，目前对于前端依赖的管理有平台内置以及三方引用两类：

## 1
由前端主应用自动加载，挂载在全局变量同其它应用共享，如React, Lodash, Redux

## 2
平台预置全局依赖

### 2.1
平台外部化依赖

平台内置三方依赖,  平台业务组件(标记为外部化的组件，没有被标记为外部化的seeyon组件无法引用)

这些依赖本质同全局依赖一样，可以供所有应用使用，只是加载和更新方式不太一样

## 3.UDC手写页面

在UDC手写页面中这两类依赖可直接被import使用

## 4.扩展工程

扩展工程中的扩展组件以及扩展插槽 可直接使用平台预置全局依赖；

平台外部化依赖需要在package.json中声明才可使用, 声明方式如下:

```
{
  "externals": {
    "@seeyon/biz-comment": "~5.5.0",
    "react-draggable": "4.4.4"
  }
}
```

对于扩展工程中的sdk以及普通js扩展代码，只能在window onLoad之后通过window[全局变量]使用平台预置全局依赖， 通过window.SeeyonGlobal.dynamicImport($组件名称)异步引用平台外部化依赖

如:

```
window.onLoad = () => {
  const SeeyonUI = window.SeeyonUI

  const useSeeyonPackage = async () => {
    const bizComment = await window.SeeyonGlobal.dynamicImport('@seeyon/biz-comment')
    // ...
  }

  useSeeyonPackage()
}
```

如需类型提示，请将依赖声明在"devDependencies"中

## 3.其它三方依赖

所有非上述两类的三方依赖都需要额外处理方能在客开工程中进行使用，主要有两类方法

1
通过引入三方包的iife或者umd格式的文件到static目录

以echarts为例，我们可以在下列cdn网站查找相关资源

https://www.jsdelivr.com/?query=echart， https://cdnjs.com/libraries/echarts，https://www.jsdelivr.com/package/npm/echarts

在下载之前我们需要检查其文件内容，确保可以在浏览器内正常加载

<img width="1920">

像这个文件我们可以明显看出它是iife的格式，并且将echarts整个模块挂载到了全局变量window.echarts上，故我们在加载了该js文件之后就可以通过window.echarts直接使用, 一般来讲官网也会有相应的介绍

<img width="1793">

将该文件下载后，放到static目录，再通过扩展html引用该资源

这样我们就可以直接在扩展工程以及手写代码中使用该依赖了（通过全局变量引用的方式）

该方式的局限性在于很多三方依赖需要参与打包才能正常工作，如echarts-wordcloud，该包依赖于echarts，它本身无法作为单独个体被引用，必须打包器告诉它如何找到echarts

2
通过生成tarball安装三方依赖

该方法原理是将三方依赖及其依赖打包成esm格式的包，通过npm pack生成一个tarball文件，然后在package json中引用该tarball就可以避免yarn在安装时从npm仓库获取该依赖

如项目需要该类依赖，可以向前端框架组申请获取该tarball，也可以自己去npm官方仓库下载，但前提需要保证该依赖的package json中没有其它任何依赖

在获取到tarball文件之后，需要将其先上传到对应环境公共桶的/custom-extensions/thirds/目录，然后在客开工程的package.json中添加该依赖（也可以直接放到static目录，通过先对路径引用）

这样我们就可以在扩展工程中import该依赖了

对于UDC手写页面，需要在扩展工程中将该依赖挂载到window上才能通过全局变量的方式使用

但是这种方法会让三方依赖即使未被代码引用也会加载，对于比较重的三方依赖这种方式会损坏平台整体性能，我们可以通过插槽的方式异步加载和使用三方包

```
// ECHARTS.lazy.ts
import echarts from 'echarts'

export default () => {
  return echarts
}

// customPage.tsx
import { extendSlots } from '@seeyon/global';

const echart = await extendSlots.load('ECHARTS')
```

## 内网安装Syf

通过yarn离线包的方式安装, 先下载离线包 <域名>/frontend-dependencies/udc-offline-pkgs/udc-code-engine-base-<平台版本>.zip (平台版本示例： 5.3, 5.0等)， 将该zip下载到工程源代码目录,  解压前先删除目录下的yarn.lock和package.json文件，解压后直接运行yarn install，在依赖安装完成后再恢复package.json即可

## 通过NPM方式安装三方依赖

如果网络条件允许，且该包的安装不依赖于高版本node可以采用该方式安装, 该方式只允许yarn1.22作为包管理器

### 客开工程

1
在客开工程的根目录下添加.npmrc文件，内容为npm仓库地址

1REGISTRYHTTPS:/REGISTRYNPMMLRRORCO
>EXTEND-COMPONENT
>LNODE_MODULES
CF[SSH:100.127.180.16]
EXAMPLE
EXTEND-JS
上年O
口NPMRCUX
PNPM-LOCKYAN
GLOBALD.TS
>CASTATIC
PACKAGEJSON
GITIGNORE
口.NPMRC
口NPMRC
.NVMRC
READMEMD

2
在package.json中的dependencies添加相应三方依赖，切记不要添加任何平台依赖！

3
本地构建测试

### UDC手写页面

1
在手写页面的pc/mobile下创建名为third-modules的目录，并增加.npmrc文件 配置npm源

2
在third-modules目录下安装相应三方包

3
在webpack-overrides-custom.js中配置alias，确保编译时webpack从third-modules目录寻找对应依赖

CONSTRENOVEURLDUPLICATESLASH=(URL)=URL.REPLACE(/([:]L/)V/+/G,$
CONSTORIGIN=REMOVEURLDUPLICATESLASH($IREQ,PROTOCOL}://$IREQ,HEADERS,HOST}$FRON]");
CONSTCUSTONPAGEMATCH=NEWREGEXP(/$APP_NAME}/CUSTON-PAGE-([',]+))
CONT2G.RESOLVE.AL1ASLECHARTSJEPATH.RESOLVE(DIRNANE,THIRD-NODULES/NODEN
CON%.TESOLVE,ALASLZRENDERJPATN.RESOLVE(_DIRNANE,THIRD-MODULES/NODEMODULES/ZRENDER)
CONSTUPSTREANRENOVEURLDUPLICATESLASH($HOSTNAME$FROM);
CONF2G,RESOLVE.,ALIASLTSLIB-PATH.TESOLVE(DIRNANE,THIRD-MODULES/NODENODULES/TSLIB);
CONTEXT:/MAIN/STATIC/VENDORS/COMMON/COMMON.VENDOR.1.0,11.JS'],
CONSTPORT=PROCESSENV.P0RT3000;
RETURN/MAIN/STATIC/VENDORS/COMMON/COMMON.VENDOR.1.0.11.DEV.JS
ONFIG.DEVSERVERPROXYPTOM-OAEE
CONSTAPPNAME=REQUIRE(./PACKAGE.JSON
MODULE,EXPORTS-(CONFIG,ENV)一
IF(ENV三DEVELOPMENTTCONFIG.DEVSERVER)
CONSOLE.LOG(${REQ.METHOD}LPROXY]);
SWEBPADCK-OVERRIDES-QUSTOMJS>O<UNKNOWN>>了EXPORTS
TARGET:HTTPS://TEST,SEEYONV8.COM,
CONSTHOSTNAMEHTTPS:/PRE.SEEYONV8.COM
CONFIGDEVSERVERPROXY.PUSH
CONFIGDEVSERVER.PROXY.PUSH(
1CONSTPATH=REQUIRE(PATH);
PATHREWRITE:FROM,REG=
CONFIGRESOLVE.ALIAS=};
IF(!CONFIGRESOLVEALIAS)
OPACKAGEJSON+README.MDONVMRC
PATHREWRITE:(FROMREQ)E
PC[SSH:100127180.16-A
WEBPACKOVERRIDES-CUSTOMJS
PC[SSH:100.127.180.16]
REACT开发版本
CHANGEORIGIN:TRUE
CHANGEORIGIN:TRUE,
CONTEXT:[!*/${APPNAM
接CUSTOMPAGETSX
>LNODE_MODULES
JSWEBPACKOVERRIDESCUSTOMJSX
王彬棋(2HOURSAGG)LN17COL95
自PACKAGEJSOR
LNODEMODULE
CTHIRD-MODULES
TARGET:HOSTNAME,
PRETIERCJS
SS出:100.12718016
STSCONFIGJSON
啤宝间
YAM.LOCK
NVMRC口NPMRC
PACKAGEJSON
GITIGNORE
TIGRAVITY-WEBPACK
ONVMRC
SECURE:FALSE
READMEMD
SXJSCOMMONJS
080A0州2
OPUSH
LGSRC
YANLOCK
LCDIST
EXPLORER
AGE.JSON.NAME
口NPMRC
>TIMELINE
O,1司]-ANTIGRAVIT
NALHELP
>OUTLINE
O
ES-CUSTOMJS
CONSTCUSTOMPAGEMAT

4
本地测试

以上配置的npm仓库地址请确保沙箱中能够正常访问

请务必上传yarn.lock文件

## 版本管理

所有的seeyon包都严格跟随平台的发布版本，但是平台发布版本号没有跟随 语义化版本 规则，

一般来讲对外发布版本的PATCH版本号对应seeyon包的MINOR版本，比如发布版本5.0.3对应seeyon包5.3.0

所有开发时所用版本必须严格跟随平台版本 不同版本之间会有兼容性问题
