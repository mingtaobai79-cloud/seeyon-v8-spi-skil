---
title: "UDC远程调试"
source: "https://www.yuque.com/seeyonkk/v8/nhvxisyq1i2hmmsh"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# UDC远程调试

> Source: https://www.yuque.com/seeyonkk/v8/nhvxisyq1i2hmmsh

## 1、确保服务启动命令中开启了debug，如下图：

<img src="https://cdn.nlark.com/yuque/0/2025/png/50254821/1753760342136-ce1317c9-e0a9-4a5e-8874-f91c9c468f1d.png" width="1281">

## 2、使用nodeport类型的service将debug端口映射出来

service的模板如下：

```
apiVersion: v1
kind: Service
metadata:
  name: xxxxx    #根据实际情况填写服务名称
  namespace: xxxxx     #根据实际情况填写k8s名称空间
spec:
  ports:
    - protocol: TCP
      port: 8888
      targetPort: 8888
  selector:
    app: xxxx    #根据实际情况填写服务名称
    type: dyapp    #根据实际情况填写服务类型（平台应用和标准应用默认为：backend;udc自建应用默认为：dyapp;）
  type: NodePort
  sessionAffinity: None
  externalTrafficPolicy: Cluster
```

### 2.1、方法一：使用kuboard 创建service

<img src="https://cdn.nlark.com/yuque/0/2025/png/50254821/1753760342158-bf593788-c6cc-4141-870f-7270b77de0a8.png" width="956">

<img src="https://cdn.nlark.com/yuque/0/2025/png/50254821/1753760342132-1de43953-7d3d-42bd-8ec1-a49f5a65ed7d.png" width="689">

<img src="https://cdn.nlark.com/yuque/0/2025/png/50254821/1753760342188-0cdc1386-7aa8-479c-a28c-506871dc4390.png" width="1410">

查看创建的service,获取8888对应的nodeport端口：

<img width="741">

然后就可以使用k8s节点的ip:nodeport 去进行调试了。

### 2.2、方法二：使用kubelet命令 创建service

根据 service的模板，创建service.yaml文件

使用kubectl命令创建service

获取nodeport端口

<img width="1616">
