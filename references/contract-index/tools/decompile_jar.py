#!/usr/bin/env python3
"""
CFR Jar Decompiler — Contract Extraction + Contract Index

Legacy usage:
    python decompile_jar.py <jar_path> <output_dir>

Index usage:
    python decompile_jar.py index <jar_path> [--index-root <dir>] [--keep-source]
    python decompile_jar.py index-dir <jar_dir> [--pattern "*.jar"] [--index-root <dir>] [--keep-source]
    python decompile_jar.py query [--symbol Name] [--fqn FQN] [--method name] [--domain domain]
    python decompile_jar.py status [--index-root <dir>]
"""

import argparse
import fnmatch
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent

def find_skill_dir(start: Path = SCRIPT_DIR) -> Path:
    for p in [start, *start.parents]:
        if (p / "SKILL.md").exists():
            return p
    raise RuntimeError("Cannot locate seeyon-v8-spi skill root")

SKILL_DIR = find_skill_dir()
DEFAULT_INDEX_ROOT = SKILL_DIR / "references" / "facts" / "jar-contracts"


JAVA_KEYWORDS = {
    "if", "for", "while", "switch", "catch", "return", "new", "throw", "else", "do", "try",
    "super", "this", "synchronized"
}


TYPE_DECL_RE = re.compile(
    r"(?P<annotations>(?:\s*@[^\n]+\n)*)\s*"
    r"public\s+(?:(?P<abstract>abstract)\s+)?(?P<kind>class|interface|enum)\s+(?P<name>\w+)"
    r"(?P<tail>[^\{;]*)",
    re.MULTILINE,
)

METHOD_RE = re.compile(
    r"(?P<annotations>(?:\s*@[^\n]+\n)*)\s*"
    r"(?P<visibility>public|protected|private)?\s*"
    r"(?P<mods>(?:(?:default|static|final|abstract|synchronized|native)\s+)*)"
    r"(?P<return>[\w.$<>\[\], ?]+?)\s+"
    r"(?P<name>\w+)\s*\((?P<params>[^)]*)\)"
    r"(?:\s+throws\s+(?P<throws>[^\{;]+))?\s*(?:\{|;)",
    re.MULTILINE,
)

FIELD_RE = re.compile(
    r"(?P<annotations>(?:\s*@[^\n]+\n)*)\s*"
    r"(?P<visibility>private|protected|public)\s+"
    r"(?P<mods>(?:(?:static|final|transient|volatile)\s+)*)"
    r"(?P<type>[\w.$<>\[\], ?]+?)\s+"
    r"(?P<name>\w+)\s*(?:=|;)",
    re.MULTILINE,
)


def find_cfr_jar():
    """Find cfr.jar relative to this script."""
    candidates = [SCRIPT_DIR / "cfr.jar"]
    for cfr_path in candidates:
        if cfr_path.exists():
            return str(cfr_path)
    return None


def now_iso():
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_artifact_version(jar_path_or_name):
    """Parse artifact/version from common Maven-ish jar names."""
    name = Path(jar_path_or_name).name
    stem = name[:-4] if name.lower().endswith(".jar") else Path(name).stem
    match = re.match(r"^(?P<artifact>.+?)-(?P<version>\d+(?:\.\d+)*(?:[-.][A-Za-z0-9]+)*)$", stem)
    if match:
        return {"artifact_id": match.group("artifact"), "version": match.group("version"), "file_name": name}
    return {"artifact_id": stem, "version": None, "file_name": name}


def decompile_jar(jar_path, output_dir):
    """Decompile jar using CFR."""
    cfr_jar = find_cfr_jar()
    if not cfr_jar:
        print("ERROR: cfr.jar not found")
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)

    cmd = ["java", "-jar", cfr_jar, jar_path, "--outputdir", output_dir]
    print(f"Running: {' '.join(cmd)}")

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    if result.returncode != 0:
        print(f"CFR error: {result.stderr}")
        sys.exit(1)

    print(f"Decompiled to: {output_dir}")
    return output_dir


