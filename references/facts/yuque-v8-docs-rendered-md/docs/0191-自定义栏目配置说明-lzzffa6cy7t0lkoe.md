---
title: "自定义栏目配置说明"
source: "https://www.yuque.com/seeyonkk/v8/lzzffa6cy7t0lkoe"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 自定义栏目配置说明

> Source: https://www.yuque.com/seeyonkk/v8/lzzffa6cy7t0lkoe

作者：谢雨良

时间：2026年3月20日

## 一、配置位置

PORTAL#1@COM.SEEYON.PORTAL.DOMAIN.ENTITY.POR
MYBATIS
门I18N
GITKEEP
TENANT
门INIT
25
26

我们在自定义栏目中需要显示角标，此功能受portal#1@com.seeyon.portal.domain.entity.PortalPortletDefinition.json(文件路径：src\main\resources\init) 文件中属于你自定义栏目的countRule控制，同时你也可以在数据库portal_dev.portal_portlet_definition中count_rule字段中（数据库中的数据在你修改完成后及时生效，json配置文件需要你重启你自己的应用，重启应用会使json配置文件的配置覆盖数据库中的配置）

## 二、PortalPortletDefinition属性说明

portal#1@com.seeyon.portal.domain.entity.PortalPortletDefinition.json文件示例如下

```
[
  {
    "appId": "zzdtsxzxqwjs8154410761066857074",// 当前应用id
    "mobileAppId": "-1",
    "categoryCode": "zzdtsxzxqwjs8154410761066857074",
    "categoryPath": "-1/zzdtsxzxqwjs8154410761066857074",//空间布局中栏目路径，自定义栏目固定写 -1/categoryCode
    "definitionInfo": "......", //pc端栏目设置相关配置
    "mobileDefinitionInfo": "......",//移动端栏目设置相关配置
    "enableMobile": true, //移动端是否启用
    "enablePc": true, //pc端是否启用
    "exposeName": "zdyyf", //栏目编码
    "mobileExposeName": "",
    "id": "775256728418206324",
    "name": "zzdtsxzxqwjs8154410761066857074.zdydblm.caption",
    "portletId": "4691630219351715089",
    "sortNo": 2,
    "spaceTypes": null,
    "sysinit": false,
    "dataStatus": 1,
    "appCode": "zzdtsxzxqwjs8154410761066857074",
    "plugins": null,
    "defaultName": "自定义已发", //栏目名称
    "countRule": null, //角标配置
    "g_l_index": "1"
  }
]
```

##### 1、重要字段说明

| 属性名 | 说明 |
| --- | --- |
| definitionInfo | pc端栏目定义，包含栏目样式、管理配置、更多跳转配置。类型为json字符串 |
| mobileDefinitionInfo | 移动端端栏目定义，包含栏目样式、管理配置、更多跳转配置。类型为json字符串 |
| countRule | 栏目角标配置，包含角标查询接口，是否启用。类型为json字符。 |
| categoryPath | 栏目路径，影响空间中栏目选择的目录，必填，自定义栏目默认为"-1/${categoryCode}"(categoryCode与应用相关) |

##### 2、文件生成方法

PortalPortletDefinition中大部分参数由系统自动生成，需要修改的字段主要是definitionInfo、mobileDefinitionInfo和countRule，建议在udc应用中创建自定义栏目后，下载应用元数据，复制/backend/sxzxqwjs3463664424332642280-assemble/src/main/resources/init/portal@com.seeyon.portal.domain.entity.PortalPortletDefinition.json文件（路径以sxzxqwjs3463664424332642280应用为例），重命名为portal#1@com.seeyon.portal.domain.entity.PortalPortletDefinition.json，修改definitionInfo、mobileDefinitionInfo和countRule配置后(如果生成文件中没有categoryPath需要手动添加)，放在ext模块的src\main\resources\init目录下。

元数据下载链接见下图：

<img width="1140">

下载文件结构见下图：

<img width="560">

## 三、definitionInfo属性说明

## 四、countRule属性说明

##### 1、countRule是一个json字符串（配置在json文件中需要对字符串中的内容进行转义，配置在数据库时不需要转义）. json对象如下:

###### 1.1、通过集成获取角标

| 属性名 | 是否必填 | 说明 |
| --- | --- | --- |
| type | 是 | 传THIRD |
| countPluginId | 是 | 传集成方法的pluginId |
| countResField | 是 | 传角标返回值字段 ,例如data.content |

