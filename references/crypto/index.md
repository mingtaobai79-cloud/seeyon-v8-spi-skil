# 加解密 SPI 域

> 本目录覆盖散列加密和对称加密两个 SPI 子场景。

## 目录结构

```
crypto/
├── index.md                    ← 本文件（纯导航）
├── shared/                     ← 共享资源
├── digest/                     ← 散列加密（DigestSpi）
└── symmetric/                  ← 对称加密（SymmetricSpi）
```

## SPI 文件夹索引

| SPI 文件夹 | 场景 | 接口 | Scope | 重启服务 |
|-----------|------|------|-------|----------|
| [digest/](digest/README.md) | 散列加密（用户密码、工资条） | `DigestSpi` | boot-starter-encrypt | 全部 |
| [symmetric/](symmetric/README.md) | 对称加密（数据库存储加密） | `SymmetricSpi` | boot-starter-encrypt | 全部 |

## 共享资源

| 文件 | 用途 |
|------|------|
| [shared/README.md](shared/README.md) | 域概述、公共约束、部署注意 |

## 公共方法双查规则

生成、改造或标注 SPI 方法时必须同时查询两类来源：

1. 子域契约：本目录对应 SPI 的 `README.md` / `constraints.md` / `shared/*contract*`，只用于接口 FQCN、SPI 方法签名、DTO、枚举、scope、spring.factories。
2. 平台公共方法：`references/platform-standard-library/index.md` 和 `references/platform-standard-library/decompiled/`，用于 boot-core / boot-starter-web / boot-starter-spi 的 JSON、HTTP、加密、BeanCopy、Transport Response/Request、RequestContext、BusinessException 等公共能力。

规则：凡是代码中要使用或标注公共 helper / Response / Request / 工具类方法，先查平台标准库；凡是 SPI 接口与 DTO，先查本子域契约。两边都查完再生成，禁止把平台公共类型误报成子域缺口，也禁止把子域契约包提升为全局公共方法。

## Evidence 状态

| SPI | 接口 Evidence | 来源 | 状态 |
|-----|--------------|------|------|
| digest | OBSERVATION ⚠️ | 语雀 0105 | 🧊 冻结 |
| symmetric | OBSERVATION ⚠️ | 语雀 0106 | 🧊 冻结 |

> **冻结原因：** boot-starter-encrypt artifact 在仓库中不存在，无法反编译确认 FQCN。

## 索取清单

```
P0:
1. boot-starter-encrypt jar（含 DigestSpi、SymmetricSpi 完整接口）
2. 确认 FQCN：com.seeyon.boot.encrypt.algorithm.digest.spi.DigestSpi
3. 确认 FQCN：com.seeyon.boot.encrypt.algorithm.symmetric.spi.SymmetricSpi

P1:
4. spring.factories 注册示例
5. 密钥来源与配置方式
6. 产品"数据加密配置"截图/配置项
7. 旧数据兼容/迁移策略
```
