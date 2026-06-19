# V8 OpenAPI 平台契约

> **Evidence: FACT ✅** — 来源：致远 V8 官方开放 API 文档（2026-06-12 版本）
> 
> Base URL = 环境配置（从 Nacos 获取）
> Path = 平台契约（固定不变）

## 1. 通用调用规范

### 1.1 请求方式

所有 OpenAPI 均为 **POST** 请求，Content-Type: application/json。

### 1.2 请求头

| Header | 必填 | 说明 |
|--------|------|------|
| app-key | true | 分配给应用的 AppKey |
| sign-type | true | 固定值：MD5 |
| sign | true | 签名 = MD5(AppSecret + 请求body的JSON串 + AppSecret)，忽略大小写 |

### 1.3 请求体结构

```json
{
    "requestId": "唯一流水号，最长32位",
    "timestamp": 1234567890123,
    "data": { ... }
}
```

| 字段 | 必填 | 类型 | 说明 |
|------|------|------|------|
| requestId | true | string | 请求流水号，同一流水号重复请求返回上次结果，最长32位 |
| timestamp | true | int64 | 请求时间戳，与服务器时间差不超过5分钟 |
| notifyUrl | false | string | 异步回调URL，非空时使用异步模式 |
| data | true | object | 业务参数 |

### 1.4 响应体结构

```json
{
    "data": {
        "content": ...
    },
    "status": 0,
    "code": "BOOT_0000",
    "message": "success",
    "traceId": "xxx"
}
```

| 字段 | 说明 |
|------|------|
| status | 0=成功，-1=异步处理中，其他=出错 |
| code | BOOT_0000=成功 |
| message | 错误信息 |
| data.content | 业务返回数据 |

### 1.5 签名算法

```java
String signStr = appSecret + bodyJsonStr + appSecret;
String sign = md5(signStr).toLowerCase();
```

**⚠️ 关键约束：** 实际请求的 body 和计算 MD5 的 body 必须严格一致。JSON 中字段顺序、空格都会影响 MD5 值。

### 1.6 SDK 方式（推荐）

```xml
<dependency>
    <groupId>com.seeyon</groupId>
    <artifactId>openapi-sdk</artifactId>
    <version>最新版本</version>
</dependency>
```

```java
OpenApiClient client = new OpenApiClient(url + api, appKey, secretKey);
ApiSingleRequest request = new ApiSingleRequest();
request.setRequestId("abc" + System.currentTimeMillis());
request.setTimestamp(System.currentTimeMillis());
request.setData(dataMap);
ApiSingleResponse response = client.send(request);
```

---

## 2. SSO 相关 API 注册表

### API-ORG-001: 根据人员编码查询人员详情

```yaml
id: API-ORG-001
path: /organization/member/code
method: POST
evidence: FACT
source: 开放API文档-组织模型.docx §2.1.6
purpose: 通过三方用户编号（code）查询 V8 用户信息
```

**请求参数（data）：**

| 字段 | 必填 | 类型 | 说明 |
|------|------|------|------|
| codes | true | array[string] | 人员编码列表 |
| includeDisable | false | boolean | 是否包含失效人员，默认不包含 |
| useThirdId | false | boolean | 是否根据 thirdId 查询 |
| thirdIds | false | array[string] | 人员 thirdId（useThirdId=true 时使用） |

**响应（data.content）：**

```json
[{
    "thirdId": "第三方唯一标识",
    "name": "姓名",
    "code": "编号",
    "username": "用户名（登录名）",
    "gender": "MALE/FEMALE/UN_KNOW",
    "birthday": "出生日期",
    "phoneNumber": "手机号码",
    "officePhone": "办公电话",
    "email": "邮箱",
    "certificateNumber": "证件号码",
    "isEnable": true,
    "id": 12345
}]
```

**SSO 用途：** 三方系统传用户编号 → 查 V8 用户 → 取 username 作为 loginName

---

### API-ORG-002: 条件查询人员列表

```yaml
id: API-ORG-002
path: /organization/base/member/selectMemberListByCondition
method: POST
evidence: FACT
source: 开放API文档-组织模型.docx（项目代码中观察到）
purpose: 通过手机号/证件号等条件查询 V8 用户
```

**请求参数（params）：**

