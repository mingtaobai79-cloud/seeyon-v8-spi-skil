---
title: "平台租户组件"
source: "https://www.yuque.com/seeyonkk/v8/pdz512cqln5ggsmt"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 平台租户组件

> Source: https://www.yuque.com/seeyonkk/v8/pdz512cqln5ggsmt

作者：李阳CD

最后更新：2025-10-22

适用版本：V3.15+

# 1
应用场景

V8平台采用多租户架构，通过数据表中的租户ID实现租户间数据隔离。

通常情况下，平台会自动处理租户ID：从登录信息、MQ消息透传或第三方OpenApi调用的应用所属租户中自动获取，并在数据操作时自动添加到SQL中，开发者无需手动处理。

但在匿名访问（无需登录即可访问）OpenApi、微流程Rest接口、SPI接口或匿名线程等特殊场景下，租户ID会丢失，导致数据操作出现以下异常：

○
新增的数据因缺少租户ID而无法显示。

○
查询数据时缺少租户ID条件而无法查到结果。

因此，在这些特殊场景中需要手动设置租户，确保数据操作正常进行，本章演示如何手动构造租户，避免数据操作出现异常。

# 2
实现步骤

## 2.1
需要构造租户的场景

其一：开发功能必须是匿名访问等丢失租户ID的特殊场景，非特殊场景无需处理租户。

其二：开发功能存在数据新增、更新、查询的场景，或者调用任何Service方法时，都需要手动构造租户。

其三：单租户的项目满足以上两者依然需要构造租户，单租户只是租户固定，但不代表就不需要维护租户。

## 2.2
获取租户ID

使用system-admin帐号，登录管理后台，进入“租户管理”。

然后打开F12刷新页面进行抓包，可以取到平台所有租户的租户ID，对应“useTenantId”字段。

按实际业务需要，获取对应的租户ID即可。

ERTMOREILTER:,AFETCH/AHROSCCSSSFONTINGMEDVAIFESTSOCKETWASNOTHER
0GRAPHQL?CTPUSERCTPROLEPERMISSIONCONTROLRESOURCEPO
ELEMENTSCONSOLESOURCESNETWORKAPERTORMANCEM
AOTQZPRESERVELOGDISABLECACHENOTHROTLIN
GRAPHGL?ORGANIZATIONORGUNITSELECTUNITCOUNTPOST
O)GRAPHGL?CTPUSERCTPMANAGERTENANTLICENCETOTALGET
O)GRAPHGL?CTPUSERLICENSEHASPLUGINPOST&CTPU5ERGTPMANA..
OATANTI[FUSETGNANTIA91T5IBGCE51S9007OUSETENANT8
IATAO:IEOAE:BOOTOOOODATA:IRONTEAT:,ELS)MEEAE:SUCC
XHESDERSPAYLADPREVIEW_RESF
TRAGETD,2TE3ZSTUUS2AOTE7ACNA..IAO.RT1.ME
DORGNAMESHOWTYPE
RKAPERFORMANCEMEMORYAPPLICATIONLIGHTHOUSE
协同运营平
DATAIMAGE/S5VG+XML
客开管理
10A1口1|琼
输入租户名称
LICENSE管理
ENT:[]},MESSEGE;"SUCCESS",STATUS:0},""}
应用管理
环境配
025
DEVTOOLSAIN/BACKSTAGEMANAGE/TP-USER/TENANTMANAGEMENT/IST
户管理
户推
NOTHROTLING,A企
系统升级
CREATETIAE:1755135783000
建时间
租户管理
系统监让
SEINITIATORTIMINGC
ATATUE:EWABLE,*EEIST:SE,]]
租户管
机构数
户名称
YFILTER
LIGHTHOUSERECORDER
已启用
注册数
596
口LNVERT|MOR
详情
户名称
DEVTOOLS
系统巡
中
INITSTATUS:AULL
小IS-MANAGER
状态
操作
RMARK:"初始化"
1230M140
92
OROOT

## 2.3
手动构造租户示例

### 2.3.1
无需返回值的场景

比如数据新增时，无需获取返回值，则按照如下方式构造租户。

### 2.3.2
需要返回值的场景

比如数据查询时，需要获取返回的数据，则按照如下方式构造租户。
