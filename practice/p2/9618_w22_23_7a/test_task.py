import pytest
from testkit import feed_input,output_lines
from practice.p2._test_support import no_shortcuts

@pytest.mark.parametrize('first,last,expected',[(1,60,['10 : Invalid identifier name','20 : Bracket mismatch','50 : Error Text Missing','60 : Type mismatch in assignment']),(20,50,['20 : Bracket mismatch','50 : Error Text Missing']),(31,49,[])])
def test_range_inclusive_missing_text_and_none(sol,candidate_path,monkeypatch,capsys,first,last,expected):
    """9618_w22_23:7(a) MP1,2,3,4,5,6,7,8; behaviour (syntax and declarations checked manually)."""
    no_shortcuts(candidate_path)
    sol.ErrCode=[10,20,50,60]+[999]*496
    sol.ErrText=['Invalid identifier name','Bracket mismatch','','Type mismatch in assignment']+['UNDEFINED']*496
    feed_input(monkeypatch,str(first),str(last))
    sol.OutputRange()
    assert output_lines(capsys.readouterr().out)==[f'List of error numbers from {first} to {last}']+expected+[f'{len(expected)} error numbers output']
