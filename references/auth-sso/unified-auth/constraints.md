# 统一认证 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 路由注解

实现类必须加 `@CtpUserChannelRouter("{type}")`，值必须等于 Nacos `seeyon.thirdauth.type`。

## 登出注意

- 需要实现 `getEncodeLogoutRedirectUrl` 或 `thirdSsoLogout`，V8 才有退出按钮。
- `getEncodeLogoutRedirectUrl` 返回的登出地址需要和 `getSsoLoginUrl` 返回地址中的 `loginUrl` 搭配验证。

## 索取清单

```
P0:
1. ✅ CtpUserSsoAuthProviderService 完整反编译源码 → shared/ctp-user-api-contract.md §1.2
2. ✅ CtpUserSpiLoginUserInfoDto / CtpUserSpiUserDto 字段 → shared/ctp-user-api-contract.md §2.2/§2.7
3. ✅ spring.factories 注册示例 → spi-01 spring.factories (key=com.seeyon.ctp.user.api.sso.CtpUserSsoAuthProviderService)

P1:
4. ✅ 示例实现类 → auth-sso-spi-parent/spi-01-unified-auth-provider/
5. Nacos 配置 key 和示例值（现场确认）
6. ✅ ctp-user-api 版本 → 5.3.351（jar 反编译），现场版本可能不同
```

## 域特有规则

1. 实现类必须加 `@CtpUserChannelRouter("{type}")`，值必须等于 Nacos `seeyon.thirdauth.type`。
2. 三个必须实现的方法：`getRequestParaKey`、`getSsoLoginUrl`、`getUserLoginInfo`。
3. 其余方法都有 default 实现，按需 override。
4. `getUserLoginInfo` 返回的 `CtpUserSpiLoginUserInfoDto` 中，5 个用户标识字段有且只有一个赋值即可。

## 禁止项

- 禁止在 `getUserLoginInfo` 中返回 null（应抛 `CtpUserSpiSsoException`）。
- 禁止吞掉 `CtpUserSpiSsoException`（平台依赖此异常展示错误页面）。
- 禁止同时赋值多个用户标识字段（thirdUserId/thirdUserCode/thirdMobile/thirdLoginName/thirdUserEmail）。
- 禁止使用 `@Autowired`、`@Service` 等 Spring 注解。
