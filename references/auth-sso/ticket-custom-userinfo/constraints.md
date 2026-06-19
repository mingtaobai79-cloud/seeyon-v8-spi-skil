# 票据自定义用户信息 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## ticket map 默认行为

`CustomUserInfoService.filterCustomUserInfo(Map<String, Object> map)` 默认 `return map;`。
不猜字段，不瞎写包装逻辑。现场给字段后再补包装/脱敏/增强。

## 索取清单

```
P0:
1. CustomUserInfoService 完整反编译源码
2. spring.factories 注册示例

P1:
3. ticket 认证返回 map 真实样例字段
4. ctp-user-api 版本
```

## 域特有规则

1. `filterCustomUserInfo` 接收 Map，返回修改后的 Map。
2. 可以添加/修改/删除 ticket 中的人员信息字段。

## 禁止项

- 禁止返回 null（应返回修改后的 Map）。
- 禁止删除核心字段（如 loginName/userId）导致下游系统异常。
- 禁止使用 `@Autowired`、`@Service` 等 Spring 注解。
