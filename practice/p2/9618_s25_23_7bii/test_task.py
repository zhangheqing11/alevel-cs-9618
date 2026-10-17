from datetime import date
import pytest

@pytest.mark.parametrize('s,expected',[('03092024',date(2024,9,3)),('29022024',date(2024,2,29)),('31122025',date(2025,12,31)),('01012022',date(2022,1,1))])
def test_parse_day_month_year(sol,s,expected):
    """9618_s25_23:7(b)(ii) MP1,2,3,4 (behaviour; syntax/declarations checked manually)."""
    sol.LastVisitDateString=s
    sol.main()
    assert type(sol.LastVisitDate) is date and sol.LastVisitDate==expected
