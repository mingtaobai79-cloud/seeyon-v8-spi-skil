---
title: "Swagger规范"
source: "https://www.yuque.com/seeyonkk/v8/tux0x37ib090xqk6"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# Swagger规范

> Source: https://www.yuque.com/seeyonkk/v8/tux0x37ib090xqk6

## Swagger规范

1
【强制】所有Controller类必须标注@RestApi("接口类描述")，如果整个类所有接口不希望出现在接口文档中则在类上则不标注。

2
【强制】所有Controller类中rest接口必须标注@RestApiOperation(value = "接口描述")，如果该rest接口不希望出现在接口文档中则不标注。

3
【强制】rest接口参数为普通参数(如String，int，long等)，如果为必填请使用@ParameterInfo(value = "参数描述")标注。

4
【强制】所有Dto类必须标注@DtoInfo("dto类描述")，每个dto类必须有对应的Controller类，Controller类中必须有@GetMapping("{id}")和@PostMapping("search")方法。

5
【强制】所有Dto类中字段必须标注@DtoAttribute(value = "字段描述")，如果该字段不希望出现在接口文档中请标注@DtoAttribute(hidden = true)。

6
【强制】如果Dto类中某个字段需要关联查询其他Dto(如订单Dto中有一个客户id字段需要查询客户信息)，则必须标注@DtoAttribute(relationDto="xxxDto")，如跨服务则标注@DtoAttribute(relationApp="demo-customer",relationDto="xxxDto")。
举例：

```
    @DtoAttribute(value = "客户ID", example = "100001", relationDto="com.seeyon.xxx.xxx.xxDto")
    private Long customerInfoId;
```

7
【强制】Rest入参或者Dto类中属性如果需要必填校验请单独使用@NotNull注解。
