import itertools,pytest

@pytest.mark.parametrize('a,b,c',list(itertools.product((False,True),repeat=3)))
def test_all_boolean_combinations(sol,monkeypatch,a,b,c):
    """9618_w22_22:5 MP1,2,3,4 (behaviour; syntax/declarations checked manually)."""
    sol.A,sol.B,sol.C=a,b,c
    calls=[]
    for n in range(1,5):
        monkeypatch.setattr(sol,'Sub'+str(n),lambda n=n:calls.append(n))
    sol.main()
    expected=[] if a and not b else [1 if a and c else 2 if a else 4 if c else 3]
    assert calls==expected
