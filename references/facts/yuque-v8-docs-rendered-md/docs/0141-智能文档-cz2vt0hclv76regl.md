---
title: "智能文档"
source: "https://www.yuque.com/seeyonkk/v8/cz2vt0hclv76regl"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 智能文档

> Source: https://www.yuque.com/seeyonkk/v8/cz2vt0hclv76regl

作者：陈晓东

时间：2026.1.5

###### 1、使用场景

提供对各类文档的文档比对、文档抽取识别、文档审核、表格解析等能力

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
com.seeyon.cip.provider.api.missive.IntelligentMissiveProviderService
```

###### 3、接口定义

```
/**
 * @Description: 智能文档
 */
public interface IntelligentMissiveProviderService extends ProviderService {
    /**
     * 获取能力类型
     */
    @Override
    @CipCapabilityComment("获取能力类型")
    default CapabilityEnum getCapabilityEnum() {
        return CapabilityEnum.Missive;
    }
    @CipCapabilityComment("获取当前能力的后台管理通道配置属性")
    default PropertiesDto getPropertiesDto() {
        return null;
    }
    /**
     * @Description: 智能推荐
     */
    @CipCapabilityComment("创建智能推荐任务")
    default RecommendApiResDto createRecommend(RecommendApiReqDto request) {
        throw new BusinessException(IMPL_NOT_EXIST);
    }
    /**
     * @Description: 智能拟文
     */
    @CipCapabilityComment("创建智能拟文任务")
    default IntelligentWriteApiResDto createWrite(IntelligentWriteApiReqDto request) {
        throw new BusinessException(IMPL_NOT_EXIST);
    }
    /**
     * @Description: 获取智能拟文结果
     */
    @CipCapabilityComment("获取智能拟文结果")
    default IntelligentWriteQueryApiResDto queryWrite(IntelligentWriteQueryApiReqDto request) {
        throw new BusinessException(IMPL_NOT_EXIST);
```

###### 4、示例demo

IdpsServiceImpl.java
(52 KB)

###### 5、参数配置

描述提供对各类文档的文档比对,文档抽取识别,文档审核,表格解析等能力
海之韵DEMO简称
当前通道:达观(V10)-服务
同运营平台
应用通道管理
C3基础设置
EXPANDLDS
日志列表用量统计
基社能力接入
服务参数配置
三方应用集
开放平台
智能文挡
PASSWORD
USERNAME
理首页
基础出信息
关闭全部
能力配置
切换通道
SOCILP
参数名
默认值
APIURL
启用
能力配置
编辑
V
