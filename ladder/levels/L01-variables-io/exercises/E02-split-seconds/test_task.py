import pytest
from testkit import feed_input, output_lines

@pytest.mark.parametrize(
    'seconds, expected',
    [
        (3725, '1 h 2 min 5 s'),
        (59, '0 h 0 min 59 s'),
        (60, '0 h 1 min 0 s'),
        (3600, '1 h 0 min 0 s'),
        (0, '0 h 0 min 0 s'),
        (86399, '23 h 59 min 59 s'),
        (7199, '1 h 59 min 59 s'),
    ],
)
def test_split_seconds(sol, monkeypatch, capsys, seconds, expected):
    """B1-B7: seconds conversion and boundaries."""
    feed_input(monkeypatch, str(seconds))
    sol.split_seconds()
    assert output_lines(capsys.readouterr().out) == [expected]
