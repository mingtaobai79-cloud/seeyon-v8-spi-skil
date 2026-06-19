# V8 接入三方 App / Mobile*ProviderService

> **Evidence: FACT ✅** — 7 个接口签名来自用户提供的 用户提供的 `cip-connector-api-5.3.286.jar`，CFR 反编译确认。
> Source: `cip-connector-api-5.3.286.jar` / package `com.seeyon.cip.connector.api.mobile`。
> 语雀 `0111-V8接入三方App-rx8blahmz6zt2u4d.md` 只作为 OBSERVATION ⚠️，不覆盖 jar 签名。

## 场景

V8 H5 应用接入企业微信、钉钉、飞书等三方 App 工作台。包括移动端应用 URL、JSAPI 签名、消息发送、组织同步、待办、回调等能力。

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>cip-connector-api</artifactId>
  <version>5.3.286</version>
</dependency>
```

## 接口清单（7 个）[FACT ✅]

所有接口位于 `com.seeyon.cip.connector.api.mobile`，并继承标记接口 `MobileProviderService`。

| 接口 | 作用 |
|------|------|
| `MobileConfigProviderService` | 三方 App 插件基础配置、配置页、AppId/Secret/AdminUrl |
| `MobileApplicationProviderService` | 移动应用 URL、应用发布、JSAPI 签名、消息、免登用户、接口状态 |
| `MobileOrgSyncBatchProviderService` | 通讯录批量同步 |
| `MobileOrgSyncProviderService` | 组织/人员单个推送、更新、删除、查询 |
| `MobileOrgSyncPullProviderService` | 组织/人员/岗位/职务/职级拉取同步 |
| `MobileTodoProviderService` | 待办创建、更新、完成、删除 |
| `MobileCallBackProviderService<T,Res>` | 三方 App 回调通知，继承 `ConnectorCallbackProviderService<T,Res>` |

## 方法表 [FACT ✅]

### MobileConfigProviderService

| 方法 | 参数 | 返回 | 调用时机 / 语义 | Evidence | Locator |
|------|------|------|----------------|----------|---------|
| `jsonCheck` | `String json` | `void` | 对 `getPageJson()` 返回的插件配置 JSON 做 jsr303 校验 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getName` | 无 | `String` | 插件唯一英文标识，如 `FEI_SHU` / `DING_TALK` | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getTypeCaption` | 无 | `String` | 三方客户端国际化名称 JSON，如 `{"zh_CN":"飞书"}` | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getSortNo` | 无 | `Integer` | 插件排序号 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getPageJson` | 无 | `String` | 插件配置页面 JSON | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getAppId` | `String json` | `String` | 从配置 JSON 取 AppId | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getAppSecret` | `String json` | `String` | 从配置 JSON 取 AppSecret | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getAppName` | `String json` | `String` | 从配置 JSON 取 AppName | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getAdminUrl` | 无 | `String` | 三方插件管理后台 URL | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getThirdApplicationDomain` | `MobilePlatformConfigDto configDto` | `String` | 三方平台接口服务域名，default 返回 null | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getThirdConfigCondition` | `String type, String corpId, String appId, String agentId` | `Map<String,Object>` | 根据 type/corpId/appId/agentId 获取第三方配置条件，default 返回 null | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getMobileCorpId` | `String corpId, String appId, String agentId` | `String` | 获取插件 corpId，default 返回 null | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `isPrivateApp` | 无 | `boolean` | 是否私有 App，SPI 模式固定返回 true | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `isOnlyBaseInfo` | 无 | `Boolean` | 是否只展示基本信息，default 返回 false | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |

### MobileApplicationProviderService

