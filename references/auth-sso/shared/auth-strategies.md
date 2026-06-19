# Auth Strategies（认证策略定义）

> 不是案例库，是策略库。新增认证方式只需加策略，不改 Workflow。

## 策略结构

每个策略定义：
- `token_source`: token 从哪里来
- `token_transform`: token 如何变换（解密/验证/换取）
- `user_query`: 如何查询 V8 用户
- `dependencies`: 需要的额外依赖
- `nacos_keys`: 需要的 Nacos 配置项
- `code_pattern`: 核心代码模式

---

## oauth2 — OAuth2 授权码模式

```yaml
token_source: request_param  # 从 request.getParameter("code") 获取
token_transform: code_to_token  # code 换 access_token
user_query: rest_api  # 用 token 调三方 userinfo 接口
dependencies:
  - cn.hutool:hutool-all:5.8.28  # HTTP 调用
nacos_keys:
  - clientId
  - clientSecret
  - tokenUrl
  - userInfoUrl
```

**核心代码模式：**
```java
// 1. code 换 token
String tokenUrl = CtpUserSpiUtils.getPropertyByName("seeyon.{project_id}.tokenUrl");
String clientId = CtpUserSpiUtils.getPropertyByName("seeyon.{project_id}.clientId");
String clientSecret = CtpUserSpiUtils.getPropertyByName("seeyon.{project_id}.clientSecret");

Map<String, Object> params = new HashMap<>();
params.put("grant_type", "authorization_code");
params.put("code", code);
params.put("client_id", clientId);
params.put("client_secret", clientSecret);
params.put("redirect_uri", redirectUri);

String tokenResp = HttpUtil.post(tokenUrl, params);
String accessToken = JsonUtils.toMap(tokenResp).get("access_token").toString();

// 2. token 换用户信息
String userInfoUrl = CtpUserSpiUtils.getPropertyByName("seeyon.{project_id}.userInfoUrl");
String userResp = HttpUtil.createGet(userInfoUrl)
    .header("Authorization", "Bearer " + accessToken)
    .execute().body();
String thirdUserId = JsonUtils.toMap(userResp).get("{user_id_field}").toString();
```

---

## cas — CAS 票据认证

```yaml
token_source: request_param  # request.getParameter("ticket")
token_transform: cas_validate  # 调用 CAS 验证接口或 SDK
user_query: cas_response  # 从验证响应中提取用户标识
dependencies:
  - 三方 CAS SDK（优先 Maven 坐标；jar 文件放 root third-jar/ 暂存后 install/deploy）
nacos_keys:
  - casServerUrl
  - serviceUrl
```

**核心代码模式：**
```java
// 1. 获取 ticket
String ticket = request.getParameter("ticket");

// 2. 调用 CAS 验证（SDK 方式）
// 或 HTTP 方式：GET {casServerUrl}/serviceValidate?ticket={ticket}&service={serviceUrl}
String validateUrl = casServerUrl + "/serviceValidate?ticket=" + ticket + "&service=" + serviceUrl;
String xmlResp = HttpUtil.get(validateUrl);
// 解析 XML 获取用户名
String username = parseXml(xmlResp, "cas:user");
```

---

## sm2 — SM2 国密加密

```yaml
token_source: encrypted_param  # request.getParameter("code") 是 SM2 加密的
token_transform: sm2_decrypt  # 用私钥解密得到明文标识
user_query: metadata_api  # 通过元数据字段查询 V8 用户
dependencies:
  - com.seeyon:boot-starter-web（含 SM2Utils）
nacos_keys:
  - sm2PrivateKey
  - metadataCode
```

**核心代码模式：**
```java
// 1. 获取加密 code
String encryptedCode = request.getParameter("code");

// 2. SM2 解密
String privateKey = CtpUserSpiUtils.getPropertyByName("seeyon.{project_id}.sm2PrivateKey");
String realCode = SM2Utils.decrypt(privateKey, encryptedCode);

// 3. 通过元数据查询用户
String metadataCode = CtpUserSpiUtils.getPropertyByName("seeyon.{project_id}.metadataCode");
String memberId = openApiUtil.selectMemberIdByMetadataValue(metadataCode, realCode);
```

---

## rsa — RSA 公钥加密

```yaml
token_source: user_info_encrypt  # 用 RSA 加密用户信息拼接到 URL
token_transform: rsa_encrypt  # 公钥加密 → URLEncode
user_query: user_map  # 从 userMap 获取 V8 用户信息（模式 C）
dependencies:
  - 自定义 RSA 工具类
nacos_keys:
  - publicKey
```

