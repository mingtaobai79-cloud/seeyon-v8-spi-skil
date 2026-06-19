# 组织同步中间表扩展 / MiddleTableOrgSyncSpi*Service

> Evidence: FACT ✅ 用户提供的反编译接口源码。语雀 `0116-组织同步中间表扩展-wthi6ignkwu033ok.md` 为 OBSERVATION。
> 样例工程已抽取核验，登记为 `sample_key:orgsync-pull-example` / `sample_key:orgsync-listener-example`；其中业务 util 不纳入通用 SPI 约束。

## 场景

在三方系统向 A9 方向进行同步的场景下，当采用中间表同步模式时，支持通过 SPI 自定义开发，提供主动拉取与被动接收两种模式，适用于标准产品 OpenAPI 写入不支持或不兼容的情况。

适用版本：5.0.69 及以上版本。

## 实现业务线

组织同步中间表 SPI 的通用业务线只关心平台调用链，不绑定具体三方业务 util：

1. 标准产品按配置触发主动拉取，或三方系统通过 `cipChannel=MIDORGSYNC` 回调触发被动接收。
2. SPI 实现解析三方组织/人员/岗位/职务/职级数据。
3. SPI 不直接操作中间表数据库，必须通过 `MiddleTableOrgSyncDataCallbackService` 写入。
4. 全量主动拉取完成后调用 `markCallbackService.markComplete(linkerCode)`；增量拉取禁止调用 mark。
5. 满足执行条件后通过 `executeCallbackService.executeSyncToOrgModel(linkerCode)` 触发从中间表向 A9 组织模型同步。

## 两种模式

### 1. 主动拉取模式（Pull）

由标准产品根据【运行配置】触发：
- 在 SPI 实现中，调用三方接口获取指定维度（机构/部门、岗位、职务、职级、人员）的同步数据
- 在阻塞式同步方式下，SPI 封装自定义逻辑处理结果数据，并分页写入中间表
- 全部数据插入完成后，标准产品立即启动将组织同步中间表数据写入 A9 组织模型的操作

### 2. 被动接收模式（Listener）

SPI 实现监听接口，当三方系统主动推送数据时触发：
- 可根据与三方约定，自定义接收数据的格式（其中集成应用唯一标识 linkerCode 为必填项）
- 将接收到的数据分页写入中间表
- 检测各维度数据是否均已写入中间表
- 所有维度数据写入完毕后，方可调用相应接口触发从中间表向 A9 组织模型的数据同步

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>cip-connector-api</artifactId>
  <version>${cip-connector.version}</version>
</dependency>
```

## 接口定义 [FACT ✅]

### 主动拉取接口

```java
package com.seeyon.cip.connector.api.midorgsync;

import com.seeyon.cip.connector.annotation.CipConnectorComment;
import com.seeyon.cip.connector.api.midorgsync.callback.MiddleTableOrgSyncDataCallbackService;
import com.seeyon.cip.connector.api.midorgsync.callback.MiddleTableOrgSyncExecuteCallbackService;
import com.seeyon.cip.connector.api.midorgsync.callback.MiddleTableOrgSyncMarkCallbackService;
import com.seeyon.cip.connector.dto.midorgsync.spi.ConfigInfoApiDto;

@CipConnectorComment("中间表方式数据同步SPI主动拉取")
public interface MiddleTableOrgSyncSpiPullService {
    
    @CipConnectorComment("全量拉取(spi必须同步阻塞执行)")
    void pullAll(
        ConfigInfoApiDto configInfoApiDto,
        MiddleTableOrgSyncDataCallbackService dataCallbackService,
        MiddleTableOrgSyncMarkCallbackService markCallbackService,
        MiddleTableOrgSyncExecuteCallbackService executeCallbackService
    );

