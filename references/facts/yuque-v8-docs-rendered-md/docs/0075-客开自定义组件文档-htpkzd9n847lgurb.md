---
title: "客开自定义组件文档"
source: "https://www.yuque.com/seeyonkk/v8/htpkzd9n847lgurb"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 客开自定义组件文档

> Source: https://www.yuque.com/seeyonkk/v8/htpkzd9n847lgurb

## 1
UDC自定义组件

当标品的udc页面设计器组件不满足客户场景 ，可以新增一个自定义的udc组件替换标准组件 具体的步骤可以参考代码的预置“日历测试”组件

### 1.1
目录结构

```
extend-components/
  └── component-a                       
      └── src/                       
          ├── components/
              ├── design.tsx        // 设计态组件
              ├── attr.tsx          // 设计器右侧自定义属性
          ├── i18n/                 // 国际化配置文件, 如果没有内容, 每个文件中必须写一个 空对象-{}
              ├── en.json     
              ├── zh_CN.json
              ├── zh_TW.json
          ├── schema.ts                 // 设计态shema描述文件
          ├── runtime.tsx               // 运行态组件
          ├── index.module.less         // 采用cssModule隔离
          ├── typings.d.ts              // 全局ts声明文件
      ├── tsconfig.json
      ├── README.md       // 组件使用文档   
      └── sy.config.json   //组件配置文件 
```

### 1.2
组件配置文件

```
{
  "packageName": "@kk/modal", // 必填 ，包名需要以@kk开头，唯一，需满足npm包名规范
  "sourceType": "CUSTOMIZE", // 可选，默认是CUSTOMIZE, PORTAL表示为门户元素
  "i18nDependencies": [
    {
      "name": "@seeyon/biz-watermark",
      "caption": "水印组件",
      "version": "2.2.9"
    }
  ], // 可选, 国际化依赖，当依赖的组件是通过外部化方式引用时，需要填写. 具体可以参考平台组件配置文件: /libs/businesses.json
  "appNames": [
    "edoc335172694483814428"
  ], // 可选, 设计态哪些应用可以使用，空值代表所有UDC应用都可以使用
  "control": {
    "name": "自定义弹窗", // 必填 控件名称
    "type": "Bizxxx",  // 必填 控件标识
    "icon": "FilledApplicationW", // 可选 控件图标 默认为 FilledApplicationW
    "description": "用于展示自定义内容", // 必填 控件描述
    "terminalType": "PC", // 必填 终端 PC/MOBILE
    "bizCategory": "custom" // 可选  控件分类, 默认值为 custom
  },
  "dataTypes": [ //重复表可以选择到新增的控件
    {
      "dataType": "MULTILINESTRING"
    },
    {
      "dataType": "STRING"
    }
  ]
}
```

该配置由5.0.3版本开始支持，5.0.3版本之前的版本请参考 1.3. 组件配置文件 (旧)

### 1.3
组件配置文件 (旧)

```
{
  "$schemaVersion": "v1", 
  "packageName": "@kk/new-edoc-handling-results",// 必填 ，包名需要以kk开头，唯一，满足npm包名规范，不允许.多个斜杠特殊字符
  "i18nDependencies": [
    {
      "name": "@seeyon/biz-watermark",
      "caption": "水印组件",
      "version": "2.2.9"
    }
  ], // 可选, 国际化依赖，当依赖的组件是通过外部化方式引用时，需要填写. 具体可以参考平台组件配置文件: /libs/businesses.json
  "appNames": [
    "edoc335172694483814428"
  ], // 可选, 设计态哪些应用可以使用，空值代表所有UDC应用都可以使用
  "controls": [
    {
      "name": "客开办理成果（公文专用）",// 控件的中文名称
      "type": "KKNewEdocHandlingResults",// 控件 ID，如 UiBusinessBaseOcr
      "icon": "LinedCamera",// 控件的 ICON
      "description": "客开新增的办理成果（公文专用）", // 控件的描述信息（请务必填写
      "terminalType": "PC",// 控件所支持的端，PC - PC端，MOBILE - 移动端
      "group": "application"; //控件分组 可选项：input - 录入控件、display - 展示控件、process - 流程控件、application - 业务控件
      "order": 2;  // 当控件为内建控件（bizCategory = builtin）时，需要配置控件顺序，// 可参考：https://docs.qq.com/sheet/DSmpGRkNMWEZLSldr?tab=we8m26&u=8b6d312f4b744a1fa28c4d0c39cec48d
      "bizCategory": "custom",// 控件业务分类，主要有两个业务分类：builtin - 内建控件；custom - 自定义控件
      "dataTypes": [{ "dataType": "MULTILINESTRING" }];  // 只需要表单控件才需要配置这个
      // 打包入口相关的配置，注意均需要用 default（默认）导出
      "designModule": "./src/components/index.tsx", // 设计态入口
      "schemaModule": "./src/components/Schema.ts", // 控件 schema 入口
      "runtimeModule":  "./src/components/index.tsx"// 运行时入口
    }
  ],
   "dataTypes": [ //重复表可以选择到新增的控件
    {
      "dataType": "MULTILINESTRING"
    },
    {
      "dataType": "STRING"
```

