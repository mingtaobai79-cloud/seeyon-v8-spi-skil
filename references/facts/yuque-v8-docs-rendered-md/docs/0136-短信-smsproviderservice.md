---
title: "短信"
source: "https://www.yuque.com/seeyonkk/v8/smsproviderservice"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 短信

> Source: https://www.yuque.com/seeyonkk/v8/smsproviderservice

文档版本：v1.0.0
适用版本：cip-capability 3.12.61，其他版本待验证
最后更新：2025-08-13

## 1. 应用场景

1
系统通知短信发送

示例：

置消息分类设置
(ZHCN:安全生产管理端
(ZHCN:法务管理系统
统消息设置邮件
三重一大系
(ZHCN":智慧党建系统
组织架构同
复默认设置
业邮箱邦
?领导日程
修改密码
蓝委集
方系统账户映
息提醒设
统参数
用语设
息提醒设置
理设置
文档管理
图个人信息设置
?任务管理
公告
账号在线管理
其他设盖
请输入
作设置
邮件消息设置
工资条
账号与安
设置
个人设置

○
系统事件通知

○
工作流提醒

○
待办提醒

○
.....

2
验证码短信发送

○
登录验证码

## 2. 开发环境搭建

### 2.1 创建工程

1
工程命名规范：

```
cip-capability-sms-{项目标识}
示例：cip-capability-sms-hodo
```

2
目录结构：

```
cip-capability-sms-{项目标识}/
├── target/                                    # 编译输出目录
│   └── cip-capability-sms-{项目标识}-{version}.jar       # 编译后的jar包
├── src/                                      # 源代码目录
│   └── main/
│       ├── java/
│       │   └── com/seeyon/cip/spi/capability/{项目标识}/
│       │       ├── service/
│       │       │   └── {项目标识}SmsServiceImpl.java  # 短信服务实现类
│       │       └── dto/
│       │           └── SmsProperties.java     # 配置属性类
│       └── resources/
│           └── META-INF/
│               └── spring.factories           # Spring SPI配置文件
└── pom.xml                                   # 项目依赖配置文件
```

### 2.2 配置依赖

```xml
<groupId>com.seeyon</groupId>
<artifactId>cip-capability-sms-{项目标识}</artifactId>
<version>1.0.0-SNAPSHOT</version>
<packaging>jar</packaging>
<dependencies>
    <!-- 必要的依赖 -->
    <dependency>
        <groupId>com.seeyon</groupId>
        <artifactId>cip-capability-api</artifactId>
        <version>3.8.5</version>
    </dependency>
</dependencies>
```

## 3. 核心接口实现

### 3.1 SPI配置文件

在 src/main/resources/META-INF/ 目录下创建 spring.factories 文件：

### 3.2 服务实现类

服务实现类需要实现SmsProviderService接口：

### 3.3 配置对象

创建配置属性类：

## 4. 实现案例：红豆电信短信通道

本章节以红豆电信短信服务为例，详细说明如何实现一个完整的短信通道适配。

### 4.1 项目结构

### 4.2 核心代码实现

#### 4.2.1 配置属性类（SmsProperties.java）

#### 4.2.2 短信服务实现类（HodoSmsServiceImpl.java）

主要实现特点：

1
配置管理：

○
使用SmsProperties类管理配置参数

2
日志完善：

○
详细的调用信息记录

○
异常信息跟踪

○
关键步骤日志

3
代码规范：

○
清晰的方法命名

○
完整的注释说明

4
扩展性：

○
支持自定义消息模板

○
灵活的参数配置

○
可扩展的实现方式

## 5. 常见问题

### 5.1 不显示[短信消息提醒设置]

1
已经启用短信通道后，在消息设置中会出现【短信消息设置】页签，进行自定义选择短信提醒业务。

2
是否显示【短信消息设置】页签，3.12版本之前受license插件控制，3.12版本及以后，默认都显示。

## 6. 系统参数配置&实现效果

### 6.1 配置通道基本信息参数

1
登录后台管理界面(需要登录对应租户管理员)

2
进入：集成平台 > 基础能力接入 > 短信

3
选择[红豆电信-网关]通道类型

4
填写服务参数配置

<img width="1920">

### 6.2 配置[签名管理]

1
选择[签名管理]页签

2
点击[导入]按钮

3
下载签名模版

4
填写签名信息（示例: sms-standard-signature.xls ）

5
上传签名

<img width="1920">

<img width="1219">

<img width="1920">

### 6.3 配置[模版管理]

1
选择[模版管理]页签3

3
下载短信模版

4
填写短信模版信息（示例： sms-standard-template.xls ）

5
上传短信模版，上传成功后模版显示[审核通过]

6
设置签名，每个短信模版都要设置签名

<img width="1901">

<img width="1768">

<img width="1546">

<img width="1920">

<img width="1920">

### 6.4 启动当前通道

1
点击[启动]按钮

### 6.5 短信消息提醒设置

#### 6.5.1 由管理员统一配置消息提醒

1
登录后台管理界面

2
进入：基础设置 > 消息提醒设置 > 短信消息设置

3
选择需要短信提醒的业务

4
点击确定

#### 6.5.2 由用户自定义消息提醒配置

1
登录前台界面

2
进入：个人设置 > 消息提醒设置 > 短信消息设置

注意事项：

1
模板管理中的会有预制模板，如果需要预制模板，需要审核通过；例如：如果是草稿状态，在走消息提醒时日志中会出现模板短信不存在；

2
自定义模板的使用，使用某个场景时需要有选择自定义短信模板；例如：流程图中选择消息节点，可选择自定义短信模板;

3
短信模板需要找厂商提供;

### 6.6 短信登录参数配置

注意：在登录时需要短信验证码的需求才需配置

参照文档：

[【集成】V8短信登录配置说明]: https://open.seeyoncloud.com/#/faq/faq/v1/share?url=Z2JySmU+NDM6Og==	"短信登录配置说明"
