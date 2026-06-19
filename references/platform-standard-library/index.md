# Platform Standard Library Index（平台标准库索引）

> 目的：生成 Seeyon V8 Super SPI 工程时，先复用平台 boot 公共能力，再考虑本工程 `spi-common` adapter，避免重复造 JSON/HTTP/加密/BeanCopy/Response 等基础轮子，也避免默认引入 Hutool / Guava / Jackson / Fastjson / BouncyCastle 等冲突依赖。
>
> 边界校正：本索引只抽取“平台通用基础能力”。`ctp-user-api` 这类 SPI 子域契约包不在本索引抽取范围内；它属于对应子域 contract index / 子模块依赖。生成 SSO/用户类 SPI 时可以按子域引用它，但不要把它当作平台公共库方法来源。

## 1. 当前 FACT 来源

| 项 | 结果 |
|---|---|
| boot jar 版本 | `5.3.358` |
| 已验证 jar | 用户提供的本地 Maven 仓库 artifact：`${LOCAL_MAVEN_REPO}/com/seeyon/boot-core/5.3.358/boot-core-5.3.358.jar`；`${LOCAL_MAVEN_REPO}/com/seeyon/boot-starter-web/5.3.358/boot-starter-web-5.3.358.jar`；`${LOCAL_MAVEN_REPO}/com/seeyon/boot-starter-spi/5.3.358/boot-starter-spi-5.3.358.jar` |
| 抽取方式 | CFR targeted decompile：只反编译目标 class，不整包反编译 |
| 反编译缓存 | `references/platform-standard-library/decompiled/` |
| 证据等级 | 本文件中标记 `FACT(jar:5.3.358)` 的签名可直接作为生成依据；未列出的语雀/样例仍是 OBSERVATION，不可硬写 |

## 1.1 初始化基线 / Version Fallback Policy

`decompiled/` 是平台 boot 公共能力的初始化基线。

生成 Super SPI 时按以下口径执行：

1. 用户提供目标 V8/boot 版本且能取得对应 jar：优先用现场版本 targeted probe / contract index。
2. 用户提供目标版本但本机找不到对应 boot 公共能力 jar：平台公共能力按 `5.3.358` baseline 生成；报告中标明 `BASELINE(boot:5.3.358)`，后续拿到现场 jar 后再补差异。
3. 用户没有提供版本：默认按 `5.3.358` baseline 初始化 Super SPI 工程；父 POM / starter / SPI 契约包版本仍保持参数化，不把 5.3.358 强行套给所有依赖。
4. baseline 只覆盖平台 boot 公共能力：JSON、HTTP、Crypto、Request/Environment、BeanCopy、Transport、SPI runtime。它不覆盖 `ctp-user-api`、`cip-connector-api`、`organization-api` 等子域 SPI 契约包。
5. 业务子域接口、DTO、spring.factories key、scope 仍必须走对应 domain contract；找不到时不能用 boot baseline 伪装成 FACT。

报告标记建议：

| Evidence | 用途 |
|---|---|
| `FACT(site-jar:<version>)` | 用户现场 jar/source 直接确认，可优先用于最终代码 |
| `BASELINE(boot:5.3.358)` | 现场 boot 版本未取得时，使用平台公共能力基线生成 |
| `FACT(jar:5.3.358)` | 5.3.358 jar 反编译确认的方法签名 |
| `OBSERVATION` / `HYPOTHESIS` | 仍不能锁死关键接口/DTO |

## 2. Artifact 分工

| Artifact | 用途判断 | Evidence | 生成规则 |
|---|---|---|---|
| `boot-core` | 平台核心公共能力：JSON、HTTP、加解密、BeanCopy、RequestContext、Apps、Transport Response/Request、ID、异常 | FACT(jar:5.3.358) | 父 POM 平台通用依赖候选；生成基础代码优先查这里 |
| `boot-starter-web` | Web 请求上下文、client ip、controller 基类、web util、mask JSON | FACT(jar:5.3.358) | 只有 SPI 需要 Web/request/response 能力时引用；不要为了普通 SPI 强行引入 |
| `boot-starter-spi` | SPI 插件加载/配置/runtime，不是业务工具库 | FACT(jar:5.3.358) | 用于 Super SPI 工程运行结构；不要从这里找 JSON/HTTP/加密方法 |
| `ctp-user-api` 等子域契约包 | 用户/SSO 子域 SPI 契约 | OUT_OF_SCOPE | 子域模块按需依赖；不纳入平台标准库索引 |

## 3. 生成时优先复用的 FACT 方法

### 3.1 JSON：`com.seeyon.boot.util.JsonUtils`（boot-core）

