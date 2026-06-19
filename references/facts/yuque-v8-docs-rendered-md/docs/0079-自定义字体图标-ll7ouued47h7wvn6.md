---
title: "自定义字体图标"
source: "https://www.yuque.com/seeyonkk/v8/ll7ouued47h7wvn6"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 自定义字体图标

> Source: https://www.yuque.com/seeyonkk/v8/ll7ouued47h7wvn6

## 1.应用场景

标品字体或图标 不满足客户场景，需要新增图标或字体，可以通过自定义字体图标的方式进行扩展

## 2.开发步骤

### 2.1.将png格式的图片转换成svg格式；

网址：https://convertio.co/zh/

于在XML中描述二维矢量和混合矢量/光扭图形.同时支持动画,交互式图
SVG是一种标记语言,可扩展失量图形,由万维网联合会(W3G)开发,
PNG到SVG转换器
颜色索引图像彩色图像PNG格式通过一种压缩形式存储图像信息.
这种格式是为了取代GIF.PNG支持三种主要类型的光精图像:灰度图像
PNG是一种使用无损压缩算法来压缩的扭格图形数据存储格式.开发PN
像和说明性脚本不支持三维物体的描述.SVG的基础是VM格式的标记语
PNG到5VG质量评璨女大女43(469570票)
在线免费转换您的PNG文件为SVG文件
使用CR或SHIF一次添加多个文件
SERVER-STORAGEPNG
可携式网络图开形格式
评价PNG到SVG质量!
QCONVERTI
+添加更多文件
可伸缩失量图形
将所有转换为V
我的文件2登录注册
IO转换VOCRAPL定价HELP
RGLFEDITORVIDEOTRAN
PNG
转换
言和PGML.
CSCONVERTIO.CO/ZH/PNG-
转换V
SVG
准备妞
梦

### 2.2 将转换后的svg格式的图标转成字体图标：

网址：https://icomoon.io/app/#/select

COMOON-FREE
NTITLEDSET2
UNTITLEDSET
彩UNTITLEDPROJE
.选中上传后的图标
生成字体图标
土LMPORTLCONSL
习LOGIN
ERATESVG&MOR
ENERATEFONTF
1
ICOMOON.IO/APP/#/SELE
8
口
品日
古
QSEARCH.
O
旦
B
即日
口
口口
目
O
租
网
个
(O)
TT
吖
S
塑
国
星
雪
园
2
10
中
O
<
四GENER
口
2
入
由
9
E
4
D
8
国
包
官
4
O
合
J
9
O
己
一
台

OUCANREFERENCEYOURFONTSINHTMLANDEASILYCHANGEYOURICONSELECTIONON
ENABLEQUICKUSAGETOUPLOADFONTSFORHOSTINGORSHARINGUSINGTHISFEATURE,
SERVER-STORAGE
HEFLY,WITHOUTHAVINGTOUPDATEYOURCSS
QUICKUSAGEANASHARING
VGLYPHS:1TTFSIZE:1756BYTE
FPREFERENCESHLRESET
4,下载字体图标
多UNTITLEDPROJECT
习LOGIN-
LRESETQSEARCH.
LECTION(1)
SICOMOONIO/AP
900
GENERATESVG&MORE
RIDSIZE:UNKNOWN

### 2.3.将下载的压缩包中的style.css和fonts这两个文件夹copy到extend-icons

### 2.4.更改style.css为icon.less，并更改其文件内容

- 将font-family发更改为 'custom-icon'

- 新增class=custom-icon, 作为该字体的class， 其内容至少需要包含"font-family: 'custom-icon'"

- 将各个icon的class统一以custom-开头

<img width="1875">

### 2.5.配置icon.json文件，设计态通过该文件展示图标列表

### 2.6.新建extend-icons/enable.ts 文件，用以控制是否可在设计器中使用扩展图标

具体用例参考模版工程中的example/extend-icons

其他方法：

在https://www.iconfont.cn/中，将svg图片上传（上传时最好选择去除颜色上传，以免碰到兼容性问题）；待审核完成之后将所有图标添加到购物车 然后点击下载源码，将下载后的文件解压，也会得到相应的css以及ttf文件，参考上面提到的方法修改对应文件

<img width="1889">

<img width="1920">

## 3.Demo

extend-icons.zip
(27 KB)
