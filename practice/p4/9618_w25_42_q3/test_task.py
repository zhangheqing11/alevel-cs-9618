"""w25/42 Q3; EXPECTED_FILE transcribed from exact MS p.38 screenshot."""
import json
from testkit import run_script

EXPECTED_FILE = '''1,40,2
6,4,3
8,82,17
9,8,4
10,21,5
31,23,7
22,1,15
16,34,25
13,67,14
-1,6,-1
-1,9,11
-1,10,12
49,13,23
35,52,19
-1,68,28
-1,2,-1
48,28,26
18,89,20
-1,85,-1
21,66,-1
-1,91,33
-1,53,30
-1,0,-1
-1,15,24
32,19,-1
27,37,37
38,31,-1
-1,35,43
46,74,29
-1,76,45
-1,54,34
-1,22,-1
-1,16,47
-1,98,-1
44,61,-1
36,48,41
40,46,-1
-1,38,39
-1,30,-1
-1,39,-1
-1,41,-1
-1,49,42
-1,50,-1
-1,36,-1
-1,58,-1
-1,80,-1
-1,71,-1
-1,18,-1
-1,25,-1
-1,12,-1'''


def test_3a_globals_and_nulls(sol):
    """9618_w25_42:3(a) MP1-MP3: 50x3 cells and two pointer initial values."""
    assert sol.TreeArray == [[-1, -1, -1] for _ in range(50)]
    assert sol.RootPointer == -1 and sol.FreeNode == 0


def test_3b_insert_left_right_and_deep(sol):
    """9618_w25_42:3(b) MP1, MP3-MP9: root, both branches, deeper parent pointers."""
    for i, value in enumerate([50, 30, 70, 20, 40, 60, 80, 35]):
        sol.AddNode(value)
        assert sol.FreeNode == i + 1 and sol.TreeArray[i][1] == value
    assert sol.RootPointer == 0
    assert sol.TreeArray[:8] == [[1, 50, 2], [3, 30, 4], [5, 70, 6], [-1, 20, -1],
                                 [7, 40, -1], [-1, 60, -1], [-1, 80, -1], [-1, 35, -1]]


def test_3b_last_node_and_full(sol, capsys):
    """9618_w25_42:3(b) MP2, MP7-MP9: 50th insertion succeeds, 51st preserves tree."""
    for value in range(50):
        sol.AddNode(value)
    assert sol.FreeNode == 50
    assert [n[1] for n in sol.TreeArray] == list(range(50))
    assert [n[2] for n in sol.TreeArray] == list(range(1, 50)) + [-1]
    before = [r[:] for r in sol.TreeArray]
    capsys.readouterr()
    sol.AddNode(100)
    assert 'The tree is full' in capsys.readouterr().out
    assert sol.TreeArray == before and sol.FreeNode == 50


def test_3c_file_inputs_call_addnode_in_order(candidate_path, tmp_path, exercise_dir):
    """9618_w25_42:3(c) MP2-MP4: all 50 integers in file order passed to AddNode."""
    out = tmp_path / 'calls.json'
    wrapper = tmp_path / 'trace_read.py'
    wrapper.write_text(
        'import json, runpy, sys\n'
        'calls = []\n'
        'def trace(frame, event, arg):\n'
        '    if event == "call" and frame.f_code.co_name == "AddNode":\n'
        '        calls.append(frame.f_locals[frame.f_code.co_varnames[0]])\n'
        '    return trace\n'
        'sys.settrace(trace)\n'
        'try:\n'
        f'    runpy.run_path({str(candidate_path)!r}, run_name="__main__")\n'
        'finally:\n'
        '    sys.settrace(None)\n'
        f'    open({str(out)!r}, "w").write(json.dumps(calls))\n'
    )
    result = run_script(wrapper, files_dir=exercise_dir / 'files')
    assert result.returncode == 0, result.stderr
    assert json.loads(out.read_text()) == [int(line) for line in (exercise_dir / 'files/TreeData.txt').read_text().splitlines()]


def test_3c_missing_input_file(candidate_path):
    """9618_w25_42:3(c) MP5: missing TreeData.txt gives a message, no unhandled exception."""
    result = run_script(candidate_path)
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip()


def test_3d_write_all_nodes_and_format(sol, monkeypatch, tmp_path):
    """9618_w25_42:3(d) MP2-MP5: 50 lines, left,data,right, including unused nodes."""
    monkeypatch.chdir(tmp_path)
    sol.AddNode(20)
    sol.AddNode(30)
    sol.WriteAllToFile()
    lines = (tmp_path / 'Tree.txt').read_text().splitlines()
    assert lines == ['-1,20,1', '-1,30,-1'] + ['-1,-1,-1'] * 48


def test_3d_write_error_handled(sol, monkeypatch, tmp_path, capsys):
    """9618_w25_42:3(d) MP1: error opening output file caught with message."""
    monkeypatch.chdir(tmp_path)
    (tmp_path / 'Tree.txt').mkdir()
    sol.WriteAllToFile()
    assert capsys.readouterr().out.strip()


def test_3e_ii_screenshot_file_content(candidate_path, exercise_dir):
    """9618_w25_42:3(e)(i) whole; 3(e)(ii) whole: all 50 lines in exact MS screenshot."""
    result = run_script(candidate_path, files_dir=exercise_dir / 'files')
    assert result.returncode == 0, result.stderr
    assert result.read('Tree.txt').splitlines() == EXPECTED_FILE.splitlines()
