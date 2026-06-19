---
title: "平台ES组件"
source: "https://www.yuque.com/seeyonkk/v8/qdmbldy183qwffre"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 平台ES组件

> Source: https://www.yuque.com/seeyonkk/v8/qdmbldy183qwffre

作者：陈晓东

时间：2025-08-18

##### 1、Maven依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>boot-starter-elasticsearch</artifactId>
</dependency>
```

##### 2、参数配置

```
seeyon:
  elasticsearch:
    enable: true #是否启用
    hosts: 10.3.9.109:9200,10.3.9.193:9200,10.3.9.194:9200 #es集群地址
```

本地调试可将ES调试日志打开：

```
logging:
  level:
    org:
      springframework:
        data:
          elasticsearch:
            client:
              WIRE: trace
```

##### 3、扫描规则

###### 3.1 Entity扫描

服务启动时默认扫描com.seeyon.**.elasticsearch.index包下的实体类映射，请将对应ES索引的实体类定义到此目录下

###### 3.2 Repository扫描

服务启动默认扫描com.seeyon.**.elasticsearch.repository包下的repository，请将对应ES索引的repository定义到此目录下

##### 4、使用说明

###### 4.1 实体定义

```java
@Getter
@Setter
@Document(indexName = "app_definition" , shards = 5, createIndex = false)
public class AppDefinition extends BaseElasticsearchIndex {
    /**
     * appId
     */
    @Field(name = "app_id",type = FieldType.Keyword)
    private String appId;

    /**
     * 应用名称
     */
    @Field(name = "app_name",type = FieldType.Keyword)
    private String appName;

    /**
     * 发布时间
     */
    @Field(name = "publish_time", type = FieldType.Date, format = DateFormat.date_optional_time)
    private Date publishTime;

    /**
     * boolean
     */
    @Field(name = "is_success", type = FieldType.Boolean)
    private boolean isSuccess;
}
```

@Document：映射到ES的索引(indexName=索引名，createIndex=是否启动服务时创建索引)<br>

@Field：字段（name=字段名，type=对应es的字段类型，详细见FieldType枚举类）<br>

注意：日期字段需要明确指定type = FieldType.Date,format = DateFormat.date_optional_time<br>

文本字段必须指定为type = FieldType.Keyword<br>

其他类型字段按实际类型对应ES的数据类型即可。

###### 4.2 Repository接口定义

```
public interface AppDefinitionRepository extends BaseElasticsearchRepository<AppDefinition> {}
```

注意：Repository接口需要继承BaseElasticsearchRepository。

###### 4.3 Repository接口使用

BaseElasticsearchRepository实现了基础能力。

注意：updateByCriteria,deleteByCriteria,updateByStringQuery,deleteByStringQuery

上面的方法是基于elasticsearch脚本的实现。当匹配的结果集很大时性能较差，慎重使用

###### 4.4 使用实例

##### 5、快捷查询
