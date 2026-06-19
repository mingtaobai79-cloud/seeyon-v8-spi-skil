---
title: "V8单点到三方"
source: "https://www.yuque.com/seeyonkk/v8/v8-cip-connector-api-ssoservice"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# V8单点到三方

> Source: https://www.yuque.com/seeyonkk/v8/v8-cip-connector-api-ssoservice

作者：张宇
最后更新：2025-03-25

## 1. 应用场景

从V8平台菜单、磁贴等方式跳转到第三方系统

从V8三方数据栏目，点击[更多]跳转到第三方系统具体功能

v8集成三方待办数据后，点击待办可以跳转到三方系统待办详情页，点击栏目[更多]跳转到三方待办列表

定义新增单点登录标识和名称
根据传入参数拼接单点登录地址
METHOD:GETTYPECAPTION0
METHODGETPAGEJSON
获取调用方传入的扩展渗数
获取可视化置参数值
PARAMSEXTENDPARAMS
PARAMS:CLIENTTYPE
定义其他可视化配置参数
获取传入的目标地址
METHOD:LOGIN0
PARAMS:USERMLAP
定义英文标识
服务内部逻辑
获取调用终端类型
METHOD:GETNAME0
PARAMSJSON
定义中文名称
获取用户映射数据
非心必要步骚
PARAMS.URL
必要步骚
开始
结束

## 2.接口说明

接口名称：com.seeyon.cip.connector.api.sso.SsoService

```xml
<dependency>
    <groupId>com.seeyon</groupId>
    <artifactId>cip-connector-api</artifactId>
    <!-- 请以实际环境的依赖版本号为准-->
    <version>3.8.211</version>
</dependency>
```

## 3 接口实现

spi代码仓库获取及工程初始化请参考：
开发准备

注意：完成接口开发并构建成功后需要重启【cip-connector】服务才能进行后续功能验证

## 4 配置说明

本章节以cip-connector-sso-alpha项目为例，详细说明单点登录服务的具体实现方法。

### 4.1 创建集成应用

<img width="1064">

### 4.2 单点登录设置

<img width="1894">

### 4.3 配置菜单

<img width="1920">

### 4.4 发布应用

<img width="1129">

### 4.5 角色授权

<img width="1906">

## 5 实现效果

### 5.1 通过菜单跳转

<img width="1911">

### 5.2 通过磁贴跳转

<img width="1916">

### 5.3 流程模版跳转

<img width="1893">

### 5.4 待办信息跳转

<img width="1897">

<img width="1894">

<img width="1916">

## 6 示例代码

spi-sso-bi.zip
(22 KB)
