#!/usr/bin/env python3
"""Batch-copy Yuque rendered pages to Markdown from an existing manifest."""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from copy_yuque_rendered_markdown import copy_page, safe_name


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("Usage: python references/facts/yuque-v8-docs-rendered-md/tools/batch_copy_yuque_rendered_markdown.py <manifest.json> <out_dir>")
        return 2

    manifest_path = Path(argv[1]).expanduser().resolve()
    out = Path(argv[2]).expanduser().resolve()
    docs_dir = out / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)

    old = json.loads(manifest_path.read_text(encoding="utf-8"))
    items = []
    for item in old:
        if item.get("url") and item.get("slug"):
            items.append({
                "slug": item.get("slug"),
                "title": item.get("title") or item.get("outline_title") or item.get("slug"),
                "updated": item.get("updated", ""),
                "url": item.get("url"),
            })
    if not items:
        raise SystemExit("manifest has no usable URLs")

    ts = datetime.now(timezone.utc).isoformat()
    (out / "outline.md").write_text(
        "# Yuque Seeyon V8 Rendered Markdown Outline\n\n"
        f"Source manifest: {manifest_path}\n\nCaptured at: {ts}\n\n"
        + "\n".join(f"- [{d['title']}]({d['url']})" + (f" — {d['updated']}" if d.get("updated") else "") for d in items)
        + "\n",
        encoding="utf-8",
    )

    result_manifest = []
    manifest_out = out / "manifest.json"
    errors = 0
    for i, item in enumerate(items, 1):
        slug = item["slug"]
        title = item["title"]
        path = docs_dir / f"{i:04d}-{safe_name(title)}-{slug}.md"
        print(f"[{i}/{len(items)}] COPY {title}", flush=True)
        try:
            res = copy_page(item["url"], path)
            record = {
                **item,
                "file": str(path.relative_to(out)),
                "title_captured": res.get("title"),
                "textLen": res.get("textLen"),
                "mdLen": res.get("mdLen"),
                "bytes": res.get("bytes"),
                "captured_at": ts,
                "capture_method": "yuque-rendered-page-copy",
            }
            result_manifest.append(record)
        except Exception as e:
            errors += 1
            print(f"  ERROR {type(e).__name__}: {e}", flush=True)
            result_manifest.append({**item, "error": f"{type(e).__name__}: {e}", "captured_at": ts})
        manifest_out.write_text(json.dumps(result_manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        time.sleep(0.3)

    print(f"DONE out={out} docs={len(result_manifest)} errors={errors}", flush=True)
    return 0 if errors == 0 else 3


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