| 方法签名 | 用途 | 生成规则 |
|---|---|---|
| `String toJson(Object object)` | 序列化 | 优先于新增 Jackson/Fastjson |
| `String toJson(Object object, boolean longToString)` | 序列化，可控制 long 转 string | 前端精度敏感场景用 |
| `String toJsonLongToString(Object object)` | long 转 string 序列化 | ID/大整数输出优先 |
| `String toJsonDecimalToString(Object object)` | decimal 转 string 序列化 | 金额/高精度输出优先 |
| `String toJsonNotIncludeNull(Object object)` | 忽略 null 序列化 | 只在接口要求忽略 null 时用 |
| `<T> T fromJson(String jsonString, Class<T> clazz)` | 反序列化对象 | 优先于 ObjectMapper 直用 |
| `<T> T fromJson(String jsonString, Class<T> clazz, Class generalClazz)` | 泛型反序列化 | List/Map 包装类型场景可用 |
| `<K,V> Map<K,V> toMap(String jsonString, Class<K> keyClass, Class<V> valueClass)` | JSON 转 typed map | 配置/第三方响应解析优先 |
| `Map<String,Object> toMap(String jsonString)` | JSON 转 map | 轻量解析优先 |
| `List<T> toList(String jsonString, Class<T> clazz)` | JSON 转 typed list | 列表解析优先 |
| `List toList(String jsonString)` | JSON 转 raw list | 无 DTO 时临时用，最终代码尽量 typed |

### 3.2 HTTP：`com.seeyon.boot.util.http.HttpClientUtil` / `HttpConfig` / `HttpHeader`（boot-core）

| 方法签名 | 用途 | 生成规则 |
|---|---|---|
| `String get(String urlString)` / `<T> T get(String urlString, Class<T> clazz)` | GET | 第三方 GET 优先用 |
| `String get(String urlString, Map<String,Object> params, int timeout)` | GET + query + timeout | 外部调用必须显式 timeout |
| `String get(String urlString, HttpHeader headers, Map<String,Object> params)` | GET + header + params | 带 token/header 场景 |
| `String post(String urlString, Map<String,Object> paramMap)` | form post | 表单提交 |
| `String post(String urlString, String json)` | JSON post | 第三方 JSON 接口优先 |
| `String post(String urlString, String json, HttpHeader headers, int timeout, Charset customCharset)` | JSON post + header + timeout + charset | 生产外部调用优先使用完整重载 |
| `<T> T post(String urlString, String json, HttpHeader headers, Class<T> clazz)` | post 并反序列化 | 第三方响应 DTO 化 |
| `HttpResult sendGet(...)` / `HttpResult sendPost(...)` | 需要 status/header 的调用 | 不要只拿 String 时丢状态码 |
| `OutputStream down(...)` / `InputStream downForInputStream(HttpConfig config)` | 下载 | 文件流场景 |
| `String upload(...)` / `HttpResult uploadAndGetResp(...)` | 上传 | 文件上传场景 |
| `HttpResult put(HttpConfig config)` / `int status(HttpConfig config)` | PUT / 状态探测 | 复杂场景用 `HttpConfig.custom()` |
| `HttpHeader.custom().add(String headerName, String header)` | 构造 header | 不自造 header map 转换 |
| `HttpConfig.custom().url(...).headers(...).json(...).timeout(...)` | 复杂请求配置 | 外部接口复杂调用优先用 builder |

### 3.3 加密 / 摘要：`com.seeyon.boot.util.encrypt.*`（boot-core）

| 类 / 方法签名 | 用途 | 生成规则 |
|---|---|---|
| `SM4Utils.encrypt(String content, String key)` | SM4 加密 | 国密对称加密优先；不新增 BouncyCastle |
| `SM4Utils.decrypt(String cipher, String key)` | SM4 解密 | 同上 |
| `SM4Utils.encrypt(byte[] in, byte[] keyBytes)` / `decrypt(byte[] in, byte[] keyBytes)` | byte[] SM4 | 文件/二进制场景 |
| `SM3Utils.encrypt(String clearText)` | SM3 摘要 | 注意 SM3 是摘要，不是可逆加密 |
| `SM3Utils.encrypt(String clearText, String key)` | 带 key 摘要 | 签名/验签按接口约定使用 |
| `SHA1Utils.encrypt(String clearText)` | SHA1 | 旧系统签名兼容 |
| `AESUtils.encrypt(String clearText, String key)` / `AESUtils.decrypt(String cipherText, String key)` | AES | 对方明确要求 AES 时用 |
| `RSAUtils.encrypt(String clearText, String publicKey)` / `RSAUtils.decrypt(String cipherText, String privateKey)` | RSA | 对方明确要求 RSA 时用 |
| `MD5Utils.md5(String src)` / `MD5.getMD5String(String content)` | MD5 | 旧系统签名兼容；新安全设计不要优先选 MD5 |

### 3.4 Bean / DTO 转换：`com.seeyon.boot.util.bean.*`（boot-core）

