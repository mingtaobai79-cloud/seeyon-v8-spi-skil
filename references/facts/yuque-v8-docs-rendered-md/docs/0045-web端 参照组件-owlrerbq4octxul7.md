---
title: "web端和mobile端 参照组件"
source: "https://www.yuque.com/seeyonkk/v8/owlrerbq4octxul7"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# web端和mobile端 参照组件

> Source: https://www.yuque.com/seeyonkk/v8/owlrerbq4octxul7

```
 import Reference from '@seeyon/ui';
 
 <Reference
      fullName="com.seeyon.organization.domain.core.entity.OrgPost"
      appName="organization"
      entityName="OrgPost"
      // 
      onChange={(value) => {
        console.debug('', value);
      }}
     value={onChange}
    />
```

组件属性

| 参数 | 说明 | 类型 | 默认值 | 必填 |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| applicationName | 当前应用名 | STRING | 是 | udc | 从哪里应用获取服务，设计态传udc，运行态传发布后应用名 |  |
| appName | 关联实体所属应用名 | STRING | 是 | - | 实体所属应用名 |  |
| fullName | 关联实体名 | STRING | 是 | - | 实体注册到元数据中心的fullName |  |
| entityName | 关联实体编码 | STRING | 是 | - | - |  |
| value | 选中数据 | [{id: 'xx', xx: 'xx'}] | 是 | - | onChange回掉返回的数组，和ids逻辑相斥 |  |
| extraSearchParam | 动态查询条件 | Record<string, any> | × | - | {
    and:{
        ${操作符}_${实体编码}_${字段编码}: 值
    },
}

demo:

{
 and:{
        GE_Shuxingdangan_secretId: 20
    }
} | v3.9 |
| remoteComponent | 模块联邦 |  | - | - | v2.7开始不需要了 | v2.7 废弃 |
| referFullName | 指定参照方案fullName | STRING | × |  | 默认用实体下默认参照方案 |  |
| multiSelect | 是否多选 | BOOLEAN | × | - | - |  |
| disabled | 是否置灰 | BOOLEAN | × | false | - |  |
| readonly | 只读状态 | BOOLEAN | × | false | 只读只渲染已选数据的纯文本，不会渲染控件 |  |
| onChange | 回掉函数 | () => {} | 是 | false | - |  |
| onClick | 点击参照按钮回调 | () => {} | × | false | - |  |
| onClose | 关闭参照弹窗回调 | () => {} | 是 | false | - |  |
| styles | 样式 |  | × | - | 自定义样式 |  |
| ids | 已选数据的ids,用作回显数据 | STRING | × | - | value数组每条数据的id

ids = value?.map((item) => item?.id).join(',') |  |
| placeholder | 占位名 | STRING | × | - | - |  |
| debounceTimeout | 防抖时间 | Number |  | 800 | - |  |
| extraOutputFileds | 额外需要返回字段 | [] |  | [] | [{name: 'xx'}] |  |
| referFullName | 指定参照方案fullName | STRING | × | - | 没有的话用实体下默认参照方案 |  |
| defaultRefernceData | 默认参照方案，不建议用了 | DataReferenceType | - | - | 参照方案需要数据恢复，从元数据中心取出来的参照方案是精简版本，只有字段id，建议用referFullName |  |
| isShowDeleteIcon | 是否渲染删除按钮 | BOOLEAN | - | true | - |  |
| openMode | 展示方式 | STRING |  | - | undefined \| 'directlyShow' \| 'modal' 

undefined：标准参照样式 下拉选择框

directlyShow：只有弹窗内容 无下拉选择框

modal：弹窗样式 无下拉选择框 |  |
| directlyShowPlaceholder | 直接展示参照内容时，未获取到参照方案数据时展位文字 | STRING | - | 未获取到参照方案 | - |  |
| fullDefaultRefernceData | 默认参照方案 | DataReferenceType |  |  | 补全后的参照方案 |  |
| enableDetailPage | 是否可跳转详情页 | BOOLEAN |  | true | 参照方案有详情页时 控制是否可以跳转详情页 |  |
| resourceSecretId | 页面资源密级 | STRING |  |  | 需要进行资源密级过滤时传递

页面资源密级获取方式：

const [resourceSecretId] = udcSdk.getUdcPageSecretId({

runtimeContext: props.runtimeContext,

dataTarget: props.dataTarget

}); | v5.5 |
|  |  |  |  |  |  |  |

interface DataReferenceType

| 属性 | 说明 | 类型 | 默认 | 是否必填 |
| --- | --- | --- | --- | --- |
| caption |  | string |  | 否 |
| configInfo |  | string | radio | 否 |
| detailPage |  | string[] |  | 否 |
| displayName |  | string |  | 否 |
| terminalType |  | string[] |  | 否 |

完全自行控制外部的触发控件渲染逻辑， 以下是示例代码

mobile端
