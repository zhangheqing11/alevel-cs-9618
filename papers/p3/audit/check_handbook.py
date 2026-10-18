#!/usr/bin/env python3
"""T36 mechanical audit of the P3 handbook (read-only; never edits cards).

Run with the shared environment from the repo root:
  ~/.venvs/alevel-cs/bin/python papers/p3/audit/check_handbook.py            # all mechanical checks (JSON)
  ~/.venvs/alevel-cs/bin/python papers/p3/audit/check_handbook.py --stats    # chapter shares quoted in front.md
  ~/.venvs/alevel-cs/bin/python papers/p3/audit/check_handbook.py --packet DR [--start 1 --end 4]
        print each card followed by the full QP / MS page text of its representative row
  ~/.venvs/alevel-cs/bin/python papers/p3/audit/check_handbook.py --quotes DR
        every MS quote in a chapter's card + core file with the quoted row's primary type
  ~/.venvs/alevel-cs/bin/python papers/p3/audit/check_handbook.py --render <row id> [--ms]
        render the source page(s) to $TMPDIR/t36 for visual checks
  ~/.venvs/alevel-cs/bin/python papers/p3/audit/check_handbook.py --validate
        check the findings file and coverage file are well formed and still match the inputs

Packets and renders are review aids; they are not a verdict. Findings are written by hand.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter, defaultdict
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile

ROOT = Path(__file__).resolve().parents[3]
AUDIT = ROOT / 'papers/p3/audit'
SOURCES = Path(os.environ.get('ALEVEL_CS_SOURCES', '/Users/zhangheqing/Desktop/alevel cs/sources'))
ROWS = {}
for _p in sorted((ROOT / 'corpus/rows/p3').glob('*.jsonl')):
    for _line in _p.read_text().splitlines():
        if _line.strip():
            _r = json.loads(_line)
            ROWS[_r['id']] = _r
REF = r'⟦([^⟧]+)⟧'
CHAPTERS = ('DR', 'CI', 'HV', 'BL', 'SY', 'SC', 'AI', 'CT', 'FP')

# D41 (1): accepted substitutions when no 2022-25 / different-paper / non-s26 second question exists.
D41_EXCEPTIONS = {
    ('P3-SY-05', 'variation'): 'extension',
    ('P3-AI-04', 'variation'): 'extension',
    ('P3-AI-07', 'variation'): 'extension',
    ('P3-CT-03', 'variation'): 'extension',
    ('P3-FP-01', 'representative'): 'extension',
    ('P3-FP-01', 'variation'): 'extension',
    ('P3-CT-08', 'variation'): 'same-paper',
    ('P3-HV-04', 'variation'): 'none',
    ('P3-BL-02', 'variation'): 'none',
    ('P3-BL-03', 'variation'): 'none',
}


def cards():
    for chapter in CHAPTERS:
        p = ROOT / f'papers/p3/cards/{chapter}.md'
        text = p.read_text()
        matches = list(re.finditer(r'^### (P3-[A-Z]+-\d+)\s+.*$', text, re.M))
        for i, m in enumerate(matches):
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            section = text[m.start():end]
            cut = section.find('### 本章易混辨析')
            if cut > 0:
                section = section[:cut]
            rep = re.search(r'#### 代表题精讲\s+' + REF, section)
            var = re.search(r'\*\*下一道变式\*\*\s+' + REF, section)
            yield {'card': m[1], 'chapter': chapter, 'file': str(p.relative_to(ROOT)),
                   'line': text[:m.start()].count('\n') + 1, 'text': section,
                   'representative': rep[1] if rep else None,
                   'variation': var[1] if var else None}


def pdf_path(row, kind):
    s, y, v = row['paper'].split('_')[1][0], row['paper'].split('_')[1][1:], row['paper'].split('_')[2]
    return SOURCES / 'pastpapers' / f'9618_{s}{y}_{kind}_{v}.pdf'


def pages_of(row, kind):
    page = row[f'{kind}_page']
    return page if isinstance(page, list) else [page]


def source_text(row, kind):
    import pymupdf
    path = pdf_path(row, kind)
    with pymupdf.open(path) as pdf:
        return '\n'.join(f'--- {path.name} p.{n} ---\n' + pdf[n - 1].get_text() for n in pages_of(row, kind))


def pick_check(c):
    failures = []
    for role in ('representative', 'variation'):
        rid = c[role]
        exc = D41_EXCEPTIONS.get((c['card'], role))
        if rid is None:
            if exc != 'none':
                failures.append(f'{role}: missing')
            continue
        if rid not in ROWS:
            failures.append(f'{role}: unknown row {rid}')
            continue
        r = ROWS[rid]
        if r['year'] == 2026:
            failures.append(f'{role}: s26 row (D1)')
        if r.get('equivalent_of'):
            failures.append(f'{role}: equivalent_of {r["equivalent_of"]}')
        if r['types']['primary'] != c['card']:
            failures.append(f'{role}: primary is {r["types"]["primary"]}')
        if r.get('extension') or not 2022 <= r['year'] <= 2025:
            if exc != 'extension':
                failures.append(f'{role}: year {r["year"]} / extension without D41 exception')
        elif exc == 'extension':
            failures.append(f'{role}: D41 says extension but row is {r["year"]}')
    rep, var = c['representative'], c['variation']
    if rep in ROWS and var in ROWS and ROWS[rep]['paper'] == ROWS[var]['paper']:
        if D41_EXCEPTIONS.get((c['card'], 'variation')) != 'same-paper':
            failures.append('representative and variation on the same paper')
    if D41_EXCEPTIONS.get((c['card'], 'variation')) == 'none' and var is not None:
        failures.append('D41 says no second question but a variation is given')
    return failures


def page_mentions(c):
    """Every 'QP p.N' mention in the card with the pages the representative row lives on."""
    out = []
    for m in re.finditer(r'QP\s*p\.?\s*(\d+)', c['text']):
        line = c['line'] + c['text'][:m.start()].count('\n')
        ctx = c['text'][max(0, m.start() - 120):m.end() + 40].replace('\n', ' ')
        ids = re.findall(REF, c['text'][max(0, m.start() - 300):m.end() + 300])
        out.append({'line': line, 'page': int(m[1]), 'rep_pages': pages_of(ROWS[c['representative']], 'qp') if c['representative'] in ROWS else None,
                    'nearby_rows': {i: pages_of(ROWS[i], 'qp') for i in ids if i in ROWS}, 'context': ctx})
    return out


FORBIDDEN = [
    (r'\bdef\b', 'Python def'), (r'\blen\(', 'len()'), (r'\w\[[^\]]*:[^\]]*\]\s*(?!OF)', 'slice-like subscript'),
    (r'\bFOR\s+\w+\s+IN\b', 'FOR x IN'), (r'\bELSIF\b|\bELSEIF\b|\bELIF\b', 'ELSIF'), (r'!=|==', '!= / =='),
    (r'\+=|-=', 'augmented assignment'), (r'\bEND (IF|WHILE|TYPE|CLASS|FUNCTION|PROCEDURE|CASE)\b', 'END X with space'),
    (r'\bNULL\b', 'NULL keyword'), (r'\bprint\(|\binput\(', 'Python I/O'), (r'(?<![<>=])=(?!=)', 'bare = (check: assignment?)'),
    (r'\bTHEN\b', None),
]


def pseudocode_lint(path):
    issues = []
    text = path.read_text()
    for m in re.finditer(r'^```pseudocode\n(.*?)^```', text, re.M | re.S):
        start = text[:m.start()].count('\n') + 2
        body = m[1]
        for k, line in enumerate(body.splitlines()):
            code = line.split('//')[0]
            if re.match(r'\s*(TYPE|DEFINE|CONSTANT)\b', code):
                code_eq = ''
            else:
                code_eq = code
            for pat, label in FORBIDDEN:
                if label is None:
                    continue
                target = code_eq if label.startswith('bare =') else code
                if label == 'slice-like subscript' and re.search(r'ARRAY\[', code):
                    continue
                if re.search(pat, target):
                    if label.startswith('bare =') and re.search(r'\b(IF|WHILE|UNTIL|CASE|RETURN|OUTPUT|AND|OR)\b|<-|←', code):
                        continue
                    issues.append({'file': str(path.relative_to(ROOT)), 'line': start + k, 'issue': label, 'code': line.strip()})
            # AND with a guard on the left that the right side depends on (D25 short-circuit)
            if re.search(r'\b(\w+)\s*<>\s*(-1|0|NullPointer|NULLPOINTER|Null\w*)\s+AND\b.*\[\s*\1\s*\]', code):
                issues.append({'file': str(path.relative_to(ROOT)), 'line': start + k, 'issue': 'AND short-circuit dependency (D25)', 'code': line.strip()})
            if re.search(r'\bAND\b.*\[\s*\w+\s*\]', code) and re.search(r'(<>|<=|>=|<|>)\s*(-1|0|NullPointer|\w*Max\w*|\w*Size\w*|\w*Top\w*)\s+AND', code):
                issues.append({'file': str(path.relative_to(ROOT)), 'line': start + k, 'issue': 'possible AND guard (D25) - review', 'code': line.strip()})
        # block balance
        opens = Counter()
        for word, end in (('IF', 'ENDIF'), ('WHILE', 'ENDWHILE'), ('FOR', 'NEXT'), ('REPEAT', 'UNTIL'), ('CASE', 'ENDCASE'),
                          ('PROCEDURE', 'ENDPROCEDURE'), ('FUNCTION', 'ENDFUNCTION'), ('CLASS', 'ENDCLASS'), ('TYPE', 'ENDTYPE')):
            code_only = '\n'.join(l.split('//')[0] for l in body.splitlines())
            if word == 'TYPE':
                n_open = len(re.findall(r'^\s*TYPE\s+\w+\s*$', code_only, re.M))
            elif word == 'IF':
                n_open = len(re.findall(r'(?<!END)\bIF\b', code_only))
            elif word == 'CASE':
                n_open = len(re.findall(r'(?<!END)\bCASE OF\b', code_only))
            elif word in ('PROCEDURE', 'FUNCTION', 'CLASS', 'WHILE'):
                n_open = len(re.findall(r'^\s*(?:PUBLIC\s+|PRIVATE\s+)?' + word + r'\b', code_only, re.M))
            elif word == 'FOR':
                n_open = len(re.findall(r'^\s*FOR\b', code_only, re.M))
            else:
                n_open = len(re.findall(r'(?<!END)\b' + word + r'\b', code_only))
            n_end = len(re.findall(r'\b' + end + r'\b', code_only))
            if n_open != n_end:
                issues.append({'file': str(path.relative_to(ROOT)), 'line': start, 'issue': f'{word}/{end} count {n_open}/{n_end} (fragment?)', 'code': ''})
    return issues


def python_blocks():
    out = []
    for p in sorted((ROOT / 'papers/p3').glob('**/*.md')):
        if 'audit' in p.parts:
            continue
        text = p.read_text()
        for m in re.finditer(r'^```python\n(.*?)^```', text, re.M | re.S):
            line = text[:m.start()].count('\n') + 1
            try:
                ast.parse(m[1])
                err = None
            except SyntaxError as e:
                err = str(e)
            out.append({'file': str(p.relative_to(ROOT)), 'line': line, 'ast_error': err})
    return out


def handwritten_counts(c):
    """Numbers like 'MS 九点 Max 4' / '4 分' near the representative heading, for manual comparison."""
    r = ROWS.get(c['representative'])
    if not r:
        return None
    sect = c['text'].split('#### 代表题精讲', 1)[-1][:1500]
    marks = re.findall(r'(\d+)\s*分', sect)
    maxes = re.findall(r'Max\s*(\d+)', sect)
    ms_max = re.findall(r'[Mm]ax\s*(\d+)', r['ms_text'])
    return {'row_marks': r['marks'], 'card_marks_mentions': marks[:6], 'card_max_mentions': maxes[:6], 'ms_max_mentions': ms_max}


def inspect():
    out = []
    for c in cards():
        out.append({k: c[k] for k in ('card', 'file', 'line', 'representative', 'variation')}
                   | {'rep_pages': {'qp': pages_of(ROWS[c['representative']], 'qp'), 'ms': pages_of(ROWS[c['representative']], 'ms')} if c['representative'] in ROWS else None,
                      'var_pages': {'qp': pages_of(ROWS[c['variation']], 'qp'), 'ms': pages_of(ROWS[c['variation']], 'ms')} if c['variation'] in ROWS else None,
                      'pick_failures': pick_check(c), 'page_mentions': page_mentions(c), 'counts': handwritten_counts(c)})
    lint = []
    for p in sorted((ROOT / 'papers/p3').glob('**/*.md')):
        if 'audit' not in p.parts:
            lint += pseudocode_lint(p)
    return {'cards': out, 'n_cards': len(out), 'python_blocks': python_blocks(), 'pseudocode_lint': lint}


def statistics():
    rows = [r for r in ROWS.values() if not r.get('extension') and not r.get('equivalent_of')]
    total = sum(r['marks'] for r in rows)
    chapters = {}
    for ch in CHAPTERS:
        g = [r for r in rows if r['types']['primary'].split('-')[1] == ch]
        chapters[ch] = {'rows': len(g), 'marks': sum(r['marks'] for r in g), 'share_%': round(100 * sum(r['marks'] for r in g) / total, 1),
                        'papers': len({r['paper'] for r in g})}
    per_type = Counter()
    for r in rows:
        per_type[r['types']['primary']] += 1
    return {'total_marks': total, 'papers': len({r['paper'] for r in rows}), 'chapters': chapters,
            'top4_share_%': round(sum(chapters[c]['share_%'] for c in ('DR', 'SY', 'FP', 'CT')), 1)}


def markpoint_map(card):
    """Recompute the '得分点地图' table: per skill, number of distinct rows (verified 2022-26, primary = card, not equivalent)."""
    rows = [r for r in ROWS.values() if r['types']['primary'] == card and r.get('markpoints')
            and not r.get('equivalent_of') and not r.get('extension')]
    cnt = Counter()
    for r in rows:
        cnt.update({s for mp in r['markpoints'] for s in mp.get('skills', [])})
    return {'rows': sorted(r['id'] for r in rows), 'skills': dict(cnt.most_common())}


def quotes(chapter):
    paths = [ROOT / f'papers/p3/{chapter}.md'] if chapter in ('front', 'back') else [
        ROOT / f'papers/p3/cards/{chapter}.md', ROOT / f'papers/p3/core/{chapter}.md']
    for p in paths:
        text = p.read_text()
        for m in re.finditer(r'「([^」]+)」' + REF, text):
            line = text[:m.start()].count('\n') + 1
            r = ROWS.get(m[2], {})
            print(f'{p.name}:{line}\t{m[2]}\t[{r.get("types", {}).get("primary")}] {m[1]}')


def render(rid, ms=False, dpi=110):
    import pymupdf
    r = ROWS[rid]
    kind = 'ms' if ms else 'qp'
    out = Path(os.environ.get('T36_RENDER', Path(tempfile.gettempdir()) / 't36'))
    out.mkdir(parents=True, exist_ok=True)
    files = []
    with pymupdf.open(pdf_path(r, kind)) as pdf:
        for n in pages_of(r, kind):
            f = out / f'{r["paper"]}_{kind}_p{n}.png'
            pdf[n - 1].get_pixmap(dpi=dpi).save(f)
            files.append(str(f))
    return files


def input_hashes():
    paths = [ROOT / 'papers/p3/front.md', ROOT / 'papers/p3/back.md']
    paths += sorted((ROOT / 'papers/p3/cards').glob('*.md')) + sorted((ROOT / 'papers/p3/core').glob('*.md'))
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}


KINDS = {'quote-misuse', 'answer-not-full-marks', 'mp-alignment', 'pick-rule', 'count', 'qp-page', 'pseudocode',
         'python', 'concept', 'other', 'symbol-lost', 'algorithm-trace', 'assembly-prolog'}


def validate():
    findings = [json.loads(l) for l in (AUDIT / 'T36-findings.jsonl').read_text().splitlines() if l.strip()]
    coverage = json.loads((AUDIT / 'T36-coverage.json').read_text())
    current = {c['card']: c for c in cards()}
    assert len(current) == 79, len(current)
    assert {c['card'] for c in coverage['cards']} == set(current)
    for path, digest in coverage['source_sha256'].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, f'Changed input since audit: {path}'
    for c in coverage['cards']:
        cur = current[c['card']]
        assert c['representative'] == cur['representative'], c['card']
        assert set(pages_of(ROWS[cur['representative']], 'qp')) <= set(c['qp_pages']), (c['card'], 'qp')
        assert set(pages_of(ROWS[cur['representative']], 'ms')) <= set(c['ms_pages']), (c['card'], 'ms')
    for f in findings:
        assert set(f) == {'file', 'line', 'card', 'kind', 'severity', 'row', 'evidence', 'suggestion'}, f
        assert f['card'] in current or f['card'] in ('front', 'back') or f['card'].startswith('core/'), f['card']
        assert f['row'] in ROWS or f['row'] == '', f['row']
        assert f['kind'] in KINDS and f['severity'] in {'error', 'warn', 'nit'}, f
        assert 1 <= f['line'] <= len((ROOT / f['file']).read_text().splitlines()), f
        assert not any(t in json.dumps(f, ensure_ascii=False) for t in ('⟦', '⟧', '「', '」')), f
    return {'cards': len(current), 'findings': len(findings),
            'severity': dict(Counter(f['severity'] for f in findings)),
            'kind': dict(Counter(f['kind'] for f in findings)), 'input_hashes': 'match'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--packet')
    ap.add_argument('--start', type=int, default=1)
    ap.add_argument('--end', type=int, default=99)
    ap.add_argument('--var', action='store_true', help='with --packet: also print the variation row pages')
    ap.add_argument('--quotes')
    ap.add_argument('--render')
    ap.add_argument('--ms', action='store_true')
    ap.add_argument('--dpi', type=int, default=110)
    ap.add_argument('--stats', action='store_true')
    ap.add_argument('--map')
    ap.add_argument('--hashes', action='store_true')
    ap.add_argument('--validate', action='store_true')
    ap.add_argument('--rows', nargs='+', help='print corpus fields (stem, MS, ER, types) of these rows')
    a = ap.parse_args()
    if a.rows:
        for rid in a.rows:
            r = ROWS[rid]
            print(f'===== {rid} marks {r["marks"]} qp {r["qp_page"]} ms {r["ms_page"]} {r["types"]} eq={r.get("equivalent_of")}')
            print('CTX:', (r.get('stem_ctx') or '')[:600])
            print('STEM:', re.sub(r'\.{6,}', '…', r['stem'])[:1200])
            print('MS:', r['ms_text'])
            print('ER:', r.get('er') or '')
    elif a.render:
        print('\n'.join(render(a.render, a.ms, a.dpi)))
    elif a.quotes:
        quotes(a.quotes)
    elif a.stats:
        print(json.dumps(statistics(), ensure_ascii=False, indent=2))
    elif a.map:
        print(json.dumps(markpoint_map(a.map), ensure_ascii=False, indent=2))
    elif a.hashes:
        print(json.dumps(input_hashes(), indent=2))
    elif a.validate:
        print(json.dumps(validate(), ensure_ascii=False, indent=2))
    elif a.packet:
        for c in cards():
            if c['chapter'] != a.packet or not a.start <= int(c['card'][-2:]) <= a.end:
                continue
            print(f'\n=== {c["card"]} {c["file"]}:{c["line"]} rep {c["representative"]} var {c["variation"]} ===')
            for role in ('representative',) + (('variation',) if a.var else ()):
                if c[role] in ROWS:
                    r = ROWS[c[role]]
                    print(f'## {role} {r["id"]} marks {r["marks"]} qp {r["qp_page"]} ms {r["ms_page"]}')
                    print(source_text(r, 'qp'))
                    print(source_text(r, 'ms'))
    else:
        print(json.dumps(inspect(), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