### 1.4
Schema配置描述

Schema 规范包括以下内容：

1
组件结构定义： 描述业务组件的结构，包括组件的布局、子组件的嵌套关系等。

2
属性定义： 定义业务组件接受的属性（props），包括属性的类型、默认值、是否必需等信息。

3
事件和方法定义： 描述业务组件可能触发或响应的事件，以及组件暴露的方法和接口。

```
import {
  defaultExpressionValue,
  basicUiModelSchema,
  inputControlStateUiModelNotIncludeDisabled,
  commonAttrs,
} from "@seeyon/global";
import { 
  commonAttrs, 
  commonFontSizeStyle, 
  commonStyle
} from '@seeyon/udc-asset-utils';

export default {
  group: "data" | "application" | "base" | "layout",// 组件分组-同 sy.config.js group
  name: '客开新的选人规则',// String类型,控件中文名-同 sy.config.js name
  type: 'KKNewSelectPeople',//String 类型,控件Type（唯一 ID）-同 sy.config.js type 
  description: '客开新的发布范围-选人控件，选中的人有目标功能权限',//控件的描述
  icon: 'LinedProjectBoard',// 图标，String类型用于UDC设计器左侧的组件显示-同 sy.config.js icon
  order: 4.9, // Number类型 顺序-用于UDC设计器左侧的组件显示-同 sy.config.js order
  isFormItem?: true,// Booleanl类型 是否为表单项
  uiModelSchema: [
    ...basicUiModelSchema,
    inputControlStateUiModelNotIncludeDisabled
  ],//可选 表达式弹窗可选项  可被外部动态修改的配置项 
  dataTypes: [{
      type: DataType.MultilineString,
      defaultCmp: true,
    }],// 默认数据类型  ["String"]
  controlActions?: [// 控件行为或操作按钮
    {
      label: 'OPEN_ORG_SELECTOR', // 用于控件动作列表展示
      value: '打开选人界面', // 组件中自己实现的动作名，如果单一记录 : [{ value: 'create', label: '新增' },...]
    }
  ], // 控件行为, 关联udc设计器中，事件配置的控件动作列表
  // 设计器中，右侧属性面板配置
  settings: [
```

备注：

1.key:dataSource 是放到外面，是预置属性，UDC会做额外的属性

classification: 'settings',控件自定义属性，UDC仅仅透传

2.调用表达式：defaultExpressionValue('')

Schema 是如何关联到 UDC 设计器的？

在控件元数据中，我们有一个 designModule 指向的地址，在这个默认导出的对象上，我们需要追加一个 Schema 属性，用来绑定控件的 Schema。

也就是说：要将 Schema 以静态属性的方式关联到设计态组件上。

示例如下：

<img src="https://cdn.nlark.com/yuque/0/2024/png/382504/1713851262625-52449286-a96e-4ddd-919c-fe9275dff8ad.png?x-oss-process=image%2Fformat%2Cwebp" width="1144">

## 2
自定义组件

当客开需要开发非UDC组件时，如多个UDC手写页面需要共用同一个组件

### 2.1
目录结构

### 2.2
组件配置文件
