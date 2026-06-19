# 入口/菜单/移动域共享资源

## 域概述

- 三方菜单：将三方系统菜单集成到 V8 导航中（ctp-user 服务）
- 移动插件：V8 平台 H5 应用接入三方 APP 工作台（cip-connector 服务）

两个 SPI 部署到不同微服务，不共享实现类。

## 注意

mobile-plugin 的 7 个接口与 auth-sso 域的 Legacy mobile-app SPI 有交叉引用。
详见 `references/auth-sso/mobile-app/README.md`。
