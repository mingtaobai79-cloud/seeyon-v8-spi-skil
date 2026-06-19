# Deployment Guide（部署指导模板）

> 生成代码后自动输出，用户按步骤操作即可。

## 模板结构

生成的 `deploy.md` 应包含以下章节：

---

### 1. Nacos 配置

```markdown
## 1. Nacos 配置

在 Nacos 中找到 **{微服务名}** 微服务，添加以下配置：

```yaml
{生成的 nacos.yaml 内容}
```

**注意：**
- 替换 `xxx` 为实际值
- 配置格式选择 YAML
- Data ID 和 Group 与现有配置保持一致
```

### 2. 构建

```markdown
## 2. 构建

### 方式一：客开管理平台构建（推荐）

1. 登录 V8 后台 → 系统管理 → 客开管理
2. 上传代码包（整个 custom-backend/Super SPI 工程打包为 zip，包含 spi-common、spi-sso、root third-jar）
3. 点击「构建」
4. 等待构建完成

### 方式二：本地 Maven 构建

```bash
cd custom-backend
mvn clean package -DskipTests
```

构建产物：业务模块 jar，例如 `spi-sso/target/spi-sso-1.0.0-TEST-SNAPSHOT.jar`；`spi-common` 只作为依赖模块不单独部署为 SPI
```

### 3. 部署

```markdown
## 3. 部署

### 通过客开管理平台（推荐）

1. 登录 V8 后台 → 系统管理 → 客开管理
2. 构建成功后自动部署

### 手动部署

1. 将 jar 包上传到服务器
2. 如果是 SPI 扩展：通过客开管理平台导入
3. 如果是文件 SPI：参考 README.md 中的文件 SPI 扩展通路
```

### 4. 重启服务

```markdown
## 4. 重启服务

**必须重启 {服务名} 服务才能生效。**

```bash
# Docker 环境
docker restart {container_name}

# 或直接重启微服务
# {服务名} = ctp-user（模式 A/B）或 cip-connector（模式 C）
```

**验证服务启动：**
- 查看日志确认无报错
- 访问 V8 后台确认服务正常
```

### 5. 验证

```markdown
## 5. 验证

### 模式 A（V8 认证登录）

1. 浏览器访问 V8 域名
2. 应自动跳转到三方认证中心登录页
3. 输入三方账号密码
4. 认证成功后应回到 V8 首页
5. 检查 V8 日志确认无报错

### 模式 B（三方→V8 免登）

1. 在三方系统中点击跳转到 V8 的链接
2. 链接格式：`{V8域名}/seeyon/reportLogin.do?sytype={third_type}&syid={标识}&{参数}`
3. 应免登进入 V8 页面
4. 检查 V8 日志确认用户匹配成功

### 模式 C（V8→三方单点）

1. 登录 V8
2. 点击配置好的菜单/磁贴
3. 应自动跳转到三方系统并完成登录
4. 检查浏览器地址栏确认 token 参数正确
```

### 6. 停用方案

```markdown
## 6. 停用

如果出现问题：

1. 在客开管理平台停用或删除对应的 SPI 扩展包
2. 重启 {服务名} 服务
3. 删除 Nacos 中新增的配置
4. 确认 V8 原登录链路正常
```

### 7. 常见问题

```markdown
## 7. 常见问题

### Q: 重启后 SPI 不生效？
A: 检查 spring.factories 接口路径是否正确，检查 spi_info.json scopes 是否匹配。

### Q: 报 ClassNotFoundException？
A: 检查 ctp-user-api / cip-connector-api 版本是否与 V8 平台版本匹配。

### Q: 认证失败但无错误提示？
A: 检查日志，确认使用 CtpUserSpiSsoException 而非 RuntimeException。

### Q: 多账号切换不生效？（模式 B）
A: 在 Nacos 中添加 seeyon.avoid.clearCookieTypes 配置。

### Q: userMap 为空？（模式 C）
A: 确认 needUserBind() 返回 true。
```

---

## verify.md 模板

```markdown
# 验证清单

## 部署前检查

- [ ] Nacos 配置已添加
- [ ] 配置值已替换为实际值（无 xxx 占位符）
- [ ] 构建成功，jar 包已生成
- [ ] jar 包已部署

## 功能验证

- [ ] 服务重启成功，日志无报错
- [ ] SSO 流程正常（按模式验证）
- [ ] 用户匹配正确
- [ ] 错误处理正常（故意传错参数测试）
- [ ] 移动端正常（如需要）

## 日志检查

- [ ] 入口日志打印正常
- [ ] 无 NullPointerException
- [ ] 无 ClassNotFoundException
- [ ] 三方接口调用成功

## 回归测试

- [ ] V8 正常登录不受影响
- [ ] 其他 SPI 扩展不受影响
- [ ] 系统管理功能正常
```

---

## nacos.yaml 生成规则

根据模式和策略自动生成 Nacos 配置：

### 模式 A

```yaml
seeyon:
  auth:
    type: spisso
  thirdauth:
    type: {channel_type}
  {project_id}:
    clientId: {third_auth_client_id}  # 三方应用 ID
    clientSecret: CHANGE_ME_IN_NACOS  # 三方应用密钥
    loginUrl: {third_login_url}          # 三方登录地址
    tokenUrl: {third_token_url}          # token 接口地址
    userInfoUrl: {third_user_info_url}       # 用户信息接口地址
    logoutUrl: {third_logout_url}         # 三方登出地址（可选）
```

### 模式 B

```yaml
seeyon:
  thirdauth:
    clientId: {third_auth_client_id}
    clientSecret: CHANGE_ME_IN_NACOS
  openApi:
    appKey: {v8_openapi_app_key}  # V8 OpenAPI appKey
    appSecret: CHANGE_ME_IN_NACOS     # V8 OpenAPI appSecret
    domain: {v8_openapi_domain}  # V8 OpenAPI 域名
  system:
    domain: {v8_domain}     # V8 域名
    protocol: https        # V8 协议
  {project_id}:
    # 策略特有配置
  avoid:
    clearCookieTypes:      # 多账号切换
      - {third_type_a}
      - {third_type_b}
```

### 模式 C

```yaml
# 模式 C 通常不需要额外 Nacos 配置
# 配置通过 V8 管理后台的集成应用设置页面填写
# 如果策略需要（如 RSA 公钥），则：
seeyon:
  {project_id}:
    publicKey: CHANGE_ME_IN_NACOS         # RSA 公钥（如帆软模式）
```
