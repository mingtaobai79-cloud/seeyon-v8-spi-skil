> 🧊 **冻结状态** — 缺少必要 jar 包，接口/DTO 均为 OBSERVATION，无法升级到 FACT。
> 待获取对应 jar 后解除冻结。

# 上传下载拦截 / StorageInterceptorSpi

> Evidence: OBSERVATION ⚠️ — 语雀文档 + jar 反编译交叉验证。
> **jar 验证结果**：`boot-starter-file-5.3.358.jar` 中未找到 `StorageInterceptorSpi`。
> 该接口可能在 5.8+ 版本中引入。

## 场景

对文件上传下载操作进行拦截，针对文件做处理后再上传/下载。例如：上传前做敏感词校验。

支持版本：5.8 及以上。支持范围：全系统文件上传和下载拦截。

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>boot-starter-file</artifactId>
  <version>5.8.0</version>
</dependency>
```

## 接口定义 [OBSERVATION ⚠️]

```java
// FQCN: com.seeyon.boot.starter.file.spi.StorageInterceptorSpi（语雀文档给出）
public interface StorageInterceptorSpi {
    // 文件上传前
    default StorageUploadRequestDto beforeUpload(StorageUploadRequestDto requestDto) {
        return requestDto;
    }
    // 文件上传后
    default UploadResultDto afterUpload(StorageUploadRequestDto requestDto, UploadResultDto resultDto) {
        return resultDto;
    }
    // 文件下载前
    default void beforeDownload(String storageKey, String bucketName) {
    }
    // 文件下载后
    default void afterDownload(String storageKey, String bucketName) {
    }
}
```

## jar 反编译确认的类 [FACT ✅]

### FileSafeInterceptor（boot-starter-file-5.3.358）

```java
package com.seeyon.boot.starter.file.safe;

// FQCN: com.seeyon.boot.starter.file.safe.FileSafeInterceptor
// 文件安全拦截器（非 SPI，是内部实现）
// 使用 ByteBuddy + Javassist 动态字节码注入
```

## 代码骨架

```java
package com.seeyon.extend.spi.file;

// import com.seeyon.boot.starter.file.spi.StorageInterceptorSpi;  // FQCN 待确认
// import com.seeyon.boot.starter.file.dto.request.StorageUploadRequestDto;
// import com.seeyon.boot.starter.file.dto.response.UploadResultDto;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * 上传下载拦截 SPI 实现
 * <p>🧊 冻结：接口 FQCN 未确认，代码无法编译</p>
 */
public class CustomStorageInterceptorSpi /* implements StorageInterceptorSpi */ {

    private static final Logger log = LoggerFactory.getLogger(CustomStorageInterceptorSpi.class);

    // @Override
    public /* StorageUploadRequestDto */ Object beforeUpload(/* StorageUploadRequestDto */ Object requestDto) {
        log.debug("[storage-interceptor] beforeUpload called");
        // TODO: 上传前处理（如敏感词校验、病毒扫描）
        return requestDto;
    }

    // @Override
    public /* UploadResultDto */ Object afterUpload(/* StorageUploadRequestDto */ Object requestDto, /* UploadResultDto */ Object resultDto) {
        log.debug("[storage-interceptor] afterUpload called");
        // TODO: 上传后处理（如日志记录、审计）
        return resultDto;
    }

    // @Override
    public void beforeDownload(String storageKey, String bucketName) {
        log.debug("[storage-interceptor] beforeDownload called, key={}, bucket={}", storageKey, bucketName);
        // TODO: 下载前处理（如权限校验）
    }

    // @Override
    public void afterDownload(String storageKey, String bucketName) {
        log.debug("[storage-interceptor] afterDownload called, key={}, bucket={}", storageKey, bucketName);
        // TODO: 下载后处理（如日志记录）
    }
}
```

## Nacos 配置

本 SPI 不需要额外 Nacos 配置。

## spring.factories

```properties
# FQCN 待 jar 确认
# com.seeyon.boot.starter.file.spi.StorageInterceptorSpi=com.seeyon.extend.spi.file.CustomStorageInterceptorSpi
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["file"]
}
```

## 重启服务

file

## 阻塞项

1. `StorageInterceptorSpi` 接口 FQCN — 5.3.358 jar 中不存在
2. 需要 5.8+ 版本 jar
