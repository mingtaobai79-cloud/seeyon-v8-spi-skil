# Seeyon V8 SPI Skill 架构审计报告

Date: 2026-06-20 03:09:41
Scope: active skill architecture：`SKILL.md` + `references/**`，排除 raw facts 的原始证据语义，只检查入口、断链、状态口径、重复/错误文件和验证链路。

## 1. 结论

结论：PASS（除冻结 SPI 外，active skill 架构已完成）。

| 项 | 结果 |
|----|------|
| 顶层入口 | PASS：`SKILL.md` 只做路由、证据规则、工程边界 |
| references 顶层 md | PASS：6 个以内，当前 6 个 |
| 域目录 | PASS：12 个业务域均有 `index.md` |
| SPI 子目录 | PASS：所有 active SPI 子目录均有 `README.md` + `constraints.md` |
| capability-channel 口径 | PASS：28 项能力拆分治理；不再把 historical provider-service 作为 active frozen SPI |
| frozen 口径 | PASS：冻结只保留 7 个 active 阻塞 SPI |
| active markdown 断链 | PASS：0 个真实断链；占位符路径不作为实际链接 |
| 旧全域 closeout 测试文档 | PASS：已清理，入口无引用 |
| 生成链路 | PASS：validator 与 Contract Index 可运行 |
| 重复/错误文件 | PASS：未发现影响 active 路由的重复/错误文件 |

## 2. 当前状态

| 类别 | 数量 |
|------|------:|
| 总域数 | 12 |
| 总 SPI / 能力项 | 55 |
| Active frozen SPI | 7 |
| 非冻结已完成项 | 48 |

### Active frozen SPI

| 域 | SPI | 阻塞 |
|----|-----|------|
| account-org-security | auth-check | 缺更高版本 `ctp-user-api`，现有版本找不到 `AbstractAuthenticationCheckService` |
| auth-sso | login-pre-portal | 缺 `boot-starter-login-pre-portal` / 预置 jar，非标准 SPI |
| crypto | digest | 缺 `boot-starter-encrypt` |
| crypto | symmetric | 缺 `boot-starter-encrypt` |
| file-storage | storage-interceptor | 缺更高版本 `boot-starter-file`，现有版本找不到 `StorageInterceptorSpi` |
| system-variable | system-variable-spi | 现有 `boot-starter-systemvariable` / `boot-starter-formula` 不含目标 SPI 接口 |
| workflow-document | edoc | 缺 `edoc-facade` / 目标接口未 FACT |

## 3. capability-channel 口径

当前金标准：

- active 结构是 `references/capability-channel/<28 capability>/`。
- active 统计是 28 项能力，状态为 ✅ 28。
- `provider-service` / `cip-provider-api` 只属于历史错误聚合口径，不作为 active SPI、不进入冻结清单、不作为生成路由。
- 生成大工程时使用一个 `spi-capability-channel` 模块承载 28 个 `Custom*ProviderService`，不拆 28 个 Maven 子模块。

## 4. 验证记录

执行结果：

```text
python -m py_compile references/generation/tools/validate_generated_spi_project.py references/contract-index/tools/contract_index_status.py
python references/contract-index/tools/contract_index_status.py

STATUS: READY
```

生成审计版大工程验证：

```text
AUDIT_CHECK classes=69 fail=0 warn=0
```

## 5. 后续维护

1. 新 jar/source 进入时，只升级对应子域 FACT，不回填大段实现到入口。
2. 冻结项除非用户明确解冻或补 artifact，否则不推进。
3. 每次改入口、workflow、status 后复跑：断链检查、py_compile、contract_index_status。
4. capability-channel 禁止恢复 `provider-service/` 或版本总账文档。
