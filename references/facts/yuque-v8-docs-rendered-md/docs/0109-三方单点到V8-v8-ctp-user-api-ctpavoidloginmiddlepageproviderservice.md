---
title: "三方单点到V8"
source: "https://www.yuque.com/seeyonkk/v8/v8-ctp-user-api-ctpavoidloginmiddlepageproviderservice"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 三方单点到V8

> Source: https://www.yuque.com/seeyonkk/v8/v8-ctp-user-api-ctpavoidloginmiddlepageproviderservice

作者：杨映海
最后更新：2025-04-18

## 1 应用场景

三方系统登录后，可以免登V8访问V8平台相关页面。由三方系统携带用户身份令牌，V8平台进行代码开发回调接口完成用户真实身份识别。

<img src="https://cdn.nlark.com/yuque/0/2025/png/26748915/1744948254450-9542a63b-eaaf-4c87-b27f-8343dd079e8c.png" width="1437">

## 2 无自定义参数

### 2.1 接口说明

接口名称：com.seeyon.ctp.user.api.avoidlogin.CtpAvoidLoginMiddlePageProviderService

```xml
<dependency>
    <groupId>com.seeyon</groupId>
    <artifactId>ctp-user-api</artifactId>
    <!-- 请以实际环境的依赖版本号为准-->
    <version>3.8.211</version>
</dependency>
```

### 2.2 接口实现

spi代码仓库获取及工程初始化请参考：
开发准备

```java
import com.seeyon.ctp.user.annotation.CtpUserChannelRouter;
import com.seeyon.ctp.user.api.avoidlogin.CtpAvoidLoginMiddlePageProviderService;
import com.seeyon.ctp.user.dto.CtpAvoidLoginUserInfoDto;
import com.seeyon.ctp.user.dto.CtpUserSpiThirdTokenDto;
import com.seeyon.ctp.user.dto.SpiWebAuthenticationDetailInfo;
import com.seeyon.ctp.user.dto.ThirdTokenDto;
import com.seeyon.ctp.user.util.CtpUserSpiUtils;
import lombok.extern.slf4j.Slf4j;

import javax.servlet.http.HttpServletRequest;
import java.util.Map;

/**
 * 免登 中间页面模式接口实现<br/>
 * 注意：<br/>
 * 类中不需要加 @Service 方法， 也不能使用 @Autowired 注解， 无法获取到对应实现。需要使用 CtpUserSpiUtils#getInstance() 方法获取实例<br/>
 * request 对象获取： CtpUserSpiUtils#getRequest()<br/>
 * nacos 等配置信息获取： CtpUserSpiUtils#getPropertyByName(java.lang.String)，通过配置的 key 直接获取
 */
@Slf4j
public class ThirdSsoMiddlePageProviderService implements CtpAvoidLoginMiddlePageProviderService {
    
    /**
     * 返回客户端标识,与免登地址中 type 参数的值一致
     */
    @Override
    public String getClientId() {
        return "ncoa";
    }

    /**
     * 从请求中提取参数并获取用户信息
     *
     * @param code    三方追加的 code 的值
     * @param extData 三方追加的扩展参数
     * @return 用户属性信息
```

注意：完成接口开发并构建成功后需要重启【ctp-user】服务才能进行后续功能验证

### 2.3. SSO地址组装

```
【V8平台访问域名】/oauth/home?
mobile=%2Fmain-mobile%2Fportal    # url encode 后重定向地址
&web=%2Fmain%2Fportal             # url encode 后重定向地址
&businessType=outsider            # 固定值
&type=ncoa                        # 三方系统sso标识(建议用三方系统名如：cas\v5\eas\ncoa)
&dynamicField=code                # 追加code的key值，这里为code,如追加ticket则这里值为ticket
&code=2403832009216967675         # 三方追加的值
```

说明：在浏览器地址栏访问以上URL即可免登进入V8平台页面

## 3 携带自定义参数

### 3.1 接口说明

接口名称：com.seeyon.ctp.user.api.avoidlogin.CtpAvoidLoginClientModeProviderService

### 3.2 接口实现

### 3.3 SSO地址组装

## 4 参数配置与获取

### 4.1 参数配置

进入NACOS，在ctp-user微服务下配置 动态参数

### 4.2 参数获取

需要通过工具类获取参数值

## 5 多帐号SSO配置

通过免登地址，登录 A 账号查看待办后再打开 B 账号的待办，不会切换账号。web 端解决方法：在nacos的ctp-user微服务下添加以下配置

## 6、示例代码

cip-spi-user-avoid-thirdavoid.zip
(63 KB)

DemoCtpAvoidLoginClientModeProviderService.java
(3 KB)

## 7、认证失败跳转自定义错误页面

抛出CtpUserSpiSsoException异常，平台会自动跳转到对应的html，示例见下图
