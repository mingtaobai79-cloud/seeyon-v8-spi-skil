# 知识库卫生与修正工作流

> 从 SKILL.md 下沉。用于控制 references 顶层复杂度。

## 知识库卫生（Knowledge Base Hygiene）

用户明确纠正过：references/ 顶层文件太多会导致上下文爆炸，skill 变得杂乱不可用。以下规则必须遵守：

1. **顶层 md 文件数控制在 6 个以内**：index.md、spi-domain-constraints.md、architecture-control-protocol.md、v8-openapi.md、yuque-local-index.md、agent-portability.md。新增知识必须下沉到域目录或合并到已有文件。
2. **能合并就合并**：相关的小文件合并成大文件的附录，不要散放。
3. **历史 legacy 目录已完全删除**：所有子域已迁移到 references/ 顶层独立目录。不要再创建任何 pre-router 嵌套 legacy 结构。
4. **旧 SSO 目录已合并为 auth-sso/**：不要再引用旧路径。
5. **旧 MQ 目录已合并到 mq/**：不要再引用旧路径。
6. **域目录结构固定**：`index.md`（纯导航）+ `shared/`（共享资源）+ `{spi-name}/`（SPI 文件夹含 README.md + constraints.md）。index.md 绝不塞实现细节。
7. **定期审计**：每次大改后跑一次 `references/` 目录审计，确认顶层文件数、目录数、总大小在合理范围。

## SPI 生成链路卫生门（2026-06 补充）

每次修改 SPI 入口、生成 workflow、平台标准库或公共约束后，必须做一次链路级复扫，不只看单文件 diff：

1. **架构形状**
   - `references/` 顶层 `.md` 保持 6 个以内。
   - 每个业务域目录必须有 `index.md`。
   - 每个业务 SPI 子目录必须有 `README.md` + `constraints.md`；`shared/` 例外。
2. **生成链路 gate**
   - `SKILL.md` 必须路由到 `references/workflows/spi-generation-workflow.md`。
   - `SKILL.md` / workflow 必须路由到 `references/generation/tools/validate_generated_spi_project.py`。
   - workflow 必须先跑 Contract Index 状态，再读取 `references/platform-standard-library/index.md`，最后生成并验证。
3. **平台标准库边界**
   - `platform-standard-library` 只抽取 boot 通用基础能力：`boot-core`、`boot-starter-web`、`boot-starter-spi`。
   - `ctp-user-api`、`cip-connector-api`、`organization-api` 是子域 SPI 契约包，只进入对应 `spi-{domain}` 子模块；不得作为 `spi-common` 公共 helper 来源。
   - 全局公共约束里不得出现 ctp-user / cip-connector 子域 helper 作为公共能力来源。它们只能在目标子域 contract 已 FACT 后使用。
4. **残留扫描必须为 0**
   - 旧路径/旧结构：pre-router legacy 目录、已归并的历史结构文档名、已归并的历史部署文档名。
   - 本地绝对路径污染：Windows 用户目录、开发盘仓库路径、真实本地文件仓库 URL；改成 `<skill-root>`、`${LOCAL_MAVEN_REPO}`、`${MAVEN_SETTINGS}`、用户提供 jar。
   - boot/子域混写：把平台 boot 通用基础能力和 ctp-user / cip-connector 子域契约包混成同一公共依赖来源的表述。
5. **脚本验证**
   - `python -m py_compile references/generation/tools/validate_generated_spi_project.py references/contract-index/tools/contract_index_status.py`
   - `python references/contract-index/tools/contract_index_status.py` 应输出 `READY` 或明确 `CONFIG_NEEDED`；`CONFIG_NEEDED` 不能继续猜接口签名。

判定口径：上述 gate 全 PASS 才能说“当前 SPI 生成链路满足”。否则只能说“局部文件已更新，链路未验证”。

## Operational Audit Gate（active skill 结构审计）

当用户要求“审计 skill / 每个 md 都看看 / 有没有藏的问题”时，不要只做断链和 secret 扫描。必须额外给出结构性 PASS/PARTIAL/FAIL：

1. **扫描分层**
   - `active`：`SKILL.md` + `references/**.md`，排除 `references/facts/**` 原始证据区与历史目录。
   - `raw facts`：只报风险类别，不为 grep 归零而清理。
   - `historical`：除非入口仍引用，否则不作为 active 内容。
2. **必查结构债**
   - `references/` 顶层 `.md` 是否仍超过 hygiene 目标 6 个；超标即使断链为 0，也只能判 `PARTIAL`。
   - 是否存在新旧同域并存目录，例如旧 SSO 活跃目录与新 `references/auth-sso/` 并存；若主入口已迁移但旧目录仍在 active references 下，判为结构污染风险。
   - 旧 root 文档（如 contract-discovery / jar-contract-indexing-plan / evidence-system 等）是否还有 active 引用；引用为 0 也不等于干净，只说明可进入移出 active tree 决策。
   - 旧 root 文档如果内容仍有用，不能只移出后宣称 PASS；必须逐项证明已有 active 下沉副本承接，或把原文移动到语义子目录（如 `references/contract-index/`、`references/status/`、`references/workflows/`、`references/generation/`），并在 `references/index.md` 或对应模块入口挂路由。否则只能判 `PARTIAL`。
3. **必查污染**
   - active 本地绝对路径、真实 secret、旧 root doc 引用必须为 0。
   - 客户/项目名命中要分类：场景名/公开产品名可保留；历史项目观察不得回流成默认 FACT。
4. **必跑验证**
   - active markdown link check：忽略代码块、http/https/mailto/data、纯锚点；root-relative `references/...` 从 skill 根解析。
   - `python -m py_compile references/generation/tools/validate_generated_spi_project.py references/contract-index/tools/contract_index_status.py`
   - `python references/contract-index/tools/contract_index_status.py`

报告口径：
- 断链 0 + 本地路径 0 + secret 0 + Contract READY，但顶层 md 超标或旧域并存 = `PARTIAL`，不是 PASS。
- 不要为了让扫描归零直接删除旧目录；先列“必修结构债”，由用户决定是否移出 active tree。

## Root 文档下沉与旧域清理

当做结构收敛、瘦身、清理旧目录时，先判断“内容是否被 active 新结构承接”，不要把有用文档移走后就报 PASS。

1. 对旧 `references/*.md` root 文档逐项建立承接表：
   - 若已有几乎 1:1 的 active 下沉副本（如 `references/contract-index/<name>.md`），旧 root 可移出 skill tree。
   - 若没有 active 承接，但内容仍有通用价值，先按语义下沉到 `references/contract-index/`、`references/status/`、`references/workflows/`、`references/generation/` 等目录，再从 root 移走。
   - `references/index.md` 要补一层“结构/治理索引”或等价入口，保证下沉文档仍可发现。
2. 对旧同域目录（例如旧 SSO 被新 `references/auth-sso/` 覆盖）：
   - 先确认主入口、生成流程、active 文档都只路由到新目录。
   - 扫 active 文档中旧路径引用为 0。
   - 如果旧目录只剩重复历史内容，不要留在 active skill tree 里占上下文；确认承接后移出 skill tree。
3. 清理后复扫两层：
   - active 层：断链、本地路径、secret、旧 root refs、旧域 refs 全为 0。
   - full skill tree 层：旧目录名、旧路径文本、临时 closeout 历史目录残留为 0；历史内容不在 skill tree 内。
4. 最后仍要跑：
   - `python -m py_compile references/generation/tools/validate_generated_spi_project.py references/contract-index/tools/contract_index_status.py`
   - `python references/contract-index/tools/contract_index_status.py`

### 结构收敛执行法（旧域 → 新域）

当用户确认“新目录没问题，旧目录可以清理”时，按 active-tree 清理执行：

1. **先做覆盖核对**：列旧域 `.md` 与新域目标文件的粗映射，确认核心入口、SPI README、shared contract/version/validation/deployment 等都有新位置；不要求字节完全一致，但必须确认新目录承担 active 路由。
2. **移出 active tree**：旧 active 域确认被新域承接后，不留在上传版 skill tree；同批顶层 legacy md 也移出 active tree。
3. **更新 active replacement 说明**：在当前 index/workflow 中说明新入口，不保留历史对照目录。
4. **清残留引用**：active 文档中旧路径、旧 root 文档名、示例路径都要清到 0；如果 hygiene workflow 自己还拿旧路径举例，也要改成非 active 表述，避免未来 agent 复活旧路由。
5. **复验口径**：active 扫描排除 `references/facts/**`；skill 根目录不得保留 full dump / old 入口；必须输出顶层 md 数、旧域 active 是否不存在、新域是否存在、断链、本地路径、secret、旧路径引用、legacy root 引用。
6. **最终验证**：同一轮跑 `py_compile` 与 `contract_index_status.py`；只有顶层 md ≤ 6、断链 0、旧域 active 引用 0、Contract Index READY 时，才能报 `PASS`。

## 现场实例污染审计

当一次实战验证使用了用户本地 Maven 仓库、IDEA 配置、私服、客户项目或临时生成工程时，经验可以沉淀，但现场实例不能变成 skill 默认。

大改或验证闭环后必须复扫 active skill 文档，确认没有把以下内容固化为通用样例：

- 本地盘符/绝对路径：如 `<local-repo-path>`、`<local-maven-repo>`、桌面临时工程路径。
- 私服/本地仓库细节：repository id、真实本地文件仓库 URL、一次性 `settings.xml`。
- 客户/项目名作为默认来源标签。
- 一次性依赖版本组合被写成全局默认。
- 编译日志、临时工程名、会话产物路径。

正确沉淀方式：

1. 将路径改为占位符，例如 `${LOCAL_MAVEN_REPO}`、`${PROJECT_LIB_DIR}`、`${MAVEN_SETTINGS}`。
2. 将“某客户项目”改为“项目观察 A/B”或带 Evidence 的匿名 locator。
3. 将 Maven 编译经验写成“可选验证模式”，不是生成默认流程。
4. 明确 Maven executable、settings.xml、localRepository、私服地址都是用户现场输入。
5. 复扫 active `.md`，本地路径/客户名/临时工程名命中应为 0；历史内容不能作为入口引用。

2026-06 实战沉淀位置：
- `references/workflows/non-frozen-audit-workflow.md`
- 历史 lowcode 个案已不作为 active skill 路由；若需保留，只能在raw facts 中以匿名观察存在。
- `references/entry-menu-mobile/shared/mobile-cip-connector-api-5.3.286.md`

## Skill 目录缓存清理（Windows）

当用户问“这个 skill 目录下面还有没有”或要求继续清理时，先区分缓存垃圾与正式知识库资产，不要看见“大文件/反编译”就删。

可清理候选：

- `.pytest_cache/`
- `__pycache__/`
- `*.pyc`
- `*.tmp`、`*.bak`、`*.orig`、`*~`
- 临时 `target/`、`build/`、`dist/`（仅确认不是正式样例/模板后）

不要默认清理：

- `references/contract-index/tools/cfr.jar`：CFR 反编译工具依赖，属于 Contract Index 工作流资产。
- `references/platform-standard-library/decompiled/`：平台标准库 FACT/签名索引来源，属于知识库资产。
- `references/**/contract-facts-*.md`、domain README/constraints、audit notes：即使近期生成，也按正式 references 处理。

Windows 上删除 skill 内缓存时，优先丢回收站而不是硬删。Git Bash 可调用 PowerShell + VisualBasic：

```python
from pathlib import Path
import subprocess
root = Path.home() / "AppData/Local/hermes/skills/software-development/seeyon-v8-spi"
items = []
p = root / ".pytest_cache"
if p.exists():
    items.append(p)
items.extend(sorted(root.rglob("__pycache__")))
for p in items:
    win = str(p).replace("/", "\\\\")
    cmd = (
        "Add-Type -AssemblyName Microsoft.VisualBasic; "
        f"[Microsoft.VisualBasic.FileIO.FileSystem]::DeleteDirectory('{win}','OnlyErrorDialogs','SendToRecycleBin')"
    )
    subprocess.run(["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", cmd], check=True)
```

清理后复验候选命中为 0，再汇报“已清理/未动原因”。注意 Python 字符串里的反斜杠转义，`replace('/', '\')` 会触发 unterminated string；必须写成 `replace('/', '\\\\')` 或直接使用 raw/Path 方式生成 Windows 路径。
