#!/usr/bin/env python3
"""Fetch and search Seeyon V8 Yuque docs with auto-login.

Auto-login flow:
1. Reads credentials from secrets.json (same directory as this script)
2. Visits https://www.yuque.com/login to get a session cookie
3. Uses that session for all subsequent page/API requests
4. For specific doc URLs, fetches /markdown variant for richer content extraction
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as _dt
import html
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import http.cookiejar
from dataclasses import dataclass, asdict
from typing import Any, Iterable

try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass

DEFAULT_BOOK_URL = "https://www.yuque.com/seeyonkk/v8"
API_DOCS_URL = "https://www.yuque.com/api/v2/repos/{namespace}/{book}/docs"
API_DOC_URL = "https://www.yuque.com/api/v2/repos/{namespace}/{book}/docs/{slug}"
MAX_RECORDED_ERRORS = 20
SECRETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "secrets.json")

# Global session: a cookie-aware opener initialized lazily
_session_opener: urllib.request.OpenerDirector | None = None


@dataclass
class Source:
    title: str
    url: str
    snippet: str
    score: int
    source_type: str
    usable_as_evidence: bool


def load_secrets() -> dict[str, str]:
    """Load credentials from secrets.json."""
    if os.path.exists(SECRETS_PATH):
        try:
            with open(SECRETS_PATH, encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def init_session() -> urllib.request.OpenerDirector:
    """Create a cookie-aware opener and initialize a Yuque session.

    Visits the login page to obtain a session cookie. The session cookie
    is sufficient to access most public docs. For private docs, actual
    login via /api/sessions would be needed.
    """
    global _session_opener
    if _session_opener is not None:
        return _session_opener

    cookie_jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(cookie_jar),
    )
    _session_opener = opener

    # Visit login page to get session cookie
    req = urllib.request.Request(
        "https://www.yuque.com/login",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        },
    )
    try:
        with opener.open(req, timeout=20):
            pass
    except Exception:
        pass  # Non-critical: session might still work on some endpoints

    # Attempt actual login if credentials are available
    secrets = load_secrets()
    phone = secrets.get("phone", "") or os.environ.get("YUQUE_PHONE", "")
    password = secrets.get("password", "") or os.environ.get("YUQUE_PASSWORD", "")
    if phone and password:
        try:
            ctoken = _get_ctoken(cookie_jar)
            login_data = json.dumps({"login": phone, "password": password}).encode()
            login_req = urllib.request.Request(
                "https://www.yuque.com/api/sessions",
                data=login_data,
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "Referer": "https://www.yuque.com/login",
                    "Origin": "https://www.yuque.com",
                    "X-CSRF-Token": ctoken or "",
                    "Accept": "application/json, text/plain, */*",
                },
            )
            with opener.open(login_req, timeout=15):
                pass
        except Exception:
            pass  # Login failure is non-fatal; session from /login may still work

    return opener


def _get_ctoken(cookie_jar: http.cookiejar.CookieJar) -> str | None:
    for c in cookie_jar:
        if c.name == "yuque_ctoken":
            return c.value
    return None


def get_session() -> urllib.request.OpenerDirector:
    if _session_opener is None:
        return init_session()
    return _session_opener


def request_text(url: str, timeout: int = 20, extra_headers: dict[str, str] | None = None) -> tuple[str | None, str | None]:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "text/html,application/json,text/plain,*/*",
    }
    token = os.environ.get("YUQUE_TOKEN")
    if token:
        headers["X-Auth-Token"] = token
    if extra_headers:
        headers.update(extra_headers)

    opener = get_session()
    req = urllib.request.Request(url, headers=headers)
    try:
        with opener.open(req, timeout=timeout) as resp:
            charset = resp.headers.get_content_charset() or "utf-8"
            data = resp.read()
            return data.decode(charset, errors="replace"), None
    except urllib.error.HTTPError as exc:
        return None, f"HTTP {exc.code} {url}"
    except urllib.error.URLError as exc:
        return None, f"URL error {url}: {exc.reason}"
    except Exception as exc:
        return None, f"Unexpected error {url}: {exc}"


def parse_book_ref(book_url: str) -> tuple[str, str]:
    parsed = urllib.parse.urlparse(book_url)
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 2:
        return "seeyonkk", "v8"
    return parts[0], parts[1]


def strip_html(value: str) -> str:
    value = re.sub(r"(?is)<script.*?</script>", " ", value)
    value = re.sub(r"(?is)<style.*?</style>", " ", value)
    value = re.sub(r"(?is)<[^>]+>", " ", value)
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def query_terms(query: str) -> list[str]:
    terms = [term.lower() for term in re.findall(r"[a-zA-Z0-9_\-.]+|[\u4e00-\u9fff]{2,}", query)]
    for chunk in re.findall(r"[\u4e00-\u9fff]{3,}", query):
        terms.extend(chunk[i : i + 2] for i in range(0, len(chunk) - 1))
    seen: set[str] = set()
    result: list[str] = []
    for term in terms:
        if term not in seen:
            seen.add(term)
            result.append(term)
    return result


def score_text(query: str, title: str, body: str) -> int:
    terms = query_terms(query)
    haystack = f"{title}\n{body}".lower()
    score = 0
    for term in terms:
        hits = haystack.count(term)
        if hits:
            score += min(hits, 5)
            if term in title.lower():
                score += 3
    return score


def make_snippet(query: str, body: str, width: int = 360) -> str:
    compact = re.sub(r"\s+", " ", body).strip()
    if not compact:
        return ""
    lower = compact.lower()
    positions = [lower.find(term) for term in query_terms(query) if lower.find(term) >= 0]
    start = max(min(positions) - 80, 0) if positions else 0
    snippet = compact[start : start + width]
    if start > 0:
        snippet = "..." + snippet
    if start + width < len(compact):
        snippet += "..."
    return snippet


def normalize_doc_url(book_url: str, slug: str | None) -> str:
    base = book_url.rstrip("/")
    return f"{base}/{slug}" if slug else base


def iter_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for child in value.values():
            yield from iter_strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_strings(child)


def load_json(text: str | None) -> Any | None:
    if text is None:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def extract_doc_body_from_appdata(html_text: str) -> str:
    """Extract doc body from appData embedded in a Yuque page.

    The document content is stored in appData.doc._cachedContent.body
    (HTML format) or body_asl (Yuque lake format).
    """
    match = re.search(
        r'window\.appData\s*=\s*JSON\.parse\(decodeURIComponent\(\"(.+?)\"\)\)',
        html_text,
    )
    if not match:
        return ""

    try:
        decoded = urllib.parse.unquote(match.group(1))
        app_data = json.loads(decoded)
        doc = app_data.get("doc", {})
        cached = doc.get("_cachedContent", {})
        body = cached.get("body", "")
        if body:
            return body
        body_asl = cached.get("body_asl", "")
        if body_asl:
            return body_asl
        body_draft = cached.get("body_draft", "")
        if body_draft:
            return body_draft
    except Exception:
        pass
    return ""


def fetch_api_sources(query: str, book_url: str, max_results: int, errors: list[str]) -> list[Source]:
    namespace, book = parse_book_ref(book_url)
    docs_url = API_DOCS_URL.format(namespace=namespace, book=book)
    text, err = request_text(docs_url)
    if err:
        errors.append(f"Yuque docs API list failed: {err}")
        return []

    payload = load_json(text or "")
    docs = payload.get("data", []) if isinstance(payload, dict) else []
    if not isinstance(docs, list):
        errors.append("Yuque docs API returned an unexpected shape.")
        return []

    candidates: list[tuple[int, dict[str, Any]]] = []
    for doc in docs:
        if not isinstance(doc, dict):
            continue
        title = str(doc.get("title") or doc.get("name") or "")
        slug = str(doc.get("slug") or "")
        summary = " ".join(str(doc.get(key) or "") for key in ("description", "summary", "body", "body_html"))
        candidates.append((score_text(query, title, summary), doc))

    candidates.sort(key=lambda item: item[0], reverse=True)
    sources: list[Source] = []
    for _, doc in candidates[: max(max_results * 2, max_results)]:
        slug = str(doc.get("slug") or "")
        if not slug:
            continue
        detail_url = API_DOC_URL.format(namespace=namespace, book=book, slug=urllib.parse.quote(slug))
        detail_text, detail_err = request_text(detail_url)
        if detail_err:
            errors.append(f"Yuque docs API detail failed for {slug}: {detail_err}")
            continue
        detail = load_json(detail_text or "")
        data = detail.get("data", {}) if isinstance(detail, dict) else {}
        if not isinstance(data, dict):
            continue
        title = str(data.get("title") or doc.get("title") or slug)
        body = strip_html(str(data.get("body") or data.get("body_html") or data.get("description") or ""))
        # Fall back to page-level extraction if API body is empty
        if not body:
            page_text, _ = request_text(normalize_doc_url(book_url, slug))
            if page_text:
                doc_body = extract_doc_body_from_appdata(page_text)
                if doc_body:
                    body = strip_html(doc_body)
        score = score_text(query, title, body)
        if score <= 0 and query.strip():
            continue
        sources.append(Source(title, normalize_doc_url(book_url, slug), make_snippet(query, body), score, "yuque-api", True))
        if len(sources) >= max_results:
            break
    return sources


def extract_app_data(html_text: str) -> Any | None:
    match = re.search(r"window\.appData\s*=\s*JSON\.parse\(decodeURIComponent\(\"(.+?)\"\)\)", html_text)
    if not match:
        return None
    try:
        decoded = urllib.parse.unquote(match.group(1))
        return json.loads(decoded)
    except Exception:
        return None


def fetch_page_source(query: str, url: str, source_type: str = "yuque-page", usable_as_evidence: bool = True) -> tuple[Source | None, list[str]]:
    errors: list[str] = []

    # Try fetching the /markdown variant which contains richer embedded content
    markdown_url = url.rstrip("/") + "/markdown"
    text, err = request_text(markdown_url)
    if not err and text:
        doc_body_html = extract_doc_body_from_appdata(text)
        if doc_body_html:
            # We got rich content from the /markdown page
            title_match = re.search(r"(?is)<title>(.*?)</title>", text[:2000])
            title = strip_html(title_match.group(1)) if title_match else url
            body = strip_html(doc_body_html)
            source = Source(
                title=title,
                url=url,
                snippet=make_snippet(query, body),
                score=score_text(query, title, body),
                source_type=source_type,
                usable_as_evidence=usable_as_evidence,
            )
            return source, errors

    # Fall back to regular page fetch
    text, err = request_text(url)
    if err:
        errors.append(err)
        return None, errors

    text = text or ""
    title_match = re.search(r"(?is)<title>(.*?)</title>", text)
    title = strip_html(title_match.group(1)) if title_match else url
    app_data = extract_app_data(text)
    app_text = " ".join(iter_strings(app_data)) if app_data is not None else ""
    body = strip_html(text)
    combined = f"{app_text}\n{body}".strip()
    source = Source(
        title=title,
        url=url,
        snippet=make_snippet(query, combined),
        score=score_text(query, title, combined),
        source_type=source_type,
        usable_as_evidence=usable_as_evidence,
    )
    return source, errors


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Search Seeyon V8 Yuque documentation.")
    parser.add_argument("--query", required=True, help="Requirement or search keywords.")
    parser.add_argument("--book", default=DEFAULT_BOOK_URL, help="Yuque book URL. Defaults to seeyonkk/v8.")
    parser.add_argument("--url", action="append", default=None, help="Specific Yuque document URL to fetch first. Can be repeated.")
    parser.add_argument("--max-results", type=int, default=8, help="Maximum source snippets to return.")
    parser.add_argument("--out", help="Optional JSON output path.")
    args = parser.parse_args(argv)

    # Initialize session at the start (auto-login)
    get_session()

    errors: list[str] = []
    sources: list[Source] = []

    for url in (args.url or []):
        source, page_errors = fetch_page_source(args.query, url, "specific-page", usable_as_evidence=True)
        errors.extend(page_errors)
        if source and (source.score > 0 or not args.query.strip()):
            sources.append(source)

    if len(sources) < args.max_results:
        sources.extend(fetch_api_sources(args.query, args.book, args.max_results - len(sources), errors))

    if len(sources) < args.max_results:
        source, page_errors = fetch_page_source(args.query, args.book, "book-overview-page", usable_as_evidence=False)
        errors.extend(page_errors)
        if source:
            sources.append(source)

    unique: dict[str, Source] = {}
    for source in sorted(sources, key=lambda item: item.score, reverse=True):
        if source.url not in unique:
            unique[source.url] = source

    result = {
        "query": args.query,
        "book": args.book,
        "fetched_at": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "sources": [asdict(source) for source in list(unique.values())[: args.max_results]],
        "errors": errors,
        "evidence_warning": (
            "Sources with usable_as_evidence=false are only access diagnostics or book overview pages; "
            "do not use them as proof for V8 API/code details."
        ),
        "fallback_instruction": (
            "If sources are empty or only show the book overview, the Yuque book likely requires login/API authorization. "
            "Ask for a specific public doc URL, exported Markdown/HTML, or credentials configured through secrets.json."
        ),
    }

    output = json.dumps(result, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write(output)
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
