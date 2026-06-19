# SSO 连接器 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 类名规则

无注解，类名必须等于 `getName() + "SsoServiceImpl"`。`getName()` 返回英文唯一标识。

## 索取清单

```
P0:
1. ✅ SsoService 完整反编译源码 → shared/cip-connector-api-contract.md §1.1
2. ✅ SsoClientTypeEnum 枚举值 → shared/cip-connector-api-contract.md §1.2 (PC=0, PHONE=1)
3. ✅ spring.factories 注册示例 → key=com.seeyon.cip.connector.api.sso.SsoService（spi-05 已确认）

P1:
4. 示例实现类（auth-sso-spi-parent/spi-05-outbound-sso-service/ 已有骨架）
5. ✅ getPageJson 格式示例 → README.md 中已有完整 JSON 模板
6. cip-connector-api 版本 → 5.3.286（父 POM 声明），现场版本可能不同
```

## 禁止项

- 禁止 `getName()` 返回中文或含空格（全英文唯一标识）。
- 禁止类名不等于 `getName() + "SsoServiceImpl"`（平台靠类名匹配）。
- 禁止 `login()` 返回 null（必须返回有效跳转 URL）。
- 禁止在 `check()` 中吞掉异常（必须抛出 RuntimeException 说明校验失败原因）。
- 禁止使用 `@Autowired`、`@Service` 等 Spring 注解。
