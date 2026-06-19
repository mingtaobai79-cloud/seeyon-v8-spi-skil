---
title: "缓存组件"
source: "https://www.yuque.com/seeyonkk/v8/cmy7zxskydsof4ag"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 缓存组件

> Source: https://www.yuque.com/seeyonkk/v8/cmy7zxskydsof4ag

作者：陈晓东

时间：2025-08-15

##### 1、组件介绍

cache组件提供采用SpringCache注解方式使用分布式缓存的能力

对于spring应用，使用分布式缓存的特点如下：

1
数据查询的性能优化

2
响应结果为null时不缓存数据。 如果需要防止数据不存在时的缓存穿透时，建议返回空对象而不是null

3
当缓存操作异常时不抛出异常

##### 2、配置说明

```
seeyon:
      cache:
        client-type: jedis # redis客户端引擎， 可选： jedis、lettuce
        redis-nodes: 127.0.0.1:6379,127.0.0.1:6380,127.0.0.1:6381 # 单机配置单节点；集群配置多节点
        redis-password: Seeyon123456
        redis-database: 0       
        expire-time: 1800 # 过期时间，单位：秒
```

##### 3、组件使用

基于spring注解使用缓存能力

```
// 先从缓存中取user 
@Cacheable(value = "cacheName",key = "#id")   
public Object findUser( long id ) {    
return user;    
}    

// 更新缓存user    
@CachePut(value="cacheName", key="#user.id")        
public Object updateUser(Object user){     
return  user ;      
}      

// 从缓存中删除user
@CacheEvict(value="cachaName")   
public void deleteUser(long id){    
return ;   
}
```

基于redisTemplate使用redis数据结构的缓存读写

```
// 获取redisTemplate bean实例 
@Autowired
private RedisTemplate redisTemplate;

// 对简单的 key-value 的封装
ValueOperations val = redisTemplate.opsForValue();
val.set("K001", "V001);
Object cachValue = val.get("test_key");
// 详细的其他方法请参考 org.springframework.data.redis.core.ValueOperations

// 对hash结构的操作 
HashOperations hash =  redisTemplate.opsForHash();
hash.put("map", "key", "value");
hash.delete("map", "key");
// 详细的其他方法请参考 org.springframework.data.redis.core.HashOperations

// 对链表结构的操作，详细的方法请参考 org.springframework.data.redis.core.ListOperations
ListOperations list = redisTemplate.opsForList();

// 对集合结构的封装，详细的方法请参考 org.springframework.data.redis.core.SetOperations
SetOperations set = redisTemplate.opsForSet();

// 对有序集合结构的操作，详细的方法请参考 org.springframework.data.redis.core.ZSetOperations
ZSetOperations zset = redisTemplate.opsForZSet();
```

key规范

保存到redis中的key的规范如下：tenantId:appName:cacheName（appId作为前缀）::cacheKey

工具

应用在采用redisTemplate进行redis的操作，可通过CacheUtils获取完整的Key，具体下：

```java
public class CacheUtils {

    /**
     * 获取完整的Key，自动拼接了tenantId、appName、appId（appName简称，用于合并部署）
     */
    public static String getCompleteCacheKey(String cacheName, String cacheKey) {
        return SystemEnvironment.getEnv() + Constants.COLON + RequestContext.get().getTenantId() + Constants.COLON + Apps.getAppName() + Constants.COLON + Apps.getBuildVersion() + Constants.COLON + cacheName + Constants.COLON + Constants.COLON + cacheKey;
    }

    /**
     * 获取完整的Key，自动拼接了tenantId、appName以及指定的BuildVersion（appName简称，用于合并部署）
     */
    public static String getCompleteCacheKeyWithBuildVersion(String cacheName, String cacheKey, String buildVersion) {
        return SystemEnvironment.getEnv() + Constants.COLON + RequestContext.get().getTenantId() + Constants.COLON + Apps.getAppName() + Constants.COLON + buildVersion + Constants.COLON + cacheName + Constants.COLON + Constants.COLON + cacheKey;
    }

    /**
     * 不拼接tenantId
     */
    public static String getCompleteCacheKeyWithoutTenantId(String cacheName, String cacheKey) {
        return SystemEnvironment.getEnv() + Constants.COLON + Apps.getAppName() + Constants.COLON + Apps.getBuildVersion() + Constants.COLON + cacheName + Constants.COLON + Constants.COLON + cacheKey;
    }

    /**
     * 不拼接appId
     */
    public static String getCompleteCacheKeyWithoutAppName(String cacheName, String cacheKey) {
        return SystemEnvironment.getEnv() + Constants.COLON + RequestContext.get().getTenantId() + Constants.COLON + cacheName + Constants.COLON + Constants.COLON + cacheKey;
    }

    /**
     * 不拼接tenantId和appName
     */
    public static String getCacheKeyWithoutTenantIdAndAppName(String cacheName, String cacheKey) {
        return SystemEnvironment.getEnv() + Constants.COLON + cacheName + Constants.COLON + Constants.COLON + cacheKey;
    }
```
