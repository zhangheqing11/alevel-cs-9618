import pytest

@pytest.mark.parametrize('expression,expected',[('803+1904',2707),('34/7',34/7),('10-12',-2),('9*11',99),('0+100',100),('100/8',12.5)])
def test_arithmetic_expression(sol,capsys,expression,expected):
    """9618_w22_21:7(a)(i) MP1,2,3,4,5,6,7,8 (behaviour; syntax/declarations checked manually)."""
    sol.Calculate(expression)
    assert float(capsys.readouterr().out.strip())==pytest.approx(expected)
