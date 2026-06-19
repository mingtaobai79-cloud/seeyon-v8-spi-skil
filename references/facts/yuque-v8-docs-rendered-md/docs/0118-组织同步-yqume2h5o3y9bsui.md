---
title: "组织同步"
source: "https://www.yuque.com/seeyonkk/v8/yqume2h5o3y9bsui"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 组织同步

> Source: https://www.yuque.com/seeyonkk/v8/yqume2h5o3y9bsui

作者：TCH
最后更新：2025-04-14

## 1. 实时

### 1.1 COP开放事件，三方异构系统订阅事件，完成组织同步模式。

#### 1.1.1应用场景

cop平台无需开发，通过事件订阅调用三方系统提供的接口，三方系统通过监听事件进行实时同步，该方式可以保障数据的时效性。

接入导图：

<img src="https://cdn.nlark.com/yuque/0/2025/png/29689686/1746688214368-ea1f3479-6dff-4dfe-8c1e-dab5d94858d7.png" width="604">

#### 1.1.2集成配置

1）启用所需的组织模型事件

操作入口：管理后台-->开放平台-->事件管理

025-05-0813:20
ANIZATIONPOSTCREATE创建岗位
ORGANZATIONLEVELCREATE创建职级
RGANIZATIONJOB.UPDATE
ORGANZATIONNMEMBERUPD再新人品
RGANIZATION,POSTUPDATE更新岗位
ORGANIZATIONJOB.CREATE创
ORGANIZATIONLEVELUPDATE更
ORGANIZATIONUNITUPDATE更
ORGANIZATION.UNIT.CREATE
8OTHERSYSTEM
2025-05081320
202505-08132(
202505-081320
025-05-0813:20
2025-05-0813:20
ORGANIZATIONNEMBERCREA
基础能力持
2025-05-0813:20
协同运营平台
创建人员日
2025-05-0813:20
创建组织图
海之韵DEMO
更新职级图
025-05-0813:20
创建岗位B
更新组织
大唐合同管
更新人员[限
础能力接入
更新职务阳
202505-0813:20
更新岗位
低代码平台
组织模型
建级
创建职务
更新时间
创建职务
PM引擎
议管理
事项中心
事件名称
DCDEMO
E更新职级
创建组织
请输入事件名彩
输入名称
事件标识
AP手册
息中心
三方应用
停用
更新职务
CRE8创建人员
批量启用
接入应用
已启用
开管理
开放平台
织模型
批量停用
启用
事件管理
用户中心
已启用
启用
P管王
已启用
状态
停用
已启用
TE更新组织
部
基础设置
公告
描述
停用
日程
新闻
停用
启用
启用
停用
操作
停用
停用
停用
停用
停用
ANTE
4
启用
Q批

2）配置事件回调

说明：收到事件通知请求后，需要返回200HTTP响应。其余响应码表示失败，开放平台会自动重发。重发的间隔越来越长，最多尝试10次。事件通知数据使用application/json格式发送。 事件通知的HTTP请求头中，包含回调令牌（需在接入应用的事件订阅中配置开启，默认不开启），用于接入应用验证事件来源。

操作入口：管理后台-->开放平台-->应用接入-->事件订阅

RGANIZATIONMEMBERCREATE
RGANIZATIONJOB.UPDATE
V8_OTHERSYSTEM
RGANZATIONLEVELUPDATE
RGANIZATIONPOSTUPDATE
RGANIZATION.UNITUPDATE
ORGANIZATIONLEVELCREATE
RGANIZATIONUNITCREATE
ORGANIZATIONJOB.CREATE
描述:组织同步V8至
证与基础信息
设置回调方式
创建人员图
组织模型
设置回调方
更新职级B
成应用
设置回调方式
更新职务日
更新人员日
三方应用集
置回调方式
置回调方式
创建职级B
更新组织图
数据范匪
更新岗位
创建胆职务B
添动加事件
织模型
创建组织日
请输入事件名称
请求网址
基础能力接
接入应用
置回调方式
求网址
事件标识
务名称
组织模型
调方式
织模型
求网
未设置
件名称
GANIZATIONNEMBERUPDATE
置回调方式
OCIP
求网
请求网址
组织摸型
置回调方式
求网
使用日志
组织模型
组织模型
戈网
组织模型
件订说
件管
基础出设置
全设置
API权限
网址
设置
关闭全音
开放平
探作
设
设置
移除
A
设定
8
1手册
组织模逛
入成
未设置
设置
请求网
设置
管理
2
移除设

3）设置回调

<img width="1240">

回调接口可以提前在集成应用中配置，接口配置参考：接口注册

#### 1.1.3事件清单

| 事件名称 | 事件标识 | 返回数据类型 | 描述 |
| --- | --- | --- | --- |
| 更新职务 | organization.job.update | JSON | 更新职务 |
| 更新组织 | organization.unit.update | JSON | 更新组织 |
| 更新职级 | organization.level.update | JSON | 更新职级 |
| 创建组织 | organization.unit.create | JSON | 创建组织 |
| 创建人员 | organization.member.create | JSON | 创建人员 |
| 创建岗位 | organization.post.create | JSON | 创建岗位 |
| 更新岗位 | organization.post.update | JSON | 更新岗位 |
| 创建职务 | organization.job.create | JSON | 创建职务 |
| 更新人员 | organization.member.update | JSON | 更新人员 |
| 创建职级 | organization.level.create | JSON | 创建职级 |

#### 1.1.4事件消息体

##### 1.1.4.1更新职务

| 参数名称 | 参数类型 | 参数描述 |
| --- | --- | --- |
| 更新职务消息 | OrgJobUpdateMessage |  |
| jobId | int64 | 职务id |
| code | string | 职务编号 |
| orgId | int64 | 所属组织 |
| isEnable | boolean | 状态 |
| oldCode | string | 更新前职务编号 |
| oldOrgId | int64 | 更新前所属组织 |
| oldIsEnable | boolean | 更新前状态 |
| eventKey | string | 消息标识 |

##### 1.1.4.2更新组织

| 参数名称 | 参数类型 | 参数描述 |
| --- | --- | --- |
| 更新组织消息体 | OrgUnitUpdateMessage |  |
| type | enum | 组织类型。枚举项可选值列表：
NONE（空），
INSTITUTION（机构），
DEPARTMENT（部门），
OUTSIDE_INSTITUTION（外部（编外）单位），
OUTSIDE_DEPARTMENT（外部（编外）部门）， |
| orgId | int64 | 组织id |
| oldOrgName | string | 组织名称 |
| orgName | string | 组织名称 |
| oldParentId | int64 | 原上级id |
| parentId | int64 | 上级id |
| oldIsEnable | boolean | 原状态 |
| isEnable | boolean | 状态 |
| oldEffectiveTime | date | 原生效日期 |
| effectiveTime | date | 生效日期 |
| oldInvalidTime | date | 原失效日期 |
| invalidTime | date | 失效日期 |
| eventKey | string | 消息标识 |

##### 1.1.4.3更新职级

| 参数名称 | 参数类型 | 参数描述 |
| --- | --- | --- |
| 更新职级消息 | OrgLevelUpdateMessage |  |
| levelId | int64 | 职级id |
| code | string | 职级编号 |
| levelSort | int32 | 职级序号 |
| isEnable | boolean | 状态 |
| oldCode | string | 职级编号 |
| oldLevelSort | int32 | 更新前职级序号 |
| oldIsEnable | boolean | 更新前状态 |
| eventKey | string | 消息标识 |

##### 1.1.4.4创建组织

| 参数名称 | 参数类型 | 参数描述 |
| --- | --- | --- |
| 创建组织消息体 | OrgUnitCreateMessage |  |
| orgId | int64 | 组织id |
| orgName | string | 组织名称 |
| parentId | int64 | 上级id |
| type | enum | 组织类型。枚举项可选值列表：
NONE（空），
INSTITUTION（机构），
DEPARTMENT（部门），
OUTSIDE_INSTITUTION（外部（编外）单位），
OUTSIDE_DEPARTMENT（外部（编外）部门）， |
| isEnable | boolean | 状态 |
| effectiveTime | date | 生效日期 |
| invalidTime | date | 失效日期 |
| eventKey | string | 消息标识 |

##### 1.1.4.5、创建人员

| 数名称 | 参数类型 | 参数描述 |
| --- | --- | --- |
| 创建人员消息体 | OrgMemberMessage |  |
| memberId | int64 | 人员id |
| name | string | 姓名 |
| phoneNumber | string | 手机号 |
| email | string | 邮箱 |
| type | enum | 人员类型。枚举项可选值列表：
NONE（空），
MEMBER（内部人员），
OUTSIDE_MEMBER（外部单位用户），
NATURAL_MEMBER（外部个人用户）， |
| image | string | 头像 |
| orgId | int64 | 主岗组织id |
| orgName | string | 主岗组织名称 |
| orgIds | array[int64] | 主岗所属机构id |
| isEnable | boolean | 启用状态 |
| effectiveTime | date | 生效日期 |
| invalidTime | date | 失效日期 |
| eventKey | string | 消息标识 |
| memberPostList | array[OrgMemberPostBaseDto] | 任职信息 |
| id | int64 | 任职id |
| main | boolean | 是否主岗 |
| orgId | int64 | 组织id |
| postId | int64 | 岗位id |
| levelId | int64 | 职级id |
| jobId | int64 | 职务id |
| sortId | int32 | 排序号 |
| isEnable | boolean | 状态 |
| effectiveTime | date | 生效日期，毫秒时间戳 |
| invalidTime | date | 失效日期，毫秒时间戳 |

##### 1.1.4.6、创建岗位

| 参数名称 | 参数类型 | 参数描述 |
| --- | --- | --- |
| 创建岗位消息 | OrgPostCreateMessage |  |
| postId | int64 | 岗位id |
| code | string | 岗位编号 |
| orgId | int64 | 所属组织 |
| isEnable | boolean | 状态 |
| eventKey | string | 消息标识 |

##### 1.1.4.7、更新岗位

| 参数名称 | 参数类型 | 参数描述 |
| --- | --- | --- |
| 更新岗位消息 | OrgPostUpdateMessage |  |
| postId | int64 | 岗位id |
| code | string | 岗位编号 |
| orgId | int64 | 所属组织 |
| isEnable | boolean | 状态 |
| oldCode | string | 更新前岗位编号 |
| oldOrgId | int64 | 更新前所属组织 |
| oldIsEnable | boolean | 更新前状态 |
| eventKey | string | 消息标识 |

##### 1.1.4.8、创建职务

| 参数名称 | 参数类型 | 参数描述 |
| --- | --- | --- |
| 创建职务消息 | OrgJobCreateMessage |  |
| jobId | int64 | 职务id |
| code | string | 职务编号 |
| orgId | int64 | 所属组织 |
| isEnable | boolean | 状态 |
| eventKey | string | 消息标识 |

##### 1.1.4.9、更新人员

| 参数名称 | 参数类型 | 参数描述 |
| --- | --- | --- |
| 更新人员消息体 | OrgUpdateMemberMessage |  |
| memberId | int64 | 人员id |
| name | string | 姓名 |
| phoneNumber | string | 手机号 |
| email | string | 邮箱 |
| type | enum | 人员类型。枚举项可选值列表：
NONE（空），
MEMBER（内部人员），
OUTSIDE_MEMBER（外部单位用户），
NATURAL_MEMBER（外部个人用户）， |
| image | string | 头像 |
| orgId | int64 | 主岗组织id |
| orgName | string | 主岗组织名称 |
| orgIds | array[int64] | 主岗所属机构id |
| isEnable | boolean | 启用状态 |
| effectiveTime | date | 生效日期 |
| invalidTime | date | 失效日期 |
| eventKey | string | 消息标识 |
| oldMemberPostList | array[OrgMemberPostBaseDto] | 更新前任职信息 |
| id | int64 | 任职id |
| main | boolean | 是否主岗 |
| orgId | int64 | 组织id |
| postId | int64 | 岗位id |
| levelId | int64 | 职级id |
| jobId | int64 | 职务id |
| sortId | int32 | 排序号 |
| isEnable | boolean | 状态 |
| effectiveTime | date | 生效日期，毫秒时间戳 |
| invalidTime | date | 失效日期，毫秒时间戳 |
| memberPostList | array[OrgMemberPostBaseDto] | 更新后任职信息 |
| id | int64 | 任职id |
| main | boolean | 是否主岗 |
| orgId | int64 | 组织id |
| postId | int64 | 岗位id |
| levelId | int64 | 职级id |
| jobId | int64 | 职务id |
| sortId | int32 | 排序号 |
| isEnable | boolean | 状态 |
| effectiveTime | date | 生效日期，毫秒时间戳 |
| invalidTime | date | 失效日期，毫秒时间戳 |

##### 1.1.4.10、创建职级

| 参数名称 | 参数类型 | 参数描述 |
| --- | --- | --- |
| 创建职级消息 | OrgLevelCreateMessage |  |
| levelId | int64 | 职级id |
| code | string | 职级编号 |
| levelSort | int32 | 职级序号 |
| isEnable | boolean | 状态 |
| eventKey | string | 消息标识 |

#### 1.1.5日志查看

操作入口：管理后台-->开放平台-->接入应用-->使用日志

#### 

## 2.定时

### 2.1 COP提供增量查询OpenAPI，由三方异构系统定时调用OpenAPI，完成组织同步模式。

#### 2.1.1应用场景

COP提供增量查询OpenAPI，由三方异构系统定时调用OpenAPI，完成组织同步，适用于组织数据变更频率不高，COP集成压力较小，cop只需提供OpenAPI接口，三方系统通过定时查询做增量统计即可。

#### 2.1.2集成配置

1）集成配置步骤

| 序号 | 步骤名称 | 责任方 | 使用场景 |
| --- | --- | --- | --- |
| 1 | 提供组织增量查询接口规范和文档 | 致远 | 必须，包含接口定义、签名规则、字段来源等信息 |
| 2 | API启用 | 致远 | 必须，只有启用的API才可以正常进行授权访问 |
| 3 | 新建接入应用 | 致远 | 必须，负责分配AppKey和APPSecret、配置访问授权、访问白名单等配置页 |
| 4 | 启用接入应用 | 致远 | 必须，未启用的接入应用，访问时会提示接入应用未启用 |
| 5 | 分配APPKey和APPSecret | 致远 | 必须，接口签名核心字段 |
| 6 | API授权 | 致远 | 必须，只有添加权限的额API接口才可以正常访问 |

##### 2.1.2.1 API启用

操作入口：管理后台-->开放平台-->API管理

<img width="1260.6666666666667">

##### 2.1.2.2 新建接入应用

V8平台中，新建应用用来分配AppKey和APPSecret、配置API访问授权、访问白名单等配置页

1
新建应用，参照
应用接入

2
进入：集成平台 > 开发平台> 接入应用 > API权限

<img width="1269.3333333333333">

#### 2.1.3接口请求

##### 2.1.3.1接口请求头（Header）

| 参数名称 | 是否必填 | 参数说明 |
| --- | --- | --- |
| app-key | true | 应用的唯一标识，创建接入应用后生成，可在应用基础信息页面获得。
示例：d43b0b442cf34076a2c4af6bb8928afb |
| sign-type | true | 固定值：MD5 |
| sign | true | 签名，字符串“AppSecret+请求体的JSON字符串+AppSecret”的MD5值（MD5值忽略大小写）
AppSecret，为应用的秘钥，创建接入应用后生成，可在应用基础信息页面获得。
示例：154fa5bc7e294deda68a15559b07c845请求体的JSON字符串，
需要将请求体中的请求参数转换为JSON字符串。 |
| Accept-Language | false | 语种：用以设置开放平台OpenAPI运行时上下文的语种参数。
枚举项可选值列表：zh-CN（简体中文），
zh-TW（繁体中文），
en（英文），
其他枚举项请参照平台语种列表。 |

##### 2.1.3.2签名示例（sign）

##### 2.1.3.3postman调用示例

第一步：配置pre-request脚本：拷贝下面代码，替换为上一步中接入应用的appKey和appSecret

### 

第二步：按图配置headers变量app-key：{{app-key}}、sign：{{signStr}}

<img width="1065.5">

第三步：配置body报文：将requestId、timestamp分别设置为{{request-id}}、{{timestamp}}

<img width="1076.5">

##### 2.1.3.4 JAVA代码调用

#### 2.1.4接口清单

| API分类 | API名称 | 接口描述 |
| --- | --- | --- |
| 组织信息查询/维护 | 根据条件分页查询组织详情 | 组织（机构+部门） |
| 组织信息同步（基于编码） | 根据组织编码查询组织详情 | 组织详情（机构+部门） |
| 岗位信息查询/维护 | 根据条件分页查询岗位 | 岗位 |
| 职务信息查询/维护 | 根据条件分页查询职务 | 职务 |
| 职级信息查询/维护 | 根据条件分页查询职级 | 职级 |
| 人员信息查询/维护 | 根据条件查询人员信息 | 人员详情 |
| 人员及任职信息同步（基于编码） | 分页查询组织下人员 | 人员&任职 |

##### 2.1.4.1、根据条件分页查询组织详情

请求地址

请求方式

请求参数（Body）

| 参数名称 | 父节点 | 是否必填 | 参数类型 | 参数描述 |
| --- | --- | --- | --- | --- |
| requestId |  | TRUE | string | 请求流水号。同一接入应用下的流水号不要重复；
最长32位，超过部分会被截断。 |
| timestamp |  | TRUE | int64 | 请求时间戳。请求时间和服务器时间不能相差过大，
默认5分钟以内。 |
| notifyUrl |  | TRUE | string | 异步回调URL。如果此参数非空，表示使用异步方式调用开放API，
执行结果将通过此URL异步通知调用者。 |
| pageInfo |  | TRUE | PageInfo | 分页 |
| pageNumber | pageInfo | TRUE | int32 | 当前页数 |
| pageSize | pageInfo | TRUE | int32 | 每页记录数 |
| pages | pageInfo | TRUE | int32 | 总页数 |
| total | pageInfo | TRUE | int32 | 总记录数 |
| needTotal | pageInfo | TRUE | boolean | 是否需要查询总记录数 |
| params |  | TRUE | map | 条件 |
| sort |  | TRUE | Sort | 排序 |
| orders | sort | TRUE | array[Sort$Order] | 排序 |
| direction | orders | TRUE | enum | 顺序,可用值:ASC,DESC。
枚举项可选值列表：ASC（ASC），DESC（DESC）， |
| property | orders | TRUE | string | 字段,可用值:DTO属性(请参照"响应参数"中content),
createTime,updateTime |

请求参数示例

响应参数（Body）

| 参数名称 | 父节点 | 是否必填 | 参数类型 | 参数描述 |
| --- | --- | --- | --- | --- |
| data |  |  | PageData | 组织信息详情分页列表 |
| pageInfo | data |  | PageInfo | 分页参数对象 |
| pageNumber | pageInfo |  | int32 | 当前页数 |
| pageSize | pageInfo |  | int32 | 每页记录数 |
| pages | pageInfo |  | int32 | 总页数 |
| total | pageInfo |  | int32 | 总记录数 |
| needTotal | pageInfo |  | boolean | 是否需要查询总记录数 |
| content | data |  | array[OrgUnitDto] | 数据集对象 |
| id | content |  | int64 | 组织ID,新建时不必填，修改时必填 |
| institutionId | content |  | int64 | 组织所属机构id。
如果是部门，就是所属机构id；
如果是机构，就是自己id(不作为入参保存) |
| name | content |  | string | 组织名称 |
| mnemonic | content |  | string | 助记符 |
| fullName | content |  | string | 组织的全路径名称 |
| shortName | content |  | string | 组织简称 |
| logo | content |  | string | 图标 |
| code | content |  | string | 组织编号 |
| type | content |  | enum | 组织类型。
枚举项可选值列表：
NONE（空），
INSTITUTION（机构），
DEPARTMENT（部门），
OUTSIDE_INSTITUTION（外部（编外）单位），
OUTSIDE_DEPARTMENT（外部（编外）部门）， |
| typeName | content |  | string | 组织类型名称 |
| parentId | content |  | int64 | 上级组织id |
| parentName | content |  | string | 上级组织名称 |
| parentCode | content |  | string | 上级组织编号 |
| parentUnit | content |  | OrgUnitDto | 上级组织 |
| firstLevelDepartment | content |  | OrgUnitDto | 一级部门 |
| parentUnitIdCode | content |  | string | 上级组织ID(参照使用)(编号) |
| firstLevelDepartmentIdCode | content |  | string | 一级部门ID(参照使用)(编号) |
| effectiveTime | content |  | date | 生效日期，毫秒时间戳 |
| invalidTime | content |  | date | 失效日期，毫秒时间戳 |
| path | content |  | string | 全路径 |
| orgLevel | content |  | int32 | 机构层级 |
| sortId | content |  | int32 | 排序号 |
| isEnable | content |  | boolean | 状态 |
| description | content |  | string | 备注 |
| authUserIds | content |  | string | 授权用户ID集合，
只保存有效人员的id，过滤掉不符合的id |
| authUserNames | content |  | string | 授权用户名称集合 |
| businessId | content |  | int64 | 多维组织 |
| orgUnitMetadataDto | content |  | OrgUnitMetadataDto | 扩展字段 |
| orgId | orgUnitMetadataDto |  | int64 | 组织id |
| createTime | orgUnitMetadataDto |  | date | 创建时间，毫秒时间戳 |
| updateTime | orgUnitMetadataDto |  | date | 更新时间，毫秒时间戳 |
| id | orgUnitMetadataDto |  | int64 | 字段ID |
| businessId | orgUnitMetadataDto |  | int64 | 业务组织id |
| createTime | content |  | date | 创建时间 |
| updateTime | content |  | date | 更新时间 |
| address | content |  | string | 地址 |
| officeNumber | content |  | string | 电话 |
| tax | content |  | string | 税号 |
| bankAccount | content |  | string | 银行账号 |
| bank | content |  | string | 开户银行 |
| isLegalEntity | content |  | boolean | 是否法人实体 |
| socialCreditCode | content |  | string | 统一社会信用代码 |
| legalPersonName | content |  | string | 法定代表人姓名 |
| legalCertificateNumber | content |  | string | 法定代表人身份证号码 |
| legalPhoneNumber | content |  | string | 法定代表人手机号号码 |
| status |  |  | int32 | 状态 |
| code |  |  | string | 错误码 |
| message |  |  | string | 返回信息 |

响应参数示例

##### 2.1.4.2、根据组织编码查询组织详情

| 参数名称 | 父节点 | 是否必填 | 参数类型 | 参数描述 |
| --- | --- | --- | --- | --- |
| requestId |  | TRUE | string | 请求流水号。同一接入应用下的流水号不要重复；
最长32位，超过部分会被截断。 |
| timestamp |  | TRUE | int64 | 请求时间戳。请求时间和服务器时间不能相差过大，
默认5分钟以内。 |
| notifyUrl |  | TRUE | string | 异步回调URL。如果此参数非空，表示使用异步方式调用开放API，
执行结果将通过此URL异步通知调用者。 |
| data |  | TRUE | SearchUnitConditionApiDto | 请求参数数据 |
| codes | data | TRUE | array[string] | 组织编码 |
| includeDisable | data | TRUE | boolean | 是否包含失效组织，默认不包含 |
| effectiveTime | data | TRUE | string | 查询某个时间点时生效的组织,缺省为系统当前时间，
includeDisable为true的时候该字段不生效 |

| 参数名称 | 父节点 | 是否必填 | 参数类型 | 参数描述 |
| --- | --- | --- | --- | --- |
| data |  |  | ListData | 组织详情 |
| content | data |  | array[OrgUnitDataDto] | 数据集对象 |
| name | content |  | string | 组织名称 |
| shortName | content |  | string | 组织简称 |
| code | content |  | string | 组织编号 |
| type | content |  | enum | 组织类型。
枚举项可选值列表：
NONE（空），
INSTITUTION（机构），
DEPARTMENT（部门），
OUTSIDE_INSTITUTION（外部（编外）单位），
OUTSIDE_DEPARTMENT（外部（编外）部门）， |
| parentCode | content |  | string | 父组织Code,根节点不填 |
| effectiveTime | content |  | string | 生效日期 |
| invalidTime | content |  | string | 失效日期 |
| sortId | content |  | int32 | 排序号 |
| isEnable | content |  | boolean | 状态 |
| description | content |  | string | 备注 |
| metadataList | content |  | array[OrgMetadataValueDataDto] | 自定义扩展属性数据 |
| k | metadataList |  | string | 扩展字段的名称 |
| v | metadataList |  | string | 扩展字段的的值 |
| address | content |  | string | 地址 |
| officeNumber | content |  | string | 电话 |
| tax | content |  | string | 税号 |
| bankAccount | content |  | string | 银行账号 |
| bank | content |  | string | 开户银行 |
| isLegalEntity | content |  | boolean | 是否法人实体 |
| socialCreditCode | content |  | string | 统一社会信用代码 |
| legalPersonName | content |  | string | 法定代表人姓名 |
| legalCertificateNumber | content |  | string | 法定代表人身份证号码 |
| legalPhoneNumber | content |  | string | 法定代表人手机号号码 |
| createTime | content |  | date | 创建时间，毫秒时间戳 |
| updateTime | content |  | date | 更新时间，毫秒时间戳 |
| status |  |  | int32 | 状态 |
| code |  |  | string | 错误码 |
| message |  |  | string | 返回信息 |

##### 2.1.4.3、根据条件分页查询岗位

| 参数名称 | 父节点 | 是否必填 | 参数类型 | 参数描述 |
| --- | --- | --- | --- | --- |
| data |  |  | PageData | 岗位详情分页列表 |
| pageInfo | data |  | PageInfo | 分页参数对象 |
| pageNumber | pageInfo |  | int32 | 当前页数 |
| pageSize | pageInfo |  | int32 | 每页记录数 |
| pages | pageInfo |  | int32 | 总页数 |
| total | pageInfo |  | int32 | 总记录数 |
| needTotal | pageInfo |  | boolean | 是否需要查询总记录数 |
| content | data |  | array[OrgPostDto] | 数据集对象 |
| id | content |  | int64 | 岗位ID |
| name | content |  | string | 岗位名称 |
| code | content |  | string | 编号 |
| type | content |  | int64 | 岗位分类的枚举id值 |
| typeName | content |  | string | 岗位分类的枚举名称 |
| orgId | content |  | int64 | 所属组织 |
| orgName | content |  | string | 所属组织对应名称 |
| category | content |  | enum | 岗位分类。
枚举项可选值列表：
NONE（空），
BENCH_MARK（基准岗），
SELF_BUILT（自用岗）， |
| masterOrgId | content |  | int64 | 来源组织id |
| masterOrgName | content |  | string | 来源名称 |
| masterPostId | content |  | int64 | 来源岗位id |
| masterName | content |  | string | 基准岗名称 |
| issuedRule | content |  | enum | 使用范围。
枚举项可选值列表：
NONE（没有范围），
INSTITUTION（本机构），
INSTITUTIONS（本机构及下级机构），
ONLY_CHILDREN（仅下级机构），
SPECIFY_INSTITUTION（指定机构），
SPECIFY_INSTITUTIONS（指定机构及下级机构）， |
| businessId | content |  | int64 | 所属业务线id |
| sortId | content |  | int32 | 排序号 |
| isEnable | content |  | boolean | 启用状态 |
| description | content |  | string | 备注 |
| createTime | content |  | date | 创建时间，毫秒时间戳 |
| updateTime | content |  | date | 更新时间，毫秒时间戳 |
| status |  |  | int32 | 状态 |
| code |  |  | string | 错误码 |
| message |  |  | string | 返回信息 |

##### 2.1.4.4、根据条件分页查询职务

| 参数名称 | 父节点 | 是否必填 | 参数类型 | 参数描述 |
| --- | --- | --- | --- | --- |
| data |  |  | PageData | 职务详情分页列表 |
| pageInfo | data |  | PageInfo | 分页参数对象 |
| pageNumber | pageInfo |  | int32 | 当前页数 |
| pageSize | pageInfo |  | int32 | 每页记录数 |
| pages | pageInfo |  | int32 | 总页数 |
| total | pageInfo |  | int32 | 总记录数 |
| needTotal | pageInfo |  | boolean | 是否需要查询总记录数 |
| content | data |  | array[OrgJobDto] | 数据集对象 |
| id | content |  | int64 | 职务主表id |
| name | content |  | string | 职务名称 |
| code | content |  | string | 编号 |
| orgId | content |  | int64 | 组织id |
| businessId | content |  | int64 | 所属业务线id |
| category | content |  | enum | 职务类型。枚举项可选值列表：
NONE（空），
BENCH_MARK（基准岗），
SELF_BUILT（自用岗）， |
| masterOrgId | content |  | int64 | 来源组织id |
| masterOrgName | content |  | string | 来源名称 |
| masterJobId | content |  | int64 | 来源职务id |
| masterName | content |  | string | 基准职务名称 |
| issuedRule | content |  | enum | 使用范围。枚举项可选值列表：
NONE（没有范围），
INSTITUTION（本机构），
INSTITUTIONS（本机构及下级机构），
ONLY_CHILDREN（仅下级机构），
SPECIFY_INSTITUTION（指定机构），
SPECIFY_INSTITUTIONS（指定机构及下级机构）， |
| orgName | content |  | string | 组织id对应的名称(不作为入参保存) |
| sortId | content |  | int32 | 排序号 |
| isEnable | content |  | boolean | 启用状态 |
| description | content |  | string | 备注 |
| createTime | content |  | date | 创建时间，毫秒时间戳 |
| updateTime | content |  | date | 更新时间，毫秒时间戳 |
| status |  |  | int32 | 状态 |
| code |  |  | string | 错误码 |
| message |  |  | string | 返回信息 |

##### 2.1.4.5、根据条件分页查询职级

| 参数名称 | 父节点 | 是否必填 | 参数类型 | 参数描述 |
| --- | --- | --- | --- | --- |
| data |  |  | PageData | 职级详情分页列表 |
| pageInfo | data |  | PageInfo | 分页参数对象 |
| pageNumber | pageInfo |  | int32 | 当前页数 |
| pageSize | pageInfo |  | int32 | 每页记录数 |
| pages | pageInfo |  | int32 | 总页数 |
| total | pageInfo |  | int32 | 总记录数 |
| needTotal | pageInfo |  | boolean | 是否需要查询总记录数 |
| content | data |  | array[OrgLevelDto] | 数据集对象 |
| id | content |  | int64 | 职级ID |
| name | content |  | string | 职级名称 |
| code | content |  | string | 编号 |
| businessId | content |  | int64 | 所属业务线id |
| orgId | content |  | int64 | 组织id |
| levelSort | content |  | int32 | 序号 |
| isEnable | content |  | boolean | 启用状态 |
| description | content |  | string | 备注 |
| createTime | content |  | date | 创建时间，毫秒时间戳 |
| updateTime | content |  | date | 更新时间，毫秒时间戳 |
| status |  |  | int32 | 状态 |
| code |  |  | string | 错误码 |
| message |  |  | string | 返回信息 |

##### 2.1.4.6、根据条件查询人员信息

| 参数名称 | 父节点 | 是否必填 | 参数类型 | 参数描述 |
| --- | --- | --- | --- | --- |
| data |  |  | ListData | 人员详情列表 |
| content | data |  | array[OrgMemberDto] | 数据集对象 |
| id | content |  | int64 | 人员id,新建时不必填，修改时必填 |
| thirdId | content |  | string | 第三方唯一标识 |
| name | content |  | string | 姓名 |
| defaultName | content |  | string | 默认语种姓名 |
| mnemonic | content |  | string | 助记符 |
| code | content |  | string | 编号 |
| image | content |  | string | 头像id |
| gender | content |  | enum | 性别。枚举项可选值列表：
NONE（空），
MALE（男），
FEMALE（女），
UN_KNOW（未知）， |
| birthday | content |  | date | 出生日期 |
| phoneNumber | content |  | string | 手机号码 |
| officeNumber | content |  | string | 工作电话 |
| email | content |  | string | 邮箱 |
| effectiveTime | content |  | date | 生效日期，毫秒时间戳 |
| invalidTime | content |  | date | 失效日期，毫秒时间戳 |
| sortId | content |  | int32 | 排序号 |
| isEnable | content |  | boolean | 状态 |
| description | content |  | string | 备注 |
| orgMemberPostDtoList | content |  | array[OrgMemberPostDto] | 人员所有任职信息 |
| id | orgMemberPostDtoList |  | int64 | 任职信息id |
| businessId | orgMemberPostDtoList |  | int64 | 业务组织id(缺省行政组织) |
| businessName | orgMemberPostDtoList |  | string | 业务组织名称(缺省行政组织) |
| memberIdCode | orgMemberPostDtoList |  | string | 人员id(编号) |
| memberName | orgMemberPostDtoList |  | string | 人员名称 |
| memberCode | orgMemberPostDtoList |  | string | 人员编号 |
| main | orgMemberPostDtoList |  | boolean | 是否主岗 |
| orgIdCode | orgMemberPostDtoList |  | string | 所属组织(编号) |
| orgName | orgMemberPostDtoList |  | string | 所属组织名称 |
| orgCode | orgMemberPostDtoList |  | string | 所属组织编号 |
| fullName | orgMemberPostDtoList |  | string | 组织全路径名称 |
| path | orgMemberPostDtoList |  | string | path |
| institutionIdCode | orgMemberPostDtoList |  | string | 组织所属机构(编号) |
| institutionName | orgMemberPostDtoList |  | string | 组织所属机构名称 |
| institutionCode | orgMemberPostDtoList |  | string | 组织所属机构编号 |
| postIdCode | orgMemberPostDtoList |  | string | 岗位(编号) |
| postName | orgMemberPostDtoList |  | string | 岗位名称 |
| postCode | orgMemberPostDtoList |  | string | 岗位编号 |
| levelIdCode | orgMemberPostDtoList |  | string | 职级(编号) |
| levelName | orgMemberPostDtoList |  | string | 职级名称 |
| levelCode | orgMemberPostDtoList |  | string | 职级编号 |
| jobId | orgMemberPostDtoList |  | int64 | 职务 |
| jobName | orgMemberPostDtoList |  | string | 职务名称 |
| jobCode | orgMemberPostDtoList |  | string | 职务编号 |
| effectiveTime | orgMemberPostDtoList |  | date | 生效日期，毫秒时间戳 |
| invalidTime | orgMemberPostDtoList |  | date | 失效日期，毫秒时间戳 |
| sortId | orgMemberPostDtoList |  | int32 | 排序号 |
| topSortId | orgMemberPostDtoList |  | int32 | 优先排序顺序 |
| isEnable | orgMemberPostDtoList |  | boolean | 状态 |
| effective | orgMemberPostDtoList |  | boolean | 生效状态 |
| edit | orgMemberPostDtoList |  | boolean | 是否可编辑 |
| createTime | orgMemberPostDtoList |  | date | 创建时间，毫秒时间戳 |
| updateTime | orgMemberPostDtoList |  | date | 更新时间，毫秒时间戳 |
| type | orgMemberPostDtoList |  | enum | 账号类型。枚举项可选值列表：
NONE（空），
MEMBER（内部人员），
EXTERNAL_MEMBER（外部联系人）， |
| memberType | orgMemberPostDtoList |  | enum | 人员类型。枚举项可选值列表：
NONE（空），
MEMBER（内部人员），
OUTSIDE_MEMBER（外部单位用户），
NATURAL_MEMBER（外部个人用户）， |
| outsideInstitutionId | orgMemberPostDtoList |  | int64 | 人员所在外部单位 |
| mainMemberPost | content |  | OrgMemberPostDto | 人员主岗任职信息 |
| id | mainMemberPost |  | int64 | 任职信息id |
| businessId | mainMemberPost |  | int64 | 业务组织id(缺省行政组织) |
| businessName | mainMemberPost |  | string | 业务组织名称(缺省行政组织) |
| memberIdCode | mainMemberPost |  | string | 人员id(编号) |
| memberName | mainMemberPost |  | string | 人员名称 |
| memberCode | mainMemberPost |  | string | 人员编号 |
| main | mainMemberPost |  | boolean | 是否主岗 |
| orgIdCode | mainMemberPost |  | string | 所属组织(编号) |
| orgName | mainMemberPost |  | string | 所属组织名称 |
| orgCode | mainMemberPost |  | string | 所属组织编号 |
| fullName | mainMemberPost |  | string | 组织全路径名称 |
| path | mainMemberPost |  | string | path |
| institutionIdCode | mainMemberPost |  | string | 组织所属机构(编号) |
| institutionName | mainMemberPost |  | string | 组织所属机构名称 |
| institutionCode | mainMemberPost |  | string | 组织所属机构编号 |
| postIdCode | mainMemberPost |  | string | 岗位(编号) |
| postName | mainMemberPost |  | string | 岗位名称 |
| postCode | mainMemberPost |  | string | 岗位编号 |
| levelIdCode | mainMemberPost |  | string | 职级(编号) |
| levelName | mainMemberPost |  | string | 职级名称 |
| levelCode | mainMemberPost |  | string | 职级编号 |
| jobId | mainMemberPost |  | int64 | 职务 |
| jobName | mainMemberPost |  | string | 职务名称 |
| jobCode | mainMemberPost |  | string | 职务编号 |
| effectiveTime | mainMemberPost |  | date | 生效日期，毫秒时间戳 |
| invalidTime | mainMemberPost |  | date | 失效日期，毫秒时间戳 |
| sortId | mainMemberPost |  | int32 | 排序号 |
| topSortId | mainMemberPost |  | int32 | 优先排序顺序 |
| isEnable | mainMemberPost |  | boolean | 状态 |
| effective | mainMemberPost |  | boolean | 生效状态 |
| edit | mainMemberPost |  | boolean | 是否可编辑 |
| createTime | mainMemberPost |  | date | 创建时间，毫秒时间戳 |
| updateTime | mainMemberPost |  | date | 更新时间，毫秒时间戳 |
| type | mainMemberPost |  | enum | 账号类型。枚举项可选值列表：
NONE（空），
MEMBER（内部人员），
EXTERNAL_MEMBER（外部联系人）， |
| memberType | mainMemberPost |  | enum | 人员类型。枚举项可选值列表：
NONE（空），
MEMBER（内部人员），
OUTSIDE_MEMBER（外部单位用户），
NATURAL_MEMBER（外部个人用户）， |
| outsideInstitutionId | mainMemberPost |  | int64 | 人员所在外部单位 |
| mainMemberPostId | content |  | int64 | 人员主岗任职Id信息 |
| orgMemberMetadataDto | content |  | OrgMemberMetadataDto | 扩展字段 |
| memberId | orgMemberMetadataDto |  | int64 | 人员id |
| createTime | orgMemberMetadataDto |  | date | 创建时间，毫秒时间戳 |
| updateTime | orgMemberMetadataDto |  | date | 更新时间，毫秒时间戳 |
| id | orgMemberMetadataDto |  | int64 | 字段ID |
| businessId | orgMemberMetadataDto |  | int64 | 业务组织id |
| loginName | content |  | string | 用户名 |
| createTime | content |  | date | 创建时间，毫秒时间戳 |
| updateTime | content |  | date | 更新时间，毫秒时间戳 |
| certificateType | content |  | int64 | 证件类型 |
| certificateNumber | content |  | string | 证件号码 |
| entryDate | content |  | date | 入职日期 |
| bankAccount | content |  | string | 银行账号 |
| bank | content |  | string | 开户银行 |
| bankOutlets | content |  | string | 开户网点 |
| memberType | content |  | enum | 人员类型。
枚举项可选值列表：
NONE（空），
MEMBER（内部人员），
OUTSIDE_MEMBER（外部单位用户），
NATURAL_MEMBER（外部个人用户）， |
| pinyinShort | content |  | string | 简拼 |
| nickName | content |  | string | 昵称 |
| orgName | content |  | string | 主部门名称 |
| postName | content |  | string | 主岗位名称 |
| jobName | content |  | string | 主职务名称 |
| levelName | content |  | string | 主职级名称 |
| naturalMemberType | content |  | int64 | 外部个人用户类型 |
| status |  |  | int32 | 状态 |
| code |  |  | string | 错误码 |
| message |  |  | string | 返回信息 |

##### 2.1.4.7、分页查询组织下人员

| 参数名称 | 父节点 | 是否必填 | 参数类型 | 参数描述 |
| --- | --- | --- | --- | --- |
| requestId |  | TRUE | string | 请求流水号。同一接入应用下的流水号不要重复；

最长32位，超过部分会被截断。 |
| timestamp |  | TRUE | int64 | 请求时间戳。请求时间和服务器时间不能相差过大，
默认5分钟以内。 |
| notifyUrl |  | TRUE | string | 异步回调URL。如果此参数非空，
表示使用异步方式调用开放API，执行结果将通过此URL异步通知调用者。 |
| params |  | TRUE | SearchMemberApiDto | 泛型参数对象 |
| code | params | TRUE | string | 组织code |
| includeChild | params | TRUE | boolean | 是否包含下级 |
| effectiveTime | params | TRUE | string | 人员生效时间,缺省系统当前时间，
配置了搜索开始/结束时间，该值不生效 |
| startTime | params | TRUE | string | 搜索开始时间 |
| endTime | params | TRUE | string | 搜索结束时间 |
| includeDisable | params | TRUE | boolean | 是否包含失效人员，默认不包含 |
| memberType | params | TRUE | enum | 人员类型。枚举项可选值列表：
NONE（空），
MEMBER（内部人员），
OUTSIDE_MEMBER（外部单位用户），
NATURAL_MEMBER（外部个人用户）， |
| sort |  | TRUE | Sort | 排序 |
| orders | sort | TRUE | array[Sort$Order] | 排序 |
| direction | orders | TRUE | enum | 顺序,可用值:ASC,DESC。
枚举项可选值列表：ASC（ASC），DESC（DESC）， |
| property | orders | TRUE | string | 字段,可用值:DTO属性(请参照"响应参数"中content),
createTime,updateTime |
| pageInfo |  | TRUE | PageInfo | 分页 |
| pageNumber | pageInfo | TRUE | int32 | 当前页数 |
| pageSize | pageInfo | TRUE | int32 | 每页记录数 |
| pages | pageInfo | TRUE | int32 | 总页数 |
| total | pageInfo | TRUE | int32 | 总记录数 |
| needTotal | pageInfo | TRUE | boolean | 是否需要查询总记录数 |

| 参数名称 | 父节点 | 是否必填 | 参数类型 | 参数描述 |
| --- | --- | --- | --- | --- |
| data |  |  | PageData | 人员信息分页列表 |
| pageInfo | data |  | PageInfo | 分页参数对象 |
| pageNumber | pageInfo |  | int32 | 当前页数 |
| pageSize | pageInfo |  | int32 | 每页记录数 |
| pages | pageInfo |  | int32 | 总页数 |
| total | pageInfo |  | int32 | 总记录数 |
| needTotal | pageInfo |  | boolean | 是否需要查询总记录数 |
| content | data |  | array[OrgMemberDataDto] | 数据集对象 |
| thirdId | content |  | string | 第三方唯一标识 |
| name | content |  | string | 姓名 |
| code | content |  | string | 编号 |
| username | content |  | string | 用户名 |
| gender | content |  | enum | 性别。枚举项可选值列表：
NONE（空），
MALE（男），
FEMALE（女），
UN_KNOW（未知）， |
| birthday | content |  | string | 出生日期 |
| phoneNumber | content |  | string | 手机号码 |
| officeNumber | content |  | string | 工作电话 |
| email | content |  | string | 邮箱 |
| effectiveTime | content |  | string | 生效日期 |
| invalidTime | content |  | string | 失效日期 |
| sortId | content |  | int32 | 排序号 |
| isEnable | content |  | boolean | 状态 |
| description | content |  | string | 备注 |
| memberPosts | content |  | array[OrgMemberPostDataDto] | 人员的任职信息 |
| main | memberPosts |  | boolean | 是否主岗 |
| unitCode | memberPosts |  | string | 组织编码 |
| postCode | memberPosts |  | string | 岗位编码(内部人员必填) |
| levelCode | memberPosts |  | string | 职级编码 |
| jobCode | memberPosts |  | string | 职务编码 |
| effectiveTime | memberPosts |  | string | 生效日期 |
| invalidTime | memberPosts |  | string | 失效日期 |
| sortId | memberPosts |  | int32 | 排序号 |
| topSortId | memberPosts |  | int32 | 优先置顶排序 |
| isEnable | memberPosts |  | boolean | 状态 |
| memberType | memberPosts |  | enum | 人员类型。枚举项可选值列表：
NONE（空），
MEMBER（内部人员），
OUTSIDE_MEMBER（外部单位用户），
NATURAL_MEMBER（外部个人用户）， |
| metadataList | content |  | array[OrgMetadataValueDataDto] | 自定义扩展属性数据 |
| k | metadataList |  | string | 扩展字段的名称 |
| v | metadataList |  | string | 扩展字段的的值 |
| certificateType | content |  | string | 证件类型 |
| certificateNumber | content |  | string | 证件号码 |
| entryDate | content |  | string | 入职日期 |
| bankAccount | content |  | string | 银行账号 |
| bank | content |  | string | 开户银行 |
| bankOutlets | content |  | string | 开户网点 |
| image | content |  | string | 头像路径 |
| memberType | content |  | enum | 人员类型。枚举项可选值列表：
NONE（空），MEMBER（内部人员），
OUTSIDE_MEMBER（外部单位用户），
NATURAL_MEMBER（外部个人用户）， |
| createTime | content |  | date | 创建时间，毫秒时间戳 |
| updateTime | content |  | date | 更新时间，毫秒时间戳 |
| status |  |  | int32 | 状态 |
| code |  |  | string | 错误码 |
| message |  |  | string | 返回信息 |

### 2.2 三方异构系统提供写入OpenAPI，由COP定时调用接口主动推送，完成组织同步模式。

#### 2.2.2应用场景

三方系统有标准的rest组织同步接口，COP通过应用集成配置进行组织同步任务设置，cop可以前端配置定时同步任务同时可以进行手动触发同步。

#### 2.2.3同步操作步骤

| 序号 | 步骤名称 | 责任方 | 使用场景 |
| --- | --- | --- | --- |
| 1 | 提供组织增量写入接口规范和文档 | 三方系统 | 必须， |
| 2 | 注册并配置鉴权AppID和秘钥 | 三方系统 | 非必须，如果三方系统接口调用时涉及到安全鉴权，则需要提供 |
| 3 | 提供接口调用示例 | 三方系统 | 必须，为了集成效率，
强烈建议三方系统提供可直接使用的postman接口调用示例， |
| 4 | 新建三方集成应用 | 致远 | 必须，三方集成应用负责封装三方系统接口和配置数据映射 |
| 5 | 发布启用三方集成应用 | 致远 | 必须，三方集成应用只有发布后才能正常使用 |
| 6 | 封装安全认证 | 致远 | 非必须，如果三方系统接口调用时涉及到安全鉴权，则需要配置安全认证 |
| 7 | 接口封装 | 致远 | 必须，三方系统提供的接口只有正常封装后才能供给COP使用 |
| 8 | 在线调试验证 | 致远 | 必须，三方系统接口封装完成后，需要在线调试，验证网络通信、
接口返回结果是否正确等 |
| 9 | 启用组织同步 | 致远 | 必须，主动推送场景中，字段映射、同步周期需要在基础集成中配置 |
| 10 | 配置同步内容 | 致远 | 必须，本场景下固定选择模式为：从三方系统获取 |
| 11 | 配置同步周期 | 致远 | 必须，根据数据量和服务器消费能力，合理配置同步周期 |
| 12 | 配置字段映射 | 致远 | 必须：三方系统接口文档中的字段名，字段释义与COP不一致，
需要配置参数映射、层级转换等 |
| 13 | 使用日志 | 致远 | 必须，配置完成并启用后，查看使用日志 |

#### 2.2.4集成配置

##### 2.2.4.1 新建三方集成应用

操作入口：管理后台-->三方应用集成-->集成应用管理

<img width="1266.6666666666667">

##### 2.2.4.2应用基础信息配置

<img width="1286">

##### 2.2.4.3接口配置

新增一个分类用于存放组织同步所需接口，创建1个认证接口以及分别获取单位、部门、人员接口)接口注册可参考：
接口注册

（注：如果三方接口需要认证，认证接口必须存在）

<img width="1276">

###### 2.2.4.3.1 配置认证接口

<img width="1274">

###### 2.2.4.3.2配置请求前认证

配置完请求认证接口之后需要将该接口配置为请求前认证，这样在其他接口请求时会优先请求该认证接口并将该接口返回的认证信息赋值在当前请求的接口中。

<img width="1270">

###### 2.2.4.3.3、配置获取单位信息接口

<img width="1920">

●
要求结构必须一致，配置方式见：配置技巧

###### 2.2.4.3.4、配置获取部门信息接口

###### 2.2.4.3.5、配置获取人员信息接口

配置技巧

Body参数在首层配置数组(对象)

<img width="1060">

##### 2.2.4.4同步配置

###### 2.2.4.4.1同步模式选择

<img width="863.3333333333334">

###### 2.2.4.4.2同步内容映射配置

<img width="1263.3333333333333">

<img width="799.3333333333334">

返回参数映射必须设置

<img width="804">

###### 2.2.4.4.3运行配置

<img width="912">

该同步模式下也可以选在实时同步，只需在运行配置中开启事件监听即可

<img width="833.3333333333334">

#### 2.2.5同步日志查看

操作入口：管理后台-->三方应用集成-->集成应用管理-->日志
