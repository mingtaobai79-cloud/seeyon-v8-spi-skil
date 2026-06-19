---
title: "数科与金格电子签章适配"
source: "https://www.yuque.com/seeyonkk/v8/mdp8vqls2pbm1bfr"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 数科与金格电子签章适配

> Source: https://www.yuque.com/seeyonkk/v8/mdp8vqls2pbm1bfr

一、产品说明
电子签章版本：iSignature_V10.2.4.10278_CA版
数科不含签章版本： aarch64-250228

二、V8 版式文件配置
版式文档
当前通道：数科-服务
服务参数配置

| 参数名 | 默认值 |
| --- | --- |
| apiUrl | https://IP:8042/web-reader |
| domain | https://IP/service |
| signUrl | https://IP:8044/iSignatureServer（可以不用填写） |

三、数科配置
1、数科配置文件修改如下：
/data/suwell/suwell-viewer-aarch64/suwell-viewer-aarch64/service/web-reader-boot/AIOCfg/service.yml 
  place: client      #获取签章列表位置(client 客户端web助手获取签章列表 , other 服务端获取签章列表需要实现接口,服务端需要放对应的库,serverAdd 服务端ofdRender获取签章列表，需要服务端放置签章库)

/data/suwell/suwell-viewer-aarch64/suwell-viewer-aarch64/service/web-reader-boot/data/rpc/render/arm64/plugins/sealV4/suwell/config_oes.ini 
#切换签章库模式,0为本地签章[oes]配置域生效,1为云签章[weboes]配置域生效,2为CA云签章[caoes]配置域生效,3为ZHYU签名[zhyu]配置域生效,4为UKEY签章 *
OESMode = 0

四、客户端安装数科组件
先安装：suwellwebassist-1.0.24.0619.1647-setup.exe ，重启电脑
再安装：webassistkey-1.0.22.1221.1437-setup.exe
修改配置文件：C:\Program Files (x86)\Suwell\webassist\webassist_pro\plugins\sealV4   删除整个suwell文件夹（这个是数科测试章）

五、V8盖章测试
再V8系统调用数科签章按钮测试

国正文喜红
修改正文
正文打印
原文档
正文盖章
上传正文
中
正文下载
处理意见
公共账号组
签章
注释
开始
请输入
8
骑缝章
?验章
撤销签章
盖章
隐藏注释
选择印章
X
常用语
A
从已读取的印章中搜索
R
KINGGRID
金格演示公章
安徽科学
拟印发文
金格电子签章预览
文件标题:
司
豫能办(2025)1号
发文字号:
紧急程度:
集团文书
综合办公室
录入单位:
拟稿人:
?刚新列表
2025-08-18 15:44:31
拟文时间:
拟印发文
所属类别:
盖章
取消
主送机关:
公共账号组
抄送机关:
签发人:
签发日期:
集团文书
2025-08-18

V8 数科+金格电子签章适配方案.docx
(194 KB)
