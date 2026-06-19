---
title: "商旅服务"
source: "https://www.yuque.com/seeyonkk/v8/shortl2okuort02z"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 商旅服务

> Source: https://www.yuque.com/seeyonkk/v8/shortl2okuort02z

作者：陈晓东

时间：2026.1.6

###### 1、使用场景

针对企业差旅场景，提供差旅审批单同步、机票预订、火车票购买、酒店预订、用车的能力

###### 2、操作步骤

SPI开发规则，参考：
开发准备

1、工程中加入maven依赖

```xml
<dependency>
    <groupId>com.seeyon</groupId>
    <artifactId>cip-connector-api</artifactId>
    <version>${platform.version}</version>
</dependency>
```

2、实现SPI接口

```
com.seeyon.cip.provider.api.trip.BusinessTripProviderService
```

###### 3、接口定义

```

public interface BusinessTripProviderService extends ProviderService, CipCallbackProviderService {

    @CipCapabilityComment("获取能力类型")
    default CapabilityEnum getCapabilityEnum() {
        return CapabilityEnum.BusinessTrip;
    }

    @CipCapabilityComment("部门同步")
    void departmentSync(TripDeptSyncRequestDto tripDeptSyncRequestDto);

    @CipCapabilityComment("人员同步")
    void isvUserSync(TripUserSyncRequestDto tripUserSyncRequestDto);

    @CipCapabilityComment("跳转预订行程页面")
    String addressGetBook(TripAddressGetBookRequestDto tripAddressGetBookRequestDto);

    @CipCapabilityComment("跳转查看订单页面")
    String addressGetOrder(TripAddressGetOrderRequestDto tripAddressGetOrderRequestDto);

    @CipCapabilityComment("跳转后台管理页面")
    String addressGetManager(TripAddressGetManagerRequestDto tripAddressGetManagerRequestDto);

    @CipCapabilityComment("跳转H5首页")
    String addressGetH5(TripAddressGetH5RequestDto tripAddressGetH5RequestDto);

    @CipCapabilityComment("成本中心查询")
    TripCostCenterQueryResponseDto costCenterQuery(TripCostCenterQueryRequestDto tripCostCenterQueryRequestDto);

    @CipCapabilityComment("发票查询")
    TripInvoiceQueryResponseDto invoiceSearch(TripInvoiceQueryRequestDto tripInvoiceQueryRequestDto);

    @CipCapabilityComment("新增出差审批单")
    TripApplyAddResponseDto applyAdd(TripApplyAddRequestDto tripApplyAddRequestDto);

    @CipCapabilityComment("修改出差审批单状态")
```

###### 4、示例demo

携程商旅

BusinessTripProviderServiceImpl.java
(31 KB)

###### 5、配置信息

供差旅审批单同步,机票预订,火车票购买,酒店预订,用车的能
协同运营平台海之韵DEMO简
描述针对企业差旅场景,提供差旅审批单
BTRIPOPEN.ALIYUNCS.CO
商旅服务
日志列表用量统
当前通道:阿里商旅
基础出能力接)
豆开放平台
应用通道管理
服务参数配置
三方应用集
:基础能力接入
8关闭全部
事件配置
OCIP
PROXYCORPLD
APIURL
能力配置
APPSECRE
基础设置
参数名
基础出信息
APPKEY
黑默认值
用量统计
理首页
人
