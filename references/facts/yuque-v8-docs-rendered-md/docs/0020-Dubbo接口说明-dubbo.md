---
title: "Dubbo接口说明"
source: "https://www.yuque.com/seeyonkk/v8/dubbo"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# Dubbo接口说明

> Source: https://www.yuque.com/seeyonkk/v8/dubbo

作者：陈晓东

时间：2025-08-15

##### 1、组件使用

初始化了dubbo基本配置，可通过Dubbo的注解配置使用Consumer和Provider。

##### 2、Provider

下面的代码暴露了DemoService服务，版本为1.0

```java
//使用dubbo提供的annotation
import org.apache.dubbo.config.annotation.DubboService;
//如果实现类只实现了一个接口，可以不指定interfaceClass，实现多个接口时，请指定要暴露的接口
@DubboService(version = "1.0")
public class DemoServiceImpl implements DemoService {

    @Override
    public String echo(String msg) {
        return msg;
    }
}
```

##### 3、Consumer

下面的代码使用了DemoService服务，版本为1.0

```
@DubboReference(version = "1.0")
private DemoService demoService;
```

version可以不指定，默认为 配置中心配置的 seeyon.dubbo.version 键对应的值

其中，在某些调用上需要进行调用缓存优化的可以在DubboRefrence注解上增加cache属性，如下面的例子

```
@DubboReference(version = "1.0"，cache = "lru")
private DemoService demoService;
```

##### 4、补充说明

Dubbo默认的请求传输负载大小为8M，同时Dubbo也不适合大数据的传输， 建议大于2M的数据通过OSS进行传输。
