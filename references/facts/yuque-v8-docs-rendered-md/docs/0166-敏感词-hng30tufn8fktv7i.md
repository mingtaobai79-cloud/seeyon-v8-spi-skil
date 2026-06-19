---
title: "敏感词"
source: "https://www.yuque.com/seeyonkk/v8/hng30tufn8fktv7i"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 敏感词

> Source: https://www.yuque.com/seeyonkk/v8/hng30tufn8fktv7i

###### 1、使用场景

提供内容审核能力

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
com.seeyon.cip.provider.api.censor.CensorProviderService
```

###### 3、接口定义

```
public interface CensorProviderService extends ProviderService{

    @CipCapabilityComment("文本内容审核")
    TextCensorApiResDto textCensor(TextCensorApiReqDto apiReqDto) throws BusinessException;

    @Override
    @CipCapabilityComment("获取能力类型")
    default CapabilityEnum getCapabilityEnum() {
        return CapabilityEnum.Censor;
    }
}
```

###### 4、示例demo

BaiduCensorServiceImpl.java
(7 KB)

###### 5、配置信息

述提供内容审核能力
海之韵DEMO简称
当前通道:百度云服务
协同运营平台
列表用量
敏感词
务参数配置
三方应用集
能力配置
::基础能力接入
切换通道
8关闭全部
应用通道管理
基础出能力接入
CLIENTSECRET
开放平台
基础设置
理首页
启用
基础出信后
SOCIP
参数名
CLIENTLD
黑默认值
0吕
APIURL
编辑
人
