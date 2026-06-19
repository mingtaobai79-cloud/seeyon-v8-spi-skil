# MQ SPI 示例工程生成与验证记录

## 背景

用户要求基于 `references/mq/` 测试生成一个项目并打包。目标不是只验证文档存在，而是验证 MQ 子域能驱动一个最小 Super SPI 工程骨架。

## 生成形态

推荐测试工程结构：

```text
custom-backend/
├── pom.xml
├── spi-common/
│   └── pom.xml
└── spi-mq/
    ├── pom.xml
    └── src/main/
        ├── java/com/seeyon/extend/spi/mq/rocketmq/AliRocketMqMessageSpi.java
        └── resources/
            ├── META-INF/spring.factories
            ├── metadata/spi_info.json
            └── application-mq-example.yml
```

## 关键生成规则

- 父 POM 必须包含 `<module>spi-common</module>` 与 `<module>spi-mq</module>`。
- `spi-common` 不是 SPI：不得放 `spring.factories`，不得放 `metadata/spi_info.json`。
- `spi-mq` 依赖：
  - `com.seeyon:boot-starter-mq:5.8.0`（除非现场指定其他版本）
  - `com.aliyun.openservices:ons-client:1.8.8.5.Final`（阿里云 ONS 样例）
- `spring.factories` 注册：
  ```properties
  com.seeyon.boot.starter.mq.spi.MQMessageSpi=com.seeyon.extend.spi.mq.rocketmq.AliRocketMqMessageSpi
  ```
- `spi_info.json` 推荐：
  ```json
  {"name":"boot-starter-spi-customized","scopes":["ALL"]}
  ```
- Java 实现必须：
  - `implements MQMessageSpi`
  - 实现 `send` / `sendBatch` / `subscribeTopic` / `unSubscribeTopic`
  - 使用 `MQSerializer.serialize(messageDto)`，不是只序列化 `data` 或手写 JSON
  - 消费时 `MQSerializer.deserialize(message.getBody())`
  - 消费后调用 `MessageListenerService.invoke(messageDto)`
  - 使用 `Apps.getBeanFactory()` / `Apps.getEnvironment()` 获取平台 bean/config
  - 禁止 `@Autowired` / `@Service` / `@Component`

## 验证清单

最小静态验证应覆盖：

1. 文件存在且非空。
2. 所有 POM XML well-formed。
3. 父 POM module 正确。
4. 依赖版本正确。
5. Java 实现和四个方法存在。
6. `MQSerializer` / `MessageListenerService.invoke` 存在。
7. 无 Spring 注解。
8. `spring.factories` 值精确匹配。
9. `spi_info.json` JSON well-formed 且 `scopes == ["ALL"]`。
10. `spi-common` 没有 SPI 注册文件。
11. 若本机有 Maven，可尝试 `mvn validate -DskipTests`；但 Maven 未安装或私服依赖不可达属于环境状态，不应覆盖静态结构验证结论。

## 产物打包

测试项目生成后可把整个工程目录打成 zip，并在根目录写 `VALIDATION.md`，记录 PASS/FAIL 和环境状态。