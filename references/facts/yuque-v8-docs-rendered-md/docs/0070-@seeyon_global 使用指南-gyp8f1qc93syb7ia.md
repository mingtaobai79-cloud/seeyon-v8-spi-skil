---
title: "@seeyon/global 使用指南"
source: "https://www.yuque.com/seeyonkk/v8/gyp8f1qc93syb7ia"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# @seeyon/global 使用指南

> Source: https://www.yuque.com/seeyonkk/v8/gyp8f1qc93syb7ia

在运行时上下文已经提供了如下全局公共组件或方法，子应用或组件可以直接使用：

### 1.常用方法

图标库 SyIcon

系统偏好配置 systemConfig

国际化初始化 i18n

事件发布 eventEmit

事件订阅 eventOn

系统变量 getSystemVariable

AJAX封装 ajax

日期时间库 dayjs

链接 SyLink

打开页签 useSyHistory （主要是在门户多页签模式下调用）

关闭页签 CloseWindow

页面打印 print

页面打印上下文配置 PrintContext

打印前事件回调 addBeforePrintCallback

动态脚本加载 useDynamicScript

远程模块加载 RemoteLoader

基于发布订阅的事件总线 EventBus

一次性事件订阅 eventOnOnce

事件取消订阅 eventOff

事件发布异步结果回调 eventEmitAsyncResult

事件广播 eventEmitBroadcast

事件订阅hooks  useEventOn

获取nanoid算法封装 nanoid

浏览器Storage存储方法封装 storage

GraphQL封装 GraphqlLoader

获取当前用户信息 getCurrentUser

显示全局加载态 showLoading

关闭全局加载态 hideLoading

获取websocket服务地址 getWsServer

创建websocket实例 WebsoketServer

### 2.文档明细

## 组件

### NotFoundPage

一个 React 组件，显示“页面未找到”的消息。

Props:

●
description: (可选) 一个要显示为描述的字符串或数字。默认为“页面找不到了，重新加载或返回首页.”。

●
notFoundNode: (可选) 一个 React 节点、字符串或 null，用作未找到页面的主要内容。默认为一张图片。

### SyLink

一个用于创建导航链接的 React 组件。它是 <a> 标签的包装器，用于处理应用内导航、打开新标签页和传递参数。

●
url: string: 链接的目标 URL。

●
children: any: 要在链接中显示的内容。

●
params?: Record<string, any>: 传递给目标路由的参数对象。

●
callback?: () => void: 导航完成后执行的函数。

●
isNewTab?: boolean: 如果为 true，链接将在新的浏览器标签页中打开。默认为 false。

●
tabTitle?: string: (已弃用) 新标签页的标题。被打开的页面应自行设置标题。

●
className?: string: 应用于链接的 CSS 类。

●
isReplace?: boolean: 如果为 true，历史堆栈中的当前条目将被替换。默认为 false。

●
updatePathNameBeforeChange?: boolean: 一个在更改前更新路径名的标志。

### useSyHistory

一个 React 钩子，提供以编程方式进行导航的方法。

返回:

●
(options: Omit<SyLinkModel, 'children'>) => void: 一个函数，调用时将执行导航。它接受 SyLink 的所有 props，除了 children。

### openTabLink

一个包含导航核心逻辑的函数。SyLink 和 useSyHistory 都使用它。

参数:

●
options: pushStateModel: 一个包含以下属性的对象：

○
currentHistory: any: 来自 react-router-dom 的 history 对象。

○
currentRoute?: any: 当前的路由对象。

○
url: string: 目标 URL。

○
isNewTab?: boolean: 如果为 true，则在新标签页中打开。

○
tabTitle?: string: (已弃用) 新标签页的标题。

○
params?: Record<string, any>: 新路由的参数。

○
isReplace?: boolean: 如果为 true，则替换当前的历史记录条目。

○
updatePathNameBeforeChange?: boolean: 一个在更改前更新路径名的标志。

○
menuKey?: string: 目标路由的菜单键。

○
forceNoNew?: boolean: 如果为 true，即使 isNewTab 为 true，也不会打开新标签页。

○
tabControl?: boolean: 一个控制标签页行为的标志。

○
callback?: () => void: 导航后调用的函数。

### SyRouter

一个自定义的路由器组件，包装了 react-router-dom 的 Router。当应用程序在离线环境中运行时，它使用 HashRouter，否则使用 SyBrowserRouter。SyBrowserRouter 是一个扩展了 React.Component 的自定义实现，提供了一种使用生命周期钩子管理应用程序路由的方法。

●
appName: string: 应用程序的名称，用于标识路由器实例。

●
basename: string: 所有位置的基础 URL。

### setSyRouterLifeCycle

一个为 SyRouter 设置全局生命周期的函数。这允许“主”应用程序控制所有使用 SyRouter 的路由器的行为。

●
lifeCycleConfig: GlobalRouterLifeCycleType: 一个定义生命周期钩子的对象。钩子包括：

○
shouldStopBackRender?(routerInfo: SyBrowserRouterInfoType, location: Location, action: Action, renderFn: Function): boolean: 当用户向后导航时调用的函数。它可以通过返回 false 来阻止渲染。

○
beforePushRender?(routerInfo: SyBrowserRouterInfoType, location: Location, action: Action): void: 在“push”或“replace”导航发生之前调用的函数。

○
willUnmount?(routerInfo: SyBrowserRouterInfoType): void: 在路由器组件卸载之前调用的函数。

○
mounted(routerInfo: SyBrowserRouterInfoType): void: 在路由器组件挂载后调用的函数。

●
register: string: 一个标识生命周期注册者的字符串。这必须是 'main'。

### StillnessProvider

此组件应放置在应用程序的根部以启用“静止”功能。它为其他 stillness 组件提供上下文。

### StillnessShow

此组件是 react-stillness-component 中 Offscreen 的别名。它包装了您想要保持活动状态的组件。

●
visible: boolean: 一个布尔值，控制被包装的组件是可见的还是处于“静止”状态。

### StillnessRoute

此组件是 react-router-dom 的 Route 的包装器，与 stillness 功能集成。当 StillnessRoute 不活动时，它渲染的组件将保持在“静止”状态，而不是被卸载。

### StillnessSwitch

此组件是 react-router-dom 的 Switch 的包装器，旨在与 StillnessRoute 一起工作。它确保一次只有一个 StillnessRoute 处于活动状态。

### SyIcon

一个显示图标的 React 组件。它可以渲染基于字体的图标或 SVG 图标。它会首先尝试渲染基于字体的图标，如果失败，它将尝试获取并渲染 SVG 图标。

●
name: string: 要显示的图标的名称。

●
customIcon?: string: 图标的自定义类名。

●
renderByContent?(span: HTMLSpanElement | null): void: 当图标由内容渲染时调用的函数。

●
inner?: boolean: 如果为 true，SVG 图标将被包装在一个带有 sy-icon-inner 类的 <span> 中。

●
所有其他 props 都将传递给底层的 <span> 或 <svg> 元素。

### DateTimezone

一个 React 组件，用于显示日期和时间，并支持不同的时区和格式化选项。

●
ts?: number: 要显示的时间戳，以毫秒为单位。默认为当前时间。

●
type?: 'DATE' | 'DATETIME' | 'TIME': 要显示的信息类型。默认为 'DATETIME'。

