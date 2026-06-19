---
title: "单点登录"
source: "https://www.yuque.com/seeyonkk/v8/thg6ef7ur7gs4f6b"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 单点登录

> Source: https://www.yuque.com/seeyonkk/v8/thg6ef7ur7gs4f6b

作者：拓春慧
最后更新：2025-04-15

## 1、应用场景

协同平台与第三方系统进行互信认证，用户在协同平台系统点击第三方系统图标/菜单，可以无需二次输入用户名和密码直接打开第三方系统。

## 2、V8平台认证

适用场景：用户身份由V8平台识别，三方系统回调V8标准接口完成握手身份识别，V8平台无需代码开发。

解析TICKET获取用户信息,完成登录逻辑
一成功免登跳转到目标页面
回调接口获取TICKET对应用户信息
三方系统
携带TICKET访I
V8平台
浏览器
登录V8平台

### 2.1 免登配置

操作入口：管理后台-->集成平台-->三方应用集成-->集成应用管理-->免登

默认跳转地址,可以为空
单点登录类型:协同认证-V8
默认跳转地址:HTTP://BAIDUCO
单点类型选择
用户映射
点登录

### 2.2 菜单配置

操作入口：管理后台-->集成平台-->三方应用集成-->集成应用管理-->菜单

单点是默认会在该地址后面追加TICKET
HTTP://BAIDU.CON
OTHERSYSTEMYY
WEB端菜单
V8_OTHERSYSTEMYY
公
8OTHERSYSTEMYY
链接地址
链接地址
移动端菜单
单点登录
WEB端菜单
方系统
编辑菜单
菜单名称
上级菜单
单角标
菜单图标
三方系统
创定
取消
O
8
删除
层级
Y
菜单
编辑
锭

### 2.3 单点跳转

协同平台登录成功后，点击三方系统菜单前，会根据当前登录用户信息，生成临时授权码，在三方原始菜单地址后拼接参数ticket，三方系统拦截ticket参数，根据【根据ticket获取用户信息】接口获取用户信息，模拟登陆，实现免登进入三方系统。

<img width="831">

例：下列地址，绿色为第三方提供地址，协同平台会在地址后面拼接红色ticket参数，后台通过request对象获取参数值：

https://www.baidu.com/?ticket=uk0jnxh8kk89ighsox5nnmlafecwrr08

<img width="755">

### 2.4 回调接口

请求地址 ：https://ip:port/service/ctp-user/auth/restore

请求方式 ：POST

请求参数 ：ticket （用户登录后，由用户中心拼接在重定向地址最后的临时授权ticket）

#### 2.4.1请求示例

#### 2.4.2返回示例

#### 2.4.3返回参数说明

| 参数名称 | 上级节点 | 参数类型 | 参数描述 |
| --- | --- | --- | --- |
| status | – | int | 状态码 |
| code | – | string | 响应码 |
| message | – | string | 响应信息 |
| data | – | object |  |
| content | data | object |  |
| code | content | string | 编号 |
| orgName | content | string | 所属组织 |
| tenantCode | content | string | 租户编码 |
| type | content | string | 账号类型。枚举项可选值列表：NONE（空），MEMBER（内部人员），EXTERNAL_MEMBER（外部联系人） |
| socialCreditCode | content | string | 统一社会信用代码 |
| orgId | content | string | 所属组织ID |
| phoneNumber | content | string | 手机号码 |
| outsideOrgName | content | string | 外部单位名称 |
| outsideOrgCode | content | string | 外部单位编码 |
| orgCode | content | string | 所属组织编码 |
| loginName | content | string | 用户名/登录名 |
| name | content | string | 姓名 |
| outsideOrgId | content | string | 外部单位ID |
| allTenantUserInfo | content | array | 所有租户任职信息 |
| code | allTenantUserInfo | string | 编号 |
| orgName | allTenantUserInfo | string | 所属组织名称 |
| tenantCode | allTenantUserInfo | string | 租户编码 |
| type | allTenantUserInfo | string | 账号类型。枚举项可选值列表：NONE（空），MEMBER（内部人员），EXTERNAL_MEMBER（外部联系人） |
| socialCreditCode | allTenantUserInfo | string | 统一社会信用代码 |
| orgId | allTenantUserInfo | string | 所属组织ID |
| phoneNumber | allTenantUserInfo | string | 手机号码 |
| outsideOrgName | allTenantUserInfo | string | 外部单位名称 |
| outsideOrgCode | allTenantUserInfo | string | 外部单位编码 |
| orgCode | allTenantUserInfo | string | 所属组织编码 |
| loginName | allTenantUserInfo | string | 用户名/登录名 |
| name | allTenantUserInfo | string | 姓名 |
| outsideOrgId | allTenantUserInfo | string | 外部单位ID |

### 2.5.代码示例

## 3、三方系统认证

### 3.1、预置三方认证

一些常用系统的单点认证，平台已经预置。项目上直接使用即可，如：JIRA、用友、263邮箱、oAuth2.0等

<img width="1485.5">

### 3.2、自定义三方认证

适用场景：用户身份由三方系统识别，V8平台调用三方系统接口获取人员真实身份且通过标品无法配置出来。

详细实现细节请参照：
V8单点到三方
