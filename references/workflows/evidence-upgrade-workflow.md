# Evidence 升级工作流

> 从 SKILL.md 下沉。用于把 OBSERVATION/HYPOTHESIS 升级为 FACT。

## Evidence 升级工作流

1. `jar tf` 列出所有 class，搜索目标接口/DTO
2. `jar xf` 提取到临时目录
3. CFR 反编译提取的 .class 文件
4. 更新 `references/{domain}/{spi}/README.md`：
   - 头部 Evidence 标记改为 `FACT ✅`
   - 接口定义段落标记 `[FACT ✅]`
   - 补充完整 FQCN、方法签名、DTO 字段
5. 更新 `references/{domain}/{spi}/constraints.md` 索取清单
6. 更新 `references/{domain}/index.md` Evidence 表格（含状态列）
7. 更新 `references/index.md` 主索引的域状态汇总
