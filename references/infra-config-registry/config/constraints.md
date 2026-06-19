# 配置中心 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 域特有规则

1. 核心 3 个 get 方法必须实现，publish 和 listener 有 default 实现。
2. 返回的配置是字符串（YAML/JSON 格式），平台自行解析。
3. `getEngineName()` 必须实现，返回自定义引擎标识。
4. 全局生效，部署后需重启所有服务。

## 禁止项

- 禁止 get 方法返回 null（应返回空字符串）。
- 禁止在 listener 回调中做阻塞操作。

## 索取清单

```
P0:
1. ✅ ConfigServiceSPI FQCN → com.seeyon.boot.starter.nacos.spi.ConfigServiceSPI（FACT）
2. ✅ ConfigChangeProcess → com.seeyon.boot.starter.nacos.service.process.ConfigChangeProcess（FACT）
3. ✅ getEngineName 方法（FACT，语雀文档截断未包含）

P1:
4. boot-starter-nacos 现场版本
```
