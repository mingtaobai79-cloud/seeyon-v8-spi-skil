# 批处理三方待办 / AbstractThirdAffairService

> Evidence: FACT ✅ 用户提供的反编译接口源码 + 用户现场 artifact 核验。
> Contract Source: `repo_key:<project-repo>!/com/seeyon/ctp-affair-facade/5.3.315/ctp-affair-facade-5.3.315.jar`。
> 语雀 `0090-批处理三方待办事项-gonq0zusief36hit.md` 为 OBSERVATION。

## 场景

三方待办数据集成到 V8 待办以后，在 V8 页面对三方数据进行批量处理。

适用版本：3.15 及以上版本；当前已核验 artifact 版本：`ctp-affair-facade-5.3.315`。

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>ctp-affair-facade</artifactId>
  <!-- 文档原始最低版本：3.15.0；当前现场已核验：5.3.315 -->
  <version>5.3.315</version>
</dependency>
```

## 接口定义 [FACT ✅]

Locator：`ctp-affair-facade-5.3.315.jar!/com/seeyon/ctp/affair/spi/third/AbstractThirdAffairService.class`。

```java
package com.seeyon.ctp.affair.spi.third;

import com.seeyon.ctp.affair.dto.AffairBatchDto;
import com.seeyon.ctp.affair.dto.AffairBatchResponseDto;
import java.util.List;

public interface AbstractThirdAffairService {
    List<AffairBatchResponseDto> batchOperateThirdAffair(AffairBatchDto var1);
}
```

## 方法说明

| 方法 | 参数 | 返回 | 语义 |
|------|------|------|------|
| `batchOperateThirdAffair` | `AffairBatchDto` | `List<AffairBatchResponseDto>` | 批量处理三方事项 |

## DTO 定义 [FACT ✅]

Locator：`ctp-affair-facade-5.3.315.jar!/com/seeyon/ctp/affair/dto/*.class`。

### AffairBatchDto（入参）

```java
package com.seeyon.ctp.affair.dto;

@DtoInfo("待办中心批处理请求")
public class AffairBatchDto extends BaseDto {
    @DtoAttribute(value = "用户ID", hidden = true)
    private Long userId;

    @DtoAttribute(value = "处理动作")
    @NotNull(message = "处理动作不能为空")
    private String operation;

    @DtoAttribute(value = "意见信息dto")
    private OpinionDto opinionDto;

    @DtoAttribute(value = "批次id")
    private String batchId;

    @DtoAttribute(value = "批处理事项列表")
    @NotEmpty(message = "批处理事项列表不能为空")
    private List<AffairBatchSubDto> list;
}
```

### AffairBatchSubDto（子项）

```java
package com.seeyon.ctp.affair.dto;

@DtoInfo("批量处理子dto")
public class AffairBatchSubDto extends BaseDto {
    @DtoAttribute(value = "affairId", example = "123456331")
    @NotNull(message = "affairId 不能为空")
    private Long affairId;

    @DtoAttribute(value = "workflow", example = "true")
    private Boolean workflow;

    @DtoAttribute(value = "审批应用运行态Id", example = "123456331")
    private Long summaryId;

    @DtoAttribute(value = "流程标题", example = "《流程名称》")
    @NotNull(message = "流程标题不能为空")
    private String title;

    @DtoAttribute(value = "表单数据，这里表单数据只传节点权限id，其它表单数据udc去做查询过滤")
    private Map<String, Object> formData;

    @DtoAttribute(value = "事项来源应用ID", example = "app_approval")
    @NotNull(message = "appName 不能为空")
    private String appName;
}
```

### OpinionDto（意见）

```java
package com.seeyon.ctp.affair.dto;

@DtoInfo("意见回复DTO")
public class OpinionDto {
    @DtoAttribute(value = "意见信息", example = "111")
    private String content;
}
```

### AffairBatchResponseDto（出参）

```java
package com.seeyon.ctp.affair.dto;

@DtoInfo("批处理返回dto")
public class AffairBatchResponseDto extends BaseDto {
    @DtoAttribute(value = "当前事项Id", example = "123456331")
    private Long affairId;

    @DtoAttribute(value = "返回错误信息", example = "《流程名称》存在同一流程中的多个事项不能被批处理")
    private String errorMessage;

    @DtoAttribute(value = "流程标题", example = "《流程名称》")
    private String title;

    @DtoAttribute(value = "状态, 是否成功", example = "true")
    private boolean success;
}
```

### BaseDto（基类）

```java
package com.seeyon.boot.transport;

@DtoInfo("dto基类")
@JsonIgnoreProperties(ignoreUnknown = true)
public abstract class BaseDto implements Serializable {
    @DtoAttribute(value = "校验标识", hidden = true, example = "true")
    private boolean validate = true;

    public void check() throws ValidationException {
        if (this.validate) {
            Validators.assertjsr303(this, new Class[0]);
        }
    }
}
```

## Nacos 配置

```yaml
# ctp-affair 微服务 Nacos 配置
seeyon:
  affair:
    third-batch:
      enabled: true
      timeout-ms: 30000
      retry-times: 1
```

## spring.factories

```properties
com.seeyon.ctp.affair.spi.third.AbstractThirdAffairService=\
com.seeyon.extend.spi.{project_id}.{Prefix}ThirdAffairService
```

## 代码骨架

```java
package com.seeyon.extend.spi.{project_id};

import com.seeyon.ctp.affair.dto.AffairBatchDto;
import com.seeyon.ctp.affair.dto.AffairBatchResponseDto;
import com.seeyon.ctp.affair.dto.AffairBatchSubDto;
import com.seeyon.ctp.affair.spi.third.AbstractThirdAffairService;
import lombok.extern.slf4j.Slf4j;

import java.util.ArrayList;
import java.util.List;

/**
 * {project_name_cn} 三方待办批处理
 *
 * 场景：三方待办数据集成到 V8 待办后，在 V8 页面对三方数据进行批量处理
 * V8 调用时机：用户在 V8 前端选择三方数据后点击批量处理，框架调用 batchOperateThirdAffair
 * 三方系统：{third_system_name}
 * 返回语义：每个事项的处理结果（成功/失败 + 错误信息）
 */
