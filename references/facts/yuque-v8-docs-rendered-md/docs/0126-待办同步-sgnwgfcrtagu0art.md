---
title: "待办同步"
source: "https://www.yuque.com/seeyonkk/v8/sgnwgfcrtagu0art"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 待办同步

> Source: https://www.yuque.com/seeyonkk/v8/sgnwgfcrtagu0art

作者：张宇
最后更新：2025-04-14

## 1. 实时

### 1.1 关联开放API

#### 1.1.1 应用场景

1
待办事项创建：将三方系统的待办事项同步创建到V8平台

2
待办事项更新：将三方系统的待办事项状态更新同步到V8平台

3
批量同步处理：支持批量创建和更新待办事项

#### 1.1.2 接入导图

二级分类:流转中-->已结束
栏目B-我的待-->栏目C-我的已办
级分类:流转中-->已终止
审批结果一通过
栏目A-我的已发
流程表单提交成
待办处理详情页
待办集成场景定义
业务系统/BPM
更新我的已发
栏目A-我的已发
栏目B-我的待力
NINNNNNNNANN4N
二级分类:无
栏目A-我的已发
BAABAAEAEAA
二级栏目切换
更新我的已发
_:级分类:元
级栏目切换
AAAAAAAAAAAA
二级分类:流转中
8集成平台
开待办处理页面
新建我的已发
数据呈现
PC门户
OPENAPI
款据展示一
NAAAAAAAAOAOOAE
OPENAPI
点击行数据
新建待办
致据呈现
AAEAEAAAAAN
OPENAPI
更新待办
欧据展示
数据星现
数据圣现
OPENAPI
数据呈现
栏目切换
我的已发
OPENAPI
数提呈现
是否结安
数据呈现
未结束
开始
已估束
款据星现
我的待办
结束
业中业业
生成
功时
驳回一
生成
流程
已结束
圣现
场

#### 1.1.3 集成配置

##### 1.1.3.1 新建连接器

1
登录后台管理界面

2
进入：集成平台 > 连接器 > 连接器管理

3
点击"新建"按钮

4
填写连接器基础信息

5
发布

我创建的我参与的所
HIRDV8事项同步
理首页连接端
冠连接器
H
基础能力接
开放平台
协同运营平台
关闭全
20亲/页V
请输入名称
连接器管
基础设置
山
REST已
共4条
M

##### 1.1.3.2 新建事项同步

配置事项同步能力，获取同步能力编码（capabilityId）。

1
设计连接器

2
进入：集成平台 > 连接器 > 同步 > 事项同步 > 新建

3
同步方向选择： 三方系统同步至A9

4
同步类型/模式选择：开放写入OpenAPI

5
获取同步能力编码，提供给接口调用方

6
启动事项配置

<img width="1903">

##### 1.1.3.3 启用API

在V8平台中启用API才可以正常进行授权访问

2
进入：集成平台 > 开发平台> API管理

3
启动【待办集成接口】

<img width="1916">

##### 1.1.3.4 新建接入应用

V8平台中，新建应用用来分配AppKey和APPSecret、配置API访问授权、访问白名单等配置页

1
新建应用，参照：
应用接入
接入应用，并获取接口appKey和appSecret

2
进入：集成平台 > 开发平台> 接入应用 > API权限

3
开通【待办集成接口】

<img width="1266.5">

注：因产品调整，事项集成由原来的集成平台迁移到了连接器下，为兼容历史，所以保留了集成平台下的事项集成接口，两者的入参一模一样，建议项目采用连接器下的事项集成。连接器下的事项集成更加高效！

集成平台下事项集成链路：三方→cip-manager→cip-connector→ctp-affair

连接器下事项集成链路：    三方→cip-connector→ctp-affair

##### 1.1.3.5 API调用日志

查看API调用记录和状态。

2
进入：集成平台 > 开发平台> 接入应用 > 使用日志 > 开放API

<img width="1915">

#### 1.1.4 参数解释

openapi中参数解释比较详细

<img width="1271.5">

### 1.3 待办自动产生消息

三方推送的待办，可以通过配置选择自动产生消息

<img width="2807">

三方待办自动产生消息来源显示默认效果：

如果想把“待办自动产生消息”，替换成自己想要的内容，看下面解决方案：

●
nacos里面，cip-connector服务里，增加配置：
  seeyon.cip.plugin.enableMsgConnectorNameByAffair=true

那么会变成【{连接器名称}】待办提醒:XXX，如果传过来的标题有国际化，那么取连接器名称对应的国际化参数。如果国际化参数没匹配上，那么还会显示【待办自动产生消息】您有待办需要处理：XXX。

例如传过来的标题{"zh_CN":"测试待办","en":"test message"}，如果连接器名称国际化只有汉语{"zh_CN":"集成连接器"},那么最终消息体是
{"zh_CN":"【集成连接器】待办提醒:测试待办","en":"[Automatic message generated for to-do list] You have a to-do list that needs to be processed::test message"}

### 1.4 如何查询已同步的事项

1、根据三方id查询V8的affair数据
新版本：
三方待办id存在了ctp_affair服务，affair表的form_record_code字段。
具体sql是
select * from affair where form_record_code='${三方待办id}';

旧版本（如果上面sql查不到）
切换到cip-connector库
select id from cip_p_sync_affair where outer_id='${三方待办id}';
查询到的id，代入到下面的sql中。

切换到ctp-affair库
select * from affair where sub_object_id=${上一步id}

2、查询通过某个集成应用推过来的待办
通过页面获取集成应用id

切换到cip-connector库
select id as pluginid from cip_p_plugin_info where connector_id=${集成应用id};

切换到ctp-affair库
将上一步查询到的pluginid，代入到下面的sql中。
select * from affair where app_name = 'CipBasePlugin-${pluginid}'

### 1.5 三方开发注意事项

1、三方通过openapi访问V8接口，必须打印一下入参和出参，否则就是来回扯皮耽误工夫。三方发了待办，我们这没收到，可能网络问题，可能三方问题，没入参出参很难界定，待办量大，v8这没有记录详细信息。原则上要三方提供证据。

2、v8总有宕机、重启的时候，三方必须做好补偿的解决方案。

## 2. 定时
