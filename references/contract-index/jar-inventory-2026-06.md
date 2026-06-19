# Jar 库存清单（2026-06 发现）

> 本文件记录曾用于 FACT 升级的 artifact/version/locator 模式。路径必须视为用户现场输入，不代表通用默认仓库。
> 同一用户可能同时有十多个项目仓库；每条 locator 必须带 `repo_key`，不能只写单一全局仓库占位。

## Repo Key 模型

`repo_key` 是仓库/项目来源标识，用于区分多个现场仓库。命名建议：

```yaml
repositories:
  <repo_key>:
    project_label: <项目/客户/环境标识，例如 project-a / project-b / dev-repo-01>
    kind: maven-local | maven-remote | project-lib | third-jar | source-tree
    root: <由用户提供或从工程配置发现的路径/URL>
    maven_settings: <可选，settings.xml 路径>
    repository_ids: [<可选，私服 id / mirror id>]
    note: <可选说明>
```

规则：

1. `repo_key` 必须由用户提供或由 agent 从目标工程配置中发现后命名。
2. 不假设固定盘符、固定仓库名、固定客户名。
3. `artifact/version/path` 只能作为该 repo_key 下的 locator，不升级为通用默认。
4. 生成/验证某个项目时，报告里必须写明使用了哪些 `repo_key`。
5. 仓库数量不设上限；按项目、客户、环境、离线包分别登记。

## Artifact locator 格式

推荐格式：

```yaml
artifact_locator:
  repo_key: <repo_key>
  groupId: com.seeyon
  artifactId: <artifactId>
  version: <version>
  packaging: jar
  relative_path: com/seeyon/<artifactId>/<version>/<artifactId>-<version>.jar
  evidence: FACT | OBSERVATION | HYPOTHESIS
  used_for: <domain/spi>
```

## 已确认 artifact/version 模式

| repo_key | Artifact | 版本 | Locator 模式 | 用途 |
|----------|----------|------|--------------|------|
| `<repo_key>` | boot-starter-file | 5.3.358 | `{repo.root}/com/seeyon/boot-starter-file/5.3.358/boot-starter-file-5.3.358.jar` | file-storage/storage-spi FACT |
| `<repo_key>` | boot-starter-nacos | 5.3.358 | `{repo.root}/com/seeyon/boot-starter-nacos/5.3.358/boot-starter-nacos-5.3.358.jar` | infra-config-registry FACT |
| `<repo_key>` | bpm-facade | 5.3.374 | `{repo.root}/com/seeyon/bpm-facade/5.3.374/bpm-facade-5.3.374.jar` | workflow-document/bpm FACT |
| `<repo_key>` | cip-connector-api | 5.3.286 | `{repo.root}/com/seeyon/cip-connector-api/5.3.286/cip-connector-api-5.3.286.jar` | datasource + entry-menu-mobile FACT |
| `<repo_key>` | ctp-user-api | 5.3.351 | `{repo.root}/ctp-user-api-5.3.351.jar` 或 Maven 标准路径 | auth-sso 多个 SPI FACT |
| `<repo_key>` | organization-facade | 5.3.368 | `{repo.root}/com/seeyon/organization-facade/5.3.368/organization-facade-5.3.368.jar` | account-org-security/address-book FACT |

## 缺失 Jar（阻塞 OBS → FACT 升级）

| repo_scope | Artifact | 阻塞的 SPI | 备注 |
|------------|----------|-----------|------|
| `<repo_key...>` | boot-starter-encrypt | crypto/digest, crypto/symmetric | 未在已检查的 repo_key 集合中找到 |

## 历史口径修正

`cip-provider-api / provider-service` 不是 active contract target；能力通道按 `cip-capability-api` 与 28 个能力文件夹治理。后续不要再按该历史 artifact 判定 capability-channel 冻结。

## 使用规则

查找 jar 时优先搜索用户提供的 repo_key 集合与目标项目随附 `lib/third-jar` 目录，按 artifactId 匹配；不要假设固定盘符或固定仓库名。

输出报告示例：

```yaml
contract_sources:
  - repo_key: project-a-maven
    artifact: com.seeyon:ctp-affair-facade:5.3.315
    locator: project-a-maven!/com/seeyon/ctp-affair-facade/5.3.315/ctp-affair-facade-5.3.315.jar
    evidence: FACT
```
