# Seeyon V8 SPI Skill Closeout Checklist

Use this when the user says the `seeyon-v8-spi` skill is "可用", "闭环", "可以收敛", or asks for final cleanup after a generation/audit cycle.

## Goal

Convert a session-built skill from "works for today's task" into a reusable, low-noise class-level skill.

Closeout is not just polishing prose. It verifies that the active skill can be loaded by a future agent without stale paths, local environment pollution, or ambiguous generation gates.

## Closeout Steps

1. Keep `SKILL.md` as router only.
   - Do not add implementation details to the entry file.
   - Entry should route to architecture, constraints, domain index, generation workflow, validator, Maven notes, Contract Index.
   - If the closeout changes active behavior, bump the skill version with a closeout/hygiene suffix.

2. Re-scan active docs for stale routing and environment pollution.
   - Old structures/doc names: legacy directories, historical structure docs, historical deployment docs.
   - Local paths: Windows user directories, development-drive repository paths, local file repository URLs, generated demo project names.
   - Dependency boundary leaks: wording that treats boot platform capabilities and ctp-user/cip-connector contract packages as one shared public helper source.

3. Exclude the right things from active-doc residual scans.
   - Raw upstream facts, especially rendered Yuque docs under `references/facts/...`, are source material, not active workflow instructions.
   - Do not mutate raw facts just to make grep return zero.

4. Verify references structure.
   - `references/` top-level markdown should stay at the hygiene limit defined in `knowledge-hygiene-workflow.md`.
   - Business domains need `index.md`.
   - Business SPI subdirectories need `README.md` + `constraints.md`; `shared/` is exempt.
   - Non-domain resource directories that contain source artifacts, such as `openapi-docs/`, should have a small `index.md` explaining their status and Evidence boundary.

5. Verify generator/tooling chain.
   - `python -m py_compile references/generation/tools/validate_generated_spi_project.py references/contract-index/tools/contract_index_status.py`
   - `python references/contract-index/tools/contract_index_status.py`
   - Accept `READY`; if `CONFIG_NEEDED`, do not continue pretending signatures are FACT.

6. Verify skill frontmatter.
   - Starts at byte 0 with `---`.
   - Has closing frontmatter delimiter.
   - Has `name` and `description`.
   - Description is short enough for Hermes skill validation.
   - Body remains compact; if entry grows, move detail to `references/`.

## Report Shape

The final user report should separate:

- files changed,
- residual scan results,
- structure checks,
- script checks,
- known exclusions such as raw source docs,
- whether the directory is a git repository.

Do not claim a git diff/commit if the skill directory is not a git repo.

## Common Pitfalls

1. Cleaning raw facts to satisfy grep.
   - Wrong: editing raw Yuque docs for cosmetic zero hits.
   - Right: define active-doc scan scope and report exclusions.

2. Leaving literal stale path tokens inside hygiene docs.
   - A hygiene document can accidentally fail its own residual scan if it quotes forbidden paths literally. Prefer semantic descriptions unless exact tokens are necessary for a script.

3. Treating Maven compile as default success criteria.
   - Static validator + Contract Index readiness are skill-level gates.
   - Maven compile is environment-dependent and must stay optional.

4. Forgetting resource directories.
   - A non-domain directory with `.docx` / raw artifacts should still have an `index.md` that says whether it is FACT, OBSERVATION, or raw source material.