| 方法 | 参数 | 返回 | 调用时机 / 语义 | Evidence | Locator |
|------|------|------|----------------|----------|---------|
| `getMobileUrlDto` | `MobileUrlProviderDto dto` | `MobileUrlDto` | 获取移动插件展示 URL | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileApplicationProviderService |
| `explainLinkInfo` | 无 | `String` | 解释链接信息 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileApplicationProviderService |
| `publishApp` | `MobilePublishAppRequestDto requestDto, MobilePlatformConfigDto configDto` | `Long` | 发布应用 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileApplicationProviderService |
| `getSignature` | `MobilePlatformConfigDto configDto, MobilePlatformSignatureDto dto` | `MobilePlatformSignatureResultDto` | 获取 JSAPI 签名 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileApplicationProviderService |
| `sendMessage` | `boolean isActionCard, MobileMessageRequestDto requestDto, MobilePlatformRequestDto platformRequestDto` | `void` | 发送消息/消息卡片 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileApplicationProviderService |
| `getMobileSsoUserDto` | `MobilePlatformConfigDto configDto, MobileSsoUserRequestDto dto` | `MobileSsoUserDto` | 获取免登用户信息 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileApplicationProviderService |
| `interfaceStatus` | `MobilePlatformConfigDto configDto` | `MobileInterfaceStatusDto` | 接口状态查询，default 返回 null | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileApplicationProviderService |
| `getOpenId` | `MobilePlatformConfigDto configDto, MobileOpenIdDto dto` | `String` | 获取用户 OpenId，`@Deprecated` | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileApplicationProviderService |
| `getLaunchCode` | `MobilePlatformConfigDto configDto, MobileLaunchCodeDto dto` | `String` | 获取 launch_code，default 返回 null | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileApplicationProviderService |
| `recallMessage` | `MobilePlatformConfigDto configDto, RecallMessageDto dto` | `RecallResultDto` | 撤回消息，default 返回 null | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileApplicationProviderService |

### MobileOrgSyncBatchProviderService

| 方法 | 参数 | 返回 | 调用时机 / 语义 | Evidence | Locator |
|------|------|------|----------------|----------|---------|
| `syncUnitBatch` | `MobileDepartmentBatchSyncDto dto, MobilePlatformConfigDto configDto` | `String` | 组织批量同步 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncBatchProviderService |
| `userSyncBatch` | `MobileUserBatchSyncDto dto, MobilePlatformConfigDto configDto` | `String` | 用户批量同步 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncBatchProviderService |
| `syncBatchResult` | `MobileBatchResultDto resultDto, MobilePlatformConfigDto configDto` | `MobileContactBatchResultDto` | 查询同步批量结果 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncBatchProviderService |

### MobileOrgSyncProviderService

| 方法 | 参数 | 返回 | 调用时机 / 语义 | Evidence | Locator |
|------|------|------|----------------|----------|---------|
| `syncUnit` | `MobileUnitRequestDto dto, MobilePlatformConfigDto configDto` | `Long` | 同步组织 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncProviderService |
| `updateUnit` | `MobileUnitRequestDto dto, MobilePlatformConfigDto configDto` | `void` | 更新组织 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncProviderService |
| `getUnit` | `MobileUnitRequestDto dto, MobilePlatformConfigDto configDto` | `String` | 查询组织 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncProviderService |
| `removeUnit` | `MobileUnitRequestDto dto, MobilePlatformConfigDto configDto` | `void` | 删除组织 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncProviderService |
| `syncUser` | `MobileUserRequestDto dto, MobilePlatformConfigDto configDto` | `String` | 同步人员 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncProviderService |
| `updateUser` | `MobileUserRequestDto dto, MobilePlatformConfigDto configDto` | `String` | 更新人员 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncProviderService |
| `getUser` | `MobileUserRequestDto dto, MobilePlatformConfigDto configDto` | `MobileUserResponseDto` | 查询人员 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncProviderService |
| `removeUser` | `MobileUserRequestDto dto, MobilePlatformConfigDto configDto` | `MobileUserResponseDto` | 删除人员 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncProviderService |
| `syncUnitNew` | `MobileUnitRequestDto dto, MobilePlatformConfigDto configDto` | `MobileOrgDto` | 同步组织并返回 DTO，default 返回 null | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncProviderService |

### MobileOrgSyncPullProviderService

| 方法 | 参数 | 返回 | 调用时机 / 语义 | Evidence | Locator |
|------|------|------|----------------|----------|---------|
| `listSyncOrg` | `MobilePlatformConfigDto configDto, String latestVersion` | `List<MobileSyncPullOrgResponseDto>` | 增量拉取组织；`latestVersion=1` 通常表示全量 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncPullProviderService |
| `listSyncUser` | `MobilePlatformConfigDto configDto, String latestVersion` | `List<MobileSyncPullUserResponseDto>` | 增量拉取用户 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncPullProviderService |
| `listSyncPost` | `MobilePlatformConfigDto configDto, String latestVersion` | `List<MobileSyncPullPostDto>` | 增量拉取岗位，default 返回 null | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncPullProviderService |
| `listSyncJob` | `MobilePlatformConfigDto configDto, String latestVersion` | `List<MobileSyncPullJobDto>` | 增量拉取职务，default 返回 null | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncPullProviderService |
| `listSyncLevel` | `MobilePlatformConfigDto configDto, String latestVersion` | `List<MobileSyncPullLevelDto>` | 增量拉取职级，default 返回 null | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncPullProviderService |

