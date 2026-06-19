---
title: "Mybatis组件"
source: "https://www.yuque.com/seeyonkk/v8/fwcydq3empfdxrso"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# Mybatis组件

> Source: https://www.yuque.com/seeyonkk/v8/fwcydq3empfdxrso

作者：陈晓东

时间：2025-08-15

##### 1、参数配置

```
seeyon:
  mybatis:
    enable: true #是否启用此组件
    settings:  #mybatis配置
    encryption: DES #实体加密算法(可选值：NONE)
    encrypt-fields: #实体加密字段配置
      com.seeyon.demo.order.domain.entity.OrderDetail:
        - productNo
        - productName
      com.seeyon.demo.order.domain.entity.OrderInfo:
        - orderNo
```

##### 2、DAO扫描

默认情况下，根据springboot特性，已经加入了当前应用的根包下的所有dao包的扫描（${appRootPackage}..dao）。

例如当前应用的根包路径为：com.seeyon.demo.customer

##### 3、SQL映射文件扫描

Mybatis增加单表增删改查通用能力，不用写一行sql语句，单表的操作能力全覆盖。

组件会在系统启动阶段组装org.apache.ibatis.mapping.SqlSource，扫描xxxDao.xml文件，配置文件位置为当前应用的src/main/resources/mybatis/下。

在xxxDao.xml文件中自定义sql语句(注意：id不能和BaseDao中的方法同名)，支持不同数据库语法。

##### 4、使用说明

###### 4.1定义Entity

```java
@Getter
@Setter
@Entity
@Table(name = "customer_type")
public class CustomerType extends BaseEntity {

    @Column(name = "name", columnDefinition = "VARCHAR(100) COMMENT '客户类型名称'")
    private String name;

}
```

注意：Entity需要继承BaseEntity，上面使用到了jpa annotation添加元数据，非数据库字段请添加transient关键字。

###### 4.2 定义DAO接口

```
public interface CustomerTypeDao extends BaseMybatisDao<CustomerType> {

}
```

注意：Dao接口需要继承BaseMybatisDao。

###### 4.3 使用DAO

```

/**
 * 插入一条记录
 *
 * @param entity 实体对象
 * @return
 */
int create(T entity);

/**
 * 批量插入多条记录
 *
 * @param list 实体对象列表
 * @return
 */
int createBatch(List<T> list);

/**
 * 更新一条记录
 *
 * @param entity 实体对象
 * @return
 */
int update(T entity);
```

BaseMybatisDao提供了基础能力，单表操作告别sql。支持指定字段或排除字段

更多能力参考com.seeyon.boot.starter.mybatis.BaseMybatisDao接口

###### 4.4 Condition使用，只支持与（and）操作

###### 4.5 Wrapper使用，支持复杂操作：或(or)、distinct、自定义查询字段、自定义排除的查询字段、排序字段、notNull、forUpdate

###### 4.6 扩展接口

●
注意：配置文件位置在src/main/resources/mybatis/OrderInfoDao.xml

●
resultType可使用别名，需要在entity上增加注解@Alias

●
不同数据库语法支持，需要设置databaseId
