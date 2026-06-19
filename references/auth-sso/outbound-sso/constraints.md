# 出站 SSO SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`
> 共享约束：与 sso-connector/ 共享类名规则。

## 与 sso-connector 的关系

outbound-sso 是旧版本机制下的 V8→三方单点，接口与 sso-connector 相同但部署方式不同。

## 索取清单

```
P0:
1. SsoService 完整反编译源码
2. spring.factories 注册示例

P1:
3. 示例实现类
4. cip-connector-api 版本
```

## 禁止项

- 禁止 `login()` 返回 null（必须返回有效跳转 URL）。
- 禁止在 `check()` 中吞掉异常。
- 禁止使用 `@Autowired`、`@Service` 等 Spring 注解。
