---
title: "OCR识别"
source: "https://www.yuque.com/seeyonkk/v8/ocr"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# OCR识别

> Source: https://www.yuque.com/seeyonkk/v8/ocr

作者：陈晓东

时间：2026.1.6

###### 1、使用场景

提供对身份证、银行卡、名片、营业执照等规则图片的文本识别能力

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
com.seeyon.cip.provider.api.ocr.OcrProviderService
```

###### 3、接口定义

```
/**
 * Ocr识别接口
 */
public interface OcrProviderService extends ProviderService {
    @CipCapabilityComment("以base64字符和文件ID方式识别" +
            "invokeAppId : 应用模块" +
            "ocrEnum : OCR识别分类" +
            "imageBase64 : Base64编码的图片文件" +
            "storageKey : 文件存储在文件中心的标识")
    default CipBaseResponseData getOcrByBase64(String invokeAppId, OcrCapabilityApiEnum ocrEnum, String imageBase64, String storageKey) {
        throw new BusinessException(IMPL_NOT_EXIST);
    }
    @CipCapabilityComment("以base64字符和文件ID方式识别" +
            "imageBase64 : Base64编码的图片文件" +
            "storageKey : 文件存储在文件中心的标识")
    default OcrCommonResultDto getOcrByBase64(String imageBase64, String storageKey) {
        throw new BusinessException(IMPL_NOT_EXIST);
    }
    @CipCapabilityComment("增值税核验" +
            "invoiceCode：发票代码" +
            "invoiceNo：发票号码" +
            "invoiceDate：发票日期" +
            "additional：附加信息")
    default InvoiceVerificationResponseData verificationInvoice(String invoiceCode, String invoiceNo, String invoiceDate, String additional) {
        throw new BusinessException(IMPL_NOT_EXIST);
    }
    @CipCapabilityComment("自定义模版识别(有的能力提供者无此能力)" +
            "templateCode：模版编码" +
            "imageBase64 ：base64编码的图片文件" +
            "storageKey ：文件存储在文件中心的标识")
    default CipBaseResponseData getOcrByCustom(String invokeAppId, String templateCode, String imageBase64, String storageKey) {
        throw new BusinessException(IMPL_NOT_EXIST);
    }
    @CipCapabilityComment("图片文件(URl图片)的大小，单位是(M)")
    default int imageFileSize() {
        return 4;
```

###### 4、示例demo

腾讯OCR

TencentOcrServiceImpl.java
(7 KB)

###### 5、配置信息

述提供对身份证,银行卡,名片,营业执照等规则图片的文本识别能
协同运营平台海之韵DEMO简
OCR.TENCENTCLOUDAPI.COM
服务参数配置
当前通道:腾讯云-服务
件配置日志列表用
:基础力接入
8关闭全部
应用通道管刊
OCR识别
致远互联-服
基础出能力接)
三方应用集
CLIENTSECRET
测试-服务
百度云-服务
方寸-服务
基础设置
能力配置
CLIENTLD
默认值
开放平台
编辑
腾讯云服务
基础信息
切换通道
理首页
参数名
未启用
APIURL
未启用
OCIP
启用
未启用
当前通道
未启用
未启用
.
O昌
V
