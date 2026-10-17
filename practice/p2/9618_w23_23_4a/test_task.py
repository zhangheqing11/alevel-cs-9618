import random
from testkit import output_lines

def test_25_strictly_increasing_integers(sol,capsys):
    """9618_w23_23:4(a) MP2,3,4,5,6 (behaviour; syntax/declarations checked manually)."""
    for seed in (1,3,25):
        random.seed(seed)
        sol.RandList()
        values=[int(s) for s in output_lines(capsys.readouterr().out)]
        assert len(values)==25
        assert all(a<b for a,b in zip(values,values[1:]))
