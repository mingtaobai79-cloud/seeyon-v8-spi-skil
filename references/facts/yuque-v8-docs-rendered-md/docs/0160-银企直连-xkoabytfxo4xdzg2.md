---
title: "银企直连"
source: "https://www.yuque.com/seeyonkk/v8/xkoabytfxo4xdzg2"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 银企直连

> Source: https://www.yuque.com/seeyonkk/v8/xkoabytfxo4xdzg2

###### 1、使用场景

通过互联网专线或者前置机模式，建立起企业与银行系统间的安全支付通道，企业无需专门登录网上银行，就可以完成支付、转账、资金归集及银行对账单等功能

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
com.seeyon.cip.provider.api.bankpay.BankpayProviderService
```

###### 3、接口定义

```
public interface BankpayProviderService extends ProviderService {

    @CipCapabilityComment("查询余额")
    default BalanceQueryRespDto balanceQuery(BalanceQueryReqDto balanceQueryReqDto) {
        return null;
    }

    @CipCapabilityComment("转账")
    default PaymentTransferRespDto paymentTransfer(PaymentTransferReqDto balanceQueryReqDto) {
        return null;
    }

    @CipCapabilityComment("查询账户明细信息")
    default PageData<AccountDetailRespDto> accountDetail(AccountDetailReqDto dto, PageInfo pageInfo) {
        return null;
    }

    @CipCapabilityComment("账户明细概要信息查询")
    default PageData<AccountSummaryRespDto> accountSummary(AccountDetailReqDto dto, PageInfo pageInfo) {
        return null;
    }

    @CipCapabilityComment("用户明细详细信息查询")
    AccountInDetailRespDto accountInDetail(AccountInDetailReqDto dto);

    @CipCapabilityComment("财务报销")
    default ExpenseRespDto expensesFinance(ExpenseReqDto dto) {
        return null;
    }

    @CipCapabilityComment("城市代码对照表下载")
    default List<CityCodeComparisonTableDownloadRespDto> cityCodeComparisonTableDownload(CityCodeComparisonTableDownloadReqDto dto){return null;}

    @CipCapabilityComment("货币代码对照表下载")
    default List<CurrencyCodeComparisonTableDownloadRespDto>  currencyCodeComparisonTableDownload(CurrencyCodeComparisonTableDownloadReqDto dto) {
        return null;
```

###### 4、示例demo

CiticBankpayProviderServiceImpl.java
(33 KB)

###### 5、配置信息

术通过互联网专线域者前置机模式,建立起企业与银行系统间的安全支付通道,企业无需专门登录网上
服务参数配置
海之韵DEMO简称
应用通道管理
豆开放平台
日志列表用量统
协同运营平台
三方应用集成
当前通道:银企直连
:基础能力接入
基础出能力接入
银企直连
盛基础设置
能力配置
8关闭全部
基础信息
管理首页
启用
...-.AMEHE心击+据造企业无需专门登录网上银行,就可以完成支付,转账,资金日果仅球内手
默认值
SOCIP
APIURL
参数名
编辑
O昌
日
人
