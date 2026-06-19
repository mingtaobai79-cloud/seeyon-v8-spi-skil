---
title: "ticket认证返回人员信息自定义"
source: "https://www.yuque.com/seeyonkk/v8/pazygl1cot73gavl"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# ticket认证返回人员信息自定义

> Source: https://www.yuque.com/seeyonkk/v8/pazygl1cot73gavl

作者：陈晓东

时间：2026.5.26

适用版本：5.0.3及以上版本

场景：通过ticket认证时需要对返回的用户信息进行自定义，并且可以进行包装

ticket认证场景参考：
单点登录
中2.4.2返回示例里面的人员信息

# 1、SPI开发

SPI开发规范，参考：
开发准备

# 2、添加依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>ctp-user-api</artifactId>
  <version>5.0.3</version>
</dependency>
```

# 3、客开实现方法

```
public interface CustomUserInfoService {
    /**
     * 自定义用户信息方法
     * 
     * @param map 用户信息
     * @return    自定义后的用户信息
     */
    Map<String,Object> filterCustomUserInfo(Map<String,Object> map);
}
```

# 4、重启服务

重启ctp-user服务
