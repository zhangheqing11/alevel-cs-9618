import re
import pytest
from testkit import feed_input,run_script,use_files

def values(t): return (t.GetTreeName(),t.GetGrowth(),t.GetMaxHeight(),t.GetMaxWidth(),t.GetEvergreen())

def test_2a_constructor_getters(sol):
    """9618_s24_41:2(a)(i) MP2, MP4; 2(a)(ii) MP2-MP3: private attributes, all getters."""
    t=sol.Tree("Oak",20,500,300,"No")
    assert values(t)==("Oak",20,500,300,"No")
    assert all("_Tree__"+n in vars(t) for n in ["TreeName","HeightGrowth","MaxHeight","MaxWidth","Evergreen"])

def test_2b_reads_nine_objects(sol,exercise_dir,monkeypatch,tmp_path):
    """9618_s24_41:2(b) MP2-MP8: file fields, integers, distinct objects, returned array."""
    work=use_files(monkeypatch,tmp_path,exercise_dir / "files")
    trees=sol.ReadData()
    expected=[]
    for line in (work / "Trees.txt").read_text().splitlines():
        name,g,h,w,e=line.split(","); expected.append((name,int(g),int(h),int(w),e))
    assert len(trees) >= 9 and len({id(t) for t in trees[:9]}) == 9
    assert [values(t) for t in trees[:9]] == expected

def test_2b_missing_file(sol,monkeypatch,tmp_path,capsys):
    """9618_s24_41:2(b) MP1: exception handler and output."""
    monkeypatch.chdir(tmp_path)
    sol.ReadData()
    assert capsys.readouterr().out.strip()

@pytest.mark.parametrize("evergreen,ending",[("Yes","does not lose its leaves"),("No","loses its leaves each year")])
def test_2c_printtrees_both_messages(sol,capsys,evergreen,ending):
    """9618_s24_41:2(c) MP1-MP4: getters, all attributes, evergreen-specific message."""
    sol.PrintTrees(sol.Tree("Oak",20,500,300,evergreen))
    actual=" ".join(capsys.readouterr().out.split()).rstrip(".")
    assert actual=="Oak has a maximum height 500 a maximum width 300 and grows 20 cm a year. It "+ending

def test_2e_filter_inclusive_all_requirements_and_years(sol,monkeypatch,capsys):
    """9618_s24_41:2(e)(i) MP1-MP6; 2(e)(ii) MP1-MP2: filter AND, inclusive bounds, selected growth."""
    trees=[sol.Tree("Exact",30,400,200,"No"),sol.Tree("Tall",20,401,100,"No"),sol.Tree("Wide",20,300,201,"No"),sol.Tree("Keep",20,300,100,"Yes"),sol.Tree("Small",20,200,100,"No")]
    shown=[]
    monkeypatch.setattr(sol,"PrintTrees",lambda t:shown.append(t.GetTreeName()))
    feed_input(monkeypatch,"lose","400","200","Exact","40")
    sol.ChooseTree(trees)
    assert shown==["Exact","Small"]
    assert re.findall(r"\d+(?:\.\d+)?",capsys.readouterr().out)[-1] in ["12","12.0"]

def test_2e_no_suitable_trees(sol,monkeypatch,capsys):
    """9618_s24_41:2(e)(i) MP7: no match message and no request to buy from an empty list."""
    feed_input(monkeypatch,"keep","10","10")
    sol.ChooseTree([sol.Tree("Large",10,100,100,"Yes")])
    assert capsys.readouterr().out.strip()

def test_2d_ii_and_2e_iii_screenshots(candidate_path,exercise_dir):
    """9618_s24_41:2(d)(i) MP1-MP2; 2(d)(ii) whole; 2(e)(iii) MP1-MP2: Beech, two conifers, 3/3.75/4."""
    result=run_script(candidate_path,stdin="keep\n400\n200\nBlue Conifer\n100\n",files_dir=exercise_dir / "files")
    assert result.returncode==0,result.stderr
    assert "Beech has a maximum height 400" in result.stdout
    assert "Blue Conifer has a maximum height 250" in result.stdout
    assert "Green Conifer has a maximum height 300" in result.stdout
    tail=result.stdout.split("Green Conifer")[-1]
    assert float(re.findall(r"\d+(?:\.\d+)?",tail)[-1]) in [3,3.75,4]


def test_2d_2e_main_call_chain(candidate_path, exercise_dir):
    """9618_s24_41:2(d)(i) MP1–MP2, 2(e)(iii) MP1; MS pp.21,28: pass returned trees onward."""
    from testkit import run_script_traced
    r = run_script_traced(candidate_path, stdin="keep\n400\n200\nBlue Conifer\n100\n", files_dir=exercise_dir / "files")
    assert r.error is None, r.error
    reads, prints, choices = r.called("ReadData"), r.called("PrintTrees"), r.called("ChooseTree")
    assert reads and prints and choices
    trees = reads[0].result
    assert list(prints[0].args.values())[0] is trees[0]
    assert list(choices[0].args.values())[0] == trees
    assert r.calls.index(reads[0]) < r.calls.index(prints[0]) < r.calls.index(choices[0])
