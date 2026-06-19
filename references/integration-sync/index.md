# 三方集成同步 SPI 域

> 本目录整合了三方集成相关的 SPI 扩展，按 SPI 类型组织为独立文件夹。

## 目录结构

```
integration-sync/
├── index.md                    ← 本文件（总索引）
├── shared/                     ← 共享资源（域约束）
├── todo-batch/                 ← 批处理三方待办 SPI
├── api-auth/                   ← 集成接口鉴权 SPI
└── org-sync-middle-table/      ← 组织同步中间表 SPI
```

## SPI 文件夹索引

| SPI 文件夹 | 场景 | 接口 | Scope | 重启服务 |
|-----------|------|------|-------|----------|
| [todo-batch/](todo-batch/README.md) | 三方待办数据批量处理 | `AbstractThirdAffairService` | ctp-affair | ctp-affair |
| [api-auth/](api-auth/README.md) | 集成应用接口认证扩展 | `LinkerSecurityService` | cip-connector | cip-connector |
| [org-sync-middle-table/](org-sync-middle-table/README.md) | 组织数据中间表同步（主动拉取/被动接收） | `MiddleTableOrgSyncSpiPullService` / `MiddleTableOrgSyncSpiListenerService` | cip-connector | cip-connector |

## 共享资源

位于 [shared/](shared/) 目录：

| 文件 | 用途 |
|------|------|
| [README.md](shared/README.md) | 域概述、通用规则、依赖版本 |
| [constraints.md](shared/constraints.md) | 域级约束（三个 SPI 共有的规则） |

## 每个 SPI 文件夹的标准结构

```
{spi-name}/
├── README.md              ← 场景描述、接口定义（FACT）、DTO、代码骨架、Nacos、spring.factories
└── constraints.md         ← 该 SPI 的独有约束、禁止项、索取清单
```

## 执行流程

1. 识别用户场景，定位到具体 SPI 文件夹
2. 读取该 SPI 的 `README.md` 了解场景和接口
3. 读取 `constraints.md` 了解独有约束
4. 如需域级约束，查阅 `shared/` 目录
5. 生成代码前先读 `references/spi-domain-constraints.md`（全局公共约束）

## 公共方法双查规则

生成、改造或标注 SPI 方法时必须同时查询两类来源：

1. 子域契约：本目录对应 SPI 的 `README.md` / `constraints.md` / `shared/*contract*`，只用于接口 FQCN、SPI 方法签名、DTO、枚举、scope、spring.factories。
2. 平台公共方法：`references/platform-standard-library/index.md` 和 `references/platform-standard-library/decompiled/`，用于 boot-core / boot-starter-web / boot-starter-spi 的 JSON、HTTP、加密、BeanCopy、Transport Response/Request、RequestContext、BusinessException 等公共能力。

规则：凡是代码中要使用或标注公共 helper / Response / Request / 工具类方法，先查平台标准库；凡是 SPI 接口与 DTO，先查本子域契约。两边都查完再生成，禁止把平台公共类型误报成子域缺口，也禁止把子域契约包提升为全局公共方法。

## 证据状态

| SPI | 接口 Evidence | DTO Evidence | 状态 |
|-----|--------------|--------------|------|
| todo-batch | FACT ✅（ctp-affair-facade-5.3.315.jar 已核验） | FACT ✅ | ✅ |
| api-auth | FACT ✅ | FACT ✅ | ✅ |
| org-sync-middle-table | FACT ✅ | FACT ✅（回调服务方法已由样例源码 FACT 化；完整接口源码仍待补） | ✅ |
