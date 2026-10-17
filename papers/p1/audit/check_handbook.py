#!/usr/bin/env python3
"""Repeatable mechanical audit; PDF text is read directly from the source files.

Run with the shared environment:
  ~/.venvs/alevel-cs/bin/python papers/p1/audit/check_handbook.py
  ~/.venvs/alevel-cs/bin/python papers/p1/audit/check_handbook.py --packet IR --start 1 --end 3
Packets are scratch review aids, not a claim of human verification.
"""
import argparse
import ast
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
SOURCES = Path(os.environ.get('ALEVEL_CS_SOURCES', '/Users/zhangheqing/Desktop/alevel cs/sources'))
ROWS = {r['id']: r for p in (ROOT / 'corpus/rows/p1').glob('*.jsonl') for line in p.read_text().splitlines() if (r := json.loads(line))}
REF = r'⟦([^⟧]+)⟧'

def cards():
    for p in sorted((ROOT / 'papers/p1/cards').glob('*.md')):
        text = p.read_text()
        matches = list(re.finditer(r'^### (P1-[A-Z]+-\d+)\s+.*$', text, re.M))
        for i, m in enumerate(matches):
            section = text[m.start():matches[i+1].start() if i+1 < len(matches) else len(text)]
            rep = re.search(r'#### 代表题精讲\s+' + REF, section)
            var = re.search(r'\*\*下一道变式\*\*\s+' + REF, section)
            yield {'card': m[1], 'file': str(p.relative_to(ROOT)), 'line': text[:m.start()].count('\n')+1, 'text': section, 'representative': rep[1] if rep else None, 'variation': var[1] if var else None}

def source(row, kind):
    import pymupdf
    paper = row['paper'].split('_')
    path = SOURCES / 'pastpapers' / f'{paper[0]}_{paper[1]}_{kind}_{paper[2]}.pdf'
    page = row[f'{kind}_page']
    pages = page if isinstance(page, list) else [page]
    with pymupdf.open(path) as pdf:
        return '\n'.join(f'--- {path.name} p.{n} ---\n' + pdf[n-1].get_text() for n in pages)

def inspect():
    out = []
    for c in cards():
        failures = []
        for role in ('representative', 'variation'):
            rid = c[role]
            if rid not in ROWS:
                failures.append(f'{role}: missing row {rid}')
                continue
            r = ROWS[rid]
            if not 2022 <= r['year'] <= 2025:
                failures.append(f'{role}: year {r["year"]}')
            if r.get('equivalent_of'):
                failures.append(f'{role}: equivalent_of {r["equivalent_of"]}')
            if r['types']['primary'] != c['card']:
                failures.append(f'{role}: primary {r["types"]["primary"]}')
        if c['representative'] and c['variation'] and ROWS[c['representative']]['paper'] == ROWS[c['variation']]['paper']:
            failures.append('representative and variation use the same paper')
        r = ROWS.get(c['representative'], {})
        out.append({k: c[k] for k in ('card', 'file', 'line', 'representative', 'variation')} | {'qp_page': r.get('qp_page'), 'ms_page': r.get('ms_page'), 'pick_failures': failures, 'page_mentions': re.findall(r'QP\s*p\.?\s*(\d+)', c['text'])})
    python_blocks = []
    for p in sorted((ROOT / 'papers/p1').glob('**/*.md')):
        if 'audit' in p.parts:
            continue
        for m in re.finditer(r'```python\n(.*?)```', p.read_text(), re.S):
            try:
                ast.parse(m[1])
                error = None
            except SyntaxError as e:
                error = str(e)
            python_blocks.append({'file': str(p.relative_to(ROOT)), 'error': error})
    return {'cards': out, 'python_blocks': python_blocks}

def statistics():
    """Use the handbook's verified, non-equivalent primary-row population."""
    rows = [r for r in ROWS.values() if not r.get('extension') and not r.get('equivalent_of')]
    chapters = {}
    for chapter in ('IR', 'CM', 'HW', 'LG', 'PF', 'SS', 'SP', 'EO', 'DB'):
        group = [r for r in rows if r['types']['primary'].split('-')[1] == chapter]
        chapters[chapter] = {'rows': len(group), 'marks': sum(r['marks'] for r in group),
                             'papers': len({r['paper'] for r in group})}
    calculation_types = {'P1-IR-' + n for n in ('01', '02', '03', '05', '12')}
    calculation_marks = sum(r['marks'] for r in rows if r['types']['primary'] in calculation_types)
    return {'chapters': chapters, 'marks': sum(r['marks'] for r in rows),
            'papers': len({r['paper'] for r in rows}),
            'ir_calculation_related_marks': calculation_marks,
            'ir_calculation_related_percent': round(100 * calculation_marks / chapters['IR']['marks'], 1)}

