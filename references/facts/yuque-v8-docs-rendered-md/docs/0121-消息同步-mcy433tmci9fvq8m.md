---
title: "消息同步"
source: "https://www.yuque.com/seeyonkk/v8/mcy433tmci9fvq8m"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 消息同步

> Source: https://www.yuque.com/seeyonkk/v8/mcy433tmci9fvq8m

作者：TCH
最后更新：2025-04-14

## 1. 应用场景

V8待办消息同步至三方系统，同时支持消息点击穿透至V8查看并处理

## 2. 实现步骤

### 2.1 接口注册

操作入口：管理后台-->集成平台-->三方应用集成-->集成应用管理-->新建集成应用-->添加接口

3请求地址T:/SEEYON/REST/THIRDPARTYMESSAGE/RECEIVE/SINGLEMESS
请求数据类型:APPLICATION小JSON
返回数据兴型:APPLICATION小JSO
方系统提供的消息同步接口地
携带签名/秘钥:关闭
口调用请求前认证
请求方式:POST
分类:消息同步
选择数据源:?.
消息推准送
白TOKEN获取
认证请求:否
认证公共参数三
回参分页设置(
是否异步:否
白待办集成
日默认分类
是否启用:是
Q日十
方法名:SENDMSG
白组织同步
返回参数
日消息同步
基础信息
台
入关键字
请求参数
描述:-.
名称:消息推送
事件
0
G
铂

接口请求body参设置，根据三方系统提供的API接口设置请求参数

直接导入按口语时J0N或者点击新增手动添加
请输入对应类型的表达式
HEADERQUERYPATHURL
THRDPARTYREGISTERCODE
THIRDPARTYRECEIVERLD
THIRDPARTYREGISTERCODE
THIRDPARTYRECEIVERLD
NONEBINDINGSENDEL
TPS://BAIDUCOM
THIRDPARTYSENDERLD
OTHERSYSTEMYY
HIRDPARTYMESSAGEL
NONEBINDINGSENDER
739161775
021-07-301440
HIRDPARTYSENDERLC
删除更多
调用请球前认证公共参数
是否必填默认值
MESSAGEHSUF
DOWNLOADURL
TPS://BAIDU.COM
TOKEN获
MESSAGEH5U
白待办集成
CREATIONDATE
MESSAGECONTENT
MESSAGEURL
THIRDPARTYMESSAGELD
DOWNLOADUR
MESSAGEURL
删除更多十
消息推送
MESSAGECONTENT
JSON编辑器
CREATIONDATE
白+
删除更多
删除更多
删除更多
默认分类
消息同步
删除更多
删除更多
组织同步
否显示操作
3456789
删除更多
删除更多
删除更多
输入关键字
显示名称
息内容
BODY
参数名
SEEYON
数类型
SEEYON
请求参数
文本
文本
文本
文本
口
文本
三
0/120
文本
文本
文本
接知
文本

注意：1、一定要调试确保接口能正常返回数据。

          2、务必将建设好的集成应用进行发布。

### 2.2事项同步配置

操作入口：管理后台-->集成平台-->三方应用集成-->集成应用管理-->新建集成应用-->同步-->消息同步

788646521403815145
用三方AP主动拉
方系统同步至A
公
同步能力编码
V8V5消息集
输入消息同步名称
步关型/模式
OTHERSYSTEMYY
同步方向
用编辑
同步事项同步
同步补偿
Q
状态
启用
删除
操作

编辑同步消息-->方向和模式选择

步类型选择外部接口模式
消息队列关联开放
请求参数映射
名称:V8V5消息集
返回参数映身
编辑消息
步方向选择主动准送
消息推送:消息推送
同步任务名称,自定义
0)主动推送3
O事件订阅
基础信息
同步方向:
主动拉取
联开放AP12一
同步类型:
置信息

编辑同步消息-->推送任务配置

<img width="1261.3333333333333">

请求参数映射配置

<img width="1272.6666666666667">

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

### 2.3任务发布及启用

消息同步启用/停用（默认为停用，配置完成之后需手动启用）

788646521403815145
三方系统同步至A9
请输入消息同步名称
同步能力编码
同步关型/模式
V8_OTHERSYSTEMYR
织同步事项同步
调用三方AP主动拉取
同步方向
同步补偿
消息同
Q1
8V5消息集
至
操作
状态
启用

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

[V8]我是消息内容
全部标记为已读
[V8]我是消息内容
团集团总部
我是消息内容
清空所有消息
应用定制平台
EEYON1外部系统
EEYON1外部系统
SEEYON1外部系统
重要的(0)
X导出记录
银棕事项的(0
复我钱的(0)
@我的(0)
领导日程
未卖(2)
全部(2/35)
业务生成器
文化建设
会议管理
表单应用
领导的(0)
知识社区
公文管理
目标管理
文档协作
SEEYON1外部系
报表中心
协同工作
09:37
我是消息内容
09:38
09:36
09:38
人

## 4、三方系统点击穿透V8查看详情：

三方系统接收到V8推送的数据之后解析接口中的穿透地址并进行二次封装，进行免登录操作，参考单点登录说明

组装前V8传递至三方系统的URL地址：

dynamic1225619914830136982/wuwaikuangxiangqing?affairId=6592588474172853573&id=-2961682948714214769&caseId=7406710989768423177&permissionId=-525215239126099679&templateId=-6965957454079506593

组装后穿透地址：

http://dev-xtcv8.seeyoncloud.com/oauth/avoid?web=%2Fmain%2Fportal%2Fdynamic3796486802071177913%2FfreeCollDetail%3FaffairId%3D-4840886716036047039%26id%3D4642078309833109590%26caseId%3D4330018422993921872%26permissionId%3D-4675419542624856289%26templateId%3D7509323934893902338&mobile=&sytype=sytoken&syid=af5787fb579f453485749d901eb91c66&sytoken=SY-mon0c9725f45l5f2
