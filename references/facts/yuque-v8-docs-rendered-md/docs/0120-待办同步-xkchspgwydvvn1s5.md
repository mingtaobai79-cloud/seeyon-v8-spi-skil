---
title: "待办同步"
source: "https://www.yuque.com/seeyonkk/v8/xkchspgwydvvn1s5"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 待办同步

> Source: https://www.yuque.com/seeyonkk/v8/xkchspgwydvvn1s5

作者：TCH
最后更新：2025-04-14

## 1. 应用场景

V8待办事项同步至三方系统，同时支持待办点击穿透至V8查看并处理

## 2. 实现步骤

### 2.1 接口注册

操作入口：管理后台-->集成平台-->三方应用集成-->集成应用管理-->新建集成应用-->添加接口

3请求地址:/SEEYON/REST/THIRDPARTYPENDING/RECE
求数据头型:APPLICATION小JSON
京
回数据关型:APPLICATION/小JSON
携带签名/秘钥:关闭
方法名:CREATAFFAIL
回参分页设置
组织同步
认证请求:否
公共参数
先择数据原:-.
白待办集成
口调用请求前
三
白TOKEN获期
是否异步:否
分类:待办集
请求方式:POST
请求参数
SYSTEMYY
默认分类
输入关
名称:待办集成
描述:-
是否启用:是
待办集成2
消息同步
返回参数
三米
8OTHER
基础信息
日
接口地址
品
强
接口X

接口请求body参设置，根据三方系统提供的API接口设置请求参数

调用请求前认证公共参数三
NONEBINDINGRECEIVE
60F293F1C3F86
NONEBINDINGRECELVE
ONEBINDINGSENDER
022-110716254
删除更多十
HTTPS://BAIDUCO
NONEBINDINGSENDE
删除更多十
删除更多十
THIRDSENDERLD
白默认分类
REGISTERCOD
白TOKEN获
THIRDSENDERLC
删除更多十
SENDERNAME
删除更多
日待钠集成
DERQUERYPATHURL)
删除更多十
删除更多
白消息同步
SENDERNAME
请输入关键字
接导入接口请求JSON字符或者点击新增手动
REGISTERCOD
THIRDRECELVERL
删除更多+
JSON编辑器
白组织同步
EEYON1
删除更多十
THIRDRECEIVERL
是否必填
SEEYON1
SEEYON1
EEYON1
删除更多十
显示名称
REATIONDATE
Q日+
REATIONDATE
求参
EYON1
待办集成
是否显示
删除更多
HEADER
TASKLD
STATE
默认值
文本
ERSYSTEMYY
文本
OD小Y
文本
文本
3002
参数关型
品
文本
参数名
文本
V
STATE
TASKLD
12
品
口
口
操作
文本
0
本
UR
口
文本
口
本
TITLE
口
TITLE
口
口
口
口
URL
口
口
品
门
口
文本
口

注意：1、一定要调试确保接口能正常返回数据。

          2、务必将建设好的集成应用进行发布。

### 2.2事项同步配置

操作入口：管理后台-->集成平台-->三方应用集成-->集成应用管理-->新建集成应用-->同步-->事项同步

79010875254836558
9同步至三方系统
步关型/模
请输入事项同步名称
8_V5待办集成
AP主动推
同步同步补信
事项同
织同步
步能力编
编辑删
步方向
消息同步
启用
拍
Q
名称
停用
品
状态
2

编辑同步事项-->方向和模式选择

EEE
3,当出除任务返回结果满足[数据不存在]逻辑时,当前删除任务会直接8过;
4,同一应用连接器下,仅允许有一套标准AP主动推送截置;
步方向:三方系统同步至A9
同步方向选择A9同步至二方系统
步至A90A9同步至三方系统2一
同步模式选择AP主动推送
步模式0AP主动推送
同出任努否称(日定义)
推送任务配置:任务类
8OTHERSYSTEMYY
三
数据范围
:V8V5待办集
中
消息体示例:
新待办内客
删除待办
编辑事项
同步任务配置
待办变已办
新增待办
办已办
配置状态
未配置
接口名称
待办集成
配置
取消
编辑
香配置
方向和楼式选择
清中

