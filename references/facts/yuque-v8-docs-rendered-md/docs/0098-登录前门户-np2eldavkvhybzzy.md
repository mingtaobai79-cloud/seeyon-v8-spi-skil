---
title: "登录前门户"
source: "https://www.yuque.com/seeyonkk/v8/np2eldavkvhybzzy"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 登录前门户

> Source: https://www.yuque.com/seeyonkk/v8/np2eldavkvhybzzy

作者：陈晓东

时间：2026.5.26

适用版本：V3.15及以上版本

场景：用户在不登录的情况下实现门户的访问

重要提醒：平台已经实现了对应的SPI，SPI对应的jar已经上传远程仓库，通过nacos配置就行

# 1、获取ctp-user-loginpre-3.15.66.jar

获取方式1：https://gitlab.seeyon.com/a9/code/backend/ctp-user-spi 拉取研发代码，切换到客户版本分支，构建jar

获取方式2：如果没有研发分支的权限，联系研发或者陈晓东进行构建

# 2、上传ctp-user-loginpre-3.15.66.jar

将第一步获取到的jar文件，上传到文件存储桶

1、使用minio做Maven私服的情况

jar包对应存放位置：摆渡桶/spi/com/seeyon/ctp-user-loginpre/3.15.66/ctp-user-loginpre-3.15.66.jar

2、使用nexus做Maven私服的情况

jar包对应存放位置：release库/com/seeyon/ctp-user-loginpre/3.15.66/ctp-user-loginpre-3.15.66.jar

# 3、nacos配置

在nacos中public下面添加配置

```
seeyon:
  spi:
    enable: true
    spi-plugins:
    - oss:com.seeyon,ctp-user-loginpre,3.15.66
```

# 4、重启服务

重启ctp-user、portal服务
