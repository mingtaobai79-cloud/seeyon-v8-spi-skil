---
title: "web端和mobile端 通用搜索 biz-search"
source: "https://www.yuque.com/seeyonkk/v8/ddpdttec3glz6pa1"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# web端和mobile端 通用搜索 biz-search

> Source: https://www.yuque.com/seeyonkk/v8/ddpdttec3glz6pa1

通用搜索组件，支持简单搜索和组合复杂搜索。

## 1.简单搜索组件效果

10.1.141.32:3000/MAIN/PORTAL/KUOZHANUDCZUJIAN1880413857437925691/YEWUYEWUZUJIANYONGFA
A不安全
有新版CHROME可用
口 所有书签
品
分布式构建系统 口DEV-XTCVB文件夹
V8315版本之前的..  口V8标品构建地址
口业务空间栏目
口 V8环境
D V8
V8前端资料及研发
CMP
金山中台
前端-搁金
品
华
SEEYON V8
关闭全部
业务业务组件用法
颜华
标题
.
开英力,简单
杨颜华
请输入
标题:
开发
请输入
单位:
重五
查询
公文管理
积分管理

## 2.简单搜索组件用法

```
import React from 'react';
import Search from '@seeyon/biz-search';

export default function CustomPage() {
  const simpleList = […];
```

## 3.简单搜索组件的属性

| 属性 | 必须 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- | --- |
| simpleFieldList | 是 | SimpleField[] | 无 | 简单搜索字段列表 |
| defaultSelectedSimpleField | 否 | string | simpleFieldList[0].name | 默认选中的简单搜索字段 |
| placeholder | 否 | string | 请输入关键字搜索 | 无 |
| onSimpleSearch | 否 | (val: string, name: string) => void | 无 | 简单字段搜索回调, val: 关键字, name: 字段名 |
| combinedFieldList | 否 | CombinedField[] | 无 | 组合搜索字段列表 |
| onCombinedSearch | 否 | (data: Record<string, any>) => void | 无 | 组合搜索查询回调 |
| onReset | 否 | (data: Record<string, any>) => void; | 无 | 重置回调 |
| searchOnReset | 否 | boolean | false | 是否在重置时执行 |
| combinedSearchDefaultValues | 否 | object | undefined | 组合搜索默认值 |
| closePopoverOnSearch | 否 | boolean | true | 是否在搜索时关闭 popover |
| popoverZIndex | 否 | number | 999 | 无 |
| popoverProps | 否 | PopoverProps | 无 |  |
| placement | 否 | TooltipPlacement | bottomRight | 无 |
| isTrim | 否 | boolean | false | 字符串类型的搜索值是否 trim |
| hideSimleFieldSelector | 否 | boolean | false | 简单搜索只有一条时是否去掉下来框 |
| style | 否 | React.CSSProperties; | undefined | 自定义搜索组件容器 style |
| fieldSelectorStyle | 否 | React.CSSProperties; | undefined | 自定义切换字段下拉框 |

## 4.组合搜索组件效果

ANUDCZUJIAN1880413857437925691/YEWUYEWUZUJIANY
/MAIN/PORTAL/KUOZHANUDCZUJIAN18
:业务业务组件用法
[门DEV-XTCV8文件夹
系统DEPNN8文件夹VG前能资料及研发.V8315版本之前的.口V0防品构建地址口V8环境口CMP口金山中台业务空间拍
.168.1.4:3000/M
文档当管理
分布式构建系统
模板状态V请选
SEEYONV8
一V8心
请选择
点名称
程权限
模板状态
口所有书
前端-掘金
杨颜
EASYMO
邵合华
请选择
公文管理
不安全
请输入
标签
请输入
开发
工资条
完成更新
品

## 5.组合搜索组件用法

## 6.组合搜索组件的属性

| 属性 | 必须 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- | --- |
| showCombinedSearch | 否 | boolean | true | 是否显示组合查询按钮 |
| singleIgnoreFields | 否 | string[] | - | 单一查询不需要提取显示的字段，对应 Form.Item

 组件 name

 字段的值 |
| singleAutoChangeFields | 否 | string[] | - | 单一查询需要自动触发 onChange

 的字段，对应 Form.Item

 组件 name

 字段的值 |
| singleFieldSelectProps | 否 | SelectProps | { style: { width: 110 } } | 单一查询 field select props |
| singleValueProps | 否 | SingleValueProps | { style: { width: 220 }, allowClear: false } | 单一查询表单子组件 props 设置 |
| popoverProps | 否 | PopoverProps & { okText?: string; cancelText?: string } | { okText: 查询, cancelText: 重置 } | Popover

 组件 props 设置 |
| footerStyle | 否 | CSSProperties | - | - |
| onChange | 否 | (values: Record<string, any>, type: 'single' \| 'combined') => void | - | 点击提交按钮回调 |
| onReset | 否 | () => void \| false | - | 重置回调，返回 false

 时阻止自动关闭弹层 |
| children | 是 | (form: FormInstance, props: SingleFormChildProps) => ReactNode | - | children 只支持 render props 模式 |

备注：调整popover的宽度，可新增属性formWidth来设置

<img width="968">

<img width="471.2">