●
mode?: 'NORMAL' | 'FORMAT' | 'PROXIMITY_MODE' | 'PASS_MODE' | 'FUTURE_MODE': 显示模式。

○
'NORMAL': 以标准格式显示日期和/或时间。

○
'FORMAT': 以自定义格式显示日期和/或时间，由 format prop 指定。

○
'PROXIMITY_MODE': 显示人类可读的相对时间（例如，“今天上午 10:00”，“昨天下午 5:00”）。

○
'PASS_MODE': 显示自基准时间以来经过的时间（例如，“5 分钟前”）。

○
'FUTURE_MODE': 显示到未来时间的剩余时间（例如，“5 分钟后”）。

●
baseTs?: number: 'PASS_MODE' 和 'FUTURE_MODE' 的基准时间戳，以毫秒为单位。默认为当前时间。

●
suffix?: boolean: 如果为 true，则会向 'PASS_MODE' 和 'FUTURE_MODE' 的输出添加后缀（例如，“前”，“后”）。默认为 true。

●
format?: string: 'FORMAT' 模式的自定义格式字符串。

### getDateTimezoneStr

一个返回格式化日期和时间字符串的函数。它接受与 DateTimezone 组件相同的 props。

### timezoneConfig

一个包含系统时区配置的对象。

### systemConfig

一个返回系统配置的函数，包括日期和时间格式。

### dayjs

dayjs 库的一个实例，它是 Moment.js 的一个快速、轻量级的替代品。它通过以下插件进行了扩展：

●
utc

●
timezone

●
calendar

●
weekday

●
localeData

●
customParseFormat

●
weekOfYear

●
quarterOfYear

●
relativeTime

●
advancedFormat

### PrintContext

一个 React 上下文，提供在应用程序内处理打印的方法。

Value:

●
onPagePrintRender?: (options: { runtimeContext: any; udcSdk: any }) => void: 在为打印渲染页面时调用的函数。

### RemoteComponent

一个 React 组件，用于从远程模块联合范围动态加载和渲染组件。

●
config: Config: 一个包含远程组件配置的对象。

○
url?: string: 远程入口脚本的 URL。如果未提供，它将被构造为 /${config.scope}/remoteEntry.js。

○
scope: string: 模块联合范围的名称。

○
module: string: 要从范围加载的模块的名称。

○
instanceKey?: string: 远程组件实例的唯一键。

○
i18nHostAppName?: string: 托管 i18n 资源的应用程序的名称。

○
serviceName?: string: 服务的名称。

○
loading?: ReactNode: 组件加载时显示的 React 节点。

○
loadingComponent?: ReactNode: 组件加载时显示的 React 节点。

○
error?: ReactNode: 如果组件加载失败，则显示的 React 节点。

○
errorComponent?: ReactNode: 如果组件加载失败，则显示的 React 节点。

○
key?: string: 组件的键。

●
properties: Record<string, any>: 要传递给远程组件的 props 对象。

●
componentName?: string: 组件的名称。

●
onPageLoadingFailed?: () => void: 如果组件加载失败，则调用的函数。

●
onload?(): void: 组件加载后调用的函数。

●
onerror?(msg?: string, error?: Error | null): void: 如果加载组件时出错，则调用的函数。

●
beforeScriptExecute?(remoteEntry: string): void: 在执行远程入口脚本之前调用的函数。

### useDynamicScript

一个 React 钩子，用于加载模块联合的远程入口脚本。

●
options: LoadDynamicScriptOptions: 一个包含以下属性的对象：

○
url: string: 远程入口脚本的 URL。

○
onload?(): void: 脚本加载后调用的函数。

○
onerror?(msg?: string, error?: Error | null): void: 如果加载脚本时出错，则调用的函数。

○
beforeScriptExexecute?(remoteEntry: string): void: 在执行脚本之前调用的函数。

●
{ ready: boolean; failed: boolean }: 一个包含两个布尔值的对象：如果脚本已加载，ready 为 true；如果出现错误，failed 为 true。

### loadComponent

一个从远程模块联合范围加载组件的函数。

●
options: { scope: string; module: string; properties?: Record<string, any> }: 一个包含以下属性的对象：

○
properties?: Record<string, any>: 要传递给远程组件的 props 对象。

●
() => Promise<{ default: ComponentType<any> }>: 一个返回 promise 的函数，该 promise 解析为加载的组件。

### MFLoader

(已弃用) 一个从模块联合范围加载资源的异步函数。

●
options: Omit<Config, 'properties' | 'key' | 'error' | 'loading'>: 一个包含远程组件配置的对象，不含 properties、key、error 或 loading 属性。

●
Promise<any>: 一个解析为加载资源的 promise。

### RemoteLoader

一个加载远程模块的 React 组件。它可以在 iframe 中或作为远程组件渲染模块。它还处理获取应用程序元数据，例如版本信息和权限。

●
appName: string: 要加载的应用程序的名称。

●
pageName?: string: 要加载的页面的名称。

●
url?: string: 如果提供，页面将在此 URL 的 iframe 中加载。

●
isMobile?: boolean: (已弃用) 一个标志，指示应用程序是否在移动设备上运行。

●
isShowLoading?: boolean: 如果为 true，则在模块加载时将显示加载指示器。

●
notNeedMetadata?: boolean: 如果为 true，组件将不会获取应用程序元数据。

●
iframeSignature?: string: iframe 的签名，用于设置 id 属性。

●
pageProps?: object: 要传递给加载的页面或组件的 Props。

○
handleClose?(): void: 关闭组件的函数。

○
handleRefresh?(): void: 刷新页面的函数。

○
handleTitle?(title: string): void: 设置页面标题的函数。

○
onPageRender?(...args: any[]): void: 页面渲染时调用的回调函数。

○
onPageLoadingFailed?(): void: 如果页面加载失败，则调用的回调函数。

○
inParams?: Record<string, any>: 页面的参数。

●
container?: ContainerType: 组件的容器类型。

●
module?: string: 要加载的模块的名称。

●
popoverProps?: Record<string, any>: 弹出框的 Props。

●
loadingComponent?: ReactNode | null: 自定义加载组件。

●
errorComponent?: ReactNode | null: 自定义错误组件。

●
hostName?: string: 主机应用程序的名称。

●
needWatermark?: boolean: 如果为 true，则会向页面添加水印。

●
onload?(): void: (已弃用) 模块加载后调用的回调函数。

●
onerror?(): void: (已弃用) 如果加载模块时出错，则调用的回调函数。

●
onError?(msg?: string, target?: Error | null): void: 如果出错，则调用的回调函数。

●
beforeScriptExecute?(remoteEntry: string): void: 在执行远程入口脚本之前调用的回调函数。

### RemotePageLoader

(已弃用) 一个加载远程页面的 React 组件。它是 RemoteLoader 的包装器，将 module prop 设置为 'Entry'。

### showRemoteModal

一个在模态对话框中显示远程组件的函数。

●
remoteLoaderProps: RemoteLoaderProps: RemoteLoader 组件的 props。

●
container?: HTMLElement: 模态框的容器元素。

●
PopoverHandler: 弹出框的处理程序。

### showRemoteDrawer

一个在抽屉中显示远程组件的函数。

●
container?: HTMLElement: 抽屉的容器元素。

### RemoteModal

一个在模态对话框中显示远程组件的 React 组件。它是 RemoteLoader 的包装器，使用 Popover 来显示模态框。

### RemoteDrawer

