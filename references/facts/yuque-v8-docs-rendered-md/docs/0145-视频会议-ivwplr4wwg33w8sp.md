---
title: "视频会议"
source: "https://www.yuque.com/seeyonkk/v8/ivwplr4wwg33w8sp"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 视频会议

> Source: https://www.yuque.com/seeyonkk/v8/ivwplr4wwg33w8sp

作者：陈晓东

时间：2026.1.6

###### 1、使用场景

提供普通视频、会议室会议的创建、查询、取消能力，支持获取会议录像、会议纪要

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
com.seeyon.cip.provider.api.video.VideoProviderService
```

###### 3、接口定义

```
/**
 * 视频会议能力扩展接口
 */
public interface VideoProviderService extends ProviderService {
    @CipCapabilityComment("获取能力类型")
    default CapabilityEnum getCapabilityEnum() {
        return CapabilityEnum.Video;
    }
    @CipCapabilityComment("创建视频会议")
    VideoMeetingOutDto createVideoMeeting(@Valid VideoMeetingCreateDto meetingData) throws BusinessException;
    
    @CipCapabilityComment("创建个人视频会议")
    VideoMeetingOutDto createPersonalVideoMeeting(@Valid VideoMeetingPersonalCreateDto meetingData) throws BusinessException;
   
    @CipCapabilityComment("修改视频会议")
    VideoMeetingOutDto updateVideoMeeting(@Valid VideoMeetingUpdateDto meetingData) throws BusinessException;
    
    @CipCapabilityComment("取消视频会议")
    void cancelVideoMeeting(VideoMeetingOperateDto videoMeetingOperateDto) throws BusinessException;
    
    @CipCapabilityComment("中止视频会议")
    void finishVideoMeeting(VideoMeetingOperateDto videoMeetingOperateDto) throws BusinessException;
    
    @CipCapabilityComment("企业管理员通过该接口分页查询企业的云会议室" +
        "pageInfo : 分页参数" +
        "searchKey : 搜索条件")
    List<VideoMeetingRoomDto> selectVmrMeetingRoom(PageInfo pageInfo, String searchKey) throws BusinessException;
    
    @CipCapabilityComment("查询会议室资源")
    PageData<VideoMeetingRoomResourceResultDto> selectVmrMeetingRoomResource(PageInfo pageInfo) throws BusinessException;
    
    @CipCapabilityComment("查询个人已分配的云会议室及个人会议ID")
    List<VideoMeetingRoomMemberDto> selectMemberVmrMeetingRoom(
            PageInfo pageInfo, String searchKey,
            @NotBlank(message = "用户id不能为空", groups = ValidationGroup.Zhumu.class) String userId)
            throws BusinessException;
```

###### 4、示例demo

瞩目会议

ZhuMuVideoMeetingServiceImpl (1).java
(27 KB)

###### 5、配置信息

述提供普通视频,会议室会议的创建,查询,取消能力,支持获取会议录像,会
事件配置会议资源日志列
HTTPS://APIMEETING.GQCOM
协同运营平台
当前通道:腾讯会议-服务
海之韵DEMO简称?
基础能力接)
三方应用集
用量统计
开放平台
服务参数配置
企微视频会议-服
应用通道管理
OPERATORUSERI
ERSIONTYPE
基础出能力接入
8关闭全部
基础信息
视频会议
华为云-服务
腾讯会议-服务
OCIP
SECRETLD
APPLD
SECRETKEY
测试-服务
切换通道
理首页
参数名
能力配置
黑默认值
APIURL
基础设置
SDKLD
未启用
未启用
未启用
未启用
V
V
人
启用
