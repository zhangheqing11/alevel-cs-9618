import pytest


@pytest.mark.parametrize("file_name, expected", [
    ("game.txt", ["house", "hose", "shoe", "houses", "use"]), ("empty.txt", []),
])
def test_load_words(sol, file_name, expected):
    """B1-B2, B6: non-blank strings in file order, stripped newline, empty file."""
    result = sol.load_words(file_name)
    assert result == expected
    assert type(result) is list
    assert all(type(word) is str for word in result)


@pytest.mark.parametrize("file_name, expected", [
    ("game.txt", "houses"), ("tie.txt", "ab"), ("empty.txt", ""),
])
def test_longest_word(sol, file_name, expected):
    """B3-B6: longest word as a string, first on ties and empty when absent."""
    result = sol.longest_word(file_name)
    assert result == expected
    assert type(result) is str
