#!/usr/bin/env python3
"""Run exact complete-answer fences on copied official files and QP test data.

No handbook code is rewritten. Random examples use seed 9618, so sample
numbers need not match MS screenshots. Outputs are evidence, not verdicts.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

from check_handbook import ROOT, SOURCES, collect

# Lists are separate fresh runs. Early evidence stages are checked separately.
INPUTS = {
 'P4-PR-01': [[30,5,3,9,4,1,2,2],[5,1,6,2,8,10,2],[5,1,6,2,8,10,7]],
 'P4-SR-02': [[30,5,3,9,4,1,2,2],[5,1,6,2,8,10,2],[5,1,6,2,8,10,7]],
 'P4-AR-01': [[11],[100],[101]], 'P4-SR-03': [[11],[100],[101]],
 'P4-AR-03': [[10,9,-1,8,7,6,5,4,3,2,1],[10,9,8,7,6,5,4,3,2,1]],
 'P4-AR-05': [['TheData.txt']], 'P4-FL-01': [['TheData.txt']], 'P4-FL-03': [['TheData.txt']],
 'P4-FL-02': [['keep',400,200,'Blue Conifer',100]],
 'P4-LT-01': [[5,1,2,3,8],[5,6,8,9,5],[10,7,8,5,6]],
 'P4-SQ-01': [list(range(11,22))], 'P4-MP-02': [list(range(11,22))],
 'P4-SR-01': [[12]],
 'P4-SQ-03': [['ADF',10,'OOP',1,'BXW',5,'XXZ',22,'HQR',6,'LLP',3,'LLP',3]],
 'P4-MP-01': [['ADF',10,'OOP',1,'BXW',5,'XXZ',22,'HQR',6,'LLP',3,'LLP',3]],
}


def complete_blocks():
    rows, cards=collect()
    answer=[]
    for c in cards:
        for m in re.finditer(r'^```python\n(.*?)^```',c['body'],re.M|re.S):
            if '完整作答' in c['body'][max(0,m.start()-220):m.start()]:
                answer.append((c,m[1],rows[c['representative']]['paper']))
    return answer


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--chapter')
    parser.add_argument('--out',type=Path,default=Path('/tmp/T38-evidence/runs.json'))
    args=parser.parse_args()
    manifest={p['paper']:p for p in json.loads((ROOT/'pipeline/extract/source_files_p4.json').read_text())}
    results=[]
    wrapper='''import random, runpy
random.seed(9618)
runpy.run_path("answer.py", run_name="__main__")
'''
    for c,code,paper in complete_blocks():
        if args.chapter and not c['card'].startswith('P4-'+args.chapter+'-'):continue
        for number,inputs in enumerate(INPUTS.get(c['card'],[[]]),1):
            with tempfile.TemporaryDirectory(prefix='T38-run-') as tmp:
                temp=Path(tmp);copied=[]
                for f in manifest[paper]['files']:
                    if f['path'].lower().endswith('.txt'):
                        source=SOURCES/'pastpapers'/manifest[paper]['sf']/f['path']
                        assert hashlib.sha256(source.read_bytes()).hexdigest()==f['sha256']
                        shutil.copyfile(source,temp/Path(f['path']).name)
                        copied.append(dict(name=Path(f['path']).name,sha256=f['sha256']))
                (temp/'answer.py').write_text(code)
                try:
                    p=subprocess.run([sys.executable,'-c',wrapper],cwd=temp,input=''.join(str(x)+'\n' for x in inputs),
                        capture_output=True,text=True,timeout=8)
                    result=dict(card=c['card'],case=number,inputs=inputs,source_files=copied,
                        exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr,
                        files={p.name:p.read_text() for p in temp.glob('*.txt')
                               if not any(f['name']==p.name and f['sha256']==hashlib.sha256(p.read_bytes()).hexdigest() for f in copied)})
                except subprocess.TimeoutExpired as exc:
                    result=dict(card=c['card'],case=number,inputs=inputs,error='timeout',stdout=str(exc.stdout))
                results.append(result)
    args.out.parent.mkdir(exist_ok=True,parents=True)
    args.out.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    for r in results:
        print(r['card'],r['case'],r.get('exit_code',r.get('error')),
            repr(r.get('stdout',''))[:180],r.get('stderr','')[-200:])


if __name__=='__main__':main()
