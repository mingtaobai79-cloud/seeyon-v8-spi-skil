# 加解密域共享资源

## 域概述

客户想用自己的密钥机制对数据进行加解密时，通过 SPI 扩展替换平台内置算法。

- 散列加密（DigestSpi）：用户密码、工资条
- 对称加密（SymmetricSpi）：数据库存储加密（实体字段上标注了加密注解的）

## 公共约束

1. SPI 部署后，**只对新产生的数据生效**，旧数据还是用原来的加解密方式。
2. Nacos 配置需要全局生效，配置到 public namespace。
3. 如果要全局生效，需要重启所有服务。
4. 产品配置入口：登录 system-admin 账号 → 数据加密配置。

## Nacos 配置

```yaml
# 散列加密 — 配置到 public namespace
seeyon:
  encrypt:
    digest: SPI

# 对称加密 — 配置到 public namespace
seeyon:
  encrypt:
    symmetric: SPI
```

## 依赖

两个 SPI 的依赖 jar 待确认，文档未给出 Maven 坐标。推测为 `boot-starter-encrypt` 或类似 artifactId。
