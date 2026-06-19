# 移动插件 / Mobile*ProviderService

> **Evidence: FACT ✅** — 7 个接口签名来自 `cip-connector-api-5.3.286.jar` CFR 反编译。
> Source: jar 反编译 + 语雀 0111

## 场景

V8 平台 H5 应用接入三方 APP 工作台中，例如企业微信、钉钉、飞书等。

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>cip-connector-api</artifactId>
  <version>5.3.286</version>
</dependency>
```

## 接口清单 [FACT ✅]

所有接口继承 `MobileProviderService`（标记接口，无方法）。

| 序号 | 功能 | 接口 FQCN |
|------|------|-----------|
| 1 | 基础配置 | `com.seeyon.cip.connector.api.mobile.MobileConfigProviderService` |
| 2 | 应用功能 | `com.seeyon.cip.connector.api.mobile.MobileApplicationProviderService` |
| 3.1 | 组织同步-批量推送 | `com.seeyon.cip.connector.api.mobile.MobileOrgSyncBatchProviderService` |
| 3.2 | 组织同步-单个推送 | `com.seeyon.cip.connector.api.mobile.MobileOrgSyncProviderService` |
| 3.3 | 组织同步-拉取 | `com.seeyon.cip.connector.api.mobile.MobileOrgSyncPullProviderService` |
| 4.1 | 待办处理 | `com.seeyon.cip.connector.api.mobile.MobileTodoProviderService` |
| 4.2 | 回调通知 | `com.seeyon.cip.connector.api.mobile.MobileCallBackProviderService` |

## 方法表 [FACT ✅]

### MobileConfigProviderService

| 方法 | 参数 | 返回 | 调用时机 / 语义 | Evidence | Locator |
|------|------|------|----------------|----------|---------|
| `jsonCheck` | `String json` | `void` | 对 `getPageJson()` 返回的插件配置 JSON 做 jsr303 校验 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getName` | 无 | `String` | 插件唯一英文标识，如 `FEI_SHU` / `DING_TALK` | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getTypeCaption` | 无 | `String` | 三方客户端国际化名称 JSON | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getSortNo` | 无 | `Integer` | 插件排序号 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getPageJson` | 无 | `String` | 插件配置页面 JSON | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getAppId` | `String json` | `String` | 从配置 JSON 取 AppId | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getAppSecret` | `String json` | `String` | 从配置 JSON 取 AppSecret | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getAppName` | `String json` | `String` | 从配置 JSON 取 AppName | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getAdminUrl` | 无 | `String` | 三方插件管理后台 URL | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getThirdApplicationDomain` | `MobilePlatformConfigDto configDto` | `String` | 三方平台接口服务域名，default 返回 null | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
| `getThirdConfigCondition` | `String type, String corpId, String appId, String agentId` | `Map<String,Object>` | 根据指定 appId/agentId 获取第三方配置条件，default 返回 null | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileConfigProviderService |
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
| `listSyncOrg` | `MobilePlatformConfigDto configDto, String latestVersion` | `List<MobileSyncPullOrgResponseDto>` | 增量拉取组织 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncPullProviderService |
| `listSyncUser` | `MobilePlatformConfigDto configDto, String latestVersion` | `List<MobileSyncPullUserResponseDto>` | 增量拉取用户 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncPullProviderService |
| `listSyncPost` | `MobilePlatformConfigDto configDto, String latestVersion` | `List<MobileSyncPullPostDto>` | 增量拉取岗位，default 返回 null | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncPullProviderService |
| `listSyncJob` | `MobilePlatformConfigDto configDto, String latestVersion` | `List<MobileSyncPullJobDto>` | 增量拉取职务，default 返回 null | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncPullProviderService |
| `listSyncLevel` | `MobilePlatformConfigDto configDto, String latestVersion` | `List<MobileSyncPullLevelDto>` | 增量拉取职级，default 返回 null | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileOrgSyncPullProviderService |

### MobileTodoProviderService

| 方法 | 参数 | 返回 | 调用时机 / 语义 | Evidence | Locator |
|------|------|------|----------------|----------|---------|
| `createTodo` | `MobilePlatformConfigDto configDto, MobileTodoRequestDto dto` | `String` | 创建待办任务 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileTodoProviderService |
| `updateTodo` | `MobilePlatformConfigDto configDto, MobileTodoRequestDto dto` | `void` | 通过待办 id 更新待办信息 | FACT ✅ | `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md` §MobileTodoProviderService |
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

## MobileConfigProviderService [FACT ✅]

