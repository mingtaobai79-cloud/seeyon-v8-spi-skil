# 数据源域共享资源

## 域概述

扩展 V8 集成平台的数据源连接能力，支持 Oracle/MySQL/SQLServer/PostgreSQL/达梦/人大金仓等。

- 核心接口 jar：cip-connector-api
- 核心接口：`com.seeyon.cip.connector.api.db.DataBaseExecutorService`
- 版本要求：5.3+

## 解决的问题

1. 数据库兼容性问题：不同数据库的 SQL 语法、数据类型、分页机制、函数差异
2. 特定功能支持：某些数据库特有的高级功能或优化手段
3. 现场环境定制化：特定数据库配置或非标准版本

## 部署效果

1. 页面数据源配置界面能看到自定义数据源类型
2. 用户可以基于自定义数据源进行配置操作
3. 系统通过 DataBaseExecutorService 接口与数据库交互
