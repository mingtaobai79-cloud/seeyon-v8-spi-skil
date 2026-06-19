# Auth-SSO 认证与单点登录 SPI 域

> 本目录整合认证与单点登录相关的新旧 SPI 内容，按 SPI 类型组织为独立文件夹。

## 目录结构

```
auth-sso/
├── index.md                    ← 本文件（总索引）
├── shared/                     ← 共享资源（策略、依赖、部署、健康检查等）
├── unified-auth/               ← 统一认证 SPI（模式 A）
├── avoid-login/                ← 免登 SPI（模式 B）
├── sso-connector/              ← SSO 连接器 SPI（模式 C）
├── auth-provider/              ← 认证提供者 SPI（登录扩展）
├── inbound-sso/                ← 入站 SSO SPI（三方→V8 免登）
├── outbound-sso/               ← 出站 SSO SPI（V8→三方单点）
├── mobile-app/                 ← 移动应用 SPI（V8 接入三方 App）
├── ticket-custom-userinfo/     ← 票据自定义用户信息 SPI
├── qrcode-login/               ← 二维码登录 SPI（M5 扫码登录 PC）
└── login-pre-portal/           ← 登录前门户 SPI（预置 jar + Nacos）
```

## SPI 文件夹索引

### Super SPI（高版本，金标准）

| SPI 文件夹 | 场景 | 接口 | Scope | 重启服务 |
|-----------|------|------|-------|----------|
| [unified-auth/](unified-auth/README.md) | V8 登录页接统一认证中心 | `CtpUserSsoAuthProviderService` | ctp-user | ctp-user |
| [avoid-login/](avoid-login/README.md) | 三方系统免登进入 V8 | `CtpAvoidLoginMiddlePageProviderService` / `CtpAvoidLoginClientModeProviderService` | ctp-user | ctp-user |
| [sso-connector/](sso-connector/README.md) | V8 菜单/磁贴/流程/待办跳转三方 | `SsoService` | cip-connector | cip-connector |

### Legacy SPI（旧版本，5.6 以下）

| SPI 文件夹 | 场景 | 接口 | Scope | 重启服务 |
|-----------|------|------|-------|----------|
| [auth-provider/](auth-provider/README.md) | 登录扩展 / 自定义认证方式 | `AbstractAuthenticationProvider` | ctp-user | ctp-user |
| [inbound-sso/](inbound-sso/README.md) | 三方→V8 免登（中间页+客户端+后端） | `CtpAvoidLoginMiddlePageProviderService` / `CtpAvoidLoginClientModeProviderService` / `CtpAvoidLoginBackendProviderService` | ctp-user | ctp-user |
| [outbound-sso/](outbound-sso/README.md) | V8→三方单点 | `SsoService` | cip-connector | cip-connector |
| [mobile-app/](mobile-app/README.md) | V8 接入三方 App（7 个接口） | `Mobile*ProviderService` | cip-connector | cip-connector |
| [ticket-custom-userinfo/](ticket-custom-userinfo/README.md) | ticket 返回人员信息自定义 | `CustomUserInfoService` | ctp-user | ctp-user |
| [qrcode-login/](qrcode-login/README.md) | M5 扫码登录 PC | `AbstractLoginQrCodeService` | ctp-user | ctp-user |
| [login-pre-portal/](login-pre-portal/README.md) | 登录前门户（预置 jar + Nacos） | 非 SPI | ctp-user / portal | ctp-user, portal |

## 共享资源

所有 SPI 共享以下资源，位于 [shared/](shared/) 目录：

