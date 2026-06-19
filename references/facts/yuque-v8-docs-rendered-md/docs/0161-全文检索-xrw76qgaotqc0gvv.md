---
title: "全文检索"
source: "https://www.yuque.com/seeyonkk/v8/xrw76qgaotqc0gvv"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 全文检索

> Source: https://www.yuque.com/seeyonkk/v8/xrw76qgaotqc0gvv

###### 1、使用场景

全文检索

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
com.seeyon.cip.provider.api.search.SearchProviderService
```

###### 3、接口定义

```
public interface SearchProviderService extends ProviderService {

    @CipCapabilityComment("获取全文检索结果地址")
    QuerySearchApiResDto querySearchUrl(QuerySearchApiReqDto apiReqDto);

    @CipCapabilityComment("获取能力类型")
    default CapabilityEnum getCapabilityEnum() {
        return CapabilityEnum.Search;
    }

}
```

###### 4、demo示例

V5SearchServiceImpl.java
(6 KB)

###### 5、配置信息

述:提供全文检索能力
当前通道:测试服务
海之韵DEMO简称
协同运营平台
全文检索
日志列表用量统
服务参数配置
基础能力接入
路三方应用集成
基础设置
应用通道管理
豆开放平台
8关全部
能力配置
启用
暂无数据
:基础出能力接入
OCIP
切换通道
基础信息
理首页
黑默认值
0吕
参数名
目
目机
人