def parse_annotations(annotation_block):
    names = []
    comments = []
    for line in (annotation_block or "").splitlines():
        line = line.strip()
        m = re.match(r"@([\w.]+)", line)
        if m:
            names.append(m.group(1).split(".")[-1])
        cm = re.search(r"@(?:CtpUserComment|CipConnectorComment)\s*\(\s*(?:value\s*=\s*)?\"([^\"]+)\"", line)
        if cm:
            comments.append(cm.group(1))
        dm = re.search(r"@DtoAttribute\s*\([^)]*value\s*=\s*\"([^\"]+)\"", line)
        if dm:
            comments.append(dm.group(1))
    return names, comments[-1] if comments else ""


def split_csv(text):
    """Split a Java-ish comma list while respecting generic angle brackets."""
    if not text or not text.strip():
        return []
    result = []
    buf = []
    depth = 0
    for ch in text:
        if ch == "<":
            depth += 1
        elif ch == ">" and depth:
            depth -= 1
        if ch == "," and depth == 0:
            item = "".join(buf).strip()
            if item:
                result.append(item)
            buf = []
        else:
            buf.append(ch)
    item = "".join(buf).strip()
    if item:
        result.append(item)
    return result


def parse_params(params_text):
    params = []
    for i, raw in enumerate(split_csv(params_text)):
        raw = re.sub(r"@\w+(?:\([^)]*\))?\s*", "", raw).strip()
        raw = re.sub(r"\bfinal\s+", "", raw).strip()
        parts = raw.rsplit(" ", 1)
        if len(parts) == 2:
            ptype, pname = parts[0].strip(), parts[1].strip()
        else:
            ptype, pname = raw, f"arg{i}"
        params.append({"type": ptype, "name": pname})
    return params


def parse_extends_implements(kind, tail):
    extends = []
    implements = []
    tail = tail or ""
    em = re.search(r"\bextends\s+([^\{;]+?)(?:\s+implements\s+|$)", tail)
    if em:
        extends = [x.strip() for x in split_csv(em.group(1))]
    im = re.search(r"\bimplements\s+([^\{;]+)$", tail)
    if im:
        implements = [x.strip() for x in split_csv(im.group(1))]
    return extends, implements


def infer_domain(fqn):
    lower = fqn.lower()
    if ".api.avoidlogin." in lower or "avoidlogin" in lower:
        return "sso.avoidlogin"
    if "cip" in lower and "connector" in lower and "sso" in lower:
        return "sso.connector"
    if ".api.sso." in lower or lower.endswith("ssoauthproviderservice") or ".sso." in lower:
        return "sso.unifiedauth"
    if ".dto" in lower:
        return "sso.dto"
    if "exception" in lower:
        return "sso.exception"
    return ""


def source_relpath(path, root):
    try:
        return str(Path(path).resolve().relative_to(Path(root).resolve())).replace("\\", "/")
    except Exception:
        return str(path).replace("\\", "/")


def extract_contracts(output_dir):
    """Extract class/interface/enum contracts from decompiled Java source."""
    contracts = []

    for root, _dirs, files in os.walk(output_dir):
        for fname in sorted(files):
            if not fname.endswith(".java"):
                continue

            fpath = os.path.join(root, fname)
            with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()

            pkg_match = re.search(r"package\s+([\w.]+);", content)
            package = pkg_match.group(1) if pkg_match else ""

            type_match = TYPE_DECL_RE.search(content)
            if not type_match:
                continue

            kind = type_match.group("kind")
            name = type_match.group("name")
            fqn = f"{package}.{name}" if package else name
            annotations, type_comment = parse_annotations(type_match.group("annotations"))
            extends, implements = parse_extends_implements(kind, type_match.group("tail"))

            methods = []
            for mm in METHOD_RE.finditer(content):
                method_name = mm.group("name")
                if method_name in JAVA_KEYWORDS or method_name == name:
                    continue
                ret = " ".join(mm.group("return").split())
                if ret in {"if", "for", "while", "switch", "catch"}:
                    continue
                method_annotations, method_comment = parse_annotations(mm.group("annotations"))
                mods = (mm.group("mods") or "").split()
                throws = [x.strip() for x in split_csv(mm.group("throws") or "")]
                params = parse_params(mm.group("params"))
                signature = f"{ret} {method_name}({', '.join((p['type'] + ' ' + p['name']).strip() for p in params)})"
                if throws:
                    signature += " throws " + ", ".join(throws)
                methods.append({
                    "owner_fqn": fqn,
                    "method_name": method_name,
                    "return_type": ret,
                    "params": params,
                    "throws": throws,
                    "default": "default" in mods,
                    "static": "static" in mods,
                    "visibility": mm.group("visibility") or "",
                    "annotations": method_annotations,
                    "comment": method_comment,
                    "signature": signature,
                })

            fields = []
            for fm in FIELD_RE.finditer(content):
                field_name = fm.group("name")
                if field_name in JAVA_KEYWORDS:
                    continue
                field_annotations, field_comment = parse_annotations(fm.group("annotations"))
                fields.append({
                    "owner_fqn": fqn,
                    "field_name": field_name,
                    "field_type": " ".join(fm.group("type").split()),
                    "visibility": fm.group("visibility"),
                    "annotations": field_annotations,
                    "comment": field_comment,
                })

            contracts.append({
                "package": package,
                "kind": kind,
                "abstract": bool(type_match.group("abstract")),
                "name": name,
                "full_name": fqn,  # legacy key
                "fqn": fqn,
                "extends": extends,
                "implements": implements,
                "annotations": annotations,
                "comment": type_comment,
                "domain_hint": infer_domain(fqn),
                "methods": methods,
                "fields": fields,
                "file": fpath,
                "source_file": source_relpath(fpath, output_dir),
            })

    return contracts


