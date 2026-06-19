---
title: "桌面端M5 Windows打包步骤"
source: "https://www.yuque.com/seeyonkk/v8/dcfn2es4v8atqcvo"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 桌面端M5 Windows打包步骤

> Source: https://www.yuque.com/seeyonkk/v8/dcfn2es4v8atqcvo

作者：杨颜华
最后更新：2025-12-09

说明:需要项目组提供替换的logo和修改对应的名称,logo大小严格按照标准的大小来进行批图

## 1.应用类型：Windows

### 1.1 ctpstudio平台对应项目仓库,推送桌面端M5的源码

### 1.2 克隆对应的桌面端的代码

### 1.3.前置条件

#### 1.3.1.node版本:V16.17.0

#### 1.3.2 其次按照npm install --global --production windows-build-tools   建议通过这个命令安装，常用工具链都会装

#### 1.3.3 windows系统下：如果yarn失败,报autoreconf找不到,请访问(https://gnuwin32.sourceforge.net/packages/autoconf.htm)

#### 1.3.4 yarn里面报python错误,需要安装python依赖

https://mirrors.tuna.tsinghua.edu.cn/python/3.10.10/

DEV-XTOV8文件夹口V8前请资及研发口V8315版本之前的口V8标
MIRRORS.TUNA.TSINGHUAEDUCN/PYTHON/3.10.
前端掘金分布式构健系统客开开发平台
N-3.10,10-AMD64.EXE
2023-02-0720:21
2023-02-0805:37
2023-02-0805:37
YTHON3,L0.L0,TAR,XZ.S1G
BED-AMD64.ZIP.CRT
2023-02-0818:00
2023-02-0720:21
BED-AMD64.ZIP,ASC
2023-02-0818:0
2023-02-0805:37
2023-02-0720:21
023-02-0818:00
2024-09-1201:51
2023-02-0805:3
2024-09-1201:51
023-02-0818:00
1G1G-EMBED-AMD64.ZIP
,10.TGZ,SIGSTORE
HON-3.10.1
YTHON-3.10.10.
YTHON-3.10.1
2023-02-0720:21
VTHON-3.10
-AMD64,EXE.SIG
27.7MIB
YVTHON-3.10..
-EMBED-AMD64.ZI
10.10.TAR.XZ
YTHON-3
YTHON-3.1
PYTHON-3.1
PYTHON-3.10.
R.XZ.SIGSTORE
PYTHON-3.1C
G-AMD64.EXE.CRT
中DY
N-3.10.10-E
24.9MIE
5.5KIB
5.5KIB
8.2MIE
AMD64,EXE
137B
010B
,TGZ.CR七
1010B
37B
836B
833B
YTHON-3..
1010B
HON-3.10.10-
YTHON
口V8
141B
.10.10
.TGZ.SIG
836B
3.10.10
141B
,七GZ.ASC
PYTHON-
OMIRRO
.10.七GZ
立
开发平台门DEV-
10.10EMBED-AMD6

### 1.4 切换到desktop\A9\electron_shell\目录下,再执行yarn下载依赖

备注：执行yarn下载依赖后ffi-napi报错，需要单独下载ffi-napi依赖

npm install ffi-napi@4.0.3

备注：切换node官方源下载ffi-napi依赖

### 1.5 替换图标的目录：desktop\A9\electron_shell\res-build\release\

备注：修改M5名称 ，直接在electron_shell目录下搜索关键字“M5”，将涉及到M5的字样的地方全部替换成客户想要的改的名称

比如：

### 1.5 执行yarn buildwin_saas 命令进行打包

### 1.6 打包成功后，会把安装包dist目录，取M5_5.8.0_x64_installer.exe安装包进行验证

## 2.应用类型：macOS

### 2.1 clone对应的桌面端的代码

### 2.2 前置条件

node版本：V16.17.0

### 2.3 修改需要替换的图标和M5名称

修改哪些文件参考windows打包里面的第5点：替换图标的目录

### 2.4.执行yarn buildmac_saas名称进行构建
