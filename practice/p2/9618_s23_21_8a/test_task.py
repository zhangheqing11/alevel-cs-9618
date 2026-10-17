import pytest

@pytest.mark.parametrize('s,exists,expected',[('AbcDE',False,True),('ABCDE',True,False),('abcd',False,False),('abcdef',False,False),('Ab3DE',False,False),('Ab DE',False,False),('abcdZ',False,True)])
def test_new_supplier(sol,monkeypatch,s,exists,expected):
    """9618_s23_21:8(a) MP1,2,3,4,5,6,7 (behaviour; syntax/declarations checked manually)."""
    def lookup(code):
        assert len(code)==5, 'QP: SuppExists raises on a wrong length'
        return exists
    monkeypatch.setattr(sol,'SuppExists',lookup)
    assert sol.IsNewSupp(s) is expected
