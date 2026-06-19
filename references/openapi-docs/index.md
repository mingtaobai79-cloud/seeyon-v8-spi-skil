# OpenAPI 原始文档

本目录保存 V8 OpenAPI / 开放事件相关原始 `.docx` 文档。

## 定位

- 这些文件是 Contract Source 候选材料，不是已归一化的 SPI contract。
- 需要使用时，先按 `references/contract-index/overview.md` 和 `references/contract-index/source-types.md` 判定 Evidence。
- `.docx` 中抽取出的接口、DTO、字段、路径，必须沉淀到对应 domain 或 `references/v8-openapi.md` 后再被生成链路引用。

## 使用规则

1. 不直接从 `.docx` 复制 method signature 到最终代码。
2. 若与 jar / OpenAPI exact match 冲突，以 FACT 级 artifact 为准。
3. 若只是文档描述，最多标为 OBSERVATION。
4. 本目录不参与 Super SPI 工程结构生成。
