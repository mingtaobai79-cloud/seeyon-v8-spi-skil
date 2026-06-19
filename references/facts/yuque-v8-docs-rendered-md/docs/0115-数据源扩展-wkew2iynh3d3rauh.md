---
title: "数据源扩展"
source: "https://www.yuque.com/seeyonkk/v8/wkew2iynh3d3rauh"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 数据源扩展

> Source: https://www.yuque.com/seeyonkk/v8/wkew2iynh3d3rauh

作者：林荣鑫

版本要求：5.3

最后更新：2025-06-17

## 1. 应用场景

在企业级应用中，数据源的多样性是一个普遍存在的挑战。不同的业务系统可能依赖于各种数据库产品（如 MySQL、Oracle、SQL Server、PostgreSQL 等），甚至同一数据库产品在不同版本间也可能存在语法或行为差异。当平台需要统一管理和操作这些异构数据源时，原生的数据库驱动和通用 JDBC 操作往往无法完全满足所有场景的需求，容易出现以下问题：

●
数据库兼容性问题：不同数据库的 SQL 语法、数据类型、分页机制、函数等存在差异，导致一套通用的 SQL 语句无法在所有数据库上正确执行。

●
特定功能支持：某些数据库可能拥有特有的高级功能或优化手段，通用驱动无法充分利用。

●
现场环境定制化：用户现场可能存在特定的数据库配置或非标准数据库版本，需要定制化的连接和操作逻辑。

为了解决上述问题，本平台引入了数据源 SPI 扩展机制。通过此机制，开发者可以：

●
为新的数据库类型提供支持：当平台未内置支持某种数据库时，开发者可以自行实现其操作接口。

●
优化现有数据库操作：针对特定数据库的某个版本或特定配置，提供更高效、更稳定的操作实现。

●
统一数据库操作接口：将不同数据库的差异性封装在 SPI 实现内部，向上层应用提供统一、标准的数据库操作接口，从而避免因底层数据库变化而引发的兼容性问题，提升系统的灵活性和可维护性。

## 2. 接口说明

核心接口 jar 包 cip-connector-api 定义了数据源扩展所需的所有契约。开发者需实现其中定义的接口，以提供特定数据库的操作能力。

●
接口接口依赖： cip-connector-api

●
核心接口名称： com.seeyon.cip.connector.api.db.DataBaseExecutorService

依赖配置：

在您的扩展项目中，需要引入 cip-connector-api 的 Maven 依赖：

```xml
<dependency>
    <groupId>com.seeyon</groupId>
    <artifactId>cip-connector-api</artifactId>
    <!-- 请以实际环境的依赖版本号为准，确保与平台版本一致 -->
    <version>xxx</version>
</dependency>
```

接口名称：com.seeyon.cip.connector.api.db.DataBaseExecutorService

```
@CipConnectorComment("数据执行接口")
public interface DataBaseExecutorService {

    // 注解说明：@CipConnectorComment 仅用于提供代码注释说明，方便API使用者理解，不影响运行时SPI的加载逻辑。

    /**
     * 获取当前实现类所支持的数据库类型。
     * 平台将根据此返回值识别并匹配对应的数据库插件。
     * @return 返回此数据源插件对应的数据库枚举类型，例如 DbTypeEnum.Oracle。
     */
    @CipConnectorComment("获取数据库类型")
    DbTypeEnum getDbTypeEnum();

    /**
     * 获取当前数据源插件的唯一名称。
     * 此名称将可能在页面上显示，用于标识不同的数据源实现。
     * @return 返回数据库插件的名称，例如 "Oracle 11g Executor"。
     */
    @CipConnectorComment("数据库名称")
    String getName();

    /**
     * 执行由平台根据 LinkerDetailApiDto 配置生成的数据库操作（如查询、更新、插入、删除）。
     * 这是核心的执行方法，负责将抽象的业务操作转换为具体的数据库SQL并执行。
     *
     * @param databaseInfoApiDto 包含数据库的连接信息（URL、用户名、密码、驱动等）。
     * @param linkerDetailApiDto 包含要执行的SQL操作的结构化配置，如查询字段、表名、条件、分组、排序、分页等。
     * @param requestMap 运行时传入的请求参数，用于SQL中的占位符替换。
     * @return 返回 ExecutorResultApiDto，包含执行结果数据（如List<Map>）、受影响的行数、分页信息或异常信息。
     */
    @CipConnectorComment("执行动作")
    ExecutorResultApiDto executeDetail(DatabaseInfoApiDto databaseInfoApiDto, LinkerDetailApiDto linkerDetailApiDto, Map<String, Object> requestMap);

    /**
     * 执行由平台根据 LinkerDetailApiDto 配置生成的计数查询。
     * 通常用于在分页查询前获取总记录数。
```

## 3. 接口实现

spi代码仓库获取及工程初始化请参考：
开发准备

要扩展数据源功能，您需要创建一个实现了 com.seeyon.cip.connector.api.db.DataBaseExecutorService 接口的类，并将其注册为 SPI 服务。该接口定义了连接管理、元数据查询、SQL 执行、结果处理等一系列核心数据库操作方法，旨在提供一个全面的数据库抽象层。

示例实现类：Oracle11gSpiDataBaseExecutorService

## 4. 参数配置

无额外特殊的参数配置。SPI 实现将通过其自身的代码逻辑来处理数据库连接和操作所需的参数。所有必要的连接信息都将通过 DatabaseInfoApiDto 等 DTO 传入。

## 5. 实现效果

当您成功实现并部署了数据源 SPI 插件后：

1
在平台的页面数据源配置界面，您将能够看到并选择您通过 SPI 实现的自定义数据源类型。

2
用户可以基于该自定义数据源进行配置操作，例如创建新的数据源实例，并利用其提供的连接、表信息获取、数据查询等功能。

3
系统将通过您实现的 DataBaseExecutorService 接口与对应的数据库进行交互，确保操作的正确性和兼容性。

## 6. 示例代码

以下是一个针对 Oracle 11g 数据库 的 DataBaseExecutorService 接口实现示例。

OracleSpiDataBaseExecutorService.java
(33 KB)

## 7.通过数据源直接查询SQL

入参：数据源Id以及需要执行的SQL
