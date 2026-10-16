import pytest
from testkit import feed_input, output_lines

@pytest.mark.parametrize(
    'values, expected, messages',
    [
        (('72',), 72, []),
        (('105', '-3', '72'), 72, ['Invalid: must be 0 to 100'] * 2),
        (('0',), 0, []),
        (('100',), 100, []),
        (('101', '100'), 100, ['Invalid: must be 0 to 100']),
        (('-1', '0'), 0, ['Invalid: must be 0 to 100']),
    ],
)
def test_get_mark(sol, monkeypatch, capsys, values, expected, messages):
    """B1-B7: validation, inclusive edges, messages and int return."""
    feed_input(monkeypatch, *values)
    result = sol.get_mark()
    assert result == expected
    assert type(result) is int
    assert output_lines(capsys.readouterr().out) == messages
