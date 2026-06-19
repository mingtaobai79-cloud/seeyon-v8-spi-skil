# 能力通道共享规则

本目录只放跨 28 项能力通用的标准方法，不存放每个版本的全量反编译总账。

## 标准方法

1. 先定位具体能力文件夹，例如 `sms/`、`pay/`、`ocr/`。
2. 读取该能力 `README.md` + `constraints.md`。
3. 如果用户提供实际 jar/source 或指定版本，先抽取该版本 FACT：
   - 接口 FQCN
   - 方法签名
   - DTO 字段
   - `CapabilityEnum` 枚举值
   - required/default 方法
4. 只把稳定结论回填到对应能力文件夹；临时反编译输出不进入 active skill。
5. 不为每个版本长期保存 `contract-facts-*` 总账，避免 skill 膨胀。

## 公共约束

- `getChannelCode()` 必须稳定、唯一，不能返回空。
- `getDescription()` 面向平台能力配置页面可读，不能写测试占位。
- `getCapabilityEnum()` 必须使用目标 jar 中真实存在的枚举值，不能猜。
- required 方法必须实现；default 方法只在业务明确要求时覆盖。
- 供应商 URL、AK/SK、token、回调地址、超时、重试等现场参数必须参数化。
- token/secret/sign/mobile/email/身份证/银行卡等敏感字段不得明文日志。
- 禁止在 SPI 实现类使用 Spring stereotype/injection annotations。
- 禁止在 `spi-common` 注册具体能力的 `spring.factories` 或 `spi_info.json`。
