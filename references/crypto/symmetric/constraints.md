# 对称加密 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 域特有规则

1. 🧊 **冻结**：接口 FQCN 未确认，代码无法编译。
2. 对称加密是可逆的（双向）。
3. 支持范围：实体字段上标注了加密注解的。
4. encrypt 和 decrypt 必须配对（加密后能正确解密）。

## 禁止项

- 禁止 encrypt/decrypt 返回 null。
- 禁止在加密/解密方法中做数据库查询。
- 禁止硬编码密钥（应从配置或密钥管理服务获取）。

## 索取清单

```
P0（阻塞）:
1. ❌ boot-starter-encrypt artifact — 仓库中不存在
2. ❌ SymmetricSpi 完整包名 — 无 jar 可反编译
3. ❌ spring.factories key — 无 jar 可确认

P1:
4. ✅ EncryptService → com.seeyon.boot.starter.security.service.EncryptService（FACT，内部服务非 SPI）
5. 需要 boot-starter-encrypt jar 或确认正确的 artifactId
```
