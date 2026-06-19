# 文件/存储域共享资源

## 域概述

- StorageInterceptorSpi：拦截全系统文件上传下载，做敏感词校验/加密等处理
- StorageSpi：接入新的对象存储、三方文件加密机、V5 历史附件逻辑迁移

## 特殊部署规则

1. **不支持 OSS 方式加载**。
2. **不支持客开管理直接提交代码**。
3. 必须打成 jar 包，使用 SPI 扩展机制的本地文件方式。
4. Nacos public 中需配置参数（标品有 bug，传入的桶名称参数可能为空）。

## 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>boot-starter-file</artifactId>
  <!-- 版本以现场为准，文档示例：5.8.0（拦截器）/ 3.8.211（StorageSpi） -->
  <version>xxx</version>
</dependency>
```
