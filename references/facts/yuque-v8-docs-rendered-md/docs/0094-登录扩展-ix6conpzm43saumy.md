---
title: "登录扩展"
source: "https://www.yuque.com/seeyonkk/v8/ix6conpzm43saumy"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 登录扩展

> Source: https://www.yuque.com/seeyonkk/v8/ix6conpzm43saumy

作者：陈晓东

时间：2026.5.27

适用版本：1.0及以上版本

场景：

●
当平台原有登录方式不够用时，我们可以自主新增、定制登录形式。

●
登录过程中也能额外增加校验等操作，比如密码校验，直接套用现有标准代码稍作修改就行。

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
public abstract class AbstractAuthenticationProvider {
    /**
     * 认证类型
     *
     * @return
     */
    public abstract String getAuthenticationType();
    /**
     * 是否支持
     *
     * @param authentication
     * @return
     */
    public abstract boolean supports(Class<?> authentication);
    /**
     * 获取用户信息
     *
     * @param authentication
     * @return
     */
    public abstract Authentication retrieveUser(Authentication authentication);
    /**
     * 验证之前的策略
     *
     * @param authentication
     */
    public abstract void preAuthenticationCheck(Authentication authentication);
    /**
     * 验证之后的策略
     *
     * @param authentication
     */
    public abstract void postAuthenticationCheck(Authentication authentication);
    /**
     * 身份验证
     *
```

同时需要实现AbstractAuthenticationToken接口，用于支持当前的认证方式

```
public abstract class AbstractAuthenticationToken implements Authentication {
    private Object details;
    @Override
    public String getName() {
        return (this.getPrincipal() == null) ? "" : this.getPrincipal().toString();
    }
    @Override
    public Object getDetails() {
        return details;
    }
    public void setDetails(Object details) {
        this.details = details;
    }
}
```

# 4、相关配置

getAuthenticationType配置完成后，需要在nacos的user空间下配置认证类型，这样才会使用当前的登录方式

```
seeyon:
  user:
    authenticationType:xxx #这里填getAuthenticationType方法的返回值
```

# 5、重启服务

重启ctp-user服务
