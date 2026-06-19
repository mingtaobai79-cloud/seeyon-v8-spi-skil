---
title: "自定义页面/组件 常见场景示例"
source: "https://www.yuque.com/seeyonkk/v8/kys62t64hfc1fnpm"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 自定义页面/组件 常见场景示例

> Source: https://www.yuque.com/seeyonkk/v8/kys62t64hfc1fnpm

## 1
ajax公共请求方法

## 2
udcSdk

props.udcSdk  暴露了 99% 的可设置页面状态， 获取页面数据的方法， 基本能通过单词就能猜出意思， 具体如何使用请参考文档

自定义页面就是给开发完全自定义的， 涉及到获取数据，设置状态的方法支持使用udcSDK

但操作实体数据，这块由于数据安全和稳定问题， 并且为了避免大家滥用 udcSDK....  因此udcSDK不对外提供方法操作实体的方法

## 3
如何修改实体数据

建议后端自定义接口，前端调用接口进行修改

## 4
支持在自定义页面中使用的控件

1
基础 UI 控件:

a
@seeyon/ui

b
@seeyon/mui

2
筛选控件  @seeyon/biz-quick-search

3
附件控件:

4
..... 其他前端业务组件

## 5
消息提示

与Antd Design  的  Message  组件使用方式一致

## 6
自定义 ES6 Module 组件

与 自定义页面/代码 的逻辑一致:

