# 入站 SSO SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`
> 共享约束：与 avoid-login/ 共享免登 DTO 五字段唯一规则、ClientMode DTO 字段映射、免登地址格式。

## 与 avoid-login 的关系

inbound-sso 是旧版本机制下的三方→V8 免登，接口与 avoid-login 相同但部署方式不同（旧 SPI 走 `seeyon.spi.spi-plugins`）。

## 索取清单

```
P0:
1. CtpAvoidLoginMiddlePageProviderService / CtpAvoidLoginClientModeProviderService / CtpAvoidLoginBackendProviderService 完整反编译源码
2. 相关 DTO 完整反编译源码
3. spring.factories 注册示例

P1:
4. 示例实现类
5. Nacos seeyon.spi.spi-plugins 配置示例
6. ctp-user-api 版本
```

## 禁止项

- 禁止 `getClientId()` 返回空或与 Nacos 配置不匹配。
- 禁止在免登失败时不抛异常（平台依赖异常展示错误页面）。
- 禁止使用 `@Autowired`、`@Service` 等 Spring 注解。
