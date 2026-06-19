---
title: "国际化"
source: "https://www.yuque.com/seeyonkk/v8/eoy2cvzi8g2xz23v"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 国际化

> Source: https://www.yuque.com/seeyonkk/v8/eoy2cvzi8g2xz23v

## 国际化规范

### 资源国际化

【强制】国际化资源文件按组出现(xxx_en.properties、xxx_zh_CN.properties、xxx_zh_TW.properties)，xxx部分不允许出现下划线。

【强制】公共词条中不允许新增词条，如需新增联系平台，公共词条中仅允许新增中性名词(不涉及业务的词语)。

【强制】异常错误码词条存放error-code_xx.properties，java枚举词条存放enums_xx.properties。

【强制】JAVA枚举类 创建国际化key为枚举类fullName + ".caption"。

【强制】JAVA枚举项 创建国际化key为枚举类fullName + "." + name。

【强制】国际化资源信息Key命名规范，建议3-5段，参考:{应用标识}.{功能标识}.xxx

麻烦大家创建key起名字要有意义，最终目的让客户能看懂.

```
org.member.age=年龄
org.department.level=部门层级
```

【强制】国际化资源key不能完整包含其他key，否则无法转换为json格式供前端使用。错误示例：

```
common.title=标题
common.title.index=标题
```

【强制】后端异常错误码国际化的key必须以"error.code.业务类型_异常编号"形式。例如：

```
error.code.ORG_0001=人员已停用
```

【强制】后端组件补充元数据描述(没有词条并且不需要实体元数据国际化/jsr303国际化的可暂时不补),描述文件位置: {starter}/resources/metadata/starter_info.json

```
{
  "name":"boot-starter-attachment", //必填组件名称
  "caption":"boot-starter-attachment.caption", //固定格式,需要编写词条,内容为组件显示名称(组件名称不需要国际化的可以直接写中文)
  "basePackage":"com.seeyon.boot.starter.attachment",//必填扫描元数据使用
  "type":"1" //0:基础组件 1:业务组件
}
```

【强制】相同词语禁止创建多个词条。

【强制】优先使用公共词条中已存在的词条，后端getMessage方法可以直接调用公共词条。

【强制】格式语句(如:属性{0}的值反序列化为{1}类型时失败)使用变量占位符，禁止创建多个key拼接使用。

【强制】禁止出现只有一段的国际化key，例如: show_title=显示标题。

【强制】后端增加实体元数据生成词条开关，请大家判断如果不需要公布实体信息的应用手动关闭， seeyon.i18n.entity-metadata.enable=false， 关闭后词条管理处不显示实体元数据分类。

示例：

```
@Autowired
private MessageRepository messageRepository;

String colStatus = messageRepository.getMessage("bpm.workflow.pending");
```

带参数的国际化可以通过占位符key及相应的方法实现。

```
common.scheduledstats.whichMonth = 第{0}月
```

```
@Autowired
private MessageRepository messageRepository;

String message= messageRepository.getMessage("demoOrder.orderStats.total", [2021,1000]);
```

跨应用调用。

```
com.seeyon.bpm.enums.FlowTypeEnum = 流程类型
```

### 数据国际化

●
应用通过组件统一设置数据国际化，例如人员姓名：

<img >

●
数据库字段长度一般为500(实际业务中按具体用量上下调整)，数据国际化语种做为key生成json字符串存储,如：

## 多时区处理

多时区统一由前端实现，前后端针对Date类型的传输统一使用Long类型。

说明：针对时间类型的数据显示和传输的格式要求如下：

#### 前端 ---> 后端

#### 后端 ---> 前端
