import pytest
EXPECTED = [1.5, 3.0, 4.2, 5.4, 10.8, 13.2]

def test_predicted(sol):
    """B1: six dry-run values."""
    assert sol.PREDICTED == pytest.approx(EXPECTED, abs=1e-09)

@pytest.mark.parametrize(
    'weight, express, expected',
    [
        (100, False, 1.5),
        (0, False, 1.5),
        (101, False, 3.0),
        (500, False, 3.0),
        (501, False, 4.2),
        (750, False, 5.4),
        (1250, False, 7.8),
        (1001, False, 6.6),
        (751, True, 10.8),
        (1000, True, 13.2),
        (100, True, 3.0),
    ],
)
def test_postage(sol, weight, express, expected):
    """B2-B8: boundaries, DIV, express and float."""
    result = sol.postage(weight, express)
    assert result == pytest.approx(expected, abs=1e-09)
    assert type(result) is float
