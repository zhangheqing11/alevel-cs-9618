import pytest


@pytest.mark.parametrize("number, expected", [(0, False), (1, False), (2, True), (3, True), (4, False), (9, False), (25, False), (97, True)])
def test_is_prime(sol, number, expected):
    """B1-B4, B9: zero/one, smallest primes, squares and Boolean return."""
    result = sol.is_prime(number)
    assert result is expected
    assert type(result) is bool


@pytest.mark.parametrize("low, high, expected", [(1, 10, 4), (1, 100, 25), (2, 2, 1), (14, 16, 0), (10, 1, 0)])
def test_count_primes(sol, low, high, expected):
    """B5-B6, B9: inclusive bands, empty/reversed range and integer count."""
    result = sol.count_primes(low, high)
    assert result == expected
    assert type(result) is int


@pytest.mark.parametrize("number, expected", [(0, 2), (1, 2), (2, 3), (13, 17), (97, 101)])
def test_next_prime(sol, number, expected):
    """B7-B9: strictly greater next prime, including boundary values."""
    result = sol.next_prime(number)
    assert result == expected
    assert type(result) is int
