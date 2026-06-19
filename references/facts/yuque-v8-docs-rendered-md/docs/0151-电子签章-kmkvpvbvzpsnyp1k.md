---
title: "电子签章"
source: "https://www.yuque.com/seeyonkk/v8/kmkvpvbvzpsnyp1k"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 电子签章

> Source: https://www.yuque.com/seeyonkk/v8/kmkvpvbvzpsnyp1k

# 契约锁通道之手写签名实现

## 1.应用场景

### 业务场景：

UDC应用法务系统，需要针对pdf文件进行手写签名。考虑通用性，就把契约锁电子签名以SPI扩展通道的方式，集成到集成平台，后续V8其他udc应用都可以使用该通道进行电子手写签名。

### 效果及具体使用：

首先，客开SPI扩展能力后，部署到集成平台就可以显示通道名，如下图所示。

契约锁接口认证TOKEN,由契约锁三方提供
力,支持电子签,手写签,支持顺序签,无序签,或签,解决传统签暑成本高,效率
N,客开回调接口加密解密使用,客开自定义
一契约锁接口认证秘钥,由契约锁三方提供
契约锁流程名,由契约锁三方提供
扩展出来的通道名
一契约锁流程D,由契约锁三方提供
契约锁接口地址,由契约锁三方提供
用通道的配置参
描述提供发起签考,签者区配置,在线签看,文
协同运营平台中国南水北调集团有限公司
,客开回调接口,客开自己定
是否以压缩文
当前通逍:契约锁通道-通用版
回调加密KEY,客
V8客开知识目
一回调接口TO
件来式下载
EDCOMPRESSFORO
下载签名
事件配置日志列表用最统计
件内容
飞三方应用线
TEGOYNAME
QQ1:1
本高,效率低等问题
C基础设置
电子签章
基础能力接
电子签章已保
服务参数配置
开放平台
OCIP
API管理X低代码定制平台
用通道管理
约锁签章
点聚爱务
1/13
WUY4HU
天印-服务
未启用
语音技才
参数名
科-服
务测试
能力配置
PPTOKEN
古&四
17307
向首页
GORYLD
刀控语诺
未启用
PPUR
ORMAL
信服务
认人值
日
未启用
日目录
ESKEY
管理首页基我能
234

回调地址如图示：callback回调接口入参出参，根据需要同契约锁对称确定。

