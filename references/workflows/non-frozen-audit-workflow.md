# 非冻结域审计工作流

> 从 SKILL.md 下沉。冻结域不修改，只审计非冻结域。

### 非冻结域审计工作流

当用户说“冻结先不动，审计其他域”时：

1. 从 `references/index.md` 的冻结清单提取 `(domain, spi)`，本轮不修改这些 SPI 的 README/constraints/shared 文件。
2. 只遍历非冻结 SPI，检查：`README.md`、`constraints.md`、Evidence 头、接口/FQCN、方法表、代码骨架、Nacos、spring.factories、spi_info.json、重启/scope、索取清单。
3. 输出 A/B/C 分级：
   - A：生成所需结构完整；允许段落级 OBSERVATION，但必须标明。
   - B：可用但缺关键可读结构（例如显式方法表）。
   - C：缺 README/constraints 或缺核心生成依据。
4. 同步做 hygiene 检查：references 顶层 md 数、旧版路径残留（SSO/MQ/legacy 旧目录名）。
5. 结果落盘到 `references/audits/non-frozen-domain-audit-YYYY-MM-DD.md`，报告必须包含数量、冻结跳过清单、A/B/C 列表、Evidence 注意点、下一步最高 ROI。
6. 除非用户明确要求修复，不要在审计轮顺手补写 B/C 文件；先给报告和建议。

**常见过期引用**：旧 SSO 路径统一改到 `references/auth-sso/`；旧 MQ 路径统一改到 `references/mq/`；legacy 聚合目录已删除。
