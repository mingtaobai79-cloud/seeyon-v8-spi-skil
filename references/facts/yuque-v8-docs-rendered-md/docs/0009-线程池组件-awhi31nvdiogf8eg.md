---
title: "线程池组件"
source: "https://www.yuque.com/seeyonkk/v8/awhi31nvdiogf8eg"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 线程池组件

> Source: https://www.yuque.com/seeyonkk/v8/awhi31nvdiogf8eg

作者：陈晓东

时间：2025-08-18

##### 1、参数配置

```
seeyon:
  threadpool:
    coreSize: 100 #可选：线程池长期维持的线程数，即使线程处于Idle状态，也不会回收 
    maxSize: 200 #可选：线程数的上限 
    queueSize: 500 #可选：任务的排队队列长度 
    middle:
        coreSize: 20 #可选：线程池长期维持的线程数，即使线程处于Idle状态，也不会回收 
        maxSize: 40 #可选：线程数的上限 
        queueSize: 100 #可选：任务的排队队列长度 
    high:
        coreSize: 10 #可选：线程池长期维持的线程数，即使线程处于Idle状态，也不会回收 
        maxSize: 20 #可选：线程数的上限 
        queueSize: 50 #可选：任务的排队队列长度
```

##### 2、使用方法

1、 注入SeeyonExecutorService对象， 可以使用sumit、submitMiddle、submitHigh和execute、executeMiddle、executeHigh方法，其中middle和high线程池跟默认线程池分开为独立线程池，线程池之间的线程不会争抢资源

2、创建隔离的线程池，支持根据名称指定提交到不通的线程池。注入IsolatorExecutorService对象

```
@Autowired
private SeeyonExecutorService executorService;
@Autowired
private IsolatorExecutorService isolatorExecutorService;
```

##### 4、注意事项

1、此线程池默认拒绝策略为：AbortPolicy，避免异步处理堆积影响整体服务可用性

2、线程池配置需要考虑实际业务中cpu密集还是I/O密集进行相应的设置
