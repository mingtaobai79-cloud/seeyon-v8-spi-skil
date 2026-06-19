---
title: "web端和mobile端 流程图组件"
source: "https://www.yuque.com/seeyonkk/v8/uu2f8kgtybtthbkg"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# web端和mobile端 流程图组件

> Source: https://www.yuque.com/seeyonkk/v8/uu2f8kgtybtthbkg

## 1
pc端

### 1.1
组件效果

FRAME/TPM8314206605968689847/CKLCTHYJQYM?TE
全175.178.251.177:8808/MAIN/CHILD-FR
875192056502928PROC
YM?TEMPLATELD=-8323
20937128F
OAUTHPAGE=TRUE
SSLDE-178
839911
不安全
@一十100%
-83236875192
&FROMOAU
发起人
开始
发起人

### 1.2
组件写法

```
import { ShowProcess } from '@seeyon/biz-bpm-run';
<ShowProcess
  containerId={containerId}
width={width}
height={height}
showLeftBar={false}
canEdit={false}
templateId={bpmCaseDto.flowChartField === 'processId' ? undefined : currentProcess.id}
processId={bpmCaseDto.flowChartField === 'processId' ? processData?.processId : undefined}
/>
```

### 1.3
组件的属性

| 属性 | 说明 | 类型 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- | --- | --- |
| caseId | 流程实例Id | string | 否 |  | 与processId相同 |
| processId | 运行时流程图id，对应caseId | string | 否， |  | processId和templateId必须至少有一个 |
| templateId | 设计态流程id,对应processId | string | 否 |  | 新建的时候不存在processId，需要templateId |
| businessTemplateId | 模板id | string | 否 |  |  |
| formId | 表单应用id,对应applicationId | string | 否 |  |  |
| applicationName | 表单应用名称 | string | 否 |  |  |
| appId | 所属服务id,例如:app-approval | string | 否 |  |  |
| width | 流程图初始化显示的宽度 | number | 是 |  | 如果with为0，则初始化为window.innerWidth |
| height | 流程图初始化显示的高度 | number | 是 |  | 如果height为0 ，则初始化高度为window.innerHeight - 150 |
| runPorcessScence | 运行时流程图模式 | RuningProcessScene | 否 | RuningProcessScene.SHOW |  |
| extendNodeMenuInfo | 扩展菜单(runPorcessScence="insertNode" 时有效),key节点id，value：菜单信息 | ExtendNodeMenuInfo | 否 |  |  |
| secondCanOperationNodeIds | 第二次可以点击的节点 | string[] | 否 |  |  |
| showLeftBar | 是否显示左侧的菜单 | boolean | 否 | true |  |
| showBottomBar | 是否显示底部bar（包含流程说明，放大缩小） | boolean | 否 | true |  |
| canEdit | 是否可以编辑流程图 | boolean | 否 |  |  |
| processJson | 流程图数据 | string | 否 |  | processJson存在时，直接流程数据渲染 |
| caseLogDtos | 日志信息 | CaseLog[] | 否 |  |  |
| currentNodeId | 当前正在处理的节点 | string |  |  |  |
| currentWorkItemId | 当前事项id | string | 否 |  | 用于runPorcessScence为RuningProcessScene.STEP_BACK时，获取可以回退的节点 |
| canOperationNodeIds | 可以操作的节点id | string[] | 否 |  |  |
| needLoad | 是否需要从数据库加载 | boolean | needLoad | true | 传false 不需要从数据库中加载，并且不会刷新页面 |
| templateType | 模板类型 | "FORM" \| "THIRD_FORM" | 否 |  |  |
| reloadTime | 重新加载的标志，如果数据改变。流程图会重新刷新 | string | 否 |  | 一般是一个当前时间戳字符串 |
| canDeleteNodeIds | 可以删除的节点 | string[] | 否 |  | 右上角可删除icon，点击执行deleteNodeCallBack |
| deleteNodeCallBack | 删除节点回调 | (deleteNodeId: string) => void; | 否 |  |  |
| nodeClick | 节点点击事件回调 | (nodeId: string, ext?: any, node?: any) => void; | 否 |  |  |
| openPropertyNodeId | 需要默认打开属性设置的节点id | string | 否 |  |  |
| errorData | 错误信息 | any | 否 |  |  |
| isSimulation | 是否为仿真 | boolean | 否 |  |  |
| extendAttr | 扩展信息 | ExtendAttr | 否 |  |  |
| applicationVersion | 流程图版本号 | string | 否 |  | 用于底部bar中流程版本展示 |
| closeProcess | 关闭流程弹框 | Function | 否 |  | 用于返回主流程关闭当前流程弹框以及跳转子流程当前流程弹框 |
| selectOptions | 可选择节点配置 | SelectOptions | 否 |  |  |
| containerId | 流程图容器id | string | 否 |  |  |
| stepBackNodeIds | 回退节点 | string[] | 否 |  |  |
| hideMainProcess | 是否隐藏查看主流按钮 | boolean | 否 | true |  |
| isTest | 是否为流程图测试 | boolean | 否 |  |  |
| flowChartInfo | 流程图测试数据 | any | 否 |  | isTest为true时必传，覆盖流程接口数据 |
| showAllNodes | 是否展示所有节点 | boolean | 否 |  |  |
| showUrge | 是否显示催办按钮 | boolean | 否 |  |  |
| modifyList | 修改节点列表 | object[] | 否 |  | 目前只是用了seeyonPolicyName属性，用于展示节点权限名称，

权限名称优先级： modify权限名称 >节点权限名称 |
| templateName | 模板名称 | string | 否 |  |  |

## 2
移动端

### 2.1
组件效果

<img width="320">

### 2.2
组件写法

### 2.3
组件的属性

与pc端基本相同，但是增加了几个移动端属性，在表格最后几行

## 3
其他信息

### 3.1
运行时流程图显示场景

### 3.2
扩展菜单信息（ExtendNodeMenuInfo）

| 属性 | 说明 | 类型 | 是否必填 |
| --- | --- | --- | --- |
| menuKey | 菜单key | string | 是 |
| menuName | menu名称 | string \| Function | 是 |
| menuClick | 点击事件 | Function | 是 |

### 3.3
扩展信息extendAttr

| 属性 | 说明 | 类型 | 是否必填 |
| --- | --- | --- | --- |
| counterSignList | 节点加签数据信息（用于hover展示处理人） | any[] | 否 |
| changeCounterSignList | 节点加签数据信息改变 | Function | 否 |
| isCreate | 是否是新建待发状态 | boolean | 否 |

### 3.4
可选择节点配置SelectOptions

| 属性 | 说明 | 类型 | 默认 | 是否必填 |
| --- | --- | --- | --- | --- |
| permissionNodes | 允许可点击选择的节点 | number[] |  | 否 |
| selectType | 节点选择类型 | 'radio' \| 'multiple' | radio | 否 |
| selectNodeIds | 选中的节点id数组，当selectType为multiple选中项保存到selectNodeIds中 | string[] |  | 否 |
| selectNodeId | 选中的节点id，当selectType为radio选中项保存到selectNodeId中 | string |  | 否 |
| permissionConfigIds | 人工节点中可点击节点：如规则节点、路径表节点 | string[] |  | 否 |
