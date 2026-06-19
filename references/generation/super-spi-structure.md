# Super SPI 统一工程结构

> 生成格式唯一来源。SSO 只是 `spi-sso` 子域，未来多个 SPI 通过 `spi-common` 融合。

## 唯一目录结构

可见模板目录：``。

```
custom-backend/
├── pom.xml
├── README.md
├── third-jar/
│   └── README.md
├── spi-common/
│   ├── pom.xml
│   └── src/main/java/com/seeyon/extend/spi/common/
│       ├── config/
│       ├── crypto/
│       ├── http/
│       ├── json/
│       └── util/
├── spi-sso/
│   ├── pom.xml
│   ├── src/main/java/com/seeyon/extend/spi/sso/
│   │   ├── unifiedauth/    # 统一认证 / 登录页接统一认证中心（模式 A）
│   │   ├── avoidlogin/     # 三方 → V8 免登（模式 B）
│   │   ├── connector/      # V8 → 三方单点（模式 C）
│   │   └── support/
│   └── src/main/resources/
│       ├── META-INF/spring.factories
│       └── metadata/spi_info.json
└── spi-{domain}/
```

## 模块职责

Auth/SSO 详细导航见：`references/auth-sso/index.md`。

- `spi-common`: 公共代码模块，不注册 SPI，不放 `spring.factories`，不放 `spi_info.json`。
- `spi-sso`: SSO/统一认证唯一落点，模式 A/B/C 在模块内分包。
  - `unifiedauth/`: 统一认证，登录页接统一认证中心，V8 认证登录扩展。
  - `avoidlogin/`: 三方系统登录后免登进入 V8。
  - `connector/`: V8 菜单/入口单点到三方系统。
- `spi-{domain}`: 后续新增其他 SPI 子域，如移动端、连接器扩展、消息等。
- `third-jar`: 本地/私有三方 jar 暂存区，不是 `lib/`。jar 必须 install/deploy 成 Maven 坐标后在 POM 引用。

## 禁止

- 禁止生成 `lib/`。
- 禁止生成独立 system-scope 平台 API 项目。
- 禁止把 SSO/统一认证拆成多个 `spi-sso-*` 模块。
- 禁止在 `spi-common` 中注册 SPI。

## 依赖规则

- 平台 API: `ctp-user-api` / `cip-connector-api` 通过 Maven dependency 引用。
- 公共代码: 业务模块依赖 `spi-common`。
- 私有 jar: 先 `mvn install:install-file` 或 deploy 到私服，再按坐标引用。
