# 免登 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 免登 DTO 五字段唯一规则

`CtpAvoidLoginUserInfoDto` 的五个用户标识字段，有且只有一个赋值：

| 外部用户标识 | 字段 |
|--------------|------|
| 人员编号 / 工号 | `thirdUserCode` |
| 三方系统内部 ID | `thirdUserId` |
| 手机号 | `thirdMobile` |
| 登录名 / 账号 | `thirdLoginName` |
| 邮箱 | `thirdUserEmail` |

模板里必须提供 `UserIdentityGuard` 或等价校验，测试里必须覆盖"有且只有一个"。

## ClientMode DTO 字段映射

`CtpUserSpiAvoidLoginClientModeDto` 不能闲置字段：

| DTO 字段 | URL 参数 | 语义 |
|----------|----------|------|
| `thirdType` | `c` | 三方标识 |
| `timestamp` | `t` | 时间戳 |
| `sign` | `s` | 签名 |
| `webUrl` | `w` | PC 端跳转 |
| `mobileUrl` | `m` | 移动端跳转 |
| `encryptData` | `d` | 加密数据 |
| `extData` | — | 扩展参数 Map |

## 免登地址格式

### 新版（优先）

```text
{V8域名}/oauth/home?
  mobile={urlEncode(移动端重定向地址)}
  &web={urlEncode(Web端重定向地址)}
  &businessType=outsider
  &type={三方系统sso标识}
  &dynamicField={凭据参数名}
  &{凭据参数名}={三方追加的凭据值}
```

### 旧版（仅在现场明确使用时采用）

```text
{V8域名}/seeyon/reportLogin.do?sytype={third_type}&syid={标识}&{自定义参数}
```

## 多账号 SSO

通过免登地址登录 A 账号查看待办后再打开 B 账号待办，默认不会切换账号。Web 端需要在 Nacos 的 `ctp-user` 微服务下添加配置：

```yaml
seeyon:
  avoid:
    clearCookieTypes:
      - {type_a}
      - {type_b}
```

## 生成器规则

1. 免登生成不是为某一个业务写死代码，而是生成可复用模板。
2. `getClientId()` / URL `type`：使用参数占位（如 `{third_type}`），不要写具体业务值，集中成常量或 Nacos 配置。
3. code 到用户标识的转换：生成默认策略链（DIRECT / HTTP_EXCHANGE / AES / SM2 / SM4 / RSA / JWT / SIGNATURE）。
4. V8 用户匹配字段：生成成配置项，默认 `thirdUserCode`。
5. web/mobile redirect：从 URL 的 `web` / `mobile` 获取并 URL decode；默认只允许站内路径。
6. 缺业务信息不阻塞模板生成；在报告里列为"业务待填配置"。

## 索取清单

```
P0:
1. CtpAvoidLoginMiddlePageProviderService / CtpAvoidLoginClientModeProviderService 完整反编译源码
2. CtpAvoidLoginUserInfoDto / CtpUserSpiAvoidLoginClientModeDto 字段
3. spring.factories 注册示例

P1:
4. 示例实现类
5. Nacos 配置 key 和示例值
6. ctp-user-api 版本
```

## 禁止项

- 禁止 `getClientId()` 返回空或与 Nacos `seeyon.thirdauth.type` 不匹配。
- 禁止在 `getUserInfo` 中返回 null 且不设置重定向（会导致登录白屏）。
- 禁止同时赋值多个用户标识字段。
- 禁止使用 `@Autowired`、`@Service` 等 Spring 注解。
