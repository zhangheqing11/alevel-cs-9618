"""Command categories remain finite and render with Chinese names."""
import json
from pathlib import Path
import shutil

import pytest

from build.build import build_component
from build.stats import command_group, calculate_stats


@pytest.mark.parametrize('word,group', [
    ('State','state'),('Identify','state'),('Give','state'),('Name','state'),('Define','state'),
    ('Describe','describe'),('Outline','describe'),
    ('Explain','explain'),('Justify','explain'),('Suggest','explain'),
    ('Complete','complete'),('Draw','complete'),('Trace','complete'),('Tick','complete'),
    ('Write program code','write'),('Write a logic expression','write'),('Write an SQL script','write'),
    ('Calculate','calculate'),('Convert','calculate'),('Show','calculate'),('Work out','calculate'),
    ('Compare','compare'),('Evaluate','compare'),('Discuss','compare'),
    ('  cOnVeRt:\t the number  ','calculate'),('GIVE\n two examples','state'),
    ('Draw (a circuit)','complete'),(None,'other'),('','other'),('Use','other'),
    ('Showcase','other'),('Programmer','other'),('DECLARE','other'),('OUTPUT','other'),
])
def test_common_command_words(word,group):
    assert command_group(word)==group


def test_distribution_excludes_extension_equivalents_and_cross_only():
    words=['Identify','Give','Convert','Show','Draw','Write','Justify','Evaluate',None]
    def row(i,word):
        return dict(id=str(i),paper='9618_s24_11',session='s',year=2024,marks=1,
                    command_word=word,types=dict(primary='P1-DB-01',cross=['P1-IR-01']))
    rows=[row(i,w) for i,w in enumerate(words)]
    rows += [row(100,'Convert')|{'extension':True},row(101,'Draw')|{'equivalent_of':'1'}]
    stats=calculate_stats(rows)
    assert stats['P1-DB-01']['command_distribution']==dict(state=2,calculate=2,complete=1,write=1,explain=1,compare=1,other=1)
    assert stats['P1-IR-01']['command_distribution']=={}
    assert sum(stats['P1-DB-01']['command_distribution'].values())==stats['P1-DB-01']['questions']==9


def test_build_displays_chinese_but_preserves_machine_keys(tmp_path):
    root=tmp_path/'root'
    shutil.copytree(Path(__file__).parent/'fixtures',root)
    path=root/'corpus/rows/p1/9618_s24_11.jsonl'
    sample=json.loads(path.read_text().splitlines()[0])
    words=['Identify','Describe','Justify','Draw','Write an SQL script','Convert','Evaluate',None]
    rows=[sample|{'id':f'9618_s24_11:{i}','q':str(i),'qn':i,'command_word':word} for i,word in enumerate(words,1)]
    path.write_text(''.join(json.dumps(r)+'\n' for r in rows))
    out=tmp_path/'out'
    build_component(root,out,1)
    md=(out/'p1/P1题型手册.md').read_text()
    html=(out/'p1/P1题型手册.html').read_text()
    for label in ['陈述/识别/列举','描述','解释/论证','补全/绘制','编写（代码/表达式/SQL）','计算/转换','比较/评价','其他']:
        assert label in md and label in html
    assert 'state 3' not in md and 'other 1' not in md
    index=json.loads((out/'p1/index.json').read_text())
    distribution=index['types']['P1-DB-01']['stats']['command_distribution']
    assert set(distribution)=={'state','describe','explain','complete','write','calculate','compare','other'}
    assert distribution['state']==3 and distribution['calculate']==1
