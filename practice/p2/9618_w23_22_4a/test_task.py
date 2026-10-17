import re,pytest
from testkit import feed_input

@pytest.mark.parametrize('values,expected',[(('99',),(0,0)),(('1','2','3','4','99'),(2,2)),(('2','100','99'),(0,2)),(('1','3','5','99'),(3,0))])
def test_counts_without_sentinel(sol,monkeypatch,capsys,values,expected):
    """9618_w23_22:4(a) MP3,4,5,6,7 (behaviour; syntax/declarations checked manually)."""
    feed_input(monkeypatch,*values)
    sol.Count()
    text=capsys.readouterr().out
    assert tuple(map(int,re.findall(r'\d+',text)))==expected
    assert any(c.isalpha() for c in text)