编辑同步事项-->推送任务配置

待办事项示例查看参考

<img width="991.3333333333334">

请求参数映射配置

<img width="1266">

注：请求参数也可以通过产品提供的公式函数自定义组装，案例中我们可以对请求PC 端链接地址进行封装：

分支条件在下方选择字段变量或者函数,且在英文输入法下编
TAL/+参数变量,PC端链接,事项中心返回给外部打开这个事项的地址,链接包含AFFAIN
HTTP://DEY-XTCV8SEEYONCLOUD.COM/OAUTH/AVOID?WEB
事件订阅时需要根据该消息进行处理
3,当删除任务返回结果满足[数据不存
消息类型(AFFAIREVENTMESSAGE
2,当更新类任务返回结果满足[数据不
4,同一应用连接器下,仅允许有一套
判定扣缴义务人是否为空
判断文本或属性是否为
当新增类任务返回结果满足[数据已
URL编码(/MAIN/PORTAL/
送任务配置:任务
同步任务配置
SNUL(扣缴义务人
注解的VALUE值一致,
请输入搜索关键
NONEBINDINGRECER
签名函数(集成应用
请输入搜索关键词
为空不为空包含(全部属
,白组织机构
THIRDRECE
自日期函教
THIRDSENC
白环境变量
回文本函数
<=ANDORNOTTRUEFALSE()
表达式设置
参数变量
复制部分复制粘贴
是否创建
可聚合函数
?条件函数
消息体示例:
REGISTER
白变化函数
区数学函数
正消息类型
一一
ISNULL对多)
器系统变量
NONEBIN
,白日期
二基础函数
CREATION
可选范围
待办已办
UTF8)
点击查看
布尔2
白枚举函数
编辑事项
显示名称
白插件
业务数据货
STATE
K函数
二
SENDERN
空验证
TASKLD
示例:
事项推送
待发已发
待办集成
取消
文本2
UR
TITLE
专用)
元
+MOD
二二
请求
二二AND
AANA.STRNG

推送补偿配置（产品提供了事项同步补偿，事项同步失败之后会根据定义的补偿频率进行二次推送）

2,当更新类任务返回结果满足[数据不存在]邀时,当前更新任务会直接转至执行新骨逻辑;
,当出除任务返回结课满足[数据不存在]逻辑时,当前出除任务会直接过
1,当新增类任务返回结果满足[数据已经存在]逻辑时,当们新增任务会直接转至执行更新逻辑
三方系统同步至A90A9同步至三方系缘
,同应用连接器下,仅允许有一套标准AP主动推送配置;
名称:V8V5待集成
同步模式:API主动推
8OTHERSYSTEMYY
定时补偿频率:10分钟
推送补偿配置
同步任务配置
方向和模式选择
同步方向:
编辑事项
提示
S
活
马
景
设亚
应用
同步
自
鱼

### 2.3任务发布及启用

事项同步启用/停用

790108752548365585
8OTHERSYSTEM
步类型/模式
9同步至三方系
织同步非项同
步能力编码
同步补偿
步方向
消息同步
输入事项同步
名称
V5待办集成
3
组织同
状态
P主动推
0
Q1
品
删除

应用发布：

V8OTHERSYSTEMYY
协同运营平台
低代码定制平台
海之DEMO
连接器管理
我参与的
管理首页
开放平台
我创建的
基础设害
高级设计
连接器
基础能力接入
所有的
已启用
REST
连接器
设计
发布
O
A

### 2.4接口调用日志查看

("THIRDPARTYSENDERLD:"18224427430,'MESSAGEURL:"HTTP://DEV-XTCV8.SEEYONCLOUD.C
"THIRDRECEIVERLD:'SEEYON1",'SENDERNAME":SEEYON1,"THIRDSENDERLD":"'SEEYON1,"NO..
SENDERLD:"18224427430,MESSAGEURL":HTTP://DEV-XTCV8.SEEY
("THIRDPARTYSENDERLD:17391617174'MESSAGEURL:HTTP/DEV-XTCV8.SEEYONDLOUD.C
[THIRDPARTYSENDERLD:"18224427430',MESSAGEURL:"HTTP/DEVXTOV8.SEEYONCLOUD.C.
("THIRDPARTYSENDERLD':"18224427430'MESSAGEURL":"HTTP:/DEV-XTCV8.SEEYONCLOUD.(
TTLEV8待办推送三方系统CREATIONDATE:1744611891818,USERNAME:V8REST,
("THIRDPARTYSENDERLD:18224427430',"MESAGEURL:HTTP//DEV-XTOV8.SEEYONCLOUDC..
R"THIRDPARTYSENDERLD:18224427430,'MESSAGEURL:HTP://DEV-XTCV6.SEEYONCOUA.C
("THIRDPARTYSENDERD:18224427430,MESSAGEURL:HTP//DEVX
2025-04-1413:3
点击查看可以查看具体的请求
2025-04-1413:30
2025-04-1414:24
录待办同步消息同步
2025-04-1414
2025-04-1413:3
2025-04-1413:3
025-04-1413:3
请输入接口名称
2025-04-1414:2
BOOT0000
看重试
CONNECT.
B00T0000
取V5TOKER
CONNECT
中间表记录
CONNECT
CONNECT
息推送
息推送
息推送
息推送
查看重试
Q.
组织同步
CONNECT
查看重试
查看重试
CONNECT.
厂查看重试
4查看重试
消息推送
求参数
调用时间
看重话
接口名称
待办集成
接口名称
消息推送
看重
查看
V-XTCV8.SEEYONCLOUDL.C...
结果码
CONNECT.
CONNECT.
.2025-04-1413
TCV8SEEYONDLOUDC.,C
查看
EVXTCV8.SEEYONCLOUD.C,
免登
队列
XTCV8.SEEYONCLOUDC...
TCV8.SEEYONCLOUD.C..
口2事件
状态

## 3. 效果展示

证字段关型(人员一2025-04-0814:
试待办.1744185356610
V8系统集成(待办
2025-04-14S8EY0N1V8系统集
试待办-1
04.13-04.19
2025-04-10SEEY0N
我安排给他人的
2025-04-10SEEY0
集团总部
8待办准送三方系统
应用定制平台
待开会议
知识社区
025-04-09SEEY0N1
近3月待力
我的日程
新建计划
2025-04-11SEEY0N1
文化建设
报表中心
公文管理
业务审批
业务生成器
办中心
8至统集成
领导发的
试待办-2
踪事项
协同工作
目标管理
试待办-3
025-04-10SEEY0R
领导日程
文档协作
添加快排
V8系统集成
通讯录
会议管理
重要待力
表单应用
V8系统集成
新建事项
我的任务
建会议
我的(0)
/8系统集
14
人
0
17
0
15
0
日
O
V8系统集成

## 4、三方系统点击穿透V8查看详情：

三方系统接收到V8推送的数据之后解析接口中的穿透地址并进行二次封装，进行免登录操作，参考单点登录说明

组装前V8传递至三方系统的URL地址：

dynamic1225619914830136982/wuwaikuangxiangqing?affairId=6592588474172853573&id=-2961682948714214769&caseId=7406710989768423177&permissionId=-525215239126099679&templateId=-6965957454079506593

组装后穿透地址：

http://dev-xtcv8.seeyoncloud.com/oauth/avoid?web=%2Fmain%2Fportal%2Fdynamic3796486802071177913%2FfreeCollDetail%3FaffairId%3D-4840886716036047039%26id%3D4642078309833109590%26caseId%3D4330018422993921872%26permissionId%3D-4675419542624856289%26templateId%3D7509323934893902338&mobile=&sytype=sytoken&syid=af5787fb579f453485749d901eb91c66&sytoken=SY-mon0c9725f45l5f2
