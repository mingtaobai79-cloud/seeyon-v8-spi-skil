# Runtime Modes（运行模式定义）[FACT ✅]

> Rule-003: Deployment Context First — 生成代码前必须先判定运行模式。

---

## 模式判定决策树

```
用户提到 SPI / 客开平台 / 上传 jar / spring.factories / spi_info.json？
  → SUPER_SPI

用户提到多个 SPI / 超级 SPI / 融合多个 SPI？
  → SUPER_SPI

用户提到 SSO / 单点登录 / 免登 / 统一认证？
  → SUPER_SPI + spi-sso

无法判断？
  → 追问
```

---

## SUPER_SPI（统一 SPI 插件工程）

### 运行环境
- 运行在已有 V8 微服务内部（ctp-user 或 cip-connector）
- 控制当前 custom-backend/Super SPI 工程 pom
- 依赖要收敛，避免与平台冲突

### 部署流程
```
开发 → 打包 SPI Jar → 上传客开平台 → Nacos 配置 → 服务动态加载
```

### 依赖来源
- **平台已有**：com.seeyon.*, com.cip.*, hutool, slf4j, lombok
- **平台依赖**：通过 Maven dependency 引入 `ctp-user-api` / `cip-connector-api`
- **三方依赖**：优先 Maven 坐标；本地/私有 jar 统一放根目录 `third-jar/`，install/deploy 后再按 dependency 引用

### 禁止
- `@Autowired` / `@Component` / `@Service` / `@Configuration`（不在 Spring 容器）
- `@RestController`（不是独立服务）
- `java.sql.*` / `javax.persistence.*`（不允许直接操作数据库）
- `org.springframework.data.redis.*`（不允许直接操作 Redis）
- `com.seeyon.ctp.user.service/dao/mapper.*`（不允许访问内部层）

### 允许
- `CtpUserSpiUtils.getInstance(Xxx.class)` — SPI 内部单例
- `CtpUserSpiUtils.getBean(Xxx.class)` — 获取 Spring Bean
- `CtpUserSpiUtils.getPropertyByName("key")` — 读 Nacos 配置
- `CtpUserSpiUtils.getRequest()` — 获取 HttpServletRequest
- `CipConnectorSpiUtils.*` — cip-connector 版本的工具类

### 文件结构
```
custom-backend/
├── pom.xml
├── third-jar/
├── spi-common/
│   ├── pom.xml
│   └── src/main/java/...
├── spi-sso/
│   ├── pom.xml
│   ├── src/main/java/...
│   └── src/main/resources/
│       ├── META-INF/spring.factories
│       └── metadata/spi_info.json
└── spi-{domain}/
```

### 谨慎使用的依赖
- guava（可能和平台版本冲突）
- fastjson（可能和平台版本冲突）
- jackson 新版（可能和平台版本冲突）

---

## CUSTOM_BRAND / 独立服务

当前 skill 不生成独立 Spring Boot 服务。用户明确要独立服务时，应说明这不属于本 Super SPI 生成格式，除非后续另建 skill/项目。

---

## 模式对比表

| 特性 | SUPER_SPI 统一格式 |
|------|-------------------|
| 运行环境 | V8 微服务内部 |
| 依赖管理 | Maven dependency；root `third-jar/` 仅作本地/私有 jar 暂存 |
| Spring 注解 | 禁止 @Autowired 等 |
| 工具类 | CtpUserSpiUtils / CipConnectorSpiUtils / App.getFactory() |
| 配置文件 | Nacos |
| 部署方式 | 上传客开平台或 SPI jar 部署 |
| spring.factories | 业务 SPI 模块必须；spi-common 禁止 |
| spi_info.json | 业务 SPI 模块必须；spi-common 禁止 |
| 重启服务 | ctp-user / cip-connector / 对应 scope 服务 |

---

## SSO 场景下的模式选择

| SSO 模式 | 运行模式 | 说明 |
|----------|---------|------|
| A: 统一认证 / V8 认证登录 | SUPER_SPI + `spi-sso/unifiedauth` | 实现 CtpUserSsoAuthProviderService |
| B: 三方→V8 免登 | SUPER_SPI + `spi-sso/avoidlogin` | 实现 CtpAvoidLogin*ProviderService |
| C: V8→三方单点 | SUPER_SPI + `spi-sso/connector` | 实现 SsoService |
| 多 SPI 融合 | SUPER_SPI | `spi-common` + 多个 `spi-*` 模块 |

**注意：** 当前 skill 以 SSO 为首个子域，但生成格式始终是 SUPER_SPI：
- 模式 A/B/C → 全部进入 `spi-sso` 分包；统一认证固定放 `spi-sso/unifiedauth`
- 公共能力 → `spi-common`
- 如果用户明确说"独立部署" → 不使用本 skill 生成，说明需另建独立 Spring Boot 项目