def print_summary(contracts):
    """Print contract summary."""
    print(f"\n{'=' * 60}")
    print(f"Contract Summary ({len(contracts)} classes)")
    print(f"{'=' * 60}\n")

    for c in contracts:
        prefix = "abstract " if c.get("abstract") else ""
        print(f"  {prefix}{c['kind']} {c.get('fqn') or c.get('full_name')}")
        if c.get("methods"):
            print(f"    methods: {len(c['methods'])}")
        if c.get("fields"):
            print(f"    fields: {len(c['fields'])}")


def ensure_index_dirs(index_root):
    index_root = Path(index_root)
    (index_root / "by-sha256").mkdir(parents=True, exist_ok=True)
    (index_root / "aliases").mkdir(parents=True, exist_ok=True)
    return index_root


def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def append_registry(index_root, meta):
    registry = Path(index_root) / "registry.jsonl"
    existing = []
    if registry.exists():
        with registry.open("r", encoding="utf-8") as f:
            existing = [json.loads(line) for line in f if line.strip()]
    existing = [row for row in existing if row.get("sha256") != meta["sha256"]]
    existing.append(meta)
    write_jsonl(registry, existing)


def flatten_index_rows(contracts, meta):
    symbols = []
    methods = []
    fields = []
    for c in contracts:
        base = {
            "sha256": meta["sha256"],
            "artifact_id": meta["artifact_id"],
            "version": meta.get("version"),
        }
        symbols.append({
            **base,
            "kind": c["kind"],
            "package": c["package"],
            "name": c["name"],
            "fqn": c["fqn"],
            "extends": c.get("extends", []),
            "implements": c.get("implements", []),
            "annotations": c.get("annotations", []),
            "source_file": c.get("source_file", ""),
            "domain_hint": c.get("domain_hint", ""),
            "comment": c.get("comment", ""),
        })
        for m in c.get("methods", []):
            methods.append({**base, **m})
        for field in c.get("fields", []):
            fields.append({**base, **field})
    return symbols, methods, fields


