---
title: "模块联邦(MF)使用指南"
source: "https://www.yuque.com/seeyonkk/v8/lygy35gzmgg4xaqf"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 模块联邦(MF)使用指南

> Source: https://www.yuque.com/seeyonkk/v8/lygy35gzmgg4xaqf

在微前端架构中，各个前端应用之间是独立部署和维护的，应用和应用之间是源代码隔离的， 设想如果某个应用需要调用另一个应用的功能，比如需要在流程中心打开一个UDC的应用发布弹窗，此时我们可以通过模块联邦使流程中心直接加载UDC的发布弹窗组件。

模块联邦需要调用方和提供方就导出的模块达成协议，提供方可以暴露整个应用，也可以单独只暴露出一个页面的组件，这取决于你的设计

#### 1
配置导出模块

在调用方调用具体组件之前，提供方需要在其webpack-overrides.js中进行如下配置

```
// 主应用通过模块联邦的方式导出组件库供login等页面使用
module.exports = function (config, env) {
  const moduleFederationPlugin = config.plugins.find(
    (p) => p.constructor?.name === 'ModuleFederationPlugin',
  );

  moduleFederationPlugin._options.exposes['./SeeyonUI'] = './src/ui/index.tsx';

  return config;
};
```

#### 2
调用方式

通过RemoteLoader加载

RemoteLoader是由@seeyon/global提供的模块联邦加载器，其常用于加载UDC搭建应用某个页面的场景，在UDC搭建应用中每个搭建的页面都可通过模块联邦的方式直接已React组件的方式引用，RemoteLoader的具体参数请参考: 运行时上下文 global 使用指南

```
export default function SubPage({
  appName,
  pageName,
  subPageInParams,
  ...rest
}: {
  appName: string;
  pageName: string;
  subPageInParams: any;
}) {
  const uniqueKey = `${appName}/${pageName}`;

  return (
    <div>
    <RemoteLoader
      uniqueKey={uniqueKey}
      appName={appName}
  pageName={pageName}
  pageProps={{
    ...rest,
    inParams: subPageInParams,
  }}
/>
  </div>
);
}
```