📌 自定义页面/栏目 只能在 pages/xxx 目录下 加 自定义代码，避免与自动生成的代码产生冲突(导致自定义代码被冲掉

可以新建 pages/xxx/components 目录 ,在这个目录下 封装公用的 ES6 Module 的前端源码, 然后通过代码路径互相引用

### 6.1
示例

创建组件： 创建一个 pages/xxx/components/MyButton/index.tsx 文件

使用组件: 然后在其他目录 引用组件

## 7
添加自定义页面的国际化配置

1
将应用源代码从远程 GIT 仓库克隆下来后

2
进入自定义页面目录 src/ pages/自定义页面/i18n(如果没有此目录，需手动创建 目录及其下面的文件)

a
zh_CN.json(中文简体国际化配置文件)

📌 

自定义国际化只需要录入 词条及其中文即可，其他语种在应用发布成功后到 国际化词条管理中心 找到对应词条进行录入

前端应用国际化方案

## 8
主页面传递数据给自定义子页面

### 8.1
自定义子页面中配置页面入参

<img width="1456">

### 8.2
主页面中绑定"自定义子页面", 然后配置参数映射

<img width="1584">

### 8.3
自定义子页面中就可以通过代码获取到对应的数据

## 9
自定义子页面传递数据给主页面

这要根据具体业务场景才能判断， 下面举一个简单的例子

比如

1
主页面 页面变量 A 作为 输入框 A 的值

2
监听自定义子页面中按钮 B  的点击事件

3
触发后设置主页面的 页面变量 A 改变

<img width="960">

## 10
多种方式打开新页面

### 10.1
seeyon/global 公共工具

### 10.2
弹窗方式打开页面

### 10.3
通过新开 TAB 页签打开页面， 并传递 URL 参数

打开新页面后的效果如下

<img width="1167">

### 10.4
关闭页面

### 10.5
完整 demo

## 11
接入原生 html(第三方代码)（目前已废弃）

遇到接入第三方源码库, 如原生 JS,JQuery 代码的场景, 我们怎么办呢？

在源码目录下 存在 src/direct-modules 目录

<img width="513">

我们可以在此目录下创建/拷贝任意 原生代码或其他前端框编译好的代码

<img width="495">

此目录下的代码与 自定义代码一样:

1
可被自定义

2
修改好推送到代码仓库

3
重新发布应用

4
 direct-modules 目录下得代码就会被部署到线上

比如： 域名/appName/direct-modules/index.html 即可访问到具体的文件

### 11.1
接入原生JS库

假设有一个原生JavaScript库文件myNativeLibrary.js，它包含一个名为myFunction的函数，你希望在React组件中使用它。

1
引入原生JavaScript库：在HTML文件中，使用<script>标签引入原生JavaScript库文件原生JavaScript库在加载时将一个全局对象window.myNativeLibrary暴露出来，以便在React组件中访问

2
创建React组件：创建一个React组件，并在其中调用原生JavaScript库的函数

3
使用ref引用DOM元素：使用useRef来创建一个ref对象，并将其分配给渲染的DOM元素，以便在之后引用。

4
在适当的时机调用原生JavaScript库方法：使用useEffect来确保在组件挂载后执行初始化操作。在useEffect中，检查原生库是否已加载，然后在DOM元素上调用库的方法。

5
渲染组件：最后，将React组件渲染到应用中。

### 11.2
接入 原生 html 页面

上面已经说过: 域名/appName/direct-modules/index.html 即可访问到具体的文件

那我们可以通过 在 React 中使用 iframe 的方式引用 index.html文件

在React中使用<iframe>引用index.html文件是相对简单的。以下是详细的步骤：

1
在React项目中创建一个组件：

在React项目中创建一个新的组件，用于承载<iframe>元素。

在src属性中，将/path-to-your-index.html替换为实际的index.html文件路径。

1
使用组件：

现在，可以在React应用程序的其他地方使用<IframeComponent />来嵌入<iframe>元素。

1
注意事项：

●
请确保在src属性中提供正确的index.html文件路径。

●
根据需要调整<iframe>的宽度和高度。

●
可以根据项目要求自定义其他属性，例如 frameBorder（边框）、scrolling（滚动）等。

●
如果您要在iframe中加载跨域内容，请确保目标网站允许在其他域中嵌入其内容，否则可能会受到同源策略的限制。

这样，您就可以在React中使用<iframe>嵌入index.html文件了。

### 11.3
更详细的DEMO

下面提供一个更详细的 demo, 提供的功能主要有:

●
通过 iframe 接入 html 文件

●
在 React 中请求数据, 然后使用 postMessage 发送给 iframe

●
在 React 中 接受 iframe 发来的消息, 并根据消息的不同类型进行逻辑处理

●
在 HTML 中处理数据, 并使用 postMessage 发送给 React

●
在 HTML 中接受 React 发来的消息, 并根据消息的不同类型进行逻辑处理

源代码:

iframe-demo.zip
(5 KB)

代码文件:

●
customPage.tsx

●
useIframeMessage.ts

●
service.ts

●
/${appName}/direct-modules/demo/index.html

#### 11.3.1
自定义页面-customPage.tsx

#### 11.3.2
自定义 iframe 收发消息react hooks-useIframeMessage.ts

#### 11.3.3
开发后端接口-service.ts

```
import { getAppName, getAppRequest } from "@utils/common";
import { getRequestByAppName } from "@seeyon/global";

// 页面树形查询
export async function getPageList() {
  const appName = getAppName();
  const { apolloQuery } = getRequestByAppName(appName);
  const data = await apolloQuery(
    `
    query ${appName}UdcRuntimeMetaDataSelectFunctionNodeTreeAppNameGet ($path: ${appName}UdcRuntimeMetaDataSelectFunctionNodeTreeAppNameGetInputPath) {
      ${appName}UdcRuntimeMetaDataSelectFunctionNodeTreeAppNameGet(path: $path) {
        data{
          content
        }
        status
        code
        message
      }
    }
    `,
    {
      path: {
        appName,
      },
    }
  );
  return data.content || [];
}
```

#### 11.3.4
index.html 中收发消息-/${appName}/direct-modules/demo/index.html

```

<script>
  window.parent.postMessage('Hello from iframe!', "*");
  // 通过按钮点击后向父页面发消息
  function callParentMethod() {
    window.parent.postMessage('callParentMethod', "*");
  }

  window.onload = function (event) {
    console.log(`onload:`, event);
  }

  window.addEventListener('message', (event) => {
    try {
      if (event.data) {
        switch (event.data.type) {
            // 从父页面接收到初始化数据 , 判断不同的消息， 处理不同的逻辑
          case "INIT_DATA":
            {
              console.log(`收到初始化数据:`, event);
            }
            break;
          case "GET_USER_INFO":
            {
              console.log(`收到用户信息:`, event);
            }
            break;

          default:
            break;
        }
      }
    } catch (error) {
      console.error("Error parsing message:", error);
    }
```

### 11.4
html 页面中 渲染 React 元素

类似下面的场景:

●
左侧菜单是 通过 iframe 渲染的 html

●
右侧内容区是通过低代码平台搭建的页面

如何通过自定义代码实现呢?

LX-23009手汽5AM
这个位置是致远搭建的模块列表
是说的外按钮
申报及任务资料整理上传背景及预研资料成果上传
当前0条,共0条<<
背景及预研资料
进度分组
品过程
成果上传
科研过程
成员
申报及任务资料
>30条/页
心OPPM
图总览
图文件
过程分组
经费管理
每沟通
采购管理
单项目管理
LX-230040
LX-230041
看板
整理上传
过程管理
资料类型
目成本
任务管理
单据编号
资料来源
白成果
没有记录
个人空间
处理环节
规划进度
进度
新建
孙悟空
关闭全部
状态
日期
提交
流程
未做
标题
未做
员

#### 11.4.1
customPage.tsx

```
import React, { useEffect, useRef, useState, useCallback, startTransition, Suspense } from 'react';
import ReactDOM from 'react-dom';

import { RemoteComponent } from '@seeyon/biz-remote-component';

import { useSendMessageToIframe, useReceiveMessageToIframe } from './useIframeMessage';

function IframeComponent() {
  const iframeRef = useRef(null);

  const ComponentA = (props: Record) => {
    return (

    );
  };

  const getExtraDom = () => {
    const styleTags = document.querySelectorAll('style');
    const linkTags = document.querySelectorAll('link[rel="stylesheet"]');

    const clonedTags: any = [];

    styleTags.forEach((tag) => {
      clonedTags.push(tag.cloneNode(true));
    });

    linkTags.forEach((tag) => {
      clonedTags.push(tag.cloneNode(true));
    });
    return {
      head: clonedTags,
    };
  };

  // 向 iframe 中插入 react 元素
  const appendReactDOMToIframe = (obj: Record) => {
```

#### 11.4.2
index.html

```

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport"
      content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Test</title>
    <script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <style>
      /*兼容浏览器*/
      * {
        margin: 0;
        padding: 0;
      }

      .content {
        width: 100%;
        height: 100%;
      }

      .content-left {
        width: 19%;
        height: 600px;
        background-color: #1c232f;
        float: left;
      }

      .content-right {
        width: 81%;
        height: 600px;
        background-color: #6495ED;
        float: left;
      }
```

#### 11.4.3
useIframeMessage.ts

参考前文- 自定义 iframe 收发消息react hooks-useIframeMessage.ts
