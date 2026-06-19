---
title: "web端和mobile端关联文档"
source: "https://www.yuque.com/seeyonkk/v8/tgmice5pknu030q5"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# web端和mobile端关联文档

> Source: https://www.yuque.com/seeyonkk/v8/tgmice5pknu030q5

## 组件效果

> C A 不安全.10.10.141323000/MAIN/PORTALLYEWUJLANUDCZUJLANI880F13657437925691/YEWUYEWUYEWUILANYONGTA
有新版CHROME可用;
冷84口I品
口 V8标品构建地址
分所有书签
口DEV-XTCV8文件夹
心前端-掏金
业务空间栏目
分布式构建系统
口 V8环境
V8前端资料及研发...
金山中台
V8315版本之前的...
EASY MOCK
CMP
品介绍
(华
SEEYON V8
四
业务业务组件用法
关闭全部
颜华
请选择
拼中小简验
杨颜华
开发
公文管理
10/\等旧

A 不安全 10.141 32:32:3000/MAIN/PORTAL/KUOZHANUDCZUJJAN1880413857437925691/YEWUYEWUJIANYONGFA
有新版CHROME可用:
品
分布式构建系统 口 DEV-XTCV8文件夹
夹口V8前端资料及研发...
口V8
口业务空间栏目
沙所有书签
口V8315版本之前的...
前端-据金
V8标品构建地址
金山中台
V8环境
EASY MOCK
CMP
&品介
SEEYON V8
关闭全部
X
关联数据
颜华
拼中力,简单
Q输入关键字搜索
标题
待助已发
Q
关注流程
我代理的
交接给我的(已力)
杨颜华
交接给我的(已发)
开发
事项中心
文档管理
发起时间
发起人
标题
2026-01-23 16:18
222222
钟传杰
公文管理
发文-测试办理成果012201
2026-01-2209:36
杨颜华
积分管理
23454343>20条/页
共841条
已选择(0)
全部清空
取消
确定

## 组件用法

```
import React, { useState } from 'react';
import { AssociateDocument } from '@seeyon/biz-associate-document';

 export default function CustomPage() {
  const [value, setValue] = useState([]);
   
  return(<>
    <div>
       <AssociateDocument
        appName={'ctp-affair'}
        value={value}
        onChange={setValue}
        appScope={['ctp-affair', 'app-doc']}
      />
    </div>
  </>) 
}
```

10.141.32:3000/MAIN/PORTAL/KUOZHANUDCZUJFAN1880413857437925691/YEWUYEWUZUJIANYONGFA
有新版CHROME可用
不安全
V8标品构建地址
业务空间栏目
口 所有书签
分布式构建系统
V8环境
前端-据金
V8
V8 315版本之前的...
DEV-XTCV8文件夹
V8前端资料及研发...
金山中台
EASY MOCK
CMP
Q品六
华
SEEYON V8
关闭全部
业务业务组件用法
颜华
打开关联文档
开中小简单
场颜华
开发
公文管理

A 不安全.10.1.141.323000/MAIN/PORTAL/KUOZHANUDCZUJIAN1880413857437925691/YEWUYEWUZUJIANYONGFA
有新版CHROME可用
品口V8前端金搁金搁分
分布式构建系统  DEV-XTCY8文件夹 口V88
口V8标品构建地址
 VB315版本之前的...
C 业务空间栏目
口金山中台
V8前端资料及研发
VB环境
EASY MOCK
所有书签
CMP
SEEYONV8
关联数据
X
颜华
开中小简单
Q输入关键字搜索
标题
待办已发
我代理的
请输入标题
交接给我的(已办)
关注流程
"
杨颜华
交接给我的(已发)
开发
事项中心
文档管理
发起时间
发起人
标题
2026-01-23 16:18
222222
钟传杰
公文管理
杨颜华
2026-01-2209:36
发文测试办理成果012201
积分管理
345.43>20条/页V
共841条
全部清空
已选择(0)
取消
确定

## 组件属性

### AssociateDocument 组件属性

| 参数 | 说明 | 类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- |
| appName | 应用服务名称 | string | - | 是 |
| value | 关联的数据 | ValueTypes[] | [] | 是 |
| onChange | 关联数据提交时的回调 | (ValueTypes[]) => void | - | 否 |
| appScope | 可配置的运行态应用列表 | AppScope[] | 当前应用、事项中心、文档管理 | 否 |
| customHandleApps | 手写应用的自定义集合(见下方“关联文档支持的手写应用”) | HandleApp[] | - | 否 |
| hostAppName | 宿主应用，无则不传即可 | string | - | 否 |
| authObjectId | 设置数据的详情页面 id，建议传当前页面的详情 id，无则不传 | string | 取 url 的 id | 否 |
| hasTemplate | 当前应用页面是否是表单流程(页面跳转时bpm鉴权使用) | boolean | false | 否 |
| maxLength | 可选择数据的最大值 | number | - | 否 |
| readonly | 是否只读 | boolean | false | 否 |
| arrangement | 数据展示方式，纵向/横向 | 'lengthways'/'crosswise' | 'lengthways' | 否 |
| nameDisplayComplete | 文档名称是否展示完整 | boolean | false | 否 |
| isShowTop | 是否展示【请选择】按钮和计数器 | boolean | true | 否 |
| isShowCounter | 是否展示计数器 | boolean | 'inner' | 否 |
| btnText | 【请选择】按钮的文案 | string | '请选择' | 否 |
| btnProps | 【请选择】按钮的 props，请见@seeyon/ui 的 Button 组件 | any | - | 否 |
| size | 组件的大小，包含字体、按钮大小 | 'large'/'middle'/'small' | 'middle' | 否 |
| isDependency | 是否走应用依赖的逻辑 | boolean | false | 否 |
| require | 提交数据的时候，是否必填 | boolean | false | 否 |
| requireTip | 提交数据的时候，如果为空并且 require 开启时的 message 提示文案 | string | '关联数据不能为空' | 否 |

### AssociateDocumentModal 组件属性

| 参数 | 说明 | 类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- |
| appName | 应用服务名称 | string | - | 是 |
| value | 关联的数据 | ValueTypes[] | [] | 是 |
| handleChangeField | 弹窗确定按钮回调 | (data: ValueTypes[]) => void | [] | 是 |
| closeModal | 弹窗取消按钮回调 | () => void | [] | 是 |
| appScope | 可配置的运行态应用列表 | AppScope[] | 当前应用、事项中心、文档管理 | 否 |
| customHandleApps | 手写应用的自定义集合(见下方“关联文档支持的手写应用”) | HandleApp[] | - | 否 |
| hostAppName | 宿主应用，无则不传即可 | string | - | 否 |
| authObjectId | 设置数据的详情页面 id，建议传当前页面的详情 id，无则不传 | string | 取 url 的 id | 否 |
| hasTemplate | 当前应用页面是否是表单流程(页面跳转时bpm鉴权使用) | boolean | false | 否 |
| maxLength | 可选择数据的最大值 | number | - | 否 |
| isDependency | 是否走应用依赖的逻辑 | boolean | false | 否 |
| require | 提交数据的时候，是否必填 | boolean | false | 否 |
| requireTip | 提交数据的时候，如果为空并且 require 开启时的 message 提示文案 | string | '关联数据不能为空' | 否 |

### ValueTypes 数据类型及描述

| 参数 | 说明 | 类型 | 必填 |
| --- | --- | --- | --- |
| id | 被关联数据的id | string | 是 |
| treeId | 左侧树被选择key(udc应用是实体FullName，普通应用是appName) | string | 是 |
| url | pc端跳转详情页面的url | string | 是 |
| mobileUrl | 移动端跳转详情页面的url | string | 是 |
| displayName | 被关联数据的文案回显 | string | 是 |
| pageTitle | 跳转详情页面的页签title | string | 否 |
| subTreeId | 应用内部子级树的treeId(文档中心、新闻应用等有) | string | 否 |
| icon | 图标 | string | 否 |
| iconColor | 图标颜色 | string | 否 |
| pcReferFullName | web端参照FullName(udc实体使用，用于获取pc端参照详情地址) | string | 否 |
| mobileReferFullName | 移动端端参照FullName(udc实体使用，用于获取移动端参照详情地址) | string | 否 |
| authObjectId | 来源数据id | string | 否 |
| authAppName | 来源应用appName | string | 否 |
| secretId | 密级id | string | 否 |
| secretValue | 密级值 | string | 否 |
| _source | 被关联数据本身 | ValueTypes | 否 |

### AppScope 属性

### 关联文档支持的手写应用
