import pytest


@pytest.mark.parametrize("name, args, expected", [
    ("left", ("ABCDEFGH", 3), "ABC"),
    ("right", ("ABCDEFGH", 3), "FGH"),
    ("mid", ("ABCDEFGH", 2, 3), "BCD"),
    ("length", ("Happy Days",), 10),
    ("left", ("ABCDEFGH", 0), ""),
    ("left", ("ABCDEFGH", 8), "ABCDEFGH"),
    ("right", ("ABCDEFGH", 0), ""),
    ("right", ("ABCDEFGH", 8), "ABCDEFGH"),
    ("mid", ("ABCDEFGH", 1, 1), "A"),
    ("mid", ("ABCDEFGH", 8, 1), "H"),
    ("mid", ("ABCDEFGH", 1, 8), "ABCDEFGH"),
    ("mid", ("ABCDEFGH", 3, 0), ""),
    ("length", ("",), 0),
])
def test_insert_functions(sol, name, args, expected):
    """B1-B10: insert examples, first/last/whole/empty slices and return types."""
    result = getattr(sol, name)(*args)
    assert result == expected
    assert type(result) is type(expected)
