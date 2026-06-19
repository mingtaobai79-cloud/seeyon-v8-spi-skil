# Seeyon V8 语雀索引（本地 SPI 子集 + 远程检索）

> Evidence: OBSERVATION ⚠️ — 来源为语雀 `https://www.yuque.com/seeyonkk/v8` 文档；接口/DTO/method signature 若能被 jar/源码/OpenAPI 精确验证，再升级为 FACT ✅。

## 当前策略

本 skill 不把整套语雀 rendered-md 全量塞进上传版；index 只说明本地子集与远程查询路径。

保留两层入口：

```text
1. 本地 SPI 子集索引（快查 / 离线兜底）
   references/facts/yuque-v8-docs-rendered-md/
   ├── manifest.json       # 85 篇 SPI / Super SPI / ProviderService / SPI 相邻规范清单
   ├── outline.md          # 子集目录
   └── docs/*.md           # SPI 相关 rendered Markdown-like 正文

2. 远程语雀检索脚本（本地无命中 / 非 SPI / 用户给 URL 时）
   references/facts/yuque-v8-docs-rendered-md/tools/yuque_fetch.py  # 搜索 https://www.yuque.com/seeyonkk/v8，可指定 --url
```

状态：

```text
local_spi_docs=85
removed_non_spi_docs=145
full_original_docs=230
online_source=https://www.yuque.com/seeyonkk/v8
capture_method=yuque-rendered-page-copy
```

## 为什么只留 SPI 子集

`seeyon-v8-spi` 的职责是 SPI / Super SPI 工程生成、契约发现、Evidence 治理，不是完整 V8 客开百科。

因此本地只保留：

- SPI 扩展 / Super SPI / `spi_info.json` / `spring.factories`
- 当前 12 个 SPI 域直接相关文档
- 能力通道 ProviderService 相关文档
- 与生成工程强相关的开发准备、工程结构、接口规范、MQ/REST/加密/配置等相邻规范

非 SPI 的前端组件、迁移、运维查看、普通客开案例等不进 active skill tree；index 说明来源即可，本地无命中就走 `references/facts/yuque-v8-docs-rendered-md/tools/yuque_fetch.py` 查远程语雀。

## OpenAPI 保留边界

OpenAPI `.docx` 是 contract/external evidence 输入，保留在 `references/openapi-docs/`；语雀瘦身只影响本地语雀 rendered-md 子集，不影响 OpenAPI 资料。

## 使用规则

1. SPI / Super SPI / ProviderService / 契约生成相关问题，先查本地 SPI 子集：

```bash
python references/contract-index/tools/query_yuque_local_index.py "SPI"
python references/contract-index/tools/query_yuque_local_index.py "ProviderService"
python references/contract-index/tools/query_yuque_local_index.py "MQ扩展"
```

1a. 用户问“通过语雀查一下 / 给调用链 / 通过这个 skill”的组合时，按“精确词 → 宽词 → 指定 URL”三段式，不要停在精确词 0 命中：

```bash
# 先查用户原词；若 0 命中，改查领域宽词或接口名
python references/contract-index/tools/query_yuque_local_index.py "数据源注册" --limit 10
python references/contract-index/tools/query_yuque_local_index.py "数据源" --limit 8
python references/contract-index/tools/query_yuque_local_index.py "DataBaseExecutorService" --limit 8

# 从本地命中的 doc frontmatter / outline 找 remote URL，再指定 URL 查远程单页
python references/facts/yuque-v8-docs-rendered-md/tools/yuque_fetch.py \
  --query "数据源注册" \
  --url "https://www.yuque.com/seeyonkk/v8/wkew2iynh3d3rauh" \
  --max-results 8
```

输出时明确区分：

- 本地 SPI 子集命中：OBSERVATION，可用于定位语雀文档与场景说明。
- 远程全书检索若只返回 `book-overview-page`、`usable_as_evidence=false` 或 API 401：只是访问诊断，不能当 API/调用链证据。
- 指定 URL 的 `specific-page` 且 `usable_as_evidence=true`：可作为语雀 OBSERVATION。
- 接口、DTO、method signature、artifact 仍必须回到 Contract Index / jar / 源码 FACT。

2. 用户给出具体语雀 URL，或本地 SPI 子集无命中，再用远程脚本：

```bash
python references/facts/yuque-v8-docs-rendered-md/tools/yuque_fetch.py --query "<需求关键词>" --url "https://www.yuque.com/seeyonkk/v8/<doc-slug>" --max-results 8
python references/facts/yuque-v8-docs-rendered-md/tools/yuque_fetch.py --query "<需求关键词>" --max-results 8
```

3. 输出 locator 时带上：本地文件路径（若有）+ 原始语雀 URL。
4. 语雀证据不替代 Contract First：涉及接口、DTO、method signature、jar artifact 时，仍先走 `references/contract-index/`，语雀最多是 OBSERVATION。
5. `usable_as_evidence=false` 的在线脚本结果只是访问诊断 / book overview，不可当 API 细节依据。
6. 不在 skill 内保存语雀账号密码；如需认证，用环境变量或脚本目录本地 `secrets.json`，不要提交/上传。

## 维护原则

1. 本地 SPI 子集可以按需要补充，但不要把全量 230 篇放入 active skill tree。
2. 若要重抓，优先用在线脚本确认 URL/slug；稳定后只把 SPI 相关文档沉淀进本地子集。
3. 新增语雀事实后必须更新 `manifest.json` 和 `outline.md`。
4. 不再维护旧的 full-assets / manifest-assets 双轨。
