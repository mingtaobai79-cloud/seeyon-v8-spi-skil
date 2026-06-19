# 配置 / 注册中心 SPI 域

> 本目录覆盖注册中心和配置中心两个 SPI 子场景。

## 目录结构

```
infra-config-registry/
├── index.md                    ← 本文件（纯导航）
├── shared/                     ← 共享资源
├── register/                   ← 注册中心扩展
└── config/                     ← 配置中心扩展
```

## SPI 文件夹索引

| SPI 文件夹 | 场景 | 接口 | Scope | 重启服务 |
|-----------|------|------|-------|----------|
| [register/](register/README.md) | 扩展非 Nacos 注册中心 | `RegisterServiceSPI` | boot-starter-nacos | 全部 |
| [config/](./config/README.md) | 扩展非 Nacos 配置中心 | `ConfigServiceSPI` | boot-starter-nacos | 全部 |

## 公共方法双查规则

生成、改造或标注 SPI 方法时必须同时查询两类来源：

1. 子域契约：本目录对应 SPI 的 `README.md` / `constraints.md` / `shared/*contract*`，只用于接口 FQCN、SPI 方法签名、DTO、枚举、scope、spring.factories。
2. 平台公共方法：`references/platform-standard-library/index.md` 和 `references/platform-standard-library/decompiled/`，用于 boot-core / boot-starter-web / boot-starter-spi 的 JSON、HTTP、加密、BeanCopy、Transport Response/Request、RequestContext、BusinessException 等公共能力。

规则：凡是代码中要使用或标注公共 helper / Response / Request / 工具类方法，先查平台标准库；凡是 SPI 接口与 DTO，先查本子域契约。两边都查完再生成，禁止把平台公共类型误报成子域缺口，也禁止把子域契约包提升为全局公共方法。

## Evidence 状态

| SPI | 接口 Evidence | 来源 | 状态 |
|-----|--------------|------|------|
| register | FACT ✅ | boot-starter-nacos-5.3.358.jar | ✅ |
| config | FACT ✅ | boot-starter-nacos-5.3.358.jar | ✅ |

## 索取清单

```
P0:
1. boot-starter-nacos jar（含 RegisterServiceSPI、ConfigServiceSPI 完整接口）
2. AppInstanceDto 完整字段
3. ConfigChangeProcess 完整定义

P1:
4. spring.factories 注册示例
5. NacosRegisterImpl.java 示例代码（文档有 11KB 附件）
6. NacosConfigImpl.java 示例代码（文档有 4KB 附件）
7. boot-starter-nacos 现场版本
```
