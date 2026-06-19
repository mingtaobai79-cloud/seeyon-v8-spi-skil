---
title: "简历解析"
source: "https://www.yuque.com/seeyonkk/v8/gdzts8d29pbzxcvf"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 简历解析

> Source: https://www.yuque.com/seeyonkk/v8/gdzts8d29pbzxcvf

作者：陈晓东

时间：2026.1.6

###### 1、使用场景

提供对简历文件的内容解析抽取能力

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
com.seeyon.cip.provider.api.resume.ResumeProviderService
```

###### 3、接口定义

```
/**
 * 上海穰川简历解析
 */
public interface ResumeProviderService extends ProviderService {
    @CipCapabilityComment("简历解析")
    ResumeResultDto analysisResume(ResumeRequestDto resumeRequestDto);
    
	@Override
    @CipCapabilityComment("获取能力类型")
    default CapabilityEnum getCapabilityEnum() {
        return CapabilityEnum.Resume;
    }
}
```

###### 4、示例demo

上海穰川简历解析

MesoorResumeServiceImpl.java
(18 KB)

###### 5、配置信息

运营平台海之韵DEMO简
描述提供对简历文件的内容解析抽
日志列表用量统
授权类型:未设置
当前通道:镶川-服务
开放平台
基础能力接入
授权配置
基础出信息
服务参数配置
三方应用集
TOKEN
8关闭全部
:基础能力接入
应用通道管理
简历解析
基础设置
能力配置
黑默认值
理首页
参数名
OCLP
编辑
UR
启用
