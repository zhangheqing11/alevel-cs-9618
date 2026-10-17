import pytest
from testkit import feed_input,output_lines

@pytest.mark.parametrize('sides,expected',[((5,3,4),True),((3,5,4),True),((3,4,5),True),((2,3,4),False)])
def test_triangle_messages(sol,monkeypatch,capsys,sides,expected):
    """9618_s24_22:4 MP1,2,3,4,5 (behaviour; syntax/declarations checked manually)."""
    feed_input(monkeypatch,*map(str,sides))
    sol.IsRA()
    message=' '.join(output_lines(capsys.readouterr().out)).lower()
    assert 'right' in message
    negative=any(word in message for word in ('not','not a',"isn't",'no '))
    assert negative is (not expected)
