#!/usr/bin/env python3
"""Search local Seeyon V8 Yuque SPI-subset rendered Markdown index."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent

def find_skill_dir(start: Path = THIS_DIR) -> Path:
    for p in [start, *start.parents]:
        if (p / "SKILL.md").exists():
            return p
    raise RuntimeError("Cannot locate seeyon-v8-spi skill root")

SPI_SKILL_DIR = find_skill_dir()
INDEX_DIR = SPI_SKILL_DIR / "references" / "facts" / "yuque-v8-docs-rendered-md"
DOCS_DIR = INDEX_DIR / "docs"
MANIFEST = INDEX_DIR / "manifest.json"


def load_manifest():
    if not MANIFEST.exists():
        return {}
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    by_file = {}
    for item in data:
        f = str(item.get("file", "")).replace("\\", "/")
        if f:
            by_file[f] = item
            by_file[Path(f).name] = item
    return by_file


def iter_matches(query: str, limit: int, regex: bool):
    if not DOCS_DIR.exists():
        raise SystemExit(f"missing local Yuque SPI-subset index: {DOCS_DIR}")
    pat = re.compile(query if regex else re.escape(query), re.I)
    manifest = load_manifest()
    emitted = 0
    for path in sorted(DOCS_DIR.glob("*.md")):
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        for i, line in enumerate(lines, 1):
            # Skip Yuque page bootstrap payloads. They are not rendered document content
            # and can contain every title/slug as URL-encoded JSON, causing noisy hits.
            if "window.appData = JSON.parse" in line or len(line) > 2000:
                continue
            if not pat.search(line):
                continue
            item = manifest.get(path.name) or manifest.get("docs/" + path.name) or {}
            start = max(1, i - 2)
            end = min(len(lines), i + 2)
            snippet_lines = []
            for n in range(start, end + 1):
                snippet_line = lines[n-1]
                if "window.appData = JSON.parse" in snippet_line or len(snippet_line) > 2000:
                    continue
                snippet_lines.append(f"{n}: {snippet_line}")
            snippet = "\n".join(snippet_lines)
            yield {
                "title": item.get("title") or path.stem,
                "file": str(path),
                "url": item.get("url", ""),
                "line": i,
                "evidence": "OBSERVATION",
                "contract_source": "local-doc-index",
                "source_type": "yuque-rendered-md",
                "locator": f"{path}:{i}" + (f" | {item.get('url')}" if item.get("url") else ""),
                "snippet": snippet,
            }
            emitted += 1
            if emitted >= limit:
                return


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--regex", action="store_true")
    ap.add_argument("--json", action="store_true", dest="as_json")
    ns = ap.parse_args(argv)
    results = list(iter_matches(ns.query, ns.limit, ns.regex))
    if ns.as_json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0 if results else 1
    print("Contract Source: local-doc-index")
    print("Source Type: yuque-rendered-md-spi-subset")
    print("Capability: local SPI-subset keyword search; use references/facts/yuque-v8-docs-rendered-md/tools/yuque_fetch.py for full Yuque / URL-specific search")
    print("Evidence: OBSERVATION")
    print(f"Results: {len(results)}")
    for idx, r in enumerate(results, 1):
        print(f"\n--- {idx} {r['title']}")
        print("Locator:", r["locator"])
        print(r["snippet"])
    return 0 if results else 1


if __name__ == "__main__":
    raise SystemExit(main())
