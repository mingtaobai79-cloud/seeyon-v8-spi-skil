---
title: "平台页面js/css/jssdk扩展"
source: "https://www.yuque.com/seeyonkk/v8/fch83t5fwntnm4zy"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 平台页面js/css/jssdk扩展

> Source: https://www.yuque.com/seeyonkk/v8/fch83t5fwntnm4zy

适用版本：3.12及以上版本

作者：杨颜华
最后更新：2025-04-08

## 1. 应用场景

标品样式/逻辑不满足某些需求，需要覆写/覆盖标品的样式或逻辑 ，可以通过扩展js/css/jssdk方式来实现。如替换默认图标, 更改表单分页位置，隐藏部门负责人和分管领导等采用js/css方式覆盖，适配第三方app的返回，关闭webView、分享链接、打开通讯录等等

### 1.1 扩展js

从3.8版本升级到3.12版本，通讯录页面多了部门负责人和分管领导字段，标品设计不可配置，但项目时不需要显示这些字段，只能通过扩展js方式隐藏该字段；

经营分析,税务管理
分管领导:陈琦
部门负责人:李梭
财务部
财务部
毛燕
职务
部门
毛燕
姓名
138
手礼

### 1.2 扩展css

标品中的待办事项里面的全选按钮的样式不满足客户想要的效果，需要把文字色和大小改大点，但是标品不支持可配置，则需要通过扩展css的方式来覆盖标品的样式

