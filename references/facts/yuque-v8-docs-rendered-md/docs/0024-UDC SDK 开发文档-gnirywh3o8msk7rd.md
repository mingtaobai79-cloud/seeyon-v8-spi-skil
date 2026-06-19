---
title: "UDC SDK 开发文档"
source: "https://www.yuque.com/seeyonkk/v8/gnirywh3o8msk7rd"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# UDC SDK 开发文档

> Source: https://www.yuque.com/seeyonkk/v8/gnirywh3o8msk7rd

UDC SDK 是一个为扩展组件提供调用 runtime-core 能力的开放 SDK，使业务组件能够便捷地访问页面、组件、数据源等核心功能。

## 1.目录

●
概述

●
获取 SDK 实例

●
API 分类

○
应用相关 API

○
页面相关 API

○
组件相关 API

○
数据源相关 API

○
表达式与事件 API

○
订阅 Hooks

○
工具方法

## 2.概述

UDC SDK 提供了一套统一的接口，让业务组件能够：

●
获取应用和页面信息

●
读写组件值和视图状态

●
操作数据源（查询、保存、删除等）

●
执行表达式和事件动作

●
订阅组件状态变化

## 3.获取 SDK 实例

```
// 在组件中使用
const MyComponent: React.FC<{ runtimeContext: UdcRuntimeContext }> = ({
  udcSdk, // 组件代理层会自动注入
  runtimeContext,
}) => {

  // 使用 SDK 方法
  const pageInfo = udcSdk.getUdcPageInfo(runtimeContext);

  return <div>{pageInfo.pageName}</div>;
};
```

## 4.核心概念：UdcRuntimeContext

UdcRuntimeContext 是 UDC SDK 中最核心的参数，几乎所有 API 都需要它来定位当前的运行时上下文。它包含了组件在页面中的完整位置信息。

### 4.1 结构定义

```

interface UdcRuntimeContext {
  /** 应用名称 */
  appName: string;
  /** 页面名称 */
  pageName: string;
  /** 组件ID（可选，某些页面级API不需要） */
  componentId?: string;
  /** 上下文ID，用于区分同一页面的多个实例 */
  contextId: string;
  /** 容器类型 */
  container?: 'UDC_SINGLE_TAB_VIEW' // 单标签页
        | 'UDC_MULTIPLE_TAB_VIEW' // 多标签页
        | 'UDC_EMBED' // 嵌入
        | 'UDC_MODAL' // 弹窗
        | 'UDC_DRAWER' // 抽屉
        | 'UDC_SUBPAGE' // 子页面
        | 'UDC_FRAME' // 外框
        | 'NONE_UDC_VIEW'; // 未定义
  /** 祖先组件信息（用于嵌套组件场景，如子表中的组件） */
  ancestorInfos?: Array<{
    componentId: string;
    rowId: string;
  }>;
  /** 打开当前页面的父页面上下文（用于子页面/弹窗场景） */
  openerRuntimeContext?: UdcRuntimeContext;
}
```

### 4.2 使用场景

### 4.3 重要说明

●
组件代理层自动注入：扩展组件无需手动构造 runtimeContext，它会通过组件代理层自动注入到组件 props 中

●
上下文隔离：contextId 确保同一页面的多个实例（如多个弹窗）之间数据隔离

●
层级追溯：通过 ancestorInfos 和 openerRuntimeContext 可以追溯组件的完整层级关系

## 5.API 分类

### 5.1 应用相关 API

#### getUdcAppInfo

获取当前应用信息。

### 5.2 页面相关 API

#### getUdcPageInfo

获取当前页面信息

#### getUdcPageInParams

获取页面入参。返回值是一个对象，每个入参都包含完整的元信息。

#### getUdcPageVariables / setUdcPageVariables

获取/设置页面变量(设计器配置的页面变量，是一个状态)。

注意：getUdcPageVariables 直接返回变量的值，而不是包装对象。

#### getUdcPageRuntimeVariable / setUdcPageRuntimeVariable

获取/设置页面运行时变量(运行时，页面级全局变量，非状态)。运行时变量包含页面运行时的各种状态信息。

getUdcPageSignature

获取页面唯一签名。

### 5.3 组件相关 API

#### getUdcComponentValue / setUdcComponentValue

获取/设置组件值。支持多种模式定位组件。

返回值格式：[value, pairValue] 元组

●
value: 组件的实际值

●
pairValue: 配对值对象, 参考接收到的值格式，包含 displayName 等附加信息（用于参照、枚举等需要显示名称的组件）

#### getUdcComponentViewState / setUdcComponentViewState

获取/设置组件视图状态。

#### 数据源相关 API

#### getUdcDatasourceData / setUdcDatasourceData

获取/设置当前数据源数据。

#### getUdcDatasouceMetaInfo

获取数据源元信息。

#### validateUdcDataSource

校验数据源数据。

#### batchSetUdcComponentValidationMsg

批量设置组件验证消息（用于后端返回的结构化错误）。

### 6.表达式与事件 API

#### 6.1 execParseUdcExpression

执行表达式。

#### 6.2 callUdcPresetEventAction

调用预置事件动作。

### 7.订阅 Hooks

#### 7.1 useUdcComponentValue

订阅组件值变化。

### 8.工具方法

#### 8.1 getUdcProfile

获取 UDC 配置信息，更通用的一种方式。

#### 8.2 getUdcPageSecretId

获取表单密级 SecretId。
