"""Render source pages via rows.py and assemble four-page review sheets in /tmp."""
import argparse,json,subprocess,sys
from pathlib import Path
import pymupdf
from workbench import ROOT,HERE,rows,duplicates,records

def main():
 parser=argparse.ArgumentParser();parser.add_argument('papers',nargs='*');parser.add_argument('--ms',action='store_true');args=parser.parse_args()
 data=rows();dups=duplicates(data);kind='ms' if args.ms else 'qp'
 tags={r['id']:r for r in records(HERE/'p3_tags.jsonl')}
 target=Path('/tmp/t31-render');target.mkdir(exist_ok=True)
 selected={}
 for rid,r in data.items():
  if rid in dups:continue
  if args.papers and r['paper'] not in args.papers:continue
  if args.ms:
   needed=tags[rid]['primary'].startswith('P3-BL-') or (r['marks']>=4 and tags[rid]['primary'][3:] in {'DR-03','DR-05','CT-02','CT-03','CT-06','CT-07','CT-08','CT-09','FP-05','FP-06','FP-10'})
  else:needed=r['has_figure'] or (r['marks']>=4 and tags[rid]['primary']=='P3-CT-09')
  if needed:selected.setdefault(r['paper'],{}).setdefault(r[kind+'_page'],rid)
 log=[]
 for paper,pages in selected.items():
  paths=[]
  for page,rid in sorted(pages.items()):
   cmd=[sys.executable,str(ROOT/'skill/cie-9618-cs-tutor/scripts/rows.py'),'render',rid,'--dpi','110','--out',str(target)]
   if args.ms:cmd.append('--ms')
   paths.append((page,Path(subprocess.check_output(cmd,cwd=ROOT,text=True).strip())))
  for batch in range(0,len(paths),4):
   sheet=pymupdf.open();canvas=sheet.new_page(width=1200,height=1740)
   for k,(page,path) in enumerate(paths[batch:batch+4]):
    x=k%2*600;y=k//2*870
    canvas.insert_text((x+4,y+14),f'{paper} {kind.upper()} p.{page}',fontsize=10)
    canvas.insert_image(pymupdf.Rect(x,y+22,x+595,y+864),filename=str(path))
   path=target/f'{paper}-{kind}-{batch//4}.png';canvas.get_pixmap(alpha=False).save(path);print(path)
  log.append({'paper':paper,'kind':kind,'pages':sorted(pages),'status':'rendered, pending visual inspection'})
 (HERE/f'render_manifest_{kind}.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
