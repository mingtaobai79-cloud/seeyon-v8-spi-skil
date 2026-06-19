# 文件操作 / StorageSpi

> **Evidence: FACT ✅** — 接口签名、DTO 来自 `boot-starter-file-5.3.358.jar` CFR 反编译。
> Source: jar 反编译 + 语雀 0113

## 场景

1. 接入新的对象存储
2. 三方文件加密机集成（上传加密、下载解密）
3. V5 系统数据迁移时，历史附件只做逻辑迁移

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>boot-starter-file</artifactId>
  <version>5.3.358</version>
</dependency>
```

## 接口定义 [FACT ✅]

```java
package com.seeyon.boot.starter.file.spi;

import com.seeyon.boot.starter.file.dto.response.UploadResultDto;
import com.seeyon.boot.starter.file.spi.dto.SpiUploadRequestDto;
import java.io.InputStream;
import javax.servlet.http.HttpServletResponse;

public interface StorageSpi {
    String getPrivateBucketName();
    String getPublicBucketName();
    String getFerryboatBucketName();
    UploadResultDto upload(SpiUploadRequestDto var1);
    void download(String var1, String var2, HttpServletResponse var3);
    InputStream download(String var1, String var2);
    String copy(String var1, String var2, String var3, String var4);
    boolean exist(String var1, String var2);
    default boolean delete(String storageKey, String bucketName) { return true; }
}
```

## 方法说明

| 方法 | 参数 | 返回 | 语义 |
|------|------|------|------|
| getPrivateBucketName | 无 | `String` | 私有桶名称 |
| getPublicBucketName | 无 | `String` | 公有桶名称 |
| getFerryboatBucketName | 无 | `String` | 摆渡桶名称 |
| upload | `SpiUploadRequestDto` | `UploadResultDto` | 上传文件 |
| download | `String, String, HttpServletResponse` | void | 下载文件到 response |
| download | `String, String` | `InputStream` | 下载文件返回流 |
| copy | `String, String, String, String` | `String` | 复制文件 |
| exist | `String, String` | `boolean` | 判断文件是否存在 |
| delete | `String, String` | `boolean` | 删除文件（default true） |

## DTO 定义 [FACT ✅]

### SpiUploadRequestDto

```java
package com.seeyon.boot.starter.file.spi.dto;

public class SpiUploadRequestDto extends BaseDto {
    InputStream inputStream;    // 流
    String bucketName;          // 桶名称
    String fileName;            // 文件下载时的文件名称
    String bizType;             // 业务类型
    String appName;             // 应用名称
    String storageKey;          // storageKey
    boolean runtime;            // 系统文件/运行态文件区分，默认 false
    boolean useFileNameAsKey;   // fileName 作为存储中的 key，默认 false
}
```

### UploadResultDto

```java
package com.seeyon.boot.starter.file.dto.response;

public class UploadResultDto extends BaseDto {
    String storageKey;
    String mimeType;
    Long fileSize;
    @Deprecated Boolean isPublic;
    String md5;
    @Deprecated String metadata;
}
```

## 代码骨架

```java
package com.seeyon.extend.spi.file;

import com.seeyon.boot.starter.file.spi.StorageSpi;
import com.seeyon.boot.starter.file.spi.dto.SpiUploadRequestDto;
import com.seeyon.boot.starter.file.dto.response.UploadResultDto;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import javax.servlet.http.HttpServletResponse;
import java.io.InputStream;

/**
 * 文件操作 SPI 实现
 * <p>示例：接入自定义对象存储</p>
 */
public class CustomStorageSpi implements StorageSpi {

    private static final Logger log = LoggerFactory.getLogger(CustomStorageSpi.class);

    @Override
    public String getPrivateBucketName() { return "custom-private"; }

    @Override
    public String getPublicBucketName() { return "custom-public"; }

    @Override
    public String getFerryboatBucketName() { return "custom-ferryboat"; }

    @Override
    public UploadResultDto upload(SpiUploadRequestDto spiRequestDto) {
        log.debug("[storage-spi] upload called, bucket={}, key={}",
            spiRequestDto.getBucketName(), spiRequestDto.getStorageKey());
        // TODO: 实现文件上传到自定义存储
        return null;
    }

    @Override
    public void download(String storageKey, String bucketName, HttpServletResponse response) {
        log.debug("[storage-spi] download called, key={}, bucket={}", storageKey, bucketName);
        // TODO: 实现文件下载
    }

    @Override
    public InputStream download(String storageKey, String bucketName) {
        log.debug("[storage-spi] download(stream) called, key={}, bucket={}", storageKey, bucketName);
        // TODO: 实现文件下载返回流
        return null;
    }

    @Override
    public String copy(String srcKey, String srcBucket, String destKey, String destBucket) {
        log.debug("[storage-spi] copy called");
        // TODO: 实现文件复制
        return null;
    }

    @Override
    public boolean exist(String storageKey, String bucketName) {
        log.debug("[storage-spi] exist called, key={}, bucket={}", storageKey, bucketName);
        return false;
    }
}
```

## Nacos 配置

public 中配置以下参数（标品有 bug，传入的桶名称参数可能为空）：

```yaml
seeyon:
  file:
    storageType: spi
    spiPlugins:
      - com.seeyon.extend.spi.file.CustomStorageSpi
```

## spring.factories

```properties
com.seeyon.boot.starter.file.spi.StorageSpi=com.seeyon.extend.spi.file.CustomStorageSpi
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["ALL"]
}
```

## 重启服务

file 服务

## 注意事项

1. **不支持 OSS 方式加载**，不支持客开管理直接提交代码。
2. 必须打成 jar 包，使用 SPI 扩展机制的本地文件方式。
3. 5.3.358 版本比语雀文档多了 `download(String, String)` 返回 InputStream、`copy`、`delete` 方法。
