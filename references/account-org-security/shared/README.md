# 账号/组织/安全域共享资源

> 三个 SPI 都依赖 ctp-user-api 或 ctp-organization-facade，部署到 ctp-user 或 ctp-organization 微服务。

## 公共约束

1. 三个 SPI 互相独立，不共享实现类。
2. address-book 部署到 ctp-organization 服务，另外两个部署到 ctp-user 服务。
3. 所有接口都是 abstract class 或 interface，实现类继承/实现即可。
4. 不需要额外 Nacos 配置（除非业务逻辑需要）。

## 依赖版本

| SPI | 依赖 | 文档示例版本 |
|-----|------|-------------|
| address-book | ctp-organization-facade | 5.0.2 |
| auth-check | ctp-user-api | 3.12.1 |
| password-policy | ctp-user-api | 5.0.3 |

注意：版本号是文档示例，生成时优先使用现场父 POM/BOM 管理的版本。
