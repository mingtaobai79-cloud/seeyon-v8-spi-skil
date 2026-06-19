> 🧊 **冻结状态** — 缺少必要 jar 包，接口/DTO 均为 OBSERVATION，无法升级到 FACT。
> 待获取对应 jar 后解除冻结。

# 公文扩展 / EdocProjectPublicService

> Evidence: OBSERVATION ⚠️ — 语雀文档 + jar 反编译交叉验证。
> **jar 验证结果**：公文应用 artifact（含数字 ID `335172694483814428`）在 libs-release 仓库中未找到。
> 该接口只能通过泛化调用方式扩展，不是传统 SPI 注册。

## 场景

通过泛化调用方式扩展公文功能。支持版本：5.8 及以上。

**重要：该文档中的接口只能通过泛化的方式进行接口调用，不是传统 SPI 注册。**

## Service 路径

```
com.seeyon.edoc335172694483814428.refactor.app.business.invoker.EdocProjectPublicService
```

注意：包名中包含数字 ID `335172694483814428`，这是公文应用的唯一标识。

## 接口定义 [OBSERVATION ⚠️]

文档给出了完整的 import 列表，涉及大量 DTO 和 Service：

```java
package com.seeyon.edoc335172694483814428.refactor.app.business.invoker;

// 核心注解
import com.seeyon.boot.annotation.AppService;
import com.seeyon.boot.annotation.AppServiceOperation;
import com.seeyon.boot.annotation.OpenApi;

// DTO 和 Service（部分）
import com.seeyon.edoc335172694483814428.dto.*;
import com.seeyon.edoc335172694483814428.service.*;

@AppService
public interface EdocProjectPublicService {
    // 方法签名需 16KB 附件确认
}
```

## 泛化调用方式

```java
// 示例：通过 AppService 泛化调用
AppServiceInvokeDto invokeDto = new AppServiceInvokeDto();
invokeDto.setInterfaceName("com.seeyon.edoc335172694483814428.refactor.app.business.invoker.EdocProjectPublicService");
invokeDto.setMethodName("methodName");
invokeDto.setParams(new Object[]{param1, param2});

Object result = appServiceReliableInvoker.invoke(invokeDto);
```

## Nacos 配置

本 SPI 不需要额外 Nacos 配置。

## spring.factories

```properties
# 不适用：该接口通过泛化调用，不是传统 SPI 注册
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["edoc"]
}
```

## 重启服务

edoc

## 阻塞项

1. 公文应用 artifact（含数字 ID）在仓库中未找到
2. `EdocProjectPublicService` 完整接口定义需 16KB 附件确认
3. 大量 DTO 和 Service 的完整字段待确认
4. 泛化调用方式的具体示例代码待确认