| 方法签名 | 用途 | 生成规则 |
|---|---|---|
| `BeanCopier.copy(Object from, Class<T> toClass, String... ignoreProperties)` | DTO 转换 | 优先于 Spring BeanUtils / MapStruct |
| `BeanCopier.copy(Object from, Object to, String... ignoreProperties)` | 拷贝到已有对象 | update/merge 场景 |
| `BeanCopier.copyList(Collection<T> from, Class<D> beanClass)` | 列表转换 | DTO list 转换优先 |
| `BeanCopier.copyPageData(PageData<T> from, Class<D> beanClass)` | 分页转换 | 平台 PageData 场景 |
| `BeanUtils.getFieldValue(Object data, String fieldName)` / `setFieldValue(...)` | 反射读写 | 只在动态字段必要时用，不要替代正常 getter/setter |

### 3.5 Transport / Response：`com.seeyon.boot.transport.*`（boot-core）

| 方法签名 | 用途 | 生成规则 |
|---|---|---|
| `SingleRequest.from(T dto)` / `getData()` | 单对象请求包装 | AppService / 内部服务调用优先 |
| `SingleResponse.from(T dto)` / `SingleResponse.ok()` | 单对象响应 | 不自建 `{success,data}` 响应 |
| `SingleResponse.getData().getContent()` | 取单对象内容 | 注意 `getData()` 返回 `SingleData<T>`，不是 T |
| `ListRequest.from(Map<String,Object> params)` / `addParam(...)` | 列表请求 | 不自造 query wrapper |
| `ListResponse.from(List<T> dtoList)` | 列表响应 | `getData().getContent()` 取 list |
| `PageRequest.from(PageInfo pageInfo, Map<String,Object> map)` | 分页请求 | 分页查询 |
| `PageData.from(PageInfo pageInfo, List<T> data)` | 分页数据 | PageResponse 输入 |
| `PageResponse.from(PageData<T> pageData)` | 分页响应 | 平台分页响应 |
| `BaseResponse.success()` / `failure()` / `processing()` | 响应状态判断 | 不要用 message/code 猜成功 |
| `BaseResponse.buildResponse(Exception e)` | 异常转响应 | 接口边界统一异常输出 |
| `BusinessException.message(String customMessage)` | 业务异常 | 需要平台业务异常时用 |

### 3.6 上下文 / 环境 / Bean：`com.seeyon.boot.context.*`（boot-core）

| 方法签名 | 用途 | 生成规则 |
|---|---|---|
| `RequestContext.get()` | 当前请求上下文 | 非 Web 直接 request 场景优先 |
| `RequestContext.get().getTenantId()` / `getUserId()` / `getLoginOrgId()` | 当前租户/用户/登录组织 | 不自造 ThreadLocal |
| `RequestContext.get().getTraceId()` / `getClientIp()` / `getUserAgent()` | trace/client 信息 | 日志/审计 |
| `Apps.getRequestContext()` | 获取 RequestContext | 等价候选；优先 `RequestContext.get()` 更直接 |
| `Apps.getApplicationContext()` / `Apps.getBeanFactory()` | Spring 容器/BeanFactory | SPI 中必须取 bean 时用；能构造注入就别乱取全局 bean |
| `Apps.getEnvironment()` / `EnvironmentHolder.get()` | Spring Environment | 配置读取 |
| `Apps.getAppName()` / `getAppCaption()` / `getAppVersion()` | 应用元信息 | 日志、标识、版本输出 |
| `SystemEnvironment.isProd()/isDev()/isLocal()/isTest()` | 环境判断 | 只用于环境分支，不要写死 profile 字符串 |

### 3.7 ID / 工具补充（boot-core）

| 方法签名 | 用途 | 生成规则 |
|---|---|---|
| `Ids.gidString()` / `Ids.gidLong()` | 全局 ID | commandId/requestId/businessId 优先 |
| `Ids.uuidString()` / `uuidLong()` | UUID | 外部系统要求 UUID 时用 |
| `StringUtils.isBlankDefault(T text, T defaultValue)` | blank 默认值 | 简单默认值场景 |
| `StringUtils.equals(String val1, String val2)` | 字符串比较 | null-safe equals |
| `StringUtils.maskMobileNo/maskEmail/maskIdCardNo/maskBankCardNo` | 脱敏 | 日志/展示脱敏优先 |
| `StringUtils.escapeJson/unescapeJson` | JSON 字符转义 | 特殊拼接兜底；正常场景仍用 JsonUtils |

### 3.8 Web request：`boot-starter-web`