    @CipConnectorComment("增量拉取(spi必须同步阻塞执行)")
    void pullIncrement(
        ConfigInfoApiDto configInfoApiDto,
        MiddleTableOrgSyncDataCallbackService dataCallbackService,
        MiddleTableOrgSyncExecuteCallbackService executeCallbackService
    );
}
```

### 被动接收接口

```java
package com.seeyon.cip.connector.api.midorgsync;

import com.seeyon.cip.connector.annotation.CipConnectorComment;
import com.seeyon.cip.connector.api.midorgsync.callback.MiddleTableOrgSyncDataCallbackService;
import com.seeyon.cip.connector.api.midorgsync.callback.MiddleTableOrgSyncExecuteCallbackService;
import com.seeyon.cip.connector.api.midorgsync.callback.MiddleTableOrgSyncMarkCallbackService;
import com.seeyon.cip.connector.dto.callback.ConnectorCallbackRequestDto;

@CipConnectorComment("中间表方式数据同步SPI被动接收")
public interface MiddleTableOrgSyncSpiListenerService {
    
    @CipConnectorComment("SPI被动接收数据治理")
    Object dataGovernance(
        ConnectorCallbackRequestDto connectorCallbackRequestDto,
        MiddleTableOrgSyncDataCallbackService dataCallbackService,
        MiddleTableOrgSyncMarkCallbackService markCallbackService,
        MiddleTableOrgSyncExecuteCallbackService executeCallbackService
    );
}
```

## 方法说明

### MiddleTableOrgSyncSpiPullService

| 方法 | 参数 | 返回 | 语义 |
|------|------|------|------|
| `pullAll` | `ConfigInfoApiDto`, 3个回调服务 | `void` | 全量拉取（必须同步阻塞执行） |
| `pullIncrement` | `ConfigInfoApiDto`, 2个回调服务 | `void` | 增量拉取（必须同步阻塞执行） |

### MiddleTableOrgSyncSpiListenerService

| 方法 | 参数 | 返回 | 语义 |
|------|------|------|------|
| `dataGovernance` | `ConnectorCallbackRequestDto`, 3个回调服务 | `Object` | 被动接收数据治理 |

## 回调服务说明

### MiddleTableOrgSyncDataCallbackService [FACT ✅: 示例源码调用]

数据保存回调接口，用于将拉取/接收到的数据写入中间表。示例源码确认的批量保存方法：

| 维度 | 请求 DTO | 回调方法 |
|------|----------|----------|
| 组织/部门 | `UnitInfoSpiReqDto` | `batchSaveOrg(UnitInfoSpiReqDto)` |
| 岗位 | `PostInfoSpiReqDto` | `batchSavePosition(PostInfoSpiReqDto)` |
| 职务 | `DutyInfoSpiReqDto` | `batchSaveDuty(DutyInfoSpiReqDto)` |
| 职级 | `LevelInfoSpiReqDto` | `batchSaveLevel(LevelInfoSpiReqDto)` |
| 人员 | `MemberInfoSpiReqDto` | `batchSaveMember(MemberInfoSpiReqDto)` |

所有请求 DTO 均需设置 `linkerCode`，并通过 `setData(List<...>)` 放入当前批次数据；示例按分页循环写入。

### MiddleTableOrgSyncMarkCallbackService [FACT ✅: 示例源码调用]

数据标记接口，用于全量同步结束后的标记完成。示例调用签名：`markComplete(String linkerCode)`。**增量模式切勿调用**。

### MiddleTableOrgSyncExecuteCallbackService [FACT ✅: 示例源码调用]

立即从中间表到 A9 组织模型执行同步的回调接口。示例调用签名：`executeSyncToOrgModel(String linkerCode)`。

## DTO 定义 [FACT ✅]

### ConfigInfoApiDto（配置信息）

```java
package com.seeyon.cip.connector.dto.midorgsync.spi;

