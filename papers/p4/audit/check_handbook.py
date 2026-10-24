#!/usr/bin/env python3
"""Reproduce T38 mechanical checks and build temporary original-page packets.

Rendering creates evidence for human inspection; it does not certify review.
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
REF = r'9618_[sw]\d{2}_4[123]:\d+(?:\([a-z0-9]+\))*'


def collect():
    rows = {r['id']: r for p in sorted((ROOT/'corpus/rows/p4').glob('*.jsonl'))
            for line in p.read_text().splitlines() if (r := json.loads(line))}
    cards = []
    for path in sorted((ROOT/'papers/p4/cards').glob('*.md')):
        text = path.read_text()
        headings = list(re.finditer(r'^### (P4-[A-Z]+-\d+).*', text, re.M))
        for i, heading in enumerate(headings):
            end = headings[i+1].start() if i+1 < len(headings) else len(text)
            body = text[heading.start():end]
            rep = re.search(r'#### 代表题精讲[^\n]*?('+REF+r')', body)
            var = re.search(r'\*\*下一道变式\*\*[^\n]*?('+REF+r')', body)
            cards.append(dict(card=heading[1], file=str(path.relative_to(ROOT)),
                line=text[:heading.start()].count('\n')+1, body=body,
                representative=rep[1] if rep else None, variation=var[1] if var else None))
    return rows, cards


def blocks(path):
    text = path.read_text()
    return [dict(line=text[:m.start()].count('\n')+2, code=m[1],
        complete='完整作答' in text[max(0,m.start()-220):m.start()])
        for m in re.finditer(r'^```python\n(.*?)^```', text, re.M|re.S)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=Path('/tmp/T38-evidence'))
    parser.add_argument('--render', action='store_true')
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    import pymupdf
    rows, cards = collect()
    results = dict(cards=[], picks=[], maps=[], map_columns=[], python=[], pages=[], inputs={})
    paths = sorted((ROOT/'papers/p4/cards').glob('*.md')) + sorted((ROOT/'papers/p4/core').glob('*.md'))
    paths += [ROOT/'papers/p4/front.md', ROOT/'papers/p4/back.md']
    for path in paths:
        results['inputs'][str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
        for b in blocks(path):
            entry = dict(file=str(path.relative_to(ROOT)), **{k:v for k,v in b.items() if k!='code'})
            try:
                ast.parse(b['code'])
                entry['ast'] = 'pass'
            except SyntaxError as exc:
                entry['ast'] = str(exc)
            results['python'].append(entry)
    for card in cards:
        entry = {k:v for k,v in card.items() if k!='body'}
        for role in ('representative','variation'):
            rid = card[role]
            if not rid:
                results['picks'].append(dict(card=card['card'], role=role, reason='missing; inspect D41 exception'))
                continue
            row = rows[rid]
            entry[role+'_pages'] = {k:row[k+'_page'] for k in ('qp','ms')}
            reasons = []
            if not 2022 <= row['year'] <= 2025: reasons.append('outside 2022-25')
            if row['types']['primary'] != card['card']: reasons.append('not primary')
            if row.get('equivalent_of'): reasons.append('equivalent_of='+row['equivalent_of'])
            if reasons: results['picks'].append(dict(card=card['card'],role=role,row=rid,reasons=reasons))
        if card['representative'] and card['variation'] and card['representative'].split(':')[0] == card['variation'].split(':')[0]:
            results['picks'].append(dict(card=card['card'], reason='same paper'))
        results['cards'].append(entry)
        sample = [r for r in rows.values() if r['types']['primary']==card['card'] and 2022<=r['year']<=2026
                  and r.get('markpoints') and not r.get('equivalent_of')]
        skills = lambda r: {s for mp in r.get('markpoints',[]) for s in mp['skills']}
        counts = Counter(s for r in sample for s in skills(r))
        results['maps'].append(dict(card=card['card'], rows=[r['id'] for r in sample], skills=dict(sorted(counts.items()))))
        section=card['body'].split('**得分点地图**',1)[1].split('**易错',1)[0]
        for line in section.splitlines():
            cells=[x.strip() for x in line.strip().strip('|').split('|')]
            if len(cells)<2 or not re.fullmatch(r'(?:各\s*)?\d+(?:\s*\+\s*\d+)*',cells[1]):continue
            tags=re.findall(r'`([^`]+)`',cells[0] if re.search(r'`[a-z]+-',cells[0]) else cells[-1])
            reported=[int(n) for n in re.findall(r'\d+',cells[1])]
            if len(reported)==1:reported*=len(tags)
            for tag,number in zip(tags,reported):
                members=[r['id'] for r in sample if tag in skills(r)]
                results['map_columns'].append(dict(card=card['card'],tag=tag,reported=number,
                    actual=len(members),delta=len(members)-number,rows=members))
        packet = card['body']+'\n\n=== ORIGINAL PDF PAGES ===\n'
        for rid in dict.fromkeys(re.findall(REF,card['body'])):
            row = rows[rid]
            for kind in ('qp','ms'):
                filename = re.sub(r'_(4[123])$', '_'+kind+r'_\1.pdf',row['paper'])
                with pymupdf.open(SOURCES/'pastpapers'/filename) as doc:
                    pages = row[kind+'_page']
                    if isinstance(pages,int): pages=[pages]
                    for number in pages:
                        packet += f'\n{rid} {filename} p.{number}\n'+doc[number-1].get_text(sort=True)
                        if args.render and rid==card['representative']:
                            target=args.out/'render'/f'{row["paper"]}_{kind}_{number}.png'
                            target.parent.mkdir(exist_ok=True)
                            if not target.exists(): doc[number-1].get_pixmap(matrix=pymupdf.Matrix(1.3,1.3)).save(target)
                            results['pages'].append(dict(card=card['card'],row=rid,kind=kind,page=number,image=str(target)))
        (args.out/(card['card']+'.txt')).write_text(packet)
    (args.out/'mechanical.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(cards=len(cards),picks=results['picks'],python=len(results['python']),
        complete=sum(b['complete'] for b in results['python']),ast_failures=[b for b in results['python'] if b['ast']!='pass'],
        rendered=len(set(p['image'] for p in results['pages'])),map_columns=len(results['map_columns']),
        map_deltas=[m for m in results['map_columns'] if m['delta']]),ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