一个在抽屉中显示远程组件的 React 组件。它是 RemoteLoader 的包装器，使用 Popover 来显示抽屉。

### PopoverHandler

一个提供控制 Popover 组件方法的类。

### loadRemoteEntryScript

一个加载模块联合远程入口脚本的异步函数。

### initI18n

一个初始化应用程序 i18n 的异步函数。

### loadI18nSource

一个加载应用程序 i18n 源的异步函数。

### usePageErrorCatch

一个 React 钩子，提供捕获页面上发生的错误的方法。

### print

一个通过创建 iframe、注入内容，然后在 iframe 窗口上调用打印函数来启动当前 HTML 内容打印的函数。

●
param: printParam: 一个打印参数对象。

○
debug?: boolean: 如果为 true，打印后不会移除 iframe，以便进行调试。

●
Promise<any>: 一个在打印过程完成时解析的 promise。

### handlePrintLifeCycleEvent

一个并行执行打印生命周期事件函数列表的异步函数。

●
eventList: Array<printLifeCycleParamType>: 一个打印生命周期事件对象数组。

○
fn: () => void: 要执行的函数。

○
mark?: string: 一个用于调试时标识函数的字符串。

○
option?: printLifeCycleParamOptionType: 函数的选项。

■
isGlobal?: boolean: 回调是否是全局的。

■
timeout?: number: 函数执行的超时时间。

●
type: string: 事件的类型（例如，'before' 或 'after'）。

●
Promise<any>: 一个在所有函数都完成后解析的 promise。

### addBeforePrintCallback

一个注册在打印前执行的回调的函数。

●
fn: () => void: 回调函数。

●
mark?: string: 一个标识回调的字符串。

●
option?: printLifeCycleParamOptionType: 回调的选项。

○
isGlobal?: boolean: 如果为 true，回调将被添加到全局回调列表中。

### addAfterPrintCallback

一个注册在打印后执行的回调的函数。

●
Promise<any>: 一个在生命周期事件被触发后解析的 promise。

### syPrint

一个协调打印过程的函数，包括显示加载指示器、触发“打印前”回调、执行打印，然后触发“打印后”回调。

●
Promise<any>: 一个在整个打印过程完成时解析的 promise。

### toPrintPage

一个导航到打印预览页面的函数。

●
appPath?: string: 要打印的应用程序路径。

### toPrintPageForOpener

一个在 window.printPageUtils 对象上调用打印实用工具函数的函数（如果存在）。此函数主要用于与旧版 UDC 应用程序兼容。

●
options: any: 要传递给打印实用工具函数的选项。

### saveUdcPagePrintData

一个在 window.printPageUtils 对象上调用打印实用工具函数以保存 UDC 页面打印数据的函数（如果存在）。此函数主要用于与旧版 UDC 应用程序兼容。

●
...reset: any[]: 要传递给打印实用工具函数的参数。

### initUdcPagePrintData

一个通过调用 saveUdcPagePrintData 来初始化 UDC 页面打印数据的函数。

●
options: any: 一个包含 pageId、pageSignature、printDesign 和 components 的对象。

### usePrintAdapter

一个提供与打印相关的状态和回调的 React 钩子。它允许组件对打印事件（打印前和打印后）做出反应。

●
comId: string: 组件的唯一 ID。

●
needPrintStatus = true: 组件是否需要打印状态。

●
{ isPrintMode: boolean }: 一个带有 isPrintMode 布尔值的对象，如果组件处于打印模式，则为 true。

## 工具

### scalePage

一个通过调整根元素的字体大小来缩放页面的函数。

●
scale: number: 缩放字体大小的量。

●
options?: scaleOptions: 一个选项对象。

○
type?: 'scale' | 'zoom' | 'meta' | 'font': 要执行的缩放类型。目前仅支持 'font'。

### eventOn

订阅一个事件。

●
eventName: string: 要订阅的事件的名称。

●
callBack: EventHandlerType<EData>: 当事件发出时要调用的函数。

### eventOnOnce

订阅一个事件，并在事件第一次发出后自动取消订阅。

### eventOff

取消订阅一个事件。

●
eventName: string: 要取消订阅的事件的名称。

●
callBack: EventHandlerType<EData>: 用于订阅事件的函数。

### registerBeforeEmitHook

注册一个在事件发出之前将被调用的钩子函数。

●
eventName: string: 事件的名称。

●
fn: HookFn: 要注册的钩子函数。

### removeBeforeEmitHook

移除一个用 registerBeforeEmitHook 注册的钩子函数。

●
fn: HookFn: 要移除的钩子函数。

### eventEmit

发出一个事件。

●
eventName: string: 要发出的事件的名称。

●
data?: EData: 要传递给事件处理程序的数据。

### eventEmitAsyncResult

发出一个事件并等待所有事件处理程序返回结果。

●
eventData?: EData: 要传递给事件处理程序的数据。

●
Promise<any[]>: 一个解析为事件处理程序结果数组的 promise。

### eventEmitBroadcast

向其他窗口广播一个事件。

●
eventName: string: 要广播的事件的名称。

●
wins: Window[] = []: 要广播事件的窗口数组。

●
limitReciveBusIds: string[] = []: 要限制广播的事件总线 ID 数组。

### EventHandlerType

事件处理程序函数的类型别名。

### useEventOn

一个 React 钩子，用于订阅事件并在组件卸载时自动取消订阅。

●
callback: EventHandlerType<any>: 当事件发出时要调用的函数。

### EventBus

一个提供发布和订阅事件方法的类。

构造函数:

●
busId: string: 事件总线实例的唯一 ID。

方法:

●
registerBeforeEmitHook(eventName: string, fn: HookFn): 注册一个在事件发出之前将被调用的钩子函数。

●
removeBeforeEmitHook(eventName: string, fn: HookFn): 移除一个用 registerBeforeEmitHook 注册的钩子函数。

●
eventEmit<EData>(eventName: string, eventData?: EData): 发出一个事件。

●
eventEmitAsyncResult<EData>(eventName: string, eventData?: EData): 发出一个事件并等待所有事件处理程序返回结果。

●
eventEmitAsyncResultByEventCallback<EData>(eventName: string, eventData: EData, callbackEventName: string, reciveCallbackHander: (callbackData: Record<string, any>) => Promise<any>, timeout = 60): 发出一个事件并等待回调事件被触发。

●
eventEmitBroadcast<EData>(eventName: string, eventData?: EData, wins: Window[] = [], limitReciveBusIds: string[] = []): 向其他窗口广播一个事件。

●
eventOn<EData>(eventName: string, callBack: Handler<EData>): 订阅一个事件。

●
eventOnOnce<EData>(eventName: string, callBack: Handler<EData>): 订阅一个事件，并在事件第一次发出后自动取消订阅。

●
eventOff<EData>(eventName: string, callBack: Handler<EData>): 取消订阅一个事件。

●
getAllEvent(): (已弃用) 返回所有已注册事件的数组。

●
all(): 返回所有已注册事件及其处理程序的映射。

●
createScopeEventName(scope: string, eventName: string): 创建一个带作用域的事件名称。

### useEventAdapter

一个为 UDC 事件系统提供适配器的 React 钩子。它返回一个带有用于发出和监听事件的函数的对象。

●
props: Record<string, any>: 组件的 props。

●
{ eventEmit, eventEmitAsync, eventOn, eventOff, asyncCallback, useEventBus, newVersion }: 一个包含以下属性的对象：

