import re
import runpy
import pytest
from testkit import run_script

def field(obj,name):
    for key,value in vars(obj).items():
        if key==name or key.endswith("__"+name): return value
    raise AssertionError(name)

def triple(n): return (n.GetLeft(),n.GetData(),n.GetRight())
EXPECTED=[(2,10,1),(-1,11,4),(3,5,5),(-1,1,-1),(6,20,-1),(-1,7,-1),(-1,15,-1)]

def test_2a_node_getters_setters(sol):
    """9618_s24_42:2(a)(i) MP4; 2(a)(ii) MP2-MP3; 2(a)(iii) MP2-MP3."""
    n=sol.Node(44)
    assert triple(n)==(-1,44,-1)
    n.SetLeft(3);n.SetRight(7);n.SetData(99)
    assert triple(n)==(3,99,7)

def test_2b_i_constructor_twenty_independent_nodes(sol):
    """9618_s24_42:2(b)(i) MP2-MP4: 20 Node(-1), FirstNode=-1, NumberNodes=0."""
    tree=sol.TreeClass(); nodes=field(tree,"Tree")
    assert len(nodes)==20 and len({id(n) for n in nodes})==20
    assert all(triple(n)==(-1,-1,-1) for n in nodes)
    assert field(tree,"FirstNode")==-1 and field(tree,"NumberNodes")==0

def test_2b_ii_insert_left_right_and_count(sol):
    """9618_s24_42:2(b)(ii) MP2-MP7: root, insertion order, pointer traversal, count on both branches."""
    tree=sol.TreeClass()
    for count,value in enumerate([10,11,5,1,20,7,15],1):
        node=sol.Node(value);tree.InsertNode(node)
        assert field(tree,"NumberNodes")==count and field(tree,"FirstNode")==0
        assert field(tree,"Tree")[count-1] is node
    assert [triple(n) for n in field(tree,"Tree")[:7]]==EXPECTED

@pytest.mark.parametrize("data",[list(range(20)),list(range(20,0,-1))])
def test_2b_ii_deep_tree_twenty_nodes(sol,data):
    """9618_s24_42:2(b)(ii) MP3-MP7: follow existing pointers repeatedly to a deep free link."""
    tree=sol.TreeClass()
    for value in data: tree.InsertNode(sol.Node(value))
    nodes=field(tree,"Tree")
    assert field(tree,"NumberNodes")==20
    for i in range(19):
        assert nodes[i].GetRight() == (i+1 if data[0]<data[-1] else -1)
        assert nodes[i].GetLeft() == (i+1 if data[0]>data[-1] else -1)

def test_2b_iii_empty_and_populated_output(sol,capsys):
    """9618_s24_42:2(b)(iii) MP1-MP4: empty message, insertion order, getters."""
    tree=sol.TreeClass();tree.OutputTree()
    assert "No nodes" in capsys.readouterr().out
    for value in [10,11,5,1,20,7,15]: tree.InsertNode(sol.Node(value))
    tree.OutputTree()
    assert contains_values(capsys.readouterr().out, [v for row in EXPECTED for v in row])

def test_2c_i_main_identifier(candidate_path,capsys):
    """9618_s24_42:2(c)(i) whole: TreeClass instance called TheTree."""
    ns=runpy.run_path(str(candidate_path),run_name="__main__")
    assert isinstance(ns["TheTree"],ns["TreeClass"])

def test_2c_iii_screenshot(candidate_path):
    """9618_s24_42:2(c)(ii) MP1-MP4; 2(c)(iii) whole: seven left/data/right rows in MS p.27."""
    result=run_script(candidate_path)
    assert result.returncode==0,result.stderr
    assert contains_values(result.stdout, [v for row in EXPECTED for v in row])


def contains_values(text, expected):
    """D31/D46: compare required values in order, allowing explanatory text."""
    values = iter(float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", text))
    return all(any(abs(value - wanted) < 1e-7 for value in values) for wanted in expected)


def test_2main_call_chain(candidate_path, exercise_dir):
    """9618_s24_42:2(c)(ii) MS p.26; 9618_s24_42:2(b)(iii) MS p.24: observe required calls, parameters and returned output (D46)."""
    from testkit import run_script_traced
    r = run_script_traced(candidate_path, stdin='', files_dir=exercise_dir / "files")
    assert r.error is None, r.error

    inserts = r.called("InsertNode")
    assert len(inserts) == 7
    assert [list(c.args.values())[0].GetData() for c in inserts] == [10,11,5,1,20,7,15]
    assert r.called("OutputTree")
    assert any(c.name.endswith("GetLeft") for c in r.calls)
    assert any(c.name.endswith("GetRight") for c in r.calls)
    assert any(c.name.endswith("GetData") for c in r.calls)
