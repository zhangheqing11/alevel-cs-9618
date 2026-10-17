"""Expand independently recorded, source-order type decisions; never reads pilot."""
import json,re
from copy import deepcopy
from workbench import HERE,rows,duplicates

def compile_tags():
 data=rows();dups=duplicates(data);tags={}
 manual=json.loads((HERE/'manual_types.json').read_text())
 overrides=json.loads((HERE/'manual_notes.json').read_text()) if (HERE/'manual_notes.json').exists() else {}
 for paper,sequence in manual.items():
  rr=[r for rid,r in data.items() if r['paper']==paper and rid not in dups]
  codes=sequence.split()
  assert len(rr)==len(codes),(paper,len(rr),len(codes))
  for row,code in zip(rr,codes):
   codes=['P3-'+re.sub(r'(\D+)(\d+)',r'\1-\2',c) for c in code.split('+')]
   tags[row['id']]={'id':row['id'],'primary':codes[0],'cross':codes[1:],'confidence':'high','note':'按产出、MS 主要得分点与指南 §7 判定。'}
   tags[row['id']].update(overrides.get(row['id'],{}))
 def resolve(rid,trail=()):
  if rid in tags:return tags[rid]
  assert rid in dups and rid not in trail,('unresolved',rid)
  t=deepcopy(resolve(dups[rid],trail+(rid,)));t['id']=rid;tags[rid]=t;return t
 for rid in data:resolve(rid)
 return [tags[rid] for rid in data]
if __name__=='__main__':
 tags=compile_tags()
 (HERE/'p3_tags.jsonl').write_text(''.join(json.dumps(t,ensure_ascii=False)+'\n' for t in tags))
 print(len(tags),'tags')
