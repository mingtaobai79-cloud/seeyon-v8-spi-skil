---
title: "web端和mobile 选人组件"
source: "https://www.yuque.com/seeyonkk/v8/sfets6yi6ugnp5sf"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# web端和mobile 选人组件

> Source: https://www.yuque.com/seeyonkk/v8/sfets6yi6ugnp5sf

## 1.业务场景

调用组织机构数据, 通过弹窗选择人员、业务线、机构、部门、岗位、职务、职级等数据。

## 2.OrgSelector参数说明

### 2.1 公共参数 && 类型定义

OptionsType

| 参数 | 说明 | 类型 | 默认值 | 版本 |
| --- | --- | --- | --- | --- |
| includeData | 白名单 | Partial<Record<IncludeExcludeType, string>> | - | - |
| excludeData | 黑名单 | Partial<Record<IncludeExcludeType, string>> | - | - |
| showDisable | 是否支持搜索停用人员 | boolean | - | - |
| tenantId | 选人组件的租户 ID | string | - | - |
| mode | 选人组件常用场景的默认配置 | MODE | - | - |
| tabs | tabs 页签 | (TABS \| TabsLiteral)[] | - | - |
| selectType | 可选数据类型 | SelectType[] | - | - |
| valueType | 组件返回数据类型 | ValueType | - | - |
| jsonify | 组件返回和接收的数据是否先经过 JSON.stringify/JSON.parse 转换 | boolean | false | - |
| maxMember | 最多可选人数 | number | 无限制 | - |
| maxCount | 最多可选多少条数据 | number | - | - |
| businessId | 部门页签选中的业务线 id | string | - | - |
| allowSwitchBusiness | 部门页签是否允许切换业务线 | boolean | - | - |
| ocipOrgViewId | 指定 ocip 组织视图 | string | - | - |
| allowSwitchOcipOrgView | 是否允许切换 OCIP 组织视图 | boolean | - | - |
| institutionId | 机构树下拉框选中的机构 id | string | - | - |
| allowSwitchInstitution | 机构树下拉框是否允许切换机构 | boolean | - | - |
| showWorkflowRadio | 流程模式是否显示底部切换串发/并发的 Radio | boolean | - | - |
| flowOptions | 流程模式下控制底部 Radio 选项 | WORKFLOW_TYPE[] | - | - |
| groupId | 流程模式-流程参数列表获取数据所需的 groupId | string | - | - |
| clearCacheOnClose | 关闭弹窗时是否清除已缓存的业务线、组织树数据和选中状态 | boolean | - | - |
| distinct | 部门下的人员, 一个人可以有多个任职 | boolean | - | - |
| permission | 选人组件的数据访问权限 | PermissionType | - | - |
| secretLevel | 人员密级 ID | string | - | - |
| includeChildren | 根据页签控制是否包含下级 | IncludeChildren | 混选模式机构、部门、多维组织、流程变量、外部单位页签默认开启 | - |
| customTabs | 自定义页签 | CustomTab[] | - | - |
| customMenus | 自定义菜单用于放自定义页签 | CustomMenu[] | - | - |
| multiOrgId | 指定多维组织 ID | string | - | - |
| outsideUnitId | 指定外部单位 ID | string | - | - |
| allowSwitchMultiOrg | 是否允许切换多维组织 | boolean | - | - |
| linkElement | 放到左下脚的链接 --- 问题上报 | React.ReactElement | - | - |
| onCurrentInstitutionChange | 当前机构变化时的回调 | (institution?: DataType) => void | - | - |
| range | 范围 | Range | - | - |
| spAccountType | 特殊账户类型 | 'VISITOR' \| 'DEVICE' \| 'ROBOT' \| 'ADMINISTRATOR' \| 'GUEST' | - | - |
| design | 设计 | boolean | - | - |
| appId | appId | string | - | - |
| roleTypes | 角色类型 | RoleType[] | - | - |
| onlyInstitutionBranch | 是否只允许选择机构下的人员 | boolean | - | - |
| maxLevel | 最大层级 | number | - | - |
| appointRootIds | appointRootIds | string | - | - |
| appointRootIncludeChildren | appointRootIncludeChildren | boolean | - | - |
| showCurrentNode | bpm 那边使用是否展示当前节点 | boolean | - | - |
| disableFlowNode | 流程节点列表不能选择的节点 | string[] | - | - |
| hideFlowNode | 流程节点列表隐藏的节点 | string[] | - | - |
| updateValueInfo | 是否更新已选择数据的最新数据 | boolean | - | - |
| selectOutsideUnit | 开启选择外部单位 | boolean | - | - |
| selectOutsideMember | 开启选择外部人员 | boolean | - | - |
| unitMemberCheckLevel | 单位下是否有成员的检测级别 | UnitMemberCheckLevel | - | - |
| memberDeduplicate | 选人模式，是否需要去重 | boolean | - | - |
| customDataSource | 自定义数据源 | DataType[] | - | - |
| alwaysShowIncludeChildren | 是否不检测根机构匹配，始终弹出包含下级角色提示框 | boolean | - | - |
| authorizedIncludeSwitch | 授权模式是否开启包含下级 | boolean | - | - |
| disableMemberGroupAction | 是否隐藏保存个人组操作 | boolean | - | - |
| trigger | 自定义触发方式 | SupportSelectTriggerEventType \| SupportSelectTriggerEventType[] | - | - |
| theme | 主题风格 | { type: ThemeType; config?: ThemeConfig; } | - | - |
| allowedRoleTypes | 允许的角色类型 | AllowedRoleType[] | - | - |
| draggable | 是否支持拖拽 | boolean | - | - |
| showRecentTabWhenNotIncludedInFront | 当页签中不包含常用页签时是否默认在前台显示常用选项卡 | boolean | true | - |
| includeFlowNodes | 流程节点白名单，后端根据此列表进行数据过滤 | string[] | - | - |
| disableFlowNode | 流程节点列表不能选择的节点 | string[] | - | - |
| hideFlowNode | 流程节点黑名单，前端根据此列表进行数据过滤 | string[] | - | - |
| resolveUserOrgTree | 解析人员机构树配置 | resolveUserOrgTreeConfig | - | - |
| flowSourceDepth | 流程模式中，源数据层级，即多少列 | number | 5 | - |

