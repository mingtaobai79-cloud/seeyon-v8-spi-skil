---
title: "语音技术"
source: "https://www.yuque.com/seeyonkk/v8/gx3fls0f39yvk5lq"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 语音技术

> Source: https://www.yuque.com/seeyonkk/v8/gx3fls0f39yvk5lq

###### 1、使用场景

提供实时语音识别等语音能力

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
com.seeyon.cip.provider.api.voice.VoiceProviderService
```

###### 3、接口定义

```
public interface VoiceProviderService extends ProviderService {

    @CipCapabilityComment("创建实时语音识别任务")
    RealTimeApiResDto createRealTime(RealtimeApiDto apiDto);

    @CipCapabilityComment("创建获取录音完整文件任务")
    QueryVoiceApiResDto createVoiceFile(QueryVoiceApiDto apiDto);

    @CipCapabilityComment("根据任务标识Id获取录音完整文件结果")
    QueryVoiceFileApiResDto queryVoiceFileResult(QueryVoiceFileApiDto apiDto);

    @CipCapabilityComment("创建录音文件转文字任务")
    CreateWordsApiResDto createFileConvertWords(CreateWordsApiDto apiDto);

    @CipCapabilityComment("获取录音文件转文字任务结果")
    QueryConvertResultApiResDto queryConvertWordsResult(QueryConvertResultApiDto apiDto);

    @CipCapabilityComment("获取能力类型")
    default CapabilityEnum getCapabilityEnum() {
        return CapabilityEnum.Voice;
    }

    @CipCapabilityComment("创建智能摘要任务")
    CreateIntelligentDigestApiResDto createIntelligentDigest(CreateIntelligentDigestApiDto apiDto);

    @CipCapabilityComment("获取智能摘要任务结果")
    QueryIntelligentDigestApiResDto queryIntelligentDigestResult(QueryIntelligentDigestApiDto apiDto);
}
```

###### 4、示例demo

HuiyanVoiceServiceImpl.java
(20 KB)

###### 5、配置信息

描述:提供实时语音识别等语音
当前通道:科大讯飞服务
同运营平台
海之韵DEMO简称
日志列表用量统
基础出能力接入
暂无数据
应用通道管理
:基础出能力接入
参数名
三方应用集
默认值
服务参数配置
理首页
语音技术
基出设置
8关闭全部
切换通道
能力配置
SOCIP
开放平台
基础T信忘
启用
0昌
