import pytest

@pytest.mark.parametrize('percent', [0,9,10,19,20,79,80,89,90,99,100])
def test_progress_boundaries(sol,monkeypatch,percent):
    """9618_s24_23:6(a) MP1,2,3,4,5,6 (behaviour; syntax/declarations checked manually)."""
    names=[]
    monkeypatch.setattr(sol,'Display',names.append)
    sol.Progress(percent,'BargraphA')
    assert names==['BargraphA-'+str(percent//10+1)+'.bmp']

def test_root_is_parameter(sol,monkeypatch):
    """9618_s24_23:6(a) MP1,2,3,4,5,6 (behaviour; syntax/declarations checked manually)."""
    names=[]
    monkeypatch.setattr(sol,'Display',names.append)
    sol.Progress(100,'Other')
    assert names==['Other-11.bmp']
