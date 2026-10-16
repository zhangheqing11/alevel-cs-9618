#!/usr/bin/env python3
"""Download 9618 past-paper material from PapaCambridge into sources/pastpapers/.

Re-runnable: existing files are skipped; every attempt is logged to
pipeline/download/manifest.csv (url, file, status, bytes).

  fetch.py --dry-run                 # list candidate files, download nothing
  fetch.py --only s24 --kinds qp,ms --papers 12
  fetch.py                           # everything (2021 – 2026 June)
"""
from __future__ import annotations

import argparse
import csv
import os
import pathlib
import sys
import ssl
import time
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[2]
SOURCES = pathlib.Path(os.environ.get("ALEVEL_CS_SOURCES", "/Users/zhangheqing/Desktop/alevel cs/sources"))
DEST = SOURCES / "pastpapers"
MANIFEST = ROOT / "pipeline" / "download" / "manifest.csv"
BASE = "https://pastpapers.papacambridge.com/directories/CAIE/CAIE-pastpapers/upload/"
import certifi  # python.org builds ship without CA roots

SSL_CTX = ssl.create_default_context(cafile=certifi.where())
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) personal-study-downloader"

# (session, two-digit year). March series has variant 2 only; w26 not yet released.
SESSIONS = [(s, y) for y in range(21, 26) for s in ("m", "s", "w")] + [("m", 26), ("s", 26)]


def candidates(only: set[str] | None, kinds: set[str] | None, papers: set[str] | None):
    for sess, yy in SESSIONS:
        code = f"{sess}{yy:02d}"
        if only and code not in only:
            continue
        variants = (2,) if sess == "m" else (1, 2, 3)
        per_paper = []
        for comp in (1, 2, 3, 4):
            for v in variants:
                p = f"{comp}{v}"
                if papers and p not in papers:
                    continue
                per_paper += [("qp", p, "pdf"), ("ms", p, "pdf")]
                if comp == 2:
                    per_paper.append(("in", p, "pdf"))   # P2 insert (built-in functions)
                if comp == 4:
                    per_paper.append(("sf", p, "zip"))   # P4 source files
        per_session = [] if papers else [("er", None, "pdf"), ("gt", None, "pdf")]
        for kind, p, ext in per_paper + per_session:
            if kinds and kind not in kinds:
                continue
            name = f"9618_{code}_{kind}_{p}.{ext}" if p else f"9618_{code}_{kind}.{ext}"
            yield name


def looks_valid(data: bytes, name: str) -> bool:
    return data.startswith(b"%PDF") if name.endswith(".pdf") else data.startswith(b"PK")


def fetch(name: str, retries: int = 2) -> tuple[str, int]:
    url = BASE + name
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60, context=SSL_CTX) as resp:
                data = resp.read()
            if not looks_valid(data, name):
                return "invalid-content", len(data)
            (DEST / name).write_bytes(data)
            return "ok", len(data)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return "missing", 0
            if attempt == retries:
                return f"http-{e.code}", 0
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt == retries:
                return f"error-{type(e).__name__}", 0
        time.sleep(2 * (attempt + 1))
    return "error", 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", help="comma-separated session codes, e.g. s24,w24")
    ap.add_argument("--kinds", help="comma-separated kinds: qp,ms,in,sf,er,gt")
    ap.add_argument("--papers", help="comma-separated paper numbers, e.g. 12,22")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--delay", type=float, default=0.4, help="seconds between requests")
    args = ap.parse_args()
    split = lambda s: set(s.split(",")) if s else None
    names = list(candidates(split(args.only), split(args.kinds), split(args.papers)))
    if args.dry_run:
        print("\n".join(names))
        print(f"{len(names)} candidate files")
        return 0

    DEST.mkdir(parents=True, exist_ok=True)
    log = {}
    if MANIFEST.exists():
        with MANIFEST.open(encoding="utf-8", newline="") as f:
            log = {r["file"]: r for r in csv.DictReader(f)}
    counts: dict[str, int] = {}
    for i, name in enumerate(names, 1):
        if (DEST / name).exists():
            status, size = "ok", (DEST / name).stat().st_size
        else:
            status, size = fetch(name)
            time.sleep(args.delay)
        log[name] = {"file": name, "url": BASE + name, "status": status, "bytes": size}
        counts[status] = counts.get(status, 0) + 1
        print(f"[{i}/{len(names)}] {status:<16} {name}", flush=True)
    with MANIFEST.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["file", "url", "status", "bytes"])
        w.writeheader()
        w.writerows(sorted(log.values(), key=lambda r: r["file"]))
    print("summary:", counts)
    return 0


if __name__ == "__main__":
    sys.exit(main())
