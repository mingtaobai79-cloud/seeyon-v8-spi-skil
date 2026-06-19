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