| 字段 | 必填 | 类型 | 说明 |
|------|------|------|------|
| cellphone | false | string | 手机号码 |
| certificateNumber | false | string | 证件号码 |
| isEnable | false | boolean | 是否启用 |
| code | false | string | 组织 code |
| includeChild | false | boolean | 是否包含下级 |
| includeDisable | false | boolean | 是否包含失效人员 |
| memberType | false | enum | MEMBER/OUTSIDE_MEMBER/NATURAL_MEMBER |

**响应（data.content）：** 同 API-ORG-001 的人员对象列表

**SSO 用途：** 三方系统传手机号 → 查 V8 用户 → 取 username

---

### API-ORG-003: 根据手机号查询个人用户

```yaml
id: API-ORG-003
path: /organization/natural/member/phoneNumber
method: POST
evidence: FACT
source: 开放API文档-组织模型.docx §2.1.3
purpose: 通过手机号查询外部个人用户
```

**请求参数（data）：**

| 字段 | 必填 | 类型 | 说明 |
|------|------|------|------|
| data | true | string | 手机号码 |

**响应（data.content）：**

```json
{
    "id": 12345,
    "name": "姓名",
    "phoneNumber": "手机号码",
    "certificateNumber": "证件号码",
    "email": "邮箱",
    "username": "用户名",
    "naturalMemberType": "自然人类型",
    "isEnable": true,
    "code": "编号"
}
```

**SSO 用途：** 三方系统传手机号 → 查外部个人用户 → 取 username

---

### API-ORG-004: 根据三方唯一标识查询人员

```yaml
id: API-ORG-004
path: /organization/member/thirdId
method: POST
evidence: FACT
source: 开放API文档-组织模型.docx §2.1.11
purpose: 通过三方系统唯一标识查询 V8 用户
```

**请求参数（data）：**

| 字段 | 必填 | 类型 | 说明 |
|------|------|------|------|
| data | true | string | 三方唯一标识 thirdId |

**响应（data.content）：** 同 API-ORG-001 的人员对象

**SSO 用途：** 三方系统传自身用户 ID → 查 V8 用户（需预先在 V8 中绑定 thirdId）

---

### API-ORG-005: 根据元数据值查询实体 ID

```yaml
id: API-ORG-005
path: /organization/metadata/selectEntityIdByMetadataValue
method: POST
evidence: FACT
source: 开放API文档-组织模型.docx §2.2.6
purpose: 通过自定义扩展字段的值查询人员/组织 ID
```

**请求参数（data）：**

| 字段 | 必填 | 类型 | 说明 |
|------|------|------|------|
| type | true | string | 实体类型：MEMBER（人员）或 UNIT（组织） |
| metadataCode | true | string | 扩展字段编码 |
| metadataValue | true | string | 扩展字段值 |

**响应（data.content）：**

```json
["12345", "12346"]
```

返回匹配的实体 ID 列表（字符串数组）。

**SSO 用途：** 三方系统传自定义标识（如工号、域账号）→ 通过元数据字段查 V8 用户 ID

---

### API-ORG-006: 根据编号查询个人用户

```yaml
id: API-ORG-006
path: /organization/natural/member/code
method: POST
evidence: FACT
source: 开放API文档-组织模型.docx §2.1.12
purpose: 通过编号查询外部个人用户
```

**请求参数（data）：**

| 字段 | 必填 | 类型 | 说明 |
|------|------|------|------|
| data | true | string | 编号 |

**响应（data.content）：** 同 API-ORG-003

---

### API-ORG-007: 分页查询组织下人员

```yaml
id: API-ORG-007
path: /organization/unit/members
method: POST
evidence: FACT
source: 开放API文档-组织模型.docx §2.1.5
purpose: 分页查询指定组织下的人员列表
```

**请求参数（params）：**

| 字段 | 必填 | 类型 | 说明 |
|------|------|------|------|
| code | false | string | 组织 code |
| includeChild | false | boolean | 是否包含下级 |
| effectiveTime | false | string | 人员生效时间 |
| startTime | false | string | 搜索开始时间 |
| endTime | false | string | 搜索结束时间 |
| includeDisable | false | boolean | 是否包含失效人员 |
| memberType | false | enum | MEMBER/OUTSIDE_MEMBER/NATURAL_MEMBER |
| thirdId | false | string | 组织三方唯一标识 |

**响应（data）：** 分页结构，content 为人员对象数组

---

### API-USER-001: 根据登录名查询用户信息

```yaml
id: API-USER-001
path: /ctp-user/loginName
method: POST
evidence: FACT
source: 开放API文档-用户中心.docx §2.1.1
purpose: 根据登录名查询 V8 用户信息
```

