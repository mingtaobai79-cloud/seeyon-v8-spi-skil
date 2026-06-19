---
title: "通讯录人员列表/卡片自定义脱敏"
source: "https://www.yuque.com/seeyonkk/v8/ctibk0kn7mbotftd"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 通讯录人员列表/卡片自定义脱敏

> Source: https://www.yuque.com/seeyonkk/v8/ctibk0kn7mbotftd

作者：陈晓东

时间：2026.6.1

适用版本：5.0.2及以上版本

使用场景：通讯录人员列表/卡片展示的时候，平台的脱敏设置不满足客户的需求时可以通过SPI扩展自定义人员信息脱敏

# 1、SPI开发

SPI开发规范，参考：
开发准备

# 2、添加依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>ctp-organization-facade</artifactId>
  <version>5.0.2</version>
</dependency>
```

# 3、客开实现方法

```
/**
 * 通讯录扩展接口
 *
 * @author liu xiong
 * @date 2025/6/28
 */
public abstract class AbstractAddressBookSpiService {
    /**
     * 处理通讯录人员字段
     *
     * @param addressBookMemberDtos
     */
    public abstract void processMembersFieldPermission(List<AddressBookMemberDto> addressBookMemberDtos);
    /**
     * 处理人员卡片字段
     *
     * @param memberCard
     */
    public abstract void processMemberCardFieldPermission(List<Map<String, String>> memberCard);
}
```

# 4、重启服务

重启 organization 服务
