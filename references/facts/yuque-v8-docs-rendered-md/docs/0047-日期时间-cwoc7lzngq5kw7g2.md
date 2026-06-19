---
title: "日期时间"
source: "https://www.yuque.com/seeyonkk/v8/cwoc7lzngq5kw7g2"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 日期时间

> Source: https://www.yuque.com/seeyonkk/v8/cwoc7lzngq5kw7g2

## （五）日期时间

1
【强制】后端通常不需要日期格式化转换，一般以long型传输到前端做多时区处理，若必须使用时请用平台提供的工具类com.seeyon.boot.util.DateUtils，如日志输出？

2
【强制】获取当前毫秒数：System.currentTimeMillis(); 而不是 new Date().getTime()。
  
说明：如果想获取更加精确的纳秒级时间值，使用 System.nanoTime 的方式。在 JDK8 中，针对统计时间等场景，推荐使用 Instant 类。

3
【强制】不允许在程序任何地方中使用：1）java.sql.Date。 2）java.sql.Time。3）java.sql.Timestamp。
  
说明：第 1 个不记录时间，getHours()抛出异常；第 2 个不记录日期，getYear()抛出异常；第 3 个在构造方法 super((time/1000)*1000)，在 Timestamp 属性 fastTime 和 nanos 分别存储秒和纳秒信息。
  
反例： java.util.Date.after(Date)进行时间比较时，当入参是 java.sql.Timestamp 时，会触发 JDK BUG(JDK9 已修复)，可能导致比较时的意外结果。

4
【强制】不要在程序中写死一年为 365 天，避免在公历闰年时出现日期转换错误或程序逻辑错误。

正例：

```
// 获取今年的天数
int daysOfThisYear = LocalDate.now().lengthOfYear();
// 获取指定某年的天数
LocalDate.of(2011, 1, 1).lengthOfYear();
```

反例：

```
// 第一种情况：在闰年 366 天时，出现数组越界异常
int[] dayArray = new int[365];
// 第二种情况：一年有效期的会员制，今年 1 月 26 日注册，硬编码 365 返回的却是 1 月 25 日
Calendar calendar = Calendar.getInstance();
calendar.set(2020, 1, 26);
calendar.add(Calendar.DATE, 365);
```

5
【推荐】避免公历闰年 2 月问题。闰年的 2 月份有 29 天，一年后的那一天不可能是 2 月 29 日。

6
【推荐】使用枚举值来指代月份。如果使用数字，注意 Date，Calendar 等日期相关类的月份 month 取值在 0-11 之间。
  
说明：参考 JDK 原生注释，Month value is 0-based. e.g., 0 for January.
  
正例： Calendar.JANUARY，Calendar.FEBRUARY，Calendar.MARCH 等来指代相应月份来进行传参或比较。
