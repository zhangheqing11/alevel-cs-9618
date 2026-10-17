from pathlib import Path
import pytest
from practice.p2._test_support import load_at,watch_open

@pytest.mark.parametrize('data,expected',[('',[]),('PROCEDURE Zap()',[['1','P','Zap()']]),('OUTPUT 1\nPROCEDURE MyProc(Z : CHAR)\nENDPROCEDURE\n\nfunction MyFun(Y : CHAR) RETURNS BOOLEAN',[['2','P','MyProc(Z : CHAR)'],['5','F','MyFun(Y : CHAR) RETURNS BOOLEAN']])])
def test_line_numbers_and_string_columns(candidate_path,exercise_dir,tmp_path,monkeypatch,data,expected):
    """9618_s24_23:8(b) MP1,2,3,5,6,7,8; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    module.ModInfo=[['','',''] for _ in range(8)]
    Path('project.txt').write_text(data)
    handles=watch_open(monkeypatch)
    module.FindModules('project.txt')
    assert module.ModInfo[:len(expected)]==expected
    assert len(module.ModInfo)==8
    assert handles and all(h.closed for h in handles)

def test_uses_header_return_value(candidate_path,exercise_dir,tmp_path,monkeypatch):
    """9618_s24_23:8(b) MP1,2,3,5,6,7,8; behaviour (syntax and declarations checked manually)."""
    module=load_at(candidate_path,exercise_dir,tmp_path,monkeypatch)
    Path('project.txt').write_text('first\nskip\nlast')
    calls=[]
    def header(line):
        calls.append(line)
        return {'first':'PA()','skip':'','last':'FB() RETURNS BOOLEAN'}[line]
    monkeypatch.setattr(module,'Header',header)
    module.FindModules('project.txt')
    assert calls==['first','skip','last']
    assert module.ModInfo[:2]==[['1','P','A()'],['3','F','B() RETURNS BOOLEAN']]
