---
title: "散列加密"
source: "https://www.yuque.com/seeyonkk/v8/htbbndul0hfirkdu"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 散列加密

> Source: https://www.yuque.com/seeyonkk/v8/htbbndul0hfirkdu

###### 1、使用场景

客户想用自己的密钥机制对数据进行加解密

###### 2、支持范围

用户密码、工资条

###### 3、实现步骤

1、需要实现的SPI接口

```
com.seeyon.boot.encrypt.algorithm.digest.spi.DigestSpi
```

2、具体接口方法

```
public interface DigestSpi {
    /**
     * 加密
     */
    String encrypt(String clearText);
}
```

###### 4、配置信息

nacos中对应服务下添加如下配置，需要全局生效配置到public

```
seeyon
  encrypt  
    digest: SPI
```

###### 5、重启服务

如果要全局生效，需要重启所有服务

###### 6、注意事项

SPI部署后，只对新产生的数据生效，旧数据还是用的原来的加解密方式

###### 7、产品配置

登录system-admin账号进行数据加密配置

加密方式:O国际算法(系统内置)
用户数据加密
*电子邮件:
了登录管理
协同运营平台
用户密码:
定制应用数据加密
数据加密
数据保护
国密算法(系统内置
手机号码:
关键字加密3:
历史数据清洗
系统数据加密
显示设置
系统参数
:数据动加密
组件管理
国际化
认证服务
数据加密
数据签名
管理首页
证件号码:
加密传输
加密存储
定时任务
