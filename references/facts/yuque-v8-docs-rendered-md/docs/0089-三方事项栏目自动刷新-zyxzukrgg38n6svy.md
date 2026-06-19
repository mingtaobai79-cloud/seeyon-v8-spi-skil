---
title: "三方事项栏目自动刷新"
source: "https://www.yuque.com/seeyonkk/v8/zyxzukrgg38n6svy"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 三方事项栏目自动刷新

> Source: https://www.yuque.com/seeyonkk/v8/zyxzukrgg38n6svy

作者：陈晓东

时间：2026.6.1

适用版本：3.15及以上版本

使用场景：刷新客开事项中心栏目

TODO： 有问题待完善

# 1、SPI开发

SPI开发规范，参考：
开发准备

# 2、添加依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>ctp-affair-facade</artifactId>
  <version>3.15.0</version>
</dependency>
```

# 3、客开实现方法

```
/**
 * 事项刷新服务类
 *
 * @author liu xiong
 * @date 2024/10/15
 */
public abstract class AbstractAffairRefreshService {
    /**
     * 刷新事项之前处理
     *
     * @param userIds   用户id
     * @return
     */
    public abstract void beforeSendPageRefreshMessage(final List<Long> userIds);

    /**
     * 刷新事项之后处理
     *
     * @param userIds   用户id
     */
    public abstract void afterSendPageRefreshMessage(final List<Long> userIds);
}
```
