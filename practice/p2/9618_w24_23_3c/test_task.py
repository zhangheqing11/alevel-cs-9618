import pytest
from pathlib import Path
from testkit import output_lines, feed_input
from practice.p2._test_support import watch_open, no_shortcuts

@pytest.mark.parametrize("head,links,expected", [(0,[],[]),(200,[(200,"last",0)],["last"]),(87,[(87,"B",2),(2,"A",200),(200,"C",0)],["B","A","C"])])
def test_follow_links_not_array_order(sol, capsys, head, links, expected):
    """9618_w24_23:3(c) MP1–MP4: HeadPointer, index 200, null and non-contiguous links."""
    sol.List = [sol.Node("unused",0) for _ in range(201)]
    for index,data,pointer in links:
        sol.List[index] = sol.Node(data,pointer)
    sol.HeadPointer = head
    sol.main()
    assert capsys.readouterr().out.splitlines() == expected
