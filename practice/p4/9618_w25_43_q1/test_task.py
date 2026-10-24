"""9618_w25_43 Q1 exact MS: 10x10 board, object coordinates and validated selection."""
import re
import runpy
import pytest
from testkit import feed_input,run_script,output_lines


def matrix(objects):
    rows=[['-']*10 for _ in range(10)]
    for r,c,code in objects:rows[r][c]=code
    return [' '.join(row) for row in rows]

MAIN_BOARD=matrix([(0,0,'A'),(9,9,'B'),(4,5,'C'),(2,2,'D'),(8,7,'E')])


def test_1ai_aii_boardobject(sol):
    """9618_w25_43:1(a)(i) MP4-MP5; 9618_w25_43:1(a)(ii) MP2-MP3."""
    o=sol.BoardObject('Z',11)
    assert o.GetCode()=='Z' and o.GetValue()==11


def test_1bi_initial_board(sol):
    """9618_w25_43:1(b)(i) MP3-MP4: real 10x10 list of empty BoardObjects."""
    b=sol.Board()
    assert any(isinstance(v,list) and len(v)==10 and all(isinstance(row,list) and len(row)==10 for row in v) for v in vars(b).values())
    for r in range(10):
        for c in range(10):
            o=b.GetObject(r,c)
            assert isinstance(o,sol.BoardObject) and (o.GetCode(),o.GetValue())==('-',0)


@pytest.mark.parametrize('r,c',[(0,9),(9,0),(4,5),(0,0),(9,9)])
def test_1bii_biii_get_set_coordinates(sol,r,c):
    """9618_w25_43:1(b)(ii) MP2; 9618_w25_43:1(b)(iii) MP2: row/column order, no shared-row alias."""
    b=sol.Board();o=sol.BoardObject('X',3);b.SetObject(o,r,c)
    assert b.GetObject(r,c) is o
    for row in range(10):
        for col in range(10):
            if (row,col)!=(r,c):assert b.GetObject(row,col).GetCode()=='-'


def test_1biv_display_qp_example(sol,capsys,monkeypatch):
    """9618_w25_43:1(b)(iv) MP1-MP3: all codes, one row per line, spaces."""
    data=[(0,7,'A'),(0,9,'B'),(1,1,'C'),(6,5,'E')]
    b=sol.Board()
    for r,c,code in data:b.SetObject(sol.BoardObject(code,1),r,c)
    calls = []
    original = sol.BoardObject.GetCode
    def spy(self):
        value = original(self)
        calls.append(value)
        return value
    monkeypatch.setattr(sol.BoardObject,"GetCode",spy)
    b.DisplayBoard()
    assert len(calls) >= 100
    assert output_lines(capsys.readouterr().out)==matrix(data)


def test_1aiii_ci_named_objects_and_placement(candidate_path,monkeypatch):
    """9618_w25_43:1(a)(iii) MP1-MP3; 9618_w25_43:1(c)(i) MP1-MP3: five names and positions."""
    feed_input(monkeypatch,'4','5');ns=runpy.run_path(str(candidate_path),run_name='__main__')
    for i,(code,value) in enumerate([('A',2),('B',3),('C',5),('D',2),('E',7)],1):
        obj=ns['Object'+str(i)];assert isinstance(obj,ns['BoardObject'])
        assert (obj.GetCode(),obj.GetValue())==(code,value)
    boards=[v for v in ns.values() if isinstance(v,ns['Board'])]
    assert any(all(b.GetObject(r,c) is ns['Object'+str(i)] for i,(r,c) in enumerate([(0,0),(9,9),(4,5),(2,2),(8,7)],1)) for b in boards)


def test_1cii_board_screenshot(candidate_path):
    """9618_w25_43:1(c)(ii) whole: exact populated board from MS p.16."""
    r=run_script(candidate_path,stdin='4\n5\n');assert r.returncode==0,r.stderr
    assert any(r.lines[i:i+10]==MAIN_BOARD for i in range(len(r.lines)-9))


def test_1dii_invalid_inputs_screenshot(candidate_path):
    """9618_w25_43:1(d)(i) MP1-MP4; 9618_w25_43:1(d)(ii) whole: 10,4,-1,5 -> C 5."""
    r=run_script(candidate_path,stdin='10\n4\n-1\n5\n');assert r.returncode==0,r.stderr
    assert re.search(r'\bC\b[\s\S]*?\b5\b',r.stdout)


@pytest.mark.parametrize('row,col,code,value',[(0,0,'A',2),(9,9,'B',3),(8,7,'E',7),(2,2,'D',2),(0,9,None,None)])
def test_1di_hit_miss_and_edges(candidate_path,row,col,code,value):
    """9618_w25_43:1(d)(i) MP1-MP4: both boundaries accepted; hit and Miss."""
    r=run_script(candidate_path,stdin=f'{row}\n{col}\n');assert r.returncode==0,r.stderr
    if code is None:assert 'Miss' in r.stdout
    else:assert re.search(r'\b'+code+r'\b[\s\S]*?\b'+str(value)+r'\b',r.stdout)


def test_1ci_1di_main_call_chain(candidate_path, exercise_dir):
    """9618_w25_43:1(c)(i) MS p.15; 9618_w25_43:1(d)(i) MS p.17; 9618_w25_43:1(b)(iv) MS p.13: 1(b)(iv) MP1; 1(c)(i) MP3; 1(d)(i) MP2–MP4; observe required calls, parameters and returned output (D46)."""
    from testkit import run_script_traced
    r = run_script_traced(candidate_path, stdin='4\n5\n', files_dir=exercise_dir / "files")
    assert r.error is None, r.error

    placements = r.called("SetObject")
    assert [list(c.args.values())[1:] for c in placements] == [[0,0],[9,9],[4,5],[2,2],[8,7]]
    assert r.called("DisplayBoard") and len(r.called("GetCode")) >= 100
    guesses = r.called("GetObject")
    assert any(list(c.args.values()) == [4,5] for c in guesses)
    assert r.called("GetValue") and r.called("GetValue")[-1].result == 5