### MobileTodoProviderService

| 方法 | 参数 | 返回 | 调用时机 / 语义 | Evidence | Locator |
|------|------|------|----------------|----------|---------|
| `createTodo` | `MobilePlatformConfigDto configDto, MobileTodoRequestDto dto` | `String` | 创建待办任务 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileTodoProviderService |
| `updateTodo` | `MobilePlatformConfigDto configDto, MobileTodoRequestDto dto` | `void` | 通过待办 id 更新待办信息，不包含完成状态 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileTodoProviderService |
| `doneTodo` | `MobilePlatformConfigDto configDto, Long userId, String taskId` | `void` | 旧完成待办方法，`@Deprecated`，default 空实现 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileTodoProviderService |
| `deleteTodo` | `MobilePlatformConfigDto configDto, Long userId, String taskId` | `void` | 旧删除待办方法，`@Deprecated`，default 空实现 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileTodoProviderService |
| `doneTodo` | `MobilePlatformConfigDto configDto, MobileTodoTaskDto taskDto` | `String` | 通过待办 id 更新为已完成，default 返回 null | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileTodoProviderService |
| `deleteTodo` | `MobilePlatformConfigDto configDto, MobileTodoTaskDto taskDto` | `String` | 通过待办 id 删除待办，default 返回 null | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileTodoProviderService |

### MobileCallBackProviderService / ConnectorCallbackProviderService

| 方法 | 参数 | 返回 | 调用时机 / 语义 | Evidence | Locator |
|------|------|------|----------------|----------|---------|
| `doCallback` | `ConnectorCallbackRequestDto requestDto, ConnectorCallbackMessageSendService<T> messageSendService` | `Res` | 回调业务处理；实现类需要加 `@ConnectorChannelRouter`，注解值需与回调请求地址中的 `type` 一致 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §Callback |
| `sendMsgAsync` | `T message` | `void` | 回调处理中异步发送 MQ 消息 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §Callback |
| `sendMsgSync` | `T message` | `void` | 回调处理中同步发送 MQ 消息 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §Callback |

## 接口定义摘要 [FACT ✅]

```java
package com.seeyon.cip.connector.api.mobile;

public interface MobileProviderService {}

public interface MobileConfigProviderService extends MobileProviderService {
    void jsonCheck(String json);
    String getName();
    String getTypeCaption();
    Integer getSortNo();
    String getPageJson();
    String getAppId(String json);
    String getAppSecret(String json);
    String getAppName(String json);
    String getAdminUrl();
    default String getThirdApplicationDomain(MobilePlatformConfigDto dto) { return null; }
    default Map<String, Object> getThirdConfigCondition(String type, String corpId, String appId, String agentId) { return null; }
    default String getMobileCorpId(String corpId, String appId, String agentId) { return null; }
    boolean isPrivateApp();
    default Boolean isOnlyBaseInfo() { return false; }
}

public interface MobileApplicationProviderService extends MobileProviderService {
    MobileUrlDto getMobileUrlDto(MobileUrlProviderDto dto);
    String explainLinkInfo();
    Long publishApp(MobilePublishAppRequestDto requestDto, MobilePlatformConfigDto configDto);
    MobilePlatformSignatureResultDto getSignature(MobilePlatformConfigDto configDto, MobilePlatformSignatureDto dto);
    void sendMessage(boolean isActionCard, MobileMessageRequestDto requestDto, MobilePlatformRequestDto platformRequestDto);
    MobileSsoUserDto getMobileSsoUserDto(MobilePlatformConfigDto configDto, MobileSsoUserRequestDto dto);
    default MobileInterfaceStatusDto interfaceStatus(MobilePlatformConfigDto configDto) { return null; }
    @Deprecated String getOpenId(MobilePlatformConfigDto configDto, MobileOpenIdDto dto);
    default String getLaunchCode(MobilePlatformConfigDto configDto, MobileLaunchCodeDto dto) { return null; }
    default RecallResultDto recallMessage(MobilePlatformConfigDto configDto, RecallMessageDto dto) { return null; }
}
```

其余组织/待办/回调接口见上方方法表；生成代码时以 `cip-connector-api-5.3.286.jar` 反编译结果为准。

## Nacos 配置

本 SPI 平台接口不强制额外 Nacos key。业务实现如果需要三方密钥/域名，建议放到 `cip-connector` 微服务 Nacos：

```yaml
seeyon:
  mobile-app:
    {app_type}:
      corp-id: CHANGE_ME_IN_NACOS
      agent-id: CHANGE_ME_IN_NACOS
      app-secret: CHANGE_ME_IN_NACOS
      admin-url: https://third.example.com/admin
      api-domain: https://third.example.com
      callback-type: CHANGE_ME  # @ConnectorChannelRouter 值
```

