# 入口 / 菜单 / 移动插件 SPI 域

> 本目录覆盖三方菜单和移动插件两个 SPI 子场景。

## 目录结构

```
entry-menu-mobile/
├── index.md                    ← 本文件（纯导航）
├── shared/                     ← 共享资源
├── third-menu/                 ← 三方菜单接入
└── mobile-plugin/              ← 移动插件（V8 接入三方 App）
```

## SPI 文件夹索引

| SPI 文件夹 | 场景 | 接口 | Scope | 重启服务 |
|-----------|------|------|-------|----------|
| [third-menu/](third-menu/README.md) | 菜单导航添加三方菜单 | `AbstractThirdMenuService` | ctp-user | ctp-user |
| [mobile-plugin/](mobile-plugin/README.md) | V8 接入三方 App（企微/钉钉/飞书） | `Mobile*ProviderService`（7 个接口） | cip-connector | cip-connector |

## 公共方法双查规则

生成、改造或标注 SPI 方法时必须同时查询两类来源：

1. 子域契约：本目录对应 SPI 的 `README.md` / `constraints.md` / `shared/*contract*`，只用于接口 FQCN、SPI 方法签名、DTO、枚举、scope、spring.factories。
2. 平台公共方法：`references/platform-standard-library/index.md` 和 `references/platform-standard-library/decompiled/`，用于 boot-core / boot-starter-web / boot-starter-spi 的 JSON、HTTP、加密、BeanCopy、Transport Response/Request、RequestContext、BusinessException 等公共能力。

规则：凡是代码中要使用或标注公共 helper / Response / Request / 工具类方法，先查平台标准库；凡是 SPI 接口与 DTO，先查本子域契约。两边都查完再生成，禁止把平台公共类型误报成子域缺口，也禁止把子域契约包提升为全局公共方法。

## Evidence 状态

| SPI | 接口 Evidence | DTO Evidence | 来源 | 状态 |
|-----|--------------|--------------|------|------|
| third-menu | FACT ✅ | FACT ✅ | ctp-user-api-5.3.351.jar | ✅ |
| mobile-plugin | FACT ✅ | FACT ✅ | cip-connector-api-5.3.286.jar | ✅ |

## 索取清单

```
P0:
1. ctp-user-api jar（含 AbstractThirdMenuService、ThirdMenuParamDto、CtpUserThirdNavFrontDto、MenuPositionEnum）
2. cip-connector-api jar（含 7 个 Mobile*ProviderService 完整接口）

P1:
3. spring.factories 注册示例
4. 企业微信/钉钉/飞书示例配置和回调样例
```