○
eventEmit: EventEmit | undefined: 发出事件的函数。

○
eventEmitAsync: EventEmitAsync | undefined: 发出事件并等待结果的函数。

○
eventOn: EventOn | undefined: 订阅事件的函数。

○
eventOff: EventOff | undefined: 取消订阅事件的函数。

○
asyncCallback: AsyncCallback | undefined: 创建异步回调的函数。

○
useEventBus: UseEventBus | undefined: 订阅事件的钩子。

○
newVersion: boolean: 一个布尔值，如果正在使用新版本的事件系统，则为 true。

### whereConvert2Sql

一个将 UDC 查询中的 where 子句转换为类 SQL 对象的函数。

●
conditions: any: 要转换的 where 子句。

●
systemVariablesValues: any: 系统变量的对象。

●
funcs?: any: 用于解析上下文变量和表达式的函数对象。

●
options?: Record<string, any>: 选项对象。

●
any: 一个表示 where 子句的类 SQL 对象。

### Cookies

js-cookie 库的重新导出，它提供了一个简单、轻量级的 API 来处理 cookie。

### getLoginUrl

一个返回应用程序登录 URL 的函数。它会检查全局 LOGINURL 变量，然后检查存储中的 login-url 项，最后根据应用程序是否在移动设备上运行，回退到 /login-mobile 或 /login 的默认值。

●
string: 登录 URL。

### getComponentStyle

一个返回组件样式的函数。它首先检查存储中的样式，如果不存在，则从服务器获取。

●
componentName: string: 组件的名称。

●
terminal: 'desktop' | 'mobile' = 'desktop': 终端类型。

●
any: 组件的样式，如果未找到则为 null。

### desensitizationsStr

一个通过用占位符替换字符串的一部分来对字符串进行脱敏的函数。

●
target: string: 要脱敏的字符串。

●
startNum: number: 字符串开头要保留的字符数。

●
endNum: number: 字符串结尾要保留的字符数。

●
placeHolader = '*' : 用作占位符的字符。

●
string: 脱敏后的字符串。

### decryptoStrByDES

一个使用 DES 解密字符串的函数。

●
encryptedMsg: JsCrypto.CipherParams: 加密的消息。

●
key: string: 用于解密的密钥。

●
string: 解密后的字符串。

### encryptoStrByDES

一个使用 DES 加密字符串的函数。

●
target: string: 要加密的字符串。

●
key?: string: 用于加密的密钥。

●
string: 加密后的字符串。

### encryptoStrByMD5

一个使用 MD5 加密字符串的函数。

●
string: 字符串的 MD5 哈希值。

### EncryptoPassword

一个加密密码的函数。它首先检查是否启用了密码加密，如果是，则从服务器获取一个种子，并用它来使用 DES 加密密码。

●
password: string: 要加密的密码。

●
Promise<string>: 一个解析为加密密码的 promise。

### nanoid

一个生成唯一 ID 的函数。

●
size?: number: 要生成的 ID 的长度。默认为 21。

●
prefix?: string: 要添加到 ID 的前缀。

●
string: 唯一的 ID。

### storage

window.localStorage 的别名。

### getThemeInfoById

一个返回给定主题 ID 的主题信息的函数。

●
themeId: string: 主题的 ID。

●
isMobile = false: 一个布尔值，如果应用程序在移动设备上运行，则为 true。

●
{ themeCss: string, themeName: string }: 一个包含主题 CSS 和主题名称的对象。

### handleAppThemeCss

一个为应用程序设置主题的函数。

●
themeId: string: 要设置的主题的 ID。

### handleThemeCss

### ajax

一个发出 AJAX 请求的函数。它可以使用 fetch API 或 XMLHttpRequest。

●
url: string: 要请求的 URL。

●
data: any: 要随请求发送的数据。

●
options: AjaxOptions: 一个选项对象。

○
method?: string: 要使用的 HTTP 方法。

○
headers?: Record<string, any>: 要随请求发送的标头对象。

○
contentType?: string | boolean: 请求的内容类型。

○
dataType?: string: 响应的预期数据类型。

○
processData?: boolean: 是否在发送前处理数据。

○
useAjax?: boolean: 是否使用 XMLHttpRequest 而不是 fetch。

○
cors?: boolean: 请求是否是跨域请求。

○
withCredentials?: boolean: 是否随请求发送凭据。

○
timeout?: number: 请求的超时时间，以毫秒为单位。

○
proxy?: any: 用于请求的代理。

○
onUploadProgress?: <T>(e: T) => any: 一个使用上传进度调用的回调函数。

○
onProgress?: <T1, T2>(loaded: T1, total: T2) => any: 一个使用下载进度调用的回调函数。

○
body?: any: 请求的主体。

○
allowNoToken?: boolean: 是否允许在没有令牌的情况下发出请求。

○
responseType?: XMLHttpRequestResponseType: 预期的响应类型。

○
urlNeedModify?: boolean: 是否在发送请求前修改 URL。

○
byH5?: boolean: 是否使用 H5 API。

●
Promise<any>: 一个解析为服务器响应的 promise。

### get

一个发出 GET 请求的函数。它是 ajax 的包装器。

### post

一个发出 POST 请求的函数。它是 ajax 的包装器。

### upload

一个上传文件的函数。它是 post 的包装器。

### put

一个发出 PUT 请求的函数。它是 ajax 的包装器。

### registerOrigin

一个注册静态文件和 API 请求源的函数。

●
{ file, api }: { file?: string; api?: string }: 一个包含文件和 API 源的对象。

### getOrigin

一个返回已注册源的函数。

●
{ file?: string; api?: string }: 一个包含文件和 API 源的对象。

### getUrlWithOrigin

一个将 API 源前置到 URL 的函数，如果它还不是绝对 URL 的话。

●
url = '': 要修改的 URL。

●
string: 修改后的 URL。

### apolloRegister

一个注册 Apollo 配置的函数。

●
config: ApolloConfig: 一个包含 Apollo 配置的对象。

○
url: string: GraphQL 端点的 URL。

○
headers?: HeadersInit: 要随请求发送的标头对象。

### getApolloConfig

一个返回已注册 Apollo 配置的函数。

●
ApolloConfig: Apollo 配置。

### apolloQuery

一个发出 GraphQL 查询的函数。

●
sql: string: GraphQL 查询。

●
payload: any: 查询的变量。

●
options: AjaxOptions = {}: 请求的选项对象。

### escapeStringToHtml

一个转义字符串以在 HTML 中使用的函数。

●
str: string: 要转义的字符串。

●
isEscapeSpace = true: 是否转义空格。

●
isEscapeBr = true: 是否转义换行符。

●
string: 转义后的字符串。

### errorMessage

一个返回给定错误代码的错误消息的函数。

●
code: number | string: 错误代码。

●
language: string: 用于错误消息的语言。

●
string: 错误消息。

### Exception

一个表示异常的类。

●
message: string: 错误消息。

### error

一个创建 Errors 对象的函数。

●
options: ErrorArgs: 一个选项对象。

○
code: number: 错误代码。

○
language?: string: 用于错误消息的语言。

○
message?: string | undefined: 错误消息。

○
stack?: string: 堆栈跟踪。

○
url?: string: 发生错误的 URL。

●
Errors: 一个 Errors 对象。

### queryLoader

一个用于发出 GraphQL 查询的 GraphqlLoader 实例。

