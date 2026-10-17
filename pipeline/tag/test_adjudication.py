"""Regression tests for repeatable design-agent adjudication writeback."""
import csv
import json
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from apply_tags import apply, load_jsonl
import apply_adjudication as adjudication


@pytest.fixture
def workspace(tmp_path):
    for folder in ('pipeline/tag', 'papers/p1', 'corpus/rows/p1'):
        (tmp_path / folder).mkdir(parents=True)
    codes = ['P1-IR-01', 'P1-IR-02', 'P1-IR-03']
    (tmp_path/'papers/p1/taxonomy.json').write_text(json.dumps({'types':[{'code':c} for c in codes]}))
    tags = [dict(id=f'paper:{i}', primary=codes[0], cross=[], confidence='low', note='uncertain') for i in range(1,4)]
    (tmp_path/'pipeline/tag/p1_tags.jsonl').write_text(''.join(json.dumps(t)+'\n' for t in tags))
    rows = [dict(id=t['id'], paper='paper', component=1, stem='原文 \\ ←', equivalent_of='paper:1' if i==1 else None) for i,t in enumerate(tags)]
    (tmp_path/'corpus/rows/p1/paper.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
    write_csv(tmp_path, [('paper:1', codes[1], ';'.join([codes[2], codes[0]]), '裁决规则 B1（示例）：解释')])
    return tmp_path


def write_csv(root, rows):
    with (root/'papers/p1/adjudication.csv').open('w',encoding='utf-8-sig',newline='') as out:
        writer=csv.writer(out);writer.writerow(['id','primary','cross','reason']);writer.writerows(rows)


def snapshot(root):
    return {str(p.relative_to(root)):p.read_bytes() for p in root.rglob('*.jsonl')}


def test_writeback_propagates_equivalents_and_is_repeatable(workspace):
    root=workspace
    assert adjudication.apply_adjudications(root)==(1,2)
    tags=load_jsonl(root/'pipeline/tag/p1_tags.jsonl')
    expected=dict(primary='P1-IR-02',cross=['P1-IR-03','P1-IR-01'],confidence='high',note='adjudicated: B1')
    assert all({k:v for k,v in t.items() if k!='id'}==expected for t in tags[:2])
    assert tags[2]['confidence']=='low'
    apply(root)
    before=snapshot(root)
    assert adjudication.apply_adjudications(root)==(1,0)
    assert apply(root)==(3,0)
    assert snapshot(root)==before
    rows=load_jsonl(root/'corpus/rows/p1/paper.jsonl')
    assert rows[0]['stem']=='原文 \\ ←'
    assert rows[0]['types']==dict(primary='P1-IR-02',cross=['P1-IR-03','P1-IR-01'])


def test_later_append_and_empty_cross_are_applied(workspace):
    root=workspace
    adjudication.apply_adjudications(root)
    with (root/'papers/p1/adjudication.csv').open('a',encoding='utf-8',newline='') as out:
        csv.writer(out).writerow(['paper:3','P1-IR-03','','裁决规则 C12（追加）：解释'])
    assert adjudication.apply_adjudications(root)==(2,1)
    tag=load_jsonl(root/'pipeline/tag/p1_tags.jsonl')[2]
    assert tag['cross']==[] and tag['note']=='adjudicated: C12' and tag['confidence']=='high'


@pytest.mark.parametrize('rows', [
    [('missing:1','P1-IR-01','','裁决规则 B1：解释')],
    [('paper:1','P1-XX-99','','裁决规则 B1：解释')],
    [('paper:1','P1-IR-01','P1-IR-02;P1-IR-02','裁决规则 B1：解释')],
    [('paper:1','P1-IR-01','P1-IR-01','裁决规则 B1：解释')],
    [('paper:1','P1-IR-01','','no rule number')],
    [('paper:1','P1-IR-01','','裁决规则 B1：解释')]*2,
    [('paper:1','P1-IR-01','','裁决规则 B1：解释'),('paper:2','P1-IR-03','','裁决规则 B2：冲突')],
])
def test_invalid_or_conflicting_csv_does_not_change_sources(workspace,rows):
    root=workspace;write_csv(root,rows);before=snapshot(root)
    with pytest.raises(ValueError):adjudication.apply_adjudications(root)
    assert snapshot(root)==before


def test_check_mode_does_not_write(workspace):
    before=snapshot(workspace)
    with pytest.raises(ValueError,match='need adjudication'):
        adjudication.apply_adjudications(workspace,check=True)
    assert snapshot(workspace)==before
    adjudication.apply_adjudications(workspace)
    assert adjudication.apply_adjudications(workspace,check=True)==(1,0)


def test_report_retains_blind_history_after_design_ruling(tmp_path,monkeypatch):
    import shutil
    import build_report
    source=Path(__file__).resolve().parents[2]
    for folder in ('corpus/rows/p1','papers/p1'):
        shutil.copytree(source/folder,tmp_path/folder)
    target=tmp_path/'pipeline/tag';target.mkdir(parents=True)
    for name in ('blind_manifest.json','p1_tags.blind.jsonl','pilot_review.jsonl'):
        shutil.copyfile(source/'pipeline/tag'/name,target/name)
    # Start from the immutable blind source, independently of current production tags.
    shutil.copyfile(target/'p1_tags.blind.jsonl',target/'p1_tags.jsonl')
    frozen=(target/'p1_tags.blind.jsonl').read_bytes()
    reviews=(target/'pilot_review.jsonl').read_bytes()
    adjudication.apply_adjudications(tmp_path)
    apply(tmp_path)
    monkeypatch.setattr(build_report,'ROOT',tmp_path)
    build_report.main()
    result=json.loads((target/'pilot_comparison.json').read_text())
    assert result['primary_cross_matches']==87
    assert result['final_primary_cross_matches']==88
    assert result['differences'][0]['review']['decision']=='adjudicated'
    assert result['differences'][0]['initial_review']['decision']=='retain_blind'
    assert (target/'p1_tags.blind.jsonl').read_bytes()==frozen
    assert (target/'pilot_review.jsonl').read_bytes()==reviews
    report=(tmp_path/'corpus/tag_report_p1.md').read_text()
    assert '低信心 0/979' in report and 'adjudicated: B3' in report
