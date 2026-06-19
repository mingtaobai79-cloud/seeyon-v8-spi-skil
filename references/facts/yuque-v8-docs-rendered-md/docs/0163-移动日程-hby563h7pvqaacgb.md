---
title: "移动日程"
source: "https://www.yuque.com/seeyonkk/v8/hby563h7pvqaacgb"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 移动日程

> Source: https://www.yuque.com/seeyonkk/v8/hby563h7pvqaacgb

###### 1、使用场景

通过日程接口可以便捷地新建日程，用于面试安排、预约线下会议、项目计划等场景

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
com.seeyon.cip.provider.api.schedule.ScheduleProviderService
```

###### 3、接口定义

```
public interface ScheduleProviderService extends ProviderService, CipCallbackProviderService<ScheduleCallBackDto, String> {

    @CipCapabilityComment("获取能力类型")
    default CapabilityEnum getCapabilityEnum() {
        return CapabilityEnum.Schedule;
    }

    @CipCapabilityComment("创建日程")
    default ScheduleInfoDto addSchedule(AddScheduleDto addScheduleDto) {
        return null;
    }

    @CipCapabilityComment("更新日程")
    default ScheduleInfoDto updateSchedule(UpdateScheduleDto updateScheduleDto) {
        return null;
    }

    @CipCapabilityComment("取消日程")
    default void cancelSchedule(ScheduleInfoDto dto) {

    }

    @CipCapabilityComment("获取日程详情")
    default ScheduleDetailDto detailSchedule(ScheduleInfoDto dto) {
        return null;
    }
}
```

###### 4、示例demo

QyWechatScheduleProviderServiceImpl.java
(26 KB)

###### 5、配置信息

描述通过日程接口可以便捷地新建日程,用于面试安排,预约线下会议,项目计划等场景
事件配置日志列表用量统计
HTTPS://QYAPI.WEIXIN.QQ.COM
服务参数配置
当前通道:企微日程服务
海之韵DEMO简称
协同运营平台
G基础设置
基础出能力接)
参数名
开放平台
应用通道管
8关闭全部
三方应用集
移动日程
基础娟能力接入
默认值
SOCIP
基础信息
编辑
能力配置
管理首页
CORPLD
AGENTLD
SECRET
APIURL
.
启用
0