### mutationLoader

一个用于发出 GraphQL 突变的 GraphqlLoader 实例。

### createLoader

一个创建新的 GraphqlLoader 实例的函数。

●
type: 'query' | 'mutation': 要创建的加载器类型。

●
config: QueryConfig: 加载器的配置。

●
valueHandleFn: (value?: Result) => { success: boolean; value: any } = defaultValueHandleFn: 一个处理从服务器返回的值的函数。

●
GraphqlLoader<Request, Result>: 一个新的 GraphqlLoader 实例。

### getRequestByAppName

一个返回给定应用程序名称的 GraphqlLoaderInstance 的函数。

●
appName: string: 应用程序的名称。

●
GraphqlLoaderInstance: 应用程序的 GraphqlLoaderInstance。

### GraphqlLoader

一个提供批处理和缓存 GraphQL 请求方法的类。

### getCurrentUser

一个返回当前用户的函数。

●
Record<string, any> | null: 当前用户，如果没有当前用户则为 null。

### setCurrentUser

一个设置当前用户的函数。

●
userInfo: Record<string, any>: 要设置为当前用户的用户。

### showLoading

一个显示加载指示器的函数。

●
props?: LoadingTypes: 一个选项对象。

○
loadingType?: 'init' | 'request': 加载类型。

### hideLoading

一个隐藏加载指示器的函数。

### showError

一个显示错误消息的函数。

●
content: string: 要显示的错误消息。

### getCurrentUi

一个返回当前 UI 库的函数。

●
isMobile?: boolean: 应用程序是否在移动设备上运行。

●
any: 当前的 UI 库，如果没有当前 UI 库则为 null。

### isMobile

一个如果应用程序在移动设备上运行则返回 true 的函数。

### setLoading

一个显示或隐藏加载掩码的函数。它使用计数器来处理并发请求，以便加载掩码只显示一次。

●
loading?: boolean: 是否显示或隐藏加载掩码。

### getServiceRequest

一个返回服务请求对象的函数。服务请求对象具有发出 GET、POST、PUT 和 UPLOAD 请求的方法。

●
serviceName: string: 服务的名称。

●
useGraphql?: boolean: 是否对请求使用 GraphQL。

●
{ get, post, put, upload }: 一个包含发出请求方法的对象。

### OpenWindow

一个打开新窗口的函数。

●
url: any: 要打开的 URL。

●
name?: string: 窗口的名称。

●
features?: string: 窗口的特性。

●
openParams?: OpenParams: 一个用于打开窗口的选项对象。

○
openType?: '_system_blank' | 'self' | 'page' | '_blank': 打开类型。

○
terminal?: 'PC' | 'MOBILE': 终端类型。

○
syHistory?: any: history 对象。

○
history?: any: history 对象。

○
tabTitle?: string: 选项卡的标题。

○
appId?: string: 应用程序的 ID。

○
isOpenLink?: boolean: 是打开链接还是页面。

○
isReplaceTop?: boolean: 是否替换历史堆栈的顶部。

●
keepAlive?: boolean: 是否保持窗口活动。

### OpenChildFrameWindow

一个在子框架中打开新窗口的函数。

●
url: string: 要打开的 URL。

### CloseWindow

一个关闭窗口的函数。

●
closeParam: CloseWindowParam = {}: 一个用于关闭窗口的选项对象。

○
singleTabCloser?: () => void: 当最后一个选项卡关闭时要调用的函数。

### CloseAllWindow

一个关闭所有打开的子窗口的函数。

### GetAncestorsWindow

一个返回调用 window.open 的祖先窗口的函数。

●
win?: any: 从中开始的窗口。

●
any: 祖先窗口。

### getWsServer

一个返回 WebSocket 服务器 URL 的函数。

●
client?: string: 客户端类型。

●
string: WebSocket 服务器 URL。

### WebsoketServer

一个提供 WebSocket 客户端的类。

●
options: WebsoketServerOption = {}: 一个选项对象。

○
debug?: boolean: 是否启用调试。

○
reconnect?: boolean: 是否自动重新连接。

○
reconnectTime?: number: 重新连接间隔，以秒为单位。

●
url?: string: WebSocket 服务器 URL。

●
protocol?: string: WebSocket 协议。

●
log(message: string): 如果启用了调试，则将消息记录到控制台。

●
connect(): 连接到 WebSocket 服务器。

●
reconnect(): 重新连接到 WebSocket 服务器。

### logger

一个包含向服务器记录消息方法的对象。

●
log(info: LoggerContent): 记录一条信息性消息。

●
error(error: Error): 记录一条错误消息。

●
warn(info: any): 记录一条警告消息。

### createLocale

一个从浏览器的语言设置创建区域设置字符串的函数。

●
string: 区域设置字符串。

### getLocaleByI18nLocal

一个从本地存储返回区域设置的函数，如果不存在则创建一个新的。

### getLocale

一个返回区域设置的函数。

●
locale?: any: 要使用的区域设置。

●
autoToReal?: boolean: 是否将“AUTO”转换为实际的区域设置。

### getDefaultLocale

一个返回默认区域设置的函数。

●
string: 默认区域设置。

### convertTree

一个将扁平数据列表转换为树形结构的函数。

●
data: Array<Record<string, any>>: 要转换的扁平数据列表。

●
options: Options = { idKey: 'id', pidKey: 'pId', rootValue: '', withChildrenIsNotLeaf: false }: 一个选项对象。

○
idKey: string: ID 键的名称。

○
pidKey: string: 父 ID 键的名称。

○
rootValue: string | number | null | undefined: 根父 ID 的值。

○
withChildrenIsNotLeaf?: boolean: 是否向非叶子节点添加 children 属性。

●
any[]: 树形结构。

### getTenant

一个返回当前租户的函数。

●
string: 当前租户。

### AppContext

一个提供对应用程序级数据和函数的访问的 React 上下文。

●
permissions: Record<string, any>: 权限对象。

●
appContextSetContext: any: 设置上下文的函数。

●
appData?: Record<string, any>: 应用程序数据对象。

●
metaData?: Record<string, any>: 元数据对象。

●
pageData?: Record<string, any>: 页面数据对象。

●
useUiModelValue?: (params: any) => any: 从 UI 模型获取值的函数。

●
generateComProperty?: (params: any, callbackData: any) => any: 生成组件属性的函数。

### useBaseStateHook

一个返回组件基本状态的 React 钩子。基本状态由组件的 uiModel、BaseStateContext 和 AppContext 决定。

●
{ uiModel = {}, componentId }: { uiModel: any; componentId: string }: 一个包含组件 uiModel 和 componentId 的对象。

●
others?: Others: 其他属性的对象。

○
required?: boolean | string: 组件是否是必需的。

○
disabled?: boolean: 组件是否被禁用。

○
readonly?: boolean: 组件是否是只读的。

○
visible?: boolean: 组件是否可见。

●
{ disabled, readonly, visible, required }: 一个包含组件基本状态的对象。

### BaseStateContext

一个提供组件基本状态的 React 上下文。此上下文用于将 disabled、readonly 和 visible 状态向下传递给子组件。

●
disabled?: boolean: 组件是否被禁用。

●
readonly: boolean: 组件是否是只读的。

●
visible: boolean: 组件是否可见。

### UdcPageContext

一个为 UDC 页面提供数据的 React 上下文。

### UdcItemContext

一个为 UDC 项目提供数据的 React 上下文。

