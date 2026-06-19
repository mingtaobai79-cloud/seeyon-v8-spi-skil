# SPI 开发与部署规范 [FACT ✅ 官方文档]

> 来源：致远 V8 SPI 开发说明文档

---

## 1. spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["spi-app-name"]
}
```

- `name`: 固定值 `boot-starter-spi-customized`，请勿修改
- `scopes`: SPI 组件的适配范围
  - `ALL` — 针对所有应用
  - `ctp-user` — 仅 ctp-user 微服务（模式 A/B）
  - `cip-connector` — 仅 cip-connector 微服务（模式 C）
  - 其他具体应用 code

**多模块项目：** module 会被编译成一个 SPI jar，spi_info.json 只需 scopes：
```json
{
  "scopes": ["spi-app-name"]
}
```

## 2. spring.factories

```
com.seeyon.cip.connector.api.sso.SsoService=\
com.seeyon.extend.spi.sso.TemplateSsoServiceImpl
```

格式：`api包里面的接口全路径=手写实现代码的全路径`

### 各模式对应的接口全路径

| 模式 | 接口全路径 |
|------|-----------|
| A: V8认证 | `com.seeyon.ctp.user.api.sso.CtpUserSsoAuthProviderService` |
| B: 三方→V8 无中间页 | `com.seeyon.ctp.user.api.avoidlogin.CtpAvoidLoginClientModeProviderService` |
| B: 三方→V8 有中间页 | `com.seeyon.ctp.user.api.avoidlogin.CtpAvoidLoginMiddlePageProviderService` |
| B: 后端直接免登 | `com.seeyon.ctp.user.api.avoidlogin.CtpAvoidLoginBackendProviderService` |
| C: V8→三方 | `com.seeyon.cip.connector.api.sso.SsoService` |

## 3. 三方 jar 依赖

三方依赖统一走 Maven dependency。

- Maven/私服已有：直接在对应模块 POM 写 `<dependency>`
- 只有 jar 文件：统一放到根目录 `/third-jar` 暂存，然后执行 `mvn install:install-file` 或 deploy 到私服，最后仍用 Maven 坐标引用
- 禁止生成 `/lib` 目录
- 默认禁止 `systemPath`；只有客开平台或客户环境强制要求 jar 随包时，才允许对模块 root `third-jar/` 例外引用，并在 Health Check 标 WARN

示例：
```bash
mvn install:install-file \
  -Dfile=third-jar/vendor-sdk-1.0.0.jar \
  -DgroupId=com.vendor \
  -DartifactId=vendor-sdk \
  -Dversion=1.0.0 \
  -Dpackaging=jar
```

```xml
<dependency>
    <groupId>com.vendor</groupId>
    <artifactId>vendor-sdk</artifactId>
    <version>1.0.0</version>
</dependency>
```

## 4. 多模块项目

一个 Super SPI 工程可以包含多个 SPI 子域 module，每个业务 module 编译成独立 SPI jar；公共代码统一进入 `spi-common`。

```
custom-backend/
├── pom.xml                    # 父 POM (packaging: pom)
├── third-jar/                 # 本地/私有三方 jar 暂存区
├── spi-common/                # 公共模块，不注册 SPI
│   ├── pom.xml
│   └── src/main/java/...
├── spi-sso/                   # SSO/统一认证模块，融合模式 A/B/C
│   ├── pom.xml
│   ├── src/main/java/...
│   └── src/main/resources/
│       ├── META-INF/spring.factories
│       └── metadata/spi_info.json
└── spi-{domain}/              # 其他 SPI 子域
    ├── pom.xml
    └── ...
```

父 POM 模板：
```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.seeyon</groupId>
        <artifactId>boot</artifactId>
        <version>{v8_version}</version>
    </parent>
    <artifactId>boot-starter-spi-customized</artifactId>
    <version>1.0.0-TEST-SNAPSHOT</version>
    <packaging>pom</packaging>
    <name>custom-backend</name>
    <modules>
        <module>spi-common</module>
        <module>spi-sso</module>
        <module>spi-{domain}</module>
    </modules>
    <properties>
        <platform.version>{platform_version}</platform.version>
    </properties>
</project>
```

## 5. 客开 SPI 限制

### 文件 SPI 扩展

**当前客开通路不支持文件 SPI 扩展。** 文件存储 SPI 需要走独立通路：

#### 方式一：磁盘部署

1. 本地构建打包 jar
2. 上传 jar 到服务器磁盘
3. 修改对应服务的 Nacos 配置：

```yaml
seeyon:
  spi:
    enable: true
  file:
    storage-type: spi
    spiPlugins: 
    - file: /xxx/xxx/xxx.jar
```

4. 重启对应服务

#### 方式二：Nexus Maven 仓库部署

1. 本地构建打包 jar
2. 上传到 Nexus 仓库
3. 修改对应服务的 Nacos 配置：

```yaml
seeyon:
  spi:
    enable: true
  file:
    storage-type: spi
    spiPlugins: 
    - maven:com.seeyon,boot-starter-file-spi,1.0.0
  dynamic:
    loader:
      type: maven
      maven:
        releaseUrl: http://ip:端口/repository/maven-releases/
        snapshotUrl: http://ip:端口/repository/maven-snapshots/
        username: 账号
        password: 密码
```

4. 重启对应服务

## 6. 部署检查清单

### 标准客开通路部署（模式 A/B/C 通用）

1. ✅ 代码打包为 zip（含父 pom.xml、spi-common、业务 spi-*、root third-jar）
2. ✅ 上传到 V8 客开管理平台构建
3. ✅ 配置 Nacos（sm4Key / openApi 等）
4. ✅ 重启对应微服务（ctp-user 或 cip-connector）

### 文件 SPI 独立通路部署

1. ✅ 本地 `mvn clean package -DskipTests`
2. ✅ 上传 jar 到磁盘或 Nexus
3. ✅ 修改 Nacos 中 `seeyon.spi.enable: true` + `seeyon.file.spiPlugins`
4. ✅ 重启对应服务
