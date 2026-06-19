---
title: "对称加密"
source: "https://www.yuque.com/seeyonkk/v8/wqgtvw7hlnaqwage"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 对称加密

> Source: https://www.yuque.com/seeyonkk/v8/wqgtvw7hlnaqwage

###### 1、使用场景

客户想用自己的密钥机制对数据进行加解密

###### 2、支持范围

数据库存储加密（实体字段上标注了加密注解的）

###### 3、实现步骤

1、需要实现的SPI接口

```
com.seeyon.boot.encrypt.algorithm.symmetric.spi.SymmetricSpi
```

2、具体接口方法

```
public interface SymmetricSpi {
    /**
     * 加密
     */
    String encrypt(String clearText);
    /**
     * 解密
     */
    String decrypt(String cipherText);
}
```

###### 4、配置信息

nacos中对应服务下添加如下配置，需要全局生效配置到public

```
seeyon
  encrypt  
    symmetric: SPI
```

###### 5、重启服务

如果要全局生效，需要重启所有服务

###### 6、注意事项

SPI部署后，只对新产生的数据生效，旧数据还是用的原来的加解密方式

###### 7、产品配置

登录system-admin账号进行数据加密配置

加密方式:O国际算法(系统内置)
密算法(系统内置)
协同运营平台
:数据加密
定制应用数据动加密
手机号码:
关键字加密:
组件管理
历史数据清洗
系统数据加密
理首页
用户数据加密
数据加密
登录管理
电子邮件:
定时任务
用户密码:
国际化
证件号码:
认证服务
加密存储
数据加密
显示设置
加密传输
系统参数
数据保护
数据签名
