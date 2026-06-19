---
title: "web端和mobile打印组件"
source: "https://www.yuque.com/seeyonkk/v8/vvumvwudaoursmpe"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# web端和mobile打印组件

> Source: https://www.yuque.com/seeyonkk/v8/vvumvwudaoursmpe

快捷搜索组件，支持简单模式和展开模式

## 1.组件效果

A 不安全 1.141.323000/MAIN/PORTALKUOZHANUDAUJJAN1880413857437925691/YEWUJIANYEWUJIANYONGFA
有新版CHROME 可用
分
心前端-据金
品
LASY MOCK
打印
1张纸
Q品心
华
SEEYON V8
MICROSOFT PRINT TO PDF
目标打印机
关团全部
页面
全部
颜华
布局
纵向
杨颜华
开发
彩色
彩色
更多设置
公文管理
积分管理
研中小简盈
打印
取消

## 2.组件用法

打印全部

```
import React from 'react';
import ReactDOM from 'react-dom';
import PrintComponent from '@seeyon/biz-print';

export default () => {
  return (
    <div>
      <h1>打印组件Demo</h1>
      <main>
        <p>这是一个普通的页面</p>
      </main>
      <p>
        <PrintComponent>
          <button>打印整个页面</button>
        </PrintComponent>
      </p>
    </div>
  );
}
```

打印局部

```
import React, { useRef } from 'react';
import ReactDOM from 'react-dom';
import PrintComponent from '@seeyon/biz-print';

export default () => {
  const domRef = useRef();
  return (
    <div>
      <h1>打印组件Demo</h1>
      <main>
        <p>这是一个普通的页面</p>
        <div ref={domRef}>
          <p>这里是页面局部</p>
        </div>
      </main>
      <p>
        <PrintComponent domNode={domRef} waterMark={true}>
          <button>打印局部DOM</button>
        </PrintComponent>
      </p>
    </div>
  );
}
```

## 3.组件属性

| 参数 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| domNode | 打印节点的DOMRef，可选。未传入则打印整个窗口 | RefObject<any> | 无 |
