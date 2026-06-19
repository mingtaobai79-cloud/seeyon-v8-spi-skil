---
title: "前端目录结构和编码规范"
source: "https://www.yuque.com/seeyonkk/v8/iukuczgt2cv98t0z"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 前端目录结构和编码规范

> Source: https://www.yuque.com/seeyonkk/v8/iukuczgt2cv98t0z

### 1
目录结构

以实际项目为准，以下为常用目录：

- assets 为静态资源目录，有 images、styles、fonts 等，代码别名为：assets；

- static 为runtime静态资源目录，有 images、styles、fonts 等，与assets区别是不参与spa bundle打包；

- components 为通用组件目录，代码别名为：components；

- constants 为常量目录，代码别名为：constants；

- containers 为容器组件目录，代码别名为：containers；

- pages 为各模块主目录，各模块下可以有业务组件、业务常量等，代码别名为：pages；

- redux 为状态管理的目录，有 actions、reducers 和 store 目录，代码别名为：redux；

- services 为接口的目录，代码别名为：services；

- utils 为工具函数，代码别名为：utils；

- models 为复杂数据初始化目录，代码别名为：models；

- i18n 为国际化词条目录。

应用名称规范：小写字母，单词连接使用中横线，如ctp-user

目录/文件规范：小写字母，单词连接使用中横线，如：portal-layout

css命名规范：小写字母，单词连接使用中横线，如：.menu-item-li

国际化词条命名规范：驼峰，如：{portalFrame:{topTitle:''}}

别称在tsconfig.json中定义

webpack-overrides.js为本地开发时的配置，所有代码规则必需写在if(env === 'development')，不然会影响线上环境。

### 2
React编码规范

#### 2.1
依赖引用

1、第三方组件：

●
严格控制第三方组件的引用，syf脚手架中会检测第三方库，对于不合理的第三方库会不允许构建成功；

●
moment、lodash等第三方库：不允许使用moment，基础组件中会集成dayjs，如需使用请引用dayjs，不允许直接使用lodash，如必要，请使用lodash-es；

●
redux状态管理，请使用redux、react-redux、redux-thunk，不允许使用其它状态管理库；

●
第三方库的版本
"react": "18.2.0",
"react-dom": "18.2.0",
"react-router-dom": "5.3.0",
"react-redux": "8.0.2",
"redux": "4.2.0",
"redux-thunk": "2.4.1"

●
仅开发过程中需要的组件，安装进devDependencies

2、seeyon系列的组件：

1
版本：根据当前开发的分支进行引用，如当前开发的分支为release/5.2-release_20250715，则引用的@seeyon组件也必须是"~5.2.x"。

2
react、redux、antd、ui或mui均已集成进主应用，由主应用控制，各应用无需要关心它们的版本，直接在运行时上下文使用。

3
编码：

4
入口文件：src/entry.tsx和app4Exposes.tsx由脚手架生成，不要修改它们，也无需要提交，可加入.gitignore中；

5
引用简化：请使用别称，如：import App from '@pages/app';

6
使用@seeyon/global中的公共方法，如：eventOn、eventEmit、eventOff、whereConvert2Sql、Cookies、security、nanoid、storage、ajax、apollo、error、queryLoader、mutationLoader、createLoader、getRequestByAppName、getCurrentUser、setCurrentUser等，不要自己造轮子。
具体API可参考seeyon-global；

7
不允许production代码中存在console.log，前端框架会统一屏蔽掉console，哪果想使用它，请在localStorage 中设置 _debugger: 0

8
React.lazy：这是一把双刃剑，拆得粗会导致加载多余的代码，拆得过细会导致打包后文件又多又小，请遵守一个UI页面一个React.lazy的规则，把打包数量与体积合理平衡，一般要求首屏单组件体积<50KB；

9
抽取公共资源：两处及以上使用的代码请抽取出来，避免重复代码，优秀的工程，src/utils下应该有不少公共方法；

10
不吝注释：优秀的程序员注释都非常清晰；

11
不使用class，使用function components + hooks，状态管理尽量简化，userReducer hooks能搞定的问题就不要使用redux库；

12
静态代码扫描：请及时修改SonarQube (seeyonv8.com)上的bug、阻断、漏洞等。

### 3
Lint规范

通过syf创建的工程会强制使用eslint插件，当校验不通过时不允许提交，lint规范包含100多项，请严格按照ide中eslint规则修改，对于不合理的代码是无法提交成功的。
