---
title: "物理印章"
source: "https://www.yuque.com/seeyonkk/v8/guror8p6i1x1srye"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 物理印章

> Source: https://www.yuque.com/seeyonkk/v8/guror8p6i1x1srye

作者：陈晓东

时间：2026.1.7

###### 1、使用场景

提供物理印章查询、用印申请、用印情况查询等能力

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
com.seeyon.cip.provider.api.physicalseal.PhysicalSealProviderService
```

###### 3、接口定义

```
public interface PhysicalSealProviderService extends ProviderService, CipCallbackProviderService {

    @CipCapabilityComment("获取能力类型")
    default CapabilityEnum getCapabilityEnum() {
        return CapabilityEnum.PhysicalSeal;
    }

    @CipCapabilityComment("部门同步")
    void syncDept(PhysicalSealDeptDto dto);

    @CipCapabilityComment("人员同步")
    void syncMember(PhysicalSealMemberDto dto);

    @CipCapabilityComment("用印申请")
    String applyAuthorize(PhysicalSealApplyDto dto);

    @CipCapabilityComment("用印申请记录查询")
    String queryApplyRecord(String applyId);

    @CipCapabilityComment("用印取消")
    void cancelApply(String applyId);

    @CipCapabilityComment("查询印章")
    PhysicalSealsDto querySeals();

    @CipCapabilityComment("获取用印详情")
    PhysicalSealImagesDto getImageByApplyId(String applyId);

    @CipCapabilityComment("获取用印照片文件")
    List<PhysicalSealFileDto> getImage(PhysicalSealImageDto dto);
}
```

###### 4、示例demo

群杰印章集成

QunJieServiceImpl.java
(19 KB)

###### 5、配置信息

述提供物理印章查询,用印申请,用印情况查
三方应用集
基础能力接入
当前通道:群杰服务
RESTLOGINNAME
关闭全部
用通道管理
基础出能力接
当前通道未启
务参数配置
用量统计
物理印章
群杰服务
9OCIP
日志列表
事件配置
RESTPWD
默认值
测试服务
切换通道
毕基础出设置
础出信息
能力配置
参数名
未启用
一开放平台
启用
编辑
管理首
UR
人