@Slf4j
public class {Prefix}ThirdAffairService implements AbstractThirdAffairService {

    @Override
    public List<AffairBatchResponseDto> batchOperateThirdAffair(AffairBatchDto affairBatchDto) {
        log.info("[todo-batch] 批处理三方待办, userId: {}, operation: {}, 事项数: {}",
                 affairBatchDto.getUserId(),
                 affairBatchDto.getOperation(),
                 affairBatchDto.getList() != null ? affairBatchDto.getList().size() : 0);

        List<AffairBatchResponseDto> results = new ArrayList<>();

        if (affairBatchDto.getList() == null || affairBatchDto.getList().isEmpty()) {
            log.warn("[todo-batch] 批处理事项列表为空");
            return results;
        }

        for (AffairBatchSubDto subDto : affairBatchDto.getList()) {
            AffairBatchResponseDto response = new AffairBatchResponseDto();
            response.setAffairId(subDto.getAffairId());
            response.setTitle(subDto.getTitle());

            try {
                // TODO: 调用三方系统处理逻辑
                // 根据 affairBatchDto.getOperation() 判断操作类型
                // 根据 subDto.getAppName() 判断来源应用
                // 根据 subDto.getFormData() 获取表单数据
                // 根据 affairBatchDto.getOpinionDto() 获取意见信息

                response.setSuccess(true);
                log.info("[todo-batch] 事项处理成功, affairId: {}, title: {}",
                         subDto.getAffairId(), subDto.getTitle());

            } catch (Exception e) {
                response.setSuccess(false);
                response.setErrorMessage("处理失败: " + e.getMessage());
                log.error("[todo-batch] 事项处理失败, affairId: {}, title: {}",
                          subDto.getAffairId(), subDto.getTitle(), e);
            }

            results.add(response);
        }

        log.info("[todo-batch] 批处理完成, 总数: {}, 成功: {}",
                 results.size(),
                 results.stream().filter(AffairBatchResponseDto::isSuccess).count());

        return results;
    }
}
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["ctp-affair"]
}
```

## 重启服务

`ctp-affair`
