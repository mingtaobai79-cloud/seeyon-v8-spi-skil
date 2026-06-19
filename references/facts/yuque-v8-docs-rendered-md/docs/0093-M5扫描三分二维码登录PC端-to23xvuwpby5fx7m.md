---
title: "M5扫描三分二维码登录PC端"
source: "https://www.yuque.com/seeyonkk/v8/to23xvuwpby5fx7m"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# M5扫描三分二维码登录PC端

> Source: https://www.yuque.com/seeyonkk/v8/to23xvuwpby5fx7m

作者：陈晓东

时间：2026.5.28

适用版本：3.12及以上版本

使用场景：PC端访问V8的登录页，通过SPI扩展获取三方的二维码展示在登录页，操作人员使用M5扫描二维码进行PC端登录

面向组织全生命周期的协同管理平台
平台汇聚智慧协同创造价值
这个登录二维码可以通过SP自定义
9领航版
......10+FIREF0X90+进行访列间
扫码登录
客户端下载
推岁田CHROME90+EDOE90+SAF

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
public abstract class AbstractLoginQrCodeService {
    /**
     * 认证类型
     *
     * @return
     */
    public abstract String getQrCodeAuthenticationType();
    /**
     * 生成二维码
     *
     * @return  二维码信息
     */
    public abstract CtpLoginQrCodeDto generateQrCode();
    /**
     * 轮训二维码结果
     *
     * @param qrValue  二维码值
     * @return         人员id
     */
    public abstract QrcodeResultDto roundScanResult(String qrValue);
}
```

getQrCodeAuthenticationType返回的类型，用于表示采用的是哪种登录类型，默认是‘default’，表示使用的是V8的二维码登录；generateQrCode返回三方生成的二维码，用于展示在页面上供客户app扫描；roundScanResult方法用于轮训扫描二维码过后的一个结果，返回是否是登录成功

```java
public class CtpLoginQrCodeDto extends BaseDto {
    private static final long serialVersionUID = 2565302127531211448L;
    @DtoAttribute("二维码值")
    private String qrValue;
    @DtoAttribute("业务id")
    private Long objectId;
    @DtoAttribute("过期时间")
    private Date expireTime;
    @DtoAttribute("二维码存储的storageKey")
    private String storageKey;
    @DtoAttribute("二维码base64数据")
    private String imageStr;
}
```

# 4、重启服务

重启ctp-user服务

# 5、参考示例

参考标品示例：

BaiChengLoginQrCodeServiceImpl.java
(6 KB)
