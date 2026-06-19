---
title: "离线消息"
source: "https://www.yuque.com/seeyonkk/v8/qhix1g6uzquoy08a"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 离线消息

> Source: https://www.yuque.com/seeyonkk/v8/qhix1g6uzquoy08a

###### 1、使用场景

提供离线消息发送能力

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
com.seeyon.cip.provider.api.message.OfflineMessageProviderService
```

###### 3、接口定义

```
public interface OfflineMessageProviderService extends ProviderService {

    @CipCapabilityComment("离线消息推送")
    void pushMessage(OfflineMessageDto dto) throws BusinessException;

    @CipCapabilityComment("获取能力类型")
    default CapabilityEnum getCapabilityEnum() {
        return CapabilityEnum.Offline;
    }
}
```

###### 4、示例demo

OfflineMessageServiceImpl.java
(7 KB)

###### 5、配置信息

述提供离线消息发送能力
202601-0800:00:00_2026-01-0823:59:59曲
当前通道:致远互联-服务
离线消息
基础能力接
应用通道管理
能力配置
日志列表
8关闭全部
豆开放平台
OCIP
三方应用集
切换通道
:基础能力接
管理首页
时间
状态
基础设置
通道
操作
启用
时间