### UdcLayoutContext

一个为 UDC 布局提供数据的 React 上下文。

### basicUiModelSchema

一个定义基本 UI 模型模式的常量。它是一个包含单个“title”字段对象的数组。

### defaultExpressionValue

一个返回默认表达式值对象的函数。

●
simple: unknown: 表达式的简单值。

●
{ type: 'Simple', expression: null, selectParam: null, simple: unknown }: 一个表示简单表达式值的对象。

### defaultExpressionValueByRightCondition

一个为右侧条件返回默认表达式值对象的函数。

●
{ type: 'CONSTANT', expression: null, selectParam: null, simple: unknown, noNeedFormate: true, value: unknown, desc: unknown }: 一个表示常量表达式值的对象。

### inputControlStateUiModelNotIncludeDisabled

一个定义输入控件状态 UI 模型模式的常量，不包括“disabled”状态。

### inputControlStateUiModelSchema

一个定义输入控件状态 UI 模型模式的常量，包括“disabled”、“readonly”和“invisible”。

### inputControlUiModelSchema

一个定义输入控件 UI 模型模式的常量，包括“required”和“status”。

### otherControlUiModelSchema

一个定义其他控件 UI 模型模式的常量，包括“status”。

### operateControlUiModelSchema

一个定义操作控件 UI 模型模式的常量，包括“status”。

### commonAttrs

一个包含 UI 组件通用属性的常量对象，例如 nanoid、name、title、titleDisplay、topTitleDisplay、text、description、auth、inputStatus、icon、inputStatusNoReadOnly、reportStatus、basicStatus、basicStatusUpload、searchStatus、encryption、desensitization、controlStatus、labelLength、validation、dataSourceField、titleStyle 和 commonStyle。每个属性都定义了其键、标签、类型、props、默认值和分类。

### VALID_RULES

一个定义组件预设验证规则名称的枚举。

●
BIND_ENTITY: 必须绑定实体。

●
BIND_EVENT: 必须绑定事件。

●
BIND_ENTITY_ALL_REQUIRED: 必须绑定实体的所有必填字段。

●
COMMON_EVENT_CONTENT: 通用事件内容验证。

### DataType

一个定义应用程序中使用的各种数据类型的枚举。

●
String: 字符串数据类型。

●
Integer: 整数数据类型。

●
Float: 单精度浮点数据类型。

●
Double: 双精度浮点数据类型。

●
Long: 长整型数据类型。

●
BigInteger: 大整数数据类型。

●
Decimal: 十进制数据类型。

●
Boolean: 布尔数据类型。

●
Date: 日期数据类型。

●
DateTime: 日期和时间数据类型。

●
Time: 时间数据类型。

●
Entity: 实体数据类型。

●
Object: 对象数据类型。

●
Dto: DTO 数据类型。

●
CtpEnum: CTP 枚举数据类型。

●
Enum: 枚举数据类型。

●
Attachment: 附件数据类型。

●
Currency: 货币数据类型。

●
MultilineString: 多行字符串数据类型。

●
Image: 图像数据类型。

●
Array: 数组数据类型。

●
Selectpeople: 选择人员数据类型。

●
Serial: 序列号数据类型。

●
Content: 内容数据类型。

●
Opinionhandler: 意见处理程序数据类型。

●
Map: 映射数据类型。

●
AssociateDocument: 关联文档数据类型。

### FilterResult

一个定义筛选操作结果的枚举。

●
SUCCESS: 筛选操作成功。

●
CONTINUE: 继续筛选操作。

●
BREAK: 中断筛选操作。

### NodeType

一个定义 UI 模型中各种节点类型的枚举。

●
APP_PROPS: 应用程序属性。

●
PAGE_PROPS: 页面属性。

●
PAGE_IN_PARAM: 页面输入参数。

●
PORTLET_IN_PARAM: Portlet 输入参数。

●
SINGLE: 单条记录。

●
LIST: 多条记录。

●
CURRENT_ROW: 当前行。

●
SELECT_ROW: 选中行。

●
CHECK_ROWS: 勾选行。

●
ENTITY: 实体。

●
ENUM: 枚举。

●
FIELD: 叶子节点，字段。

●
PAGE: 页面。

### convStyles

一个将样式对象转换为 React CSS 属性对象的函数。

●
attrs: StyleAttr: 样式属性。

●
React.CSSProperties: 一个 React CSS 属性对象。

### variableStyle

一个返回带有 CSS 变量的样式对象的函数。

●
name: string: CSS 属性的名称。

●
value?: string: CSS 属性的值。

●
Record<string, string>: 一个样式对象。

### buildBgStyle

一个构建背景样式对象的函数。

●
{ backgroundImage, backgroundColor, backgroundAdapt, gradient }: Record<string, any>: 一个包含背景属性的对象。

●
any: 一个背景样式对象。

### BpmPageContext

一个为 BPM 页面提供数据的 React 上下文。

### UdcNavBarBottomContext

一个为页面底部的 UDC 导航栏提供数据和函数的 React 上下文。

●
pageSettings: Record<string, any>: 页面设置对象。

●
changeContext: () => void: 更改上下文的函数。

### builtInFunctions

一个包含表达式引擎内置函数的对象。

### ExpressExecuteEngine

一个执行表达式的类。

### traverseTokens

一个遍历表达式标记的函数。

### traverseExpressionTokens

### expressExecute

一个执行表达式的函数。

●
context: AnyRecord: 表达式的上下文。

●
schema: string | AnyRecord: 表达式模式。

●
options?: Options: 一个选项对象。

○
getValueHandler?: (s: any) => any: 一个处理获取值的函数。

○
customTranslate?: (operator: AnyRecord) => string: 一个翻译自定义运算符的函数。

○
customNodeRewrite?: (node: AnyRecord) => AnyRecord: 一个重写自定义节点的函数。

○
customFunctions?: AnyRecord: 自定义函数。

●
any: 表达式的结果。

### systemVariableResolution

一个根据不同业务场景解析系统变量的函数。

●
options: Options: 一个选项对象。

○
variableName: string: 系统变量的名称。

○
useOriginValue?: boolean: 是使用原始值还是解析值。

○
sysMethodType?: 'defaultSysMethod' | 'initialValueSysMethod' | 'expressionSystemVariableMethod': 要使用的系统方法类型。

○
customSystemVariableValue?: any: 自定义系统变量值。

●
any: 解析后的系统变量值。

### expressionSystemVariableObject

一个包含表达式系统变量的对象。

### getExpressionSystemVariableObject

一个返回包含表达式系统变量的对象的函数。

●
customSystemVariableValue?: Record<string, any>: 自定义系统变量值。

●
Record<string, any>: 一个包含表达式系统变量的对象。

### getSystemVariable

systemVariableValue 的别名，它是一个包含来自本地存储的系统变量值的对象。

### serverTimeCache

服务器时间的缓存。

### DEFAULT_DATE

一个定义默认日期值的常量。

### DEFAULT_NUMBER

一个定义默认数值的常量。

### DEFAULT_VALUE

一个定义默认字符串值的常量。

### DEFAULT_ZERO

一个定义默认零字符串值的常量。

### getDiffDatatypeDefeultValue

一个返回给定数据类型默认值的函数。

●
{ dataType, multiSelect = false, supportClear }: Props: 一个包含数据类型、是否多选以及是否支持清除的对象。

●
any: 默认值。

### isInvalidValue

