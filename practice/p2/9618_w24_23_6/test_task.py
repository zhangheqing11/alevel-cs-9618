import calendar,pytest

@pytest.mark.parametrize('year',[2020,2021,2022,2023,2024,2025,2026,2027,2028,2030])
def test_third_sunday_calendar(sol,year):
    """9618_w24_23:6 MP3,4,5,6,7,8 (behaviour; syntax/declarations checked manually)."""
    sundays=[week[calendar.SUNDAY] for week in calendar.monthcalendar(year,3) if week[calendar.SUNDAY]]
    result=sol.AdjustClock(year)
    assert type(result) is int and result==sundays[2]
