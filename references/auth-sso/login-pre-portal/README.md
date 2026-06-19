> 🧊 **冻结状态** — 缺少必要 jar 包，接口/DTO 均为 OBSERVATION，无法升级到 FACT。
> 待获取对应 jar 后解除冻结。

# 登录前门户 / 预置 jar + Nacos

> Evidence: OBSERVATION ⚠️ — 语雀文档 + jar 反编译交叉验证。
> **jar 验证结果**：`ctp-user-loginpre` artifact 在 libs-release 仓库中未找到。
> 本场景不生成 SPI 实现代码，是平台预置 jar 通过 Nacos 启用。

## 场景

登录前门户是平台预置的 SPI jar，通过 Nacos 配置启用，不需要客开重新实现 SPI。

## 实现方式

不重新实现 SPI，按预置 jar + Nacos 启用。

## 预置 jar

```text
ctp-user-loginpre-3.15.66.jar
```

## Nacos 配置

```yaml
# ctp-user 微服务 Nacos 配置
seeyon:
  spi:
    enable: true
    spi-plugins:
    - oss:com.seeyon,ctp-user-loginpre,3.15.66
```

## jar 上传位置

上传到 OSS 或 Nacos 配置中心。

## 重启服务

ctp-user

## 阻塞项

1. `ctp-user-loginpre` artifact 在 libs-release 仓库中未找到
2. 需要确认 jar 来源（可能在其他仓库或需要手动上传）
3. 版本号 3.15.66 是否为最新