一个检查值是否无效的函数。

●
{ dataType, multiSelect = false, value }: isDefaultValueProps: 一个包含数据类型、是否多选和值的对象。

●
boolean: 如果值无效则为 true，否则为 false。

### isEmptyValue

一个检查值是否为空的函数。

●
boolean: 如果值为空则为 true，否则为 false。

### fileUpload

一个上传文件的异步函数。它处理获取上传签名、上传到 OSS 以及将文件信息保存到数据库。

●
file: File: 要上传的文件。

●
options: Options = {}: 一个选项对象。

○
appName?: string: 应用程序的名称。默认为 'app-common'。

○
isPublic?: boolean: 文件是否是公开的。默认为 false。

●
Promise<{ url: string; storageKey: string }>: 一个解析为包含上传文件 URL 和存储键的对象的 promise。

### attachmentDisplayFieldsInfo

一个定义要查询的附件显示名称字段的常量数组。

### attachmentDisplayFieldsName

一个包含要查询的附件显示名称字段名称的常量数组。

### getFileIdByStorageKey

一个从存储键中提取文件 ID 的函数，处理不同的版本控制方案。

●
imgSource: ImgSource: 一个包含图像源信息的对象，包括 id、storageKey 和 udcDesignerVersion。

●
string: 提取的文件 ID。

### getFileUrlByStorageKey

一个根据存储键和应用程序名称构造文件 URL 的函数。

●
imgSource: ImgSource: 一个包含图像源信息的对象，包括 appName、storageKey 和 fileName。

●
string: 构造的文件 URL。

### getFileUrlByStorageKeyAsync

一个根据存储键和应用程序名称异步构造文件 URL 的函数，必要时获取 udcDesignerVersion。

●
params: getFileUrlByStorageKeyAsyncInterface: 一个包含 appName、hostAppName 和 imgSource 的对象。

●
Promise<string>: 一个解析为构造的文件 URL 的 promise。

### getAttachmentUrl

一个构造附件 URL 的函数。

●
url: string: 附件的 URL。

●
appName?: string: 应用程序的名称。

●
string: 附件的 URL。

### getFileConfigAll

一个返回给定应用程序的文件配置的函数。

●
isAll?: boolean: 是否返回所有文件配置。

●
any: 文件配置。

### safeParse

一个安全解析 JSON 字符串的函数。

●
jsonStr: unknown: 要解析的 JSON 字符串。

●
options?: { defaultValue?: T }: 一个选项对象。

○
defaultValue?: T: 如果解析失败，则返回的默认值。

●
T | null: 解析的 JSON 对象，如果解析失败则为 null。

### getStaticPrefix

一个返回 URL 静态前缀的函数。

●
string: 静态前缀。

### customizationUrl

一个返回自定义 URL 的函数。如果 URL 还不是绝对 URL 或尚未自定义，它会将基本路由器前置到 URL。

●
browserUrl?: string: 要自定义的 URL。

●
string: 自定义的 URL。

### transformToGraphqlPath

一个将路径转换为 GraphQL 路径的函数。

●
path: string: 要转换的路径。

●
string: 转换后的 GraphQL 路径。

### getCtpEnumOptions

一个根据枚举代码检索 CTP 枚举选项的异步函数。

●
props: Props: 一个包含以下内容的对象：

○
appName: string: 应用程序的名称。

○
params: CtpEnumParams: 一个包含 enumCode、appId（可选）和 itemValue（可选）的对象。

○
showLoading?: boolean: 是否显示加载指示器。

●
Promise<any>: 一个解析为枚举选项的 promise。

### getCtpEnumOptionsByRelation

一个根据父枚举值和代码（用于级联枚举）检索 CTP 枚举选项的异步函数。

### batchDownloadUrl

一个检索文件批量下载 URL 的异步函数。

●
props: any: 一个包含 appName、params 和 showLoading 的对象。

●
Promise<any>: 一个解析为下载 URL 的 promise。

### formatI18nCtpEnumOptions

一个使用国际化格式化 CTP 枚举选项的函数。

●
list: any[]: 枚举选项列表。

●
any[]: 格式化后的枚举选项列表。

### getEnumApplicationName

一个返回枚举应用程序名称的函数。

●
{ appName, relationApp, appData }: { appName?: string; relationApp?: string; appData?: any }: 一个包含应用程序名称、关联应用程序和应用程序数据的对象。

●
string: 应用程序名称。

### renderCtpEnumStatus

一个渲染 CTP 枚举项状态的函数。

●
item: { delete?: boolean; enable?: boolean; show?: boolean }: 枚举项。

●
string: 状态字符串。

### filterCtpEnumData

一个筛选出已禁用或已删除的 CTP 枚举项的函数。

●
item: { delete?: boolean; enable?: boolean }: 枚举项。

●
boolean: 如果应筛选该项，则为 true，否则为 false。

### isI18nData

一个检查值是否是国际化数据的函数。

●
value: any: 要检查的值。

●
boolean: 如果值是国际化数据，则为 true，否则为 false。

### getLocaleValueByI18n

(已弃用) 一个返回当前区域设置的国际化值的函数。

●
{ value, dataI18n }: { value?: string; dataI18n?: boolean }: 一个包含值以及它是否是国际化数据的对象。

●
string: 国际化值。

### getOrgLocalValue

一个检索组织的区域设置列表并将其存储在本地存储中的异步函数。

●
userInfo: Record<string, any>: 用户信息。

●
Promise<void>: 一个在检索并存储区域设置列表后解析的 promise。

### InitI18n

一个为应用程序或组件初始化国际化的 React 组件。

●
backend: string: 后端 URL。

●
client: string: 客户端类型。

●
i18nHostAppName: string: i18n 主机应用程序的名称。

●
type: "app" | "component": 国际化类型。

●
getSystemCommonI18n: () => Promise<any>: 获取系统通用 i18n 资源的函数。

●
getTenantCommonI18n: () => Promise<any>: 获取租户通用 i18n 资源的函数。

●
getAppI18n: () => Promise<any>: 获取应用程序 i18n 资源的函数。

●
needRef: boolean: 是否使用 ref。

●
mergeRequestCommon: boolean: 是否合并通用请求。

●
children: ReactNode: 国际化初始化后要渲染的子项。

### fetchAppI18n

一个获取应用程序国际化资源的函数。

●
i18nVersion: string: i18n 版本。

●
Promise<any>: 一个解析为 i18n 资源的 promise。

### InitI18n4App

一个为应用程序初始化国际化的 React 组件。它是 InitI18n 的包装器。

### InitI18n4Component

一个为组件初始化国际化的 React 组件。它只渲染其子项。

### i18n

一个提供国际化功能的对象。

●
t(args: any): 将键翻译为当前区域设置。

○
参数:

■
args: any: 要翻译的键。它可以是一个字符串或一个具有以下属性的对象：

●
k: string: 要翻译的键。

●
v?: string[]: 要替换到翻译后字符串中的值数组。

●
d: string: 如果未找到键，则使用的默认值。

○
返回:

■
string: 翻译后的字符串。

### initApp

一个为应用程序初始化国际化的函数。它从后端获取 i18n 资源并将其合并到全局 I18nResource 对象中。

●
args: initAppArgs: 一个参数对象。

○
backend: string: 后端应用程序名称。

○
i18nHostAppName?: string: i18n 主机应用程序的名称。

○
locale?: string: 要使用的区域设置。

