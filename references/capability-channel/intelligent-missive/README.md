# 智能文档能力通道 — SPI 接口完整定义

> **Evidence: FACT ✅** — 接口签名来自 `cip-capability-api-5.5.147.jar` CFR 反编译。  
> 当前模板基线：`cip-capability-api-5.5.147.jar`；现场指定新版本时，以现场 jar/source 重新 FACT 化并局部更新。

## 场景

扩展智能公文/智能文档的生成、审核、提取、检索等通道。

## 接口

```java
public interface IntelligentMissiveProviderService
default public CapabilityEnum getCapabilityEnum() {
default public PropertiesDto getPropertiesDto() {
default public RecommendApiResDto createRecommend(RecommendApiReqDto request) {
default public IntelligentWriteApiResDto createWrite(IntelligentWriteApiReqDto request) {
default public IntelligentWriteQueryApiResDto queryWrite(IntelligentWriteQueryApiReqDto request) {
default public CardPageApiResDto queryCardPage(CardPageApiReqDto request) {
default public ExtractingTaskApiResDto createExtractingTask(ExtractingTaskApiReqDto request) {
default public ExtractingPageApiResDto queryExtractingPage(ExtractingPageApiReqDto request) {
default public ExtractingDetailApiResDto queryExtractingDetail(ExtractingDetailApiReqDto request) {
default public DiffRuleApiResDto queryDiffRule(DiffRuleApiReqDto request) {
default public DiffTaskApiResDto createDocDiffTask(DiffTaskApiReqDto request) {
default public DiffPageApiResDto queryDocDiffPage(DiffPageApiReqDto request) {
default public DiffDetailApiResDto queryDocDiffDetail(DiffDetailApiReqDto request) {
default public DiffDownApiResDto downloadDiffFile(Map<String, Object> request) {
default public DiffDetailViewApiResDto queryDocDiffView(DiffDetailApiReqDto apiReqDto) {
default public CardRuleApiResDto queryCardRule(CardRuleApiReqDto request) {
default public ReviewTaskApiResDto createReviewTask(ReviewTaskApiReqDto request) {
default public ReviewPageApiResDto queryReviewPage(ReviewPageApiReqDto request) {
default public ReviewDetailApiResDto queryReviewDetail(ReviewDetailApiReqDto request) {
default public TableTaskApiResDto createTableTask(TableTaskApiReqDto request) {
default public TableDetailApiResDto queryTableDetail(TableDetailApiReqDto request) {
default public SettingTaskApiResDto createSettingByTemplate(SettingTaskApiReqDto request) {
default public ProofreadTaskApiResDto createOnlineProofread(ProofreadTaskApiReqDto request) {
default public ProofreadTaskApiResDto queryProofreadDetail(ProofreadTaskDetailApiReqDto request) {
default public SensitiveWordApiResDto checkSensitiveWord(SensitiveWordApiReqDto request) {
default public UploadTempFileApiResDto uploadTempFile(UploadTempFileApiReqDto request) {
default public IntelligentPushOfficialApiResDto pushOfficial(IntelligentPushOfficialApiReqDto request) {
default public AssistReadingApiResDto assistReading(AssistReadingApiReqDto request) {
default public QueryResultApiResDto queryResultByTaskId(QueryResultApiReqDto request) {
default public ReadingDetailApiResDto readingDetail(ReadingDetailApiReqDto request) {
default public RetrievalApiResDto retrieval(RetrievalApiReqDto request) {
default public RelatedApiResDto queryRelated(RelatedApiReqDto request) {
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
| getCapabilityEnum | `无` | `CapabilityEnum` | default |
| getPropertiesDto | `无` | `PropertiesDto` | default |
| createRecommend | `RecommendApiReqDto request` | `RecommendApiResDto` | default |
| createWrite | `IntelligentWriteApiReqDto request` | `IntelligentWriteApiResDto` | default |
| queryWrite | `IntelligentWriteQueryApiReqDto request` | `IntelligentWriteQueryApiResDto` | default |
| queryCardPage | `CardPageApiReqDto request` | `CardPageApiResDto` | default |
| createExtractingTask | `ExtractingTaskApiReqDto request` | `ExtractingTaskApiResDto` | default |
| queryExtractingPage | `ExtractingPageApiReqDto request` | `ExtractingPageApiResDto` | default |
| queryExtractingDetail | `ExtractingDetailApiReqDto request` | `ExtractingDetailApiResDto` | default |
| queryDiffRule | `DiffRuleApiReqDto request` | `DiffRuleApiResDto` | default |
| createDocDiffTask | `DiffTaskApiReqDto request` | `DiffTaskApiResDto` | default |
| queryDocDiffPage | `DiffPageApiReqDto request` | `DiffPageApiResDto` | default |
| queryDocDiffDetail | `DiffDetailApiReqDto request` | `DiffDetailApiResDto` | default |
| downloadDiffFile | `Map<String, Object> request` | `DiffDownApiResDto` | default |
| queryDocDiffView | `DiffDetailApiReqDto apiReqDto` | `DiffDetailViewApiResDto` | default |
| queryCardRule | `CardRuleApiReqDto request` | `CardRuleApiResDto` | default |
| createReviewTask | `ReviewTaskApiReqDto request` | `ReviewTaskApiResDto` | default |
| queryReviewPage | `ReviewPageApiReqDto request` | `ReviewPageApiResDto` | default |
| queryReviewDetail | `ReviewDetailApiReqDto request` | `ReviewDetailApiResDto` | default |
| createTableTask | `TableTaskApiReqDto request` | `TableTaskApiResDto` | default |
| queryTableDetail | `TableDetailApiReqDto request` | `TableDetailApiResDto` | default |
| createSettingByTemplate | `SettingTaskApiReqDto request` | `SettingTaskApiResDto` | default |
| createOnlineProofread | `ProofreadTaskApiReqDto request` | `ProofreadTaskApiResDto` | default |
| queryProofreadDetail | `ProofreadTaskDetailApiReqDto request` | `ProofreadTaskApiResDto` | default |
| checkSensitiveWord | `SensitiveWordApiReqDto request` | `SensitiveWordApiResDto` | default |
| uploadTempFile | `UploadTempFileApiReqDto request` | `UploadTempFileApiResDto` | default |
| pushOfficial | `IntelligentPushOfficialApiReqDto request` | `IntelligentPushOfficialApiResDto` | default |
| assistReading | `AssistReadingApiReqDto request` | `AssistReadingApiResDto` | default |
| queryResultByTaskId | `QueryResultApiReqDto request` | `QueryResultApiResDto` | default |
| readingDetail | `ReadingDetailApiReqDto request` | `ReadingDetailApiResDto` | default |
| retrieval | `RetrievalApiReqDto request` | `RetrievalApiResDto` | default |
| queryRelated | `RelatedApiReqDto request` | `RelatedApiResDto` | default |

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
com.seeyon.cip.provider.api.missive.IntelligentMissiveProviderService=com.seeyon.extend.spi.capability.CustomIntelligentMissiveProviderService
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

import com.seeyon.cip.provider.api.missive.IntelligentMissiveProviderService;
import com.seeyon.cip.provider.enums.CapabilityEnum;

/**
 * 智能文档能力通道扩展。
 * 业务参数、供应商 SDK / HTTP API、通道 code 从 Nacos 或平台能力配置读取，不在模板中写死。
 */
public class CustomIntelligentMissiveProviderService implements IntelligentMissiveProviderService {

    @Override
    public String getDescription() {
        return "自定义智能文档通道";
    }

    @Override
    public CapabilityEnum getCapabilityEnum() {
        // 按 cip-capability-api 目标版本的 CapabilityEnum 实际枚举值替换；不要猜不存在的枚举。
        return null;
    }

    @Override
    public String getChannelCode() {
        return "custom-intelligent-missive";
    }

    // TODO: 按目标版本 FACT 方法签名实现 required 方法；default 方法只有业务需要时覆盖。
}
```

## Evidence 摘要

| 项 | 值 |
|----|----|
| 接口 FQCN | `com.seeyon.cip.provider.api.missive.IntelligentMissiveProviderService` |
| required 方法数 | 0 |
| default 方法数 | 32 |
| Contract Source | `cip-capability-api-5.5.147.jar` + CFR |
| Evidence | FACT ✅ |
