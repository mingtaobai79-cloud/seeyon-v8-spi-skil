---
title: "M5集成第三方H5页面"
source: "https://www.yuque.com/seeyonkk/v8/klndd3gy9c0k9pci"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# M5集成第三方H5页面

> Source: https://www.yuque.com/seeyonkk/v8/klndd3gy9c0k9pci

## 1.应用场景

第三方H5页面想要调用M5 APP内的原生插件能力，比如位置信息、拍照定位、录音、附件预览、获取当前登录用户信息等等

## 2.实现方式

需要第三方页面，需要引入https://apaas.seeyonv8.com/m5-cloud/static/h5-js-sdk-2.6.24.js 文件，才能调用到M5 APP内的原生功能

比如获取位置的基本信息：

LPTEST-FZYHL13.PROJECTV59.0SP1SEEY
PPSLSEEYONLAPPLAA.HTML
YHL3.PROJECTV59.0SP1
APACHEJETSPEEDWEBAPPSSEEYONAPPAA.HTML
气国VHS
非
-CAESUTILIAVAX
XCVBJAVAXDVBHSJAVAXAAHLMLXEI
JAVAXCGAPPLCALIONYNLX
GUTIPWDENCODERJAVA
AXCMINIOJAVAXG
MINIOJAVAXECHANNELCLASSX
TSRC="HTTPS://APAAS.SEEYONV8,CON/N5-CLOUD/STATIC/H5-JS-SDK-2.6.24,IS"></SCR
识库
DOCUMANT.GETELENENTBYID("DOM0BTN1").ONCLICK=FUNCTI
CONSOLE,LOG("定位基础信S只近间经韩克.....,STARTDN")
ENCODINGSXML
LETYDE三1"MODE":1;111单次定位2
CONSOLE.LOG("WINDOW",WINDOW)
执行WINDOWNATIVESDK.MAP.LOCATION方法就可以获
JARREPOSITORIESXN
CONSOLE.LOG(WINDOWNATIVESDK",WINDOWNATIVESDK)
AMISCXML
CONSOLE,LOG("WINDOW.NATIVESDK.NAP",WINDOWVESDK.NAP)
取经纬度
AMODULESXML
定做仅经韩吃)
UIDESIGNERXML
ARGETLTWINDOWNATIVESDLKMAP,TOCATION(TYPE,DATA)=>
AWORKSPACEXM
CONSOE.LOG("DATA>SS>,DATA)
SRC
LETLATITUDE=DATA.LATITUDE//H/G
MAIN
LETLONGITUDE=DATA.LONGITUDE//经度
引入获取原生插件S
LETID=DATA.ID
1/美用定位
CAIMUV8
LETSTOPPARAM={"ID":ID
ERDM
VARSTOPWINDOW,NATIVESDK.NAP.STOPLOCATION(STOPPARAN)
查看
CMINIO
CONSOLE.LOG("关闭定位......",STOP)
ESFIPFILELRANSFER
试多
CSFIPFILEUPLOADER
},(ERROR
CTEST
CONSOLE,LOG("定位找岩......ERROR",ERROR)
第三方
CISDATA
CV8
CVBHS
CUMENT.GETELEMENTBYID("DON0BTN2")ONCLCKFUNCTION
BCONTRONLLER
CONSOLE.LOG("定位详组信空信息.....,STARTXX0W")
CTSETCONTEOLLE
LETTYPE={"MODE":1};//1单次定位2连续定位
BGROORY
/定位(详细信息)
发送话求GROOY
VARGETLTINFOEWINDOW.NATIVESDK,NAP.LOCATONINFO(TYPE,(DATAJE>
CHTTPPOSTRAW
CONSOLE.LOG("DATA>>>>,DATA)
电装动20250621.GRO
//定位信息
6
LETLATITUDEDATA.LATITUDE//度
CBASE64UTIL
LETLONGITUDEDATA.LONGITUDE//经度
CIRENSHI
LETID三DAT.ID
CYONYOUBIP
B5
/关用定位
CAESUTILJAVA
LETSTOPPARAMEF"ID":ID
CUTILBASE64
VAPSTOPWINDOW.NATIVESDK.NAP.STOPLOCATION(STOPPARAM)
动UTILPWDENCODE
CONSOLE.LOG("关闭定位......",STOP)
启天康制药
CEXCELMAPWRITER
CRS
GTESTAPPLICATION
WHTML>BODYBUTTON#DOMOBTNL
ANOOPOHLEMSOSONATLINTGPROFLERTERMINALBUITDDEPE

## 3.目前已支持的 API 汇总

nativeSdk 生成后会挂在 window.nativeSdk 变量上，部分暴露api如下

LOOKR:[GETOESTURESTATES:/,SETGESTURESTATES:/SETNDESTURELOCK:/,VERIFYESTUMRELOCK:/,SUPPORTTYPVES:/.
DEVICE:(ISM5:/,ISWIN:/,ISLINUX:/,ISMAC:/,ISLMBPC:J"J
SHOWCHOOSETOSTARTCHAT:(PARAMS,SUCCESS,ERROR/>("
(SHELIEVENT:F),DERICE:F),MEDIA:F),SCAN:F],CANUSE:.
元素LIGHTHOUSE控制台源代码/来源
HTTP:FREQUEST:/,CANCEL:/,DOMMLOAD:/UPLOAD:
,1OCATIONINFO:(PARAMS,SUCCESS,ERROR)三>("
)STOPLOCATION:(PARAMS,SUCCESS,ERROR)=)("]
SEARCH:(PARAMS,SUOCESSERROR)=)("]
CAPTURELOCATION:(PARAMS,SUCCESS,ERROR>("
LIDENTIFICATION:[GETSTATE:/,SETSTATE:/,ISSUPPORT:
SHOWCONVERSATIONLIST:(PARAMS,SUCCESS,ERROR)=)("]
GETGROUPCHAT:(PARAMS,SUCCESS,ERROR)三>{""]
JUMPTOMESSAGE:(PARAMS,SUOCESS,ERRORT""
SHOWGROUPCHATLIST:(PARAMS,STOCESS,ERRORI"!
)1OCATION:(PARAMS,SUCCESS,ERROR)三){""]
LANGUAGE:(GETLIST:SETLANGAGE:力...
ATTACHMENT:READATTACHMENT:
HOOSEFILE:(PARAMS,SUCCESS,ERROR
KEPICTURE:(PARAMS,SUOOESS,ERROR
NG:IOINMEETINGBYCONFID:
START:PARAMS,SUCCESS,ERROR)三){"]
STARTGROUN:(PARAMS,SUCCESS,ERROR)=>(")
定义级别,0无问题
[[PROTOTYPE]]:OBJECT
SAVEVIDEOTOGALLERY:(PARAMS
AUDIO:STARTRECORD:/STOP
SAVEIMAGETOGALLERY:
CHOOSEMEDIA:(PARAMS
)VIEFPICTURES:(PARAMS,S
)DATA:GET:FSET:F
>WINDOWNATIVESDK
拥中少,简:
新变化性能网络
SSUCCESS,ERROR
控制台A/助理
LLPROTOTYPEJJ:OBJECT
TATIC/H5JS-SDK-2.624JS
过滤
MSSUCCESS,ERROR)=)U
:(PARAMS,SUCCESS,E
SERROR)=)FUN.
VIDEO:[STARTRECORD:IPLAY
/SHOWCREATEMEETING:/SHOWTOINMEETING:]
无详细消息
EDIA:F),SCAN:F],CANLSE:,"]A
LLFROLOTYPEJUDJECT
S,ERROR)=)FURJ
公无警
OTOPV
(PARAMS,SUCCESS,
0无信息
搜索X问题
CANUSE:(STR)=>F"J
MEDIA:
VCHAT:
RROR)=)FOJ
UDIO:TPAUSEADIO:,"'J
SPLAYVIDEO:L
PLAYAUDIO:STOPAUDIO
F]

| API名称 | 接口名 | 入参 | 入参字段意义 | 返回值 | 返回值字段意义 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| 横竖屏切换 | device.setOrientation | {

orientation：'portrait-primary'

},

success,

error | orientation：方向，无默认值，字符串类型，"any"/"portrait"/"landscape"/"portrait-primary"/"portrait-secondary"/"landscape-primary""landscape-secondary"分别代表任意方向/竖屏/横屏/正向竖屏/反向竖屏/正向横批/反向横屏

success:成功回调，比如 function(){}

error:异常回调, 比如funcion(){} | 无 | 无 | window.nativeSdk.device.setOrientation({orientation: 'portrait-primary'},function(){},function(){}) |
| 生成二维码 | scan.encode | {

  data:""

},

success,

error | data:生成二维码字符串，字符串类型

success:成功回调：比如function(){}

error:异常回调：比如function(){} | callback | image:base64编码后的二维码图片数据（string类型） | window.nativeSdk.scan.encode({data:''},function(res){console.log(res.image)},function(){}) |
| 扫二维码 | scan.scan | {

nativeHandle：true

}，

success,

error | nativeHandle: 如果原生壳可以处理扫描结果，扫描结果交由原生壳处理，默认true，

success:成功回调：比如function(){}

error:异常回调：比如function(){} | callback | text ： 扫码结果

format: 结果的编码类型 | window.nativeSdk.scan.scan({scanType:0,nativeHandle:false},function(res){console.log(res.text,res.format)},function(){}) |
| 获取经纬度（定位(仅经纬度)） | map.location | {

mode:1

},

success,

error | mode 模式,'1'单次定位,'2'连续定位

success:成功回调：比如function(){}

error:异常回调：比如function(){} | callback | id:当前定位的id

latitude:纬度  longitude:经度 | window.nativeSdk.map.location({mode:1},function(res){ console.log(res.latitude,res.longitude,res.id)},function(){}) |
| 定位（详细信息） | map.locationInfo | {

mode:1

},

success,

error | mode 模式,'1'单次定位,'2'连续定位

success:成功回调：比如function(){}

error:异常回调：比如function(){} | callback | id:当前定位的id

latitude:纬度 longitude:经度lbsAddr:详细地址 lbsCountry：国家lbsProvince：省

 lbsCity：城市

lbsTown：镇 lbsStreet：街道

provider：定位信息提供源，gaode google | window.nativeSdk.map.locationInfo({mode:1},function(res){ console.log(res)},function(){}) |
| 获取当前登录用户信息 | user.getLoginUserInfo | 无 | 无 | 返回用户信息字符串 | {i18nextLng: 'zh-CN', isAdmin: 'false', login-device: 'mobile', memberId:'1234', name:'张三'...} | window.nativeSdk.user.getLoginUserInfo() |
| 获取当前登录环境的一些信息 | user.getLoginSystemConfig | 无 | 无 | 返回环境信息 | {/portal/config接口全量信息} | window.nativeSdk.user.getLoginSystemConfig() |
| 拍照定位 | map.captureLocation | {

 frontCamera:false,

 userName:"",

 location:"",

uploadPicUrl:"" ,

serverDateUrl:"",

},

success,

error | frontCamera :是否默认前置摄像头（boolean类型，默认为false）

 userName: 用户名，用于界面显示，默认当前用户 （String类型)

 location: 位置信息，如果有值将不再重新定位(String类型)

 uploadPicUrl: 生成的照片上传地址（String 类型）

 serverDateUrl :同步服务器日志信息接口，如果不传将使用手机本地时间（String类型）

success:成功回调：比如function(){}

error:异常回调：比如function(){} | callback | localSource:生成的照片的本地地址

createDate:照片的生成时间

filename:照片名 | window.nativeSdk.map.captureLocation({ frontCamera:false,userName:"",location:"",uploadPicUrl:"" ,serverDateUrl:""},function(res){},function(){}) |
| 附件查看 | attachment.readAttachment | {

      url:"", 

      filename:"", 

      headers:{

      lastModified:"",

      isSaveToLocal:true,

     wpsParams:{

       android:{

     androidWpsKey:"",         isReviseMode:false,

     isClearTrace:false,

isShowReviewingPaneRightDefault:false,

          isScreenshotForbid:false

          isReadOnly:false,

         userName:"",

        waterMark:""

     },

     ios:{ }

   }

}，

success,

error | url:String //文件路径，支持http或file协议

 filename:String //文件名

 headers:{} //请求头

 lastModified:String //文件最后修改日期，将用于判断是否需要下载

 isSaveToLocal:Boolean //是否保存记录到数据库，默认true

 wpsParams:{//使用wps打开的参数，如果不传将不使用wps打开

android:{//android端的参数

androidWpsKey://String //WPS 的key信息

 isReviseMode:Boolean //是否编辑模式，默认false

isClearTrace:Boolean //是否清除痕迹，默认false isShowReviewingPaneRightDefault:Boolean //是否显示编辑面板，默认false

 isScreenshotForbid:Boolean //是否可截屏，默认false

 isReadOnly:Boolean //是否强制只读，默认false

 userName:String //编辑用户的名字，不传默认取当前用户名

waterMark:String //水印文字,传了将使用水印

ios:{//ios端的参数}

success:成功回调：比如function(){}

error:异常回调：比如function(){} | 无 | 无 | window.nativeSdk.attachment.readAttachment({url:"",filename:""},function(){},function(){}) |
| 图片预览组件，支持图片/gif/视频 | media.viewPictures | {

   items:[ {

      path:"",

      originPath:"",

      filename:""

      }],

    showIndex:0,

    autoShowOrigin:false

}，

success,

error | path:string  //图片路径，支持file://,http://,https://协议，以及A9文件storageKey

originPath:  string  //原图路径，支持file://,http://,https://协议，以及A9文件storageKey

filename:string//文件名

showIndex:number //初始显示的图片位置，默认0

autoShowOrigin:boolean //有原图时自动展示原图，默认false

success:成功回调：比如function(){}

error:异常回调：比如function(){} | 无 | 无 | window.nativeSdk.media.viewPictures({ items: [{ path: "", filename: '查看原图' }],},function(){},function(){}); |
| 调用拍照,获取图片 | media.takePicture | {

crop:true

}，

success,

error | crop ：是否要对结果图片进行裁剪

success:成功回调：比如function(){}

error:异常回调：比如function(){} | callback | path:String

filename:String

size:numner

mimeType:string | window.nativeSdk.media.takePicture({crop: true,frontCamera:true},function(res){},function(){}) |
| 选择文件 | media.chooseFile | {

  maxSelectNum:1,

   maxSize:500

  },

success,

error | maxSelectNum: 最大选择张数，默认1 maxSize :每个文件最大大小限制，单位MB，默认无限制

success:成功回调：比如function(){}

error:异常回调：比如function(){} | callback | path:String

filename:String

size:numner

mimeType:string | window.nativeSdk.media.chooseFile({maxSelectNum:9},function(res){},function(){}) |
| 选择图片/视频 | media.chooseMedia | { 

  maxSelectNum:1,

   type :'image',

   maxSize:500,

   showCamera:true,

   crop:true

},

success,

error | maxSelectNum 最大选择张数，默认1

  type 可选择的文件类型，可选值：'image','video','both' 默认'image'

maxSize 每个文件最大大小限制，单位MB，默认无限制

 showCamera 是否显示拍照按钮，仅maxSelectNum为1时生效

crop 选择完后是否要对结果图片进行裁剪，crop为true时，将强制type为image，maxSelectNum为1

success:成功回调：比如function(){}

error:异常回调：比如function(){} | callback | path:String

filename:String

size:numner

mimeType:string | window.nativeSdk.media.chooseMedia({type:'both',maxSelectNum:9,showCamera:true,crop:true},function(res){},function(){}) |
| 打开web页面 | router.push | {

   url

    param 跳转携带的参数

    options:{ 

      openWebView:true，

      useNativeBanner:true，

      useNativeStatusBar:true，

      nativeStatusBarTextBlack:true，

      replaceTop:false,

      showOrientationButton:true

      pushInDetailPad:true,

     clearDetailPad:true,

     appInfo:{

        appId:“”，

        homePage:"应用首页",

        description:""

      }

  }

     pcOptions: {

        openType: 'inTab' \| 'inModal'

  }

},

success,

error | url  跳转路径

param 跳转携带的参数

options:移动端

openWebView  是否新开webview，默认true

useNativeBanner 是否使用原生导航栏，默认true

useNativeStatusBar 是否使用原生状态栏，默认true，如果为false，webview将在导航栏底下

nativeStatusBarTextBlack 原生状态栏文字是否为黑色，默认true（如果适配了暗黑模式，在暗黑模式下此项意义为是否为白色）replaceTop 是否替换调当前webview栈顶页面，默认false，优先级高于openWebView

showOrientationButton 是否强制显示标题栏右侧的横屏按钮

pushInDetailPad 在pad上时，是否显示在内容区

clearDetailPad 在pad上时，是否清空内容区

appInfo:{

           appId:'xxx',应用id

           homePage:'xxx',应用首页

           description,应用描述

   }

pcOptions:{}//PC端ss

 openType: 'inTab' \| 'inModal'

success:成功回调：比如function(){}

error:异常回调：比如function(){} | 无 | 无 | window.jsSdk.router.push({url:'http://www.baidu.com',options:{openWebView:true,pushInDetailPad:true}},function(){},function(){}) |
| 返回上一页 | router.pop | {

   backIndex :1,

   param:"",

    options:{

         clearDetailPad:true

   }

}，

success,

error | backIndex :需要关闭的页面层数，默认1

param :关闭跳转携带的参数         clearDetailPad: 在pad上时，是否清空内容区 | 无 | 无 | window.nativeSdk.router.pop({backIndex:1},function(){},function(){}) |
| 关闭当前页面 | router.close | 无 | 无 | 无 | 无 | window.nativeSdk.router.close() |
| 接管物理返回键 | overrideBack | {

  override:true

},

success,

error | override:Boolean类型，是否接管

success:成功回调：比如function(){}

error:异常回调：比如function(){} | 无 | 无 | window.nativeSdk.router.overrideBack({override:1},function(){},function(){}) |
| 标题栏设置接口，全部整合到一起 | titleBar.setTitleBar | {

   titleBar：{

     visible:true,

     dividerVisible:true,

     title:"",

     float:true,

     gravity:middle，

     textColor:""

     backgroundColor:""

   }

     statusBar:{

       visible:true,

       color:"",

       textBlack:"",

     }

    rightButtons:[{

        id:"",

       text:"测试",

       textColor:"#333",

      textSize："",

       imageUrl："" }]

       leftButtons:[{

          id: "",

          backgroundColor:"",

         activeBackgroundColor: "",

         backgroundImage: "",

        activeBackgroundImage: "",

         text: "",

         activeText: "",

         textColor: "",

         activeTextColor: "",

         textSize: 12

         activeTextSize: 12

      }]

      backVisible

     closeVisible

   } ,

success,

error | visible 是否显示原生标题栏

dividerVisible是否显示原生标题栏下部分割线

title:标题名称

float:bool  //标题栏透明且悬浮在页面上，float时背景色设置将不生效

gravity标题位置，仅支持left，middle，默认middle

textColor标题颜色，同时影响返回按钮等默认按钮的颜色

backgroundColor

visible:是否显示

color//状态栏颜色，如果不设置默认跟标题背景色相同

textBlack//状态栏文字是否是黑色，如果不设置将根据statusBarColor自动处理

id:按钮的id

text:按钮文字

textColor：按钮文字颜色

textSize：按钮文字大小

imageUrl：图片类型时的url地址

id: strig类型 按钮的id

backgroundColor: string类型， 默认态背景色

activeBackgroundColor: string类型， 激活态背景色

backgroundImage: string类型 默认态背景图

activeBackgroundImage: string类型 激活态背景图

text: string类型， 默认文字               activeText:string类型， 激活态文字

textColor:string类型， 默认文字颜色

activeTextColor: string类型， 激活态文字颜色

textSize: int类型， 默认态文字大小  activeTextSize: int类型 激活态文字大小

backVisible：boolean,返回是否可见

closeVisible：boolean ,关闭是否可见 | 无 | 无 |  |
| 下载附件 | http.download | {

    filename:"",

     url:"",

     headers:"",

     lastModified:"",

     isSaveToLocal:true,

    requestId:""

},

success,

error | filename:文件保存的名字

 url:文件下载路径

 headers:请求头信息，将与原生默认头合并

 lastModified:文件最后修改日期，将用于判断是否需要下载

 isSaveToLocal：是否保存记录到数据库，默认true

 requestId 下载请求id | callback | pos 下载进度

 target  下载文件本地路径

 requestId 下载请求id |  |
| 上传附件 | http.upload | {

 url:"",

 headers""

 fileList:[ {

    filepath:"",

     base64:"",

     requestId:""} ]

  },

success,

error | url:上传地址

headers:请求头信息，将与原生默认头合并

filepath:文件路径

base64:如果是base64编码的图片，将以base64为准

requestId:请求id | callback | pos 上传进度

response  上传结果

requestId 上传请求id |  |

## 4.具体实例

查看该示例页面：

demo.html
(6 KB)
