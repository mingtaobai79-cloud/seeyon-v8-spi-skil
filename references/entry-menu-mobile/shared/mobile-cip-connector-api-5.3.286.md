# Mobile Provider Contract — cip-connector-api-5.3.286

Session-derived contract note. Use this when working on either:

- `references/auth-sso/mobile-app/`
- `references/entry-menu-mobile/mobile-plugin/`

## Source

- Artifact: `cip-connector-api-5.3.286.jar`
- Package: `com.seeyon.cip.connector.api.mobile`
- Evidence: FACT ✅, CFR反编译确认

These two skill domains cover the same 7 mobile provider interfaces. Do not treat them as two different artifact sources.

## Interfaces

- `MobileProviderService` — marker interface
- `MobileConfigProviderService`
- `MobileApplicationProviderService`
- `MobileOrgSyncBatchProviderService`
- `MobileOrgSyncProviderService`
- `MobileOrgSyncPullProviderService`
- `MobileTodoProviderService`
- `MobileCallBackProviderService<T, Res>`
- callback parent: `com.seeyon.cip.connector.api.callback.ConnectorCallbackProviderService<T, Res>`
- callback sender: `ConnectorCallbackMessageSendService<T>`

## Important correction

An older/early整理版 of `auth-sso/mobile-app` used simplified or wrong signatures such as:

- `MobileConfigProviderService#getThirdConfigCondition()`
- `MobileConfigProviderService#getThirdConfig(String appId)`
- `getAdminUrl(String appId)`
- `MobileApplicationProviderService#getApplicationUrl(...)`
- `sendMessage(String appId, ...)`
- Maven version `3.8.211`

For V8 `cip-connector-api-5.3.286.jar`, those are not authoritative. Use the jar signatures below.

## Core method signatures

### MobileConfigProviderService

```java
void jsonCheck(String json);
String getName();
String getTypeCaption();
Integer getSortNo();
String getPageJson();
String getAppId(String json);
String getAppSecret(String json);
String getAppName(String json);
String getAdminUrl();
default String getThirdApplicationDomain(MobilePlatformConfigDto configDto) { return null; }
default Map<String, Object> getThirdConfigCondition(String type, String corpId, String appId, String agentId) { return null; }
default String getMobileCorpId(String corpId, String appId, String agentId) { return null; }
boolean isPrivateApp();
default Boolean isOnlyBaseInfo() { return false; }
```

### MobileApplicationProviderService

```java
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
```

### MobileOrgSyncBatchProviderService

```java
String syncUnitBatch(MobileDepartmentBatchSyncDto dto, MobilePlatformConfigDto configDto);
String userSyncBatch(MobileUserBatchSyncDto dto, MobilePlatformConfigDto configDto);
MobileContactBatchResultDto syncBatchResult(MobileBatchResultDto resultDto, MobilePlatformConfigDto configDto);
```

### MobileOrgSyncProviderService

```java
Long syncUnit(MobileUnitRequestDto dto, MobilePlatformConfigDto configDto);
void updateUnit(MobileUnitRequestDto dto, MobilePlatformConfigDto configDto);
String getUnit(MobileUnitRequestDto dto, MobilePlatformConfigDto configDto);
void removeUnit(MobileUnitRequestDto dto, MobilePlatformConfigDto configDto);
String syncUser(MobileUserRequestDto dto, MobilePlatformConfigDto configDto);
String updateUser(MobileUserRequestDto dto, MobilePlatformConfigDto configDto);
MobileUserResponseDto getUser(MobileUserRequestDto dto, MobilePlatformConfigDto configDto);
MobileUserResponseDto removeUser(MobileUserRequestDto dto, MobilePlatformConfigDto configDto);
default MobileOrgDto syncUnitNew(MobileUnitRequestDto dto, MobilePlatformConfigDto configDto) { return null; }
```

### MobileOrgSyncPullProviderService

```java
List<MobileSyncPullOrgResponseDto> listSyncOrg(MobilePlatformConfigDto configDto, String latestVersion);
List<MobileSyncPullUserResponseDto> listSyncUser(MobilePlatformConfigDto configDto, String latestVersion);
default List<MobileSyncPullPostDto> listSyncPost(MobilePlatformConfigDto configDto, String latestVersion) { return null; }
default List<MobileSyncPullJobDto> listSyncJob(MobilePlatformConfigDto configDto, String latestVersion) { return null; }
default List<MobileSyncPullLevelDto> listSyncLevel(MobilePlatformConfigDto configDto, String latestVersion) { return null; }
```

### MobileTodoProviderService

```java
String createTodo(MobilePlatformConfigDto configDto, MobileTodoRequestDto dto);
void updateTodo(MobilePlatformConfigDto configDto, MobileTodoRequestDto dto);
@Deprecated default void doneTodo(MobilePlatformConfigDto configDto, Long userId, String taskId) {}
@Deprecated default void deleteTodo(MobilePlatformConfigDto configDto, Long userId, String taskId) {}
default String doneTodo(MobilePlatformConfigDto configDto, MobileTodoTaskDto taskDto) { return null; }
default String deleteTodo(MobilePlatformConfigDto configDto, MobileTodoTaskDto taskDto) { return null; }
```

### Callback

```java
Res doCallback(ConnectorCallbackRequestDto requestDto, ConnectorCallbackMessageSendService<T> messageSendService);
void sendMsgAsync(T message);
void sendMsgSync(T message);
```

## Maintenance rule

When updating either mobile-app or mobile-plugin documentation, keep both aligned to this contract source. If a future jar version is supplied, re-run targeted CFR extraction and update this note plus both domain README files together.