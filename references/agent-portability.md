# Agent Portability / Claude Code 适配

## 定位

`seeyon-v8-spi` 是 Hermes skill，但它的知识结构必须能被 Claude Code、Codex、OpenCode 等外部 coding agent 当作普通项目知识库读取。

跨 Agent 适配的核心原则：

1. `seeyon-v8-spi/SKILL.md` 是唯一主入口。
2. 外部 Agent 不需要理解 Hermes 的 `skill_view()`、`metadata.hermes` 或 nested skill loader。
3. 外部 Agent 应按路径读取知识库文件，而不是依赖 skill 自动发现。
4. `references/contract-index/overview.md` 可被发现时只是兼容入口；主流程仍以路径读取模块为准。
5. 不把所有 references 合并进一个超大 `CLAUDE.md`，避免上下文污染。

## Claude Code 推荐接入形态

在目标项目里使用预置的适配文件目录 `references/agent-portability.md`：

```text
references/agent-portability.md
├── CLAUDE.md              # 放项目根目录
├── skills/
│   └── seeyon-v8-spi.md   # 放 .claude/skills/
└── .mcp.json              # 放项目根目录
```

`CLAUDE.md` 只写最小项目级指针，`skills/seeyon-v8-spi.md` 是完整入口规则（SSO/MQ/Contract Index 路由 + MCP 说明 + 关键坑位），`.mcp.json` 配 `seeyon_contract` MCP server 连接。

直接复制这三个文件到目标项目，不需要按以下旧版手工编写。

适用于 Claude Code、Codex、OpenCode 或普通 IDE Agent：

1. 给 Agent 一个“薄入口文件”，指向 `seeyon-v8-spi` 根目录。
2. 要求先读 `SKILL.md`，再按路由读 references。
3. Contract Index 一律按路径进入 `references/contract-index/`。
4. 生成代码前，凡涉及接口/DTO/method signature，先跑状态检查。
5. 不要求外部 Agent 支持 Hermes skill loader。
6. 不把 Hermes 专属字段当作执行前提。

## 禁止事项

- 禁止复制整套 references 到 `CLAUDE.md`。
- 禁止把 `seeyon-contract-index` 当成必须独立加载的外部 skill。
- 禁止让外部 Agent 在未读 `SKILL.md` 的情况下直接按记忆生成 SPI 代码。
- 禁止在无 Contract Source / Evidence / Locator 的情况下输出确定性接口结论。


## Claude Code / External Agent Inline Templates

原 `references/agent-portability.md` 目录已合并进本文档，不再作为根目录下的常驻文件夹。需要给 Claude Code / Codex / OpenCode 接入时，从这里复制薄入口即可。

### CLAUDE.md minimal pointer

```markdown
# CLAUDE.md

## Seeyon V8 SPI Knowledge

For Seeyon V8 SPI / Super SPI / SSO / MQ work, use this knowledge base:

```
<seeyon-v8-spi-skill-root>
```

**Always start with `SKILL.md`** — it's the router. It tells you which reference to read next based on what the user asked for (SSO? MQ? Contract check?).

**Before generating code involving interfaces / DTOs / method signatures**, run the Contract Index status check from the seeyon-v8-spi root:

```bash
python references/contract-index/tools/contract_index_status.py
```

- `READY` → query external/local contract index first
- `CONFIG_NEEDED` → ask user: A) configure Swagger/OpenAPI/MCP, B) import local jar, C) skip (evidence → HYPOTHESIS)
- External index exact match → FACT, stop there. Don't hand-roll.

**MCP**: if `seeyon-contract-mcp` is enabled in `config/external-indexes.yaml`, Claude Code uses its own `.mcp.json` to connect to the same MCP server. Capability mapping is defined in `config/external-indexes.yaml` — Claude Code maps its MCP tools to the same capabilities.

Treat `references/contract-index/` as a path-based internal module, not as a nested skill.
```

### Claude skill adapter content

```markdown
# Seeyon V8 SPI

When working on Seeyon V8 SPI / Super SPI / SSO / unified auth / avoidlogin / connector / MQ tasks:

## Knowledge Base

```
<seeyon-v8-spi-skill-root>
```

## Entry Rules

1. **Read `SKILL.md` first.** It routes to the right sub-document: SSO → `references/auth-sso/index.md`, MQ → `references/mq/index.md`, Contract → `references/contract-index/`.

2. **Contract Index is path-based.** Don't assume nested skill discovery. Read by path:
   - `references/contract-index/overview.md`
   - `references/contract-index/initialization.md`

3. **Before generating code** involving interfaces / DTOs / method signatures, run from the seeyon-v8-spi root:
   ```bash
   python references/contract-index/tools/contract_index_status.py
   ```

4. **Status branches:**
   - `READY` → query external index / local jar index first
   - `CONFIG_NEEDED` → ask user: A) configure Swagger/OpenAPI/MCP, B) import local jar, C) skip (evidence → HYPOTHESIS)

5. **Every contract-related answer must include:**
   - Contract Source
   - Source Type
   - Evidence (FACT / OBSERVATION / HYPOTHESIS)
   - Locator

## MCP

If the user wants to use the MCP contract index source, Claude Code connects to the `seeyon_contract` MCP server defined in `.mcp.json`. Capability mapping (which MCP tool to call for `search_symbol` / `resolve_operation` etc.) is in `config/external-indexes.yaml`.

MCP is one source in the query chain: OpenAPI → MCP → HTTP → jar → probe → version_matrix. If MCP misses a capability, record `Missing Capability` and fall through to the next source.

## Key Pitfalls

- Don't copy the full knowledge base into project context — read files as needed
- Don't default full-jar decompilation — try targeted probe first
- External index exact match → FACT, stop querying. Don't hand-roll.
- `spi-common` is NOT an SPI module — no `spring.factories`, no `spi_info.json`
- SM3 is a digest, not encryption. If user says "SM3 decrypt", correct them.
- Don't assume Hutool `StrUtil` is available unless proven by POM/source.
```

### .mcp.json template

```json
{
  "mcpServers": {
    "seeyon_contract": {
      "comment": "MCP server for Seeyon V8 SPI contract index queries. Capability mapping is in config/external-indexes.yaml under seeyon-contract-mcp.",
      "transport": {
        "type": "stdio",
        "command": "python",
        "args": ["-m", "seeyon_contract_mcp.server"],
        "comment_args": "Replace with actual MCP server entry point. Could also be HTTP/SSE transport."
      }
    }
  }
}
```