**核心代码模式（模式 C）：**
```java
// 1. 从 userMap 获取用户
String loginName = (String) userMap.get("innerUserLoginName");
long timestamp = System.currentTimeMillis();

// 2. 构造 payload 并 RSA 加密
String payload = "{\"username\":\"" + loginName + "\",\"issueTime\":" + timestamp + "}";
String publicKey = Apps.getApplicationContext().getEnvironment().getProperty("seeyon.{project_id}.publicKey");
String encrypted = RSAEncrypt.encrypt(payload, publicKey);

// 3. URL 拼接
String ssoUrl = url + "&ssoToken=" + URLEncoder.encode(encrypted, "UTF-8");
```

---

## sm4 — SM4 国密对称加密

```yaml
token_source: encrypted_param  # request.getParameter("token") 是 SM4 加密的
token_transform: sm4_decrypt  # SM4/ECB/PKCS5Padding 解密得到明文标识
user_query: decrypted_value  # 解密后的值即为用户标识（如人员编号直接当 loginName）
dependencies:
  - org.bouncycastle:bcprov-jdk15on:1.70  # SM4 国密算法
nacos_keys:
  - sm4Key  # Hex 编码，32 字符 = 16 字节
```

**核心代码模式：**
```java
// 1. 获取加密 token
String encryptedToken = request.getParameter("token");

// 2. SM4 解密（BouncyCastle）
String sm4Key = CtpUserSpiUtils.getPropertyByName("seeyon.{project_id}.sm4Key");
byte[] keyBytes = hexToBytes(sm4Key);
byte[] encryptedBytes = Base64.getDecoder().decode(encryptedToken);

Security.addProvider(new BouncyCastleProvider());
SecretKeySpec keySpec = new SecretKeySpec(keyBytes, "SM4");
Cipher cipher = Cipher.getInstance("SM4/ECB/PKCS5Padding", "BC");
cipher.init(Cipher.DECRYPT_MODE, keySpec);
byte[] decryptedBytes = cipher.doFinal(encryptedBytes);
String staffCode = new String(decryptedBytes, StandardCharsets.UTF_8);

// 3. 解密结果直接作为用户标识（如人员编号 = loginName）
```

**注意事项：**
- SM4 是国密对称加密（类似 AES），不是 SM3（摘要/哈希）也不是 SM2（非对称）
- BouncyCastle Provider 必须在 static 块或首次调用时注册
- 密钥用 Hex 编码存储（32 字符 = 16 字节），不是 Base64
- 密文用 Base64 编码传输

---

## aes — AES 对称加密

```yaml
token_source: encrypted_param  # 加密的 token 参数
token_transform: aes_decrypt  # AES-CBC 解密
user_query: decrypted_value  # 解密后的值即为用户标识
dependencies:
  - cn.hutool:hutool-all:5.8.28（含 AES 工具）
nacos_keys:
  - aesKey
  - aesIv（可选，默认固定）
```

**核心代码模式：**
```java
// AES-CBC 解密
String key = CtpUserSpiUtils.getPropertyByName("seeyon.{project_id}.aesKey");
AES aes = new AES(Mode.CBC, Padding.PKCS5Padding,
    key.getBytes(StandardCharsets.UTF_8),
    AES_IV.getBytes(StandardCharsets.UTF_8));
String decrypted = aes.decryptStr(encryptedToken);
```

**V8 平台标准 AES 签名模式（模式 A 免登授权码）：**
```java
// 1. 参数自然排序
String[] arr = {clientId, clientSecret, data, timestamp};
Arrays.sort(arr);
String sorted = String.join("", arr);

// 2. SHA-256 签名
String sign = sha256(sorted);

// 3. AES 加密 data
String encryptedData = aes.encryptHex(data);

// 4. 调用获取授权码接口
// POST {V8域名}/service/ctp-user/auth/avoid/sytoken
```

---

## oidc — OpenID Connect

```yaml
token_source: request_param  # code 参数
token_transform: oidc_flow  # code → token → id_token → claims
user_query: id_token_claims  # 从 id_token 解析用户信息
dependencies:
  - cn.hutool:hutool-all:5.8.28
  - com.auth0:java-jwt:3.10.2（JWT 解析）
nacos_keys:
  - clientId
  - clientSecret
  - issuerUrl
  - jwksUri
```

**核心代码模式：**
```java
// 1. code 换 token（同 oauth2）
// 2. 解析 id_token
JWT jwt = JWT.decode(idToken);
String sub = jwt.getClaim("sub").asString();
String email = jwt.getClaim("email").asString();
// 3. 用 sub/email 匹配 V8 用户
```

---

