import pytest
from testkit import output_lines

@pytest.mark.parametrize('points',[[0],[11],[0,10,11,22],[10]*999+[11]])
def test_threshold_average_and_full_array(sol,capsys,points):
    """9618_s25_22:7(b) MP3,4,5,6,7,8; behaviour (syntax and declarations checked manually)."""
    sol.Loyalty=[[10001+i,p] for i,p in enumerate(points)]+[[99999,5000] for _ in range(1000-len(points))]
    before=[row[:] for row in sol.Loyalty]
    sol.PointsReport()
    lines=output_lines(capsys.readouterr().out)
    assert lines[:-1]==[str(10001+i) for i,p in enumerate(points) if p>=11]
    prefix='The average points of all the customers is '
    assert lines[-1].startswith(prefix)
    assert float(lines[-1][len(prefix):])==pytest.approx(sum(points)/len(points))
    assert sol.Loyalty==before
