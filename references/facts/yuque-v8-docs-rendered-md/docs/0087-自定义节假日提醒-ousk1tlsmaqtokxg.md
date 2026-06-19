---
title: "自定义节假日提醒"
source: "https://www.yuque.com/seeyonkk/v8/ousk1tlsmaqtokxg"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 自定义节假日提醒

> Source: https://www.yuque.com/seeyonkk/v8/ousk1tlsmaqtokxg

作者：陈晓东

时间：2026.6.2

适用版本：3.10及以上版本

使用场景：当标品的节假日提醒不满足需求时，客开通过实现SPI的方式进行自定义扩展

# 1、SPI开发

SPI开发规范，参考：
开发准备

# 2、添加依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>portal-facade</artifactId>
  <version>3.10.0</version>
</dependency>
```

# 3、客开代码实现

```
public interface AbstractHolidayReminderService {
    /**
     * 返回需要提醒的人员
     *
     * @param userId          当前人员id
     * @param client          客户端类型 PC，MOBILE
     * @param holidayContents 带过滤提醒列表
     */
    List<HolidayConfigDto> remind(String userId, String client, List<HolidayConfigDto> holidayContents);

    /**
     * 记录当前人员点击列表
     *
     * @param userId          当前人员id
     * @param client          客户端类型 PC，MOBILE
     * @param holidayContents 查看了哪些内容
     */
    void record(String userId, String client, List<HolidayConfigDto> holidayContents);

    default String remindType() {
        return "birthday";
    }

    default String remindDescription() {
        return "生日";
    }
}
```

HolidayConfigDto属性：

```java
public class HolidayConfigDto extends BaseDto {
    @DtoAttribute(value = "ID")
    private Long id;
    @DtoAttribute(value = "标题")
    private String title;
    @DtoAttribute(value = "提醒类型 birthday", example = "birthday")
    private String remindType;
    @DtoAttribute(value = "指定范围", example = "")
    private String useScope = "";
    @DtoAttribute(value = "开始时间")
    private Date startTime;
    @DtoAttribute(value = "结束时间")
    private Date endTime;
    @DtoAttribute(value = "排序号", example = "")
    private Integer sortNo;
    @DtoAttribute(value = "提醒内容-内容类型", example = "")
    private String contentType;
    @DtoAttribute(value = "提醒内容-提醒内容", example = "")
    private List<HolidayContentDto> content;
}
```

# 4、重启服务

重启portal服务