述提伏发起然置,级雷区配置,在线然署,文情验签等最力,支持电子签,手写签,支情顺特松,无序然,或然,解决传统控雪成本高,效枣等问
回间地U上:HT(PS/1070.9523:8081/3ERVCE/CP-CAPABLLYBASE/CALBACK?ID-QMMJV8TYPE-SIGNATU
CHANNELQLYUESUOSHOUXIEQIANMING&ACTION
件订阅置请将下列信息填写至厂商系统管理后台
当前通道:契约锁通道通用版
日志列表用量统计
电子签章
基础信息
事件配
述提供发起签薯,签区配置,
O-G

第二步，客开spi包部署完后，需要配置cip-capability对应的nacos配置，平台找到对应客开的spi扩展包，配置如下图所示。

PUBLIC|DUBBODEV|DUBBOOLDSC|DUBBOSZ
详情示例代码编辑删除
配直当里命名空间DSEEYOND
详情示例代码编辑|删除|
详情示例代码|编辑|删除|
详情示例代码|编辑删除
详情示例代码|编辑|删除
详情|示例代码编辑删除
详情示例代码编辑|删除
详情|示例代码|编辑删除|
建配置DATAID已开启默认模糊查
详情示例代码编辑|删除
询到77条满足要求的配置
详情|示例代码编辑删除|
SEEYONOLDSC|SEEYONSZP
已开启默认模糊查询
CIP-CONNECTOR
|SEEYONDEV
默认模御匹配
归属应用
APP-SANDBOX
NAC0S2.2.3
CIPCONVERT
IP-MANAGER
DP-SCHEDULE
DATALD小R
IP-CAPABILITY
配置列表
导入配置
CDP-DATA
监听查询
APPAPPROVAL
GROUPR
SEEYON
历史版本
名空间
SEEYON
SEEYON
SEEYON
APP-COMMON
群管理
高级查询,
SEEYON
管理
SEEYON
管理
SEEYON
查询
EEYON
SEEYON
控制
操作
GROUP上
SEEYON
BPM

KB8DC3商水项目N8RC:业南水工具上传奥约肪+开放平台致远互联PE206机,中国高水北调集国
COM,SEEYONCIP-CAPABI1ITY-SMS-SPI-CHINAUNICOM,2.0
TY8GROUP=SEEYONNAMESPACE三SEEYON-DEV8EDASA
EYON-DEV&EDASAPPNAME=&SEARCHDATALD=8SEARCHGROUP-8PAGESIZE-10
TORY/MAVEN-RELEASESL
致远A8+协同管理,3南水项目日志-LNDE..
*MD5:334D4244245U
RLD=CENTER&DATALD三CIP-CAPABILLITY&GROUP
HP日工OCCYUIRUCV
CY/MAVEN-SNAPSHOTS
ENABLE:TRUE
RELEASEUR1:HTL.
DE.项目管理-致远互联..
SNAPSHOTUR1:HT*
-MAVEN:COM.SEEYON,CIP-CAPAB
*配置内容
PASSWORD:SEE
CIP-CAPABILITY
PIPLUGINS:
ENABLE:TRUE
业中国南水北调集团.,
...J7CA
更多高级选项
-MAVEN:COM.SEEYONGYS-SMS1.0.8
SPI-PLUGINS:
SEEYON
R南水项目-KUBOARDCO南水
不安全10.70.95.233:8848/NACOS/特/CON19
UP=&PAGESIZE=10&PAGENO-1
ATALD
GROUP
SPI:
6#SPI:
描述
15
18
19
北:HTL

第三，配置完nacos，重启cip-capability服务才能生效。

第四，在UDC低代码平台中使用：如下图所示

1.发起电子手写签名，udc使用规则搭建如下。

<img width="1517.6">

<img width="1536">

2.监听契约锁回调，处理后续业务规则，搭建配置如下。

<img width="1532">

以上就是从客开好的jar包部署到集成平台，展现的效果及在udc低代码平台里使用的具体配置搭建操作。

## 2.开发环境搭建

### 2.1 创建工程

创建普通Maven工程即可，pom.xml如下图

<img width="1014.9333333333333">

### 2.2 配置依赖

<img width="1061.6">

## 3.核心接口实现

### 3.1 SPI配置文件

<img width="1444.8">

### 3.2 服务实现类

SPI通道编号：

<img width="1512.8">

SPI通道名：

<img width="1485.6">

发起签名服务：

<img width="1524.8">

回调地址服务：

<img width="1497.6">

### 3.3 配置对象

配置字段，如下图所示，具体对应含义，见注释，具体的配置字段，根据需要自定义。

<img width="1520">

## 4.实现案例:电子签章-手写签名-契约锁通道

### 4.1 项目结构

<img width="519.2">

### 4.2 核心代码实现

#### 4.2.1 配置属性类

SignatureProperties.java
(2 KB)

#### 4.2.2 服务实现类

CipCallbackProviderServiceImpl.java
(10 KB)

SignatureProviderServiceImpl.java
(17 KB)

#### 4.2.3 服务工具类

QiyuesuoCallbackUtils.java
(3 KB)

OkHttpRequestJsonClientUtils.java
(12 KB)

OkHttpMultipartFileClientUtils.java
(6 KB)

#### 4.2.4 pom.xml文件

pom.xml
(2 KB)

### 4.3 完整工程

cip-spi-capability-signature.zip
(112 KB)

# 北京ca通道之电子签章实现

### 1.1流程表单里使用电子签章

<img width="1914">

### 1.2实施人员配置流程表单的电子签章按钮

<img width="1905">

### 1.3点击正文盖章，就自动触发调用SPI扩展的北京CA电子签章通道进行发起电子签章功能

<img width="1917">

### 1.4点击右侧列表中，显示的签章，拖拽到正文指定的位置即可。

<img width="1929">

### 1.5点击确认签署：同意签署认证的四种方式

<img width="1920">

### 1.6选择短信验证，接收验证码，点击同意签署即可完成文件签章。

<img width="1731">

<img width="1910">

<img width="1908">

## 2.开发环境搭建实例

<img width="1770">

<img width="1886">

### 3.1发起电子签章

SignatureProviderService.stamp

<img width="1878">

CAServiceImpl.java
(29 KB)

### 3.2回调电子签章

CACallbackServiceImpl.java
(13 KB)

CipCallbackProviderService.doCallback

<img width="1890">

### 3.3.完整工程代码

cip-spi-signature-ca-crrc.zip
(121 KB)
