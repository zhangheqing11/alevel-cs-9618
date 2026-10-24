import re
import pytest
from testkit import run_script

def test_3a_node_references(sol):
    """9618_s25_43:3(a)(i) MP4; 3(a)(ii) MP2-MP3; 3(a)(iii) MP2: correct data, None, setter identity."""
    a,b=sol.Node(4),sol.Node(8)
    assert a.GetData()==4 and a.GetNextNode() is None
    a.SetNextNode(b)
    assert a.GetNextNode() is b

def test_3b_i_ii_iii_empty_and_head_insertion(sol):
    """9618_s25_43:3(b)(i) MP2; 3(b)(ii) MP2-MP4; 3(b)(iii) MP1-MP3: prepend and traverse."""
    linked=sol.LinkedList()
    assert linked.Traverse()==""
    for value in [10,20,-3]: linked.InsertNode(value)
    assert linked.Traverse().strip()=="-3 20 10"

def test_3b_iv_empty_and_singleton(sol):
    """9618_s25_43:3(b)(iv) MP1-MP4, MP7: empty, missing singleton, then remove sole head."""
    linked=sol.LinkedList()
    assert linked.RemoveNode(1) is False
    linked.InsertNode(4)
    assert linked.RemoveNode(9) is False and linked.Traverse().strip()=="4"
    assert linked.RemoveNode(4) is True and linked.Traverse()==""

@pytest.mark.parametrize("remove,expected",[(50,"40 30 20 10"),(30,"50 40 20 10"),(10,"50 40 30 20"),(99,"50 40 30 20 10")])
def test_3b_iv_head_middle_tail_missing(sol,remove,expected):
    """9618_s25_43:3(b)(iv) MP1, MP3-MP7: splice at head/middle/tail; no match leaves list intact."""
    linked=sol.LinkedList()
    for value in [10,20,30,40,50]: linked.InsertNode(value)
    assert linked.RemoveNode(remove) is (remove != 99)
    assert linked.Traverse().strip()==expected

def test_3b_iv_removes_only_first_match(sol):
    """9618_s25_43:3(b)(iv) MP5-MP6: remove the first matching node, preserve rest."""
    linked=sol.LinkedList()
    for value in [5,2,5,1]: linked.InsertNode(value)
    assert linked.RemoveNode(5) is True
    assert linked.Traverse().strip()=="1 2 5"

def test_3c_ii_screenshots_before_after(candidate_path):
    """9618_s25_43:3(c)(i) MP1-MP3; 3(c)(ii) MP1-MP2: 50 40 30 20 10 then 50 40 20 10."""
    result=run_script(candidate_path)
    assert result.returncode==0,result.stderr
    assert [int(v) for v in re.findall(r"-?\d+",result.stdout)]==[50,40,30,20,10,50,40,20,10]
