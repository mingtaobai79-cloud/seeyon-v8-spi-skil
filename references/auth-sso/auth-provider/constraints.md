# 登录扩展 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 域特有规则

1. 抽象类（非接口），用 `extends` 而非 `implements`。
2. 7 个抽象方法全部必须实现。
3. `supports()` 决定该 Provider 是否处理当前 Authentication 类型。
4. `retrieveUser()` 是核心方法，负责从认证请求中提取用户信息。
5. 认证流程：preCheck → retrieveUser → additionalChecks → postCheck → createSuccess。

## 禁止项

- 禁止在 retrieveUser 中直接返回 null（应抛出认证异常）。
- 禁止跳过 preAuthenticationCheck（安全检查）。

## 索取清单

```
P0:
1. ✅ AbstractAuthenticationProvider FQCN → com.seeyon.ctp.user.security.authentication.provider.AbstractAuthenticationProvider（FACT）
2. ✅ Authentication → com.seeyon.ctp.user.security.authentication.Authentication（FACT）
3. ✅ AbstractAuthenticationToken → com.seeyon.ctp.user.security.authentication.AbstractAuthenticationToken（FACT）

P1:
4. spring.factories key 确认
5. 示例实现类
```
