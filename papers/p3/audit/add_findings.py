#!/usr/bin/env python3
"""Append hand-written findings (a JSON list in a file) to T36-findings.jsonl after checking the fields.

  ~/.venvs/alevel-cs/bin/python papers/p3/audit/add_findings.py <findings.json>
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
KEYS = ['file', 'line', 'card', 'kind', 'severity', 'row', 'evidence', 'suggestion']
items = json.loads(Path(sys.argv[1]).read_text())
with open(ROOT / 'papers/p3/audit/T36-findings.jsonl', 'a') as f:
    for x in items:
        assert set(x) == set(KEYS), x
        text = (ROOT / x['file']).read_text().splitlines()[x['line'] - 1]
        print(f"{x['card']} {x['file']}:{x['line']} [{x['severity']}/{x['kind']}] -> {text[:110]}")
        f.write(json.dumps({k: x[k] for k in KEYS}, ensure_ascii=False) + '\n')
