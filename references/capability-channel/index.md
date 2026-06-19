# 能力通道扩展 SPI 域

> 本目录覆盖集成平台 28 项基础能力的通道扩展。  
> 入口只做导航；不沉淀版本总账，不按每个 jar 版本堆 `contract-facts-*`。目标版本由用户提供 jar/source 时再 FACT 化并回填目标能力文件夹。

## 目录结构

```text
capability-channel/
├── index.md                    ← 本文件（纯导航）
├── shared/                     ← 共享规则/标准方法
├── ai/
├── sms/
├── email/
├── doc-online/
├── ofd/
├── intelligent-missive/
├── resume/
├── ocr/
├── video/
├── business-trip/
├── credit/
├── invoice/
├── physical-seal/
├── electronic-signature/
├── translation/
├── weather/
├── gis/
├── location/
├── offline-message/
├── label-print/
├── bankpay/
├── search/
├── voice/
├── schedule/
├── archives/
├── faceid/
├── censor/
├── pay/
```

## 28 项能力文件夹索引

| 序号 | 能力文件夹 | 当前接口 FQCN | Scope | 重启服务 |
|------|------------|---------------|-------|----------|
| 1 | [AI](ai/README.md) | `com.seeyon.cip.provider.api.ai.AiProviderService` | cip-capability | cip-capability |
| 2 | [短信](sms/README.md) | `com.seeyon.cip.provider.api.sms.SmsProviderService` | cip-capability | cip-capability |
| 3 | [电子邮件](email/README.md) | `com.seeyon.cip.provider.api.email.EmailProviderService` | cip-capability | cip-capability |
| 4 | [在线文档](doc-online/README.md) | `com.seeyon.cip.provider.api.doc.DocOnlineProviderService` | cip-capability | cip-capability |
| 5 | [版式文档](ofd/README.md) | `com.seeyon.cip.provider.api.ofd.OfdProviderService` | cip-capability | cip-capability |
| 6 | [智能文档](intelligent-missive/README.md) | `com.seeyon.cip.provider.api.missive.IntelligentMissiveProviderService` | cip-capability | cip-capability |
| 7 | [简历解析](resume/README.md) | `com.seeyon.cip.provider.api.resume.ResumeProviderService` | cip-capability | cip-capability |
| 8 | [OCR 识别](ocr/README.md) | `com.seeyon.cip.provider.api.ocr.OcrProviderService` | cip-capability | cip-capability |
| 9 | [视频会议](video/README.md) | `com.seeyon.cip.provider.api.video.VideoProviderService` | cip-capability | cip-capability |
| 10 | [商旅服务](business-trip/README.md) | `com.seeyon.cip.provider.api.trip.BusinessTripProviderService` | cip-capability | cip-capability |
| 11 | [企业征信](credit/README.md) | `com.seeyon.cip.provider.api.credit.CreditProviderService` | cip-capability | cip-capability |
| 12 | [发票服务](invoice/README.md) | `com.seeyon.cip.provider.api.Invoice.InvoiceProviderService` | cip-capability | cip-capability |
| 13 | [物理印章](physical-seal/README.md) | `com.seeyon.cip.provider.api.physicalseal.PhysicalSealProviderService` | cip-capability | cip-capability |
| 14 | [电子签章](electronic-signature/README.md) | `com.seeyon.cip.provider.api.signature.electronic.SignatureProviderService` | cip-capability | cip-capability |
| 15 | [翻译服务](translation/README.md) | `com.seeyon.cip.provider.api.translation.TranslationProviderService` | cip-capability | cip-capability |
| 16 | [天气查询](weather/README.md) | `com.seeyon.cip.provider.api.weather.WeatherProviderService` | cip-capability | cip-capability |
| 17 | [GIS 服务](gis/README.md) | `com.seeyon.cip.provider.api.gis.GisProviderService` | cip-capability | cip-capability |
| 18 | [地理位置](location/README.md) | `com.seeyon.cip.provider.api.location.LocationProviderService` | cip-capability | cip-capability |
| 19 | [离线消息](offline-message/README.md) | `com.seeyon.cip.provider.api.message.OfflineMessageProviderService` | cip-capability | cip-capability |
| 20 | [标签打印](label-print/README.md) | `com.seeyon.cip.provider.api.print.label.LabelPrintProviderService` | cip-capability | cip-capability |
| 21 | [银企直连](bankpay/README.md) | `com.seeyon.cip.provider.api.bankpay.BankpayProviderService` | cip-capability | cip-capability |
| 22 | [全文检索](search/README.md) | `com.seeyon.cip.provider.api.search.SearchProviderService` | cip-capability | cip-capability |
| 23 | [语音技术](voice/README.md) | `com.seeyon.cip.provider.api.voice.VoiceProviderService` | cip-capability | cip-capability |
| 24 | [移动日程](schedule/README.md) | `com.seeyon.cip.provider.api.schedule.ScheduleProviderService` | cip-capability | cip-capability |
| 25 | [档案系统](archives/README.md) | `com.seeyon.cip.provider.api.archives.ArchivesProviderService` | cip-capability | cip-capability |
| 26 | [人脸识别](faceid/README.md) | `com.seeyon.cip.provider.api.faceid.FaceIdProviderService` | cip-capability | cip-capability |
| 27 | [敏感词](censor/README.md) | `com.seeyon.cip.provider.api.censor.CensorProviderService` | cip-capability | cip-capability |
| 28 | [在线支付](pay/README.md) | `com.seeyon.cip.provider.api.pay.PayProviderService` | cip-capability | cip-capability |