**请求参数（data）：**

| 字段 | 必填 | 类型 | 说明 |
|------|------|------|------|
| data | true | string | 登录名 |

**响应（data.content）：** 用户信息对象

---

### API-ORG-008: 查询指定人员的扩展字段值

```yaml
id: API-ORG-008
path: /organization/metadata/selectMemberMetadataInfo
method: POST
evidence: FACT
source: 开放API文档-组织模型.docx §2.2.9
purpose: 查询指定人员的指定扩展字段值
```

**请求参数（data）：**

| 字段 | 必填 | 类型 | 说明 |
|------|------|------|------|
| memberId | true | int64 | 人员 ID |
| code | true | string | 扩展字段编号 |

---

### API-ORG-009: 根据条件查询扩展字段信息

```yaml
id: API-ORG-009
path: /organization/metadata/selectByCondition
method: POST
evidence: FACT
source: 开放API文档-组织模型.docx §2.2.5
purpose: 查询扩展字段定义信息
```

---

### API-ORG-010: 查询指定组织的指定扩展字段下的人员

```yaml
id: API-ORG-010
path: /organization/metadata/selectMemberByUnitMetadata
method: POST
evidence: FACT
source: 开放API文档-组织模型.docx §2.2.1
purpose: 查询指定组织下具有特定扩展字段值的人员
```

---

## 3. SSO 场景 API 选择决策树

```
三方系统传什么标识？
├── 用户编号（code）
│   └── → API-ORG-001: /organization/member/code
│       取 content[0].username 作为 loginName
│
├── 手机号
│   ├── 内部人员 → API-ORG-002: /organization/base/member/selectMemberListByCondition
│   │   params: { cellphone: "xxx", isEnable: true }
│   └── 外部个人用户 → API-ORG-003: /organization/natural/member/phoneNumber
│
├── 三方唯一标识（thirdId）
│   └── → API-ORG-004: /organization/member/thirdId
│       需预先在 V8 中绑定 thirdId
│
├── 自定义扩展字段值（如工号、域账号）
│   └── → API-ORG-005: /organization/metadata/selectEntityIdByMetadataValue
│       type: "MEMBER", metadataCode: "字段编码", metadataValue: "值"
│       返回 ID 列表，再用 ID 查用户详情
│
├── 证件号码（身份证等）
│   └── → API-ORG-002: /organization/base/member/selectMemberListByCondition
│       params: { certificateNumber: "xxx", isEnable: true }
│
└── 登录名（username）
    └── → API-USER-001: /ctp-user/loginName
        直接查询用户信息
```

---

## 4. OpenAPI 工具类生成模板

