import pytest
from testkit import feed_input, output_lines

@pytest.mark.parametrize(
    'bill, people, expected',
    [
        ('100', '4', ['Total: 110.00', 'Each: 27.50']),
        ('80', '3', ['Total: 88.00', 'Each: 29.33']),
        ('12.40', '1', ['Total: 13.64', 'Each: 13.64']),
        ('0', '5', ['Total: 0.00', 'Each: 0.00']),
        ('45', '2', ['Total: 49.50', 'Each: 24.75']),
    ],
)
def test_split_bill(sol, monkeypatch, capsys, bill, people, expected):
    """B1-B5: service charge, real input, split and two decimals."""
    feed_input(monkeypatch, bill, people)
    sol.split_bill()
    assert output_lines(capsys.readouterr().out) == expected
