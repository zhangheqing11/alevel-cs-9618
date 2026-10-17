import random,pytest
from testkit import output_lines

@pytest.mark.parametrize('count',[1,2,25,100])
def test_roll_average(sol,capsys,count):
    """9618_s25_23:3 MP1,2,3,4,5,6,7 (behaviour; syntax/declarations checked manually)."""
    random.seed(82)
    average=sol.RollDice(count)
    values=[int(s) for s in output_lines(capsys.readouterr().out)]
    assert len(values)==count
    assert all(1<=n<=6 for n in values)
    assert type(average) is float
    assert average==pytest.approx(sum(values)/count)
