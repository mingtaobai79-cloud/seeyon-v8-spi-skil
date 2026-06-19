# 移动插件 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 域特有规则

1. 7 个接口按需选择实现，不需要全部实现。
2. 所有接口继承 `MobileProviderService`（标记接口，无方法）。
3. `MobileConfigProviderService` 是基础配置接口，通常必须实现。
4. `isPrivateApp()` SPI 方式固定返回 true。
5. 与 auth-sso/mobile-app 域覆盖相同接口，不要重复开发。

## 禁止项

- 禁止与 auth-sso/mobile-app 重复注册同一个 spring.factories key。
- 禁止使用 `@Autowired`、`@Service` 等 Spring 注解。

## 索取清单

```
P0:
1. ✅ MobileConfigProviderService FQCN + 完整接口（FACT）
2. ✅ MobileApplicationProviderService FQCN（FACT）
3. ✅ MobileOrgSyncBatchProviderService FQCN + 完整接口（FACT）
4. ✅ MobileOrgSyncProviderService FQCN + 完整接口（FACT）
5. ✅ MobileOrgSyncPullProviderService FQCN + 完整接口（FACT）
6. ✅ MobileTodoProviderService FQCN + 完整接口（FACT）
7. ✅ MobileCallBackProviderService FQCN + 完整接口（FACT）

P1:
8. 企业微信/钉钉/飞书示例配置
9. 各 DTO 完整字段（MobilePlatformConfigDto 等）
```