@DtoInfo("连接器配置参数")
public class ConfigInfoApiDto {
    private String linkerCode;  // 连接器编码（必填）
    private Map<String, Object> config;  // 配置参数
}
```

### ConnectorCallbackRequestDto（回调请求）

```java
package com.seeyon.cip.connector.dto.callback;

@DtoInfo("连接器回调请求")
public class ConnectorCallbackRequestDto {
    // 示例源码通过 getBody() 获取三方推送 JSON 字符串，再由 SPI 自行解析
    private String body;
}
```

### 样例源码确认的请求体字段 [FACT ✅]

被动监听示例从 `ConnectorCallbackRequestDto.getBody()` 解析 JSON，并读取：

| 字段 | 类型 | 语义 |
|------|------|------|
| `linkerCode` | `String` | 集成应用唯一标识，后续写入/mark/execute 均使用该值 |
| `orgSyncType` | `String` | 数据维度：`unit` / `staff` / `staffClass` / `staffDuty` / `position` |
| `dataType` | `String` | `full` 全量；`increment` 增量 |
| `runningNowType` | `Boolean` | `true` 表示本批结束后立即执行同步到组织模型 |
| `finishStatus` | `Boolean` | 当前批次/维度结束标识；为 `true` 时才考虑 mark/execute |
| `dataList` | `List<Map<String,Object>>` | 本批组织/人员/岗位/职级/职务数据 |

示例 URL 固定使用 `cipChannel=MIDORGSYNC`，业务体格式可与三方约定，但以上字段是官方样例验证过的最小控制字段。

## Nacos 配置

```yaml
# cip-connector 微服务 Nacos 配置
seeyon:
  connector:
    midorgsync:
      enabled: true
      mode: pull  # pull（主动拉取）或 listener（被动接收）
      batch-size: 1000
      timeout-ms: 60000
      retry-times: 3
```

## spring.factories

```properties
# 主动拉取模式
com.seeyon.cip.connector.api.midorgsync.MiddleTableOrgSyncSpiPullService=\
com.seeyon.extend.spi.{project_id}.{Prefix}OrgSyncPullService

# 被动接收模式
com.seeyon.cip.connector.api.midorgsync.MiddleTableOrgSyncSpiListenerService=\
com.seeyon.extend.spi.{project_id}.{Prefix}OrgSyncListenerService
```

### 示例包注册事实 [FACT ✅]

用户提供的两个样例工程均采用 `cip-spi-extend` 作为 parent，依赖 `com.seeyon:cip-connector-api`，打包类型为 `jar`：

| 样例工程 | SPI 接口 key | 实现类 | Channel Router |
|----------|-------------|--------|----------------|
| `sample_key:orgsync-pull-example` | `com.seeyon.cip.connector.api.midorgsync.MiddleTableOrgSyncSpiPullService` | `com.seeyon.cip.connector.orgsync.pull.test.TestPullServiceImpl` | `@MiddleTableChannelRouter(value = {"test_pull"}, description = "测试拉取")` |
| `sample_key:orgsync-listener-example` | `com.seeyon.cip.connector.api.midorgsync.MiddleTableOrgSyncSpiListenerService` | `com.seeyon.cip.connector.orgsync.listener.test.TestListenerServiceImpl` | `@MiddleTableChannelRouter(value = {"test_listener"}, description = "测试监听")` |

生成工程时必须同时满足：
- `META-INF/spring.factories` 使用对应 SPI 接口 FQCN 作为 key。
- 实现类加 `@MiddleTableChannelRouter`，`value` 是连接器配置中选择/识别的通道编码，不是 linkerCode。
- POM 只需依赖 `cip-connector-api`；不要为样例里的 Hutool/Lombok 额外引入未知版本，除非父工程已统一管理。

## 代码骨架（主动拉取）

```java
package com.seeyon.extend.spi.{project_id};

