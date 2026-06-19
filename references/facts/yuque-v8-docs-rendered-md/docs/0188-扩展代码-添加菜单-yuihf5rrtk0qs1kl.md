---
title: "扩展代码-添加菜单"
source: "https://www.yuque.com/seeyonkk/v8/yuihf5rrtk0qs1kl"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 扩展代码-添加菜单

> Source: https://www.yuque.com/seeyonkk/v8/yuihf5rrtk0qs1kl

使用场景：在UDC设计态以外的菜单，按项目需要增加一级菜单，及其下面的二级菜单，会注册进菜单和工作台中

# 实现场景举例：

标品中的日程管理应用：

<img src="https://cdn.nlark.com/yuque/0/2025/png/50254821/1753771143588-677f4faa-d45f-4581-9fd3-16c7de3e007f.png" width="613">

<img src="https://cdn.nlark.com/yuque/0/2025/png/50254821/1753771143466-199783a7-53aa-4bc9-b532-7a438fac2121.png" width="613">

<img src="https://cdn.nlark.com/yuque/0/2025/png/50254821/1753771143516-cc515ae9-6443-4f4a-a824-56b75eb6e348.png" width="613">

<img src="https://cdn.nlark.com/yuque/0/2025/png/50254821/1753771143686-ac0f81e8-a6a3-4cfa-8f9a-0b760f1e803e.png" width="613">

# 实现方式：

实现方式说明：

在UDC应用构建后，系统会生成菜单注册的相关代码，通过在注册菜单的代码中加入自己需要的额外的一级菜单及下级菜单来实现添加额外菜单

后端代码目录位置和图示说明：

<img src="https://cdn.nlark.com/yuque/0/2025/png/50254821/1753771143696-dcef4214-268c-4d44-b81e-0ad6783c4c19.png" width="613">

## 重要字段说明：

### id、code：

用途：要引用的菜单资源id和code

获取方式：

数据库查询示例：

SELECT * FROM `ctp_user_dev`.`ctp_resource` where `name` like '菜单名称' and path = '' and data_type = 'other'

注意：后面的条件是为了去区分菜单，不能去掉，系统中同名称菜单至少都有2个

这里以【秘书用领导日程】举例，同CODE的不同ID菜单资源都是存在的，用错了菜单是没用的

<img width="613">

### parentId:

用途：上级菜单ID

获取方式：去看代码里面其他菜单结构，1级菜单不用录入，2级往下的找已有的菜单id

### level：

用途：菜单级次

获取方式：按当前要添加菜单的级次录入即可

### path：

用途：添加的菜单的路径地址

获取方式：基于上面获取的id和上级菜单id自己拼

### url：

用途：菜单打开地址

获取方式：通过UDC设计态对页面右键属性获取

### urlParameters：

用途：菜单打开地址附加参数

获取方式：视实际使用场景而定，一般不赋值

### openType:

用途：菜单的打开方式

获取方式：看其他菜单的打开方式，也可以自己定义

### sortNumeber:

用途：排序号，控制同级菜单的前端页面展示排序

获取方式：按需配置

### appId：

用途：应用绑定逻辑字段

获取方式：参照JSON文件下的其他菜单

# 代码示例：

{
  "validate": true,
  "id": -983994601175823950,
  "code": "4731464887532206939",
  "name": "查看领导日程",
  "icon": "",
  "parentId": 7653571467689150164,
  "level": 2,
  "path": "7653571467689150164.4731464887532206939",
  "url": "/schedulemanagement1879887445425932710/leaderAgendaWebForSec",
  "urlParameters": "",
  "openType": "WORKSPACE",
  "admin": false,
  "allowEnd": false,
  "sortNumber": 99,
  "appId": "schedulemanagement1879887445425932710",
  "entityFullName": "",
  "appType": "BASIC",
  "frontendAppId": "schedulemanagement1879887445425932710",
  "origin": "SYSTEM",
  "type": "MENU",
  "dataType": "",
  "clientType": "PC",
  "referId": -1,
  "referAppId": "",
  "objectId": -1,
  "dataStatus": 1,
  "groupId": null,
  "plugins": "schedulemanagement1879887445425932710leader",
  "packageTime": 0
}
