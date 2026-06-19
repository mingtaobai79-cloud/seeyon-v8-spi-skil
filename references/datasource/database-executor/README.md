# 数据源扩展 / DataBaseExecutorService

> **Evidence: FACT ✅** — 接口签名、DTO、枚举来自 `cip-connector-api-5.3.286.jar` CFR 反编译。

## 场景

为新的数据库类型提供支持，或优化现有数据库操作。当平台未内置支持某种数据库时，开发者可以自行实现操作接口。

版本要求：5.3+

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>cip-connector-api</artifactId>
  <version>5.3.286</version>
</dependency>
```

## 接口定义 [FACT ✅]

```java
package com.seeyon.cip.connector.api.db;

import com.seeyon.boot.transport.PageData;
import com.seeyon.cip.connector.dto.db.*;
import com.seeyon.cip.connector.enums.DbTypeEnum;
import java.sql.Connection;
import java.util.List;
import java.util.Map;

@CipConnectorComment("数据执行接口")
public interface DataBaseExecutorService {
    @CipConnectorComment("获取数据库类型")
    DbTypeEnum getDbTypeEnum();

    @CipConnectorComment("数据库名称")
    String getName();

    @CipConnectorComment("执行动作")
    ExecutorResultApiDto executeDetail(DatabaseInfoApiDto var1, LinkerDetailApiDto var2, Map<String, Object> var3);

    @CipConnectorComment("执行动作,获取数量")
    Integer executeDetailForCount(DatabaseInfoApiDto var1, LinkerDetailApiDto var2, Map<String, Object> var3);

    // 更多方法（文档截断部分）：
    // executeSql, getTableInfo, testConnection 等
}
```

## 方法说明

| 方法 | 参数 | 返回 | 语义 |
|------|------|------|------|
| getDbTypeEnum | 无 | `DbTypeEnum` | 返回支持的数据库类型枚举 |
| getName | 无 | `String` | 返回数据源插件名称（页面展示用） |
| executeDetail | `DatabaseInfoApiDto, LinkerDetailApiDto, Map` | `ExecutorResultApiDto` | 执行查询/更新/插入/删除 |
| executeDetailForCount | `DatabaseInfoApiDto, LinkerDetailApiDto, Map` | `Integer` | 执行计数查询 |

## DTO 定义 [FACT ✅]

### DatabaseInfoApiDto

```java
package com.seeyon.cip.connector.dto.db;

@DtoInfo("数据配置dto")
public class DatabaseInfoApiDto extends BaseDto {
    Long id;
    String caption;          // 名称，max 30
    ConfigModeEnum mode;     // 配置类型 DB/MQ，默认 DB
    String type;             // 类型（mysql/oracle 等）
    Boolean status;          // 状态，默认 true
    String url;              // 数据库地址
    String username;         // 用户名
    String password;         // 密码
    String driver;           // 驱动类名
    // ... 更多字段
}
```

### ExecutorResultApiDto

```java
package com.seeyon.cip.connector.dto.db;

@DtoInfo("执行结果")
public class ExecutorResultApiDto extends BaseDto {
    Object param;                    // 参数
    Object result;                   // 结果
    Object httpRequest;              // http 请求数据
    Object httpResponse;             // http 应答主数据
    BusinessException exception;     // 异常
    PageInfo pageInfo;               // 分页
}
```

### DbTypeEnum [FACT ✅]

```java
package com.seeyon.cip.connector.enums;

public enum DbTypeEnum implements Messageable {
    Oracle(1, "Oracle", "jdbc:oracle:thin:@//127.0.0.1:1521/orcl"),
    MySQL(2, "MySQL", "jdbc:mysql://127.0.0.1:3306/..."),
    // ... 更多枚举值（SQLServer, PostgreSQL, 达梦, 人大金仓等）
}
```

## 代码骨架

```java
package com.seeyon.extend.spi.datasource;

import com.seeyon.cip.connector.api.db.DataBaseExecutorService;
import com.seeyon.cip.connector.dto.db.*;
import com.seeyon.cip.connector.enums.DbTypeEnum;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.Map;

public class CustomDataBaseExecutorService implements DataBaseExecutorService {

    private static final Logger log = LoggerFactory.getLogger(CustomDataBaseExecutorService.class);

    @Override
    public DbTypeEnum getDbTypeEnum() {
        return DbTypeEnum.Oracle; // 替换为目标数据库类型
    }

    @Override
    public String getName() {
        return "Custom DB Executor";
    }

    @Override
    public ExecutorResultApiDto executeDetail(DatabaseInfoApiDto dbInfo,
            LinkerDetailApiDto linkerDetail, Map<String, Object> requestMap) {
        log.debug("[datasource] executeDetail called, db={}", dbInfo.getCaption());
        ExecutorResultApiDto result = new ExecutorResultApiDto();
        // TODO: 实现数据库连接、SQL 构建、执行、结果封装
        return result;
    }

    @Override
    public Integer executeDetailForCount(DatabaseInfoApiDto dbInfo,
            LinkerDetailApiDto linkerDetail, Map<String, Object> requestMap) {
        log.debug("[datasource] executeDetailForCount called");
        return 0;
    }
}
```

## Nacos 配置

本 SPI 不需要额外 Nacos 配置。所有连接信息通过 DatabaseInfoApiDto 传入。

## spring.factories

```properties
com.seeyon.cip.connector.api.db.DataBaseExecutorService=com.seeyon.extend.spi.datasource.CustomDataBaseExecutorService
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
