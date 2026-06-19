---
title: "注册中心"
source: "https://www.yuque.com/seeyonkk/v8/qc6siuqr3xa5ti0c"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 注册中心

> Source: https://www.yuque.com/seeyonkk/v8/qc6siuqr3xa5ti0c

###### 1、使用场景

扩展非nacos作为注册中心

###### 2、集成步骤

参考SPI的开发规则：
开发准备

1、引入maven坐标

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>boot-starter-nacos</artifactId>
  <version>5.8.0</version>
</dependency>
```

2、需要实现的接口

```
com.seeyon.boot.starter.nacos.spi.RegisterServiceSPI
```

3、接口详解

```
public interface RegisterServiceSPI {
    /**
     * web服务注册
     */
    void registerInstance();
    /**
     * 服务注册(websocket组件注册websocket服务用)
     */
    void registerInstance(AppInstanceDto dto);
    /**
     * web服务卸载
     */
    void deregisterInstance();
    /**
     * web服务卸载
     */
    void deregisterInstance(String appName);
    /**
     * web服务卸载
     */
    default void deregisterInstance(String appName, String appVersion) {

    }
    /**
     * 获取指定应用实例列表
     */
    List<AppInstanceDto> getInstances(String appName);
    /**
     * 获取指定应用健康实例
     */
    AppInstanceDto getOneHealthyInstance(String appName);
    /**
     * 获取在线服务列表
     */
    List<String> selectAllServices();
    /**
```

###### 3、示例代码

NacosRegisterImpl.java
(11 KB)
