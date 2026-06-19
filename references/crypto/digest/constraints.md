# 散列加密 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 域特有规则

1. 🧊 **冻结**：接口 FQCN 未确认，代码无法编译。
2. 散列加密是不可逆的（单向）。
3. 支持范围：用户密码、工资条。
4. encrypt 方法返回加密后的字符串。

## 禁止项

- 禁止返回 null（应返回加密结果）。
- 禁止在加密方法中做数据库查询。

## 索取清单

```
P0（阻塞）:
1. ❌ boot-starter-encrypt artifact — 仓库中不存在
2. ❌ DigestSpi 完整包名 — 无 jar 可反编译
3. ❌ spring.factories key — 无 jar 可确认

P1:
4. ✅ EncryptService → com.seeyon.boot.starter.security.service.EncryptService（FACT，内部服务非 SPI）
5. 需要 boot-starter-encrypt jar 或确认正确的 artifactId
```
