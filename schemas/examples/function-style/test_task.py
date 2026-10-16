def test_finds_first_occurrence(sol):
    """format example: returns index of first match"""
    assert sol.linear_search([4, 7, 7, 2], 7) == 1


def test_finds_last_element(sol):
    """format example: loop must reach the final element"""
    assert sol.linear_search([4, 7, 2], 2) == 2


def test_not_found(sol):
    """format example: -1 when absent (and an int, not a Boolean)"""
    result = sol.linear_search([4, 7, 2], 9)
    assert result == -1 and type(result) is int


def test_empty(sol):
    assert sol.linear_search([], 1) == -1
