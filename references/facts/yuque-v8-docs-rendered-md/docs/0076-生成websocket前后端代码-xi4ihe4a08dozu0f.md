---
title: "生成websocket前后端代码"
source: "https://www.yuque.com/seeyonkk/v8/xi4ihe4a08dozu0f"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 生成websocket前后端代码

> Source: https://www.yuque.com/seeyonkk/v8/xi4ihe4a08dozu0f

## 应用场景

待办详情页面处理完之后需要自动更新待办列表数据信息，可通过websocket来处理更新

## 代码

```
/******************** 后端代码开始 ********************/
@Autowired
private EventBus eventBus;

Set<Long> users = new HashSet<>();
//users.add(1L); // TODO 推送给指定用户，传人员ID
TextMessage sendMessage = new TextMessage();
sendMessage.setUserIdSet(users);
sendMessage.setOperate(demoKey);
sendMessage.setTenantId(Apps.getRequestContext().getTenantId());
sendMessage.addMessage("data", "TODO 推送给前端的数据");
eventBus.publish(sendMessage);
/******************** 后端代码结束 ********************/

/******************** 前端代码 tsx 文件开始 ********************/
//说明：以此部分代码创建名为WebSocketDemo.tsx的文件，其中import useMemoizedFn 的路径需要与下方ts代码所在文件一致
import React, { useState, useEffect, useRef } from "react";
import useMemoizedFn from "./service/socket"; // 确保能引用到socket.ts文件

interface Props {}

const WebSocketDemo: React.FC<Props> = (props) => {
  // region websocket
  // 调用websock
  const [websocketUUID, setWebsocketUUID] = useState<string>();
  const socketInitRef = useRef(false);

  // 初始化socket
  const initSocket = useMemoizedFn(() => {
    if ((window as any)?.jsSdk?.socket?.on) {
      (window as any)?.jsSdk?.socket?.on({
        messageType: "demoKey", // 跟后端约定好的消息Key
        callback: (data: any) => {
          // 第一次注册会调一次callback 传入uuid，此时不执行业务逻辑
```

备注：此代码只是示例代码
