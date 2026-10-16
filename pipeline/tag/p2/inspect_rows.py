from pathlib import Path
import json,re,sys
R=Path(__file__).resolve().parents[3]
def clean(s):
 s=re.sub(r'\.{6,}',' ',s);return re.sub(r'\s+',' ',s).strip()
for paper in sys.argv[1:]:
 rows=[json.loads(l) for l in (R/f'corpus/rows/p2/{paper}.jsonl').read_text().splitlines()]
 for r in rows:
  print(f"{r['q']} [{r['marks']}] qp{r['qp_page']}/ms{r['ms_page']} | {clean(r['stem'])}")
  print('CTX:',clean(r['stem_ctx'])[:550])
  print('MS:',clean(r['ms_text'])[:700])