```java
/**
 * V8 OpenAPI 通用调用工具类
 *
 * Generated by seeyon-v8-spi skill v5.0-LTS
 * Base URL: 从 Nacos 获取（seeyon.openApi.domain）
 * AppKey: 从 Nacos 获取（seeyon.openApi.appKey）
 * AppSecret: 从 Nacos 获取（seeyon.openApi.appSecret）
 */
@Slf4j
public class V8OpenApiClient {

    private static final String SIGN_TYPE = "MD5";

    /**
     * 通用 API 调用方法
     *
     * @param apiPath   API 路径（如 /organization/member/code）
     * @param paramName 参数包装名（"data" 或 "params"）
     * @param paramData 业务参数
     * @return 响应中的 data 部分
     */
    public Map invokeApi(String apiPath, String paramName, Object paramData) {
        String domain = CtpUserSpiUtils.getPropertyByName("seeyon.openApi.domain");
        String appKey = CtpUserSpiUtils.getPropertyByName("seeyon.openApi.appKey");
        String appSecret = ***;

        Map<String, String> headers = new HashMap<>();
        headers.put("app-key", appKey);
        headers.put("sign-type", SIGN_TYPE);

        Map<String, Object> body = new HashMap<>();
        body.put("requestId", UUID.randomUUID().toString());
        body.put("timestamp", System.currentTimeMillis());
        body.put(paramName, paramData);

        String bodyStr = JsonUtils.toJson(body);
        headers.put("sign", doSignMd5(bodyStr, appSecret));

        HttpResponse response = HttpUtil.createPost(domain + apiPath)
            .addHeaders(headers)
            .body(bodyStr)
            .execute();

        if (response.isOk()) {
            Map result = JsonUtils.toMap(response.body());
            return MapUtil.get(result, "data", Map.class);
        }
        log.error("OpenAPI 调用失败: api={}, status={}, body={}",
            apiPath, response.getStatus(), response.body());
        return null;
    }

    // ===== SSO 常用查询方法 =====

    /** 通过编号查用户登录名 (API-ORG-001) */
    public String queryLoginNameByCode(String code) {
        Map<String, Object> params = new HashMap<>();
        params.put("codes", Arrays.asList(code));
        params.put("includeDisable", false);
        Map data = invokeApi("/organization/member/code", "data", params);
        List content = MapUtil.get(data, "content", List.class);
        if (CollectionUtil.isNotEmpty(content)) {
            return MapUtil.getStr(((Map) content.get(0)), "username", "");
        }
        return "";
    }

    /** 通过手机号查用户登录名 (API-ORG-002) */
    public String queryLoginNameByPhone(String phone) {
        Map<String, Object> params = new HashMap<>();
        params.put("cellphone", phone);
        params.put("isEnable", true);
        Map data = invokeApi("/organization/base/member/selectMemberListByCondition", "params", params);
        List content = MapUtil.get(data, "content", List.class);
        if (CollectionUtil.isNotEmpty(content)) {
            return MapUtil.getStr(((Map) content.get(0)), "username", "");
        }
        return "";
    }

    /** 通过元数据值查用户 ID (API-ORG-005) */
    public String queryMemberIdByMetadata(String metadataCode, String metadataValue) {
        Map<String, Object> params = new HashMap<>();
        params.put("type", "MEMBER");
        params.put("metadataCode", metadataCode);
        params.put("metadataValue", metadataValue);
        Map data = invokeApi("/organization/metadata/selectEntityIdByMetadataValue", "data", params);
        List<String> content = MapUtil.get(data, "content", List.class);
        if (CollectionUtil.isNotEmpty(content)) {
            return content.get(0);
        }
        return null;
    }

    /** 通过三方标识查用户登录名 (API-ORG-004) */
    public String queryLoginNameByThirdId(String thirdId) {
        Map data = invokeApi("/organization/member/thirdId", "data", thirdId);
        Map content = MapUtil.get(data, "content", Map.class);
        if (content != null) {
            return MapUtil.getStr(content, "username", "");
        }
        return "";
    }

    private String doSignMd5(String data, String secret) {
        try {
            String signStr = secret + data + secret;
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] digest = md.digest(signStr.getBytes(StandardCharsets.UTF_8));
            StringBuilder sb = new StringBuilder();
            for (byte b : digest) {
                sb.append(String.format("%02x", b));
            }
            return sb.toString();
        } catch (Exception e) {
            log.error("MD5 签名失败", e);
            return "";
        }
    }
}
```

---

## 5. Nacos 配置（OpenAPI 相关）

```yaml
seeyon:
  openApi:
    appKey: {v8_openapi_app_key}  # 开放平台分配的 AppKey
    appSecret: CHANGE_ME_IN_NACOS  # 开放平台分配的 AppSecret
    domain: {v8_openapi_domain}  # V8 OpenAPI 域名（含协议和端口）
```

**注意：** domain 是环境配置，不同环境值不同。Path 是平台契约，固定不变。

---

## 6. 其他文档索引

以下文档包含更多 API，SSO 场景不常用但可能需要：

| 文档 | 主要内容 | SSO 相关性 |
|------|---------|-----------|
| 开放API文档-BPM引擎 | 流程、审批 | 低 |
| 开放API文档-事项中心 | 待办、已办 | 中（待办跳转） |
| 开放API文档-消息中心 | 消息推送 | 低 |
| 开放API文档-门户 | 门户页面 | 低 |
| 开放API文档-连接器 | 集成连接器 | 中（模式 C） |
| 开放API文档-流程中心 | 流程管理 | 低 |
| 开放API文档-日程 | 日程管理 | 低 |
| 开放API文档-报表中心 | 报表 | 低 |
| 开放API文档-低代码平台 | 低代码应用 | 低 |
| 开放API文档-基础设置 | 系统设置 | 低 |
| 开放API文档-移动办公 | 移动端 | 中（移动端 SSO） |
| 开放API文档-集成平台 | 集成管理 | 低 |
| 开放API文档-集成转换 | 数据转换 | 低 |
| 开放API文档-音视频服务 | 音视频 | 低 |
| 开放事件文档集合 | 事件订阅 | 低 |


---

## 附录：OpenAPI 文档索引

> 原 openapi-index.md

