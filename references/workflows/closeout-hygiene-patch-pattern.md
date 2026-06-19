# Closeout Hygiene Patch Pattern

Use this when a Seeyon V8 SPI skill closeout/audit finds that the architecture is usable but a few structural debts remain.

## Trigger

- User or reviewer reports `PARTIAL` because active routing is correct but there are residual legacy files, status-count drift, or frozen README formatting drift.
- The goal is a small收敛 patch, not a new domain audit.

## Patch sequence

1. Fix status math in `references/index.md` from the actual domain table. Do not reuse old totals after capability-channel or other domains were split.
2. For every SPI listed in `references/status/frozen-artifacts.md`, ensure `README.md` starts with a visible frozen banner:

   ```md
   > 🧊 **冻结状态** — 缺少必要 jar 包，接口/DTO 均为 OBSERVATION，无法升级到 FACT。
   > 待获取对应 jar 后解除冻结。
   ```

3. If a domain root contains migrated legacy files while the active route is now `index.md` + `shared/` + `<spi>/`, remove those root legacy files from the active upload tree after confirming their content is covered by the current route.
4. Do not keep historical docs in the active route/link hygiene scope.
5. Re-run verification:
   - active Markdown links
   - exact duplicate scan
   - `python -m py_compile` for changed Python tools
   - `references/contract-index/tools/contract_index_status.py`

## Reporting rule

Use `PASS-with-frozen-boundary` when:

- active links are 0 broken;
- active routing is clean;
- frozen SPI remain OBSERVATION by design;
- Contract Index is READY;
- remaining duplicates, if any, are non-business package placeholders like empty `__init__.py` files.

Do not report unconditional full PASS if the user’s pass criteria include FACT completion of frozen SPI.
