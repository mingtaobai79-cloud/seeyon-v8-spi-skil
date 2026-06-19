# 视频会议能力通道 — SPI 接口完整定义

> **Evidence: FACT ✅** — 接口签名来自 `cip-capability-api-5.5.147.jar` CFR 反编译。  
> 当前模板基线：`cip-capability-api-5.5.147.jar`；现场指定新版本时，以现场 jar/source 重新 FACT 化并局部更新。

## 场景

扩展视频会议创建、更新、取消、会议室、用户、录制等通道。

## 接口

```java
public interface VideoProviderService
default public CapabilityEnum getCapabilityEnum() {
public VideoMeetingOutDto createVideoMeeting(@Valid VideoMeetingCreateDto var1) throws BusinessException;
public VideoMeetingOutDto createPersonalVideoMeeting(@Valid VideoMeetingPersonalCreateDto var1) throws BusinessException;
public VideoMeetingOutDto updateVideoMeeting(@Valid VideoMeetingUpdateDto var1) throws BusinessException;
public void cancelVideoMeeting(VideoMeetingOperateDto var1) throws BusinessException;
public void finishVideoMeeting(VideoMeetingOperateDto var1) throws BusinessException;
public List<VideoMeetingRoomDto> selectVmrMeetingRoom(PageInfo var1, String var2) throws BusinessException;
public PageData<VideoMeetingRoomResourceResultDto> selectVmrMeetingRoomResource(PageInfo var1) throws BusinessException;
public List<VideoMeetingRoomMemberDto> selectMemberVmrMeetingRoom(PageInfo var1, String var2, @NotBlank(message="\u7528\u6237id\u4e0d\u80fd\u4e3a\u7a7a", groups={ValidationGroup.Zhumu.class}) @NotBlank(message="\u7528\u6237id\u4e0d\u80fd\u4e3a\u7a7a", groups={ValidationGroup.Zhumu.class}) String var3) throws BusinessException;
public void deleteVmwareMeetingRoom(VideoMeetingRoomOperateDto var1) throws BusinessException;
public void allotVmwareMeetingRoom(VideoMeetingRoomAllotDto var1) throws BusinessException;
public void updateVmwareMeetingRoom(VideoMeetingRoomUpdateDto var1) throws BusinessException;
public void recycleVmwareMeetingRoom(VideoMeetingRoomOperateDto var1) throws BusinessException;
public VideoMeetingUserDto addUser(@Valid VideoMeetingUserDto var1) throws BusinessException;
public VideoMeetingAuthOutDto authentication(String var1) throws BusinessException;
public VideoMeetingEndedDetailDto getEndedMeetingDetail(VideoMeetingEndedSelectDto var1) throws BusinessException;
public VideoMeetingRecordDto getMeetingRecord(VideoMeetingRecordSelectDto var1) throws BusinessException;
public VideoMeetingOutDto getMeetingDetail(VideoMeetingDetailDto var1) throws BusinessException;
```

## 基接口：ProviderService

所有能力通道接口均继承或遵循 `com.seeyon.cip.provider.api.ProviderService`：

```java
public interface ProviderService {
    String getDescription();
    CapabilityEnum getCapabilityEnum();
    String getChannelCode();
}
```

## 方法说明

| 方法 | 参数 | 返回 | 类型 |
|------|------|------|------|
| getCapabilityEnum | `无` | `CapabilityEnum` | default |
| createVideoMeeting | `VideoMeetingCreateDto var1` | `VideoMeetingOutDto` | required |
| createPersonalVideoMeeting | `VideoMeetingPersonalCreateDto var1` | `VideoMeetingOutDto` | required |
| updateVideoMeeting | `VideoMeetingUpdateDto var1` | `VideoMeetingOutDto` | required |
| cancelVideoMeeting | `VideoMeetingOperateDto var1` | `void` | required |
| finishVideoMeeting | `VideoMeetingOperateDto var1` | `void` | required |
| selectVmrMeetingRoom | `PageInfo var1, String var2` | `List<VideoMeetingRoomDto>` | required |
| selectVmrMeetingRoomResource | `PageInfo var1` | `PageData<VideoMeetingRoomResourceResultDto>` | required |
| selectMemberVmrMeetingRoom | `PageInfo var1, String var2, String var3` | `List<VideoMeetingRoomMemberDto>` | required |
| deleteVmwareMeetingRoom | `VideoMeetingRoomOperateDto var1` | `void` | required |
| allotVmwareMeetingRoom | `VideoMeetingRoomAllotDto var1` | `void` | required |
| updateVmwareMeetingRoom | `VideoMeetingRoomUpdateDto var1` | `void` | required |
| recycleVmwareMeetingRoom | `VideoMeetingRoomOperateDto var1` | `void` | required |
| addUser | `VideoMeetingUserDto var1` | `VideoMeetingUserDto` | required |
| authentication | `String var1` | `VideoMeetingAuthOutDto` | required |
| getEndedMeetingDetail | `VideoMeetingEndedSelectDto var1` | `VideoMeetingEndedDetailDto` | required |
| getMeetingRecord | `VideoMeetingRecordSelectDto var1` | `VideoMeetingRecordDto` | required |
| getMeetingDetail | `VideoMeetingDetailDto var1` | `VideoMeetingOutDto` | required |

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>cip-capability-api</artifactId>
  <version>${cip-capability-api.version}</version>
</dependency>
```

已 FACT 版本：`5.5.147`。父 POM 平台版本、boot starter 版本、SPI 契约包版本必须分别参数化。

## spring.factories

```properties
com.seeyon.cip.provider.api.video.VideoProviderService=com.seeyon.extend.spi.capability.CustomVideoProviderService
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["cip-capability"]
}
```

## 重启服务

cip-capability

## 代码骨架

```java
package com.seeyon.extend.spi.capability;

import com.seeyon.cip.provider.api.video.VideoProviderService;
import com.seeyon.cip.provider.enums.CapabilityEnum;

/**
 * 视频会议能力通道扩展。
 * 业务参数、供应商 SDK / HTTP API、通道 code 从 Nacos 或平台能力配置读取，不在模板中写死。
 */
public class CustomVideoProviderService implements VideoProviderService {

    @Override
    public String getDescription() {
        return "自定义视频会议通道";
    }

    @Override
    public CapabilityEnum getCapabilityEnum() {
        // 按 cip-capability-api 目标版本的 CapabilityEnum 实际枚举值替换；不要猜不存在的枚举。
        return null;
    }

    @Override
    public String getChannelCode() {
        return "custom-video";
    }

    // TODO: 按目标版本 FACT 方法签名实现 required 方法；default 方法只有业务需要时覆盖。
}
```

## Evidence 摘要

| 项 | 值 |
|----|----|
| 接口 FQCN | `com.seeyon.cip.provider.api.video.VideoProviderService` |
| required 方法数 | 17 |
| default 方法数 | 1 |
| Contract Source | `cip-capability-api-5.5.147.jar` + CFR |
| Evidence | FACT ✅ |
