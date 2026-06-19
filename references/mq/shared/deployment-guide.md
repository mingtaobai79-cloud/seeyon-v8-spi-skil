# MQ SPI 工程落点与部署

## 开发前准备

所有 SPI 开发/生成/改造前先读：`references/spi-domain-constraints.md`。该文档记录客开管理入口、父 POM modules、`spring.factories`、`spi_info.json`、scope、构建和重启规则。

## Super SPI 落点

MQ 是独立 SPI 子域。若用户明确要求生成工程代码，推荐落到：

```text
custom-backend/
├── spi-common/
├── spi-sso/        # 第一子域：SSO
└── spi-mq/         # 第二子域：MQ
    ├── pom.xml
    ├── src/main/java/com/seeyon/extend/spi/mq/...
    └── src/main/resources/
        ├── META-INF/spring.factories
        └── metadata/spi_info.json
```

父 POM 增加：

```xml
<module>spi-mq</module>
```

## POM 依赖

平台 MQ：

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>boot-starter-mq</artifactId>
  <version>5.8.0</version>
</dependency>
```

代码中必须使用的核心 FQN：

```java
com.seeyon.boot.starter.mq.spi.MQMessageSpi
com.seeyon.boot.starter.mq.support.dto.MessageDto
```

阿里云 RocketMQ / ONS 样例依赖：

```xml
<dependency>
  <groupId>com.aliyun.openservices</groupId>
  <artifactId>ons-client</artifactId>
  <version>1.8.8.5.Final</version>
</dependency>
```

## spring.factories

格式：接口全路径 = 实现类全路径。

示例：

```properties
com.seeyon.boot.starter.mq.spi.MQMessageSpi=com.seeyon.extend.spi.mq.rocketmq.AliRocketMqMessageSpi
```

如果沿用样例包名，则是：

```properties
com.seeyon.boot.starter.mq.spi.MQMessageSpi=com.seeyon.ali.rocketmq.AliOnesMqService
```

实现类必须显式实现 `MQMessageSpi` 四个方法，不要依赖接口 default `true`。

## spi_info.json

MQ 文档写明生效范围是全系统，因此推荐：

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["ALL"]
}
```

## Nacos 配置

观察到的自定义配置键（非平台标准）：

```yaml
seeyon:
  ones:
    accessKey: "${ALIYUN_ROCKETMQ_ACCESS_KEY}"
    secretKey: "${ALIYUN_ROCKETMQ_SECRET_KEY}"
    send-time-out: "3000"
    server: "{aliyun_rocketmq_name_srv_addr}"
```

平台原生 MQ 配置前缀为 `seeyon.mq`，见 `references/mq/shared/contract.md#11-mqproperties-配置契约-fact-`。`seeyon.ones.*` 这类命名只能视为现场自定义三方连接配置，不等同于平台原生配置。

通用命名建议（非官方事实）：

```yaml
seeyon:
  mq:
    aliyun:
      accessKey: "${ALIYUN_ROCKETMQ_ACCESS_KEY}"
      secretKey: "${ALIYUN_ROCKETMQ_SECRET_KEY}"
      nameSrvAddr: "{aliyun_rocketmq_name_srv_addr}"
      sendTimeoutMillis: "3000"
```

生成时需二选一：

- 若目标是兼容现场既有实现，沿用现场已有配置前缀。
- 若目标是通用 MQ 子域，使用 `seeyon.mq.aliyun.*` 并在 README 说明。

## 部署与重启

官方文档要求：重启所有服务。

部署说明必须明确：

1. 构建 SPI jar。
2. 上传/部署 MQ SPI。
3. 配置 Nacos MQ 连接信息。
4. 重启所有服务，而不是只重启某个单服务。
