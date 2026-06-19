#!/usr/bin/env python3
"""Check Seeyon Contract Index readiness.

Exit code:
  0 READY
  2 CONFIG_NEEDED
"""

import json
import os
import sys
from pathlib import Path

try:
    import yaml
except Exception:
    yaml = None

THIS_DIR = Path(__file__).resolve().parent

def find_skill_dir(start: Path = THIS_DIR) -> Path:
    for p in [start, *start.parents]:
        if (p / "SKILL.md").exists():
            return p
    raise RuntimeError("Cannot locate seeyon-v8-spi skill root")

SPI_SKILL_DIR = find_skill_dir()
CONFIG_PATH = SPI_SKILL_DIR / "config" / "external-indexes.yaml"
LOCAL_INDEX_REGISTRY = SPI_SKILL_DIR / "references" / "facts" / "jar-contracts" / "registry.jsonl"


def load_config(path):
    if not path.exists():
        return None, f"missing config: {path}"
    text = path.read_text(encoding="utf-8")
    if yaml is None:
        # Minimal fallback: enough for enabled checks; keep robust for fresh envs.
        enabled_count = sum(1 for line in text.splitlines() if line.strip() == "enabled: true")
        return {"_fallback_enabled_count": enabled_count}, None
    return yaml.safe_load(text) or {}, None


def count_enabled_sources(config):
    if not config:
        return 0
    if "_fallback_enabled_count" in config:
        return config["_fallback_enabled_count"]
    return sum(1 for src in config.get("sources", []) if src.get("enabled") is True)


def count_local_jars():
    if not LOCAL_INDEX_REGISTRY.exists():
        return 0
    count = 0
    with LOCAL_INDEX_REGISTRY.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                count += 1
    return count


def main():
    config, error = load_config(CONFIG_PATH)
    enabled_sources = count_enabled_sources(config)
    local_jars = count_local_jars()

    print(f"Config: {CONFIG_PATH}")
    if error:
        print(f"Config check: {error}")
    else:
        print(f"Enabled external sources: {enabled_sources}")
    print(f"Local jar index entries: {local_jars}")

    if enabled_sources > 0 or local_jars > 0:
        print("STATUS: READY")
        print("NEXT: query external/local contract index before generating code.")
        return 0

    print("STATUS: CONFIG_NEEDED")
    print("OPTIONS:")
    print("  A. Configure Swagger/OpenAPI/MCP/HTTP source in config/external-indexes.yaml")
    print("  B. Import local jar index with references/contract-index/tools/decompile_jar.py index-dir")
    print("  C. Skip contract index for this task; mark generated contract as HYPOTHESIS")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
