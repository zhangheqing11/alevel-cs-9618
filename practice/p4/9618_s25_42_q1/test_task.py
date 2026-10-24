"""9618_s25_42 Q1 file-backed stack calculator."""
from pathlib import Path
import re
import pytest
from testkit import run_script, use_files


def test_1a_initial_state(sol):
    """9618_s25_42:1(a) MP1-MP2: string -1 slots, integer -1 pointer."""
    assert isinstance(sol.Stack, list) and sol.Stack == ['-1'] * 20
    assert sol.TopOfStack == -1


def test_1b_push_full(sol):
    """9618_s25_42:1(b) MP2-MP4: top is last occupied index; twenty successes, then -1."""
    for i in range(20):
        assert sol.Push(str(i)) == 1
        assert sol.TopOfStack == i and sol.Stack[i] == str(i)
    before = sol.Stack[:]
    assert sol.Push('overflow') == -1 and sol.Stack == before and sol.TopOfStack == 19


def test_1c_pop_empty_lifo_reuse(sol):
    """9618_s25_42:1(c) MP1-MP4: string empty sentinel and correct top element."""
    assert sol.Pop() == '-1'
    for v in ['10', '+', '4']:
        sol.Push(v)
    for i, v in [(1, '4'), (0, '+'), (-1, '10')]:
        assert sol.Pop() == v and sol.TopOfStack == i
    assert sol.Pop() == '-1'
    sol.Push('8'); assert sol.Pop() == '8'


@pytest.mark.parametrize('filename', ['StackData.txt', 'SecondStack.txt'])
def test_1d_read_official_files(sol, monkeypatch, tmp_path, exercise_dir, filename):
    """9618_s25_42:1(d) MP2-MP4: supplied filename, all lines to Push in source order."""
    use_files(monkeypatch, tmp_path, exercise_dir / 'files')
    expected = Path(filename).read_text().splitlines()
    calls = []; original = sol.Push
    def spy(value):
        calls.append(value); return original(value)
    monkeypatch.setattr(sol, 'Push', spy)
    sol.ReadData(filename)
    assert calls == expected
    assert sol.Stack[:len(expected)] == expected and sol.TopOfStack == len(expected) - 1


def test_1d_overflow_and_missing_file(sol, monkeypatch, tmp_path, exercise_dir, capsys):
    """9618_s25_42:1(d) MP3/MP5/MP6: unknown length, one message per failed push, missing file."""
    use_files(monkeypatch, tmp_path, exercise_dir / 'files')
    Path('Long.txt').write_text('\n'.join(map(str, range(23))))
    sol.ReadData('Long.txt')
    assert sol.TopOfStack == 19 and sol.Stack == list(map(str, range(20)))
    assert capsys.readouterr().out.count('Stack full') == 3
    sol.ReadData('Absent.txt')
    assert capsys.readouterr().out.strip()


@pytest.mark.parametrize('popped,expected', [
    (['10', '+', '3', '-', '2'], 11),
    (['5', '+', '7'], 12), (['10', '-', '4'], 6),
    (['7', '/', '2'], 3.5), (['3', '*', '4'], 12),
    (['2', '^', '3'], 8), (['9'], 9),
    (['8', '/', '4', '+', '3', '*', '2', '^', '2', '-', '1'], 99),
])
def test_1e_calculate_all_operators(sol, monkeypatch, popped, expected):
    """9618_s25_42:1(e) MP2-MP7: Pop calls, alternation, all operators, running total."""
    for value in reversed(popped):
        sol.Push(value)
    calls = []; original = sol.Pop
    def spy():
        value = original(); calls.append(value); return value
    monkeypatch.setattr(sol, 'Pop', spy)
    assert sol.Calculate() == pytest.approx(expected)
    assert calls[:len(popped)] == popped
    assert sol.TopOfStack == -1


@pytest.mark.parametrize('filename,total', [('StackData.txt', 131), ('SecondStack.txt', 320)])
def test_1f_screenshots(candidate_path, exercise_dir, filename, total):
    """9618_s25_42:1(f)(i) MP1-MP2; 1(f)(ii) MP1/MP2: own-MS totals 131 and 320."""
    r = run_script(candidate_path, stdin=filename + '\n', files_dir=exercise_dir / 'files')
    assert r.returncode == 0, r.stderr
    values = re.findall(r'-?\d+(?:\.\d+)?', r.stdout)
    assert values and float(values[-1]) == total


def test_1b_no_algorithm_shortcuts(candidate_path):
    """9618_s25_42:1(b) MP2 (D10): required algorithm cannot be delegated to built-ins."""
    import ast
    tree = ast.parse(candidate_path.read_text(encoding='utf-8'))
    forbidden = {'sort', 'sorted', 'index', 'count', 'max', 'min'}
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = node.func.id if isinstance(node.func, ast.Name) else (
                node.func.attr if isinstance(node.func, ast.Attribute) else '')
            assert name not in forbidden, f'D10: implement the algorithm without {name}()'
        if isinstance(node, ast.Compare):
            assert not any(isinstance(op, (ast.In, ast.NotIn)) for op in node.ops), \
                'D10: implement search with pointers/comparisons rather than membership'
