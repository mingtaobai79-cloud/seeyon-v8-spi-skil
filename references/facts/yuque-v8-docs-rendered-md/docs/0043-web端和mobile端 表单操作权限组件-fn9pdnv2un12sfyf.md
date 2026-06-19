---
title: "web端和mobile端 表单操作权限组件"
source: "https://www.yuque.com/seeyonkk/v8/fn9pdnv2un12sfyf"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# web端和mobile端 表单操作权限组件

> Source: https://www.yuque.com/seeyonkk/v8/fn9pdnv2un12sfyf

●
图标库的图标选择器

```
引入： import { FormOperation } from '@seeyon/biz-form-permission'

使用：
    const processData: FormOperationInterface = {
        mode: 'design'| 'runtime'   // 区分运行态、设计态
        expressMode: string   // 表达式模式 
        scrollY?: string     // 表格高度滚动样式
        showSubPage?: boolean  // 是否展示子页面控件，默认展示
        fieldInfoMap: FieldInfo;        // 字段信息map  {fullName: fieldInfo}
        serverName: string;  // 表达式后端服务名
        appId: string;       // 应用Id，用于表达式
        permissionsCode?: PermissionsCode; // 权限类型
        applicationName: string;  // 应用编码，用于表达式
        rootEntityId?: string;     // 模板的rootEntityId， 用于表达式
        rootEntityName?: string;   // 模板的rootEntityName， 用于表达式
        paramType: 'ENTITY_RT' | 'ENTITY'; // 表达式的paramType 区分运行态、设计态
        schemaInfoList: SchemaInterface[];  // schema信息列表
        authData: any[];      // 权限数据列表
        ref: any;
        setChangeFlag?: any;  // 页面状态改变时，执行 setChangeFlag(true)，用于监听修改
        dealEntityField?: any; // 获取实体、字段名称，用于更新子页面字段的名称map
        isFieldSame: boolean;   // 是否字段联动设置
    }
    <FormOperation
          ref={authRef}
          linkageStyle={{ left: '50px'  }}
          mode={mode}
          isFieldSame={true}
          appId={appId}
          expressMode={MODE}
          scrollY='calc(100vh - 460px)'
          fieldInfoMap={fieldInfoMap}
          permissionsCode={authDetail.permissionsCode}
          applicationName={templateInfo?.applicationName}
          rootEntityId={templateInfo?.rootEntityId}
          rootEntityName={templateInfo?.rootEntityName}
```

●
获取权限数据 使用 authRef.current.getSaveData()

●
获取字段联动设置 使用authRef.current.getLinkage()

# API

#### FormOperationInterface

| 参数 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| mode | 区分运行态、设计态 | 'design' / 'runtime' | - |
| expressMode | 表达式模式，参考表达式组件的mode | string | - |
| scrollY | 表格高度滚动样式 | string | - |
| showSubPage | 是否展示子页面控件（当前页面有子页面才会生效） | boolean | true |
| fieldInfoMap | 字段信息map {fullName: FieldInfo} | any | - |
| serverName | 表达式后端服务名 | string | - |
| appId | 应用Id，用于表达式 等同于 Flow的id | string | - |
| permissionsCode | 权限类型 | PermissionsCode | - |
| applicationName | 应用编码 | string | - |
| rootEntityId | 模板的rootEntityId， 用于表达式 | string | - |
| rootEntityName | 模板的rootEntityName， 用于表达式 | string | - |
| paramType | 表达式的paramType 区分运行态、设计态 | 'ENTITY_RT' / 'ENTITY' | - |
| schemaInfoList | schema信息列表 | SchemaInterface[] | - |
| authData | 权限数据列表 | any | - |
| linkageStyle | 字段联动设置样式 | any | - |
| ref | ref | any | - |
| setChangeFlag | 页面状态改变时，执行 setChangeFlag(true)，用于监听修改 | string | - |
| dealEntityField | 获取实体、字段名称，用于更新子页面字段的名称map | () => {} | - |
| isFieldSame | 是否字段联动的勾选状态 | boolean | - |

●
PermissionsCode: 'CUSTOM' | 'APPROVAL' | 'INFORM' | 'WRITE'

#### SchemaInterface

| 参数 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| tabName | tab名称 | string | - |
| schema | 页面schema | string | - |
| key | tab的key，目前只支持 PC\ MOBILE | WidgetDeviceType | - |

●
WidgetDeviceType: 'PC' | 'MOBILE'

#### FieldInfo

| 参数 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| caption | 字段显示名 | string | - |
| dataType | 数据类型 | string | - |
| type | 字段类型 | string | - |
| entityId | 实体主键ID | string | - |
