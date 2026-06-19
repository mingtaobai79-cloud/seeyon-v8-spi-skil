# 登录前门户 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 域特有规则

1. 🧊 **冻结**：预置 jar 未找到，无法启用。
2. 本场景不需要客开实现 SPI。
3. 通过 Nacos 配置启用预置 jar。
4. jar 格式：`oss:groupId,artifactId,version`。

## 禁止项

- 禁止重复启用（Nacos 配置中只出现一次）。
- 禁止修改预置 jar 内容。

## 索取清单

```
P0（阻塞）:
1. ❌ ctp-user-loginpre artifact — libs-release 仓库中未找到
2. ❌ jar 来源确认 — 可能在其他仓库或需要手动上传
3. ❌ 版本号确认 — 3.15.66 是否为最新

P1:
4. Nacos 配置示例（完整）
5. OSS 上传路径规范
```
