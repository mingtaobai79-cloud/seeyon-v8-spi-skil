---
title: "批处理三方待办事项"
source: "https://www.yuque.com/seeyonkk/v8/gonq0zusief36hit"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 批处理三方待办事项

> Source: https://www.yuque.com/seeyonkk/v8/gonq0zusief36hit

作者：陈晓东

时间：2026.6.1

适用版本：3.15及以上版本

使用场景：三方待办数据集成到V8待办以后，在V8页面对三方数据进行批量处理

# 1、SPI开发

SPI开发规范，参考：
开发准备

# 2、添加依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>ctp-affair-facade</artifactId>
  <version>3.15.0</version>
</dependency>
```

# 3、客开实现方法

```
/**
 * 三方事项服务类
 *
 * @author liu xiong
 * @date 2024/10/17
 */
public interface AbstractThirdAffairService {

    /**
     * 批量处理三方事项
     * @param affairBatchDto   三方事项
     * @return                 事项处理结果
     */
    List<AffairBatchResponseDto> batchOperateThirdAffair(AffairBatchDto affairBatchDto);
}
```

说明：AffairBatchDto 入参是操作人员在V8前端页面选择到的三方数据信息，客开在batchOperateThirdAffair方法里面调用三方的处理逻辑，进行事项处理。处理完成以后按照出参规则AffairBatchResponseDto返回

```java
/**
 * @description : 待办中心批处理请求
 * @company : Seeyon.com
 * @author : liuhf
 * @since  : V8 1.0
 */
@Getter
@Setter
@DtoInfo(value = "批处理dto")
public class AffairBatchDto extends BaseDto {
    private static final long serialVersionUID = 3028531161808711665L;

    @DtoAttribute(value = "用户ID", hidden = true)
    private Long userId ;

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

```java
/**
 * @description : 待办中心批处理响应
 * @company : Seeyon.com
 * @author : liuhf
 * @since  : V8 1.0
 */
@Getter
@Setter
@DtoInfo(value = "批处理返回dto")
public class AffairBatchResponseDto extends BaseDto {
    private static final long serialVersionUID = -2202876467700115154L;

    @DtoAttribute(value = "当前事项Id", example = "123456331")
    private Long affairId ;

    @DtoAttribute(value = "返回错误信息", example = "《流程名称》存在同一流程中的多个事项不能被批处理")
    private String errorMessage;

    @DtoAttribute(value = "流程标题", example = "《流程名称》")
    private String title;

    @DtoAttribute(value = "状态, 是否成功", example = "true")
    private boolean success;
}
```

# 4、重启服务

重启ctp-affair服务