## saml — SAML2

```yaml
token_source: post_body  # SAMLResponse 在 POST body 中
token_transform: saml_validate  # 解析 SAML Assertion
user_query: saml_nameid  # 从 NameID 获取用户标识
dependencies:
  - org.opensaml（或三方 SAML SDK）
nacos_keys:
  - idpMetadataUrl
  - spEntityId
  - certificate
```

**核心代码模式：**
```java
// 1. 获取 SAMLResponse
String samlResponse = request.getParameter("SAMLResponse");
// 2. Base64 解码 + XML 解析
// 3. 验证签名
// 4. 提取 NameID
String nameId = parseSamlAssertion(decodedXml);
```

---

## jwt — JSON Web Token

```yaml
token_source: request_param  # token 参数
token_transform: jwt_verify  # 验证签名 + 解析 claims
user_query: jwt_claims  # 从 claims 获取用户标识
dependencies:
  - com.auth0:java-jwt:3.10.2
nacos_keys:
  - jwtSecret（HMAC）或 jwtPublicKey（RSA）
```

**核心代码模式：**
```java
String token = request.getParameter("token");
String secret = CtpUserSpiUtils.getPropertyByName("seeyon.{project_id}.jwtSecret");
Algorithm algorithm = Algorithm.HMAC256(secret);
JWTVerifier verifier = JWT.require(algorithm).build();
DecodedJWT jwt = verifier.verify(token);
String userId = jwt.getClaim("sub").asString();
```

---

## ldap — LDAP/AD 域认证

```yaml
token_source: credentials  # 用户名 + 密码
token_transform: ldap_bind  # LDAP bind 验证
user_query: ldap_search  # LDAP search 获取用户属性
dependencies:
  - JDK 内置 javax.naming
nacos_keys:
  - ldapUrl
  - ldapBaseDn
  - ldapBindDn
  - ldapBindPassword
  - ldapUserFilter
```

**核心代码模式：**
```java
String ldapUrl = CtpUserSpiUtils.getPropertyByName("seeyon.{project_id}.ldapUrl");
String baseDn = CtpUserSpiUtils.getPropertyByName("seeyon.{project_id}.ldapBaseDn");

Hashtable<String, String> env = new Hashtable<>();
env.put(Context.INITIAL_CONTEXT_FACTORY, "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, ldapUrl);
env.put(Context.SECURITY_AUTHENTICATION, "simple");
env.put(Context.SECURITY_PRINCIPAL, userDn);  // cn=username,ou=users,dc=example,dc=com
env.put(Context.SECURITY_CREDENTIALS, password);

DirContext ctx = new InitialDirContext(env, null);  // bind 成功即验证通过
// search 获取用户属性
```

---

## custom_token — 自定义 Token 签名验证

```yaml
token_source: request_param  # 自定义参数名
token_transform: signature_verify  # 验证签名（MD5/SHA256/HMAC）
user_query: token_payload  # 从 token payload 提取用户标识
dependencies:
  - cn.hutool:hutool-all:5.8.28
nacos_keys:
  - signKey
  - signAlgorithm（MD5/SHA256/HMAC-SHA256）
```

**核心代码模式：**
```java
String token = request.getParameter("token");
String timestamp = request.getParameter("timestamp");
String sign = request.getParameter("sign");
String signKey = CtpUserSpiUtils.getPropertyByName("seeyon.{project_id}.signKey");

// 验证签名
String expectedSign = SecureUtil.sha256(token + timestamp + signKey);
if (!expectedSign.equals(sign)) {
    throw new CtpUserSpiSsoException("签名验证失败");
}

// 验证时间戳（防重放，5分钟有效）
long ts = Long.parseLong(timestamp);
if (Math.abs(System.currentTimeMillis() - ts) > 300000) {
    throw new CtpUserSpiSsoException("请求已过期");
}

// token 即为用户标识（或解密后得到）
String userId = token;
```

---

## 策略选择决策树

```
用户提到 OAuth2 / 授权码 / code 换 token？ → oauth2
用户提到 CAS / ticket / 票据验证？ → cas
用户提到 SM2 / 国密非对称？ → sm2
用户提到 SM4 / 国密对称？ → sm4
用户提到 RSA / 公钥？ → rsa
用户提到 AES / 对称加密？ → aes
用户提到 OIDC / OpenID？ → oidc
用户提到 SAML / SAML2？ → saml
用户提到 JWT / JSON Web Token？ → jwt
用户提到 LDAP / AD / 域账号？ → ldap
用户提到 签名 / sign / HMAC？ → custom_token
都不匹配？ → 追问认证协议细节
```
