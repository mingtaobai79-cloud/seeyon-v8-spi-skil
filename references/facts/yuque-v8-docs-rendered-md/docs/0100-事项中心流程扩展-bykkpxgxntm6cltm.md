---
title: "事项中心流程扩展"
source: "https://www.yuque.com/seeyonkk/v8/bykkpxgxntm6cltm"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 事项中心流程扩展

> Source: https://www.yuque.com/seeyonkk/v8/bykkpxgxntm6cltm

###### 1、使用场景

同一条流程，流程中的某个人有多条事项(已发、已办、待办)的时候，比如人员从已发中点击已发事项，由客户来指定打开的优先级，是待办还是已办

###### 2、开发步骤

1、SPI的开发规则，参照：
开发准备

2、引入maven坐标

```xml
<dependency>
    <groupId>com.seeyon</groupId>
    <artifactId>bpm-facade</artifactId>
    <version>5.8.0</version>
</dependency>
```

3、需要实现的SPI,两个SPI都需要做实现，才能将场景画圆

```
com.seeyon.bpm.spi.BpmOperationSpi
com.seeyon.bpm.spi.BpmDetailViewSpi
```

4、接口详解

```
public interface BpmDetailViewSpi{

    /**
     * 根据需求规则将当前的workitem事项替换成需要优先打开事项的workitem
     * 如果规则是优先打开待办，当前是从已发中打开的已发事项，那么将入参中的已发事项workitem
      替换成待办事项的workitem并作为出参返回
     * @param bpmForwardReq    当前正在加载的workItem事项
     * @return              需要重定向到的事项ID
     */
    BpmForwardResp forwardAffair(BpmForwardReq bpmForwardReq);
    /**
     * 将当前流程中，该人员所有事项(已发、已办、待办)的操作权限合并到一起
     * @param requestDto 事项权限合并请求
     * @return 事项权限合并响应
     */
    BpmNodePermissionMergeResp mergeNodePermission(BpmNodePermissionMergeReq requestDto);
}
```

BpmDetailViewSpi的mergeNodePermission接口将同一条流程中同一个人的所有操作权限合并在一起后，点击操作权限的时候需要对这个权限做校验，需要实现BpmOperationSpi中的checkNodePermission接口

```
public interface BpmOperationSpi {
    /**
     * 节点权限操作校验
     * @param requestDto 校验参数
     * @return 校验结果
     */
    BpmCheckNodePermissionResp checkNodePermission(BpmCheckNodePermissionReq requestDto);
}
```
