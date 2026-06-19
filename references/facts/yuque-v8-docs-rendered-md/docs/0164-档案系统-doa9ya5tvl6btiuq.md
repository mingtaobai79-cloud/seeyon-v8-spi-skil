---
title: "档案系统"
source: "https://www.yuque.com/seeyonkk/v8/doa9ya5tvl6btiuq"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 档案系统

> Source: https://www.yuque.com/seeyonkk/v8/doa9ya5tvl6btiuq

文档版本：v1.0.0
适用版本：5.0.6，其他版本待验证
最后更新：2025-11-23

## 1、开发环境搭建

### 1.1 创建工程

1
工程命名规范：

```
cip-capability-archives-{项目标识}
示例：cip-capability-archives-cscec5b
```

2
目录结构：

```
cip-capability-archives-{项目标识}/
├── target/                                    # 编译输出目录
│   └── cip-capability-archives-{项目标识}-{version}.jar       # 编译后的jar包
├── src/                                      # 源代码目录
│   └── main/
│       ├── java/
│       │   └── com/seeyon/cip/spi/capability/{项目标识}/
│       │       ├── service/
│       │       │   └── {项目标识}ArchivesServiceImpl.java  # 服务实现类
│       │       └── dto/
│       │           └── ArchivesProperties.java     # 配置属性类
│       └── resources/
│           └── META-INF/
│               └── spring.factories           # Spring SPI配置文件
└── pom.xml                                   # 项目依赖配置文件
```

### 1.2 配置依赖

```xml
<groupId>com.seeyon</groupId>
<artifactId>cip-capability-archives-{项目标识}</artifactId>
<version>1.0.0-SNAPSHOT</version>
<packaging>jar</packaging>
<dependencies>
    <!-- 必要的依赖 -->
    <dependency>
        <groupId>com.seeyon</groupId>
        <artifactId>cip-capability-api</artifactId>
        <version>5.0.50</version>
    </dependency>
    <dependency>
        <groupId>com.seeyon</groupId>
        <artifactId>cip-capability-facade</artifactId>
        <version>5.0.63</version>
    </dependency>
</dependencies>
```

## 2. 核心接口实现

### 2.1 SPI配置文件

在 src/main/resources/META-INF/ 目录下创建 spring.factories 文件：

```
# SPI服务实现类配置
com.seeyon.cip.provider.api.archives.ArchivesProviderService=\
com.seeyon.cip.capability.archives.cscec5b.service.impl.Cscec5bArchivesServiceImpl

# 归档后回调类(可选)
com.seeyon.cip.provider.api.callback.CipCallbackProviderService=\
com.seeyon.cip.capability.archives.cscec5b.service.impl.DigitalArchiveCallbackServiceImpl
```

### 2.2 服务实现类

服务实现类需要实现ArchivesProviderService接口：

