import pymupdf,json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[3]
S=Path('/Users/zhangheqing/Desktop/alevel cs/sources/pastpapers')
paper=sys.argv[1]
rows=[json.loads(x) for x in (R/f'corpus/rows/p2/{paper}.jsonl').read_text().splitlines()]
pages=sorted({r['qp_page'] for r in rows if r['has_figure']})
session,variant=paper.removeprefix('9618_').split('_')
doc=pymupdf.open(S/f'9618_{session}_qp_{variant}.pdf')
for batch in range(0,len(pages),4):
 sheet=pymupdf.open();canvas=sheet.new_page(width=1200,height=1740)
 for k,page in enumerate(pages[batch:batch+4]):
  x=(k%2)*600;y=(k//2)*870
  canvas.insert_text((x+4,y+14),f'{paper} QP p.{page}',fontsize=10)
  canvas.show_pdf_page(pymupdf.Rect(x,y+22,x+595,y+864),doc,page-1)
 path=Path(f'/private/tmp/t28-{paper}-{batch//4}.png')
 canvas.get_pixmap(alpha=False).save(path);print(path)
