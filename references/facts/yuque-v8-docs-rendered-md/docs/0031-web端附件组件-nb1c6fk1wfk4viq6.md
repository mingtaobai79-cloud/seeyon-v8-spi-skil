---
title: "web端附件组件"
source: "https://www.yuque.com/seeyonkk/v8/nb1c6fk1wfk4viq6"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# web端附件组件

> Source: https://www.yuque.com/seeyonkk/v8/nb1c6fk1wfk4viq6

### 1.组成

组件分为Attachment、AttachmentUpload、AttachmentDownload；

#### 1.1  AttachmentUpload为上传组件，标准API请参考官方的antd Upload：https://4x-ant-design.antgroup.com/components/upload-cn/#API；

#### 1.2 AttachmentDownload为下载组件，用于展示文件列表，根据参数可进行这些操作：下载、预览、编辑、删除、重命名、设置密级等；

#### 1.3 AttachmentUpload和AttachmentDownload共同组成Attachment，它包含了附件的上传及下载功能，主要使用于udc搭建出来的附件组件，不建议手写代码调用。

### 2.API

以下为致远V8的附件组件特有API：

#### 2.1 Attachment组件：

| 参数 | 说明 | 类型 | 默认值 | 可选值 | 可选值的含义 |
| --- | --- | --- | --- | --- | --- |
| uploadStyle | 控件样式 | string | 'uploadBtnStyle' | 'uploadBtnStyle'\| 'photoWall' \| 'dragArea' \| photoList' | 上传按钮式、照片墙式、拖拽区域式、照片列表式 |
| enableList | 是否显示适配列表的样式 | boolean | false | true\| false |  |
| value | 文件的storageKey，多个以英文逗号分隔 | string | '' |  |  |
| renameStatus | 附件重命名的状态 | string | 'invisible' | 'basic'\| 'disabled' \| 'invisible' | 正常、禁用、隐藏 |

#### 2.2 AttachmentUpload组件，请使用uploadFile方法进行上传：

#### 2.3 uploadFile方法

| 参数 | 说明 | 类型 | 默认值 | 可选值 | 可选值的含义 |
| --- | --- | --- | --- | --- | --- |
| appName | 应用名称（必填） | string | - | - | - |
| fileList | 已经上传的文件列表（受控） | [UploadFile] | [] | [] | - |
| photoWallWidth | 照片宽度（仅照片墙样式下生效） | number | 100 | 100-500 |  |
| photoWallHeight | 照片高度（仅照片墙样式下生效） | number | 100 | 100-500 |  |
| photoWallSizeMode | 适配方式 | string | 'cover' | 'contain'\| 'cover' \| 'fill' | 适中、铺满、拉伸 |
| uploadText | 上传按钮文字 | string |  |  |  |
| uploadIcon | 上传按钮图标（来源于图标库） | string | '' |  |  |
| btnType | 上传按钮样式 | string | 'default' | 'default'\| 'primary' \| 'link' \| 'dashed' | 次按钮、主按钮、文字按钮、虚线按钮 |
| isEdit | 是否开启图片编辑 | boolean | false | true\| false |  |
| isImgCompress | 图片质量 | number | 0.3 | 0.3\| 0.5 \| 0.8 | 低、中、高 |
| countLimitType | 数量限制 | string | 'system' | 'system'\| 'custom' | 系统默认、自定义 |
| countLimit | 数量设置（当countLimitType为'custom'生效） | number | 5 | 大于0的整数 |  |
| fileSizeType | 大小限制 | string | 'system' | 'system' \| 'custom' | 系统默认、自定义 |
| fileSize | 大小设置（当fileSizeType为'custom'时生效） | number | 5 | 大于0的整数 | 单位：MB |
| onEntitySecretChange | 获取当前实体的密级的事件 | async function，返回的数据构：onEntitySecretChangeData |  |  |  |
| isPublic | 是否开启上传文件夹 | boolean |  | true\| false |  |
| showQrcode | 是否显示扫码的上传按钮 | boolean |  | true\| false |  |
| showUploadBtn | 是否显示上传的按钮 | boolean |  | true\| false |  |
| showItemNum | 是否显示附件个数 | boolean | true | true\| false |  |
| renderInDesign | 是否处于设计器中 |  |  |  |  |
| showUploadList | 是否展示文件列表, 照片墙模式不展示 | boolean |  |  |  |
| accept | 同官方API |  |  |  |  |
| onChange | 同官方API | function |  |  |  |
| onQrChange | 扫码上传成功后发生的事件 | function |  |  |  |
| onError | 上传文件遇到错误时发生的事件 | function |  |  |  |
| showUploadBtn | 是否显示上传按钮，默认为true | boolean | true | true\| false |  |
| showQrcode | 是否显示扫码上传按钮,默认为false | boolean | false | true\| false |  |
| disabledUploadBtn | 是否禁用上传按钮，默认为false | boolean |  |  |  |
| disabledQrcode | 是否禁用扫码上传，默认为false | boolean |  |  |  |

#### 2.4 AttachmentDownload组件：

