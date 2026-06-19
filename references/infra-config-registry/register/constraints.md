# 注册中心 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 域特有规则

1. 接口方法较多，文档截断了部分方法，需 jar 确认完整接口。
2. deregisterInstance 有 3 个重载，其中带 version 的有 default 实现。
3. 全局生效，部署后需重启所有服务。

## 禁止项

- 禁止在 registerInstance 中抛异常（会导致服务启动失败）。
- 禁止 getInstances 返回 null（应返回空 List）。

## 索取清单

```
P0:
1. RegisterServiceSPI 完整接口（文档截断）
2. AppInstanceDto 完整字段
3. NacosRegisterImpl.java 示例代码

P1:
4. boot-starter-nacos 现场版本
```
