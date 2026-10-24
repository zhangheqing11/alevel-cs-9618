import re
import runpy
from testkit import run_script

def test_3a_i_ii_iii_node_references(sol):
    """9618_s25_41:3(a)(i) MP4; 3(a)(ii) MP2-MP3; 3(a)(iii) MP2-MP3: None and object identity."""
    a,b,c=sol.Node(10),sol.Node(5),sol.Node(20)
    assert a.GetData()==10 and a.GetLeft() is None and a.GetRight() is None
    a.SetLeft(b);a.SetRight(c)
    assert a.GetLeft() is b and a.GetRight() is c

def test_3c_i_ii_root_is_original_node(sol):
    """9618_s25_41:3(c)(i) MP2; 3(c)(ii) whole: root retains original Node reference."""
    n=sol.Node(10)
    assert sol.Tree(n).GetRootNode() is n

def test_3c_iii_insert_identity_and_duplicate_right(sol):
    """9618_s25_41:3(c)(iii) MP2-MP6: both branches, deep traversal, equality goes right."""
    root=sol.Node(10);tree=sol.Tree(root)
    nodes=[sol.Node(v) for v in [20,5,15,7,10]]
    for n in nodes: tree.Insert(n)
    assert root.GetRight() is nodes[0] and root.GetLeft() is nodes[1]
    assert nodes[0].GetLeft() is nodes[2] and nodes[1].GetRight() is nodes[3]
    assert nodes[2].GetLeft() is nodes[4]

def test_3d_recursive_inorder(sol,monkeypatch,capsys):
    """9618_s25_41:3(d) MP1-MP5: real recursion visiting left, current, right."""
    root=sol.Node(10);tree=sol.Tree(root)
    for v in [20,5,15,7]:tree.Insert(sol.Node(v))
    original=sol.OutputInOrder;calls=[]
    def spy(node): calls.append(node);return original(node)
    monkeypatch.setattr(sol,"OutputInOrder",spy)
    spy(root)
    assert [int(v) for v in re.findall(r"-?\d+",capsys.readouterr().out)]==[5,7,10,15,20]
    assert len([n for n in calls if n is not None])==5

def test_3b_and_3e_i_main_objects(candidate_path,capsys):
    """9618_s25_41:3(b) MP1-MP2; 3(e)(i) MP1-MP3: five nodes and tree rooted at 10."""
    ns=runpy.run_path(str(candidate_path),run_name="__main__")
    values=[v.GetData() for v in ns.values() if isinstance(v,ns["Node"])]
    assert set(values)>={10,20,5,15,7}
    trees=[v for v in ns.values() if isinstance(v,ns["Tree"])]
    assert any(t.GetRootNode().GetData()==10 for t in trees)

def test_3e_ii_screenshot(candidate_path):
    """9618_s25_41:3(e)(ii) whole: output 5,7,10,15,20, in ascending order."""
    result=run_script(candidate_path)
    assert result.returncode==0,result.stderr
    assert [int(v) for v in re.findall(r"-?\d+",result.stdout)]==[5,7,10,15,20]