## 标准方法

每个能力文件夹只保留该能力的可生成模板：

```text
{capability-name}/
├── README.md              ← 场景、接口定义、方法表格、代码骨架、注册与部署
└── constraints.md         ← 该能力独有约束、索取清单、禁止项
```

生成或更新时遵循：

1. 先定位 28 项能力文件夹之一。
2. 若用户只问模板，读取该能力 `README.md` + `constraints.md`。
3. 若用户给实际 jar/source 或指定目标版本，先从该 artifact 抽取 FACT：接口 FQCN、方法签名、DTO、枚举、required/default。
4. 只更新受影响的能力文件夹；不要为每个版本长期保存一份全量总账。
5. 临时反编译产物属于过程材料，不进入 active skill；稳定结论才回填到对应能力文档。
6. 生成工程前读取 `references/spi-domain-constraints.md` 和 `references/platform-standard-library/index.md`。
7. 生成后运行 `references/generation/tools/validate_generated_spi_project.py`。

## 公共方法双查规则

生成、改造或标注 SPI 方法时必须同时查询两类来源：

1. 子域契约：本目录对应 SPI 的 `README.md` / `constraints.md` / `shared/*contract*`，只用于接口 FQCN、SPI 方法签名、DTO、枚举、scope、spring.factories。
2. 平台公共方法：`references/platform-standard-library/index.md` 和 `references/platform-standard-library/decompiled/`，用于 boot-core / boot-starter-web / boot-starter-spi 的 JSON、HTTP、加密、BeanCopy、Transport Response/Request、RequestContext、BusinessException 等公共能力。

规则：凡是代码中要使用或标注公共 helper / Response / Request / 工具类方法，先查平台标准库；凡是 SPI 接口与 DTO，先查本子域契约。两边都查完再生成，禁止把平台公共类型误报成子域缺口，也禁止把子域契约包提升为全局公共方法。

## Evidence 口径

当前 28 项能力文档基于 `cip-capability-api-5.5.147.jar` 做过一次 FACT 回填；这只是当前模板基线，不代表所有现场版本。  
现场指定新版本时，以现场 jar/source 为准，局部更新对应能力文档。

## 索取清单

```text
P0:
1. 要扩展哪一个能力通道（28 选 N）
2. 目标 V8 / cip-capability-api 版本，或直接提供 jar/source
3. 通道 code / description / 配置参数字段
4. 供应商 SDK 或 HTTP API 示例

P1:
5. 平台页面“能力配置”参数字段
6. 示例实现和 spring.factories（如有）
7. 错误码、超时、重试、回调、幂等策略
```
