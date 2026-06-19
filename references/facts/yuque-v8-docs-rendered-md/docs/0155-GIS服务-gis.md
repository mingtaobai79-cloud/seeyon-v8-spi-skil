---
title: "GIS服务"
source: "https://www.yuque.com/seeyonkk/v8/gis"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# GIS服务

> Source: https://www.yuque.com/seeyonkk/v8/gis

作者：陈晓东

时间：2026.1.8

###### 1、使用场景

提供全国各省市地区天气查询的能力

###### 2、操作步骤

SPI开发规则，参考：
开发准备

1、SPI工程中加入maven依赖

```xml
<dependency>
    <groupId>com.seeyon</groupId>
    <artifactId>cip-connector-api</artifactId>
    <version>${platform.version}</version>
</dependency>
```

2、实现SPI接口

```
com.seeyon.cip.provider.api.gis.GisProviderService
```

###### 3、接口定义

```
public interface GisProviderService extends ProviderService {

    @CipCapabilityComment("获取能力类型")
    default CapabilityEnum getCapabilityEnum() {
        return CapabilityEnum.Gis;
    }

    @CipCapabilityComment("获取token")
    String getToken(GisTokenRequestDto gisTokenRequestDto);
}
```

###### 4、示例demo

SnkoudaiGisProviderServiceImpl.java
(5 KB)

###### 5、配置信息

二三维一体化GIS数据和引擎服务,应用于智慧城市,智慧农业,智慧
述:GIS专网地图服务,提供二三维
海之韵DEMO简称
上海测绘-服务
前通道:上海测绘-服务
协同运营平台
:基础能力接人
基础出能力接)
左岸芯慧-服务
三方应用集成
默认值
服务参数配置
8关闭全部
基础设置
应用通道管理
PASSWORD
用量统计
GIS服务
理首页
USERNAME
开放平台
换通道
能力配置
OCIP
础出信
参数名
日志列表
未启用
未启用
APIURL
62
编辑
V
