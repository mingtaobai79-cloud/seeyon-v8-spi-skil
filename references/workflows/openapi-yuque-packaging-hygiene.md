# OpenAPI / Yuque Packaging Hygiene

Use this when slimming or release-preparing `seeyon-v8-spi`.

## Durable lesson

Do not let Yuque slimming accidentally remove OpenAPI materials. They are different evidence channels:

- `references/openapi-docs/` is the official OpenAPI document bundle and can upgrade exact API matches to FACT.
- `references/facts/yuque-v8-docs-rendered-md/` is Yuque rendered-md evidence; its ceiling is OBSERVATION unless backed by jar/source/OpenAPI exact match.
- `references/facts/yuque-v8-docs-rendered-md/tools/yuque_fetch.py` is the fallback for full Yuque / specific URL lookup when the local SPI subset does not cover the question.

## Expected active shape after packaging

```text
references/openapi-docs/
  index.md
  *.docx                         # keep the OpenAPI bundle; do not prune with Yuque docs

references/facts/yuque-v8-docs-rendered-md/
  manifest.json                  # local SPI subset manifest
  outline.md
  docs/*.md                      # SPI/Super SPI/ProviderService-relevant Yuque subset

references/facts/yuque-v8-docs-rendered-md/tools/yuque_fetch.py           # online Yuque lookup for non-SPI or URL-specific docs
```

## Verification gate before reporting COMPLETE

Run/confirm all of these before saying release-ready:

1. OpenAPI bundle present:
   - `references/openapi-docs/index.md` exists
   - expected `.docx` count is present for the current bundle
2. Yuque local subset is internally consistent:
   - `len(manifest.json) == count(docs/*.md)`
   - `outline.md` describes the subset, not an obsolete full count
3. Online fallback present:
   - `references/facts/yuque-v8-docs-rendered-md/tools/yuque_fetch.py --help` exits 0
4. Python scripts compile:
   - `python -m py_compile <all skill *.py>`
5. Link hygiene:
   - Markdown links resolve
   - active `SKILL.md` backtick references under `references/...` resolve
6. Contract Index still works:
   - `references/contract-index/tools/contract_index_status.py` exits 0 and reports READY or a clearly explained non-ready state
7. Package inspection:
   - final zip contains OpenAPI `.docx`
   - final zip contains Yuque SPI docs
   - final zip contains `references/facts/yuque-v8-docs-rendered-md/tools/yuque_fetch.py`

## Pitfall

If the user says “openapi 的那些要保留”, treat it as a packaging gate: ensure `references/openapi-docs/` exists first, then rerun the whole verification gate. Do not defend removing it; OpenAPI is not part of the Yuque-pruning budget.
