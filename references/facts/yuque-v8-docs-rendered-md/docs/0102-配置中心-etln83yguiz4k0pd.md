---
title: "配置中心"
source: "https://www.yuque.com/seeyonkk/v8/etln83yguiz4k0pd"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 配置中心

> Source: https://www.yuque.com/seeyonkk/v8/etln83yguiz4k0pd

###### 1、使用场景

扩展非nacos作为配置中心

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
com.seeyon.boot.starter.nacos.spi.ConfigServiceSPI
```

3、接口详解

```
public interface ConfigServiceSPI {
    /**
     * 获取应用配置
     */
    String getAppConfigStr();
    /**
     * 获取全局配置
     */
    String getGlobalConfigStr();
    /**
     * 获取指定配置
     */
    String getConfigStr(String configName);
    /**
     * 发布指定配置
     */
    default boolean publishConfig(String configName, String configStr) {
        return false;
    }
    /**
     * 发布应用配置
     */
    default boolean publishAppConfig(String configStr) {
        return false;
    }
    /**
     * 应用配置监听
     */
    default void addAppConfigChangeListener(ConfigChangeProcess process) {
    }
    /**
     * 全局配置监听
     */
    default void addGlobalConfigChangeListener(ConfigChangeProcess process) {
    }
    /**
```

###### 3、示例代码

NacosConfigImpl.java
(4 KB)