新产业共赢质量标杆
待事项(99+)已办事项()关注流程(99+)
CMI提交流程验证(USX12
CNI提交流程验证(XUSXL2..
汇聚强国建设力量技能让生活更美好
CMI提交流程验证(XUSX12.
NI提交流程验证(RUSX12.
测试三方快捷(管理员202.
CMI提交流程验证(XUSX12.
CMI提交流程验证(XUSXL12.
CMI提交流程验证(XUSX12.
测则试APPLICATIONNAR
CMI提交流程验证(XUSX12..
CMI提交流程验证(XUSX12.
.虎课网-原创PS视频.
提交流程验证(XUSX1
全选幼理
5/4/802:32下午
提交流程验证(XUSX12..
流程中心25/4/802
5/4/802:33下午
程中心25/4/1010:23上午
请输入关键字
丝乐
I提交流程验证(XUSX12.
GOLANG教程LT营GOLANG教程GO
5/4/802:33下4
提交流程验证(XUSX
25/4/802:33下
XUSX部门111
添加快捷
腾讯课堂职业培训L.
XUSX部门111
XUSX部门111
254202
54802:28下4
XUSX部门11
XU5X部门111
5/4/80233下
发起流程
流程中心
提交流程验证(XUSX1
流程中心
202...管理员流程中
4802
I提交流程验证(XUSX12...
交流福验证(XUSX12
25/4/80233下
REACT学习
XUSX部门111
4802
流程中心
管理员
54/802
4802:3
用中心
的文栏
的收藏
USX部门111
WSX0910
流程中心
指定URL
XUSX1
流程中心
通讯
午致远互联
514/802
流程中心
USX1
USX部门111
其他收藏夫
XUSX部门11
流程中心
XUSX1
页VQ
品
首页
日
USX1
2...XUSX1济
XUSX1
品搜索REACTLT营
XUSX1
我的收藏
EPPYTH
XUSX1

### 1.3 扩展jssdk

V8推送待办到三方APP后，在第三方APP打开V8待办处理后无法自动关闭页面，需要适配层适配关闭webView逻辑。这样在第三方APP 审批后自动关闭当前页或者跳转到V8待办列表页。

### 1.4 扩展图标

当客户想在设计器中使用其它图标时可以使用该扩展能力。

比如用户想替换分组图标，可以在选择图标时，使用自定义图标中的图标

<img width="1862">

<img width="1156">

图标库只支持字体图标，字体图标的制作可以参考如下方式: 如何制作字体图标

### 1.5 扩展字体

用户可以覆写平台全局的字体

<img width="1914">

或者搭建应用的某一部分的字体

<img width="1359">

## 2. 开发步骤

环境搭建详见：开发准备-前端代码开发

### 2.1 扩展js

实现逻辑：

<img width="1645">

实现效果：

<img width="1920">

### 2.2 扩展css

<img width="1440">

<img width="1916">

### 2.3 扩展jssdk

实现逻辑：覆写router.back方法：

<img width="1834">

视频讲解如下：

WeChat_20250410163708.mp4
(3 MB)

### 2.4 依赖管理

所有的扩展项目都使用一个package.json来管理

依赖主要分为3类：

1
全局依赖(https://docs.qq.com/sheet/DQ2RISEdBQ29UeFhE?tab=et7652)

在扩展js/jssdk中可以直接通过window[全局变量]使用，但是需要确保使用时机在windows.onload之后

2.  @seeyon组件(https://docs.qq.com/sheet/DQ2RISEdBQ29UeFhE?tab=BB08J2)

在列表里面的外部化组件可以通过window.SeeyonGlobal.dynamicImport(组件名称)引用

3. 三方依赖

平台预置三方组件（https://docs.qq.com/sheet/DQ2RISEdBQ29UeFhE?tab=re0r1f）也可以通过window.SeeyonGlobal.dynamicImport引用

如果需要使用的三方组件不在全局依赖和预置组件里面 需要确保当前客户环境的服务器可以访问公网，确保在构建时可以正常从http://39.107.192.235:9082/安装依赖

如果客户环境无法访问外网，可以将三方库的iife或者umd格式的文件下载下来放到static文件夹下 然后在extend-html/pc.html 中单独引入，然后通过全局变量使用。如：

<script src="/custom-extensions/static/jquery.min.js" />

### 2.5 如何在内网环境引用@seeyon组件

当沙箱无法访问公网npm仓库时，可以使用外部化组件，动态引用线上的组件资源而不依赖node_modules.

可以引用的外部化组件请查看该列表（https://docs.qq.com/sheet/DQ2RISEdBQ29UeFhE?tab=BB08J2）（其中被标记为外部化组件的才能使用dynamicImport）

另外全局依赖中的组件可以直接通过window[全局变量]使用

这两种方法所引用的组件都无需在dependencies中声明，但需要在package.json中定义一个externals字段，格式同dependencies一样！ 另外 可以在本地安装devDependecines获取类型

### 注： 如以上办法都无法生效，可以将本地build好的扩展工程产物./dist上传到对应环境的公共桶中，注意需要保留custom-extensions路径， 不要直接将文件夹中的内容上传到根目录!!

## 3. 备注

1.custom-frontend 工程每个目录存放什么类型文件及目录说明，参考当前根目录下README.md

2
3.18以下版本 扩展js/css/jssdk/业务组件的步骤 具体可参考如下地址

https://www.yuque.com/u221766/qb4gf1/yo64od7gkienbgad?singleDoc#

https://www.yuque.com/u221766/qb4gf1/dgqr2xy97aegixix?singleDoc

https://www.yuque.com/u221766/qb4gf1/vh4uzptw7z7ln2dy

3.jssdk可以扩展哪些api，具体参考如下地址

## 4. 遗留客开脚本迁移

a. Nacos注入脚本迁移：

将Nacos中的html代码片段直接复制到客开工程的extend-html目录下的pc.html/mobile.html中

后续的代码维护需要使用目前提供的扩展能力，如之前是通过该nacos代码片段注入一个css文件，那么可以直接将css源码放到extend-css下的pc.less/mobile.less中, 不用再单独写html代码插入

b. 主应用html注入：

将之前运维手动注入的html片段直接复制到客开工程的extend-html目录下的pc.html/mobile.html中

## 5.demo例子

extend-js.zip
(1 KB)

extend-css.zip
(0 KB)

extend-js-sdk.zip
(5 KB)

extend-icons.zip
(27 KB)
