---
title: "开发准备"
source: "https://www.yuque.com/seeyonkk/v8/fqdmdrodt7x7p6no"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 开发准备

> Source: https://www.yuque.com/seeyonkk/v8/fqdmdrodt7x7p6no

适用版本：3.18

作者：杨映海
最后更新：2025-04-11

## 1. GIT帐号开通

联系项目运维工程师开通GIT帐号并授权代码分组

## 2、后端代码开发

### 2.1. SPI扩展代码

#### 2.1.1 Git地址获取

入口：开发环境-->system-admin账号登录后台-->系统管理-->客开管理

TTPS://V8GIT.SEEYONV8.COM/A9/DE
/EXTEND/FRONTEND/CUSTOM
EXTEND/BACKEND/CUSTOM-BACKEN
HTTPS://V8GIT.SEEYONV8.COM/A9/DEV
协同运营平台
MAVENSETTINGSXML下载
2025-04-1510:2437
理首页客开管理
CUSTOM-FRONTEND
GITLAB工程名称
导出日志
GITLAB工程地址
CUSTOM-BACKEND
2025-04-1517:29:3
构建成功
客户端资原类型
FRONTENDQ
租户推送
8关闭全部
上次构建时间
客开管理
吕系统升级
司客开管理
国应用管理
灰度发布
租户管理
LICENSE管
后端扩广展
系统巡检
田环境配置
构建导
构建成功
0昌
系统监控
构建状态
前扩广展
构建
工具集
操作
导出日志

#### 2.1.2 工程结构解析

