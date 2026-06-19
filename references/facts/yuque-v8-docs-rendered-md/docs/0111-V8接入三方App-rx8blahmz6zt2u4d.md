---
title: "V8接入三方App"
source: "https://www.yuque.com/seeyonkk/v8/rx8blahmz6zt2u4d"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# V8接入三方App

> Source: https://www.yuque.com/seeyonkk/v8/rx8blahmz6zt2u4d

作者：杨映海
最后更新：2025-05-07

## 1. 应用场景

V8平台H5应用接入三方APP工作台中，例如企业微信、钉钉、飞书等

## 2. 接口说明

1、基础配置：com.seeyon.cip.connector.api.mobile.MobileConfigProviderService 

2、应用功能：com.seeyon.cip.connector.api.mobile.MobileApplicationProviderService

3.1、组织同步-批量推送：com.seeyon.cip.connector.api.mobile.MobileOrgSyncBatchProviderService

3.2、组织同步-单个推送：com.seeyon.cip.connector.api.mobile.MobileOrgSyncProviderService 

3.3、组织同步-拉取：com.seeyon.cip.connector.api.mobile.MobileOrgSyncPullProviderService 

4.1、待办处理：com.seeyon.cip.connector.api.mobile.MobileTodoProviderService 

4.2、回调通知：com.seeyon.cip.connector.api.mobile.MobileCallBackProviderService

## 3.接口实现

spi代码仓库获取及工程初始化请参考：
开发准备

注意：完成接口开发并构建成功后需要重启【cip-connector】服务才能进行后续功能验证

## 4.参数配置

<img width="1489.5">