import com.seeyon.cip.connector.api.midorgsync.MiddleTableOrgSyncSpiPullService;
import com.seeyon.cip.connector.api.midorgsync.callback.MiddleTableOrgSyncDataCallbackService;
import com.seeyon.cip.connector.api.midorgsync.callback.MiddleTableOrgSyncExecuteCallbackService;
import com.seeyon.cip.connector.api.midorgsync.callback.MiddleTableOrgSyncMarkCallbackService;
import com.seeyon.cip.connector.dto.midorgsync.spi.ConfigInfoApiDto;
import lombok.extern.slf4j.Slf4j;

/**
 * {project_name_cn} 组织同步中间表主动拉取
 *
 * 场景：三方系统向 A9 同步组织数据，采用中间表模式，主动拉取三方数据
 * V8 调用时机：标准产品根据【运行配置】触发全量或增量同步
 * 三方系统：{third_system_name}
 * 返回语义：无返回值，通过回调服务写入中间表
 */
@Slf4j
public class {Prefix}OrgSyncPullService implements MiddleTableOrgSyncSpiPullService {

    @Override
    public void pullAll(
            ConfigInfoApiDto configInfoApiDto,
            MiddleTableOrgSyncDataCallbackService dataCallbackService,
            MiddleTableOrgSyncMarkCallbackService markCallbackService,
            MiddleTableOrgSyncExecuteCallbackService executeCallbackService) {
        
        log.info("[org-sync] 全量拉取开始, linkerCode: {}", configInfoApiDto.getLinkerCode());

        try {
            // 1. 调用三方接口获取全量数据
            // TODO: 实现三方接口调用
            // List<OrgData> orgList = fetchAllOrgData(configInfoApiDto.getConfig());

            // 2. 分页写入中间表
            // TODO: 实现数据写入逻辑
            // for (List<UnitInfoSpiDto> batch : partition(unitList, 1000)) {
            //     UnitInfoSpiReqDto req = new UnitInfoSpiReqDto();
            //     req.setLinkerCode(configInfoApiDto.getLinkerCode());
            //     req.setData(batch);
            //     dataCallbackService.batchSaveOrg(req);
            // }

            // 3. 标记全量同步完成（增量模式切勿调用）
            markCallbackService.markComplete(configInfoApiDto.getLinkerCode());

            // 4. 立即执行从中间表到 A9 组织模型的同步
            executeCallbackService.executeSyncToOrgModel(configInfoApiDto.getLinkerCode());

            log.info("[org-sync] 全量拉取完成");

        } catch (Exception e) {
            log.error("[org-sync] 全量拉取失败", e);
            throw new RuntimeException("全量拉取失败: " + e.getMessage(), e);
        }
    }

    @Override
    public void pullIncrement(
            ConfigInfoApiDto configInfoApiDto,
            MiddleTableOrgSyncDataCallbackService dataCallbackService,
            MiddleTableOrgSyncExecuteCallbackService executeCallbackService) {
        
        log.info("[org-sync] 增量拉取开始, linkerCode: {}", configInfoApiDto.getLinkerCode());

        try {
            // 1. 调用三方接口获取增量数据
            // TODO: 实现三方接口调用
            // List<OrgData> incrementList = fetchIncrementOrgData(configInfoApiDto.getConfig());

            // 2. 分页写入中间表
            // TODO: 实现数据写入逻辑
            // for (List<UnitInfoSpiDto> batch : partition(unitIncrementList, 1000)) {
            //     UnitInfoSpiReqDto req = new UnitInfoSpiReqDto();
            //     req.setLinkerCode(configInfoApiDto.getLinkerCode());
            //     req.setData(batch);
            //     dataCallbackService.batchSaveOrg(req);
            // }

            // 3. 立即执行从中间表到 A9 组织模型的同步
            executeCallbackService.executeSyncToOrgModel(configInfoApiDto.getLinkerCode());

            log.info("[org-sync] 增量拉取完成");

        } catch (Exception e) {
            log.error("[org-sync] 增量拉取失败", e);
            throw new RuntimeException("增量拉取失败: " + e.getMessage(), e);
        }
    }
}
```

## 代码骨架（被动接收）

```java
package com.seeyon.extend.spi.{project_id};

