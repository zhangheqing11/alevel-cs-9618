from pathlib import Path
import re,json
R=Path(__file__).resolve().parents[3]
D=R/'pipeline/tag/p2'
norm=lambda s:re.sub(r'\s+',' ',s).strip()
def rows(paper):return [json.loads(s) for s in (R/f'corpus/rows/p2/{paper}.jsonl').read_text().splitlines()]
def numbered(row):
 lines=row['ms_text'].splitlines();heads=[]
 for i,line in enumerate(lines):
  match=re.match(r'^\s*(?:MP\s*)?(\d{1,2})[.)]?\s+(.+)',line)
  if match and not re.match(r'marks?\b',match[2],re.I):heads.append((i,int(match[1]),match[2]))
 candidates=[]
 for pos,(i,n,body) in enumerate(heads):
  if n!=1:continue
  run=[(i,n,body)]
  for h in heads[pos+1:]:
   if h[1]==run[-1][1]+1:run.append(h)
   elif h[1]==1:break
  if len(run)>=2:candidates.append(run)
 if not candidates:return []
 run=candidates[0]; result=[]
 for k,(i,n,body) in enumerate(run):
  end=run[k+1][0] if k+1<len(run) else len(lines)
  content=[body]
  for line in lines[i+1:end]:
   if re.match(r'^\s*(?:(?-i:PROCEDURE|FUNCTION)\b|Note\b|Max\b|Example\b|Alternative\b|VARIATION\b|Mark Scheme\b|Solution (?:Two|Three|Four)\b|The [‘\x27]|Mark as|Marks? awarded|One mark|1 mark)',line,re.I):break
   content.append(line)
  result.append(norm(' '.join(content)))
 return result

def code(c):return f'P2-{c[:2]}-{int(c[2:]):02}' if not c.startswith('P2-') else c

def read_source(name):
 path=D/name
 return {r['id']:r for r in map(json.loads,path.read_text().splitlines())} if path.exists() else {}

def write_source(name,records):
 (D/name).write_text(''.join(json.dumps(records[k],ensure_ascii=False)+'\n' for k in sorted(records)),encoding='utf-8')

def annotate(paper,labels,skills,cross=None,notes=None,manual=None):
 rr=rows(paper);labels=labels.split();assert len(rr)==len(labels),(paper,len(rr),len(labels))
 tags=read_source('p2_tags.jsonl');points=read_source('p2_markpoints.jsonl')
 for row,label in zip(rr,labels):
  rid=row['id'];q=row['q'];cs=(cross or {}).get(q,[])
  tags[rid]={'id':rid,'primary':code(label),'cross':[code(c) for c in cs],'confidence':'high','note':(notes or {}).get(q,'按题干产出及指南 §2、§7 定主题型；副题型按 §4 阈值。')}
  if q in skills:
   texts=(manual or {}).get(q,numbered(row));sk=skills[q].split(';')
   assert len(texts)==len(sk),(rid,texts,sk)
   mps=[]
   for n,(text,ss) in enumerate(zip(texts,sk),1):
    assert norm(text) in norm(row['ms_text']),(rid,text)
    mps.append({'n':n,'text':text,'marks':1,'skills':ss.split(',')})
   cap=None
   m=re.search(r'(?:Note:\s*)?Max\s*(\d+)',row['ms_text'],re.I)
   if len(mps)>row['marks']:cap=int(m[1]) if m else row['marks']
   assert len(mps)>=row['marks'],(rid,len(mps),row['marks'])
   points[rid]={'id':rid,'ms_max':cap,'markpoints':mps}
 write_source('p2_tags.jsonl',tags);write_source('p2_markpoints.jsonl',points)
 print(paper,len(rr),'labels',len(skills),'splits')
 for row in rr:
  if row['q'] in skills:
   print(row['q'],points[row['id']])
