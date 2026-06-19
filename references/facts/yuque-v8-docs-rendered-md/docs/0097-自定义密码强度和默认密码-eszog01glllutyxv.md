---
title: "自定义密码强度和默认密码"
source: "https://www.yuque.com/seeyonkk/v8/eszog01glllutyxv"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 自定义密码强度和默认密码

> Source: https://www.yuque.com/seeyonkk/v8/eszog01glllutyxv

作者：陈晓东

时间：2026.5.26

适用版本：自定义密码强度5.0.3及以上版本、自定义默认密码：5.3.0及以上版本

场景：

1、当前系统密码强度不满足客户需求，可以通过spi的方式自定义密码强度
2、当前系统的默认密码不符合客户要求，可以通过spi的方式自定义默认密码

# 1、SPI开发

SPI开发规范参考：
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
public interface PasswordCheckService {
    /**
     * 方法类型
     *
     * @return  方法类型集合
     */
    default List<PasswordMethodTypeEnum> getMethodType() {
        return Lists.newArrayList(PasswordMethodTypeEnum.CHECK_STRENGTH);
    };
    /**
     * 密码强度校验
     * @param password
     * @return
     */
    default Boolean checkPasswordStrength(String password) {
        return Boolean.TRUE;
    }
    /**
     * 自定义初始化密码
     *
     * @param userDto 用户信息
     * @param password  原始密码
     * @return
     */
    default String customInitPassword(CtpUserSpiUserDto userDto, String password) {
        return password;
    }
}
```

getMethodType说明执行的功能，如果只执行密码强度，则返回Lists.newArrayList(PasswordMethodTypeEnum.CHECK_STRENGTH)；如果既要执行密码强度，又要执行自定义初始化密码，则返回Lists.newArrayList(PasswordMethodTypeEnum.CHECK_STRENGTH, PasswordMethodTypeEnum.INIT_PASS)

# 4、自定义密码规则

实现checkPasswordStrength 方法，判断传入的password是否符合客户自定义的密码规则，如果符合，就返回true，不符合就返回false
注意：如果一旦配置自定义的密码规则，通过系统管理员配置的密码规则不会再生效，完全以客开规则为准

# 5、自定义初始化密码

实现customInitPassword 方法，自定义初始化密码，返回自定义后的初始化密码
注意：如果一旦配置自定义的初始化密码，通过系统管理员配置的初始密码不会再生效，并且也不会受是否启用初始化密码开关控制，完全以自定义的为准

# 6、重启服务

重启ctp-user服务
