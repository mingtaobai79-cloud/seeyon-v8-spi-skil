---
title: "接口规范"
source: "https://www.yuque.com/seeyonkk/v8/wpinkgn5ggfwmkta"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 接口规范

> Source: https://www.yuque.com/seeyonkk/v8/wpinkgn5ggfwmkta

## 接口规范

1
【强制】对外暴露的接口定义放到应用的facade工程中。facade工程只包含对外暴露的API接口、对外暴露的DTO定义、对外暴露的枚举类。接口实现放到应用的biz工程中。

说明：所有需要提供给其他应用调用的Dubbo接口必须定义在facade工程中，包括：API接口、DTO定义、枚举类、Message类。

2
【强制】仅内部使用的AppService和DTO定义放到应用的biz工程中。

说明：应用开发中有很多appservice层的接口只需要在本服务内部调用。对于这种接口直接再appservice包下面定义具体类即可。

举例：组织模型微服务有一些接口需要提供给其他应用调用，有一些接口则只是内部使用。

```
    - 提供给其他应用调用的接口
        -   需要在facade中定义api接口，例如：com.seeyon.organization.api.OrgAppService。
        -   同时需要在biz中提供相应的实现，例如：com.seeyon.organization.appservice.OrgAppServiceImpl。
    - 只在组织模型微服务内部调用的接口
        - 只需要在biz的appservice包中定义对应的类即可，不需要定义接口。
        - 例如在biz的appservice包中定义MemberAppService或者DepartmentAppService提供相应的Member和Department的操作接口。
```

3
【强制】API的package必须符合com.seeyon.xxx.xxx.api，实现类的package必须符合com.seeyon.xxx.appservice，DTO的package必须符合com.seeyon.xxx.xxx.dto。

说明：其中中间的两节分别对应所属的应用和模块。

4
【强制】API的接口的请求参数和返回类型说明如下。

○
SingleRequest: 单请求对象

○
ListRequest: 列表请求对象

○
PageRequest: 分页请求对象

○
SingleResponse: 单返回对象

○
ListResponse: 列表返回对象

○
PageResponse: 分页返回对象

5
【强制】 DTO只包括属性定义，不允许包括任何的逻辑处理。
