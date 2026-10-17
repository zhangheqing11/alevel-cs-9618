from datetime import date
import pytest

@pytest.mark.parametrize('previous,increment',[(date(2025,3,1),4),(date(2025,2,28),1),(date(2024,3,3),4)])
def test_updates_both_byref_values(sol,monkeypatch,previous,increment):
    """9618_s25_23:7(a)(i) MP2,3,5,6 (behaviour; syntax/declarations checked manually)."""
    today=date(2025,3,31)
    monkeypatch.setattr(sol,'TODAY',lambda:today)
    points=[10]
    last=[previous]
    sol.UpdateVisit(points,last)
    assert points==[10+increment]
    assert last==[today]
