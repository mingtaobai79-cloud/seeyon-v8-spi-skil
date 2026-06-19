# 文件 / 存储 SPI 域

> 本目录覆盖上传下载拦截和文件操作两个 SPI 子场景。
> 注意：文件域有特殊部署规则，不要按普通 SPI 粗暴处理。

## 目录结构

```
file-storage/
├── index.md                    ← 本文件（纯导航）
├── shared/                     ← 共享资源
├── storage-interceptor/        ← 上传下载拦截
└── storage-spi/                ← 文件操作（接入新存储）
```

## SPI 文件夹索引

| SPI 文件夹 | 场景 | 接口 | Scope | 重启服务 |
|-----------|------|------|-------|----------|
| [storage-interceptor/](storage-interceptor/README.md) | 上传下载文件拦截（敏感词/加密等） | `StorageInterceptorSpi` | boot-starter-file | file |
| [storage-spi/](storage-spi/README.md) | 接入新对象存储/文件加密机/数据迁移 | `StorageSpi` | boot-starter-file | file |

## 公共方法双查规则

生成、改造或标注 SPI 方法时必须同时查询两类来源：

1. 子域契约：本目录对应 SPI 的 `README.md` / `constraints.md` / `shared/*contract*`，只用于接口 FQCN、SPI 方法签名、DTO、枚举、scope、spring.factories。
2. 平台公共方法：`references/platform-standard-library/index.md` 和 `references/platform-standard-library/decompiled/`，用于 boot-core / boot-starter-web / boot-starter-spi 的 JSON、HTTP、加密、BeanCopy、Transport Response/Request、RequestContext、BusinessException 等公共能力。

规则：凡是代码中要使用或标注公共 helper / Response / Request / 工具类方法，先查平台标准库；凡是 SPI 接口与 DTO，先查本子域契约。两边都查完再生成，禁止把平台公共类型误报成子域缺口，也禁止把子域契约包提升为全局公共方法。

## Evidence 状态

| SPI | 接口 Evidence | DTO Evidence | 来源 | 状态 |
|-----|--------------|--------------|------|------|
| storage-interceptor | OBSERVATION ⚠️ | OBSERVATION ⚠️ | 语雀 0104 | 🧊 冻结 |
| storage-spi | FACT ✅ | FACT ✅ | boot-starter-file-5.3.358.jar | ✅ |

> **storage-interceptor 冻结原因：** boot-starter-file jar 中未找到 StorageInterceptorSpi 接口类。

## 特殊部署规则

文件 SPI **不支持 OSS 方式加载**，也不支持通过客开管理直接提交代码。
必须打成 jar 包，使用 SPI 扩展机制的本地文件方式部署。

## 索取清单

```
P0:
1. boot-starter-file jar（含 StorageInterceptorSpi、StorageSpi 完整接口）
2. StorageUploadRequestDto、StorageDownloadRequestDto、UploadResultDto、DownloadResultDto 完整字段
3. SpiUploadRequestDto 完整字段
4. UnifyFileService 示例代码（文档有 zip 附件）

P1:
5. spring.factories 注册示例
6. Nacos 配置（public 中的桶名称参数 bug 修复配置）
7. 文件流/桶/路径/metadata 字段语义
```
