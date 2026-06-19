# 流程/公文域共享资源

## 域概述

- 公文扩展：通过泛化调用方式扩展公文功能（不是传统 SPI）
- BPM 扩展：事项中心流程扩展，两个 SPI 配合使用

## 关键区别

| 特性 | 公文扩展 | BPM 扩展 |
|------|---------|---------|
| 调用方式 | 泛化调用（非 SPI 注册） | 标准 SPI（spring.factories） |
| 接口类型 | AppService（OpenAPI/service） | SPI interface |
| 部署方式 | 不能直接 SPI 注册 | 标准 SPI 部署 |
