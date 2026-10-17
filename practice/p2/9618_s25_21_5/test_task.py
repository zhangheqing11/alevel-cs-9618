import pytest
from pathlib import Path
from testkit import output_lines, feed_input
from practice.p2._test_support import watch_open, no_shortcuts

@pytest.mark.parametrize("items,start", [(["item 1","item 2","item 3","item 4","item 5","item 6"],0),(["same","B","same"],4),(["only"],0),([],0)])
def test_reversed_active_items_and_pointer_meanings(sol, items, start):
    """9618_s25_21:5 MP1–MP10: both transfer loops and all three public pointers."""
    sol.Stack = items + ["unused"] * 8
    sol.Queue = ["unused"] * (start+len(items)+8)
    sol.TopOfStack = len(items)-1
    sol.FrontPointer = sol.RearPointer = start
    sol.main()
    assert sol.TopOfStack == len(items)-1
    assert sol.Stack[:len(items)] == list(reversed(items))
    assert sol.FrontPointer == sol.RearPointer == start+len(items)
