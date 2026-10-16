import pytest
from testkit import feed_input, output_lines

@pytest.mark.parametrize(
    'num1, operator, num2, expected',
    [
        ('7', '+', '5', 'Result: 12'),
        ('7', '-', '10', 'Result: -3'),
        ('6', '*', '7', 'Result: 42'),
        ('7', '/', '2', 'Result: 3.5'),
        ('6', '/', '3', 'Result: 2.0'),
        ('17', '%', '5', 'Result: 2'),
        ('5', '/', '0', 'Error: division by zero'),
        ('5', '%', '0', 'Error: division by zero'),
        ('5', '^', '2', 'Error: unknown operator'),
    ],
)
def test_calculator(sol, monkeypatch, capsys, num1, operator, num2, expected):
    """B1-B9: operators, real division, MOD and errors."""
    feed_input(monkeypatch, num1, operator, num2)
    sol.calculator()
    assert output_lines(capsys.readouterr().out) == [expected]
