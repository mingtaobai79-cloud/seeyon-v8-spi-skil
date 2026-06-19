---
title: "组织同步中间表扩展"
source: "https://www.yuque.com/seeyonkk/v8/wthi6ignkwu033ok"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 组织同步中间表扩展

> Source: https://www.yuque.com/seeyonkk/v8/wthi6ignkwu033ok

作者：武海峰

版本要求：5.0.69

最后更新：2025-06-17

## 1.应用场景

在三方系统向A9方向进行同步的场景下，当采用中间表同步模式时，支持通过SPI自定义开发，提供主动拉取与被动接收两种模式，适用于标准产品OpenAPI写入不支持或不兼容的情况。

### 1.1、SPI主动拉取模式：

由标准产品根据【运行配置】触发。

在SPI实现中，调用三方接口获取指定维度（机构/部门、岗位、职务、职级、人员）的同步数据。

在阻塞式同步（即待所有维度数据均插入中间表完成后）方式下，SPI封装自定义逻辑处理结果数据，并分页写入中间表。

全部数据插入完成后，标准产品立即启动将组织同步中间表数据写入A9组织模型的操作。

### 1.2、SPI被动接收模式：

SPI实现监听接口，当三方系统主动推送数据时触发。

可根据与三方约定，自定义接收数据的格式（其中集成应用唯一标识linkerCode为必填项）。

将接收到的数据分页写入中间表。

检测各维度数据是否均已写入中间表。

所有维度数据写入完毕后，方可调用相应接口（例如，立即触发从中间表向A9组织模型的数据同步）。

## 2.接口说明

### 2.1、主动拉取

接口名称：com.seeyon.cip.connector.api.midorgsync.MiddleTableOrgSyncSpiPullService

```xml
<dependency>
    <groupId>com.seeyon</groupId>
    <artifactId>cip-connector-api</artifactId>
    <!-- 请以实际环境的依赖版本号为准-->
    <version>${cip-connector.version}</version>
</dependency>
```

### 2.2、被动接收

接口名称：com.seeyon.cip.connector.api.midorgsync.MiddleTableOrgSyncSpiListenerService

## 3.接口实现

spi代码仓库获取及工程初始化请参考：
开发准备

### 3.1、主动拉取

### 3.2、被动接收

注意：完成接口开发并构建成功后需要重启【cip-connector】服务才能进行后续功能验证

## 4.参数配置

### 4.1、主动拉取

#### 4.1.1、新建连接器-同步参数配置-设置主动拉取spi模式

<img width="1341">

#### 4.1.2、 同步内容映射配置举例

##### 4.1.2.1、部门配置-全量

关键词：TestSpiPull 或者 测试Spi拉取

步骤：在【wuhf测试勿删】 下创建一个部门【测试全量停用】，启用该部门

O202505090017

<img width="1937">

<img width="1874">

##### 4.1.2.2、职级配置-增量

##### 4.1.2.3、截图

<img width="1834">

##### 4.1.2.4、未配置的不参与spi的增量还是全量

<img width="1881">

#### 4.1.3、 运行配置

##### 4.1.3.1、步骤

【运行配置】下执行【立即同步】

<img width="1325">

### 4.2、被动接收

#### 4.2.1、新建连接器-同步参数配置-设置被动监听spi模式

<img width="1037">

#### 4.2.2、 同步内容映射配置

##### 4.2.2.1、部门配置-全量

##### 4.2.2.2、职级配置-增量

##### 4.2.2.3、截图

#### 4.2.3、 运行配置

##### 4.2.3.1、步骤

##### 4.2.3.2、postman模拟

post url:

dev环境：

https://dev.seeyonv8.com/service/cip-connector/base/callback/cip?cipTid=cop&cipType=null&cipChannel=MIDORGSYNC&cipAction=null

参数：

postman 参数"runningNowType": true, 标识执行立即同步，监听到数据结束后，不需要手动【运行配置】下执行【立即同步】

参数"runningNowType": false, 标识不执行立即同步,中间表状态为0 未处理

<img width="1378">

监听到数据结束后，需要手动【运行配置】下执行【立即同步】，执行后中间表状态为2 已处理

## 5.实现效果

### 5.1、主动拉取

#### 5.1.1、全量组织预期

<img width="1348">

组织模型新增俩条【测试_Spi_拉取】作为前缀的部门，部门【测试全量停用】状态变为停用，页面不显示

<img width="1915">

#### 5.1.2、增量职级预期

中间表数据库新增俩条【测试Spi拉取】作为前缀的的职级数据，状态为2同步成功状态

<img width="1353">

组织模型新增俩条【测试Spi拉取】作为前缀的职级

<img width="1917">

### 5.2、被动接收

#### 5.2.1、增量职级预期

中间表数据库新增俩条【测试Spi监听】作为前缀的的职级数据，状态为2同步成功状态

<img width="1372">

组织模型新增俩条【测试Spi监听】作为前缀的职级

<img width="1921">

## 6.示例代码

### 6.1、主动拉取

cip-connector-orgsync-pull-test.rar
(6 KB)

### 6.2、被动接收

cip-connector-orgsync-listener-test.rar
(4 KB)
