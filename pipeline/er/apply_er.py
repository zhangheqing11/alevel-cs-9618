#!/usr/bin/env python3
"""Attach examiner-report excerpts (corpus/er/*.jsonl) to corpus rows as the `er` field.

Usage: python pipeline/er/apply_er.py [--check]

Owns only `er`: every other byte of a row line (field order, spacing, escapes, line endings)
is kept, so the script can be re-run any time (also after P4 rows appear or other
annotation scripts rewrite the rows). --check writes nothing and exits 1 if any row file
would change.

Matching (task T27):
  * a row whose `q` equals an ER label gets that label's text;
  * otherwise the nearest enclosing label ("6(c)" for 6(c)(ii), then "6") is used and the
    text is prefixed with its scope, e.g. "[Q6(c)] ...";
  * a finer ER label than any row (ER says 6(a)(i), rows stop at 6(a)) is never guessed onto
    a row; comments flagged duplicate_label are not attached either. Both are listed by
    `unmatched()` for corpus/er_report.md.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ER_DIR = 'corpus/er'
ROWS_DIR = 'corpus/rows'
FIELD = 'er'


def _unique(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f'duplicate JSON key: {key}')
        out[key] = value
    return out


DECODER = json.JSONDecoder(object_pairs_hook=_unique)


def encode(value) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))


def field_spans(line: str):
    """{key: (key_start, value_start, value_end)} for the top-level object; plus the index of '}'."""
    def skip(i):
        while i < len(line) and line[i].isspace():
            i += 1
        return i

    i = skip(0)
    if i >= len(line) or line[i] != '{':
        raise ValueError('row is not a JSON object')
    i = skip(i + 1)
    spans = {}
    while i < len(line) and line[i] != '}':
        key_start = i
        key, i = DECODER.raw_decode(line, i)
        i = skip(i)
        if line[i] != ':':
            raise ValueError('expected colon')
        start = skip(i + 1)
        _, end = DECODER.raw_decode(line, start)
        spans[key] = (key_start, start, end)
        i = skip(end)
        if line[i] == '}':
            break
        if line[i] != ',':
            raise ValueError('expected comma')
        i = skip(i + 1)
    return spans, i


def merge_line(line: str, text: str | None) -> str:
    """Set (text) or remove (None) the `er` field; everything else is untouched."""
    spans, close = field_spans(line)
    if FIELD in spans:
        key_start, start, end = spans[FIELD]
        if text is not None:
            return line[:start] + encode(text) + line[end:]
        # remove together with its separating comma
        before = line[:key_start].rstrip()
        if before.endswith(','):
            cut = len(before) - 1
            return line[:cut] + line[end:]
        after = line[end:]
        comma = re.match(r'\s*,\s*', after)
        return line[:key_start] + (after[comma.end():] if comma else after)
    if text is None:
        return line
    insert = (',' if spans else '') + encode(FIELD) + ':' + encode(text)
    return line[:close] + insert + line[close:]


# ------------------------------------------------------------------ ER side

def load_er(root: Path):
    """-> (by_paper: {paper: {label: entry}}, duplicates: [entry], generals: {paper: entry})"""
    by_paper: dict[str, dict[str, dict]] = defaultdict(dict)
    duplicates, generals = [], {}
    for path in sorted((root / ER_DIR).glob('*.jsonl')):
        for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            entry = json.loads(line)
            if entry['label'] == '_general':
                generals[entry['paper']] = entry
            elif entry.get('duplicate_label'):
                duplicates.append(entry)
            elif entry['label'] in by_paper[entry['paper']]:
                raise ValueError(f'{path}:{number}: duplicate label {entry["paper"]} {entry["label"]}')
            else:
                by_paper[entry['paper']][entry['label']] = entry
    return by_paper, duplicates, generals


def ancestors(q: str):
    """'6(c)(ii)' -> ['6(c)(ii)', '6(c)', '6']"""
    out = [q]
    while q.endswith(')'):
        q = q[:q.rindex('(')]
        out.append(q)
    return out


def excerpt_for(q: str, labels: dict[str, dict]):
    """-> (text, label_used) or (None, None)."""
    for i, label in enumerate(ancestors(q)):
        entry = labels.get(label)
        if entry:
            text = entry['text'] if i == 0 else f'[Q{label}] {entry["text"]}'
            return text, label
    return None, None


# ------------------------------------------------------------------ rows side

def row_files(root: Path):
    return sorted((root / ROWS_DIR).glob('p*/*.jsonl'))


def plan(root: Path = ROOT):
    """Compute new content for every row file.

    -> (changes {path: new_bytes}, stats {paper: {...}}, er_labels_used {paper: set})
    """
    by_paper, duplicates, generals = load_er(root)
    changes = {}
    stats: dict[str, dict] = {}
    used: dict[str, set] = defaultdict(set)
    for path in row_files(root):
        raw = path.read_bytes().decode('utf-8')
        lines = raw.splitlines(keepends=True)
        paper = path.stem
        labels = by_paper.get(paper, {})
        st = stats.setdefault(paper, dict(rows=0, attached=0, own=0, inherited=0, no_er=0, rows_file=str(path.relative_to(root))))
        out = []
        for line in lines:
            if not line.strip():
                out.append(line)
                continue
            row = json.loads(line, object_pairs_hook=_unique)
            if row['paper'] != paper:
                raise ValueError(f'{path}: row {row["id"]} belongs to {row["paper"]}')
            text, label = excerpt_for(row['q'], labels)
            st['rows'] += 1
            if text is None:
                st['no_er'] += 1
            else:
                st['attached'] += 1
                st['own' if label == row['q'] else 'inherited'] += 1
                used[paper].add(label)
            out.append(merge_line(line, text))
        new = ''.join(out)
        if new != raw:
            changes[path] = new.encode('utf-8')
    return changes, stats, used


def unmatched(root: Path = ROOT, stats=None, used=None):
    """ER labels that reached no row -> [(paper, label, reason, entry)]"""
    by_paper, duplicates, generals = load_er(root)
    if stats is None or used is None:
        _, stats, used = plan(root)
    rows_by_paper: dict[str, set] = defaultdict(set)
    for path in row_files(root):
        for line in path.read_text(encoding='utf-8').splitlines():
            if line.strip():
                rows_by_paper[path.stem].add(json.loads(line)['q'])
    out = []
    for paper, labels in sorted(by_paper.items()):
        rows = rows_by_paper.get(paper)
        for label, entry in labels.items():
            if label in used.get(paper, set()):
                continue
            if rows is None:
                reason = 'no rows for this paper in corpus/rows (not extracted yet)'
            else:
                children = sorted(q for q in rows if label in ancestors(q)[1:])
                if children:  # cannot happen: a parent label always reaches its leaf rows
                    reason = 'covered only by more specific ER labels: ' + ', '.join(children)
                elif any(label in ancestors(x)[1:] for x in labels if x != label) and not any(
                        r == label for r in rows):
                    reason = 'ER label is finer than any row; no row to carry it'
                else:
                    reason = 'no row with this question number (ER label finer than rows, or ER typo)'
            out.append((paper, label, reason, entry))
    for entry in duplicates:
        out.append((entry['paper'], entry['label'], 'ER prints this label twice; second block not attached', entry))
    return out


def write_atomic(path: Path, data: bytes):
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix='.er-', delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(data)
        os.chmod(temporary, path.stat().st_mode & 0o777)
        os.replace(temporary, path)
    finally:
        if temporary and temporary.exists():
            temporary.unlink()


def apply(root: Path = ROOT, check: bool = False):
    changes, stats, used = plan(root)
    if not check:
        for path, data in changes.items():
            write_atomic(path, data)
    return changes, stats, used


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='exit 1 if any row file would change; never writes')
    args = parser.parse_args()
    try:
        changes, stats, used = apply(check=args.check)
    except (ValueError, KeyError, OSError) as exc:
        sys.exit(f'ER application failed: {exc}')
    rows = sum(s['rows'] for s in stats.values())
    attached = sum(s['attached'] for s in stats.values())
    if args.check:
        if changes:
            sys.exit(f'{len(changes)} row file(s) need er updates (run apply_er.py)')
        print(f'er is current: {attached}/{rows} rows carry an excerpt, 0 files would change')
    else:
        print(f'{attached}/{rows} rows carry an excerpt; updated {len(changes)} row files')


if __name__ == '__main__':
    main()
