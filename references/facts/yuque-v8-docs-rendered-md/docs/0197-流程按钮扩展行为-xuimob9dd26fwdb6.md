---
title: "流程按钮扩展行为"
source: "https://www.yuque.com/seeyonkk/v8/xuimob9dd26fwdb6"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 流程按钮扩展行为

> Source: https://www.yuque.com/seeyonkk/v8/xuimob9dd26fwdb6

## 一、功能场景

1
客户期望自己全部由定义自己流程按钮功能，比如加签

2
在流程按钮提交前做一些前置交互，比如客户期望在点击按钮后弹出一个流程预测的弹框，在预测完后点击确定再触发流程的功能。

| 应用客户及业务组 | 需求场景 | 应用场景 |
| --- | --- | --- |
| 中建 | 平铺选人加签后需要在提交动作之前做校验 | 行为执行之前校验 |
| 中海 | 流程提交前进行流程预测 | 行为执行之前校验 |
| 内部公文组 | 流程提交之后需要跳转页面 | 行为执行之后校验 |

支持的功能场景：

●
支持流程行为之前、行为执行之后做一些第三方的客开能力。

●
支持完全客开bpm流程类按钮，完全劫持bpm操作按钮执行效果。

●
支持获取bpm流程的相关信息

●
目前仅支持3.16及以后的版本

支持版本：3.16.0及以上

## 二、应用场景

多个注册拦截行为可能会存在如下问题：

1
多个行为拦截的先后顺序问题。

2
行为拦截校验后的后续执行问题。

为了解决上述问题，所以实现了如下的客开技术方案

## 三、客开技术方案

支持的功能场景：支持流程行为之前、行为执行之后做一些第三方的客开能力。支持完全客开bpm流程类按钮，完全劫持bpm操作按钮执行效果。支持获取bpm流程的相关信息目前仅支持3.16及以后的版本整体大致实现客开的代码如下：

```
import { eventEmit } from '@seeyon/global';

type Dispatch = ({ type, payload }: {
  type: TField;
  payload: unknown;
}) => unknown

type BpmSdk = {
  countersignInfo: CountersignInfo;
  setFormExtraParam: (key: string, value: any) => void;
  syncSignInfo: (countersignParam: SyncSignParams) => void;
  getBpmState: (key?: string) => any;
  setBpmState: Dispatch;
}

interface EventParams {
  /** 需要自定义的流程行为 */
  actions: string[];
  /** 执行校验 **/
  func: (bpmAction: BpmAction, bpmSdk: BpmSdk ) => Promise<any>;
  type: 'AFTER_ACTION' | 'BEFORE_ACTION';
  /** 执行顺序*/
  order: number;
}

eventEmit(eventName, {
  // 具体需要拦截的流程行为
  actions: ['NODE_ADD'],
  func: (bpmAction, bpmSdk) => {
    return new Promise((resolve)=> resolve('success'));
  },
  type: 'BEFORE_ACTION', // 必传
  order: 1,  // 校验顺序
});
```

●
actions 具体需要的注册进来的拦击行为，见code表

●
func 具体需要执行的校验方法，当返回的Promise是resolve状态就会往后执行，reject状态就不会往后执行了

●
type 指定行为执行的类型，行为执行之前：BEFORE_ACTION，行为执行之后：AFTER_ACTION；

●
order: 可选，注册多个的校验行为时，根据传递的执行顺序来执行，不传就按注册的属性来传递。

## 四、业务系统内部扩展

BPM流程行为由第三方实现，实现客开功能，比如加签。

### 1
行为执行之前拦截

如果需要再继续使用bpm的能力，则执行promise函数中的resolve方法继续执行。如果内部行为执行之前校验失败则执行promise函数中的reject函数，则后续不会再执行。

行为执行之前的大致执行顺序如下：

100%

### 2
完全拦截流程行为

完全拦截流程行为可以由行为执行之前的方案去实现，完全拦截则可以通过返回函数reject来实现完全客开的功能。

在传递的func函数中执行客户自己的业务逻辑。

### 3
行为执行之后拦截

行为执行之后的拦截如果存在校验失败或拦截不往后执行，会影响页面关闭逻辑，需要客开自行根据校验情况来resolve，如果不resolve则需要第三方自行控制关闭页面逻辑。

行为执行之后的执行顺序如下：

## 五、业务系统外部扩展

第三方插入一段js到index.html中，然后想客开bpm的能力。则可以通过以下方式来实现。

## 六、流程行为code表

上面拦截行为中的actions取值，参考code表。

| 操作类型 (Code) | 描述 (Description) |
| --- | --- |
| SEND | 发送 |
| SUBMIT | 提交 |
| READ | 已阅 |
| AGREE | 同意 |
| DIS_AGREE | 不同意 |
| TEMPORARY | 暂存 |
| DRAFT_HANDLE | 保存 |
| BACK | 回退 |
| UNDO | 撤销 |
| TERMINATION | 终止 |
| TRANSFER | 移交 |
| AFFAIR_CONSULT | 咨询 |
| RETRIEVE | 取回 |
| NOTICE | 知会 |
| GIVE | 会签 |
| NODE_ADD | 加签 |
| NODE_DEL | 减签 |
| DELETE_DRAFT | 删除待发 |
| MULTI_COOPERATE | 多人填写 |
| PAUSE | 挂起 |
| TRACK | 关注 |

## 七.实际场景DEMO

custom-frontend.zip
(1 KB)

custom-frontend.zip
(3 KB)

备注：流程按钮扩展行为PC端和移动端都支持
