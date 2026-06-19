---
title: "Rest规范"
source: "https://www.yuque.com/seeyonkk/v8/lkrzaod5edg33r8k"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# Rest规范

> Source: https://www.yuque.com/seeyonkk/v8/lkrzaod5edg33r8k

## Rest规范

### HTTP请求方式

只支持GET和POST

```
  - R(Retrieve)使用GET，CUD(create,update,delete)使用POST。
  - 本应该是获取数据的接口，如果请求参数等于或超过3个，应使用POST。
```

允许使用动词参数描述update,delete以代替PUT、DELETE，其它请使用名词，如

```
  - GET  member/{id}（获取）
  - POST member（新增）
  - POST member/update（修改）
  - POST member/delete（删除）
```

### URL路径规则

```
  http://127.0.0.1/organization/member/v2/{id}
    - organization 服务名称
    - member 实体名称
    - v2 版本号
```

●
版本号通过注解@ApiVersion在Controller中进行定义，如果不定义永远保持最新版本，如果请求中不指定api版本号则返回最新版本。

●
名词对应数据库中的表。

●
URL结尾不应该包含斜杠“/”。

●
”/“必须用来指示层级关系。

●
URL命名规则使用脊柱命名法，使用连接符”-“来提高URL的可读性。

○
驼峰命名法和蛇形命名法（使用下划线”_”）都会涉及到输入法的切换，在实际情况中确实会增加操作的复杂性。

●
URL统一使用小写字母。

示例：

| method | api | 接口描述 |
| --- | --- | --- |
| GET | collaboration/{id} | 获取协同 |
| POST | collaboration | 新建协同 |
| POST | collaboration/update | 修改协同 |
| POST | collaboration/delete | 删除协同 |
| POST | collaboration/search | 搜索协同 |
| GET | collaboration/{id}/opinions | 获取协同意见列表 |
| POST | collaboration/opinion | 新建协同意见 |
| POST | collaboration/opinion/update | 修改协同意见 |
| POST | collaboration/opinion/delete | 删除协同意见 |

### 响应格式说明

●
返回结果：

```
{
  "status": 0,
  "code": "BOOT-0000",
  "message": "SUCCESS",
  "data": {
    "content": "69419779910270992"
  }
}
```

●
返回参数说明：

| 参数 | 说明 |
| --- | --- |
| status | 状态，成功返回“0”，处理中返回“-1”，失败会返回对应的状态码。 |
| code | 错误码，如：BOOT-1001为参数错误。 |
| message | 返回信息，包括接口请求发生错误时的详细信息。 |
| data | 返回数据。 |

●
状态码说明

| 状态码 | 说明 |
| --- | --- |
| -1 | 处理中 |
| 0 | 成功 |
| 1 | 请求参数异常 |
| 2 | 业务异常 |
| 3 | 未知异常 |

### 框架统一处理类型

●
Long输出为字符串。

●
Date输出为长整型值。

●
Enum输出为Json格式。
