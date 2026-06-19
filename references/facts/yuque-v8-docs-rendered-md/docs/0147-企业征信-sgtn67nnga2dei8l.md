---
title: "企业征信"
source: "https://www.yuque.com/seeyonkk/v8/sgtn67nnga2dei8l"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 企业征信

> Source: https://www.yuque.com/seeyonkk/v8/sgtn67nnga2dei8l

作者：陈晓东

时间：2026.1.6

###### 1、使用场景

提供企业基础工商信息、工商股东、融资信息、行政处罚、产品信息、行政许可等企业征信信息查询能力

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
com.seeyon.cip.provider.api.credit.CreditProviderService
```

###### 3、接口定义

```
public interface CreditProviderService extends ProviderService {

    @CipCapabilityComment("分页获取企业信息" +
        "pageNumber : 页码号" +
        "keyWord : 企业名称")
    EnterpriseInfoResponseData getEnterpriseInfo(Integer pageNumber,String keyWord);

    @CipCapabilityComment("获取企业基础工商信息报告" +
        "keyWord : 企业名称")
    EnterpriseBasicBusinessInfoResponseData getBasicBusinessInfo(String keyWord);

    @CipCapabilityComment("获取工商照面信息")
    EnterpriseBasicInfoDto getBasicInfo(CreditRequestDto dto);

    @CipCapabilityComment("获取股东信息")
    EnterprisePartnersDto getPartners(CreditRequestDto dto);

    @CipCapabilityComment("获取开庭公告信息")
    EnterpriseCourtNoticeDto getCourtNotice(CreditRequestDto dto);

    @CipCapabilityComment("获取能力类型")
    default CapabilityEnum getCapabilityEnum() {
        return CapabilityEnum.Credit;
    }

    @CipCapabilityComment("获取立案信息")
    EnterpriseCaseDetailDto getCaseDetailList(CreditRequestDto dto);

    @CipCapabilityComment("获取行政处罚信息")
    EnterpriseAdminPunishDto getAdminPunish(CreditRequestDto dto);

    @CipCapabilityComment("获取环保处罚信息")
    EnterpriseEnvpDto getEnvp(CreditRequestDto dto);

    @CipCapabilityComment("获取环保处罚详情")
    EnterpriseEnvpDetailDto getEnvpDetail(CreditRequestDto dto);
```

###### 4、示例demo

QiXinBaoProviderServiceImpl.java
(31 KB)

###### 5、配置信息

商信息,工商股东,融资信息,行政处罚,产品信息,行政许可等企业征信信息查询
协同运营平台
街述:提供企业基础工商信息
基础设置
理首页:基础出能力接
台海之韵DEMO简称
当前通道:启信宝服
列表用量
三方应用集成
基础出能力接入
服务参数配置
应用通道管!
企业征信
参数名
SECRETKEY
开放平台
能力配置
默认值
8关闭全部
切换通道
基础出信所
OCIP
APPKEY
启用
编辑
GS