def render_contract_md(meta, symbols, methods, fields):
    lines = [
        f"# Contract Index: {meta['file_name']}",
        "",
        f"- Artifact: {meta['artifact_id']}",
        f"- Version: {meta.get('version') or 'unknown'}",
        f"- SHA256: {meta['sha256']}",
        f"- Evidence: {meta['evidence']} ✅",
        f"- Indexed At: {meta['indexed_at']}",
        "",
        "## Symbols",
        "",
    ]
    methods_by_owner = {}
    fields_by_owner = {}
    for m in methods:
        methods_by_owner.setdefault(m["owner_fqn"], []).append(m)
    for f in fields:
        fields_by_owner.setdefault(f["owner_fqn"], []).append(f)
    for s in symbols:
        lines.append(f"### {s['kind']} {s['fqn']}")
        if s.get("domain_hint"):
            lines.append(f"- Domain: {s['domain_hint']}")
        if s.get("comment"):
            lines.append(f"- Comment: {s['comment']}")
        owned_methods = methods_by_owner.get(s["fqn"], [])
        if owned_methods:
            lines.append("- Methods:")
            for m in owned_methods:
                marker = " default" if m.get("default") else ""
                lines.append(f"  - `{m['signature']}`{marker}")
        owned_fields = fields_by_owner.get(s["fqn"], [])
        if owned_fields:
            lines.append("- Fields:")
            for f in owned_fields:
                comment = f" — {f['comment']}" if f.get("comment") else ""
                lines.append(f"  - `{f['field_type']} {f['field_name']}`{comment}")
        lines.append("")
    return "\n".join(lines)


def index_decompiled_dir(jar_path, decompiled_dir, index_root=DEFAULT_INDEX_ROOT, keep_source=False):
    jar_path = Path(jar_path)
    decompiled_dir = Path(decompiled_dir)
    index_root = ensure_index_dirs(index_root)

    parsed = parse_artifact_version(jar_path.name)
    digest = sha256_file(jar_path)
    meta = {
        "sha256": digest,
        "file_name": parsed["file_name"],
        "artifact_id": parsed["artifact_id"],
        "version": parsed.get("version"),
        "size": jar_path.stat().st_size,
        "indexed_at": now_iso(),
        "decompiler": "cfr",
        "source": {"type": "local_file", "path": str(jar_path)},
        "evidence": "FACT",
    }

    contracts = extract_contracts(str(decompiled_dir))
    symbols, methods, fields = flatten_index_rows(contracts, meta)

    jar_dir = index_root / "by-sha256" / digest
    jar_dir.mkdir(parents=True, exist_ok=True)
    write_json(jar_dir / "jar-meta.json", meta)
    write_jsonl(jar_dir / "contracts.jsonl", symbols)  # Phase 1: contracts=symbols rows
    write_jsonl(jar_dir / "symbols.jsonl", symbols)
    write_jsonl(jar_dir / "methods.jsonl", methods)
    write_jsonl(jar_dir / "fields.jsonl", fields)
    (jar_dir / "contract.md").write_text(render_contract_md(meta, symbols, methods, fields), encoding="utf-8")

    if keep_source:
        target = jar_dir / "decompiled"
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(decompiled_dir, target)

    append_registry(index_root, meta)
    if meta.get("version"):
        alias_name = f"{meta['artifact_id']}-{meta['version']}.json"
        write_json(index_root / "aliases" / alias_name, {"sha256": digest, "artifact_id": meta["artifact_id"], "version": meta["version"]})

    return meta


def iter_jsonl(path):
    path = Path(path)
    if not path.exists():
        return
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def query_index(index_root=DEFAULT_INDEX_ROOT, symbol=None, fqn=None, method=None, domain=None):
    index_root = Path(index_root)
    hits = {"symbols": [], "methods": [], "fields": []}
    by_sha = index_root / "by-sha256"
    if not by_sha.exists():
        return hits
    for jar_dir in by_sha.iterdir():
        if not jar_dir.is_dir():
            continue
        for row in iter_jsonl(jar_dir / "symbols.jsonl") or []:
            if symbol and row.get("name") != symbol:
                continue
            if fqn and row.get("fqn") != fqn:
                continue
            if domain and row.get("domain_hint") != domain:
                continue
            if symbol or fqn or domain:
                hits["symbols"].append(row)
        if method:
            for row in iter_jsonl(jar_dir / "methods.jsonl") or []:
                if row.get("method_name") == method:
                    hits["methods"].append(row)
    return hits


def print_query_results(results):
    for key in ("symbols", "methods", "fields"):
        rows = results.get(key, [])
        print(f"{key}: {len(rows)}")
        for row in rows[:50]:
            if key == "symbols":
                print(f"  {row.get('artifact_id')}:{row.get('version')} {row.get('kind')} {row.get('fqn')} [{row.get('domain_hint', '')}]")
            elif key == "methods":
                print(f"  {row.get('artifact_id')}:{row.get('version')} {row.get('owner_fqn')}#{row.get('signature')}")
            else:
                print(f"  {row.get('owner_fqn')}#{row.get('field_name')}")


