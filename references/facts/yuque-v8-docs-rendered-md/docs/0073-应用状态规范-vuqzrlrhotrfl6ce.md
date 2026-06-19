---
title: "应用状态规范"
source: "https://www.yuque.com/seeyonkk/v8/vuqzrlrhotrfl6ce"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 应用状态规范

> Source: https://www.yuque.com/seeyonkk/v8/vuqzrlrhotrfl6ce

规则：能用useReducer hook搞定的，请不要使用redux

低(逻辑复杂时)
复杂状态逻辑
REDUX风格
类以概念
集中管理
直接赋值
可维护性
代码组织
简单状态
USEREDUCER
适用场景
USESTATE
特性
分散
高
低

### 1.useReducer

对于状态较为简单的功能，请使用useReducer，使用方法参照官方文档：Hook API 索引 – React (docschina.org)

### 2.redux

对于复杂的页面，必须使用redux时，可使用它，在package.json中引用"react-redux": "8.0.2","redux": "4.2.0","redux-thunk": "2.4.1"

使用规范：不使用connet及mapStateToProps，统一使用useSelector，使用教程可参照Hooks | React Redux (react-redux.js.org)

### 3.业务组件中使用redux

当业务组件比较复杂时，或者原本是某个应用后来抽为业务组件(如bpm-run)，会用到redux，

但为了防止影响调用方，应使用自定义context，参考custom-context

```
// 自定义context
const MyContext = React.createContext(null)

// 后续调用useDispatch， useSelector都引用这里导出的，而不是react-redux库的
export const useStore = createStoreHook(MyContext)
export const useDispatch = createDispatchHook(MyContext)
export const useSelector = createSelectorHook(MyContext)
```
