---
title: "常量枚举"
source: "https://www.yuque.com/seeyonkk/v8/pesrxqxqa29onawb"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 常量枚举

> Source: https://www.yuque.com/seeyonkk/v8/pesrxqxqa29onawb

## （二）常量&枚举

### 常量定义

1
【强制】不允许任何魔法值（即未经预先定义的常量）直接出现在代码中。

反例：

```
String key = "Id#taobao_" + tradeId;       
cache.put(key, value); 
```

2
【强制】long或者Long初始赋值时，使用大写的L，不能是小写的l，小写容易跟数字1混淆，造成误解。 

说明：Long a = 2l; 写的是数字的21，还是Long型的2?

3
【推荐】不要使用一个常量类维护所有常量，按常量功能进行归类，分开维护。 

说明：大而全的常量类，非得使用查找功能才能定位到修改的常量，不利于理解和维护。 

正例：缓存相关常量放在类CacheConstant下；系统配置相关常量放在类ConfigConstant下。

### 枚举规范

1
【强制】枚举必须继承Messageable

●
数据库以code存储，使用smallint类型

●
如前端使用，国际化key为枚举值全路径，如：com.seeyon.demo.order.enums.OrderTypeEnum.IN_SALE=内销

```
public enum OrderTypeEnum implements Messageable {

    /**
     * 内销
     */
    IN_SALE(0),
    /**
     * 外销
     */
    OUT_SALE(1);

    private int code;

    OrderTypeEnum(int code) {
        this.code = code;
    }

    @Override
    public int code() {
        return this.code;
    }

}
```

2
【强制】所有的枚举类型字段必须要有注释，说明每个数据项的用途。

3
【参考】枚举类名建议带上Enum后缀，枚举成员名称需要全大写，单词间用下划线隔开。 

说明：枚举其实就是特殊的常量类，且构造方法被默认强制是私有。 

正例：枚举名字为ProcessStatusEnum的成员名称：SUCCESS / UNKNOWN_REASON。
