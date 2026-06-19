---
title: "前端常用组件整理及api"
source: "https://www.yuque.com/seeyonkk/v8/bgg5pklzervvnndm"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 前端常用组件整理及api

> Source: https://www.yuque.com/seeyonkk/v8/bgg5pklzervvnndm

作者：杨颜华
最后更新：2025-07-28

## 1.人员头像组件调用

```
import {getCurrentUser} from '@seeyon/global'
import { Avatar } from '@seeyon/biz-avatar';

const currentUser = getCurrentUser();

<Avatar 
            key={currentUser.userId}
            reqKey={currentUser.userId}
            type="user"
            id={currentUser.userId}
            iconName="LinedUser"
            size={24}
            label={currentUser.userName}
          /> 
```

## 2.选人组件调用

```
import { OrgSelectorInput } from '@seeyon/biz-org-selector';

<OrgSelectorInput
              key="1"
              options={{
                mode: 'custom',
                maxCount: 100,
                distinct: false,
              }}
              selectType ={['MEMBER','DEPARTMENT']}
            />
```

3.加载远程模块的调用

```
import React from 'react';
import { RemoteLoader } from '@seeyon/global';

const Index = () => {
  return (
    <>
      <h1>hello world!</h1>
      <RemoteLoader
         // 唯一标识
        key="leaderBoard"
        // 应用名称
        appName="schedulemanagement1879887445425932710"
        // 页面名称
        module="leaderBoard"
        // 要给目标页面传哪些 props
        pageProps={{
          userName: '111',
        }}
      />
    </>
  );
};

export default Index;
```

## 3.页面跳转

```
import {  useSyHistory } from '@seeyon/global';
const history = useSyHistory();
history({
            url: '/organization/extra/onlineAddressBook/pc',
            isNewTab: true,
            tabTitle: i18n.t({ k: 'portalFrame.other.online_member', d: '在线人员' }),
          });
```

## 4.国际化

import { i18n} from "@seeyon/global";

const i18nPrefix = "xhdxkfzyy7882320728204987658.pc.xihudaxuemenhu.grkp."; // 国际化前缀

i18n.t({ k: i18nPrefix + "xqxxts", d: "日程功能请下载i西湖APP使用!" })

## 5.如何查看并使用V8前端图标库

https://pre.seeyonv8.com/seeyon/main/backstageManage/app-common/system/iconLibrary

注意：用哪个环境就把main前面的替换一下

## 6.UDC应用里面的自定义页面注意点

1.目前不支持通过yarn add/npm install方式下载第三方依赖方式引入插件到自定义页面，只能通过cdn或者将依赖下载本地，相对路径的方式引入来进行验证

pc.zip
(686 KB)

## 7.扩展工程的注意事项

在有外网的前提下 可以通过yarn add方式引入第三方依赖，引入三方依赖的前提建议参考标品是否有支持对应插件引入就无需再次下载引入。

## 8.UI组件库

http://ui.seeyonv8.com/dev/pc

备注：该地址需要登录vpn才能访问，外网可参考访问：ant design react官网  https://4x-ant-design.antgroup.com/docs/react/introduce-cn/

我们UI组件库是基于antd库进行二次封装，加了些功能，跟官网原有组件功能不一致。

## 9.查看当前环境的沙箱版本号

前置条件 需要先登录OA环境，再开一个新的页签输入 环境ip+/service/app-sandbox/monitor/jar-info 查询当前环境的沙箱版本号

<img width="1312">

## 10.查询当前环境前端组件的版本号（不对外后期会变更，便于问题排查）

OA版本：3.15及以上版本： 前置条件 需要先登录OA环境，再开一个新的页签输入

ip+端口+/libs/5_0_versions.json 这个地址查询当前环境的前端组件版本号

## 

## 10.查询当前环境前端组件的版本号

ip+端口+/libs/businesses.json

<img width="1120">

## 11.扩展工程产物不生效可以执行更新接口

3.2版本刷新main/index.html文件接口  /service/app-common/i18n/refresh-index

## 12.移动端修改头部区标题

window.jsSdk.router.setNavTitle({title: '西湖大学'})//修改头部区的标题

## 13.查询服务的版本号：

/service/app-doc/metadata/online-app-info

<img width="1164">

## 14.更新元数据

/service/app-common/metadata/upgrade?appName=app-doc

## 15.标品组件清单目录

https://docs.qq.com/sheet/DQ2RISEdBQ29UeFhE?tab=re0r1f

## 16.udc应用里面的手页页面支持国际化

<img width="1528.8">

<img width="1360">

<img width="736.8">

## 17.公文应用对应的graphql地址

/service/edoc335172694483814428/graphql/doc.html

<img width="1344">

<img width="1536">

## 18.浏览器上查看模块的版本

http://10.101.68.14/app-doc-mobile/version.json

<img width="556">
