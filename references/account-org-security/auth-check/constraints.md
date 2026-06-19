# 登录人数控制 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 域特有规则

1. 🧊 **冻结**：接口 FQCN 未确认，代码无法编译。
2. 抽象类（非接口），用 `extends` 而非 `implements`。
3. handleMaxOnlineUser 返回过滤后的用户列表。
4. 超过限制时抛出 MaxOnlineUserExceedException。

## 禁止项

- 禁止吞掉异常（必须抛出 MaxOnlineUserExceedException）。
- 禁止修改入参 List 结构（应返回新 List）。

## 索取清单

```
P0（阻塞）:
1. ❌ AbstractAuthenticationCheckService 完整包名 — 5.3.429 不存在
2. ❌ MaxOnlineUserExceedException 完整定义 — 5.3.429 不存在
3. ❌ BaseDto 完整字段 — 5.3.429 未找到

P1:
4. ✅ PasswordCheckService → com.seeyon.ctp.user.api.passwordCheck.PasswordCheckService（FACT）
5. 需要更高版本 jar 或独立 artifact
```
