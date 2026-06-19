---
title: "swagger查看"
source: "https://www.yuque.com/seeyonkk/v8/swagger"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# swagger查看

> Source: https://www.yuque.com/seeyonkk/v8/swagger

作者：杨映海
最后更新：2025-04-27

## 1. 组件介绍

swagger组件用于扫描注解生成统一风格的rest api接口文档，同时提供可视化的Rest接口调试工具，可用于接口的测试。

## 2. 组件使用

@RestApi 标记在RestController类,用于描述Controller Rest接口类的显示名称。

RestController类不标注@RestApi则不会出现到swagger界面及元数据中。

@RequestMapping前缀必须是服务名

```java
@RestController
@RequestMapping({appName} + "/orderInfo")
@RestApi("订单访问接口")
public class OrderInfoController {

}
```

@RestApiOperation标记在RestController类中方法上，用于描述方法的作用。

RestController类中方法上不标注@RestApiOperation则不会出现到swagger界面及元数据中。

```
@RestApiOperation(value = "创建订单")
@PostMapping
public SingleResponse<Long> create(@RequestBody OrderInfoDto dto) {
    return appService.create(SingleRequest.from(dto));
}
```

@ParameterInfo标记在Rest接口的参数上，用于描述该参数（如果入参为dto类型的对象则无需描述）。

```
@RestApiOperation(value = "获取订单详情")
@GetMapping("{id}")
public SingleResponse<OrderInfoDto> selectById(@PathVariable("id") @ParameterInfo(value = "订单id") Long id) {
    return appService.selectById(SingleRequest.from(id));
}
```

@DtoInfo 标注于dto类上,用于描述该dto类。

@DtoAttribute 标注于已标注@DtoInfo注解的dto类的属性上,用于描述该属。

```java
@DtoInfo("订单信息")
public class OrderInfoDto {

    @DtoAttribute(value = "客户ID", example = "100001")
    private Long customerInfoId;

    @DtoAttribute(value = "订单编号", example = "X0001")
    @NotNull(groups = AppService.ValidationGroup.Create.class)
    private String orderNo;

    ......
}
```

@DtoAttribute的relationDto字段和relationApp用于描述该字段关联其他微服务的Dto,关联本服务dto时relationApp字段不填。

```
@DtoAttribute(value = "客户ID", example = "100001",relationApp="demo-customer", relationDto = "com.seeyon.demo.customer.dto.CustomerInfoDto")
private Long customerInfoId;
```

@NotNull,@NotEmpty,@NotBlank注解标注到Dto类的字段或者Rest接口的参数上用于标志该参数为必填。

```
@DtoAttribute(value = "客户ID", example = "100001", relationApp="demo-customer", relationDto = "com.seeyon.demo.customer.dto.CustomerInfoDto")
@NotNull
private Long customerInfoId;
```

```
@RestApiOperation(value = "获取订单详情")
@GetMapping("/get")
public SingleResponse<OrderInfoDto> selectById(@ParameterInfo(value = "订单id") @NotNull Long id) {
    return appService.selectById(SingleRequest.from(id));
}
```

## 3. JSR303支持

组件支持对JSR303 注解（@NotNull @Size @Max @Min等）的解析支持.

## 4、服务开启

进入Nacos，在对应命名空间的public中配置如下参数，开启swagger

## 5、在线查看

查看地址：https://{域名}/service/{服务名}/doc.html【需要用户先登录后才能访问】

示       例：https://pre.seeyonv8.com/service/edoc335172694483814428/doc.html

<img width="1650.5555992803468">
