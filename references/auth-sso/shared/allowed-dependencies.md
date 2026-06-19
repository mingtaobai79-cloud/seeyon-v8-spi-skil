# Allowed Dependencies（封闭世界代码生成约束）

> **Rule-002: Closed-world Code Generation**
> 生成的代码只能使用白名单中的包和类。未在白名单中的依赖一律禁止。

## 约束层级

```
Layer 1: API Registry（生成前）
  → 扫描 jar，提取可用类和方法
  → 生成 allowed_packages 白名单

Layer 2: Prompt Constraint（生成时）
  → 注入白名单到生成上下文
  → 模型只能使用白名单中的类

Layer 3: Import Check（生成后）
  → Health Check 验证所有 import 语句
  → 非白名单 import → FAIL
```

## 白名单（Always Allowed）

### Tier 0: JDK 标准库（无需声明）

```yaml
always_allowed:
  - java.lang.*
  - java.util.*
  - java.io.*
  - java.net.*
  - java.nio.*
  - java.time.*
  - java.math.*
  - java.text.*
  - java.security.*
  - javax.crypto.*
  - javax.servlet.*
  - javax.annotation.*
  - javax.validation.*
```

### Tier 1: V8 平台 API（按模式自动注入）

```yaml
mode_a:
  - com.seeyon.ctp.user.api.sso.*
  - com.seeyon.ctp.user.dto.*
  - com.seeyon.ctp.user.enums.*
  - com.seeyon.ctp.user.exception.*
  - com.seeyon.ctp.user.annotation.*
  - com.seeyon.ctp.user.util.*

mode_b:
  - com.seeyon.ctp.user.api.avoidlogin.*
  - com.seeyon.ctp.user.dto.*
  - com.seeyon.ctp.user.exception.*
  - com.seeyon.ctp.user.util.*

mode_c:
  - com.seeyon.cip.connector.api.sso.*
  - com.seeyon.cip.connector.enums.*
```

### Tier 2: V8 平台通用包（Always Allowed）

```yaml
platform_common:
  - com.seeyon.boot.util.*          # JsonUtils, StringUtils, IpUtils, DateUtils 等
  - com.seeyon.boot.annotation.*    # @MessageInfo 等
  - com.seeyon.boot.context.*       # Apps.getApplicationContext()
  - com.seeyon.boot.exception.*     # BusinessException
  - com.seeyon.boot.starter.*       # MessageProducer 等
  - com.seeyon.boot.util.encrypt.*  # SM2Utils 等
```

### Tier 3: 常用三方库（需显式声明在 POM 中）

```yaml
common_third_party:
  - cn.hutool.*                     # hutool-all（HTTP、加密、集合工具）
  - lombok.*                        # @Slf4j, @Getter, @Setter
  - org.slf4j.*                     # 日志接口
  - com.alibaba.fastjson.*          # JSON 处理（部分项目使用）
  - org.apache.commons.lang3.*      # 通用工具
  - org.apache.commons.collections4.* # 集合工具
```

### Tier 4: 策略特有依赖（按策略自动注入）

```yaml
strategy_deps:
  oauth2:
    - cn.hutool.http.*              # HTTP 调用
  jwt:
    - com.auth0.jwt.*               # JWT 解析
    - com.auth0.jwt.algorithms.*
  sm2:
    - com.seeyon.boot.util.encrypt.* # SM2Utils
  rsa:
    - java.security.*               # JDK RSA
  cas:
    - com.eetrust.security.*        # CA SDK（三方 jar）
  aes:
    - cn.hutool.crypto.*            # hutool AES
```

## 黑名单（Always Forbidden）

```yaml
always_forbidden:
  # 不允许直接操作数据库
  - java.sql.*
  - javax.persistence.*
  - org.hibernate.*
  - com.baomidou.*
  - org.mybatis.*

  # 不允许直接操作 Redis（除非项目显式需要）
  - org.springframework.data.redis.*
  - redis.clients.*

  # 不允许引入其他微服务的内部包
  - com.seeyon.ctp.user.service.*   # 内部 service 层
  - com.seeyon.ctp.user.dao.*       # 内部 dao 层
  - com.seeyon.ctp.user.mapper.*    # 内部 mapper 层
  - com.seeyon.ctp.user.repository.* # 内部 repository 层

  # 不允许使用 Spring 容器注解（SPI 不在 Spring 容器中）
  - org.springframework.beans.factory.annotation.Autowired  # 禁止 @Autowired
  - org.springframework.beans.factory.annotation.Value      # 禁止 @Value
  - org.springframework.stereotype.Component                # 禁止 @Component
  - org.springframework.stereotype.Service                  # 禁止 @Service（模式 A/B）

  # 不允许动态加载未知类
  - java.lang.ClassLoader.loadClass
  - java.lang.reflect.*（除明确需要外）
```

## Jar 扫描流程

当用户提供 jar 文件时：

```
Step 1: 扫描 jar 中的所有 class
  → jar tf xxx.jar | grep ".class$"

Step 2: 提取 public interface / class
  → javap 每个 class，提取 public 方法签名

Step 3: 生成 API Registry
  → allowed_packages: [从 jar 中提取的包列表]
  → allowed_classes: [从 jar 中提取的类列表]
  → allowed_methods: [从 jar 中提取的方法签名]

Step 4: 合并白名单
  → Tier 0 (JDK) + Tier 1 (平台 API) + Tier 2 (通用) + Tier 3 (三方) + Tier 4 (策略) + Jar 扫描结果

Step 5: 注入生成上下文
  → 生成代码时只能使用合并后的白名单
```

## Import Check 规则（Health Check 扩展）

```yaml
Rule-013: Import 白名单检查
  check: |
    遍历生成代码中的所有 import 语句
    对每个 import:
      1. 检查是否在 Tier 0-4 白名单中
      2. 检查是否在 Jar 扫描结果中
      3. 检查是否在黑名单中
  pass: 所有 import 在白名单中且不在黑名单中
  fail: 发现非白名单 import 或黑名单 import
  report: |
    [FAIL] Rule-013: 发现非白名单 import
      → import: org.springframework.data.redis.core.RedisTemplate
      → 原因: 不在白名单中
      → 修复: 移除此 import，使用 V8 OpenAPI 替代
```

## POM 依赖检查

生成的 POM 中每个 dependency 必须满足以下条件之一：

1. 在 Tier 1（平台 API）中
2. 在 Tier 3（常用三方库）中
3. 在 Tier 4（策略特有依赖）中
4. 用户显式提供的三方 jar（放根目录 third-jar/ 暂存，install/deploy 后按 Maven 坐标引用）

不允许出现"凭空引入"的依赖。

## 特殊规则

### 模式 A/B 的 @Service 限制

```yaml
mode_a_b:
  forbidden:
    - "@Service"      # SPI 类不加 @Service
    - "@Component"    # SPI 类不加 @Component
    - "@Autowired"    # 用 CtpUserSpiUtils.getInstance() 替代
  allowed:
    - "@Slf4j"        # 日志
    - "@CtpUserChannelRouter"  # 模式 A 必须
```

### 模式 C 的 @Service 规则

```yaml
mode_c:
  allowed:
    - "@Service"      # 模式 C 的 SsoService 实现类可以加 @Service
    - "@Slf4j"
  forbidden:
    - "@Autowired"    # 仍然禁止
```

### Bean 获取方式

```yaml
always:
  use: "CtpUserSpiUtils.getInstance(Xxx.class)"
  or: "App.getFactory().getBean(Xxx.class)"
  never: "@Autowired"
```
