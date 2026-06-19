---
title: "扩展插槽"
source: "https://www.yuque.com/seeyonkk/v8/zngrgup351qls4gv"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 扩展插槽

> Source: https://www.yuque.com/seeyonkk/v8/zngrgup351qls4gv

适用版本：5.3以上版本

作者：杨颜华
最后更新：2025-07-14

## 1、能力说明

扩展客户端定制化开发能力以及平台内部跨应用通信能力, 平台目前可通过插槽扩展的列表： https://docs.qq.com/sheet/DQ0ZDb0NPUVBpSnVw?tab=ssmi0n

## 2、应用场景

标品某些入口需要弹出react组件，或者覆盖标品某些显示的数量统计

### 2.1、 函数调用

当特定事件发生时（例如用户提交表单），可以触发自定义操作。

### 2.2、 React 组件渲染

这些是特定的函数调用，通常用于自定义UI的某部分（例如列表）。

## 3.协议规范

### 3.1 约定

插槽的定义主要由两部分组成，名称以及函数签名。调用方需要先提供插槽的定义，实现方必须严格遵循对应插槽的签名规范来编写代码。

插槽定义示例：

| 名称 | 输入参数 | 输出类型 |
| --- | --- | --- |
| UDC_LIST_TODO_FC | props: {id:string} | JSX.Element |
| BPM_BEFORE_SUBMIT | {formData: {name: string; age: string}} | Promise<Boolean> |

注意：插槽只能由大写字母和下划线命名, 请以业务模块名称开头, 如果该插槽为React组件请以FC结尾

### 3.2 调用方规范

调用方必须遵循以下要求：

1
调用前必须检查插槽是否存在, 如不存在需要有相应的平台逻辑

2
应主动捕获异常以保证平台稳定性

### 4.客开插槽定义

#### 4.1扩展代码配置

在扩展工程中新建extend-slots文件夹

#### 4.2 文件命名

插槽文件命名格式为：extend-slots/[SLOT_NAME].<lazy>.[ts|tsx]，必须是合法的ESModule模块并默认导出函数/组件

1
SLOT_NAME
采用大写下划线命名法，与插槽定义名称严格对应

2
lazy后缀
当需要分包加载时添加lazy标识, 从5.12开始会强制开启lazy模式，因为插槽在被调用时，所有其它的同步插槽也会被自动加载，此时如果使用了PC端组件的插槽在移动端被自动加载时就会造成SeeyonUI is not defined的错误

注意此模式下如果插槽跟插槽之间有公共模块，请不要使用模块变量来通信，因为在打包时公共模块默认会被分别打包到不同插槽代码里面。如下面代码将不会如预期工作:

对于上述代码如果调用方先调用SLOT_A再调用SLOT_B其输出依然为undefined，这是因为模块变量 singleton会在两个不同插槽中初始化， 其实则为两个不同变量, 但是通常来讲插槽跟插槽之间不应该有公共代码，因为它们一般代表不同业务场景。

如果确实需要该种能力，可以通过修改webpack配置，将其runtimeChunk更改为'single'，并且改为异步import加载的方式引用公共模块

#### 4.3 代码结构

当代码复杂度上升到一定程度时，将所有代码都编写到单个插槽文件会使项目维护难度上升， 我们可以通过文件夹的方式的来模块化插槽代码，提升代码的可读性。
在插槽的文件夹中，所有位于extend-slots第一层的文件会被视为插槽文件，其命名规范必须满足插槽名称的限制，如果我们想模块化插槽代码，可以通过在extend-slots下新建文件夹来将代码分组：

<img width="345">

#### 4.4 示例

UDC_TODO_LIST_FC.tsx

BPM_VALIDATION_FORM.lazy.ts

## 4.兼容性处理

请不要随意更改插槽入参出参类型，如果不确定实现方能同步修改，请新建插槽如UDC_EX_LIST_V_ONE_FC

TODO:  1. 类型校验, 2.列表校验（不在列表的插槽不允许定义？）

## 5.实际场景例子

以5.3版本，需求：系统登录后弹窗帆软报表

1.调用方 需要按照插槽规范命名文件，比如：PORTAL_OPEN_CUSTOM_MODAL_HOME_SLOT ;以上代码只做参考具体需求具体分析

<img width="1920">

2.接收方 接收定义插槽

<img width="1207">

<img width="1105">

实际效果截图：

<img width="1531.2">

6.实际场景代码

参考 ，具体业务按照项目上的需求场景来开发

extend-slots.zip
(3 KB)
