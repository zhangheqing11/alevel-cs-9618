import pytest


@pytest.mark.parametrize("rows, expected", [
    (["XXX", "OO ", "   "], "X"),
    (["OX ", "OX ", "O X"], "O"),
    (["X O", " XO", "  X"], "X"),
    (["  O", " O ", "O X"], "O"),
    (["XOX", "XOO", "OXX"], ""),
    (["   ", "   ", "   "], ""),
    (["XO ", "   ", "OX "], ""),
])
def test_winner(sol, rows, expected):
    """B1-B8: row/column/diagonal wins, drawn/empty boards and no input mutation."""
    board = [list(row) for row in rows]
    assert sol.winner(board) == expected
    assert board == [list(row) for row in rows]