# V8 OpenAPI 文档索引

> 快速查找表，避免扫描 18 份 Word 文件。

## 文档清单

| 模块 | 文件 | API 数量 | SSO 相关性 |
|------|------|---------|-----------|
| 组织模型 | 开放API文档-组织模型.docx | 204 | ⭐⭐⭐ 高（用户查询、元数据） |
| 用户中心 | 开放API文档-用户中心.docx | 79 | ⭐⭐⭐ 高（登录名查询、角色） |
| 事项中心 | 开放API文档-事项中心.docx | 86 | ⭐⭐ 中（待办跳转） |
| 消息中心 | 开放API文档-消息中心.docx | 64 | ⭐⭐ 中（消息推送） |
| BPM引擎 | 开放API文档-BPM引擎.docx | ~100 | ⭐⭐ 中（流程启动/审批） |
| 流程中心 | 开放API文档-流程中心.docx | ~80 | ⭐⭐ 中（流程管理） |
| 连接器 | 开放API文档-连接器.docx | ~60 | ⭐⭐ 中（模式 C 集成） |
| 门户 | 开放API文档-门户.docx | ~40 | ⭐ 低 |
| 基础能力接入 | 开放API文档-基础能力接入.docx | ~120 | ⭐ 低（含通用调用规范） |
| 基础设置 | 开放API文档-基础设置.docx | ~50 | ⭐ 低 |
| 低代码平台 | 开放API文档-低代码平台.docx | ~80 | ⭐ 低 |
| 报表中心 | 开放API文档-报表中心.docx | ~40 | ⭐ 低 |
| 日程 | 开放API文档-日程.docx | ~60 | ⭐ 低 |
| 移动办公 | 开放API文档-移动办公.docx | ~50 | ⭐ 低 |
| 集成平台 | 开放API文档-集成平台.docx | ~40 | ⭐ 低 |
| 集成转换 | 开放API文档-集成转换.docx | ~30 | ⭐ 低 |
| 音视频服务 | 开放API文档-音视频服务.docx | ~56 | ⭐ 低 |
| 开放事件 | 开放事件文档集合.docx | ~100 | ⭐ 低（事件订阅） |

## 常见需求 → 文档映射

| 需求场景 | 查哪个文档 | 关键 API |
|---------|-----------|---------|
| SSO 用户匹配 | v8-openapi.md（已提取） | /organization/member/code 等 |
| 根据工号查用户 | 组织模型.docx §2.1.6 | /organization/member/code |
| 根据手机号查用户 | 组织模型.docx §2.1.3 | /organization/natural/member/phoneNumber |
| 根据三方标识查用户 | 组织模型.docx §2.1.11 | /organization/member/thirdId |
| 根据元数据查用户 | 组织模型.docx §2.2.6 | /organization/metadata/selectEntityIdByMetadataValue |
| 根据证件号查用户 | 组织模型.docx | /organization/base/member/selectMemberListByCondition |
| 查询登录名 | 用户中心.docx §2.1.1 | /ctp-user/loginName |
| 角色查询/维护 | 用户中心.docx §2.2 | /ctp-user/role/* |
| 发送待办 | 事项中心.docx | /ctp-affair/affair/create-batch |
| 查询待办 | 事项中心.docx | /ctp-affair/affair/search |
| 更新待办状态 | 事项中心.docx | /ctp-affair/affair/update-done |
| 发送消息 | 消息中心.docx | /ctp-message/openapi/message/send |
| 启动流程 | BPM引擎.docx | /ctp-bpm/* |
| 审批流程 | BPM引擎.docx | /ctp-bpm/* |
| 查询流程状态 | 流程中心.docx | /ctp-workflow/* |
| 组织/部门查询 | 组织模型.docx §2.5 | /organization/unit/* |
| 岗位查询 | 组织模型.docx | /organization/post/* |
| 职务查询 | 组织模型.docx | /organization/job/* |
| 职级查询 | 组织模型.docx | /organization/level/* |
| 文件操作 | 基础能力接入.docx | FileAppService/* |
| 事件订阅 | 开放事件文档集合.docx | 回调 URL 接收 |

## 使用方式

1. **SSO 生成时** → 直接读 `v8-openapi.md`（已提取 10 个核心 API）
2. **需要其他 API 时** → 查本索引确定文档 → 用 python-docx 读取对应 Word 提取参数表
3. **文档更新时** → 替换 `openapi-docs/` 下的 Word 文件，更新本索引的 API 数量

