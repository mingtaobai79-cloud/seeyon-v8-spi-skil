---
title: "自定义租户、机构登录人数控制"
source: "https://www.yuque.com/seeyonkk/v8/lbtxv6th0m01v9im"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 自定义租户、机构登录人数控制

> Source: https://www.yuque.com/seeyonkk/v8/lbtxv6th0m01v9im

作者：陈晓东

时间：2026.5.28

适用版本：5.30及以上版本

使用场景：用户可以自定义租户，机构登录人数控制

# 1、SPI开发

SPI开发规范，参考：
开发准备

# 2、添加依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>ctp-user-api</artifactId>
  <version>3.12.1</version>
</dependency>
```

# 3、客开实现方法

```
public abstract class AbstractAuthenticationCheckService {
    /***
     * 处理租户或者机构已经达到最大的用户数的用户
     * @param users  用户
     * @return  过滤掉超过最大用户数的用户，返回剩余的用户
     * @throws MaxOnlineUserExceedException 超过最大数时抛出异常
     */
    public <T extends BaseDto> List<T> processLoginUsers(List<T> users) throws MaxOnlineUserExceedException {
        return users;
    }
    /**
     * 验证切换租户时是否已经达到最大的用户数
     * @param userDto 用户dto
     * @throws MaxOnlineUserExceedException 超过最大数时抛出异常
     */
    public void validateSwitchTenantExceedMaxUser(BaseDto userDto) throws MaxOnlineUserExceedException {
    }
    /**
     * 验证切换者机构时是否已经达到最大的用户数
     * @param userId  用户id
     * @param targetOrgId   机构id
     * @throws MaxOnlineUserExceedException 超过最大数时抛出异常
     */
    public void validateSwitchOrgExceedMaxUser(Long userId, Long targetOrgId) throws MaxOnlineUserExceedException {
    }
}
```

说明：客户有一个专门维护租户级，机构级的登录人数控制(可以做一个底表来维护)，在登录(账号密码登录)，切换租户，切换机构的时候，分别实现已上方法。在方法内通过dubbo或者其他方式调用到客户维护的人数控制接口，进行判断

# 4、重启服务

重启ctp-user服务
