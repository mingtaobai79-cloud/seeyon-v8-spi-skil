# 移动应用 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## MobileCallBackProviderService 泛型边界

```java
MobileCallBackProviderService<T extends BaseDto, Res>
```

- 可生成保守模板：`implements MobileCallBackProviderService<BaseDto, Object>`。
- 必须用 `@ConnectorChannelRouter("CUSTOM_APP")` 或可配置常量。
- 真实项目要按具体回调 DTO/Res 收窄泛型。
- `@ConnectorChannelRouter` 的值必须等于回调请求地址中的 type 值。

## 索取清单

```
P0:
1. 7 个 Mobile*ProviderService 完整反编译源码 ✅ 已有
   - 来源：cip-connector-api-5.3.286.jar
   - 对齐：README.md §接口清单 / 方法表，entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md
2. 相关 DTO 完整反编译源码 ✅ 已有（按 README.md 方法表引用）
3. spring.factories 注册示例 ✅ 已有（README.md §spring.factories）

P1:
4. 企业微信/钉钉/飞书示例配置（业务实现示例；非 FACT 化阻塞）
5. 回调事件类型枚举（按具体三方 App 类型补充；非通用 SPI 契约缺口）
6. cip-connector-api 版本 ✅ 已确认：5.3.286
```

## 域特有规则

1. 7 个接口按需选择实现，不需要全部实现。
2. 与 entry-menu-mobile/mobile-plugin 域覆盖相同接口，不要重复开发。
3. 如果 auth-sso-spi-parent 已有 spi-06~12 模块，优先复用。

## 禁止项

- 禁止与 entry-menu-mobile/mobile-plugin 重复注册同一个 spring.factories key。
- 禁止使用 `@Autowired`、`@Service` 等 Spring 注解。
