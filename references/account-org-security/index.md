# 账号 / 组织 / 租户安全治理 SPI 域

> 本目录覆盖通讯录脱敏、登录人数控制、密码策略三个 SPI 子场景。

## 目录结构

```
account-org-security/
├── index.md                    ← 本文件（纯导航）
├── shared/                     ← 共享资源
├── address-book/               ← 通讯录脱敏
├── auth-check/                 ← 登录人数控制
└── password-policy/            ← 密码强度/默认密码
```

## SPI 文件夹索引

| SPI 文件夹 | 场景 | 接口 | Scope | 重启服务 |
|-----------|------|------|-------|----------|
| [address-book/](address-book/README.md) | 通讯录人员列表/卡片自定义脱敏 | `AbstractAddressBookSpiService` | organization | ctp-organization |
| [auth-check/](auth-check/README.md) | 自定义租户/机构登录人数控制 | `AbstractAuthenticationCheckService` | ctp-user | ctp-user |
| [password-policy/](password-policy/README.md) | 自定义密码强度和默认密码 | `PasswordCheckService` | ctp-user | ctp-user |

## 公共方法双查规则

生成、改造或标注 SPI 方法时必须同时查询两类来源：

1. 子域契约：本目录对应 SPI 的 `README.md` / `constraints.md` / `shared/*contract*`，只用于接口 FQCN、SPI 方法签名、DTO、枚举、scope、spring.factories。
2. 平台公共方法：`references/platform-standard-library/index.md` 和 `references/platform-standard-library/decompiled/`，用于 boot-core / boot-starter-web / boot-starter-spi 的 JSON、HTTP、加密、BeanCopy、Transport Response/Request、RequestContext、BusinessException 等公共能力。

规则：凡是代码中要使用或标注公共 helper / Response / Request / 工具类方法，先查平台标准库；凡是 SPI 接口与 DTO，先查本子域契约。两边都查完再生成，禁止把平台公共类型误报成子域缺口，也禁止把子域契约包提升为全局公共方法。

## Evidence 状态

| SPI | 接口 Evidence | DTO Evidence | 来源 | 状态 |
|-----|--------------|--------------|------|------|
| address-book | FACT ✅ | FACT ✅ | organization-facade-5.3.368.jar | ✅ |
| auth-check | OBSERVATION ⚠️ | OBSERVATION ⚠️ | 语雀 0092 | 🧊 冻结 |
| password-policy | FACT ✅ (partial) | OBSERVATION ⚠️ | ctp-user-api-5.3.351.jar + 语雀 0097 | ✅ |

## 执行流程

1. 识别用户场景 → 进入对应 SPI 文件夹
2. 读 `README.md` 了解场景、接口、代码骨架
3. 读 `constraints.md` 了解独有约束
4. 生成代码前先读 `references/spi-domain-constraints.md`（全局公共约束）

## 索取清单

```
P0:
1. ✅ organization-facade jar（含 AbstractAddressBookSpiService、AddressBookMemberDto）→ FACT
2. ✅ ctp-user-api jar（含 PasswordCheckService）→ FACT
3. ❌ ctp-user-api 更高版本（含 AbstractAuthenticationCheckService）→ 冻结

P1:
4. AddressBookMemberDto 完整字段列表（jar 反编译截断）
5. spring.factories key 确认
```
