---
title: "自定义事项中心列表查询条件"
source: "https://www.yuque.com/seeyonkk/v8/wd0xlssvr25new8k"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 自定义事项中心列表查询条件

> Source: https://www.yuque.com/seeyonkk/v8/wd0xlssvr25new8k

作者：陈晓东

时间：2026.6.2

适用版本：3.15及以上版本

使用场景：当事项中心列表、栏目查询条件不满足客户需求时，可以通过实现SPI的方式，自定义查询条件、排序规则

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
public interface AbstractAffairSearchService {
    /**
     * 设置排序字段
     * @param sort 已有的排序规则
     * @return
     */
    default Sort getSearchOrder(Sort sort) {
        return sort;
    }

    /**
     * 设置查询条件
      * @param wrapper 当前wrapper条件
     * @return 修改后的wrapper条件
     */
    default Wrapper getSearchWrapper(Wrapper wrapper) {
        return wrapper;
    }
}
```

# 4、生效范围

对事项中心所有的列表、栏目生效

# 5、重启服务

重启ctp-affair服务
