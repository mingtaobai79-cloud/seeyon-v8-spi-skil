# 天气查询能力通道独有约束

> 公共约束：`../../spi-domain-constraints.md`  

## 生成器规则

1. 生成前必须以目标 jar/source 核对 `com.seeyon.cip.provider.api.weather.WeatherProviderService` 的 FACT 方法签名；当前文档只作为模板基线。
2. required 方法必须实现；default 方法只在业务明确要求时覆盖。
3. `getChannelCode()` 必须稳定、唯一，不能返回空；建议来自配置常量或 Nacos，不要散落硬编码。
4. `getDescription()` 面向平台能力配置页面可读，不能写测试占位。
5. `getCapabilityEnum()` 必须使用目标 jar 中真实存在的 `CapabilityEnum` 枚举值；不确定时不要猜，先查 jar/source。
6. 供应商 API 的 URL、AK/SK、token、回调地址、超时、重试等属于现场参数，不算知识库缺口，必须参数化。
7. token/secret/sign/mobile/email/身份证/银行卡等敏感字段不得明文日志。

## 索取清单

```text
P0:
1. 通道 code / description
2. 供应商 API 或 SDK 文档
3. 平台能力配置参数字段
4. 目标 V8 / cip-capability-api 版本（若不是 5.5.147，需重新 FACT 化）

P1:
5. 已跑通示例实现或标品通道行为截图
6. 错误码映射规则
7. 超时、重试、幂等、回调策略
```

## 禁止项

- 禁止凭能力名猜 DTO 字段、方法签名或 `CapabilityEnum` 枚举名。
- 禁止把供应商 demo 里的业务 util 沉淀成通用能力通道约束。
- 禁止在 SPI 实现类使用 Spring stereotype/injection annotations。
- 禁止在 `spi-common` 注册本能力的 `spring.factories` 或 `spi_info.json`。
