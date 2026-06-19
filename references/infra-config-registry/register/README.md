# 注册中心 / RegisterServiceSPI

> **Evidence: FACT ✅** — 接口签名、DTO 来自 `boot-starter-nacos-5.3.358.jar` CFR 反编译。

## 场景

扩展非 Nacos 作为注册中心（如 Consul、Eureka、Zookeeper 等）。

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

import com.seeyon.boot.starter.nacos.dto.AppInstanceDto;
import com.seeyon.boot.starter.nacos.service.process.AppChangeProcess;
import java.util.List;

public interface RegisterServiceSPI {
    void registerInstance();
    void registerInstance(AppInstanceDto var1);
    void deregisterInstance();
    void deregisterInstance(String var1);
    default void deregisterInstance(String appName, String appVersion) {}
    List<AppInstanceDto> getInstances(String var1);
    AppInstanceDto getOneHealthyInstance(String var1);
    List<String> selectAllServices();
    void subscribe(String var1, AppChangeProcess var2);
    String getEngineName();
}
```

## 方法说明

| 方法 | 参数 | 返回 | 语义 |
|------|------|------|------|
| registerInstance | 无 | void | web 服务注册 |
| registerInstance | `AppInstanceDto` | void | websocket 服务注册 |
| deregisterInstance | 无 | void | web 服务卸载 |
| deregisterInstance | `String appName` | void | 指定应用卸载 |
| deregisterInstance | `String, String` | void | 指定应用+版本卸载（default） |
| getInstances | `String appName` | `List<AppInstanceDto>` | 获取应用实例列表 |
| getOneHealthyInstance | `String appName` | `AppInstanceDto` | 获取健康实例 |
| selectAllServices | 无 | `List<String>` | 获取在线服务列表 |
| subscribe | `String, AppChangeProcess` | void | 订阅服务变更 |
| getEngineName | 无 | `String` | 返回注册引擎名称 |

## DTO 定义 [FACT ✅]

### AppInstanceDto

```java
package com.seeyon.boot.starter.nacos.dto;

public class AppInstanceDto implements Serializable {
    String instanceId;
    String ip;
    int port;
    double weight = 1.0;
    boolean healthy = true;
    String clusterName;
    String serviceName;
    Map<String, String> metadata = new HashMap<>();
}
```

## 代码骨架

```java
package com.seeyon.extend.spi.infra;

import com.seeyon.boot.starter.nacos.spi.RegisterServiceSPI;
import com.seeyon.boot.starter.nacos.dto.AppInstanceDto;
import com.seeyon.boot.starter.nacos.service.process.AppChangeProcess;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.ArrayList;
import java.util.List;

public class CustomRegisterService implements RegisterServiceSPI {

    private static final Logger log = LoggerFactory.getLogger(CustomRegisterService.class);

    @Override
    public void registerInstance() {
        log.info("[register] registerInstance called");
    }

    @Override
    public void registerInstance(AppInstanceDto dto) {
        log.info("[register] registerInstance(dto) called");
    }

    @Override
    public void deregisterInstance() {
        log.info("[register] deregisterInstance called");
    }

    @Override
    public void deregisterInstance(String appName) {
        log.info("[register] deregisterInstance({}) called", appName);
    }

    @Override
    public List<AppInstanceDto> getInstances(String appName) {
        log.debug("[register] getInstances({}) called", appName);
        return new ArrayList<>();
    }

    @Override
    public AppInstanceDto getOneHealthyInstance(String appName) {
        log.debug("[register] getOneHealthyInstance({}) called", appName);
        return null;
    }

    @Override
    public List<String> selectAllServices() {
        log.debug("[register] selectAllServices called");
        return new ArrayList<>();
    }

    @Override
    public void subscribe(String serviceName, AppChangeProcess process) {
        log.debug("[register] subscribe({}) called", serviceName);
    }

    @Override
    public String getEngineName() {
        return "custom-registry";
    }
}
```

## Nacos 配置

本 SPI 不需要额外 Nacos 配置。

## spring.factories

```properties
com.seeyon.boot.starter.nacos.spi.RegisterServiceSPI=com.seeyon.extend.spi.infra.CustomRegisterService
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
