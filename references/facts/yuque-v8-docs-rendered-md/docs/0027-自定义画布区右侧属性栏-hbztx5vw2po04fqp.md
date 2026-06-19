---
title: "自定义画布区右侧属性栏"
source: "https://www.yuque.com/seeyonkk/v8/hbztx5vw2po04fqp"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 自定义画布区右侧属性栏

> Source: https://www.yuque.com/seeyonkk/v8/hbztx5vw2po04fqp

## 1.现状

udc目前只提供了有限的属性渲染组件，当不满足需求时，由于没有扩展机制，目前只能在udc前端工程的common文件夹下自定义，这导致业务组件逻辑侵入udc，且可任意引用udc工程其他文件，无法约束其范围。考虑到现在自定义组件也有自定义其属性渲染组件的需求，需要将属性渲染组件与udc解耦，支持自定义组件在自己的工程中实现，udc为其提供接入机制和相关能力。

## 2.控件属性支持自定义渲染组件设计

<img src="https://cdn.nlark.com/yuque/0/2025/png/382504/1748245929262-cf554dcd-8762-46fa-aa30-579c663bd30d.png?x-oss-process=image%2Fformat%2Cwebp" width="1649">

## 3.开发流程

### 3.1 在 sy.config.json 中定义 attrModule

<img src="https://cdn.nlark.com/yuque/0/2025/png/382504/1748246017610-14832bad-9675-44da-b463-a61481514f17.png?x-oss-process=image%2Fformat%2Cwebp" width="1442">

### 3.2 新增自定义渲染的代码

<img src="https://cdn.nlark.com/yuque/0/2025/png/382504/1748246131590-b6710dae-2bcb-4659-9325-7ce969ecdf21.png?x-oss-process=image%2Fformat%2Cwebp" width="1632">

packages/bpm-run/src/components-attr 代码示例:

components-attr.zip
(4 KB)

### 3.3 构建部署

### 3.4 设计器中进行调试

<img width="1920">

## 4.其他

目前低代码设计器画布区，右侧自定义属性渲染- 对应组件的键值对

https://docs.qq.com/sheet/DUnR1WFZlRWpFTExs?nlc=1&tab=BB08J2
