---
title: "版式文档"
source: "https://www.yuque.com/seeyonkk/v8/dygyzew5otosm4pc"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 版式文档

> Source: https://www.yuque.com/seeyonkk/v8/dygyzew5otosm4pc

作者：陈晓东

时间：2025.1.5

###### 1、使用场景

提供针对版式文件的预览能力

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
com.seeyon.cip.provider.api.doc.DocOnlineProviderService
```

3、接口定义

```
public interface OfdProviderService extends ProviderService {

    /**
     * 获取能力类型
     * @return
     */
    @Override
    @CipCapabilityComment("获取能力类型")
    default CapabilityEnum getCapabilityEnum() {
        return CapabilityEnum.Ofd;
    }

    @CipCapabilityComment("校验Token")
    default Map<String, Object> checkToken(String token){
        return null;
    };
    /**
     * @Description: OFD文档预览
     * @Author: wuhf
     * @DateTime: 2022/6/14 12:55
     */
    @CipCapabilityComment("OFD文档预览")
    OfdFileApiResponseDto getOfdViewUrl(OfdFileApiRequestDto dto);
    @CipCapabilityComment("OFD文档下载")
    OfdDownApiResDto downFile(OfdDownApiReqDto reqDto);

    @CipCapabilityComment("获取文档盖章信息")
    default OfdSealApiResDto getSealInfo(OfdSealApiReqDto reqDto){
        throw new BusinessException(IMPL_NOT_EXIST);
    }
    @CipCapabilityComment("获取配置参数")
    OfdPropertiesDto getOfdProperties();

    @CipCapabilityComment("获取印章列表")
    default List<OfdSealItemApiReqDto> getSealList(String userCode) {
```

###### 3、示例demo

点聚版式文件集成

DianjuServiceImpl.java
(5 KB)

###### 4、配置信息

述提供针对版式文件的预览能
BB7391675EF44EB804E863B682D6B99
HTTPS://DEV-XTCV8.SEEYONCLOUDCOM/SERVICE
HTTPS://DJ-ALI.SEEYONV8.COM/OFD
当前通道:点聚-服务
APPSECRET
海之韵DEMO简称
理首页能力配置
日志列表用量统计
协同运营平台
基础能力接)
应用通道管理
三方应用集
服务参数配置
基础设置
8关闭全部
版式文档
APPKEY
能力配置
切换通道
开放平台
默认值
APIURL
出信怎
停用
DOMAIN
OCILP
参数名
编辑
