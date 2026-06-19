# 系统变量扩展域

> 本目录覆盖"系统变量扩展"SPI 子域。

## 目录结构

```
system-variable/
├── index.md                    ← 本文件（总索引）
├── shared/                     ← 共享资源
└── system-variable-spi/        ← 系统变量 SPI
```

## SPI 文件夹索引

| SPI 文件夹 | 场景 | 接口 | Scope | 重启服务 |
|-----------|------|------|-------|----------|
| [system-variable-spi/](system-variable-spi/README.md) | 计算条件弹框添加自定义系统变量 | `SystemVariableSPIService` | UDC 应用 | UDC 应用对应服务 |

## 共享资源

位于 [shared/](shared/) 目录：

| 文件 | 用途 |
|------|------|
| [README.md](shared/README.md) | 域概述、注解属性、方法限制、部署指南 |

## 执行流程

1. 识别用户场景 → 进入 `system-variable-spi/`
2. 读 `README.md` 了解场景、接口、代码骨架
3. 读 `constraints.md` 了解独有约束
4. 如需注解/限制/部署细节 → `shared/README.md`
5. 生成代码前先读 `references/spi-domain-constraints.md`（全局公共约束）

## 公共方法双查规则

生成、改造或标注 SPI 方法时必须同时查询两类来源：

1. 子域契约：本目录对应 SPI 的 `README.md` / `constraints.md` / `shared/*contract*`，只用于接口 FQCN、SPI 方法签名、DTO、枚举、scope、spring.factories。
2. 平台公共方法：`references/platform-standard-library/index.md` 和 `references/platform-standard-library/decompiled/`，用于 boot-core / boot-starter-web / boot-starter-spi 的 JSON、HTTP、加密、BeanCopy、Transport Response/Request、RequestContext、BusinessException 等公共能力。

规则：凡是代码中要使用或标注公共 helper / Response / Request / 工具类方法，先查平台标准库；凡是 SPI 接口与 DTO，先查本子域契约。两边都查完再生成，禁止把平台公共类型误报成子域缺口，也禁止把子域契约包提升为全局公共方法。

## 证据状态

| SPI | 接口 Evidence | SPI | 接口 Evidence | DTO Evidence | 状态 |
|-----|--------------|--------------|------|
| system-variable-spi | OBSERVATION ⚠️ | OBSERVATION ⚠️ | 🧊 冻结 |

> **冻结原因：** boot-starter-systemvariable-5.3.313 和 boot-starter-formula-5.3.313 均不包含 SPI 接口类。
> 需要更高版本 jar 才能升级 FACT。已确认 Apps 和 ExpressionService 的 FQCN。

## 触发词

看到以下词，进入本子域，不要跳到 SSO/MQ：

- 系统变量扩展、系统变量 SPI、自定义系统变量
- 计算条件弹框添加变量
- `SystemVariableSPIService`、`SPISystemVariable`、`SPISystemVariableType`
- `boot-starter-systemvariable`、`getSystemVariableResultByName`、`currentUserId`