import com.seeyon.cip.connector.api.midorgsync.MiddleTableOrgSyncSpiListenerService;
import com.seeyon.cip.connector.api.midorgsync.callback.MiddleTableOrgSyncDataCallbackService;
import com.seeyon.cip.connector.api.midorgsync.callback.MiddleTableOrgSyncExecuteCallbackService;
import com.seeyon.cip.connector.api.midorgsync.callback.MiddleTableOrgSyncMarkCallbackService;
import com.seeyon.cip.connector.dto.callback.ConnectorCallbackRequestDto;
import com.seeyon.boot.util.JsonUtils;
import lombok.extern.slf4j.Slf4j;

import java.util.Map;

/**
 * {project_name_cn} 组织同步中间表被动接收
 *
 * 场景：三方系统向 A9 同步组织数据，采用中间表模式，被动接收三方推送数据
 * V8 调用时机：三方系统主动推送数据时触发
 * 三方系统：{third_system_name}
 * 返回语义：处理结果对象
 */
@Slf4j
public class {Prefix}OrgSyncListenerService implements MiddleTableOrgSyncSpiListenerService {

    @Override
    public Object dataGovernance(
            ConnectorCallbackRequestDto connectorCallbackRequestDto,
            MiddleTableOrgSyncDataCallbackService dataCallbackService,
            MiddleTableOrgSyncMarkCallbackService markCallbackService,
            MiddleTableOrgSyncExecuteCallbackService executeCallbackService) {
        
        try {
            // 1. 解析三方推送的数据
            String body = connectorCallbackRequestDto.getBody();
            Map<String, Object> payload = JsonUtils.toMap(body);
            String linkerCode = String.valueOf(payload.get("linkerCode"));
            log.info("[org-sync] 被动接收数据, linkerCode: {}", linkerCode);
            // TODO: 根据与三方约定的格式解析数据

            // 2. 分页写入中间表
            // TODO: 实现数据写入逻辑
            // UnitInfoSpiReqDto req = new UnitInfoSpiReqDto();
            // req.setLinkerCode(linkerCode);
            // req.setData(parsedUnits);
            // dataCallbackService.batchSaveOrg(req);

            // 3. 检测各维度数据是否均已写入中间表
            // TODO: 实现完整性检测逻辑
            // boolean allDimensionsReady = checkAllDimensionsReady();

            // 4. 所有维度数据写入完毕后，触发同步
            // if (allDimensionsReady) {
            //     executeCallbackService.executeSyncToOrgModel(linkerCode);
            // }

            log.info("[org-sync] 被动接收数据处理完成");

            return "success";

        } catch (Exception e) {
            log.error("[org-sync] 被动接收数据处理失败", e);
            throw new RuntimeException("数据处理失败: " + e.getMessage(), e);
        }
    }
}
```

## 配置步骤

### 主动拉取模式

1. 新建连接器 → 同步参数配置 → 设置主动拉取 SPI 模式
2. 配置同步内容映射（部门、职级等）
3. 运行配置 → 执行【立即同步】

### 被动接收模式

1. 新建连接器 → 同步参数配置 → 设置被动监听 SPI 模式
2. 配置同步内容映射
3. 三方系统通过回调 URL 推送数据：

```
POST https://{domain}/service/cip-connector/base/callback/cip
  ?cipTid={tenantId}
  &cipType=null
  &cipChannel=MIDORGSYNC
  &cipAction=null
```

参数说明：
- `runningNowType: true`：执行立即同步，监听到数据结束后不需要手动执行
- `runningNowType: false`：不执行立即同步，中间表状态为 0（未处理），需要手动执行

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["cip-connector"]
}
```

## 重启服务

`cip-connector`
