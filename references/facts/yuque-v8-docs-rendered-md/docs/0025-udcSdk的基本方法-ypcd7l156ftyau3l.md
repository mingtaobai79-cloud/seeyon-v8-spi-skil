---
title: "udcSdk的基本方法"
source: "https://www.yuque.com/seeyonkk/v8/ypcd7l156ftyau3l"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# udcSdk的基本方法

> Source: https://www.yuque.com/seeyonkk/v8/ypcd7l156ftyau3l

## 1.应用场景

由于手写代码不能直接操作页面规则或者获取页面的一些变量等，因此udc提供一系列的sdk用于在手写代码中对页面规则进行操作

udcSdk：udc提供的sdk的字段，一般从props中可以获取

runtimeContext：udc的一些上下文，一般从props中获取

dataTarget: 文档页面的单一记录，一般用于获取文单的一些实体对象

## 2.暴露api

```
{
  // app
  getUdcAppInfo, // 获取应用信息

    // page
    getUdcPageInParams, // 获取页面入参
    getUdcPageInfo, // 获取页面信息
    getUdcPageRuntimeVariable, // 获取页面运行时参数
    getUdcPageSignature, // 获取页面签名
    getUdcPageVariables, // 获取页面变量
    setUdcPageRuntimeVariable, // 设置页面运行时参数
    setUdcPageVariables, // 设置页面变量

    // component
    getUdcComponentInfo, // 获取组件信息
    getUdcComponentSignature, // 获取组件签名
    getUdcComponentValue, // 获取组件值
    getUdcComponentViewState, // 获取组件视图状态
    setUdcComponentValue, // 设置组件值
    setUdcComponentViewState, // 设置组件状态
    getUdcParentComponentInfo, // 获取父级组件信息
    getUdcDataContainerComponentInfo, // 获取组件对应的数据容器信息
    getUdcSubComponentViewState, // 获取子组件视图状态
    getUdcRecordIdByUiModelString, // 获取组件对应的内部 recordId
    setUdcSubComponentViewState, // 设置子组件状态
    getComponentMetadata, // 获取组件对应的数据源信息
    /** @deprecated */
    useUdcComponentValue, // 订阅组件值变化
    /** @deprecated */
    useUdcComponentViewState, // 订阅组件视图变化

    // datasource
    getUdcDatasouceMetaInfo, // 获取实体的数据源信息
    queryUdcDatasourceDetail, // 查询数据详情
    queryUdcDatasourceList, // 查询数据列表
    queryUdcDatasourceListSummary, // 查询数据列表汇总信息
```

## 3.使用方法

#### 3.1 设置单一变量

```
// 设置单一变量
const resetUdcComponentValue = async (key: string, value: any) => {
  await udcSdk?.setUdcComponentValue(
    runtimeContext,
    [value],
    {
      parentId: formId,
      dataField: key,
    }
  );
}
```

#### 3.2 修改页面变量

```
udcSdk.setUdcPageVariables(runtimeContext, key, value);
```

#### 3.3 获取页面信息

这个可以用来获取文单的formId

formId可以获取到发文主体

```
const pageInfo = udcSdk?.getUdcPageInfo(runtimeContext)

const formId =
      udcSdk?.getUdcPageInfo(runtimeContext)?.masterEntityComponentId ||
      udcSdk?.getUdcPageInfo(runtimeContext.openerRuntimeContext)?.masterEntityId;
```

#### 3.4 获取发文主体

能获取发文的很多实体信息，包括密级，文单名称啥的

如果dataTarget能从props中拿到，则直接用就可以了

```
getDatasource = (dataTarget: string) =>
  udcSdk.getUdcDatasourceData({
    ...runtimeContext.openerRuntimeContext,
    componentId: dataTarget,
  });
```

如果dataTarget拿不到

```
const { formId } = udcSdk.getUdcPageInfo(runtimeContext.openerRuntimeContext);

//获取发文主体
data =
  udcSdk?.getUdcDatasourceData({
    ...runtimeContext.openerRuntimeContext,
    componentId: formId,
  })
```

#### 3.5 获取入参

获取设计态传入的参数

#### 3.6 获取节点权限？

用的比较少

#### 3.7 手页页面里面获取当前应用参数

实际验证截图

<img width="1488">

#### 3.8 获取某个控件的值

比如获取正文控件的值