返回对应路径下会有哪些属性,可以在归档设置配置属性映射
返回归档门类树,表示数据最终存储到哪一个路径下
DEFAULTLISTRESPONSE<ARCHIVESETTINGLATEGORYPTOQUERYANCHIVESYSTENCATEGORY(SINGLEREQUEST<LONG>REQUEST)
返回存储业务标题的属性CODE
TITLEATTRIBUTE(SINGLEREQUEST<LONG>REQUEST){RETURNNULL;}
PACKAGECONSEEYONCIP,CAPABIITY,APICONNON,ARCHIVES;
TARCHIVINGSINGLEREQUEST<ARCHIVINGINFOLRAPPERDTO>REQUEST)
1DECOMPILED.CLASSFILE,BYTECODEVERSION:52.0(JAVA8)
UTESBYTYPEIDS(SINGLEREQUEST<FIELDMAPPINGREQUESTDTO>REQUEST){
DEFAULTLISTRESPONSE<FIELDMAPPINGDTO>
PUBLICINTERFACEARCHIVESAPPSERVICE
IP-CAPABILITY-FACADE-5.6.2JAR>COM>SEEY
>SEEYON>CIP>CAPABILITY>API>CON
进行归档动作
OARCHIVESCHANNELSERVICELMPLJAVA
DEFAULTSINGLERESPONSE<STR
CBASEARCHIVESERVICEAPILMPLJAVE
RCHIVES>OARCHIVESAPPSERVICE
XCCONTENTCOMMONSTRUCTDTOJAVA
OCONTENTHUALIANLTEMDTOJAVA
DARCHIVESAPPSERVICECLASSXC
EFAULTSINGLER
EFAULTLISTRESPONSE<AR
RETURNNULL
RETURNNULL
RCHIVERESULTDTO
RETURNNULL;
IMPORT..
1USAGE1OV
NGLERESPONSE<ARCH1
BUSAGESIIMPEMENTATION
1OVERRIDE
OCOMMONUTIL
>..
1OVERRIDE
1USAGE
801
V
O
文
TO>STARTARCHIVING
>COMMON>ARCH
1OVERRIDE
V
EL
I
9L
25

注意：

1.实现类需要添加注解@CipChannelRouter(CHANNEL_CODE)，CHANNEL_CODE为自己定义的通道编码。

2.startArchiving为执行归档动作的方法，在此方法中开发归档逻辑，入参ArchivingInfoWrapperDto中的ArchiveContentSummaryDto可获取文件与配置的映射字段的值。

## 3. 系统配置

### 3.1 配置通道基本信息参数

1
登录后台管理界面(需要登录对应租户管理员)

2
进入：集成平台 > 基础能力接入 > 档案系统

C5B.COM.CN/MAIN/BACKSTAGEMANAGE/CIP-MANAGER/CAPABILITY/APP
供人脸识别认证能力,可用于敏感数据查看,
银行系统间的安全支付通道,企业无需专门登录
签等能力,支持电子签,手写签,支持顺序签,
提供发起签署,签署区配置,在线签薯,文档验
通过互联网专线或者前置机模式,建立起企业与
通过日程接口可以便捷地新建日程,用于面试安
提供中,英,法,德等常用的多国语言文本翻译
排,预约线下会议,项目计划等场景
引擎服务,应用于智慧城市,智慧农业,智慧
图服务,提供二三维一体化GIS数据和
提供全国各省市地区天气查询的能力
询,用印申请,用印情况查询等
提供实时语音识别等语音能力
入不同的档当案系统
提供各种在线支付服务
提供离线消息发送能力
协同运营平台集团
提供内容审核能力
基础出能力接入
能力,支持语种识别
提供全文检索能力
操作前的人身核验.
设置IPAAS平台通
,地理编码查询测距等地理
力配置
应用通道管理
基础设置
豆运维监控
供物理印章查
地理位置
档案系统
三方应用集
口所有书签
物理印章
人脸识别
SOCIP
在线支付
银企直连
能力配置
全文检索
电子签章
PI手册
未启用
移动日程
语音技术
能力配置
标签打印
开放平台
已启用
件管理
未启用
未启用
未启用
未启用
未启用
未启用
翻译服务
天气查询
标签打印
未启用
未启用
未启用
未启用
未启用
接入应用
未启用
GIS专网地图服务,提供
离线消息
敏感词
行政区戈
OADEVCSCEC5B.CO
IS服务
8关闭全部
未启用
位置能力
0未启用
P管理
日
目
理省页
8
0吕
能力
日
品
V

3
选择代码中定义的通道名称，并可配置代码中需要的参数，例如档案系统接口、FTP的地址等，此处配置的参数可以通过com.seeyon.cip.provider.api.common.ParameterService.getProviderParameterMapRefresh方法获取

描述:接入不同的档案系统
当前通道:中建五局-众优档案集成
2647714671091516426集团20251029
TY/APP/-2124661315894851770
事件配置日志列表
授权类型:周期限制
协同运营平台集团
OADEV.CSCEC5B.COR
员2647714671091516426集团20
ARCHIVESOURCECODE
COM.CN/MAIN/BACKST
授权配置O
三方应用集
开放平台
基础能力接入
豆运维监挂
档案系统
8关闭全部
ECIP-MANAGEL
能力配置
所有书签
用通道管
服务参数配置
事件管理
YSETMNAM
ER/CAPABILITYA
列表用量统计
网智服务
USERNAME
理首页
切换通道
接入应用
中建五局-众优档..
SECRETKEY
API手册
能力配置
PI管理
基信息
OCIP
默认值
基础设置
CKSTAGEMANAG
参数名
SERVERURL
编辑
0昌
.已启用
未启用
部
人

4
如果当前通道已经实现了相关方法，服务特征信息中显示为可用

当前通道:中建五局-众优档案集
事件配置日志列表
ERYARCHIVESYSTEMCATEGORY
描述:接入不同的档案系统
服务有效期:2026-12-31
OADEV.CSCEC5O.COL
STARTARCHIVING
基础能力接入
ELECTATTRIBUTESBYTYPELDS
协同运营平台集团
B.COM.CN/MAIN/BACK
点运维监控
STAGEVANAGE
三方应立用集
基础信息
获取门类元数据
/CIP-MANAGE
服务特征信息
授权配置O
授权类型:周期限制
获取门类元数据
-212466131
APABILITY/APY
315894851770
应用通道首管理
获取归档路径
开始归档
口所有书签
列表用量统计
获取归档路径
8关闭全部
档案系统
能力配置
理首页
件管理
开始归档
切换通道
AP手册
基础设置
PI管理
入应用
开放平台
能力配置
可用
OCIP
说明
停用
编辑
0昌
状态
名称
GUERYA
编码
RY可用
可用
目协办居
集团20251029

5
档案集成默认提供回调方法，如果有需要可将此回调接口配置到档案系统，此处对应回调类中实现的doCallback方法

调IG址:HT/172.30234800/SERVCE/AIP-CAPABITYBASE(CALBACKCIPCPTID-GROUPBCIPTYPE=ARCHVES&CPCHANNEL=EVERYBESTACIP
事件订阅配置请将下列信息填写至厂商系统管理后台
当前通道:中建五局众优档案集成
TY/APP/-2124661315894851770
SOADEV.CSCEC5B.COM.CN/MAIN/B
描述接入不同的档案系统
协办同运营平台集团
AIN/BACKSTAGEMANAGE
基础信息事件配置
基础出能力接入
DOCALLBACK
事件配置日志列表用量统计
47714671091516426集团20251029
8关闭全部
档案系统
三方应用集成
E/CIP-MANAGER/CA
基础设置
口所有书签
开放平台
豆运维监控
钱能力配置
事件管理
切换通道
接入应用
理首页
应用通道管刊
能力配置
团管理员264771467101.,....
API管理
0昌
216426集团2025102G
停用
R/CAPABILITY/APP
API手册
OCILP
三
品

### 3.2 归档管理配置

1
登录对应租户的归档管理员账号

2
进入：归档管理 > 应用管理 > 参数设置

3
进入默认分组，其他分组均为系统预置，归档路径选择“档案通道”，其他配置根据需要进行配置。

注意：开启"档案通道调试"会影响应用归档设置中“归档门类”的选项，所以不要开启。

<img width="1531">

4
再进入：归档管理 > 应用归档设置，去配置手动\自动归档具体方式与字段映射

<img width="1532">

5
根据具体需求，去选择文档中心哪一个文件夹下可归档、归档内容，同时可选择配置手动\自动归档

<img width="1502">

6
根据档案系统需要，配置表单\公文中字段对应的映射字段，映射字段支持自定义函数处理，映射字段对应代码中selectAttributesByTypeIds方法返回的字段设置

<img width="1522">

7
根据需要配置归档消息设置，系统会根据归档实际结果向消息接收人发送归档消息

<img width="1519">

## 4. 实现效果

### 4.1 从文档中心手动归档到第三方档案系统

<img width="1520">

## 5. 开发过程中注意事项

1、归档管理-归档日志里面看有没有日志，再查看归档管理应用的info日志，是不是卡到startArchiving前面的步骤了。

2、 检查归档的数据（应用、归档的页面）等信息有没有在归档管理里面配置对应的归档设置。

## 6.标品内置档案系统(网智-服务)

### 6.1 网智档案系统连接器配置相关

准备数据

1. V8系统 org-admin账号

2. 档案系统环境地址、档案系统单点登录地址

3. 档案系统rest账号的appKey 和 appInfo

4. 具有归档管理应用管理员角色的账号

### 6.2 导入网智的连接器

档案系统连接器.zip
(12 KB)

使用org-admin登录后台管理-切换根机构-集成平台-三方应用集成-新建-导入,导入后保存。

导入连接器时选择原样导入！

<img width="604">

### 6.3 修改地址

1. 保存的连接器-设计-进入设计态-基础信息修改连接地址并测试确保能测试通过，这里配置的是【档案系统环境地址】

2. 免登-设置，配置登录地址【档案系统单点登录地址】

3. 配置档案系统获取token的rest接口

4. 配置安全认证，其中缓存有效时长调整为5分钟(网智设置了token时长为6分钟）

5. 配置后选择发布，发布后。连接器已配置完毕并启用成功

### 6.4 配置网智的接入认证

1. 集成平台-开放平台-接入应用-新建一个档案管理的接入应用

新建后将接入应用的AppKey和AppSecret提供给网智档案系统，用作网智档案访问V8的认证信息，提供给网智档案的开发或实施人员

2. 授权API权限

需要授权的API权限有

组织模型-人员及任职信息同步（基于编码）

组织模型-组织信息同步（基于编码）

用户中心-认证信息

归档管理-微流程接口

<img width="582">

如果碰到API授权下找不到对应的应用或者API，请到API管理下启用对应应用的API

3. 事件订阅-添加事件

需要添加的事件有

组织模型-创建组织

组织模型-更新组织

组织模型-创建人员

组织模型-更新人员

4. 启用网智接入应用

### 6.5 配置归档管理应用

1. 使用具有 归档管理应用管理员角色的账号在运行态 归档管理-应用管理-参数设置

2. 设置网智档案系统单点地址和归档路径

3. 进行具体的归档设置配置然后验证整个归档通路

### 6.6 配置单点登录到网智系统

1. 使用org-admin账号切换到后台管理-应用中心-应用管理，找到 档案系统连接器

选择编辑进入应用详情--WEB端菜单-编辑-在编辑菜单中启用单点登录

2. 个人用户在前台-个性化设置-菜单设置-勾选档案系统连接器菜单即可

### 6.7 注意事项

#### 6.7.1网智特性1. 字段映射中所属部门、所属部门描述、所属人、所属人描述配置

跟网智系统对接协议商定。 所属部门、所属部门描述只能采用快捷下拉选择 组织实体 字段，

所属人、所属人描述只能采用快捷下拉选择 人员实体 字段， 这四个值网智有特殊处理，用以标识网智档案的人员和机构等信息

创建人，创建人描述只能采用快捷下拉选择 人员实体 字段，

#### 6.7.2. 映射管理枚举属性或选项集的配置枚举做双边对照，网智档案建立一套同样的枚举，致远通过传递“枚举名称”，双边对照映射。在映射关系中可使用函数 获取枚举名称 进行设值

### 

选项集直接传递选项集的名称

#### 6.7.3. 公文的关联文档无法归档

公文的文单设置关联文档字段时，需要配置关联文档的应用为公文管理，移除事项中心和文档管理，配置公文管理的参照，只保留发文、收文、签报实体，其余移除。并且编辑参照方案，只选择对应机构下的全部文

#### 6.7.4. 自动归档或手动归档，没有显示正文

检查归档设置正文字段中勾选的正文类型，归档时默认只归档已勾选的正文类型. 如勾选了OFD正文，实际业务中正文只有word正文或其他非OFD格式的正文，就不会归档正文

#### 6.7.5. 自动归档或手动归档后，不显示多页签数据

检查归档设置是否勾选了文单，多页签默认跟随文单的，没有文单就没有多页签内容

<img width="578">

#### 6.7.6. 配置公文的文号映射

归档设置配置映射关系时，传递文号时选择文号解析后的字段

发文文单 ： 发文.发文字号

收文文单 ： 收文.来文文号、收文.收文编号 需要根据项目需要选择

签报单	 ： 签报单.发文字号

#### 6.7.7. 调整网智的appKey和appInfo

调整后进行重新发布，发布后生效

#### 6.7.8.网智从V8 同步组织模型，默认的组织编码设置

如果从根机构进行同步，根机构默认的编码卫“group”也可从后台管理-行政组织管理-机构那里查看组织编码

#### 6.7.9.网智档案访问组织模型数据接口不通，需网智检查配置访问组织模型的open-API 地址是否正确

另：网智与V8的人员访问的接口地址

http://【COP平台域名】/service/ctp-user/auth/restore

这里的COP平台域名 是V8正常登录时的网络地址

#### 6.7.10. 归档后、归档应用-归档日志下不显示归档结果

归档后、等待3~5分钟后在归档管理-归档日志下仍然看不到归档结果，首先使用org-admin账号登录后台管理、切换根机构，在集成管理-三方应用集成下找到档案系统连接器，进入设计态查看日志。根据日志的状态或者返回结果初步排查原因

<img width="584">

如果只有档案归档的结果都是成功的，进行下一步判断档案系统是否回调V8系统告知归档结果使用org-admin账号登录后台管理、切换根机构，在集成管理-开放平台-接入应用中找到 网智档案的接入应用，查看-使用日志-开放API，在API接口搜索”网智归档结果回调“，对比上一步对应时间节点，查看是否有对应的回调记录。如果没有对应的回调记录，联系档案系统的人员定位排查，如果存在对应的回调记录，联系致远的研发定位排查

#### 6.7.11. 查看传输到档案系统的文件信息

1、 根据具体的归档时间点，使用org-admin账号登录后台管理、切换根机构，在集成管理-三方应用集成下找到档案系统连接器，进入设计态，找到对应的“档案归档”接口，找到里面的请求参数 file = temp/035001505961366209-/paas-private/fjgs/doc534502257506599167/n

<img width="560">

2、 将file的值拼接到下面地址中，在浏览器中访问服务器地址 + /service/doc534502257506599167/file/download-url?&clientType=PC&storageKey=该处替换为file的值. (注意地址中不要出现双斜杠//，并且用户登录了V8系统 )

3、 将上面一步请求返回的content中的内容拼接上前缀后继续访问

服务器地址/service+上面一步content中的内容(注意地址中不要出现双斜杠//，并且用户登录了V8系统 )

访问地址后浏览器会自动下载文件，解压文件后可得到往档案系统推送的文件
