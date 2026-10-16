"""Print source evidence for manual blind tagging; never read pilot labels."""
from pathlib import Path
import argparse,json,re,sys
ROOT=Path(__file__).resolve().parents[2]
def clean(text):
    return re.sub(r'\s+',' ',re.sub(r'\.{3,}',' ',text)).strip()
def main():
    p=argparse.ArgumentParser();p.add_argument('paper');p.add_argument('--full',action='store_true');args=p.parse_args()
    rows=[json.loads(l) for l in (ROOT/'corpus/rows/p1'/f'{args.paper}.jsonl').read_text().splitlines()]
    for i,r in enumerate(rows,1):
        print(f"{i:02} {r['q']} [{r['marks']}] {'FIG' if r['has_figure'] else ''} QP{r['qp_page']} MS{r['ms_page']} equiv={r['equivalent_of']}")
        for name,limit in [('stem',380),('stem_ctx',110),('ms_text',290)]:
            text=clean(r[name]);print(name+':',text if args.full else text[:limit])
if __name__=='__main__':main()
