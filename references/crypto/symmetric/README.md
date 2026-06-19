> 🧊 **冻结状态** — 缺少必要 jar 包，接口/DTO 均为 OBSERVATION，无法升级到 FACT。
> 待获取对应 jar 后解除冻结。

# 对称加密 / SymmetricSpi

> Evidence: OBSERVATION ⚠️ — 语雀文档 + jar 反编译交叉验证。
> **jar 验证结果**：`boot-starter-encrypt` artifact 在已检查的用户私有仓库中未找到。
> `boot-starter-security-5.3.265.jar` 中有 `EncryptService` 但非 SPI 接口。

## 场景

客户想用自己的密钥机制对数据库存储数据进行对称加密/解密。支持范围：实体字段上标注了加密注解的。

## Maven 依赖

```xml
<!-- artifactId 待确认，boot-starter-encrypt 在仓库中不存在 -->
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>boot-starter-encrypt</artifactId>
  <version>待确认</version>
</dependency>
```

## 接口定义 [OBSERVATION ⚠️]

```java
// FQCN: com.seeyon.boot.encrypt.algorithm.symmetric.spi.SymmetricSpi（语雀文档给出）
public interface SymmetricSpi {
    /**
     * 加密
     */
    String encrypt(String clearText);
    /**
     * 解密
     */
    String decrypt(String cipherText);
}
```

## jar 反编译确认的类 [FACT ✅]

### EncryptService（boot-starter-security-5.3.265）

```java
package com.seeyon.boot.starter.security.service;

// FQCN: com.seeyon.boot.starter.security.service.EncryptService
// 内部服务，非 SPI 接口
// 使用 DESUtils 进行前端密码解密
```

## 代码骨架

```java
package com.seeyon.extend.spi.crypto;

// import com.seeyon.boot.encrypt.algorithm.symmetric.spi.SymmetricSpi;  // FQCN 待确认
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * 对称加密 SPI 实现
 * <p>🧊 冻结：接口 FQCN 未确认，代码无法编译</p>
 */
public class CustomSymmetricSpi /* implements SymmetricSpi */ {

    private static final Logger log = LoggerFactory.getLogger(CustomSymmetricSpi.class);

    // @Override
    public String encrypt(String clearText) {
        log.debug("[crypto-symmetric] encrypt called");
        // TODO: 实现自定义对称加密算法
        // 例如：使用自定义密钥 + AES-256
        return clearText; // 替换为加密结果
    }

    // @Override
    public String decrypt(String cipherText) {
        log.debug("[crypto-symmetric] decrypt called");
        // TODO: 实现自定义对称解密算法
        return cipherText; // 替换为解密结果
    }
}
```

## Nacos 配置

本 SPI 不需要额外 Nacos 配置。

## spring.factories

```properties
# FQCN 待 jar 确认
# com.seeyon.boot.encrypt.algorithm.symmetric.spi.SymmetricSpi=com.seeyon.extend.spi.crypto.CustomSymmetricSpi
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["encrypt"]
}
```

## 重启服务

encrypt

## 阻塞项

1. `boot-starter-encrypt` artifact 在仓库中不存在
2. `SymmetricSpi` 接口 FQCN 待 jar 确认
3. spring.factories key 待确认
