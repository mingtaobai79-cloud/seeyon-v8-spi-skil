# 案例污染 / 示例值污染清理清单

适用场景：用户指出某个 reference 文件“性质接近 header-code / 一次性案例 / 会让 agent 学成默认业务”，或要求把具体业务 type、示例域名、明文 secret 占位等具体示例值改成参数占位。

## 处理原则

1. 一次性案例文件优先删除或下沉为归一化 OBSERVATION，不作为默认加载源。
2. 保留可复用契约/实现规则，删除或改写会误导生成的“具体客户/业务样例”。
3. 具体业务值一律参数化：
   - 域名：`{v8_domain}` / `{v8_openapi_domain}`
   - 三方类型：`{third_type}` / `{channel_type}`
   - 凭据字段：`{credential_param_name}` / `{credential_value}`
   - 密钥：`CHANGE_ME_IN_NACOS`
   - URL：`{third_login_url}` / `{third_token_url}` / `{third_user_info_url}` / `{third_logout_url}`
4. `xxx` 不是安全占位；在模板里也会被 agent 学成默认形态。能命名的参数必须命名，敏感值用 `CHANGE_ME_IN_NACOS`。
5. 示例依赖版本、旧工程路径、`.flattened-pom.xml` 等只可作为观察，不得升级为平台标准。

## 操作步骤

1. 定位污染源：先搜用户点名文件，再搜同类 token。
2. 对一次性样例文件：
   - 删除独立文件，或把可复用内容并入目标 README 的“归一化实现观察”。
   - 更新所有引用，避免断链或让 future agent 继续主动读取已删除案例。
3. 对 auth-sso / URL / Nacos 示例：
   - URL 改成参数化格式，不保留真实域名、客户 type、真实 code/ticket 值。
   - YAML 中 `clientId/appKey/domain/loginUrl/tokenUrl/userInfoUrl/logoutUrl/publicKey` 全部参数化。
   - `clientSecret/appSecret` 等敏感项用 `CHANGE_ME_IN_NACOS`。
4. 复扫验证：
   - 搜污染 token：文件名、业务名、域名、明文 secret 占位、未命名 `xxx` 占位、业务列表值等。
   - 扫 markdown 断链。
   - 确认删除文件不存在。
5. 若补丁未命中但扫描仍有残留，不要相信旧快照；重新读目标行，用更精确的实际字符串 patch。常见原因：示例 `code=***` 实际已被写成真实数字。

## 验收口径

报告只给结果：

- P0/P1 已处理项
- 残留 token 命中数均为 0
- markdown 断链数为 0
- 删除文件存在性为 False
- 最终 `VERIFY OK`

不要把“具体业务参数缺失”报成知识库缺口；这些是生成时由现场填写的运行时配置。
