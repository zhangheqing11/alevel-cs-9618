"""Build markpoints from reviewed MS checklist/blank mappings; no pilot reads."""
import json,re
from copy import deepcopy
from workbench import HERE,rows,duplicates,norm

def checklist(text,spec):
 if 'texts' in spec:return spec['texts']
 if spec.get('end'):text=text.split(spec['end'])[0]
 text=re.split(r'(?m)^\s*(?:Example|Sample|Completed|CLASS\s)',text)[0]
 
 if not spec.get('end'):text=re.split(r'(?m)^ {15,}\S',text)[0]
 if re.search(r'\bMP1\b',text):
  result=re.split(r'(?m)^\s*MP\d+\s+',text)[1:]
 elif '•' in text:result=text.split('•')[1:]
 else:result=re.findall(r'(?ms)(?:^|\n)\s*(One mark for .*?)(?=\n\s*One mark for|\Z)',text)
 return [norm(s) for s in result]

def compile_points():
 data=rows();specs=json.loads((HERE/'split_spec.json').read_text());points={}
 for rid,spec in specs.items():
  if spec['kind']=='copy':continue
  text=data[rid]['ms_text']
  texts=checklist(text,spec) if spec['kind']=='A' else spec['lines']
  assert len(texts)==len(spec['skills'])==spec.get('count',len(texts)),(rid,texts)
  weights=spec.get('weights',[1]*len(texts))
  assert len(weights)==len(texts),rid
  mp=[]
  for n,(t,skills,marks) in enumerate(zip(texts,spec['skills'],weights),1):
   assert norm(t) in norm(text),(rid,t)
   mp.append({'n':n,'text':t,'marks':marks,'skills':skills})
  total=sum(weights);assert total>=data[rid]['marks'],(rid,total)
  points[rid]={'id':rid,'ms_max':data[rid]['marks'] if total>data[rid]['marks'] else None,'markpoints':mp}
 dups=duplicates(data);dups.update({rid:s['source'] for rid,s in specs.items() if s['kind']=='copy'})
 def resolve(rid,trail=()):
  if rid in points:return points[rid]
  if rid not in dups:return None
  assert rid not in trail,rid
  parent=resolve(dups[rid],trail+(rid,))
  if parent:
   t=deepcopy(parent);t['id']=rid;points[rid]=t;return t
 for rid in data:resolve(rid)
 return [points[rid] for rid in data if rid in points]
if __name__=='__main__':
 pp=compile_points();(HERE/'p3_markpoints.jsonl').write_text(''.join(json.dumps(p,ensure_ascii=False)+'\n' for p in pp));print(len(pp),'split rows;',sum(len(p['markpoints']) for p in pp),'points')
