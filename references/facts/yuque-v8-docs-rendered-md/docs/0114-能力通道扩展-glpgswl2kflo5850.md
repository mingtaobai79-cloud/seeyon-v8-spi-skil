---
title: "能力通道扩展"
source: "https://www.yuque.com/seeyonkk/v8/glpgswl2kflo5850"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 能力通道扩展

> Source: https://www.yuque.com/seeyonkk/v8/glpgswl2kflo5850

作者：杨映海
最后更新：2025-04-18

## 1. 应用场景

集成平台预置了28项基础能力，每一项目能力可对通道进行扩展，如果标品的通道不满足要求，项目上可以通过SPI方式进行扩展（如：短信能力 增加阿里云通道）

## 2. 接口说明

| 序号 | 能力名称 | 通道接口 |
| --- | --- | --- |
| 1 | AI | com.seeyon.cip.provider.api.ai.AiProviderService |
| 2 | 短信 | com.seeyon.cip.provider.api.sms.SmsProviderService
com.seeyon.cip.provider.api.sms.SmsSignAutoService
com.seeyon.cip.provider.api.sms.SmsTemplateAutoService |
| 3 | 电子邮件 | com.seeyon.cip.provider.api.email.EmailProviderService |
| 4 | 在线文档 | com.seeyon.cip.provider.api.doc.DocOnlineProviderService
com.seeyon.cip.provider.api.doc.DocFileService |
| 5 | 版式文档 | com.seeyon.cip.provider.api.ofd.OfdProviderService |
| 6 | 智能文档 | com.seeyon.cip.provider.api.missive.IntelligentMissiveProviderService |
| 7 | 简历解析 | com.seeyon.cip.provider.api.resume.ResumeProviderService |
| 8 | OCR识别 | com.seeyon.cip.provider.api.ocr.OcrProviderService |
| 9 | 视频会议 | com.seeyon.cip.provider.api.video.VideoProviderService |
| 10 | 商旅服务 | com.seeyon.cip.provider.api.trip.BusinessTripProviderService |
| 11 | 企业征信 | com.seeyon.cip.provider.api.credit.CreditProviderService |
| 12 | 发票服务 | com.seeyon.cip.provider.api.Invoice.InvoiceProviderService |
| 13 | 物理印章 | com.seeyon.cip.provider.api.physicalseal.PhysicalSealProviderService |
| 14 | 电子签章 | com.seeyon.cip.provider.api.signature.electronic.SignatureProviderService |
| 15 | 翻译服务 | com.seeyon.cip.provider.api.translation.TranslationProviderService |
| 16 | 天气查询 | com.seeyon.cip.provider.api.weather.WeatherProviderService |
| 17 | GIS服务 | com.seeyon.cip.provider.api.gis.GisProviderService |
| 18 | 地理位置 | com.seeyon.cip.provider.api.location.LocationProviderService |
| 19 | 离线消息 | com.seeyon.cip.provider.api.message.OfflineMessageProviderService |
| 20 | 标签打印 | com.seeyon.cip.provider.api.print.label.LabelPrintProviderService |
| 21 | 银企直连 | com.seeyon.cip.provider.api.bankpay.BankpayProviderService |
| 22 | 全文检索 | com.seeyon.cip.provider.api.search.SearchProviderService |
| 23 | 语音技术 | com.seeyon.cip.provider.api.voice.VoiceProviderService |
| 24 | 移动日程 | com.seeyon.cip.provider.api.schedule.ScheduleProviderService |
| 25 | 档案系统 | com.seeyon.cip.provider.api.archives.ArchivesProviderService |
| 26 | 人脸识别 | com.seeyon.cip.provider.api.faceid.FaceIdProviderService |
| 27 | 敏感词 | com.seeyon.cip.provider.api.censor.CensorProviderService |
| 28 | 在线支付 | com.seeyon.cip.provider.api.pay.PayProviderService |

## 3.接口实现

spi代码仓库获取及工程初始化请参考：
开发准备
。以下是

注意：完成接口开发并构建成功后需要重启【cip-capability】服务才能进行后续功能验证

## 4、能力配置

操作入口：系统后台-集成平台-基础能力接入-->能力配置

<img width="2130.000056425732">
