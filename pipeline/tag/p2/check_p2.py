from pathlib import Path
import argparse,json,re,subprocess
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
norm=lambda text:re.sub(r'\s+',' ',text).strip()
def records(path):return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
def unique(path):
 result={}
 for row in records(path):
  assert row['id'] not in result,('duplicate annotation',row['id'])
  result[row['id']]=row
 return result

def main():
 parser=argparse.ArgumentParser(description='Check independent P2 annotation sources without reading pilot data.')
 parser.add_argument('--partial',action='store_true')
 args=parser.parse_args()
 rows={r['id']:r for path in (ROOT/'corpus/rows/p2').glob('*.jsonl') for r in records(path)}
 tags=unique(HERE/'p2_tags.jsonl');points=unique(HERE/'p2_markpoints.jsonl')
 types={t['code'] for t in json.loads((ROOT/'papers/p2/taxonomy.json').read_text())['types']}
 skills={t['tag'] for t in json.loads((ROOT/'papers/p2/skill_tags.json').read_text())['tags']}
 assert set(tags)<=set(rows) and set(points)<=set(tags)
 if not args.partial:assert set(tags)==set(rows),('missing labels',set(rows)-set(tags))
 for rid,tag in tags.items():
  assert set(tag)=={'id','primary','cross','confidence','note'},rid
  assert tag['primary'] in types and all(t in types for t in tag['cross']),rid
  assert len(set(tag['cross']))==len(tag['cross'])<=2 and tag['primary'] not in tag['cross'],rid
  assert tag['confidence'] in {'high','low'} and (tag['confidence']!='low' or tag['note']),rid
 for rid,record in points.items():
  assert set(record)=={'id','ms_max','markpoints'},rid
  assert rows[rid]['marks']>=4,rid
  total=0
  for n,point in enumerate(record['markpoints'],1):
   assert set(point)=={'n','text','marks','skills'} and point['n']==n,rid
   assert point['text'] and norm(point['text']) in norm(rows[rid]['ms_text']),(rid,point['text'])
   assert type(point['marks']) is int and point['marks']>=1,rid
   assert 1<=len(point['skills'])<=3 and len(set(point['skills']))==len(point['skills']),rid
   assert set(point['skills'])<=skills,(rid,point['skills'])
   forbidden={'translate-pseudocode','class-definition','encapsulation','getter-setter','inheritance','polymorphism','containment','exception-handling','p4-identifiers'}
   assert not set(point['skills'])&forbidden,rid
   total+=point['marks']
  cap=record['ms_max']
  assert (cap is None and total==rows[rid]['marks']) or (cap==rows[rid]['marks'] and total>=cap),(rid,total,cap,rows[rid]['marks'])
 for rid,row in rows.items():
  parent=row.get('equivalent_of')
  if row['paper'] in {'9618_s21_23','9618_w21_23'}:parent=row['paper'][:-2]+'21:'+row['q']
  if parent and rid in tags and parent in tags:
   assert {k:v for k,v in tags[rid].items() if k!='id'}=={k:v for k,v in tags[parent].items() if k!='id'},rid
   assert (rid in points)==(parent in points),rid
   if rid in points:assert {k:v for k,v in points[rid].items() if k!='id'}=={k:v for k,v in points[parent].items() if k!='id'},rid
 print(f'{len(tags)}/{len(rows)} tags; {len(points)} split rows; {sum(len(p["markpoints"]) for p in points.values())} points; {sum(t["confidence"]=="low" for t in tags.values())} low; validation passed')
if __name__=='__main__':main()
