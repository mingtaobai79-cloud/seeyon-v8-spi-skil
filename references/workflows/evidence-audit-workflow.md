# Evidence 批量审计工作流

> 从 SKILL.md 下沉。用于全量审计域 Evidence 状态。

## Evidence 批量审计工作流

当需要全量审计所有域状态时：

1. 遍历所有域 `index.md`，统一 Evidence 表格格式（加状态列：✅ / 🧊 冻结）
2. 遍历所有 SPI `README.md`：
   - FACT 级：检查是否有 jar 引用、FQCN、FACT 标记
   - FROZEN 级：检查是否有 🧊 冻结 banner
3. 检查所有 `constraints.md` 是否存在
4. 扫描顶层文件（`spi-domain-constraints.md`、`architecture-control-protocol.md`）中的过期路径引用
5. 更新主 `references/index.md` 的域目录表（含 ✅/🧊 计数）