## spring.factories

```properties
com.seeyon.cip.connector.api.mobile.MobileConfigProviderService=\
com.seeyon.extend.spi.{project_id}.{Prefix}MobileConfigProviderService
com.seeyon.cip.connector.api.mobile.MobileApplicationProviderService=\
com.seeyon.extend.spi.{project_id}.{Prefix}MobileApplicationProviderService
com.seeyon.cip.connector.api.mobile.MobileOrgSyncBatchProviderService=\
com.seeyon.extend.spi.{project_id}.{Prefix}MobileOrgSyncBatchProviderService
com.seeyon.cip.connector.api.mobile.MobileOrgSyncProviderService=\
com.seeyon.extend.spi.{project_id}.{Prefix}MobileOrgSyncProviderService
com.seeyon.cip.connector.api.mobile.MobileOrgSyncPullProviderService=\
com.seeyon.extend.spi.{project_id}.{Prefix}MobileOrgSyncPullProviderService
com.seeyon.cip.connector.api.mobile.MobileTodoProviderService=\
com.seeyon.extend.spi.{project_id}.{Prefix}MobileTodoProviderService
com.seeyon.cip.connector.api.mobile.MobileCallBackProviderService=\
com.seeyon.extend.spi.{project_id}.{Prefix}MobileCallBackProviderService
```

## 代码骨架（MobileConfigProviderService）

```java
package com.seeyon.extend.spi.{project_id};

import com.seeyon.cip.connector.api.mobile.MobileConfigProviderService;
import com.seeyon.cip.connector.dto.mobile.MobilePlatformConfigDto;
import java.util.Map;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * {project_name_cn} 三方 App 基础配置。
 *
 * Contract Source: cip-connector-api-5.3.286.jar [FACT ✅]
 * Scope: cip-connector
 */
public class {Prefix}MobileConfigProviderService implements MobileConfigProviderService {
    private static final Logger log = LoggerFactory.getLogger({Prefix}MobileConfigProviderService.class);

    @Override
    public void jsonCheck(String json) {
        log.debug("[mobile-app] validate config json");
        // TODO: 校验 getPageJson() 对应配置 JSON。
    }

    @Override
    public String getName() { return "{APP_TYPE}"; }

    @Override
    public String getTypeCaption() { return "{\"zh_CN\":\"{APP_NAME_CN}\"}"; }

    @Override
    public Integer getSortNo() { return 99; }

    @Override
    public String getPageJson() { return "{}"; }

    @Override
    public String getAppId(String json) { return ""; }

    @Override
    public String getAppSecret(String json) { return ""; }

    @Override
    public String getAppName(String json) { return "{APP_NAME_CN}"; }

    @Override
    public String getAdminUrl() { return ""; }

    @Override
    public String getThirdApplicationDomain(MobilePlatformConfigDto configDto) { return null; }

    @Override
    public Map<String, Object> getThirdConfigCondition(String type, String corpId, String appId, String agentId) {
        return null;
    }

    @Override
    public String getMobileCorpId(String corpId, String appId, String agentId) { return corpId; }

    @Override
    public boolean isPrivateApp() { return true; }
}
```

## 代码骨架（MobileCallBackProviderService）

```java
package com.seeyon.extend.spi.{project_id};

import com.seeyon.boot.transport.BaseDto;
import com.seeyon.cip.connector.annotation.ConnectorChannelRouter;
import com.seeyon.cip.connector.api.callback.ConnectorCallbackMessageSendService;
import com.seeyon.cip.connector.api.mobile.MobileCallBackProviderService;
import com.seeyon.cip.connector.dto.callback.ConnectorCallbackRequestDto;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * {project_name_cn} 三方 App 回调通知。
 *
 * @ConnectorChannelRouter 的值必须等于回调请求地址中的 type 值。
 */
@ConnectorChannelRouter("{CALLBACK_TYPE}")
public class {Prefix}MobileCallBackProviderService implements MobileCallBackProviderService<BaseDto, Object> {
    private static final Logger log = LoggerFactory.getLogger({Prefix}MobileCallBackProviderService.class);

    @Override
    public Object doCallback(ConnectorCallbackRequestDto requestDto,
                             ConnectorCallbackMessageSendService<BaseDto> messageSendService) {
        log.info("[mobile-app] callback received");
        // TODO: 按三方回调事件类型分发处理。
        return null;
    }
}
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["cip-connector"]
}
```

## 重启服务

`cip-connector`
