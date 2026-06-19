# Contract Index 模块治理规则

## 定位

`references/contract-index/` 是 `seeyon-v8-spi` 的 Contract Index 模块。

它不再保留独立 `SKILL.md`，不再作为 nested skill 暴露；主入口按路径读取 `overview.md`。

## 主流程规则

1. `seeyon-v8-spi/SKILL.md` 是唯一主入口。
2. 主入口进入契约索引流程时，按路径读取模块文件：
   - `references/contract-index/overview.md`
   - `references/contract-index/initialization.md`
   - `references/contract-index/source-types.md`
   - `references/contract-index/capability-contract.md`
   - `config/external-indexes.template.yaml`
   - `references/contract-index/tools/contract_index_status.py`
3. 不要求 Hermes loader 支持 nested skill。
4. 不要求 `seeyon-contract-index` 可被 `skill_view()` 发现。
5. 不把 Contract Index 挪回 `software-development/` 平级 skill 目录，避免破坏 `seeyon-v8-spi` 作为统一入口的内聚边界。

## 配置文件边界

唯一运行时配置文件在父 skill 根目录：

```text
config/external-indexes.yaml
```

模块内的 YAML 只能放模板：

```text
config/external-indexes.template.yaml
```

主流程、状态检查脚本、后续 adapter 都必须读取外层 `config/external-indexes.yaml`。模块模板只用于初始化/重置；客户现场配置、source enabled 开关、capability mapping 都不得维护在模板里。

## 模块化规则

Contract Index 保持一个内聚模块，不按 MCP/HTTP/OpenAPI 拆成多个 skill。

内部按文件拆分：

| 文件 | 职责 |
|------|------|
| `references/contract-index/overview.md` | 入口、startup check、查询顺序、输出要求 |
| `references/contract-index/source-types.md` | OpenAPI/MCP/HTTP/local jar/probe/version matrix 的来源分类 |
| `references/contract-index/capability-contract.md` | 通用 capability 协议、MCP/HTTP mapping、Missing Capability 降级 |
| `config/external-indexes.template.yaml` | capability mapping 配置模板 |
| `references/contract-index/tools/contract_index_status.py` | readiness 检查 |
| `references/contract-index/tools/query_yuque_local_index.py` | 查询已合并的事实库 rendered-md 索引，Evidence 上限 OBSERVATION |

MCP 差异必须由 `capabilities` 映射吸收，不通过新增一堆 MCP 专属 skill 解决。

## 脚本执行规则

从 `seeyon-v8-spi` 根目录执行：

```bash
python references/contract-index/tools/contract_index_status.py
```

也必须兼容从模块目录执行：

```bash
cd references/contract-index
python references/contract-index/tools/contract_index_status.py
```

脚本以 `seeyon-v8-spi` 根目录为执行上下文；如从其他目录调用，使用绝对路径或先 `cd` 到根目录。

## 禁止事项

- 禁止在主入口把 nested skill loader 写成前置依赖。
- 禁止把大 jar、完整 Swagger/OpenAPI 正文、完整反编译源码放入模块。
- 禁止把 token 明文写入 `config/external-indexes.yaml`；只允许写 `token_env`。
- 禁止默认整包反编译大 jar；本地未命中时先做 targeted probe。
- 禁止假设所有 MCP 都有同一组工具名；必须走 capability mapping。
- 禁止 capability 缺失时脑补结果；应记录 Missing Capability 并降级。

## 验收项

- [ ] 主入口无“必须加载子 skill”语义。
- [ ] `contract_index_status.py` 从 `seeyon-v8-spi` 根目录可执行。
- [ ] 全目录无 `seeyon-v8-sso` 残留。
- [ ] 全目录无错误的 `../seeyon-v8-spi` 路径。
- [ ] 模块已拆出 `source-types.md` 与 `capability-contract.md`。
- [ ] MCP/HTTP 外部源通过 `capabilities` 映射声明能力，不写死固定工具清单。
- [ ] 事实库语雀索引只指向 `references/facts/yuque-v8-docs-rendered-md/`，旧抓取目录不作为入口。
