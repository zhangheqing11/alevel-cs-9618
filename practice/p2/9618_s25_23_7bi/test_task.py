from datetime import date
import pytest

@pytest.mark.parametrize('points,today,expected',[(132,date(2025,3,10),142),(0,date(2025,3,11),0),(7,date(2025,3,10),17),(12345,date(2025,3,12),12345)])
def test_current_day_and_variable_length_points(sol,monkeypatch,points,today,expected):
    """9618_s25_23:7(b)(i) MP1,2,3,4,5,6,7,8 (behaviour; syntax/declarations checked manually)."""
    monkeypatch.setattr(sol,'TODAY',lambda:today)
    def find(cid):
        assert cid=='100123'
        return cid+','+str(points)+',05032025'
    monkeypatch.setattr(sol,'FindCustomer',find)
    result=sol.MondayCheck('100123')
    assert type(result) is int and result==expected