```java
package com.seeyon.cip.connector.api.mobile;

public interface MobileConfigProviderService extends MobileProviderService {
    void jsonCheck(String var1);
    String getName();
    String getTypeCaption();
    Integer getSortNo();
    String getPageJson();
    String getAppId(String var1);
    String getAppSecret(String var1);
    String getAppName(String var1);
    String getAdminUrl();
    default String getThirdApplicationDomain(MobilePlatformConfigDto dto) { return null; }
    default Map<String, Object> getThirdConfigCondition(String type, String corpId, String appId, String agentId) { return null; }
    default String getMobileCorpId(String corpId, String appId, String agentId) { return null; }
    boolean isPrivateApp();
    default Boolean isOnlyBaseInfo() { return false; }
}
```

## MobileApplicationProviderService [FACT ✅]

核心方法（部分）：消息发送/撤回、签名、URL 提供、OpenId 获取、SSO 免登、应用发布等。

## MobileOrgSyncBatchProviderService [FACT ✅]

```java
public interface MobileOrgSyncBatchProviderService extends MobileProviderService {
    String syncUnitBatch(MobileDepartmentBatchSyncDto var1, MobilePlatformConfigDto var2);
    String userSyncBatch(MobileUserBatchSyncDto var1, MobilePlatformConfigDto var2);
    MobileContactBatchResultDto syncBatchResult(MobileBatchResultDto var1, MobilePlatformConfigDto var2);
}
```

## MobileOrgSyncProviderService [FACT ✅]

```java
public interface MobileOrgSyncProviderService extends MobileProviderService {
    Long syncUnit(MobileUnitRequestDto var1, MobilePlatformConfigDto var2);
    void updateUnit(MobileUnitRequestDto var1, MobilePlatformConfigDto var2);
    String getUnit(MobileUnitRequestDto var1, MobilePlatformConfigDto var2);
    void removeUnit(MobileUnitRequestDto var1, MobilePlatformConfigDto var2);
    // + syncUser, updateUser, getUser, removeUser 等
}
```

## MobileOrgSyncPullProviderService [FACT ✅]

```java
public interface MobileOrgSyncPullProviderService extends MobileProviderService {
    List<MobileSyncPullOrgResponseDto> listSyncOrg(MobilePlatformConfigDto var1, String var2);
    List<MobileSyncPullUserResponseDto> listSyncUser(MobilePlatformConfigDto var1, String var2);
    default List<MobileSyncPullPostDto> listSyncPost(...) { return null; }
}
```

## MobileTodoProviderService [FACT ✅]

```java
public interface MobileTodoProviderService extends MobileProviderService {
    String createTodo(MobilePlatformConfigDto var1, MobileTodoRequestDto var2);
    void updateTodo(MobilePlatformConfigDto var1, MobileTodoRequestDto var2);
    @Deprecated default void doneTodo(MobilePlatformConfigDto configDto, Long userId, String taskId) {}
    @Deprecated default void deleteTodo(MobilePlatformConfigDto configDto, Long userId, String taskId) {}
}
```

## MobileCallBackProviderService [FACT ✅]

```java
public interface MobileCallBackProviderService<T extends BaseDto, Res>
    extends MobileProviderService, ConnectorCallbackProviderService<T, Res> {
}
```

## 代码骨架

```java
package com.seeyon.extend.spi.mobile;

import com.seeyon.cip.connector.api.mobile.MobileConfigProviderService;
import com.seeyon.cip.connector.dto.mobile.MobilePlatformConfigDto;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.Map;

public class CustomMobileConfigProvider implements MobileConfigProviderService {

    private static final Logger log = LoggerFactory.getLogger(CustomMobileConfigProvider.class);

    @Override
    public void jsonCheck(String json) {
        log.debug("[mobile-config] jsonCheck called");
    }

    @Override
    public String getName() { return "CUSTOM_APP"; }

    @Override
    public String getTypeCaption() { return "{\"zh_CN\":\"自定义应用\"}"; }

    @Override
    public Integer getSortNo() { return 99; }

    @Override
    public String getPageJson() { return "{}"; }

    @Override
    public String getAppId(String json) { return ""; }

    @Override
    public String getAppSecret(String json) { return ""; }

    @Override
    public String getAppName(String json) { return ""; }

    @Override
    public String getAdminUrl() { return ""; }

    @Override
    public boolean isPrivateApp() { return true; }
}
```

## Nacos 配置

本 SPI 不需要额外 Nacos 配置。如果业务逻辑需要读取配置，通过 `CipConnectorSpiUtils.getPropertyByName(...)` 获取。

## spring.factories

```properties
# 按需注册，7 个接口各自独立
com.seeyon.cip.connector.api.mobile.MobileConfigProviderService=com.seeyon.extend.spi.mobile.CustomMobileConfigProvider
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["cip-connector"]
}
```

## 重启服务

cip-connector

## 交叉引用

本 SPI 与 auth-sso 域的 Legacy mobile-app SPI 覆盖相同接口。
详见 `references/auth-sso/mobile-app/README.md`（已有工程模块 spi-06~12）。
