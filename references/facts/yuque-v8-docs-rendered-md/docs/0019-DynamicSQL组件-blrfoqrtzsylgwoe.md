---
title: "DynamicSQL组件"
source: "https://www.yuque.com/seeyonkk/v8/blrfoqrtzsylgwoe"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# DynamicSQL组件

> Source: https://www.yuque.com/seeyonkk/v8/blrfoqrtzsylgwoe

作者：陈晓东

时间：2025-08-15

##### 1、组件介绍

本组件提供应用动态拼装LEFT JOIN SQL查询的能力 本组件支持的操作类型包含："EQ", "NEQ", "LT", "LE", "GT", "GE", "IN", "NOTIN", "LIKE", "RLIKE", "LLIKE", "NOTLIKE", "NULL", "NOTNULL"

##### 2、maven坐标

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>boot-starter-dynamicsql</artifactId>
  <version>版本号</version>
</dependency>
```

##### 3、接口示例

```java
@RestController
@RequestMapping("demo-user/dynamic")
@Api(tags = "动态接口")
@Slf4j
public class DynamicController extends AbstractDynamicSelectController<CtpRoleDynamicDto> {
}
```

方法参数JSON结构说明见下面代码块示例

```
{
    "pageInfo":{
        "needTotal":false,
        "pageNumber":1,
        "pageSize":20,
        "pages":0,
        "total":0
    },
    "params":{
        "name":"Dto1",
        "children":[{
            "name":"Dto2",
            "join":"attribute1", // Dto2的属性字段，指向父Dto
            "children":null
        }],
        "fieldSet": ["attribute1"] // 指定查询结果字段，如果没有指定则查询所有字段
    },
    "cond":{
        "cond": {},  // 见下面cond结构说明（Left Join的查询条件）
        "in": {}     // 见下面的in结构说明（In子查询的查询条件）
    },
    "sort":{
        "orders":[
            {
                "direction":"ASC",
                "property":"Dto1_createTime"  // 和标准sort不同，property需要Dto1_前缀
            }
        ]
    }
}
```

```
// AND 条件：
{
  "and":[
    {"EQ_Dto1_attribute1":1},
    {"NEQ_Dto1_attribute1":2}
  ]
}
// OR 条件：
{
  "or":[
    {"EQ_Dto1_attribute1":1},
    {"NEQ_Dto1_attribute1":2}
  ]
}
// AND 和 OR联合使用
{
  "and":[
    {"EQ_Dto1_attribute1":1},
    {"NEQ_Dto1_attribute2":2},
    {
      "or":[
        {"EQ_Dto2_attribute1":1},
        {
          "and":[
            {"EQ_Dto2_attribute2":2},
            {"EQ_Dto2_attribute3":3}
          ]
        }
      ]
    },
    {"NEQ_Dto1_attribute3":3}
  ]
}
```

```
{
  "Dto1":{  // 必须指定一个Dto，in的的条件字段从此Dto获取
    "and":[
      {"EQ_Dto1_attribute1":1},
      {"NEQ_Dto1_attribute2":2},
      {
        "or":[
          {"EQ_Dto2_attribute1":1},  // in子查询中的查询条件可以是非Dto1的字段，见下面解释
          {
            "and":[
              {"EQ_Dto2_attribute2":2},
              {"EQ_Dto2_attribute3":3}
            ]
          }
        ]
      },
      {"NEQ_Dto1_attribute3":3}
    ]
  }
}
解释：In查询的查询条件可以是非Dto1的字段，当出现非Dto1字段时，子查询内部将会变成一个连接查询，如下所示
SELECT
        略
FROM
        略
LEFT JOIN 略
WHERE
        ctp_role.tenant_id = - 1
AND(
        ctp_role.id IN(
                SELECT DISTINCT
                        (ctp_role_resource.role_id)
                FROM
                        ctp_role_resource,ctp_role        //ctp_role_resource和ctp_role将会连接
                WHERE
                        (
```

```
{
  "status": 0,
  "code": "BOOT-0000",
  "message": "SUCCESS",
  "data": {
    "content": {
      "pageInfo": {
        "pageNumber": 1,
        "pageSize": 5,
        "pages": 0,
        "total": 0,
        "needTotal": false
      },
      "content": [
        {
            "code":"userAdmin",
            "createTime":1621057940000,
            "name":"用户管理员",
            "tenantId":"-1",
            "description":"",
            "updateTime":1621313835000,
            "id":"406712268269642752",
            "version":11,
            "ctpUserRoleDtoList":[
    
            ],
            "ctpRoleResourceDtoList":[
                {
                    "resourceId":"406712264679318528",
                    "createTime":1621057940000,
                    "roleId":"406712268269642752",
                    "tenantId":"-1",
                    "updateTime":1621057940000,
                    "id":"406712268705850368",
                    "version":0,
                    "resourceType":"MENU"
```

##### 4、DynamicEntitySelectService服务

###### 4.1 数据查询

```
public PageResponse<Object> dynamicProxySelect(ProxyParamDto param)
```

###### 4.2 条数查询

```
public SingleResponse<Integer> dynamicProxySelectCount(ProxyParamDto param) 
```

###### 4.3 参数说明

```
ProxyParamDto 封装了：PageInfo、Sort、MainConditionDto、DynamicConditionDto
参数和DynamicSelectService 一样
```

##### 5、DynamicAutoJoinSelectService 服务

注意：这个是给udc提供的新的动态查询接口 1、业务自己控制拼接SQL的实体列表 2、业务自己控制distinct操作 3、业务自己控制join方式 4、业务自己控制返回字段 5、和DynamicEntitySelectService、DynamicSelectService不一样，参数中所有属性均是基于 "Entity" 而非 "DTO"

###### 5.1 数据查询

###### 5.2 条数查询

###### 5.3 参数说明

##### 6、DynamicAliasSelectService 服务

注意：这个是给udc提供的新的动态查询接口 1、业务自己控制拼接SQL的实体列表 2、业务自己控制distinct操作 3、业务自己控制join方式 4、业务自己控制返回字段 5、和DynamicEntitySelectService、DynamicSelectService不一样，参数中所有属性均是基于 "Entity" 而非 "DTO" 6、和DynamicAutoJoinSelectService不一样，这个服务参数需要指定表的 "别名"，指定别名之后，查询字段、连接字段、分组、排序、查询条件等，会变成"别名.属性名" （原来是 "表名.属性名"）

###### 6.1 数据查询

###### 6.2 条数查询

###### 6.3 参数说明

##### 7、调用示例
