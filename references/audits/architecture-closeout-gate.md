# Seeyon V8 SPI Skill 架构收口审计 Gate

用于用户要求“看看这个 skill 架构是不是收口、入口有没有问题、引用有没有错、有没有重复/错误文件、除了冻结是否都完成了”时。

## 1. 审计分层

只把 active skill 当当前事实来源：

- active：`SKILL.md` + `references/**`，但排除 raw facts / archive / 历史归档。
- raw facts：只作为证据库，不为了 grep 归零清理原始资料。
- archive / superseded audit：只保留历史，不作为当前状态来源。

若历史审计报告含旧计数或旧口径，必须加 tombstone / superseded note，避免后续 agent 误读为当前状态。

## 2. 必查项

1. 入口：`SKILL.md` 只做路由、证据规则、工程边界，不塞实现细节。
2. 顶层 references：顶层 `.md` 保持在 hygiene 目标内；当前目标是 6 个以内。
3. 域目录：每个 active 业务域必须有 `index.md`。
4. SPI 子目录：每个 active SPI 子目录必须有 `README.md` + `constraints.md`；`shared/` 例外。
5. 链路：入口路由到 `references/workflows/spi-generation-workflow.md` 和 `references/generation/tools/validate_generated_spi_project.py`。
6. 断链：active markdown link check 必须为 0；占位符、glob、纯锚点、http/https、fenced code block 不算真实断链。
7. 旧口径残留：旧 closeout 测试文档、旧 frozen 计数、旧 provider-service 聚合口径不得出现在 active 当前状态里。
8. 验证：`py_compile` validator / contract_index_status；Contract Index 输出 `READY` 或明确 `CONFIG_NEEDED`。

## 3. Capability Channel 金标准

- active 结构是 `references/capability-channel/<28 capability>/`。
- active 统计是 28 项能力，状态为 ✅ 28。
- `provider-service` / `cip-provider-api` 只属于历史错误聚合口径，不作为 active SPI、不进入冻结清单、不作为生成路由。
- 生成大工程时默认使用一个 `spi-capability-channel` 模块承载 28 个 `Custom*ProviderService`，不拆 28 个 Maven 子模块，除非用户明确要求。

## 4. 全 SPI 审计版大工程生成口径

当用户要求“按实际业务审计、自己编几个实际业务、覆盖所有 SPI 重新生成”时：

1. 不生成测试型 closeout md；测试/临时报告不要挂 active skill 路由。
2. 每个 SPI / 能力项都要有实际业务场景、日志点、method skeleton、Evidence 标记。
3. FACT / FACT_PARTIAL：保留真实 `implements` / `extends`。
4. FROZEN：不要硬 `implements` / `extends` 未 FACT 接口；保留审计可见方法和冻结说明，避免伪编译假象。
5. capability-channel 放进一个 `spi-capability-channel` 模块，内部 28 个 provider 实现。
6. 输出 manifest + audit checker；checker 至少验证类存在、方法可见、日志点、frozen 不硬关联、场景注释。

## 5. 文档更新规则

发现状态口径变化时，不能只修生成物：

- 更新 `references/index.md` 的总数、状态、冻结清单。
- 更新 `references/status/frozen-artifacts.md`。
- 更新 `references/status/evidence-summary.md`，让它转发到最新状态来源。
- 更新 contract inventory 中旧 artifact 阻塞说明，避免历史缺失 jar 继续阻塞 active 路由。
- 旧审计报告若会误导，改成 superseded/tombstone，而不是继续保留旧表当当前事实。

## 6. PASS 判定

只有同时满足以下条件才能报 PASS：

- active markdown 断链 0。
- active 结构缺失 0。
- 顶层 references `.md` 不超 hygiene 目标。
- 旧 closeout / provider-service / stale frozen count 等当前口径残留为 0。
- validator 和 Contract Index 检查完成。
- 除冻结 SPI 外，所有 active 域均有可路由的 README / constraints / index。

否则只能报 PARTIAL，并列出必须修的结构债。