| 文件 | 用途 |
|------|------|
| [auth-strategies.md](shared/auth-strategies.md) | 认证/加密策略（OAuth2/CAS/SM2/SM4/RSA/AES/OIDC/SAML/JWT/LDAP） |
| [allowed-dependencies.md](shared/allowed-dependencies.md) | SSO 依赖白名单/黑名单 |
| [version-matrix.md](shared/version-matrix.md) | SSO 相关版本矩阵 |
| [deployment-guide.md](shared/deployment-guide.md) | SSO 部署指导 |
| [health-check-rules.md](shared/health-check-rules.md) | SSO Health Check |
| [ctp-user-api-contract.md](shared/ctp-user-api-contract.md) | ctp-user SSO/免登契约 |
| [cip-connector-api-contract.md](shared/cip-connector-api-contract.md) | cip-connector SsoService 契约 |
| [validation-results.md](shared/validation-results.md) | SSO 资料校验记录 |

## 每个 SPI 文件夹的标准结构

```
{spi-name}/
├── README.md              ← 场景描述、接口定义、方法表格
├── constraints.md         ← 该 SPI 的独有约束
├── template.md            ← Nacos 配置模板、spring.factories 注册
├── code-skeleton.md       ← 完整代码骨架（含 JavaDoc、日志、错误处理）
└── prompts.md             ← 提示词、索取清单、生成指导
```

## 执行流程

1. 识别用户场景，定位到具体 SPI 文件夹
2. 读取该 SPI 的 `README.md` 了解场景和接口
3. 读取 `constraints.md` 了解独有约束
4. 读取 `template.md` 获取配置模板
5. 读取 `code-skeleton.md` 获取代码骨架
6. 如需共享资源（策略、部署、健康检查），查阅 `shared/` 目录
7. 生成代码前先读 `references/spi-domain-constraints.md`（全局公共约束）

## 公共方法双查规则

生成、改造或标注 SPI 方法时必须同时查询两类来源：

1. 子域契约：本目录对应 SPI 的 `README.md` / `constraints.md` / `shared/*contract*`，只用于接口 FQCN、SPI 方法签名、DTO、枚举、scope、spring.factories。
2. 平台公共方法：`references/platform-standard-library/index.md` 和 `references/platform-standard-library/decompiled/`，用于 boot-core / boot-starter-web / boot-starter-spi 的 JSON、HTTP、加密、BeanCopy、Transport Response/Request、RequestContext、BusinessException 等公共能力。

规则：凡是代码中要使用或标注公共 helper / Response / Request / 工具类方法，先查平台标准库；凡是 SPI 接口与 DTO，先查本子域契约。两边都查完再生成，禁止把平台公共类型误报成子域缺口，也禁止把子域契约包提升为全局公共方法。

## Evidence 状态

| SPI | 接口 Evidence | DTO Evidence | 契约来源 | 状态 |
|-----|--------------|--------------|----------|------|
| unified-auth | FACT ✅ | FACT ✅ | ctp-user-api-5.3.351.jar | ✅ |
| avoid-login | FACT ✅ | FACT ✅ | ctp-user-api-5.3.351.jar | ✅ |
| sso-connector | FACT ✅ | FACT ✅ | cip-connector-api-5.3.286.jar | ✅ |
| auth-provider | FACT ✅ | FACT ✅ | ctp-user-api-5.3.351.jar | ✅ |
| inbound-sso | FACT ✅ | FACT ✅ | ctp-user-api-5.3.351.jar | ✅ |
| outbound-sso | FACT ✅ | FACT ✅ | ctp-user-api-5.3.351.jar | ✅ |
| mobile-app | FACT ✅ | FACT ✅ | cip-connector-api-5.3.286.jar | ✅ |
| ticket-custom-userinfo | FACT ✅ | FACT ✅ | ctp-user-api-5.3.351.jar | ✅ |
| qrcode-login | FACT ✅ | FACT ✅ | ctp-user-api-5.3.351.jar | ✅ |
| login-pre-portal | OBSERVATION ⚠️ | N/A | 语雀文档 | 🧊 冻结 |

## 质量标准

- **Super SPI（unified-auth、avoid-login、sso-connector）**：金标准，接口全部 FACT ✅
- **Legacy SPI**：对标 Super SPI 深度，完整接口定义 + 方法表格 + 代码骨架 + Nacos 配置 + spring.factories