| 参数 | 说明 | 类型 | 默认值 | 可选值 | 可选值的含义 |
| --- | --- | --- | --- | --- | --- |
| appName | 应用名称（必填） | string | - | - | - |
| storageKeys | 已经上传的文件列表（受控） | [UploadFile] | [] | [] | - |
| hideFieldInfo | 是否隐藏文件信息 | select【multiple】 | [] | ['fileName','fileSize','createTime','createUserName','createDeptName'] | 附件标题、附件大小、上传时间、上传人、上传人部门 |
| showItemNum | 是否显示附件个数 | boolean | true | true\| false |  |
| fileArrangement | 文件排列 | string | 'horizontal' | 'transverse'\| 'horizontal' \| 'tablelist' | 纵向、横向、表格 |
| sortType | 文件排序 | string | 'default' | 'default'\| 'uploadTimeAsc' \| 'uploadTimeDesc' \| 'fileNameAsc' \| 'fileNameDesc' \| 'extensionAsc' \| 'extensionDesc' | 自定义排序、按上传时间升序、按上传时间降序、按文件名称升序、按文件名称降序、按文件扩展名升序、按文件扩展名降序 |
| copy | 预览时是否可复制 | boolean | true | true\| false | 系统默认、无水印 |
| useWaterMark | 水印内容 | string | 'default' | 'default'\| 'none' |  |
| showBatchOperation | 是否支持批量操作 | boolean | true | true\| false |  |
| showDownloadButton | 是否支持批量下载 | boolean | true | true\| false |  |
| showDeleteButton | 是否支持批量删除 | boolean | true | true\| false |  |
| showBatchSecretButton | 是否支持批量设置密级 | boolean | true | true\| false |  |
| batchDownloadFileName | 批量下载文件名 | boolean | true | true\| false |  |
| toType | 哪些格式需要转PDF下载 | string | '' | 'txt,doc,pdf'等 | 文件格式的扩展名，以英文逗号分隔 |
| qrUploadStatus | 扫码上传的状态 | string | 'invisible' | 'basic'\| 'disabled' \| 'invisible' | 正常、禁用、隐藏 |
| uploadStatus | 本地上传的状态 | string | 'basic' | 'basic'\| 'disabled' \| 'invisible' | 正常、禁用、隐藏 |
| downloadStatus | 下载文件的状态 | string | 'basic' | 'basic'\| 'disabled' \| 'invisible' | 正常、禁用、隐藏 |
| previewStatus | 预览文件的状态 | string | 'basic' | 'basic'\| 'disabled' \| 'invisible' | 正常、禁用、隐藏 |
| removeStatus | 删除文件的状态 | string | 'basic' | 'basic'\| 'disabled' \| 'invisible' | 正常、禁用、隐藏 |
| editFileStatus | 编辑文件的状态 | string | 'invisible' | 'basic'\| 'disabled' \| 'invisible' | 正常、禁用、隐藏 |
| renameStatus | 附件重命名的状态 | string | 'invisible' | 'basic'\| 'disabled' \| 'invisible' | 正常、禁用、隐藏 |
| setSecretStatus | 密级设置的状态 | string | 'basic' | 'basic'\| 'disabled' \| 'invisible' | 正常、禁用、隐藏 |
| showDownload | 是否显示下载的按钮 | boolean | true | true\| false |  |
| showPreview | 是否显示预览的按钮 | boolean | true | true\| false |  |
| showRemove | 是否显示删除的按钮 | boolean | true | true\| false |  |
| rename | 是否显示重命名的按钮 | boolean | true | true\| false |  |
| disableRenameButton | 是否禁用重命名的按钮 | boolean | false | true\| false |  |
| showSecretButton | 是否显示设置密级的按钮 | boolean | true | true\| false |  |
| showEditFile | 是否显示编辑文件的按钮 | boolean | true | true\| false |  |
| showSecretName | 是否显示密级标识 | boolean | true | true\| false |  |
| onFileEdited | 编辑文件后发生的事件 | function |  |  |  |
| onSecreted | 设置密级后发生的事件 | function |  |  |  |
| onRename | 重命名后发生的事件 | function |  |  |  |
| onEntitySecretChange | 获取当前实体的密级的事件 | async function，返回的数据构：onEntitySecretChangeData |  |  |  |
| enableTableOrderNumber | 是否启用表格的排序号 | boolean | false | true\| false |  |
| renderInDesign | 是否处于设计器中 |  |  |  |  |

### 3. UDC搭建应用中需要，手写代码可不关心：

| 参数 | 说明 | 类型 | 默认值 | 可选值 | 可选值的含义 |
| --- | --- | --- | --- | --- | --- |
| dataField | 绑定的字段编码（仅UDC搭建应用中需要） |  |  |  |  |
| dataParent | 上级数据容器控件id（仅UDC搭建应用中需要） |  |  |  |  |
| dataTarget | 独立数据源控件id（仅UDC搭建应用中需要） |  |  |  |  |
| udcSdk | udc运行态的sdk（仅UDC搭建应用中需要） |  |  |  |  |
| runtimeContext | udc运行态的上下文（仅UDC搭建应用中需要） |  |  |  |  |
|  |  |  |  |  |  |

### 4 说明：

#### 4.1 onEntitySecretChangeData

#### 4.2 UploadFile

## 5.实际用法

### 1.上传附件

### 2.下载附件

### 3.预览附件，比如点击某个按钮直接批量预览多个附件

### 4.单个附件预览
