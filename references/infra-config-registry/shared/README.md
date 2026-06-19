# 配置/注册中心域共享资源

## 域概述

扩展非 Nacos 的注册中心和配置中心。当客户使用 Consul、Eureka、Apollo 等替代 Nacos 时，通过 SPI 替换平台内置实现。

- 依赖：boot-starter-nacos
- 全局生效，需重启所有服务

## 公共约束

1. 两个 SPI 都部署到 boot-starter-nacos scope。
2. 全局生效，需要重启所有服务。
3. 示例代码文档有附件（NacosRegisterImpl.java 11KB、NacosConfigImpl.java 4KB）。
