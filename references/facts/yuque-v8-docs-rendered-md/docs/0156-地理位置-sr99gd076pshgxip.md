---
title: "地理位置"
source: "https://www.yuque.com/seeyonkk/v8/sr99gd076pshgxip"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 地理位置

> Source: https://www.yuque.com/seeyonkk/v8/sr99gd076pshgxip

作者：陈晓东

时间：2026.1.8

###### 1、使用场景

提供行政区划查询、地理编码查询、测距等地理位置能力

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
com.seeyon.cip.provider.api.location.LocationProviderService
```

###### 3、接口定义

```
public interface LocationProviderService extends ProviderService {

    @CipCapabilityComment("获取定位")
    String getLocation();

    @CipCapabilityComment("行政区划查询")
    List<DistrictsDto> regionSearch(RegionDto regionDto);

    @CipCapabilityComment("查询jsKey")
    JsApiDto getJsApiInfo();

    @CipCapabilityComment("地理信息查询")
    GeocoderResultDto geocoding(GeocoderRequestDto dto);

    @CipCapabilityComment("关键字查询")
    default List<SearchResultDto> keywordSearch(KeywordSearchDto keywordSearchDto) {
        return null;
    }

    @CipCapabilityComment("周边搜索查询")
    default List<SearchResultDto> aroundSearch(AroundSearchDto aroundSearchDto) {
        return null;
    }

    @CipCapabilityComment("获取能力类型")
    default CapabilityEnum getCapabilityEnum() {
        return CapabilityEnum.Location;
    }
}
```

###### 4、示例demo

GaoDeLocationProviderServiceImpl.java
(11 KB)

###### 5、配置信息

提供行政区划查询,地理编码查询,测距等地理
HTTPS:/RESTAPI.AMAPCOM/V3
当前通道:高德位置-服务
海之韵DEMO简称
基础能力接)
日志列表用量
三方应用集成
服务参数配置
:基础能力接入
8关闭全部
应用通道管
基仙出设置
协同运营平台
地理位置
开放平台
JSCODE
切换通道
力配置
基础信息
参数名
理首页
启用
EOASI0E
JISKEY
编辑
APIURL
默认值
OCLP
KEY
目
