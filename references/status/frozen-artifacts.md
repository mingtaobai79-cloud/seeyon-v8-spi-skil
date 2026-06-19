# 冻结 Artifact 清单

> 从 SKILL.md 下沉。状态类信息，随 artifact 可用性更新。

## 已知缺失 Artifact（🧊 冻结清单）

以下 artifact 在已检查的用户私有仓库中未找到，遇到时直接标记 🧊 冻结：

| Artifact | 阻塞的 SPI | 域 |
|----------|-----------|-----|
| `boot-starter-encrypt` | digest, symmetric | crypto |
| `ctp-user-loginpre` | login-pre-portal | auth-sso |
| `boot-starter-systemvariable` (高版本) | system-variable-spi | system-variable |
| `boot-starter-formula` (高版本) | system-variable-spi | system-variable |
| `edoc-facade` | edoc | workflow-document |
| `ctp-user-api` (更高版本) | auth-check | account-org-security |
| `boot-starter-file` (更高版本) | storage-interceptor | file-storage |

**冻结语义**：用户说"冻结"时，意思是停止该域的工作推进，不修改已冻结域的文件内容（除非用户明确要求）。冻结的 SPI README.md 头部必须加 🧊 banner。

## 历史口径修正

`cip-provider-api` / `provider-service` 是历史聚合口径，已被 `cip-capability-api` 基线下的 28 个能力文件夹替代。它不属于 active frozen SPI，不进入生成路由，也不计入冻结数量。