第三方JAR的存放位置,文件名固定
SP生效的范围配置文件
ECOMSEEYONEXTENDSPI.WORKFLOWSERVICE
每个SP对应的子工程
指定SP接口和对应的实现类
LDCUSTOM-BACKEND[BOOT-STARTERSPI-CUSTOMIZ
DROPFILESHERETOOPENTHEM
NAVIGATIONBARALT+HOME
SEARCHEVERYWHEREDOUBLESHIF
需要白己实现的后端代码
后端代码父级工程
GOTOFILECTRL+SHIFT+R
CBPMDETAIVIEWSERVICELMPL
一个MODULE对应一个SPL
>EPRIVATEJAVASDKJAR
RECENTFILESCTRL+E
LDSPI-WORKFLOW
CSPRING.FACTORIES
METADATA
READMEMD
>ASPI-FILE
OMETA-INF
CDSPI-MOBILE
TSPIINFOJSOR
DTHIRD-IAR
LRESOURCES
OMAIN
MPOM.XM
JSRC
口JAVA
LDSPI-SSO
MPOM.XM
CUSTOMIZED

#### 2.1.3 相关配置说明

```
{
  "name": "boot-starter-spi-customized",
  "scopes": ["announcement1492794990099121396","kekaiguanli7996550270124641378"]
}
```

属性说明：

name: 固定值请勿修改；

scope: 适配服务范围：["ctp-user","kekaiguanli7996550270124641378"],适配所有服务配置为：["ALL"]

格式：api包里面的接口全路径=手写实现代码的全路径

#### 2.1.4 子工程添加

新增spi子工程需要在父级工程的modules中引入

<img width="1303.2">

#### 2.1.5 三方依赖引入

#### 2.1.6 编译构建

入口：开发环境-->system-admin账号登录后台-->系统管理-->客开管理-->构建

<img width="1532">

#### 2.1.6 验证

构建好以后重启对应的服务，才能进行验证,当前方式不支持文件操作的StorageSpi,文件操作的SPI需要打成jar然后在nocas中配置。

SPI代码中不能使用@Autowired，获取bean只能通过App.getFactory.getBean()的方式

### 2.2 UDC扩展代码

#### 2.2.1 Git地址获取

第一步：新建UDC应用执行测试构建并成功后，在应用管理，发布界面获取应用编码

<img width="1256">

第二步：获取GIT仓库地址

UDC扩展开发代码（客开代码提交到此工程）：http://{ip}:{port}/autocode-extend/backend/{应用编码}.git

UDC自动生成代码（不能提交任何手写代码）：http://{ip}:{port}/autocode/backend/{应用编码}.git

注：UDC应用扩展代码工程在UDC应用新建并执行首次测试构建且构建成功之后才会自动创建

#### 2.2.3 注意事项

1、需要手动创建一个分支，并在该分支上作业

<img width="1536">

2、pom文件中的版本号要与构建中的版本号一致

<img width="1495.2">

### 2.3 配置maven-setting

在客开管理下载setting.xml文件并在Idea中配置好，复制Git地址后在IDE中拉取代码，

<img width="1533.6">

## 3、前端代码开发

### 3.1. UDC扩展代码

#### 3.1.1  Git地址获取

第一步：新建UDC应用执行测试构建并成功后，在应用管理->应用发布界面获取应用编码

第二步：获取GIT仓库地址

UDC扩展代码后端工程：http://{ip}:{port}/autocode-extend/frontend/{应用编码}.git

UDC动态代码前端工程：http://{ip}:{port}/autocode-extend/frontend/{应用编码}.git

注：UDC应用扩展代码工程在UDC应用新建并执行首次测试构建且构建成功之后才会自动创建

### 3.2 扩展工程代码

#### 3.2.1 Git地址获取

入口：开发环境-->system-admin账号登录后台-->系统管理-->客开管理，见下图：

<img width="1920">

### 3.3 编译调试

1、node源地址：http://39.107.192.235:9082/

2、版本要求：node：18.20.5及以上版本    yarn：1.22.22

工程clone之后，切换到根目录执行yarn命令下载依赖，下载完之后再切换到example目录执行yarn 命令下载；具体参考如图：

<img width="1350">

<img width="1531">

修改代理环境地址, 请在example/webpack-overrides.js中配置

<img width="1749">

5.调试：再根目录下输入yarn dev和example目录下输入yarn dev 回车，启动本地调试

<img width="1744">

<img width="1804">

<img width="1814">

### 3.4 工程构建

### 

### 3.5 标品应用本地调试

比如标品应用：新闻、公告、文档中心、工资条，考勤管理等

#### 3.5.1.工程clone后，切换到需要启动的工程目录(比如pc或者mobile目录)，eg:切换pc目录启动pc端进行调试

前置条件：切换node源：http://39.107.192.235:9082/  node版本：v18.20.5及以上

<img width="732">

#### 3.5.2 执行 yarn install --ignore-engines命令 下载对应工程的依赖

<img width="1252">

<img width="1180.8">

#### 3.5.3 修改代理环境地址, 在/webpack-overrides.js中搜索“hostName”关键字，修改成代理V8地址

<img width="1825">

#### 3.5.4 找到当前目录下package.json文件查看启动脚本的命令，平台3.10及以上版本将启动命令封装到“syf dev-udc-custom“命令里，搜索关键字"syf dev-udc-custom"找到对应的脚本名称 并执行它，启动对应的工程。

<img width="1179.2">

<img width="1192">

备注：看到http:localhost:3000 字样和building 就表示启动好了。

#### 3.5.5 工程启动后，pc端登录访问：前端ip+端口+/login  移动端登录访问：前端ip+端口+/login-mobile 登录成果后再找到需要调试页面地址进行调试

<img width="1515.2">

<img width="1520">

## 4、生产环境部署

### 4.1 代码包导出

<img width="1477.7778169255207">

### 4.1 代码包导入

入口：生产环境-->system-admin账号登录后台-->系统管理-->客开管理

<img width="1561.1111524664336">

注意：如果导入的是后端扩展，则需要重启spi作用域内的服务才能进行功能验证,如果导入的前端扩展，只要导入成功，页面前台刷新下就直接生效了
