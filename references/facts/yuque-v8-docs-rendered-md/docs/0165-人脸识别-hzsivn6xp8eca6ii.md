---
title: "人脸识别"
source: "https://www.yuque.com/seeyonkk/v8/hzsivn6xp8eca6ii"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 人脸识别

> Source: https://www.yuque.com/seeyonkk/v8/hzsivn6xp8eca6ii

###### 1、使用场景

提供人脸识别认证能力，可用于敏感数据查看、操作前的人身核验

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
com.seeyon.cip.provider.api.faceid.FaceIdProviderService
```

###### 3、接口定义

```
public interface FaceIdProviderService extends ProviderService {
    @Override
    @CipCapabilityComment("获取能力类型")
    default CapabilityEnum getCapabilityEnum() {
        return CapabilityEnum.FaceId;
    }

    @CipCapabilityComment("人脸添加")
    default FaceAddApiResDto addFace(FaceAddApiReqDto request) {
        throw new BusinessException(IMPL_NOT_EXIST);
    }

    @CipCapabilityComment("人脸认证")
    default FaceIdentifyApiResDto faceCheck(FaceIdentifyApiReqDto request){
        throw new BusinessException(IMPL_NOT_EXIST);
    }

    @CipCapabilityComment("人脸修改")
    default FaceUpdateApiResDto updateFace(FaceUpdateApiReqDto request){
        throw new BusinessException(IMPL_NOT_EXIST);
    }

    @CipCapabilityComment("获取access_token")
    default String getAccessToken() {
        throw new BusinessException(IMPL_NOT_EXIST);
    }
}
```

###### 4、示例demo

KuangShiFaceIdProviderServiceImpl.java
(1 KB)

###### 5、配置信息

提供人脸识别认证能力,可用于敏感数据查看,操作有
应用通道管理
服务参数配置
海之韵DEMO简称
当前通道:广视服务
人脸识别
国基础出能力接入
三方应用集成
:基础能力接)
8关闭全部
协同运营平台
基础设置
基础信息
日志列表
开放平台
SOCIP
启用
理首页
能力配置
用量统计
默认值
参数名
暂无数据
编辑
人
