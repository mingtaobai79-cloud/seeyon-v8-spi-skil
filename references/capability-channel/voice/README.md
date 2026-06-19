# 语音技术能力通道 — SPI 接口完整定义

> **Evidence: FACT ✅** — 接口签名来自 `cip-capability-api-5.5.147.jar` CFR 反编译。  
> 当前模板基线：`cip-capability-api-5.5.147.jar`；现场指定新版本时，以现场 jar/source 重新 FACT 化并局部更新。

## 场景

扩展实时语音、语音文件、转文字、智能摘要等通道。

## 接口

```java
public interface VoiceProviderService
public RealTimeApiResDto createRealTime(RealtimeApiDto var1);
public QueryVoiceApiResDto createVoiceFile(QueryVoiceApiDto var1);
public QueryVoiceFileApiResDto queryVoiceFileResult(QueryVoiceFileApiDto var1);
public CreateWordsApiResDto createFileConvertWords(CreateWordsApiDto var1);
public QueryConvertResultApiResDto queryConvertWordsResult(QueryConvertResultApiDto var1);
default public CapabilityEnum getCapabilityEnum() {
public CreateIntelligentDigestApiResDto createIntelligentDigest(CreateIntelligentDigestApiDto var1);
public QueryIntelligentDigestApiResDto queryIntelligentDigestResult(QueryIntelligentDigestApiDto var1);
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
| createRealTime | `RealtimeApiDto var1` | `RealTimeApiResDto` | required |
| createVoiceFile | `QueryVoiceApiDto var1` | `QueryVoiceApiResDto` | required |
| queryVoiceFileResult | `QueryVoiceFileApiDto var1` | `QueryVoiceFileApiResDto` | required |
| createFileConvertWords | `CreateWordsApiDto var1` | `CreateWordsApiResDto` | required |
| queryConvertWordsResult | `QueryConvertResultApiDto var1` | `QueryConvertResultApiResDto` | required |
| getCapabilityEnum | `无` | `CapabilityEnum` | default |
| createIntelligentDigest | `CreateIntelligentDigestApiDto var1` | `CreateIntelligentDigestApiResDto` | required |
| queryIntelligentDigestResult | `QueryIntelligentDigestApiDto var1` | `QueryIntelligentDigestApiResDto` | required |

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
com.seeyon.cip.provider.api.voice.VoiceProviderService=com.seeyon.extend.spi.capability.CustomVoiceProviderService
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

import com.seeyon.cip.provider.api.voice.VoiceProviderService;
import com.seeyon.cip.provider.enums.CapabilityEnum;

/**
 * 语音技术能力通道扩展。
 * 业务参数、供应商 SDK / HTTP API、通道 code 从 Nacos 或平台能力配置读取，不在模板中写死。
 */
public class CustomVoiceProviderService implements VoiceProviderService {

    @Override
    public String getDescription() {
        return "自定义语音技术通道";
    }

    @Override
    public CapabilityEnum getCapabilityEnum() {
        // 按 cip-capability-api 目标版本的 CapabilityEnum 实际枚举值替换；不要猜不存在的枚举。
        return null;
    }

    @Override
    public String getChannelCode() {
        return "custom-voice";
    }

    // TODO: 按目标版本 FACT 方法签名实现 required 方法；default 方法只有业务需要时覆盖。
}
```

## Evidence 摘要

| 项 | 值 |
|----|----|
| 接口 FQCN | `com.seeyon.cip.provider.api.voice.VoiceProviderService` |
| required 方法数 | 7 |
| default 方法数 | 1 |
| Contract Source | `cip-capability-api-5.5.147.jar` + CFR |
| Evidence | FACT ✅ |
