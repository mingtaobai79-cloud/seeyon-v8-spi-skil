---
title: "web端和mobile端 快捷搜索组件"
source: "https://www.yuque.com/seeyonkk/v8/vv995gmo2i772pqg"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# web端和mobile端 快捷搜索组件

> Source: https://www.yuque.com/seeyonkk/v8/vv995gmo2i772pqg

快捷搜索组件，支持简单模式和展开模式

## 1.简单模式组件效果

192.168.1.4:3000/MAIN/PORTAL/KUOZHANUDCZUJIAN188041
金V分布式构建系统口DEVXTCV8文件夹
ZHANUDCZUJIAN1880413857437925691/YEWUYEWUZUJIANYONGFA
业务业务组件用法>
SEEYONV8
本之前的,口V8标品构建地址口V8环境口C(MP口金山中合口业务空间栏目
名称CCCCC请输
口V8心前端-掘金
别XXXX请
EASYMO
科技综合管理系统
公文管理
YY5请输.
YYY3请输
口所有书
文档当管理
名称CCCCC
请输入
Y4请输入
V请输入
YY7请选择
请输入
领导日程
会议管理
工资条
请选择
请选择
开发
YYY请输)
杨颜华
年龄
曲
日期
不安全
胎
重置
YYY6

## 2.简单模式组件用法

```
import { SimpleSearch, ExpandedSearch } from '@seeyon/biz-quick-search';

export default function CustomPage() {
  const fieldList = [
    { name: 'name', label: '名称ccccc', defaultValue: '涛涛', dataType: 'STRING' },
    { name: 'age', label: '年龄', defaultValue: 18, dataType: 'INTEGER' },
    { name: 'sex', label: '性别xxxx', dataType: 'BOOLEAN' },
    { name: 'xx', label: '日期', dataType: 'DATETIME' },
    { name: 'yyy', label: 'yyy', dataType: 'STRING' },
    { name: 'yyy2', label: 'yyy2', dataType: 'STRING' },
    { name: 'yyy3', label: 'yyy3', dataType: 'STRING' },
    { name: 'yyy4', label: 'yyy4', dataType: 'STRING' },
    { name: 'yyy5', label: 'yyy5', dataType: 'STRING' },
    { name: 'yyy6', label: 'yyy6', dataType: 'ENUM', enumCode: 'aaa' },
    {
      name: 'yyy7',
      label: 'yyy7',
      dataType: 'BIGINTEGER',
      fullName: 'com.seeyon.organization.domain.core.entity.OrgPost',
      appName: 'organization',
      entityName: 'OrgPost',
      ids: '-4428542449888116320',
    },
  ];

  return(<>
    <div>
      <SimpleSearch
        fieldList={fieldList}
        onSearch={(res) => {
          console.debug('onSearch', res);
        }}
        />
    </div>
  </>) 
}
```

## 3.展开模式组件效果

前满:据全分布式构建系统口DEVTK6文件夫V6时端资科及研发.18315板本之前的.白V0示品有建地址口V(环镇口MP口全U中
不安全192168.143000/MAIN/PORTA/KUOZHANUDCZUJAN1880413857437925691/YEWUYEWUZUJANYONGFA
V8OTHERSYSTEMYY
科技综合管理系统
口金山中台口业务空间栏目
广电合同系统0000000
业务业务组件用法
白文档当管理
SEEYONV8
>|口所有
旦公文管理
EASYMOCK
称CCCCC请输
Q品台4
YY3请输)
性别XXX请
工资条
YY7请选择
C不安全192.1
会议管理
完成更新
领导日程
YY请输入
YY2请输
8关闭全部
YYY请输)
船口V8
Y4请输入
龄请输入
~请输入
前
请选择
请选择
请输入
重置
请输入
重置
性别XXX
请输入
请输入
请选择
请选择
杨颜华
日期
请选择
开发
YYY4
YYY6
年龄
YYY5
文

## 4.展开模式组件用法

```
import React,{useState} from 'react';
import { SimpleSearch, ExpandedSearch } from '@seeyon/biz-quick-search';

 export default function CustomPage() {
   const fieldList = [
    { name: 'name', label: '名称ccccc', defaultValue: '涛涛', dataType: 'STRING' },
    { name: 'age', label: '年龄', defaultValue: 18, dataType: 'INTEGER' },
    { name: 'sex', label: '性别xxxx', dataType: 'BOOLEAN' },
    { name: 'xx', label: '日期', dataType: 'DATETIME' },
    { name: 'yyy', label: 'yyy', dataType: 'STRING' },
    { name: 'yyy2', label: 'yyy2', dataType: 'STRING' },
    { name: 'yyy3', label: 'yyy3', dataType: 'STRING' },
    { name: 'yyy4', label: 'yyy4', dataType: 'STRING' },
    { name: 'yyy5', label: 'yyy5', dataType: 'STRING' },
    { name: 'yyy6', label: 'yyy6', dataType: 'ENUM', enumCode: 'aaa' },
    {
      name: 'yyy7',
      label: 'yyy7',
      dataType: 'BIGINTEGER',
      fullName: 'com.seeyon.organization.domain.core.entity.OrgPost',
      appName: 'organization',
      entityName: 'OrgPost',
      ids: '-4428542449888116320',
    },
  ];
   
  return(<>
    <div>
      <ExpandedSearch
        fieldList={fieldList}
        sourceId="wyhhhhhhhhhhhhh3"
        onSearch={(res) => {
          console.debug('onSearch', res);
        }}
      />
    </div>
```

组件属性

| 参数 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| appName | 可选 |  | 'udc' |
| remoteComponent | 可选 |  |  |
| env | 可选 |  |  |
| fieldList |  |  |  |
| loading | 可选 |  | false |
| placeholder | 可选 |  |  |
| defaultSelectField | 可选 |  |  |
| value | 可选 |  |  |
| onSearch |  |  |  |
| style | 可选 |  |  |
| className | 可选 string |  |  |
| dynamicWidth | 可选boolean |  | false |
