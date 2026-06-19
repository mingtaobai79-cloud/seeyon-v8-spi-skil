# 入口路由器瘦身工作流

适用：Seeyon V8 SPI skill 继续增长，`SKILL.md` 开始承载历史、流程、状态、坑位、长 references 列表，偏离“入口只路由”的原则。

目标形态：`SKILL.md` 控制在 200-300 行，只保留路由、证据规则、工程边界、默认执行流程、灾难级红线。长期知识下沉到 `references/`。

## 判断信号

出现任一信号就应瘦身：

- `SKILL.md` 超过约 300 行，且包含大量当前任务无关细节。
- CFR/Jar、审计、hygiene、域升级等具体流程写在入口。
- 冻结清单、Evidence 数量、实战状态路径等状态信息写在入口。
- “关键坑”编号乱序、重复，入口变成历史补丁收容器。
- References 区列出大量子域细节，而不是核心入口。
- 规则和状态混在一起，导致入口频繁改。

## 下沉规则

保留在 `SKILL.md`：

- 一句话职责：统一入口，只负责路由、证据规则、工程边界。
- 必读顺序。
- Contract First / Evidence First / Closed-world / Super SPI / Frozen / 缺口口径。
- 一级路由表。
- 默认执行流程（10 步以内）。
- 高频灾难级红线。
- 核心 references 入口。

下沉到 `references/workflows/`：

- Evidence 升级工作流。
- Evidence 批量审计工作流。
- 非冻结域审计工作流。
- Knowledge hygiene 修正工作流。
- 域升级检查清单。
- Frozen skeleton / 占位升级流程。

下沉到 `references/contract-index/`：

- CFR 反编译工作流。
- Jar 发现路径。
- Contract discovery 命令和细节。
- Contract bundle / normalization 细节。

下沉到 `references/status/`：

- 冻结 artifact 清单。
- Evidence 总览。
- 已知缺口状态。
- 某次实战状态位置。

下沉到 `references/pitfalls/`：

- 关键坑长列表。
- domain-specific pitfalls。
- Windows/CFR 坑。
- 示例包处理坑。

## 执行步骤

1. 不要在 skill 根目录保留原入口历史快照、full dump 或 old 入口副本。
2. 按章节识别入口中的 workflow/status/pitfalls/contract-index 内容。
3. 创建或更新对应 `references/` 文件，搬运原文并加一句来源说明。
4. 重写 `SKILL.md` 为路由器，不继续追加历史细节。
5. 修正入口中不存在的路径引用，避免死链。
6. 验证：
   - `SKILL.md` 200-300 行。
   - 入口中 concrete references 全部存在。
   - 本次新增/修改 md code fence 平衡。
   - 下沉内容可通过入口工作流表找到。
7. 如需交付，重新打包 skill，并报告 zip path、size、sha256。

## 验证口径

瘦身不是删内容，而是移动责任边界：

- 入口变轻。
- 子域更深。
- workflow/status/pitfalls/contract-index 分层明确。
- skill 根目录不保留 full dump / old 入口。
- 未来修改状态或流程时，不必频繁污染 `SKILL.md`。

## 禁忌

- 不要为了瘦身删除事实；只移动和修引用。
- 不要把冻结域当作可顺手修复对象。
- 不要把所有流程合并进一个新的巨型 workflow。
- 不要把 `references/index.md` 变成第二个臃肿入口。
- 不要保留旧路径残留；下沉后必须复扫 concrete references。

