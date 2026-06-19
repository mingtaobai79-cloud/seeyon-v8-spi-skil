# 流程 / 公文 SPI 域

> 本目录覆盖公文扩展和事项中心流程扩展两个子场景。
> 注意：公文扩展不是传统 SPI，是 OpenAPI/service 泛化调用接口。

## 目录结构

```
workflow-document/
├── index.md                    ← 本文件（纯导航）
├── shared/                     ← 共享资源
├── edoc/                       ← 公文扩展（泛化调用）
└── bpm/                        ← 事项中心流程扩展（BPM SPI）
```

## SPI 文件夹索引

| SPI 文件夹 | 场景 | 接口 | Scope | 重启服务 |
|-----------|------|------|-------|----------|
| [edoc/](edoc/README.md) | 公文扩展接口 | `EdocProjectPublicService`（泛化调用） | edoc | edoc |
| [bpm/](bpm/README.md) | 事项中心流程扩展 | `BpmOperationSpi` + `BpmDetailViewSpi` | bpm | bpm |

## 公共方法双查规则

生成、改造或标注 SPI 方法时必须同时查询两类来源：

1. 子域契约：本目录对应 SPI 的 `README.md` / `constraints.md` / `shared/*contract*`，只用于接口 FQCN、SPI 方法签名、DTO、枚举、scope、spring.factories。
2. 平台公共方法：`references/platform-standard-library/index.md` 和 `references/platform-standard-library/decompiled/`，用于 boot-core / boot-starter-web / boot-starter-spi 的 JSON、HTTP、加密、BeanCopy、Transport Response/Request、RequestContext、BusinessException 等公共能力。

规则：凡是代码中要使用或标注公共 helper / Response / Request / 工具类方法，先查平台标准库；凡是 SPI 接口与 DTO，先查本子域契约。两边都查完再生成，禁止把平台公共类型误报成子域缺口，也禁止把子域契约包提升为全局公共方法。

## Evidence 状态

| SPI | 接口 Evidence | DTO Evidence | 来源 | 状态 |
|-----|--------------|--------------|------|------|
| edoc | OBSERVATION ⚠️ | OBSERVATION ⚠️ | 语雀 0099 | 🧊 冻结 |
| bpm | FACT ✅ | FACT ✅ | bpm-facade-5.3.374.jar | ✅ |

> **edoc 冻结原因：** EdocProjectPublicService 接口在现有 jar 中未找到，需要 edoc-facade 或更高版本 jar。

## 索取清单

```
P0:
1. 公文：EdocProjectPublicService 完整接口（文档有 16KB 附件）
2. BPM：BpmOperationSpi、BpmDetailViewSpi 完整接口
3. BPM DTO：BpmForwardReq、BpmForwardResp、BpmNodePermissionMergeReq/Resp、BpmCheckNodePermissionReq/Resp

P1:
4. spring.factories 注册示例
5. 示例：事项重定向、权限合并、操作按钮/权限扩展的现场示例
6. bpm-facade 现场版本
```
