---
title: "离线消息配置"
source: "https://www.yuque.com/seeyonkk/v8/xgzdb06lbk09z1gv"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 离线消息配置

> Source: https://www.yuque.com/seeyonkk/v8/xgzdb06lbk09z1gv

作者：潘峰
最后更新：2026-06-09

# 首先条件

1、V8能够访问外网，如果是内网环境，外网不能全面放开，则必须打开以下几个域名的访问

| 厂商 | 访问域名 (出方向) | 需加入服务器白名单的 IP (入方向/回调) | 关键端口 |
| --- | --- | --- | --- |
| 华为 | push-api.cloud.huawei.com https://oauth-login.cloud.huawei.com | 建议放行华为云相关网段 (无固定单一IP) | 443 (HTTPS) |
| 小米 | api.xmpush.xiaomi.com | 无强制固定 IP，建议通过域名验证 | 443 (HTTPS) |
| OPPO | api.push.oppomobile.com | 无强制固定 IP，依赖后台配置回调地址 | 443 (HTTPS) |
| vivo | api-push.vivo.com.cn | 117.50.33.0/25
116.198.10.0/24 等 (见上文列表) | 443 (HTTPS) |
| 苹果 | api.push.apple.com | 不需要 IP 白名单 | 443 (HTTPS) |

除了上面的域名，还有https://openapi-saas.seeyonv8.com，自动获取证书用

2、nacos里，cip-capability中，增加配置，是离线消息的总开关

```
seeyon:
  certificate:
    enable: true
```

### 场景一：使用M5

登录对应租户管理员账号
【集成平台】-【基础能力接入】-【能力配置】-【离线消息】
选择离线消息通道，启用即可

### 场景二：独立上架的app

这里独立上架的app，只能是M5的套娃，就是内核还得是M5，外面包装一层变成了新的app。

1
使用system-admin登录后台，进入【集成平台】-【基础能力接入】-【能力配置】

配置内容实例：其中除了 com.seeyon.a9.SplashActivity，都需要更改为项目对应app的

<img width="1896">

注意：ios目前代码只支持p12证书，不支持p8.
不匹配可能报错：TopicDisallowed

配置后启用，登录对应租户管理员账号，启用离线消息
然后重启cip-capability

### 场景三：不使用离线消息

有些项目没有外面连通，则需要关闭离线消息，nacos加如下配置
