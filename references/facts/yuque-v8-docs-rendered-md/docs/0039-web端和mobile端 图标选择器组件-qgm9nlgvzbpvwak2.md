---
title: "web端和mobile端 图标选择器组件"
source: "https://www.yuque.com/seeyonkk/v8/qgm9nlgvzbpvwak2"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# web端和mobile端 图标选择器组件

> Source: https://www.yuque.com/seeyonkk/v8/qgm9nlgvzbpvwak2

## 1.组件效果

10.141.32:32:3000/MAIN/PORTAL/KUOZHANUDCZUJIAN1880413857437925691/YEWUZUJIANYONGFA
@不安全
有新版CHROME可用
品
分布式构建系统
业务空间栏口
V8标品构建地址
前端-润金
所有书签
金山中台
V8环境
DEV-XTCV8文件夹
V8
V8前端资料及研发...
/8 315版本之前的....
EASY MOCK
品办
华
SEEYON V8
业务业务组件用法
关闭全部
颜华
选择图标
图标展示:
杨颜华
开发

A 不安全.10.1.141.32:32:300/MAIN/PORTAL/KUOZHANUDCZUJIAN1880413857437925691/YEWUJIANYONGFA
一门
有新版CHROME可用:
品口V8 前滨-揭金
口V8前端资料及研发
分布式构建系统
CMP
口DEV-XTCVB文件夹
V8 315版本之前的...
所有书签
口业务空间栏目
V8标品构建地址
V8环境
EASY MOCK
口金山中台
华
SEEYONV8
选择图标
关团全部
系统预五图标
颜华
请输入搜索关键字
全部分类
展开~
国
设置
提示
工具
用户
容器
韩选:
常用
方位
杨颜华
开发
面形图标
多色图标
COLOURAD...
CODEFILEB
COLOURN...
COLOURC1.....
COLOURPA...
COLOURM...
COLOURAD...
COLOURAD...
COLOURSU
工资
公告
代码文件
通讯录
会议
会议
添加
考勤
文档
告办
双色图标
公文管理
系统
0
积分管理
COLOURAP...
COLOURBA...
COLOURBILL
COLOURAP...
COLOURAP...
COLOURBA,..
COLOURBA...
COLOURBP...
COLOURBU...
COLOURBA...
数据
公文
工作台
后台管理
别人人
待办事项
任务管理
待办
流程中心
市批
待办
应用
品
目
十口
COLOUREX...
COLOURDA...
COLOURD...
COLOUREN...
COLOURED...
COLOURDA...
COLOURCU...
COLOUREX....
COLOURD...
COLOURCU...
方向
集团空间
农格
数据工厂
流程督办
自定义空间
预算管理
费用报销
货币
会议记录
基础资料
文档
开中小简盘
流程
COLOURLNI....
COLOURLM...
COLOURHT...
COLOURLNF...
COLOURGE...
COLOURFE...
COLOURGR...
分组标题
阳片
在线文档
发起流程
通用
已力
报表管理
文件夹
流程绩效
费用申请
版式布局
取消
确定

## 2.组件用法

```
import { Button } from '@seeyon/ui';
import { SyIcon } from '@seeyon/global'
import React, { useState } from 'react';
import { IconSelector } from '@seeyon/biz-icon-library';

function ComponentDemo() {
  const [visible, setVisible] = useState(false);
  const [iconName, setIconName] = useState('');

  const onOk = (name: string, svgContent: string) => {
    setIconName(name);
  };
  const onCancel = () => {
    setVisible(false);
  };
  const onSelect = () => {
    setVisible(true);
  };

  return (
    <>
      <Button onClick={onSelect}>选择图标</Button>
      <div>
        图标展示： <SyIcon name={iconName} className="demo-icon" />
      </div>
      <IconSelector visible={visible} onOk={onOk} onCancel={onCancel} />
    </>
  );
}
```

## 3.组件属性

| 参数 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| visible | 是否显示 | Bool | - |
| onCancel | 点击取消按钮回调 | () => void | - |
| onOk | 点击确定按钮回调 | (name: string, svgContent: string) => void | - |