其他字段可不填

###### 1.2、通过接口获取角标

| 属性名 | 是否必填 | 说明 |
| --- | --- | --- |
| type | 是 | 传CUSTOM |
| countUrl | 是 | 请求地址，例如/ctp-affair/affair-center/select/section/category/by/data/get/count |
| method | 是 | 请求方法（get， post） |
| params | 否 | 请求参数（类型json对象）

key：countUrl请求地址的参数的key,

vlaue： 如果用${xx}包裹是动态参数,从栏目配置中读取或者从paramsMapping转换的数据中获取,例如 "${neironglaiyuan}";否者就是countUrl请求地址的参数的固定值 |
| paramsMapping | 否 | 请求参数映射,数组,将栏目配置做相应的转换 |
| 标准待办中${}参数说明 |  | - categoryInfo

 - 含义：角标接口的业务参数集合（数组）。

- categoryInfo[].identify

 - 含义：分类/栏目标识。

- categoryInfo[].categoryData

 - 含义：分类筛选数据（通常是栏目配置里的分类条件）。 |

说明：

```
例子:
{
"type": "CUSTOM",
"params": {
"neironglaiyuan": "${paramsMappingkey_1}",在paramsMapping中有对应的key,取paramsMapping转换后的paramsMappingkey_1
"xinwenfenlei": "${paramsMappingkey_2}",在paramsMapping中有对应的key,取paramsMapping转换后的paramsMappingkey_2
"param1": "${portletConfigKey1}",//在paramsMapping中没有对应的key,取栏目配置的portletConfigKey1
"param2": "66",//固定值
....
},
"method": "post",
"countUrl": "/billarchive2776130152975518413/portal/count-portal-news",
"countResField": "data.content",
"paramsMapping": [
{
"key": "paramsMappingkey_1",//对应params->neironglaiyuan
"value": "neironglaiyuan.value", //读取栏目配置 的neironglaiyuan 字段中的value字段的原始值
},
{
"key": "paramsMappingkey_2",//对应params->xinwenfenlei
"value": "xinwenfenlei.value",//读取栏目配置 的xinwenfenlei.value 字段中的value字段
"valueType": "string",//会将读取的值转换成string类型, 如果不用转换类型可不填
},
...
]
}
```

## 五、系统中配置

重启应用或者直接在数据库中设置，配置生效后，我们添加栏目或者编辑栏目时，可以看到“显示统计数”配置，打开“显示统计数”开关并保存栏目配置

编辑组合栏拦目
显示名称是
显示名称请输
显示高度300
添加栏目
基本信息
#7CA3A3
栏目名称待办事
待办事顶
图标颜色
册删除栏目
显示统计数
编辑栏目
女交马
办事项
100%%
图标
图标
图片
布

或者进入设计个人空间

[已读]全文检索测词
电峰公文管理2026-03-0609:2
[未读]收文分发确认0306.1
最近缺卡记录:2026-03-18
今天上班辛苦了,别忘记打
电峻峰公文理2026-03-0609:21
[已读]SSSS
谢雨良科技支综合管理系统20
检测到核栏目已更新,
谢雨良流程中心2025
快到上班时间了,别忘了打卡
最近缺卡记录:2026-03-1
快到上班时间了,别忘了打
近缺卡记录:2026-03-1
[未读]收文办理成0202.5
最缺卡记录:2
科技综合管理系统
部标记为已读
V8OTHERSY..
高度自适应显示
现新版本
2026-03-1115:
天上班幸苦了,
12:00上班卡
考琴异常处
8:00下班卡
考勤异常处理
基本信息
,别忘记打
点击设置内容
18:00下班卡
待办事项
栏目显示含
2026-0319
待办事项
内容设置
待办项V
考勤异常处理
考勤异常处理
显示统计姿
领导日程
图标
办事项
栏目名称
12:00上班卡
暂无数据
班卡哦~
数据范围
显示名称
班卡哦
14:03
18:05
示高度
03-18
图标
03-18
图片
300
已办事项
,是否更新最新内容
14:03
23:00
买
请输入
昨天
02:03
03-18
0759
昨天
11:5
昨天
样式
80
..一.
你
昨天
是
内容
昨天
哦~
品
用~
更新
A
0
O
