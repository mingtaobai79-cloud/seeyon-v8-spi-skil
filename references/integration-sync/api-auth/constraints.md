# 集成接口鉴权 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 域特有规则

1. **认证模式选择**：根据实际场景选择 `AuthInfoModeEnum`：
   - `ANONYMOUS(0)`：匿名模式，无需认证
   - `TENANT(1)`：租户模式，租户级认证
   - `USER(2)`：用户模式，用户级认证

2. **配置 JSON 结构**：`getPageJson()` 返回的 JSON 必须符合前端组件规范，字段包括：
   - `name`：字段名（对应 `AuthenticationDto.json` 中的 key）
   - `label`：显示标签
   - `type`：输入类型（input/password/select 等）
   - `required`：是否必填

3. **认证结果 Map**：`doAuthentication()` 返回的 Map 可包含：
   - `access_token`：访问令牌
   - `header_*`：需要添加到请求头的参数（如 `header_Authorization`）
   - `query_*`：需要添加到查询参数的参数
   - `body_*`：需要添加到请求体的参数

4. **回调解密**：`doDecode()` 用于处理三方回调时的认证信息解密，需根据三方协议实现。

5. **异常处理**：认证失败时必须抛出异常，不能返回空 Map 或 null。

## 禁止项

- 禁止在 `doAuthentication()` 中硬编码 clientId/clientSecret，必须从配置 JSON 读取。
- 禁止在日志中明文打印 clientSecret、access_token 等敏感信息。
- 禁止绕过 `jsonCheck()` 直接信任前端传入的配置 JSON。

## 索取清单

```
P0:
1. LinkerSecurityService 完整反编译源码 ✅ 已有
2. AuthenticationDto / AuthEventDto / AuthInfoModeEnum ✅ 已有
3. spring.factories 注册示例 ✅ 已有

P1:
4. 示例 SecurityServiceImpl 完整源码（如有；只作为 OBSERVATION，不作为通用约束）
5. 页面参数配置截图（语雀有图但看不到）
6. cip-connector-api 版本确认
```
