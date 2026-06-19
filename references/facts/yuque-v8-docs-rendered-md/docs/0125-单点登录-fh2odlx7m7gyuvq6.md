---
title: "单点登录"
source: "https://www.yuque.com/seeyonkk/v8/fh2odlx7m7gyuvq6"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 单点登录

> Source: https://www.yuque.com/seeyonkk/v8/fh2odlx7m7gyuvq6

作者：杨映海
最后更新：2025-04-08

## 1. 应用场景

三方异构系统免密单点登录至V8平台指定页面

## 2. V8平台认证

适用场景：用户身份由V8平台识别，三方系统调V8标准接口完成接入，V8平台无需代码开发。

### -2.3,返回临时授权码SYTOKEN
2.2,验证用户有效性
APPKEYAPPSECRET
请求COP平台应用
携带时授权码SVTOKER
输入账号密码
2.1,携带当前用户信息
3.2交险SYTOKEN
,按要求拼接免登地址
1,账号密码校验
分配临时授权秘必钥
重定向到目示URL
COP平台应用
模摸拟登陆
1,URL问
2,准备访问
成功登录
COP平台
待接入系统
览器
ACTOR
2.1 接入应用

参照：
应用接入
接入应用，并获取接口appKey和appSecret

### 2.2 获取免登授权码

接口地址：【COP平台访问域名】/service/ctp-user/auth/avoid/sytoken（请求方式：POST）

请求参数说明：（body）

| 参数名称 | 是否必填 | 参数类型 | 参数描述 |
| --- | --- | --- | --- |
| responseType | TRUE | string | 请求类型，
固定值：create |
| clientId | TRUE | string | 应用ID，操作步骤中的接入应用-AppKey
例如：cd13f41d30f44d438b05b6588411178f |
| dataType | TRUE | string | 用户标识键，双方约定的用户标识字段，标识用于生成签名的用户标识键等于COP平台的对应字段
枚举值：
loginName=用户名；
mobile=手机号码；
code=用户编号；
email=邮箱；
userid=用户ID； |
| dataValue | TRUE | string | AES用户信息加密；当dataType=mobile时,用户手机号码为17300001234，则明文为17300001234
加密配置信息：
明文：17300001234
模式：CBC固定模式不可变；
填充：Pkcs7或Pkcs5固定类型不可变；
偏移量：apaasseeyonv8com 固定值不可变
密文编码：HEX类型不可变；
秘钥：接入应用分配的AppSecret，例如：93ec877511d24dda8cf86a9d7870f681
加密后结果集示例：6d52cb81d4f8ee6359b0559f3aa0bcba
AES在线加密参考网站：http://tool.lvtao.net/aes |
| signature | TRUE | string | 签名函数，以下四个参数经过自然排序后，拼接成一个字符串，使用SHA256加密
加密前四个参数：
AppKey(接入应用分类的AppKey);
AppSecret(接入应用分配的AppSecret);
data(加密后的用户信息dataValue);
时间戳：请求参数中的timestamp；
如对 “abcd” 进行签名后的结果为 “88d4266fd4e6338d13b845fcf289579d209c897823b9217da3e161936f031589”
SHA256在线加密参考网站：https://crypot.51strive.com/sha256.html |
| timestamp | TRUE | string | 毫秒级时间戳，参与生成签名；
例如：“1720669311740” |

### 2.3 组装SSO地址

#### 3.3.1 基本格式

#### 3.3.2 参数说明

| 参数名称 | 参数说明 | 示例值 |
| --- | --- | --- |
| V8平台访问域名 | V8平台前台访问域名 | http://dev-xtcv8.seeyoncloud.com |
| Web端待跳转地址 | 免登成功后需要跳转的V8平台地址 | /main/portal |
| 移动端待跳转地址 | 免登成功后需要跳转的V8平台地址 | /main-mobile/portal |
| appKey | V8平台为每个应用分配的AppKey | b575c80cecc45826a3d42bdb7389df52 |
| 免登授权码 | 通过接口获取的免登授权码 | SY-oi6tkwsxht7knsby |

#### 2.3.3 注意事项

1
urlencode: 为了防止出现参数冲突，【Web端待跳转地址】和【移动端待跳转地址】需要采用url编码后再拼接到免登地址中

2
sytype: 固定值为"sytoken"

3
syid: 使用申请到的appKey

4
sytoken: 通过"获取免登授权码"接口获取的授权码

#### 2.3.4 示例

说明：

●
Web端跳转地址"/main/portal"编码后为"%2Fmain%2Fportal"

●
移动端跳转地址"/main-mobile/portal"编码后为"%2Fmain-mobile%2Fportal"

●
在浏览器地址栏访问以上URL即可免登进入V8平台首页

### 2.4 验证免登授权码

适用场景：用于校验免登授权码是否有效，不用频繁调用接口获取登录验证码

请求地址：【V8平台访问域名】/service/ctp-user/auth/avoid/sycheck（请求方式：GET）

#### 3.4.1 请求参数说明

| 参数名称 | 是否必填 | 参数类型 | 参数描述 |
| --- | --- | --- | --- |
| sytoken | TRUE | string | 免登授权码例如：SY-o5vtq1z3bnvecwta |
| syid | TRUE | string | 接入应用AppKey例如：cd13f41d30f44d438b05b6588411178f |

#### 3.4.2 返回值说明

| 参数名称 | 父节点 | 参数类型 | 参数描述 |
| --- | --- | --- | --- |
| data |  | SingleData | 返回值数据 |
| content | data | void | 数据对象 |
| sytokenValid | content | string | 授权码是否有效 |
| syidValid | content | string | syid/AppKey/ClientId是否有效 |
| validity | content | string | 授权码剩余可使用次数 |
| status |  | int32 | 状态 |
| code |  | string | 错误码 |
| message |  | string | 返回信息 |

### 2.5 单点注销

适用场景：用于三方系统注销后，同步注销V8用户

请求地址：【V8平台访问域名】/service/ctp-user/auth/token/revoke-by-token（请求方式：POST）

| 参数名称 | 是否必填 | 参数类型 | 参数描述 |
| --- | --- | --- | --- |
| token | TRUE | string | 免登授权码例如：SY-o5vtq1z3bnvecwta |

### 2.6. 示例代码

## 3. 三方系统认证

适用场景：用户身份由三方系统识别，V8平台调用三方系统接口获取人员真实身份。

<img width="1437">

详细实现细节请参照：
三方单点到V8
