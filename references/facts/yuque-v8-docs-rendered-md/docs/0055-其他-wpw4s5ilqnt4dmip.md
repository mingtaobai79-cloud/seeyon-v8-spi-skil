---
title: "其他"
source: "https://www.yuque.com/seeyonkk/v8/wpw4s5ilqnt4dmip"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 其他

> Source: https://www.yuque.com/seeyonkk/v8/wpw4s5ilqnt4dmip

## （十）其他

1
【强制】在使用正则表达式时，利用好其预编译功能，可以有效加快正则匹配速度。 

说明：不要在方法体内定义：Pattern pattern = Pattern.compile(规则);

2
【强制】注意 Math.random() 这个方法返回是double类型，注意取值的范围 0≤x<1（能够取到零值，注意除零异常），如果想获取整数类型的随机数，不要将x放大10的若干倍然后取整，直接使用Random对象的nextInt或者nextLong方法。
