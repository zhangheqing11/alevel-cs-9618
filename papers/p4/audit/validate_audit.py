#!/usr/bin/env python3
"""Validate findings, coverage and SHA-256 inputs; do not infer human review."""
from collections import Counter
import hashlib
import json
from pathlib import Path
from check_handbook import ROOT

BASE=Path(__file__).resolve().parent


def main():
    snapshot=json.loads((BASE/'input_snapshot.json').read_text())
    for path,digest in snapshot.items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest, f'Changed input: {path}; re-audit before updating snapshot'
    findings=[json.loads(line) for line in (BASE/'T38-findings.jsonl').read_text().splitlines()]
    fields={'file','line','card','kind','severity','row','evidence','suggestion'}
    kinds={'quote-misuse','answer-not-full-marks','mp-alignment','pick-rule','count','qp-page','python','concept',
           'evidence-cell','practice-transcription','practice-test','other'}
    for f in findings:
        assert set(f)==fields and f['kind'] in kinds and f['severity'] in {'error','warn','nit'}
        assert (ROOT/f['file']).exists() and 1<=f['line']<=len((ROOT/f['file']).read_text().splitlines())
        assert not any(c in json.dumps(f,ensure_ascii=False) for c in ('⟦','⟧','「','」'))
    coverage=json.loads((BASE/'T38-coverage.json').read_text())
    assert len(coverage['cards'])==36 and all(c['representative_pages'] for c in coverage['cards'])
    runs=json.loads((BASE/'python-runs.json').read_text())
    assert len({r['card'] for r in runs})==35 and all(r.get('exit_code')==0 for r in runs)
    practice=json.loads((BASE/'practice-runs.json').read_text())
    assert len(practice)==17
    for r in practice:
        expected_pass=r['case'] in {'reference','alternate','invalid_main_no_calls'}
        assert (r['exit_code']==0)==expected_pass,(r['exercise'],r['case'],r['summary'])
    report=(BASE/'T38-report.md').read_text()
    assert not any(c in report for c in ('⟦','⟧','「','」'))
    print(json.dumps(dict(inputs=len(snapshot),cards=36,complete_blocks=35,runs=len(runs),
        findings=dict(Counter(f['severity'] for f in findings)),practice_cases=len(practice)),ensure_ascii=False))


if __name__=='__main__':main()
