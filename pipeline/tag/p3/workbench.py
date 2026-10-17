"""Read P3 source rows and track guide-mandated duplicate inheritance (no pilot input)."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
norm=lambda s:' '.join(s.split())
def records(p):return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
def rows():return {r['id']:r for p in sorted((ROOT/'corpus/rows/p3').glob('*.jsonl')) for r in records(p)}
def duplicates(data):
 result={}
 for rid,r in data.items():
  base=r['paper'][:-1]+'1:'+r['q']
  if r['equivalent_of']:result[rid]=r['equivalent_of']
  elif base!=rid and base in data and all(norm(r[k])==norm(data[base][k]) for k in ('stem','ms_text')):result[rid]=base
 return result
if __name__=='__main__':
 import sys
 data=rows();dups=duplicates(data)
 for rid,r in data.items():
  if rid in dups or not any(s in r['paper'] for s in sys.argv[1:]):continue
  print('\n'+rid+' ['+str(r['marks'])+(' FIG' if r['has_figure'] else '')+']')
  print(__import__('re').sub(r'\.{3,}', '',norm(r['stem']))[:650])
  print('CTX:',norm(r['stem_ctx'])[:160])
  print('MS:',norm(r['ms_text'])[:int(__import__('os').environ.get('MS_LIMIT','300'))])
