#!/usr/bin/env python3
"""Validate a generated Seeyon V8 Super SPI project.

This validator is intentionally static-first. Maven availability and private
repository reachability are environment states; static structure failures are
real workflow failures.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable, List, Optional, Tuple


FORBIDDEN_SPRING_ANNOTATIONS = ["@Autowired", "@Service", "@Component", "@Repository", "@Controller"]
MQ_REQUIRED_METHODS = ["send", "sendBatch", "subscribeTopic", "unSubscribeTopic"]


@dataclass
class Check:
    name: str
    status: str  # PASS | FAIL | WARN | SKIP
    detail: str = ""


def add(checks: List[Check], name: str, status: str, detail: str = "") -> None:
    checks.append(Check(name=name, status=status, detail=detail))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def parse_xml(path: Path) -> Tuple[Optional[ET.Element], Optional[str]]:
    try:
        return ET.parse(path).getroot(), None
    except Exception as exc:  # noqa: BLE001 - validator should report, not crash
        return None, str(exc)


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1] if "}" in tag else tag


def child_texts(root: ET.Element, child_name: str) -> List[str]:
    values: List[str] = []
    for elem in root.iter():
        if local_name(elem.tag) == child_name and elem.text:
            values.append(elem.text.strip())
    return [v for v in values if v]


def find_modules(root_pom: Path) -> List[str]:
    root, err = parse_xml(root_pom)
    if root is None:
        return []
    return child_texts(root, "module")


def iter_files(root: Path, pattern: str) -> Iterable[Path]:
    if not root.exists():
        return []
    return root.rglob(pattern)


def relative_list(paths: Iterable[Path], root: Path, limit: int = 20) -> str:
    rels = []
    for p in paths:
        try:
            rels.append(str(p.relative_to(root)).replace("\\", "/"))
        except ValueError:
            rels.append(str(p))
        if len(rels) >= limit:
            break
    return ", ".join(rels)


def has_file(module_dir: Path, rel: str) -> bool:
    return (module_dir / rel).is_file()


def java_sources(module_dir: Path) -> List[Path]:
    src = module_dir / "src" / "main" / "java"
    return list(src.rglob("*.java")) if src.exists() else []


def all_java_text(module_dir: Path) -> str:
    chunks = []
    for p in java_sources(module_dir):
        chunks.append(read_text(p))
    return "\n".join(chunks)


def check_project(root: Path, run_maven: str = "auto") -> List[Check]:
    checks: List[Check] = []
    root = root.resolve()

    if not root.exists():
        add(checks, "project_root_exists", "FAIL", f"not found: {root}")
        return checks
    if not root.is_dir():
        add(checks, "project_root_is_dir", "FAIL", f"not a directory: {root}")
        return checks
    add(checks, "project_root_exists", "PASS", str(root))

    root_pom = root / "pom.xml"
    if not root_pom.is_file():
        add(checks, "root_pom_exists", "FAIL", "missing pom.xml")
        modules: List[str] = []
    else:
        add(checks, "root_pom_exists", "PASS", "pom.xml")
        xml_root, err = parse_xml(root_pom)
        if xml_root is None:
            add(checks, "root_pom_xml_well_formed", "FAIL", err or "parse failed")
            modules = []
        else:
            add(checks, "root_pom_xml_well_formed", "PASS")
            modules = find_modules(root_pom)
            if modules:
                add(checks, "root_pom_modules_present", "PASS", ", ".join(modules))
            else:
                add(checks, "root_pom_modules_present", "FAIL", "no <module> entries")

    # Forbidden project-level structure.
    lib_dir = root / "lib"
    if lib_dir.exists():
        add(checks, "no_root_lib_dir", "FAIL", "lib/ is forbidden; use third-jar + Maven install/deploy")
    else:
        add(checks, "no_root_lib_dir", "PASS")

    pom_files = list(root.rglob("pom.xml"))
    system_path_hits = [p for p in pom_files if "<systemPath>" in read_text(p)]
    if system_path_hits:
        add(checks, "no_systemPath", "FAIL", relative_list(system_path_hits, root))
    else:
        add(checks, "no_systemPath", "PASS")

    # Module checks.
    module_dirs: List[Path] = []
    for module in modules:
        module_dir = root / module
        module_dirs.append(module_dir)
        if module_dir.is_dir():
            add(checks, f"module_exists:{module}", "PASS")
        else:
            add(checks, f"module_exists:{module}", "FAIL", f"missing directory {module}")
            continue
        module_pom = module_dir / "pom.xml"
        if not module_pom.is_file():
            add(checks, f"module_pom_exists:{module}", "FAIL")
        else:
            add(checks, f"module_pom_exists:{module}", "PASS")
            parsed, err = parse_xml(module_pom)
            add(checks, f"module_pom_xml_well_formed:{module}", "PASS" if parsed is not None else "FAIL", err or "")

    actual_pom_dirs = sorted(
        p.parent.name for p in root.glob("*/pom.xml") if p.parent.name not in set(modules)
    )
    if actual_pom_dirs:
        add(checks, "extra_unregistered_module_dirs", "WARN", ", ".join(actual_pom_dirs))
    else:
        add(checks, "extra_unregistered_module_dirs", "PASS")

    # spi-common must not register SPI.
    spi_common = root / "spi-common"
    if spi_common.exists():
        forbidden_common = [
            spi_common / "src/main/resources/META-INF/spring.factories",
            spi_common / "src/main/resources/metadata/spi_info.json",
        ]
        hits = [p for p in forbidden_common if p.exists()]
        if hits:
            add(checks, "spi_common_no_spi_registration", "FAIL", relative_list(hits, root))
        else:
            add(checks, "spi_common_no_spi_registration", "PASS")
    else:
        add(checks, "spi_common_present", "WARN", "spi-common not found; allowed only for very small validation-only projects")

    spi_modules = [m for m in modules if m.startswith("spi-") and m != "spi-common"]
    if not spi_modules:
        # Fallback to directories, useful when root pom already failed.
        spi_modules = [p.name for p in root.glob("spi-*") if p.is_dir() and p.name != "spi-common"]
    if spi_modules:
        add(checks, "spi_modules_present", "PASS", ", ".join(spi_modules))
    else:
        add(checks, "spi_modules_present", "FAIL", "no business SPI module such as spi-sso/spi-mq/spi-{domain}")

    for module in spi_modules:
        module_dir = root / module
        sf = module_dir / "src/main/resources/META-INF/spring.factories"
        spi_info = module_dir / "src/main/resources/metadata/spi_info.json"
        if sf.is_file() and sf.stat().st_size > 0:
            add(checks, f"spring_factories_present:{module}", "PASS")
        else:
            add(checks, f"spring_factories_present:{module}", "FAIL", "missing or empty META-INF/spring.factories")
        if not spi_info.is_file():
            add(checks, f"spi_info_json_present:{module}", "FAIL", "missing metadata/spi_info.json")
        else:
            try:
                data = json.loads(read_text(spi_info))
                add(checks, f"spi_info_json_well_formed:{module}", "PASS")
                scopes = data.get("scopes")
                spring_factories_text = read_text(sf) if sf.is_file() else ""
                if scopes == ["ALL"]:
                    add(checks, f"spi_info_scopes_acceptable:{module}", "PASS", "scopes=['ALL']")
                elif "AbstractThirdAffairService" in spring_factories_text and scopes == ["ctp-affair"]:
                    add(checks, f"spi_info_scopes_acceptable:{module}", "PASS", "todo-batch/AbstractThirdAffairService allows scopes=['ctp-affair']")
                else:
                    add(checks, f"spi_info_scopes_acceptable:{module}", "WARN", f"scopes={scopes!r}; expected ['ALL'] unless scenario says otherwise")
            except Exception as exc:  # noqa: BLE001
                add(checks, f"spi_info_json_well_formed:{module}", "FAIL", str(exc))

        text = all_java_text(module_dir)
        if not text.strip():
            add(checks, f"java_sources_present:{module}", "WARN", "no Java sources found")
        forbidden_hits = [ann for ann in FORBIDDEN_SPRING_ANNOTATIONS if ann in text]
        if forbidden_hits:
            add(checks, f"no_forbidden_spring_annotations:{module}", "FAIL", ", ".join(forbidden_hits))
        else:
            add(checks, f"no_forbidden_spring_annotations:{module}", "PASS")

    # MQ-specific checks.
    if (root / "spi-mq").exists() or "spi-mq" in spi_modules:
        module_dir = root / "spi-mq"
        text = all_java_text(module_dir)
        add(checks, "mq_module_present", "PASS")
        add(checks, "mq_implements_MQMessageSpi", "PASS" if "MQMessageSpi" in text else "FAIL")
        for method in MQ_REQUIRED_METHODS:
            pattern = rf"\b{re.escape(method)}\s*\("
            add(checks, f"mq_method_present:{method}", "PASS" if re.search(pattern, text) else "FAIL")
        add(checks, "mq_uses_MQSerializer", "PASS" if "MQSerializer" in text else "FAIL")
        add(checks, "mq_invokes_MessageListenerService", "PASS" if "MessageListenerService.invoke" in text else "FAIL")
    else:
        add(checks, "mq_specific_checks", "SKIP", "spi-mq not present")

    # SSO-specific checks.
    if (root / "spi-sso").exists() or "spi-sso" in spi_modules:
        module_dir = root / "spi-sso"
        text = all_java_text(module_dir)
        scenario_markers = ["unifiedauth", "avoidlogin", "connector"]
        marker_hits = []
        for marker in scenario_markers:
            if (module_dir / f"src/main/java/com/seeyon/extend/spi/sso/{marker}").exists() or marker in text:
                marker_hits.append(marker)
        add(checks, "sso_module_present", "PASS")
        if marker_hits:
            add(checks, "sso_scenario_marker_present", "PASS", ", ".join(marker_hits))
        else:
            add(checks, "sso_scenario_marker_present", "WARN", "no unifiedauth/avoidlogin/connector marker found")
    else:
        add(checks, "sso_specific_checks", "SKIP", "spi-sso not present")

    # Optional Maven validate.
    if run_maven == "false":
        add(checks, "maven_validate", "SKIP", "disabled by --maven false")
    else:
        mvn = shutil.which("mvn")
        if not mvn:
            status = "FAIL" if run_maven == "true" else "WARN"
            add(checks, "maven_validate", status, "mvn not found; static validation remains authoritative")
        else:
            try:
                proc = subprocess.run(
                    [mvn, "validate", "-DskipTests"],
                    cwd=str(root),
                    text=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    timeout=120,
                    check=False,
                )
                tail = "\n".join(proc.stdout.splitlines()[-20:])
                add(checks, "maven_validate", "PASS" if proc.returncode == 0 else "WARN", tail)
            except subprocess.TimeoutExpired:
                add(checks, "maven_validate", "WARN", "timeout after 120s; static validation remains authoritative")
            except Exception as exc:  # noqa: BLE001
                add(checks, "maven_validate", "WARN", str(exc))

    return checks


def summarize(checks: List[Check]) -> Tuple[int, dict]:
    counts = {"PASS": 0, "FAIL": 0, "WARN": 0, "SKIP": 0}
    for c in checks:
        counts[c.status] = counts.get(c.status, 0) + 1
    exit_code = 1 if counts.get("FAIL", 0) else 0
    return exit_code, counts


def print_text_report(project_root: Path, checks: List[Check]) -> None:
    exit_code, counts = summarize(checks)
    print("# Generated SPI Project Validation")
    print(f"Project: {project_root}")
    print(f"Summary: PASS={counts.get('PASS',0)} FAIL={counts.get('FAIL',0)} WARN={counts.get('WARN',0)} SKIP={counts.get('SKIP',0)}")
    print(f"Result: {'FAIL' if exit_code else 'PASS'}")
    print()
    print("| Check | Result | Detail |")
    print("|---|---|---|")
    for c in checks:
        detail = c.detail.replace("\n", "<br>").replace("|", "\\|") if c.detail else ""
        print(f"| {c.name} | {c.status} | {detail} |")


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Validate generated Seeyon V8 Super SPI project")
    parser.add_argument("project_root", help="Path to generated custom-backend project root")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of markdown table")
    parser.add_argument("--maven", choices=["auto", "true", "false"], default="auto", help="Run mvn validate: auto/true/false")
    args = parser.parse_args(argv)

    project_root = Path(args.project_root)
    checks = check_project(project_root, run_maven=args.maven)
    exit_code, counts = summarize(checks)

    if args.json:
        print(json.dumps({
            "project_root": str(project_root),
            "result": "FAIL" if exit_code else "PASS",
            "summary": counts,
            "checks": [asdict(c) for c in checks],
        }, ensure_ascii=False, indent=2))
    else:
        print_text_report(project_root, checks)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
