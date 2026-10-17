import random
from testkit import output_lines

def test_random_domains_and_conditional_third(sol,capsys):
    """9618_s25_22:3 MP1,2,3,4,5,6,7,8 (behaviour; syntax/declarations checked manually)."""
    branches=set()
    for seed in range(100):
        random.seed(seed)
        sol.main()
        values=[int(s) for s in output_lines(capsys.readouterr().out)]
        assert len(values) in (2,3)
        a,b=values[:2]
        assert -10<=a<=10 and -10<=b<=10 and a!=b
        both=a<0 and b<0
        branches.add(both)
        assert (len(values)==3) is both
        if both:
            assert 30<=values[2]<=35
    assert branches=={False,True}
