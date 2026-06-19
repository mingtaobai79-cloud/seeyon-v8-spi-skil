# 数据源扩展 SPI 域

> 本目录覆盖数据源扩展 SPI 子场景。

## 目录结构

```
datasource/
├── index.md                    ← 本文件（纯导航）
├── shared/                     ← 共享资源
└── database-executor/          ← 数据源扩展
```

## SPI 文件夹索引

| SPI 文件夹 | 场景 | 接口 | Scope | 重启服务 |
|-----------|------|------|-------|----------|
| [database-executor/](database-executor/README.md) | 数据源扩展（Oracle/MySQL/达梦等） | `DataBaseExecutorService` | cip-connector | cip-connector |

## 公共方法双查规则

生成、改造或标注 SPI 方法时必须同时查询两类来源：

1. 子域契约：本目录对应 SPI 的 `README.md` / `constraints.md` / `shared/*contract*`，只用于接口 FQCN、SPI 方法签名、DTO、枚举、scope、spring.factories。
2. 平台公共方法：`references/platform-standard-library/index.md` 和 `references/platform-standard-library/decompiled/`，用于 boot-core / boot-starter-web / boot-starter-spi 的 JSON、HTTP、加密、BeanCopy、Transport Response/Request、RequestContext、BusinessException 等公共能力。

规则：凡是代码中要使用或标注公共 helper / Response / Request / 工具类方法，先查平台标准库；凡是 SPI 接口与 DTO，先查本子域契约。两边都查完再生成，禁止把平台公共类型误报成子域缺口，也禁止把子域契约包提升为全局公共方法。

## Evidence 状态

| SPI | 接口 Evidence | DTO Evidence | 来源 | 状态 |
|-----|--------------|--------------|------|------|
| database-executor | FACT ✅ | FACT ✅ | cip-connector-api-5.3.286.jar | ✅ |

## 索取清单

```
P0:
1. cip-connector-api jar（含 DataBaseExecutorService 完整接口）
2. DatabaseInfoApiDto、ExecutorResultApiDto、LinkerDetailApiDto、DbTypeEnum 完整定义
3. OracleSpiDataBaseExecutorService 示例代码（文档提到有 33KB 附件）

P1:
4. spring.factories 注册示例
5. 目标数据库类型
6. 页面参数配置截图
```
