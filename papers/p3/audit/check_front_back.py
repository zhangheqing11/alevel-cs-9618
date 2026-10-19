#!/usr/bin/env python3
"""T36: mechanical checks for papers/p3/back.md and front.md.

1. back.md "跨章入口一" table: every example row's primary type lies in the type range named in that line.
2. back.md line 7: on the 18 papers (2022-25, near-duplicate _33 variants of s22-w24 removed), which chapter
   question 1 and the last question belong to (chapter = majority of the question's leaf rows).
Run: ~/.venvs/alevel-cs/bin/python papers/p3/audit/check_front_back.py
"""
from collections import Counter
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).parent))
import check_handbook as h  # noqa: E402


def table_types():
    out = []
    lines = (h.ROOT / 'papers/p3/back.md').read_text().splitlines()
    for i, line in enumerate(lines[8:31], start=9):
        cells = line.split('|')
        if len(cells) < 5:
            continue
        allowed = set()
        for ch, a, b in re.findall(r'([A-Z]{2})-(\d\d) 至 [A-Z]{2}-(\d\d)', cells[3]):
            allowed |= {f'P3-{ch}-{k:02d}' for k in range(int(a), int(b) + 1)}
        allowed |= {f'P3-{ch}-{n}' for ch, n in re.findall(r'([A-Z]{2})-(\d\d)', cells[3])}
        for rid in re.findall(h.REF, cells[4]):
            t = h.ROWS[rid]['types']['primary']
            if t not in allowed:
                out.append((i, rid, t, sorted(allowed)))
    return out


def paper_order():
    rows = [r for r in h.ROWS.values() if not r.get('extension') and 2022 <= r['year'] <= 2025]
    papers = sorted({r['paper'] for r in rows})
    near_dup = {p for p in papers if p.endswith('_33') and not p.startswith(('9618_s25', '9618_w25'))}
    use = [p for p in papers if p not in near_dup]
    first, last = Counter(), Counter()
    for p in use:
        leaves = [r for r in rows if r['paper'] == p]

        def chapter(q):
            return Counter(r['types']['primary'].split('-')[1] for r in leaves if r['qn'] == q).most_common(1)[0][0]
        first[chapter(min(r['qn'] for r in leaves))] += 1
        last[chapter(max(r['qn'] for r in leaves))] += 1
    return len(use), dict(first), dict(last)


if __name__ == '__main__':
    bad = table_types()
    for b in bad:
        print('back.md line %d: %s is %s, not in %s' % b)
    print('table rows outside stated range:', len(bad))
    print('papers, first-question chapters, last-question chapters:', paper_order())
