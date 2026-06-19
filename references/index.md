# Seeyon V8 SPI 域索引

> 本目录按 SPI 子域组织，每个子域包含接口定义、DTO、代码骨架和约束。

## 域目录

| 域 | 场景 | SPI 数量 | 状态 |
|----|------|---------|------|
| [account-org-security/](account-org-security/index.md) | 通讯录脱敏、登录人数控制、密码策略 | 3 | ✅ 2 / 🧊 1 |
| [auth-sso/](auth-sso/index.md) | 认证与单点登录（统一认证、免登、SSO 连接器等） | 10 | ✅ 9 / 🧊 1 |
| [capability-channel/](capability-channel/index.md) | 能力通道扩展（28 项基础能力） | 28 | ✅ 28 |
| [crypto/](crypto/index.md) | 加解密（散列、对称） | 2 | 🧊 2 |
| [datasource/](datasource/index.md) | 数据源扩展 | 1 | ✅ 1 |
| [entry-menu-mobile/](entry-menu-mobile/index.md) | 三方菜单、移动插件 | 2 | ✅ 2 |
| [file-storage/](file-storage/index.md) | 文件存储（上传下载拦截、新存储接入） | 2 | ✅ 1 / 🧊 1 |
| [infra-config-registry/](infra-config-registry/index.md) | 注册中心、配置中心扩展 | 2 | ✅ 2 |
| [integration-sync/](integration-sync/index.md) | 三方集成同步（待办批处理、接口鉴权、组织同步） | 3 | ✅ 3 |
| [mq/](mq/index.md) | 消息队列（RocketMQ / ONS） | 1 | ✅ 1 |
| [system-variable/](system-variable/index.md) | 系统变量扩展 | 1 | 🧊 1 |
| [workflow-document/](workflow-document/index.md) | 流程 / 公文（BPM SPI、公文扩展） | 2 | ✅ 1 / 🧊 1 |

**总计：12 域 / 57 SPI/能力项**

## Evidence 状态说明

- ✅ **FACT**：接口 FQCN、方法签名、DTO 字段已通过 jar 反编译确认
- ⚠️ **OBSERVATION**：基于语雀文档推断，未通过 jar 验证
- 🧊 **冻结**：缺少必要 jar 包，无法升级到 FACT

## 冻结清单（缺少 jar 包）

| 域 | SPI | 缺失 jar | 阻塞原因 |
|----|-----|---------|---------|
| account-org-security | auth-check | ctp-user-api (更高版本) | `AbstractAuthenticationCheckService` 在 5.3.351/5.3.429 中不存在 |
| auth-sso | login-pre-portal | boot-starter-login-pre-portal | 预置 jar + Nacos 配置模式，非标准 SPI |
| crypto | digest | boot-starter-encrypt | artifact 在仓库中不存在 |
| crypto | symmetric | boot-starter-encrypt | artifact 在仓库中不存在 |
| file-storage | storage-interceptor | boot-starter-file (更高版本) | `StorageInterceptorSpi` 在 5.3.358 中未找到 |
| system-variable | system-variable-spi | boot-starter-systemvariable / boot-starter-formula | 5.3.313 和 5.30.6 均不包含 SPI 接口类 |
| workflow-document | edoc | edoc-facade | `EdocProjectPublicService` 接口未找到 |

## 执行流程

1. 识别用户场景 → 进入对应域目录
2. 读域 `index.md` 了解子场景和 SPI 列表
3. 进入具体 SPI 文件夹，读 `README.md` 和 `constraints.md`
4. 生成代码前先读 `spi-domain-constraints.md`（全局公共约束）

## 结构/治理索引

| 主题 | 入口 |
|------|------|
| 架构控制、Evidence 总协议、知识治理 | [architecture-control-protocol.md](architecture-control-protocol.md) |
| Evidence 分级细则 | [status/evidence-system.md](status/evidence-system.md) |
| Contract Index 总入口 | [contract-index/overview.md](contract-index/overview.md) |
| Contract Index 模块治理 | [contract-index/contract-index-module.md](contract-index/contract-index-module.md) |
| Contract Bundle | [contract-index/contract-bundle.md](contract-index/contract-bundle.md) |
| Contract Discovery | [contract-index/contract-discovery.md](contract-index/contract-discovery.md) |
| Contract Normalization | [contract-index/contract-normalization.md](contract-index/contract-normalization.md) |
| External/OpenAPI Contract Index | [contract-index/external-contract-index.md](contract-index/external-contract-index.md) / [contract-index/openapi-index.md](contract-index/openapi-index.md) |
| Jar Contract Indexing | [contract-index/jar-contract-indexing-plan.md](contract-index/jar-contract-indexing-plan.md) |
| Knowledge Organization | [workflows/knowledge-organization.md](workflows/knowledge-organization.md) |
| Runtime Modes | [workflows/runtime-modes.md](workflows/runtime-modes.md) |
| Skill Architecture Health Check | [workflows/skill-architecture-health-check.md](workflows/skill-architecture-health-check.md) |
| Skill 架构收口审计 / closeout gate | [audits/architecture-closeout-gate.md](audits/architecture-closeout-gate.md) |
| Closeout hygiene 小收敛 patch | [workflows/closeout-hygiene-patch-pattern.md](workflows/closeout-hygiene-patch-pattern.md) |
| SPI Deployment Guide | [generation/spi-deployment-guide.md](generation/spi-deployment-guide.md) |
| Super SPI Structure | [generation/super-spi-structure.md](generation/super-spi-structure.md) |

## 共享资源

| 文件 | 用途 |
|------|------|
| [spi-domain-constraints.md](spi-domain-constraints.md) | 全局 SPI 域约束（所有域共用） |
| [platform-standard-library/](platform-standard-library/index.md) | 平台标准库 FACT 索引：生成前优先复用 boot 通用基础能力；子域 API 只按 contract 引入 |
| [facts/](facts/) | 跨域共享事实（部署、版本、依赖等） |
| [contract-index/](contract-index/) | 契约索引（jar 反编译工具、版本矩阵） |
