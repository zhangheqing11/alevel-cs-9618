import pytest

@pytest.mark.parametrize(
    'character, expected',
    [
        ('M', 'upper'),
        ('A', 'upper'),
        ('Z', 'upper'),
        ('a', 'lower'),
        ('z', 'lower'),
        ('0', 'digit'),
        ('9', 'digit'),
        (' ', 'space'),
        ('@', 'other'),
        ('[', 'other'),
        (chr(96), 'other'),
        ('{', 'other'),
        ('/', 'other'),
        (':', 'other'),
    ],
)
def test_char_type(sol, character, expected):
    """B1-B8: ASCII ranges, edges and neighbours."""
    assert sol.char_type(character) == expected
