---
title: "发票服务"
source: "https://www.yuque.com/seeyonkk/v8/dsbmug3v87eqheii"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 发票服务

> Source: https://www.yuque.com/seeyonkk/v8/dsbmug3v87eqheii

作者：陈晓东

时间：2026.1.6

###### 1、使用场景

支持发票识别、发票验真，支持识别单张或多张票据（如增值税专用发票、增值税普通发票(卷式)、火车票，飞机票，汽车票等），支持增值税发票的验真

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
com.seeyon.cip.provider.api.trip.InvoiceProviderService
```

###### 3、接口定义

```
public interface InvoiceProviderService extends ProviderService {

    @CipCapabilityComment("发票单次识别")
    InvoiceOutItemApiDto getInvoicesOcr(InvoiceSingleOcrApiDto singleOcrApiDto) throws BusinessException;

    @CipCapabilityComment("发票批量识别")
    List<InvoiceOutItemApiDto> getInvoicesOcr(InvoiceOcrProviderApiDto invoiceOcrDto) throws BusinessException;

    @CipCapabilityComment("增值税核验(批量核算)")
    InvoiceCheckOutApiDto checkBatchInvoice(InvoiceCheckApiDto invoiceCheckApiDto);

    @CipCapabilityComment("增值税核验(批量核算)" +
            "batchNumber : 发票数目")
    InvoiceCheckOutApiDto batchGetCheck(String batchNumber);

    @CipCapabilityComment("发票核验(单个验真)")
    InvoiceCheckOutItemApiDto singleCheck(InvoiceCheckItemApiDto invoiceCheckItemApiDto);

    @CipCapabilityComment("创建影像任务(慧财支持)")
    default InvoiceImageApiResDto createImageTask(InvoiceImageApiReqDto request) {
        throw new BusinessException(IMPL_NOT_EXIST);
    }

    @CipCapabilityComment("上传附件(慧财支持)")
    default InvoiceImageUploadApiResDto uploadImageFile(InvoiceImageUploadApiReqDto request) {
        throw new BusinessException(IMPL_NOT_EXIST);
    }

    @CipCapabilityComment("图片文件(URl图片)的大小，单位是(M)")
    default int imageFileSize() {
        return 4;
    }

    @CipCapabilityComment("图片文件格式")
    default String imageFormat() {
        return "PNG、JPG、JPEG、BMP";
```

###### 4、示例demo

大象慧云集成

EleCloudInvoiceServiceImpl.java
(28 KB)

###### 5、配置信息

HTTPS://SANDBOX.ELE-CLOUDCOM/API
海之韵DEMO简称
同运营平台
述支持发票识别,发票验真,支
应用通道管理
前通道:大象慧云服务
大象慧云-服务
当前通道未启用
致远互联-服务
::基础能力接入
服务参数配置
基础能力接)
8关闭全部
三方应用集
基础设置
测试-服务
发票服务
日志列表
用量统计
APPKEY
础出信息
开放平台
APPSECRE
未启用
能力配置
切换通道
OCIP
黑默认值
理首页
参数名
APIURL
未启用
票,飞机票,汽车票等),支
ENTCODE
6
编辑
启用
