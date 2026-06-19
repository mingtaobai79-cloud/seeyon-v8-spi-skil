---
title: "人员头像biz-avator"
source: "https://www.yuque.com/seeyonkk/v8/rpd5kylbiak348hn"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 人员头像biz-avator

> Source: https://www.yuque.com/seeyonkk/v8/rpd5kylbiak348hn

## 用户头像

### 1.组件效果：

<img src="https://cdn.nlark.com/yuque/0/2026/png/50254821/1769351095298-3954eaea-48ca-4c26-acb7-4cc00914447f.png" width="750.4">

## 2.组件用法

```
import { Avatar } from '@seeyon/biz-avatar';

export default function MemberList(props:any){
  return (
    <>
     <Avatar
        type="user"
        size={40}
        id={user?.userId}
        label={getTranslateLangData(user?.userName)}
        reqKey={user?.userId}
      />
    </>
  )
}
```

```
import React from 'react';
import { Avatar } from '@seeyon/biz-avatar';
import {getCurrentUser} from '@seeyon/global'

export default function CustomPage() {
  const currentUser = getCurrentUser();
  return(<>
    <div>
      <Avatar 
        key={currentUser.userId}
        reqKey={currentUser.userId}
        type="user"
        id={currentUser.userId}
        iconName="LinedUser"
        size={95}
        label={currentUser.userName}
        subType="user"
        />
    </div>
  </>) 
}
```

## 3.组件属性

| 参数 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| type | 头像的类型（必填） | 'user' ， 'app' ， 'group' | - |
| id | 对象的id（选填），色系计算依赖id | string | - |
| size | 组件大小（必填），支持指定size，见效果图 | number | 24 |
| label | 用户姓名or应用名称（选填） | string | - |
| reqKey | 请求的参数（选填），用户传用户id，应用传storageKey | string | - |
| wrapperClassName | 包裹dom的classname（选填） | string | - |
| iconName | 应用的图标，用 SyIcon 的name（选填） | string | - |
| userImgUrl | 已经拿到头像时使用（选填） | string | - |
| appImgUrl | 已经拿到系统头像时使用（选填） | string | - |
| groupImgUrl | 已经拿到群组头像时使用（选填） | string | - |
| defaultIcon | 给出几组默认色系（选填） | 'synergy', 'knowledge', 'meeting', 'cultural', 'approval', 'costControlManagement', 'toDo', 'clockIn', 'message', 'done', 'report', 'user-0', 'user-1', 'user-2', 'user-3', 'user-4', 'user-5' | - |
| userAvatarDetailEnable(废弃) | 点击头像弹出用户详情弹窗（选填） | boolean | true |
| onClick | click回调事件（选填） | (id: string) => void | - |
| personnelCardProps（废弃） | 用户详情弹窗（PersonnelCard）的props属性（选填） | PersonnelCardType | - |
| onClickContent | 内容domclick回调事件（选填） | (id: string) => void | - |
| onGetUrl | 获取到url后的回调（选填） | (url: string) => unknown; | - |
| cacheUrl | 是否需要缓存url（选填）（如虚拟列表会销毁组件重复请求） | - | - |
| shape | 头像形状 | 'circle', 'square' | 应用默认为 'square'，头像默认为 'circle' |
| color | 自定义文字或字体颜色（选填） | string | '' |
| backgroundColor | 自定义背景颜色（选填） | string | '' |
