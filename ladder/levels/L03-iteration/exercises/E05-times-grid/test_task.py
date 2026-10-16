import pytest
from testkit import feed_input, output_lines

@pytest.mark.parametrize(
    'size, expected',
    [
        (3, ['1 2 3', '2 4 6', '3 6 9', 'Total: 36']),
        (1, ['1', 'Total: 1']),
        (5, ['1 2 3 4 5', '2 4 6 8 10', '3 6 9 12 15', '4 8 12 16 20', '5 10 15 20 25', 'Total: 225']),
    ],
)
def test_grid(sol, monkeypatch, capsys, size, expected):
    """B1-B3: nested dimensions, separators and total."""
    feed_input(monkeypatch, str(size))
    sol.times_grid()
    assert output_lines(capsys.readouterr().out) == expected

def test_grid_max(sol, monkeypatch, capsys):
    """B4: N=9 includes final row/column and total 2025."""
    feed_input(monkeypatch, '9')
    sol.times_grid()
    lines = output_lines(capsys.readouterr().out)
    assert len(lines) == 10
    assert lines[8] == '9 18 27 36 45 54 63 72 81'
    assert lines[-1] == 'Total: 2025'
