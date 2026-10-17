from datetime import date
import pytest

@pytest.mark.parametrize('production,life,expected',[(date(2025,1,1),1,date(2025,1,2)),(date(2025,1,10),21,date(2025,1,31)),(date(2025,1,31),1,date(2025,2,1)),(date(2025,2,8),21,date(2025,3,1)),(date(2025,4,30),21,date(2025,5,21)),(date(2025,12,31),1,date(2026,1,1))])
def test_month_end_and_year_rollover(sol,production,life,expected):
    """9618_w24_21:6(b) MP2,3,4,5,6,7,8,9; behaviour (syntax and declarations checked manually)."""
    assert sol.GetDate(production,life)==expected
