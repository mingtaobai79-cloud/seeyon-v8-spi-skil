# 密码策略 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 域特有规则

1. 5.3.351 版本只有 `checkPasswordStrength` 一个方法，可直接实现。
2. `getMethodType()` 和 `customInitPassword()` 在 5.3.351 中不存在，需更高版本 jar 确认。
3. 一旦配置自定义密码规则，系统管理员配置的密码规则**不再生效**。
4. 一旦配置自定义初始化密码，不受初始化密码开关控制。

## 版本差异

| 方法 | 5.3.351 | 语雀文档版本 |
|------|---------|-------------|
| checkPasswordStrength | ✅ FACT | ✅ |
| getMethodType | ❌ 不存在 | OBSERVATION |
| customInitPassword | ❌ 不存在 | OBSERVATION |
| PasswordMethodTypeEnum | ❌ 不存在 | OBSERVATION |

## 禁止项

- 禁止在 checkPasswordStrength 中修改密码（只做校验）。
- 禁止在 customInitPassword 中返回 null（会导致密码为空）。
- 禁止在 5.3.351 版本中使用 getMethodType / customInitPassword（编译失败）。

## 索取清单

```
P0:
1. ✅ PasswordCheckService FQCN → com.seeyon.ctp.user.api.passwordCheck.PasswordCheckService（FACT）
2. ✅ checkPasswordStrength 签名 → Boolean checkPasswordStrength(String)（FACT）

P1（需更高版本 jar）:
3. PasswordMethodTypeEnum 完整枚举值
4. getMethodType / customInitPassword 方法签名确认
5. 现场 ctp-user-api 版本号
```