| 类 / 方法签名 | 用途 | 生成规则 |
|---|---|---|
| `HttpServletRequestContext.getRequest()` / `getResponse()` | 当前 Servlet request/response | 只有确需 Servlet 对象时用 |
| `WebUtils.getClientIp(HttpServletRequest request)` | 获取客户端 IP | Web 审计/日志 |
| `WebUtils.checkETag(...)` / `writeETag(...)` | ETag | 下载/缓存接口 |
| `BaseController.getUserId()` / `getLoginOrgId()` / `getClientType()` / `getCookie(String)` | Controller 便捷能力 | 只有生成 Controller 时继承/参考 |
| `MaskableDto.addMaskType(String fieldName, MaskType maskType)` | JSON 字段脱敏 | 输出 DTO 动态脱敏场景 |

## 4. boot-starter-spi FACT 结论

`boot-starter-spi` 主要是 SPI runtime/plugin loader，不是公共业务工具库。

| 类 / 方法签名 | 用途 | 生成规则 |
|---|---|---|
| `SPIProperties.isEnable()` / `getSpiPlugins()` | SPI 开关与插件列表 | 运行配置识别，不生成业务调用 |
| `ArtifactInfo.getGroupId()/getArtifactId()/getVersion()/isSnapshot()` | 插件 artifact 元信息 | 生成/发布工具可参考 |
| `SpiMavenProperties.getSnapshotUrl()/getReleaseUrl()/getUsername()/getPassword()` | SPI Maven 仓库配置 | 发布/下载插件时参考 |

## 5. allowlist / denylist

### 5.1 allowlist（FACT，可优先复用）

```text
com.seeyon.boot.context.Apps
com.seeyon.boot.context.RequestContext
com.seeyon.boot.context.EnvironmentHolder
com.seeyon.boot.context.SystemEnvironment
com.seeyon.boot.transport.SingleRequest
com.seeyon.boot.transport.ListRequest
com.seeyon.boot.transport.PageRequest
com.seeyon.boot.transport.SingleResponse
com.seeyon.boot.transport.ListResponse
com.seeyon.boot.transport.PageResponse
com.seeyon.boot.transport.PageData
com.seeyon.boot.transport.PageInfo
com.seeyon.boot.transport.Sort
com.seeyon.boot.transport.BaseResponse
com.seeyon.boot.util.JsonUtils
com.seeyon.boot.util.StringUtils
com.seeyon.boot.util.http.HttpClientUtil
com.seeyon.boot.util.http.common.HttpConfig
com.seeyon.boot.util.http.common.HttpHeader
com.seeyon.boot.util.http.common.HttpResult
com.seeyon.boot.util.bean.BeanCopier
com.seeyon.boot.util.bean.BeanUtils
com.seeyon.boot.util.encrypt.SM4Utils
com.seeyon.boot.util.encrypt.SM3Utils
com.seeyon.boot.util.encrypt.SHA1Utils
com.seeyon.boot.util.encrypt.AESUtils
com.seeyon.boot.util.encrypt.RSAUtils
com.seeyon.boot.util.encrypt.MD5Utils
com.seeyon.boot.util.id.Ids
com.seeyon.boot.exception.BusinessException
com.seeyon.boot.starter.web.servlet.HttpServletRequestContext
com.seeyon.boot.starter.web.util.WebUtils
```

### 5.2 denylist（默认不要生成/引入）

```text
com.seeyon.ctp.user.*     # 子域契约，不是平台公共库；只在 SSO/user 子域 SPI 中按 contract 引入
cn.hutool.*               # 文档里可能有现场样例，但全局生成不默认套
com.google.common.*       # Guava 版本冲突风险
com.alibaba.fastjson.*    # Fastjson 版本/安全风险；优先 JsonUtils
com.fasterxml.jackson.*   # 平台已有 JsonUtils；除非目标工程已有且必须定制
org.bouncycastle.*        # 平台已有 SM/AES/RSA 工具前不新增
org.springframework.beans.BeanUtils  # 有平台 BeanCopier 时优先查平台
```

## 6. 生成器规则（强制）

1. 生成 `spi-common` 前先查本索引：能用 boot 平台标准库就不要自造。
2. `ctp-user-api`、`organization-api` 等只作为子域 SPI 契约依赖，不作为“通用平台能力”抽取目标。
3. 对外 HTTP、JSON 转换、加解密/摘要、DTO copy、平台响应包装，优先使用本文件 FACT allowlist。
4. 父 POM 放平台通用依赖/公共运行时能力；子 SPI 模块只放对应 SPI 契约包和 `spi-common`。
5. 平台 boot parent 版本、平台 starter 版本、SPI 契约包版本分别参数化，不互相套版本。当前 FACT 只证明 boot 系列 `5.3.358`。
6. 未经 FACT 的平台方法不要散落业务代码；必须加 adapter/wrapper 隔离，并在 `VALIDATION.md` 标注待验证。
7. 生成代码时优先输出 import + exact method signature 来源注释（如 `// FACT: boot-core 5.3.358 JsonUtils#fromJson`），方便后续升级核对。
