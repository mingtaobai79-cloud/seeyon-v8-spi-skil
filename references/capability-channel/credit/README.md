# 企业征信能力通道 — SPI 接口完整定义

> **Evidence: FACT ✅** — 接口签名来自 `cip-capability-api-5.5.147.jar` CFR 反编译。  
> 当前模板基线：`cip-capability-api-5.5.147.jar`；现场指定新版本时，以现场 jar/source 重新 FACT 化并局部更新。

## 场景

扩展企业征信、工商、司法、税务、知识产权等查询通道。

## 接口

```java
public interface CreditProviderService
public EnterpriseInfoResponseData getEnterpriseInfo(Integer var1, String var2);
public EnterpriseBasicBusinessInfoResponseData getBasicBusinessInfo(String var1);
public EnterpriseBasicInfoDto getBasicInfo(CreditRequestDto var1);
public EnterprisePartnersDto getPartners(CreditRequestDto var1);
public EnterpriseCourtNoticeDto getCourtNotice(CreditRequestDto var1);
default public CapabilityEnum getCapabilityEnum() {
public EnterpriseCaseDetailDto getCaseDetailList(CreditRequestDto var1);
public EnterpriseAdminPunishDto getAdminPunish(CreditRequestDto var1);
public EnterpriseEnvpDto getEnvp(CreditRequestDto var1);
public EnterpriseEnvpDetailDto getEnvpDetail(CreditRequestDto var1);
public EnterpriseBiddingDto getBiddingList(CreditRequestDto var1);
public EnterpriseBiddingDetailDto getBiddingDetail(CreditRequestDto var1);
public EnterpriseAdministrativeLicenseDto getAdministrativeLicenseList(CreditRequestDto var1);
public EnterpriseEntCreditRatingDto getEntCreditRating(CreditRequestDto var1);
public List<EnterpriseTaxpayerDto> getTaxpayerList(CreditRequestDto var1);
public EnterpriseTrademarkDto getTrademark(CreditRequestDto var1);
public EnterpriseTrademarkDetailDto getTrademarkDetail(CreditRequestDto var1);
public EnterprisePatentDto getPatentList(CreditRequestDto var1);
public EnterprisePatentDetailDto getPatentDetail(CreditRequestDto var1);
public EnterpriseCopyrightSoftDto getCopyrightSoft(CreditRequestDto var1);
public EnterpriseCertificateDto getCertificate(CreditRequestDto var1);
public EnterpriseProjectDto getProject(CreditRequestDto var1);
public EnterpriseFinancingDto getFinancing(CreditRequestDto var1);
default public EnterpriseShellEntInfoDto getShellEntInfoByName(CreditRequestDto dto) {
default public EntJusticeScoreDto getEntJusticeScore(CreditRequestExtendDto dto) {
```

## 基接口：ProviderService

所有能力通道接口均继承或遵循 `com.seeyon.cip.provider.api.ProviderService`：

```java
public interface ProviderService {
    String getDescription();
    CapabilityEnum getCapabilityEnum();
    String getChannelCode();
}
```

## 方法说明

| 方法 | 参数 | 返回 | 类型 |
|------|------|------|------|
| getEnterpriseInfo | `Integer var1, String var2` | `EnterpriseInfoResponseData` | required |
| getBasicBusinessInfo | `String var1` | `EnterpriseBasicBusinessInfoResponseData` | required |
| getBasicInfo | `CreditRequestDto var1` | `EnterpriseBasicInfoDto` | required |
| getPartners | `CreditRequestDto var1` | `EnterprisePartnersDto` | required |
| getCourtNotice | `CreditRequestDto var1` | `EnterpriseCourtNoticeDto` | required |
| getCapabilityEnum | `无` | `CapabilityEnum` | default |
| getCaseDetailList | `CreditRequestDto var1` | `EnterpriseCaseDetailDto` | required |
| getAdminPunish | `CreditRequestDto var1` | `EnterpriseAdminPunishDto` | required |
| getEnvp | `CreditRequestDto var1` | `EnterpriseEnvpDto` | required |
| getEnvpDetail | `CreditRequestDto var1` | `EnterpriseEnvpDetailDto` | required |
| getBiddingList | `CreditRequestDto var1` | `EnterpriseBiddingDto` | required |
| getBiddingDetail | `CreditRequestDto var1` | `EnterpriseBiddingDetailDto` | required |
| getAdministrativeLicenseList | `CreditRequestDto var1` | `EnterpriseAdministrativeLicenseDto` | required |
| getEntCreditRating | `CreditRequestDto var1` | `EnterpriseEntCreditRatingDto` | required |
| getTaxpayerList | `CreditRequestDto var1` | `List<EnterpriseTaxpayerDto>` | required |
| getTrademark | `CreditRequestDto var1` | `EnterpriseTrademarkDto` | required |
| getTrademarkDetail | `CreditRequestDto var1` | `EnterpriseTrademarkDetailDto` | required |
| getPatentList | `CreditRequestDto var1` | `EnterprisePatentDto` | required |
| getPatentDetail | `CreditRequestDto var1` | `EnterprisePatentDetailDto` | required |
| getCopyrightSoft | `CreditRequestDto var1` | `EnterpriseCopyrightSoftDto` | required |
| getCertificate | `CreditRequestDto var1` | `EnterpriseCertificateDto` | required |
| getProject | `CreditRequestDto var1` | `EnterpriseProjectDto` | required |
| getFinancing | `CreditRequestDto var1` | `EnterpriseFinancingDto` | required |
| getShellEntInfoByName | `CreditRequestDto dto` | `EnterpriseShellEntInfoDto` | default |
| getEntJusticeScore | `CreditRequestExtendDto dto` | `EntJusticeScoreDto` | default |

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>cip-capability-api</artifactId>
  <version>${cip-capability-api.version}</version>
</dependency>
```

已 FACT 版本：`5.5.147`。父 POM 平台版本、boot starter 版本、SPI 契约包版本必须分别参数化。

## spring.factories

```properties
com.seeyon.cip.provider.api.credit.CreditProviderService=com.seeyon.extend.spi.capability.CustomCreditProviderService
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["cip-capability"]
}
```

## 重启服务

cip-capability

## 代码骨架

```java
package com.seeyon.extend.spi.capability;

import com.seeyon.cip.provider.api.credit.CreditProviderService;
import com.seeyon.cip.provider.enums.CapabilityEnum;

/**
 * 企业征信能力通道扩展。
 * 业务参数、供应商 SDK / HTTP API、通道 code 从 Nacos 或平台能力配置读取，不在模板中写死。
 */
public class CustomCreditProviderService implements CreditProviderService {

    @Override
    public String getDescription() {
        return "自定义企业征信通道";
    }

    @Override
    public CapabilityEnum getCapabilityEnum() {
        // 按 cip-capability-api 目标版本的 CapabilityEnum 实际枚举值替换；不要猜不存在的枚举。
        return null;
    }

    @Override
    public String getChannelCode() {
        return "custom-credit";
    }

    // TODO: 按目标版本 FACT 方法签名实现 required 方法；default 方法只有业务需要时覆盖。
}
```

## Evidence 摘要

| 项 | 值 |
|----|----|
| 接口 FQCN | `com.seeyon.cip.provider.api.credit.CreditProviderService` |
| required 方法数 | 22 |
| default 方法数 | 3 |
| Contract Source | `cip-capability-api-5.5.147.jar` + CFR |
| Evidence | FACT ✅ |