○
isChangeLocale?: boolean: 是否正在更改区域设置。

○
resolve: (res?: any) => Record<string, any> | void: promise 的 resolve 函数。

○
reject: (res?: any) => Record<string, any> | void: promise 的 reject 函数。

○
type?: 'app': 初始化类型。

○
client?: 'web' | 'mobile': 客户端类型。

○
getSystemCommonI18n?: boolean: 是否强制获取系统通用 i18n 资源。

○
getTenantCommonI18n?: boolean: 是否强制获取租户通用 i18n 资源。

○
getAppI18n?: boolean: 是否强制获取应用程序 i18n 资源。

○
needRef?: boolean: 是否获取引用的 i18n 资源。

○
mergeRequestCommon?: boolean: 是否合并通用请求。

○
isCacheI18nRequest?: boolean: 是否缓存 i18n 请求。

○
version?: string: 应用程序的版本。

### getIsUdcApp

一个检查应用程序是否是 UDC 应用程序的函数。

●
boolean: 如果应用程序是 UDC 应用程序，则为 true，否则为 false。

### isPersonalDetailApp

一个确定应用程序是否是“个人详细信息”应用程序的函数，这可能需要对个性化页面进行特殊处理。

●
appInfo: { appName: string; isUdcApp?: boolean; urlPath?: string }: 一个包含应用程序信息的对象。

●
boolean: 如果应用程序是个人详细信息应用程序，则为 true，否则为 false。

### getData

一个检索给定应用程序的个性化页面数据的异步函数。它首先检查本地存储，如果未找到数据或数据已过期，则从服务中获取。

●
appInfo: AppInfo: 一个包含应用程序信息的对象，包括 appName、terminal 和 pageUrl。

●
Promise<any>: 一个解析为个性化页面数据的 promise，如果未找到自定义页面 URL，则为 false。

### removeLocalStorageData

一个从本地存储中删除个性化页面数据的函数。

●
appInfo?: AppInfo: 如果提供，则仅删除指定应用程序的数据。否则，将清除所有个性化页面数据。

### getAppInfoFromUrl

一个从 URL 中提取应用程序信息的函数。

### refreshAppInfoCache

一个刷新应用程序信息缓存的函数。它获取更新的应用程序版本并将其存储在本地存储中。

●
apps: string[] = []: 要刷新的应用程序名称数组。如果为空，将刷新所有缓存的应用程序。

●
boolean: 如果刷新了任何应用程序，则为 true，否则为 false。

### clearAppInfoCache

一个清除本地缓存中所有应用程序信息的函数。

### SlotsExtends

一个通过为事件拦截、数据拦截和 UI 拦截注册回调方法来扩展前端组件的类。

●
如果尚不存在，则初始化全局 __SLOTS_EXTENDS_SDK__ 对象。

●
extend({ cmpType, desc, key, value }: IExtendCmp): 扩展一个组件。

○
cmpType: string: 要扩展的组件类型。

○
desc: any: 扩展的描述。

○
key: string: 扩展的唯一键。

○
value: any: 扩展的值（例如，回调函数）。

### SlotsExtendsForPlatform

一个为平台注册和描述前端组件扩展点的方法的类。

●
如果尚不存在，则初始化全局 __SLOTS_EXTENDS_SDK__DESCRIBE__ 对象。

●
register({ cmpType, key, desc }: IRegisterExtend): 注册一个扩展点。

○
key: string: 扩展点的唯一键。

○
desc?: string: 扩展点的描述。

●
any: 与注册的扩展点关联的值（如果有）。

### libsRouteTable

一个提供管理库路由表功能的对象。

●
get(key: string): 一个异步函数，用于检索给定键的解析器。如果尚未初始化，它将初始化路由表。

●
Promise<IResolver>: 一个解析为 IResolver 实例的 promise。

### IResolver

一个定义解析器方法的接口。

●
getNames(): Promise<string[]>: 返回此解析器可以处理的组件名称列表。

●
resolve(packageName: string, info?: Version): Promise<string>: 解析包的版本。

●
load(packageName: string, libVersion: string, subPackageName?: string): Promise<Readonly<unknown>>: 从库中加载组件。

●
getDefaultExport(packageName: string, info: Version): Promise<string>: 返回组件的默认导出。

### Resolver

一个实现 IResolver 接口的类。它为其他解析器提供了基础。

●
libsAccess: LibsAccess: LibsAccess 的一个实例。

●
getNames(): Promise<string[]>: 抛出错误，必须由子类实现。

●
resolve(pkgName: string, copVersion?: string): Promise<string>: 抛出错误，必须由子类实现。

●
getDefaultExport(packageName: string, info?: Version): Promise<string>: 返回 'module'。

●
load(packageName: string, version: string, subPackageName?: string): Promise<Readonly<EsModule>>: 动态加载模块。

### Version

包版本的类型别名。它可以是字符串、undefined 或具有 host 和 caller 属性的对象。

### dynamicImport

一个从库中动态导入模块的异步函数。

●
packageName: string: 要导入的包的名称。

●
info?: Version: 要导入的包的版本。

●
subPackageName?: string: 要导入的子包的名称。

●
Promise<Readonly<T>>: 一个解析为导入模块的 promise。

### appDynamicImport

一个从应用程序动态导入模块的异步函数。

●
appName: string: 要从中导入的应用程序的名称。

●
resourceName: string: 要导入的资源的名称。

### PasswordUtils

一个包含密码相关实用函数的对象。

枚举:

●
PasswordSafeLevel: LOW, MEDIUM, HIGH, CUSTOM

●
PasswordSafeGrade: FAIL, LOW, MEDIUM, HIGH

常量:

●
PASSWORD_LEVEL_LABEL: 一个将密码强度级别映射到其标签的对象。

●
PASSWORD_LEVELS: 一个密码强度级别标签的数组。

●
SYS_UNSAFE_MIN_LEN: 不安全密码的最小长度。

●
SYS_SAFE_MIN_LEN: 安全密码的最小长度。

●
SPECIAL_CHARS: 一个特殊字符的字符串。

●
UPPER_LOWER_CHARS: 一个用于检查大写和小写字母的正则表达式。

●
LETTER_CHARS: 一个用于检查字母的正则表达式。

●
REGEX_VALIDATE_RULE: 一个用于验证的正则表达式规则对象。

类型:

●
CustomRuleKey: 自定义规则键的类型。

●
ConfigKey: 配置键的类型。

●
CustomConfigRule: 自定义配置规则的类型。

●
RuleCheckProps: 规则检查属性的接口。

钩子:

●
usePasswordConfig(configKeys: ConfigKey[]): 一个返回密码配置的钩子。

●
usePasswordCheck(password: string): 一个检查密码强度的钩子。

函数:

●
getPasswordConfig(configKeys: ConfigKey[]): 一个返回密码配置的函数。

●
getPasswordSafeGrade({ passwordStrength, password, customRequiredRule }): 一个返回密码安全等级的函数。

●
checkPasswordSafe(props: RuleCheckProps): 一个检查密码是否安全的函数。

●
getPasswordLevelRule(passwordStrength: PasswordSafeLevel, customRequiredRule?: CustomConfigRule): 一个返回密码级别规则的函数。

### businesses

一个提供管理业务库功能的对象。

●
list(): 一个异步函数，用于检索业务库列表。

●
Promise<any[]>: 一个解析为业务库数组的 promise。
