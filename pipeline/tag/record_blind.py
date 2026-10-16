"""Record manually reviewed decisions in printed row order (no pilot input)."""
from pathlib import Path
import argparse,json,re
ROOT=Path(__file__).resolve().parents[2]
def record(paper,labels,notes=None):
    source=ROOT/'pipeline/tag/p1_tags.jsonl'
    existing=[json.loads(l) for l in source.read_text().splitlines()] if source.exists() else []
    if any(r['id'].startswith(paper+':') for r in existing):raise ValueError('paper already recorded')
    rows=[json.loads(l) for l in (ROOT/'corpus/rows/p1'/f'{paper}.jsonl').read_text().splitlines()]
    valid={t['code'] for t in json.loads((ROOT/'papers/p1/taxonomy.json').read_text())['types']}
    tokens=labels.split();assert len(tokens)==len(rows),(len(tokens),len(rows))
    notes=notes or {}
    for row,token in zip(rows,tokens):
        confidence='low' if token.endswith('?') else 'high'
        parts=token.rstrip('?').split('+');codes=['P1-'+p for p in parts]
        assert set(codes)<=valid and len(codes)<=3 and len(set(codes))==len(codes),token
        note=notes.get(row['q'],'')
        assert confidence!='low' or note,(row['id'],'low needs reason')
        existing.append(dict(id=row['id'],primary=codes[0],cross=codes[1:],confidence=confidence,note=note))
    source.write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in existing))
    print(paper,'recorded',len(rows),'total',len(existing))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('paper');p.add_argument('labels');p.add_argument('--notes',default='{}');a=p.parse_args();record(a.paper,a.labels,json.loads(a.notes))
