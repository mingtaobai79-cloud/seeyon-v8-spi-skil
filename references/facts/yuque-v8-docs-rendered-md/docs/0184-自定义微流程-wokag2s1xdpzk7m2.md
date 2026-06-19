---
title: "自定义微流程"
source: "https://www.yuque.com/seeyonkk/v8/wokag2s1xdpzk7m2"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 自定义微流程

> Source: https://www.yuque.com/seeyonkk/v8/wokag2s1xdpzk7m2

作者：杨映海

最后更新：2025-04-07

## 1. 应用场景

标准微流程配置实现不了（事务处理、递归、多层循环、多线程），或业务逻辑复杂配置起来非常繁琐的情况下，使用自定义微流程（后端手写代码）来处理逻辑。

1
场景一：提供业务接口供前端规则、三方系统、跨应用调用

2
场景二：监听平台事件做后续逻辑处理
图片加载失败

3
场景三：定时任务调试

## 2. 实现步骤

操作入口：管理后台-->低代码平台-->UDC应用-->规则

### 2.1 业务接口

#### 2.1.1 接口定义

描述信息:此方法实现将V5的表单结构自动创建为V8的实体结构
幸定时输出应用日
主自定义微流程
接口名
主定时输出日志
组织机构同步
主自定义事(件监听
去定时输出字符串
白默认分组
主测试发布API
创建V5表单实体
触发方式:O服务员
去名
立标准微流程
称:数据迁移
建微流程
*类型:O标
CW基到础I规
属分组:默认分组
2

1、编码默认系统会自动生成（例：MFCUSTOMOpL330），建议按Java代码方法命名规则自定义。

2、所属接口系统默认为：CustomMicroFlowAppService，建议按Java代码类命名规则自定义。

3、接口定义完成之后，需要先执行一次构建，待UDC生成相应接口代码并发布到依赖库后再进行下一步。

#### 2.1.3 接口调用

构建成功并完成上一步操作后，在拉取的扩展代码工程中（参照：UDC扩展代码准备），创建实现类(包名为：com.seeyon.{应用编码}.extend.appservice)

1、实现类头部务必添加 @AppService 、@Transactional注解

##### 2.1.3.1 前端规则调用

<img width="1490.5">

<img width="1481.5">

<img width="1491.5">

##### 2.1.3.2 微流程调用

<img width="1491.5">

<img width="1493.5">

##### 2.1.3.3 OpenApi调用

在需要暴露为OpenApi接口的方法头部添加 @AppServiceOperation 注解,属性说明如下：

value：接口名称

description：接口描述

returnValue：返回值描述

openApi/url：自定义请求path(默认为当前方法名)

<img width="1468.5">

##### 2.1.3.4 跨应用Dubbo接口调用

1、在实现类头部添加 @DubboService 注解

2、调用方必须添加被调用方作为依赖，比如A应用调用B应用暴露的Dubbo接口，必须在A应用中，选择添加应用依赖（A应用->依赖设置->应用依赖->添加B应用） 或在A应用扩展代码工程的POM文件中直接添加B应用作为依赖，如：

<dependency>

    <groupId>com.seeyon</groupId>

    <artifactId>kekaiguanli7996550270124641378-facade</artifactId>

    <version>1.0.110</version>

</dependency>

3、通过@DubboReference 添加Dubbo接口对象

### 2.2 事件监听

<img width="1487.5">

<img width="1472.5">

1、自定义事件监听方法所属接口系统固定为：CustomMicroFlowAppService（不可修改）

2、编码默认系统会自动生成（例：MFCUSTOMOpL330），建议按Java代码方法命名规则自定义。

### 2.3 定时任务

<img width="1481.5">

<img width="1467.5">

1、自定义定时任务方法所属接口系统固定为：CustomMicroFlowAppService（不可修改）。

2、编码默认系统会自动生成（例：MFCUSTOMOpL330），建议按Java代码方法命名规则自定义。
