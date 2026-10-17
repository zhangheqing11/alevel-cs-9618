import pytest
from testkit import feed_input,output_lines

@pytest.mark.parametrize('values',[[5]+[0]*98+[7],[-1]*100,list(range(-50,50))])
def test_exact_100_positive_sum(sol,monkeypatch,capsys,values):
    """9618_w24_23:2(a) MP1,2,3,4,5,6 (behaviour; syntax/declarations checked manually)."""
    feed_input(monkeypatch,*map(str,values))
    sol.main()
    assert output_lines(capsys.readouterr().out)==[str(sum(x for x in values if x>0))]
