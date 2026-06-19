# 事项中心流程扩展 / BpmOperationSpi + BpmDetailViewSpi

> **Evidence: FACT ✅** — 接口签名、DTO 来自 `bpm-facade-5.3.374.jar` CFR 反编译。

## 场景

同一条流程中，某个人有多条事项（已发、已办、待办）时，由客户指定打开的优先级。
两个 SPI 都需要实现，才能将场景画圆。

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>bpm-facade</artifactId>
  <version>5.3.374</version>
</dependency>
```

## 接口定义 [FACT ✅]

### BpmDetailViewSpi

```java
package com.seeyon.bpm.spi;

import com.seeyon.bpm.spi.dto.detail.BpmForwardReq;
import com.seeyon.bpm.spi.dto.detail.BpmForwardResp;
import com.seeyon.bpm.spi.dto.detail.BpmNodePermissionMergeReq;
import com.seeyon.bpm.spi.dto.detail.BpmNodePermissionMergeResp;

public interface BpmDetailViewSpi {
    BpmForwardResp forwardAffair(BpmForwardReq var1);
    BpmNodePermissionMergeResp mergeNodePermission(BpmNodePermissionMergeReq var1);
}
```

### BpmOperationSpi

```java
package com.seeyon.bpm.spi;

import com.seeyon.bpm.spi.dto.operation.BpmCheckNodePermissionReq;
import com.seeyon.bpm.spi.dto.operation.BpmCheckNodePermissionResp;

public interface BpmOperationSpi {
    BpmCheckNodePermissionResp checkNodePermission(BpmCheckNodePermissionReq var1);
}
```

## 方法说明

| 接口 | 方法 | 参数 | 返回 | 语义 |
|------|------|------|------|------|
| BpmDetailViewSpi | forwardAffair | `BpmForwardReq` | `BpmForwardResp` | 事项重定向（优先级选择） |
| BpmDetailViewSpi | mergeNodePermission | `BpmNodePermissionMergeReq` | `BpmNodePermissionMergeResp` | 权限合并 |
| BpmOperationSpi | checkNodePermission | `BpmCheckNodePermissionReq` | `BpmCheckNodePermissionResp` | 权限校验 |

## DTO 定义 [FACT ✅]

### BpmForwardReq

```java
package com.seeyon.bpm.spi.dto.detail;

@DtoInfo("事项重定向请求")
public class BpmForwardReq {
    Long currentWorkItemId;  // 当前事项ID
}
```

### BpmForwardResp

```java
package com.seeyon.bpm.spi.dto.detail;

@DtoInfo("事项重定向响应")
public class BpmForwardResp {
    Long forwardWorkItemId;   // 需要重定向到的事项ID
    Long formPermissionId;    // 重定向到的事项对应的表单权限ID
}
```

### BpmNodePermissionMergeReq

```java
package com.seeyon.bpm.spi.dto.detail;

@DtoInfo("事项权限合并请求Dto")
public class BpmNodePermissionMergeReq {
    Long caseId;                                          // 流程实例ID
    Long affairId;                                        // 事项ID
    Long nodePermissionId;                                // 节点权限ID
    List<BpmNodePermissionOperationSimpleDto> originalOperationList;  // 原始的节点权限列表
}
```

### BpmNodePermissionMergeResp

```java
package com.seeyon.bpm.spi.dto.detail;

@DtoInfo("事项权限合并响应Dto")
public class BpmNodePermissionMergeResp {
    List<BpmNodePermissionOperationSimpleDto> operationList;  // 合并后的节点权限操作列表
}
```

### BpmCheckNodePermissionReq

```java
package com.seeyon.bpm.spi.dto.operation;

@DtoInfo("节点权限操作校验请求")
public class BpmCheckNodePermissionReq {
    Long caseId;           // 流程实例ID
    Long affairId;         // 事项ID
    Long permissionId;     // 节点权限ID
    BpmCommentDto commentDto;  // 意见实体
    String operationCode;  // 操作编码
}
```

### BpmCheckNodePermissionResp

```java
package com.seeyon.bpm.spi.dto.operation;

@DtoInfo("节点权限操作校验响应")
public class BpmCheckNodePermissionResp {
    boolean passOperationVerify = false;         // 是否通过操作合法校验
    boolean passCommentRequiredVerify = false;   // 是否通过操作意见必填校验
    boolean passCommentLengthVerify = false;     // 是否通过操作意见长度校验
    Long affairId;                               // 真实需要操作的事项
}
```

## 两个 SPI 的协作关系

1. `mergeNodePermission` 将同一条流程中同一个人的所有操作权限合并。
2. 点击操作权限时，`checkNodePermission` 对合并后的权限做校验。
3. 两个 SPI 必须配合实现，才能完整覆盖场景。

## 代码骨架

```java
package com.seeyon.extend.spi.bpm;

import com.seeyon.bpm.spi.BpmDetailViewSpi;
import com.seeyon.bpm.spi.BpmOperationSpi;
import com.seeyon.bpm.spi.dto.detail.*;
import com.seeyon.bpm.spi.dto.operation.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class CustomBpmDetailViewSpi implements BpmDetailViewSpi {

    private static final Logger log = LoggerFactory.getLogger(CustomBpmDetailViewSpi.class);

    @Override
    public BpmForwardResp forwardAffair(BpmForwardReq bpmForwardReq) {
        log.debug("[bpm] forwardAffair called, currentWorkItemId={}",
            bpmForwardReq.getCurrentWorkItemId());
        BpmForwardResp resp = new BpmForwardResp();
        // TODO: 实现事项重定向逻辑（如优先打开待办）
        // resp.setForwardWorkItemId(targetWorkItemId);
        return resp;
    }

    @Override
    public BpmNodePermissionMergeResp mergeNodePermission(BpmNodePermissionMergeReq requestDto) {
        log.debug("[bpm] mergeNodePermission called, caseId={}, affairId={}",
            requestDto.getCaseId(), requestDto.getAffairId());
        BpmNodePermissionMergeResp resp = new BpmNodePermissionMergeResp();
        // TODO: 实现权限合并逻辑
        // resp.setOperationList(mergedOperations);
        return resp;
    }
}

class CustomBpmOperationSpi implements BpmOperationSpi {

    private static final Logger log = LoggerFactory.getLogger(CustomBpmOperationSpi.class);

    @Override
    public BpmCheckNodePermissionResp checkNodePermission(BpmCheckNodePermissionReq requestDto) {
        log.debug("[bpm] checkNodePermission called, caseId={}, operationCode={}",
            requestDto.getCaseId(), requestDto.getOperationCode());
        BpmCheckNodePermissionResp resp = new BpmCheckNodePermissionResp();
        // TODO: 实现权限校验逻辑
        // resp.setPassOperationVerify(true);
        // resp.setPassCommentRequiredVerify(true);
        // resp.setPassCommentLengthVerify(true);
        return resp;
    }
}
```

## Nacos 配置

本 SPI 不需要额外 Nacos 配置。

## spring.factories

```properties
com.seeyon.bpm.spi.BpmDetailViewSpi=com.seeyon.extend.spi.bpm.CustomBpmDetailViewSpi
com.seeyon.bpm.spi.BpmOperationSpi=com.seeyon.extend.spi.bpm.CustomBpmOperationSpi
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["bpm"]
}
```

## 重启服务

bpm