def contexts(chapter):
    paths = [ROOT / f'papers/p1/{chapter}.md'] if chapter in ('front', 'back') else [
        ROOT / f'papers/p1/cards/{chapter}.md', ROOT / f'papers/p1/core/{chapter}.md']
    refs = {rid for p in paths for rid in re.findall(REF, p.read_text())}
    for rid in sorted(refs):
        r = ROWS[rid]
        print(f'\n{rid} QP {r["qp_page"]} / MS {r["ms_page"]}; {r["marks"]} marks')
        print('QP context:', r.get('stem_ctx', ''), r['stem'])
        print('MS context:', r['ms_text'])

def validate():
    """Validate the recorded review, without marking future changed input reviewed."""
    audit = ROOT / 'papers/p1/audit'
    coverage = json.loads((audit / 'T26-coverage.json').read_text())
    findings = [json.loads(line) for line in (audit / 'T26-findings.jsonl').read_text().splitlines()]
    current = {c['card']: c for c in inspect()['cards']}
    assert len(current) == len(coverage['cards']) == 88
    assert set(current) == {c['card'] for c in coverage['cards']}
    for path, digest in coverage['source_sha256'].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, f'Changed input: {path}'
    for c in coverage['cards']:
        actual = current[c['card']]
        assert c['representative'] == actual['representative']
        for role, field in (('qp_pages', 'qp_page'), ('ms_pages', 'ms_page')):
            pages = actual[field]
            pages = pages if isinstance(pages, list) else [pages]
            assert set(pages) <= set(c[role]), (c['card'], role)
        assert not actual['pick_failures'], actual
        assert all(re.fullmatch(r'F\d{2}', f) and 1 <= int(f[1:]) <= len(findings) for f in c['findings'])
    kinds = {'quote-misuse', 'answer-not-full-marks', 'mp-alignment', 'pick-rule', 'count', 'qp-page', 'pseudocode', 'python', 'concept', 'other'}
    for f in findings:
        assert set(f) == {'file', 'line', 'card', 'kind', 'severity', 'row', 'evidence', 'suggestion'}
        assert f['card'] in current and f['row'] in ROWS
        assert f['kind'] in kinds and f['severity'] in {'error', 'warn', 'nit'}
        assert 1 <= f['line'] <= len((ROOT / f['file']).read_text().splitlines())
        assert all(token not in json.dumps(f, ensure_ascii=False) for token in ('⟦', '⟧', '「', '」'))
    assert not inspect()['python_blocks'], 'Review any new Python examples manually'
    return {'cards': len(current), 'picks': len(current) * 2, 'findings': len(findings),
            'severity': dict(Counter(f['severity'] for f in findings)), 'input_hashes': 'pass'}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--packet')
    ap.add_argument('--contexts', help='Print full corpus QP/MS contexts for every referenced row in a chapter')
    ap.add_argument('--stats', action='store_true')
    ap.add_argument('--validate', action='store_true')
    ap.add_argument('--start', type=int, default=1)
    ap.add_argument('--end', type=int, default=99)
    args = ap.parse_args()
    if args.contexts:
        contexts(args.contexts)
        return
    if args.stats or args.validate:
        print(json.dumps(validate() if args.validate else statistics(), ensure_ascii=False, indent=2))
        return
    if not args.packet:
        print(json.dumps(inspect(), ensure_ascii=False, indent=2))
        return
    for c in cards():
        if c['card'].split('-')[1] != args.packet or not args.start <= int(c['card'].split('-')[-1]) <= args.end:
            continue
        print(f'\n=== {c["file"]}:{c["line"]} ===\n{c["text"]}')
        r = ROWS[c['representative']]
        print(source(r, 'qp'))
        print(source(r, 'ms'))

if __name__ == '__main__':
    main()