类型定义&使用示例

流程节点配置

使用示例：

类型定义：

解析人员机构树配置：resolveUserOrgTreeConfig

包含下级配置：IncludeChildren

MODE

TABS

TabConfigs

IncludeExcludeType

ValueType

WORKFLOW_TYPE

PermissionType

CustomTab

CustomMenu

AllowedRoleType && RoleType

SupportSelectTriggerEventType

UnitMemberCheckLevel

DataType

ThemeType

OrgSelectorInstance

ThemeConfig

### 2.2 弹窗式选人组件

默认的选人组件，弹窗由组件提供

| 参数 | 说明 | 类型 | 默认值 | 是否必填 | 版本 |
| --- | --- | --- | --- | --- | --- |
| visible | 选人界面是否显示 | boolean | false | 是 | - |
| onClose | 点击关闭、取消、遮罩层的回调 | () => void | - | 是 | - |
| value | 选择器的值 | ValueTypes | - | 否 | - |
| onOk | 点击确定时的回调 | (value: ValueTypes, full: ValueWithName[]) => void | - | 是 | - |
| _onOk | 通过 Input 模式调用时内部使用的回调函数 | (data: DataType[], confirm?: boolean) => void | - | 否 | - |
| options | 配置项 | Partial | - | 否 | - |
| modalProps | Modal 组件 props | ModalProps | - | 否 | - |
| onGetInstance | 获取选人组件实例方法与属性 | (instance: OrgSelectorInstance) => void | - | 否 | - |

### 内嵌式选人组件

选人组件的嵌入模式，仅提供内容区，外层容器（如：Modal）由调用方提供，目前 BPM 流程多分支条件使用较多

| 参数 | 说明 | 类型 | 默认值 | 是否必填 | 版本 |
| --- | --- | --- | --- | --- | --- |
| className | CSS 类名 | string | - | 否 | - |
| onSelect | 选中数据时时的回调 | (value: DataType[]) => void | - | 否 | - |
| onChange | 已选数据发生变化时的回调 | (value: DataType[], triggerType?: TOnChangeReferenceType) => void | - | 否 | - |
| hideInstitutionSelector | 是否隐藏机构选择器 | boolean | - | 否 | - |

对外暴露的ref信息

| 参数 | 说明 | 类型 | 默认值 | 是否必填 | 版本 |
| --- | --- | --- | --- | --- | --- |
| getModalFooter | 获取模态框的页脚 | () => React.ReactNode | - | 是 | - |
| afterCloseAnimation | 关闭动画结束后的回调 | () => void | - | 是 | - |
| handleOk | 点击确定时的回调 | () => Promise | - | 是 | - |
| onCancel | 取消时的回调 | () => void | - | 是 | - |
| setTargetList | 设置目标列表 | IMmutableContextType['setTargetList'] | - | 是 | - |
| removeTarget | 移除目标 | IMmutableContextType['removeTarget'] | - | 是 | - |
| appendTarget | 追加目标 | IMmutableContextType['appendTarget'] | - | 是 | - |
| setSelectedTarget | 设置选中目标 | IMmutableContextType['setSelectedTarget'] | - | 是 | - |
| setSelectedSource | 设置选中源 | IMmutableContextType['setSelectedSource'] | - | 是 | - |
| selectedTarget | 选中的目标 | MutableContextType['selectedTarget'] | - | 是 | - |
| selectedSource | 选中的源 | MutableContextType['selectedSource'] | - | 是 | - |

## 3.PC端实际用法

## 4.移动端 组件
