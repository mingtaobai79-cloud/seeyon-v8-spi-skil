---
title: "UDC接入规范"
source: "https://www.yuque.com/seeyonkk/v8/wt9vwigxca0vl0z5"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# UDC接入规范

> Source: https://www.yuque.com/seeyonkk/v8/wt9vwigxca0vl0z5

# UDC应用接入规范

前提：被UDC创建应用所依赖

## 1. 实体

### 1.1 实体扫描规则

●
设置isPublic = true

○
实体被UDC发现（如：实体-字段类型为实体时选择实体；微流程-实体服务选择实体；）

●
设置sort

○
实体顺序

```java

@EntityInfo(value = "人员", description = "人员", entityType = EntityType.MASTER_ENTITY, isPublic = true, sort = 5)
public class OrgMember extends BaseEntity {
}
```

## 2. Dubbo接口

主要用于微流程

### 2.1 实体服务接口（基于实体的增删改查）

#### 2.1.1 实体服务接口扫描规则

●
按照命名规范过滤

●
必须按照【实体名称】+AppServiceImpl的命名规则，例如实体名称是Person，则接口名称命名为PersonAppService，实现类命名PersonAppServiceImpl，认定为实体服务，否则在其他服务中

●
实体服务中的方法必须按照标准方法名称命名：
create【新增】
createBatch【批量新增】
update【更新】
updateBatch【批量更新】
deleteById【删除】
deleteByIds【批量删除】
selectById【单实体id查询】
selectByIds【单实体批量id查询】
selectCascadeById【聚合查询】
selectCascadeByIds【批量聚合查询】
selectListByConditions【简单条件查询】
selectPageByConditions【简单分页条件查询】
selectCountByConditions【简单总数查询】
selectListByComplexConditions【复杂条件查询-支持or】
selectPageByComplexConditions【复杂分页条件查询-支持or】
selectCountByComplexConditions【复杂总数查询】

●
以上接口中
create createBatch update updateBatch 入参需要是实体对应的DTO
其他查询接口的出参，需要是实体对应的DTO

●
在微流程的”实体服务接口“列表中，只会出现符合微流程命名规范的接口。

#### 2.1.2 接口规范

●
接口必须在facade中定义

●
接口命名、入参类型、返回值类型须按照以下示例规范
特别说明：
a.接口命名：必须按照【实体名称】+AppServiceImpl的命名规则，例如实体名称是Person，则接口名称命名为PersonAppService，实现类命名PersonAppServiceImpl
b.针对需要暴露到实体中的服务
  create：入参必须是实体Entity+Dto的命名规范，例如实体名称为Entity,则该实体的Create方法的入参必须是PersonDto,否则将被当做【其他服务】
      出参必须是Long,代表该次create成功后的实体ID
  createBatch：同上，只是出参调整为Integer，代表插入成功的数量
update：入参必须是实体Entity+Dto的命名规范，例如实体名称为Entity,则该实体的Create方法的入参必须是PersonDto,否则将被当做【其他服务】
      出参必须是Integer,代表该次update成功的数量
  updateBatch：同上，只是出参调整为Integer，代表插入成功的数量

●
接口描述须按照以下示例规范（新增XXX，更新XXX，删除XXX等）1.如果接口存在出参，请在@AppServiceOperation注解中打上returnValue说明，用于描述该接口的出参信息
2.如果接口存在入参，请打上@ParameterInfo注解，用于描述该接口的入参信息

●
以下接口按需实现

#### 2.1.3 Dto规范

●
标注dto对应的实体

●
如果需要对dto数据明确 操作类型（如：dto集合中 1条数据新增，2条数据更新），需要继承 BaseTraceableActionDto。

### 2.2 其他服务接口

#### 2.2.1 实体接口扫描规则

●
在微流程的”其他服务接口“列表中，只会出现非实体服务接口中的并且命名不在实体服务接口范围内的。

#### 2.2.2 接口规范

## 3.Rest接口

主要用于参照查询

### 3.1 rest接口规范

●
接口路径为{appName}/{entityName}

●
支持参照，须继承平台动态SQL基础类AbstractDynamicSelectController实现动态查询，T为实体对应的dto

●
支持graphql的关联查询，须提供id，ids方法
