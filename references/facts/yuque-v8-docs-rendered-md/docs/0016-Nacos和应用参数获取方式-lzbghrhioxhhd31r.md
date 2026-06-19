---
title: "Nacos和应用参数获取方式"
source: "https://www.yuque.com/seeyonkk/v8/lzbghrhioxhhd31r"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# Nacos和应用参数获取方式

> Source: https://www.yuque.com/seeyonkk/v8/lzbghrhioxhhd31r

作者：陈晓东

时间：2025-8-15

##### 1、nacos配置参数获取

###### 1.1 通过参数key进行获取

```
Apps.getApplicationContext().getEnvironment().getProperty("seeyon.datasource.database")
```

###### 1.2 通过注解获取

```java
@Data
@Component
@ConfigurationProperties(prefix = "seeyon.chenxd")
public class PeixunProperties {
    private String name;
    private Integer age;
    private String phone;
}
//在需要使用参数的类里面注入PeixunProperties
@Autowired
private PeixunProperties peixunProperties;
```

通过注解获取指定前缀下面的参数

SERVER-ADDR:$NAC0SADDR:127.0.0.1:8848
PASSWORD:$NACOSPASSWORD:NACOS
1ICHUPEIXUN6416391523783754075DEV
$NACOSUSERNAME:NACOS
H0NE:1838044748
DATABASE:
DATASOURCE:
USERNAME:
NAME:TOM
AGE:20
CHENXD:
CONFIG:
SEEYON:

###### 1.3 获取public和指定服务配置参数

```
//获取dataId是public下所有参数
String globalConfigStr = ConfigCenterService.getInstance().getGlobalConfigStr();
//使用平台提供的YamlUtil将参数转换成map
Map<String, Object> map = YamlUtil.yamlString2Map(globalConfigStr);
//获取指定服务的参数：例如获取dataId是ctp-affair下面的所有配置参数
String configStr = ConfigCenterService.getInstance().getConfigStr("ctp-affair");
```

##### 2、应用参数获取

如下图在应用中设置的参数

导入导出模板
培训川(1.0
定义对象
数据类型
扩展方案
外框模板
PEIXUNREN
页面模板
验证参数
门名称
选项集
陈晓东
字段集
流水号
默认值
二维码
编码
枚举
培训人
文本
设置
参数
菜单
应用
描述
车
立耳

如果跨应用获取应用参数可使用泛化调用方式获取，参考：

https://www.yuque.com/teamdocs/v8-client-kb/cyxtucgh7gn9gggc