def index_jar(jar_path, index_root=DEFAULT_INDEX_ROOT, keep_source=False):
    jar_path = Path(jar_path)
    if not jar_path.exists():
        raise FileNotFoundError(f"jar not found: {jar_path}")
    digest = sha256_file(jar_path)
    jar_dir = Path(index_root) / "by-sha256" / digest
    if (jar_dir / "jar-meta.json").exists():
        with (jar_dir / "jar-meta.json").open("r", encoding="utf-8") as f:
            meta = json.load(f)
        print(f"Index hit: {jar_path.name} sha256={digest}")
        return meta

    output_dir = jar_dir / "decompiled-work"
    decompile_jar(str(jar_path), str(output_dir))
    meta = index_decompiled_dir(str(jar_path), str(output_dir), str(index_root), keep_source=keep_source)
    if not keep_source and output_dir.exists():
        shutil.rmtree(output_dir)
    print(f"Indexed: {meta['file_name']} sha256={meta['sha256']}")
    return meta


def index_dir(jar_dir, pattern="*.jar", index_root=DEFAULT_INDEX_ROOT, keep_source=False):
    jar_dir = Path(jar_dir)
    jars = sorted(p for p in jar_dir.rglob("*") if p.is_file() and fnmatch.fnmatch(p.name, pattern))
    print(f"Found jars: {len(jars)}")
    metas = []
    for jar in jars:
        metas.append(index_jar(str(jar), str(index_root), keep_source=keep_source))
    return metas


def print_status(index_root=DEFAULT_INDEX_ROOT):
    index_root = Path(index_root)
    registry = list(iter_jsonl(index_root / "registry.jsonl") or [])
    print(f"Index root: {index_root}")
    print(f"Jars: {len(registry)}")
    for row in registry:
        print(f"  {row.get('artifact_id')}:{row.get('version')} {row.get('file_name')} sha256={row.get('sha256')[:12]}")


def build_parser():
    parser = argparse.ArgumentParser(description="Decompile jar and build/query Seeyon contract index")
    sub = parser.add_subparsers(dest="command")

    p_index = sub.add_parser("index")
    p_index.add_argument("jar_path")
    p_index.add_argument("--index-root", default=str(DEFAULT_INDEX_ROOT))
    p_index.add_argument("--keep-source", action="store_true")

    p_index_dir = sub.add_parser("index-dir")
    p_index_dir.add_argument("jar_dir")
    p_index_dir.add_argument("--pattern", default="*.jar")
    p_index_dir.add_argument("--index-root", default=str(DEFAULT_INDEX_ROOT))
    p_index_dir.add_argument("--keep-source", action="store_true")

    p_query = sub.add_parser("query")
    p_query.add_argument("--index-root", default=str(DEFAULT_INDEX_ROOT))
    p_query.add_argument("--symbol")
    p_query.add_argument("--fqn")
    p_query.add_argument("--method")
    p_query.add_argument("--domain")

    p_status = sub.add_parser("status")
    p_status.add_argument("--index-root", default=str(DEFAULT_INDEX_ROOT))

    return parser


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)

    # Backward compatible legacy mode: python decompile_jar.py <jar_path> <output_dir>
    if len(argv) >= 2 and argv[0] not in {"index", "index-dir", "query", "status", "-h", "--help"}:
        jar_path, output_dir = argv[0], argv[1]
        if not os.path.exists(jar_path):
            print(f"ERROR: jar not found: {jar_path}")
            return 1
        decompile_jar(jar_path, output_dir)
        contracts = extract_contracts(output_dir)
        print_summary(contracts)
        return 0

    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "index":
        index_jar(args.jar_path, args.index_root, keep_source=args.keep_source)
        return 0
    if args.command == "index-dir":
        index_dir(args.jar_dir, args.pattern, args.index_root, keep_source=args.keep_source)
        return 0
    if args.command == "query":
        results = query_index(args.index_root, symbol=args.symbol, fqn=args.fqn, method=args.method, domain=args.domain)
        print_query_results(results)
        return 0
    if args.command == "status":
        print_status(args.index_root)
        return 0
    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
