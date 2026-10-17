import pytest
from testkit import feed_input,output_lines

@pytest.mark.parametrize('values,expected',[([3.5,3.5],[3.5]),([4.5,2.5],[4.5]),([-3.5,-2.0,0.5,0.0],[-3.5,-2.0,0.5]),([i+0.25 for i in range(20)],[i+0.25 for i in range(20)])])
def test_stop_equal_decrease_and_exact_full_input(sol,monkeypatch,capsys,values,expected):
    """9618_w25_21:4(a) MP2,3,4,5,6; behaviour (syntax and declarations checked manually)."""
    sol.Number=[-999.0]*20
    feed_input(monkeypatch,*map(str,values))
    sol.Store()
    assert sol.Number[:len(expected)]==expected
    assert len(sol.Number)==20
    assert output_lines(capsys.readouterr().out)==[f'{len(expected)} values were stored in the array']
