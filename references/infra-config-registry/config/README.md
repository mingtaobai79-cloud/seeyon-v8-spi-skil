# 配置中心 / ConfigServiceSPI

> **Evidence: FACT ✅** — 接口签名来自 `boot-starter-nacos-5.3.358.jar` CFR 反编译。

## 场景

扩展非 Nacos 作为配置中心（如 Apollo、Spring Cloud Config 等）。

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>boot-starter-nacos</artifactId>
  <version>5.3.358</version>
</dependency>
```

## 接口定义 [FACT ✅]

```java
package com.seeyon.boot.starter.nacos.spi;

import com.seeyon.boot.starter.nacos.service.process.ConfigChangeProcess;

public interface ConfigServiceSPI {
    String getAppConfigStr();
    String getGlobalConfigStr();
    String getConfigStr(String var1);
    default boolean publishConfig(String configName, String configStr) { return false; }
    default boolean publishAppConfig(String configStr) { return false; }
    default void addAppConfigChangeListener(ConfigChangeProcess process) {}
    default void addGlobalConfigChangeListener(ConfigChangeProcess process) {}
    default void addConfigChangeListener(String configName, ConfigChangeProcess process) {}
    String getEngineName();
}
```

## 方法说明

| 方法 | 参数 | 返回 | 语义 |
|------|------|------|------|
| getAppConfigStr | 无 | `String` | 获取应用配置（YAML/JSON 字符串） |
| getGlobalConfigStr | 无 | `String` | 获取全局配置 |
| getConfigStr | `String configName` | `String` | 获取指定配置 |
| publishConfig | `String, String` | `boolean` | 发布指定配置（default false） |
| publishAppConfig | `String` | `boolean` | 发布应用配置（default false） |
| addAppConfigChangeListener | `ConfigChangeProcess` | void | 应用配置变更监听（default 空） |
| addGlobalConfigChangeListener | `ConfigChangeProcess` | void | 全局配置变更监听（default 空） |
| addConfigChangeListener | `String, ConfigChangeProcess` | void | 指定配置变更监听（default 空） |
| getEngineName | 无 | `String` | 返回配置引擎名称 |

## DTO 定义 [FACT ✅]

### ConfigChangeProcess

```java
package com.seeyon.boot.starter.nacos.service.process;

public interface ConfigChangeProcess {
    void process(String var1);
}
```

## 代码骨架

```java
package com.seeyon.extend.spi.infra;

import com.seeyon.boot.starter.nacos.spi.ConfigServiceSPI;
import com.seeyon.boot.starter.nacos.service.process.ConfigChangeProcess;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class CustomConfigService implements ConfigServiceSPI {

    private static final Logger log = LoggerFactory.getLogger(CustomConfigService.class);

    @Override
    public String getAppConfigStr() {
        log.debug("[config] getAppConfigStr called");
        return "";
    }

    @Override
    public String getGlobalConfigStr() {
        log.debug("[config] getGlobalConfigStr called");
        return "";
    }

    @Override
    public String getConfigStr(String configName) {
        log.debug("[config] getConfigStr({}) called", configName);
        return "";
    }

    @Override
    public String getEngineName() {
        return "custom-config";
    }
}
```

## Nacos 配置

本 SPI 不需要额外 Nacos 配置。

## spring.factories

```properties
com.seeyon.boot.starter.nacos.spi.ConfigServiceSPI=com.seeyon.extend.spi.infra.CustomConfigService
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["ALL"]
}
```

## 重启服务

全部服务
