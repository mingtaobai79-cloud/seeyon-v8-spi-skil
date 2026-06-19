---
title: "认证系统接入"
source: "https://www.yuque.com/seeyonkk/v8/uevxy4zvbfi6bs11"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 认证系统接入

> Source: https://www.yuque.com/seeyonkk/v8/uevxy4zvbfi6bs11

作者：杨映海
最后更新：2025-04-18

## 1.应用场景

使用三方认证中心进行统一身份认证， 在登录v8系统时， 会先跳转到三方认证中心进行登录， 三方认证中心登录成功后， 重定向v8目标地址，完成系统登录过程。

<img src="https://cdn.nlark.com/yuque/0/2025/jpeg/26748915/1745295237250-8a91ab86-1827-4de3-b25f-7fd3044b7b08.jpeg" width="1106">

<img src="https://cdn.nlark.com/yuque/0/2025/png/26748915/1745295266468-45232438-3fb1-4cce-84b4-d0cd9a7275c6.png" width="844">

## 2.接口说明

接口名称：com.seeyon.ctp.user.api.sso.CtpUserSsoAuthProviderService

```xml
<dependency>
    <groupId>com.seeyon</groupId>
    <artifactId>ctp-user-api</artifactId>
    <!-- 请以实际环境的依赖版本号为准-->
    <version>3.8.211</version>
</dependency>
```

## 3.接口实现

spi代码仓库获取及工程初始化请参考：SPI扩展代码开发

注意：1、完成接口开发后需要添加SPI配置文件，参考：SPI配置文件

          2、完成接口开发并构建成功后需要重启【ctp-user】服务才能进行后续功能验证

## 4.参数配置

### 4.1 v8 域名配置

进入NACOS，在public 配置如下参数

### 4.2 开启spi认证

进入NACOS，在ctp-user微服务下配置如下参数【其中spisso为固定值】

### 4.3 认证类型配置

进入NACOS，在ctp-user微服务下配置如下参数【其中"thirdauth"为spi扩展的认证类型由用户自定义，对应spi实现类头部注解：@CtpUserChannelRouter("thirdauth") 】

## 5.实现效果

在浏览器地址栏中输入【服务域名】/main/portal，点击回车/访问

<img width="481">

浏览器自动重定向到统一身份认证中心认证页，输入认证中心账号密码后，成功进入V8平台首页

<img width="2740">

## 6.预置认证

常见的三方认证服务（信安、腾讯玉符、派拉软件、CAS、SAML2）平台已经做了标准化接入，登录管理后面填写相关配置参数开启服务即可

开启入口：system-admin帐号登录-->基础设置-->认证服务

<img width="1482.5">

## 7.示例代码

cip-spi-user-sso-thirdauth.zip
(65 KB)

## 8.注意事项

需要实现getEncodeLogoutRedirectUrl或者thirdSsoLogout接口V8才有退出按钮

如果实现的是getEncodeLogoutRedirectUrl接口，该接口返回的登出地址需要和getSsoLoginUrl接口返回的地址中loginUrl后的地址一致

示例：

## 9.多租户不同域名场景

多个租户下，每个租户可能有独立 OA 域名，并且每个租户可能对接不同统一认证中心地址的情况下：

nacos配置新增：

添加获取nacos的配置类

在getSsoLoginUrl方法中添加关于根据域名获取不同租户的配置信息

在getUserLoginInfo方法中添加关于根据域名获取不同租户的配置信息

在getEncodeLogoutRedirectUrl方法中添加关于根据租户id获取不同租户的配置信息

完整service参考代码：
ThirdauthSsoAuthProviderService.java
(27 KB)
