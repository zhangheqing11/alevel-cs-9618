import random,string

def test_password_groups(sol,monkeypatch):
    """9618_s22_23:9(a) MP1,2,3,4,5,6,7,8 (behaviour; syntax/declarations checked manually)."""
    chars=iter('aaB1ZaaB1ZaaB1Z')
    monkeypatch.setattr(sol,'RandomChar',lambda:next(chars))
    value=sol.Generate()
    assert value == 'aB1Z-aB1Z-aB1Z'

def test_generated_shape(sol):
    """9618_s22_23:9(a) MP1,2,3,4,5,6,7,8 (behaviour; syntax/declarations checked manually)."""
    random.seed(21)
    for _ in range(20):
        value=sol.Generate()
        assert len(value)==14
        groups=value.split('-')
        assert len(groups)==3
        for group in groups:
            assert len(group)==4 and len(set(group))==4
            assert all(c in string.ascii_letters+string.digits for c in group)
