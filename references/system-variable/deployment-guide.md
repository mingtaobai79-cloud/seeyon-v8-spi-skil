# 系统变量 SPI 工程落点与部署

## Super SPI 落点

系统变量扩展是独立 SPI 子域。若用户明确要求生成工程代码，推荐落到：

```text
custom-backend/
├── spi-common/
├── spi-sso/                 # SSO 子域
├── spi-mq/                  # MQ 子域
└── spi-system-variable/     # 系统变量扩展子域
    ├── pom.xml
    ├── src/main/java/com/seeyon/extend/spi/systemvariable/...
    └── src/main/resources/
        ├── META-INF/spring.factories
        └── metadata/spi_info.json
```

父 POM 增加：

```xml
<module>spi-system-variable</module>
```

## POM 依赖

平台公式/系统变量能力：

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>boot-starter-formula</artifactId>
  <version>5.30.6</version>
</dependency>
```

> 该坐标来自语雀 rendered-md，Evidence 为 OBSERVATION；现场生成前需核对目标 V8 私服/源码/jar。

## spring.factories

格式仍按 SPI 通用形态：接口全路径 = 实现类全路径。

```properties
<confirmed SystemVariableSPIService FQCN>=com.seeyon.extend.spi.systemvariable.CustomSystemVariableService
```

`SystemVariableSPIService` 的 full qualified name 未出现在 rendered-md 中，禁止在未确认前写死。

## spi_info.json

系统变量文档未给出 scope 细节。默认生成时建议沿用 Super SPI 通用元数据，并在交付报告标注待现场确认：

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["ALL"]
}
```

如果后续 jar/source 证明系统变量只对 UDC 应用生效，应按现场要求调整 scope。

## 部署与重启

语雀文档要求：重启 UDC 应用对应的服务。

部署说明必须明确：

1. 构建 SPI jar。
2. 上传/部署系统变量 SPI。
3. 确认 `boot-starter-formula` 依赖在现场可解析。
4. 重启 UDC 应用对应服务。
5. 在计算条件弹框中验证系统变量是否出现、排序是否符合预期、隐藏变量是否不再可选。

## 验证重点

1. POM XML well-formed，父 POM 注册 `spi-system-variable`。
2. 不存在 `lib/` 和默认 `systemPath`。
3. `spi-common` 不注册 SPI。
4. `spi-system-variable` 包含 `META-INF/spring.factories` 和 `metadata/spi_info.json`。
5. 实现类实现已确认 FQCN 的 `SystemVariableSPIService`。
6. 每个系统变量方法：`public`、无参数、带 `@SPISystemVariable`、返回基本类型或基本类型集合。
7. 使用 `relationEntity` 时，fullName 与返回值语义匹配。
8. 部署后重启 UDC 应用对应服务。
