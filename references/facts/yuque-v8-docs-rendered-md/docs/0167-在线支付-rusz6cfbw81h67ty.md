---
title: "在线支付"
source: "https://www.yuque.com/seeyonkk/v8/rusz6cfbw81h67ty"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 在线支付

> Source: https://www.yuque.com/seeyonkk/v8/rusz6cfbw81h67ty

###### 1、使用场景

提供各种在线支付服务

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
com.seeyon.cip.provider.api.pay.PayProviderService
```

###### 3、接口定义

```
public interface PayProviderService extends ProviderService {
    @Override
    @CipCapabilityComment("获取能力类型")
    default CapabilityEnum getCapabilityEnum() {
        return CapabilityEnum.Pay;
    }

    @CipCapabilityComment("h5下单")
    H5PayOrderResultDto h5Pay(H5PayOrderParamsDto dto);

    @CipCapabilityComment("商户订单号查询")
    TransactionResultDto queryTransactionByOutTradeNo(TransactionParamsDto dto);

    @CipCapabilityComment("关闭订单")
    void closeTransaction(TransactionParamsDto dto);

    @CipCapabilityComment("申请退款")
    RefundResultDto refund(RefundParamsDto dto);

    @CipCapabilityComment("商户退款订单查询")
    QueryRefundResultDto queryRefund(QueryRefundParamsDto dto);

    @CipCapabilityComment("申请交易账单")
    BillDownloadResultDto downloadTradeBill(BillDownloadParamsDto dto);

    @CipCapabilityComment("申请资金账单")
    BillDownloadResultDto downloadFundFlowBill(BillDownloadParamsDto dto);

    @CipCapabilityComment("查询平台证书")
    List<CertificateDto> getCert(CertificateReqDto certificateReqDto);
}
```

###### 4、示例demo

WeixinPayServiceImpl.java
(27 KB)

###### 5、配置信息

协同运营平台海之韵DEMO简称
理首页:基础能力接)
BA51200060120G
基础设置
述提供各种在线支付服
当前通道:微信支付
路三方应用集成
SOCP
服务参数配置
商户管理日志列表
基础出能力接入
<在线支付
NOTIFYURL
应用通道管理
8关闭全部
授权配置O
豆开放平台
表用量统计
能力配置
基础出信息
参数名
默认值
编辑
启用
02
:
