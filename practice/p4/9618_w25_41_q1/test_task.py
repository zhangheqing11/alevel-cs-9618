"""w25/41 Q1: fixed stack, deterministic random main, extrema via Pop."""
import json
import re
import pytest
from testkit import run_script


def test_1a_null_array_last_used_pointer(sol):
    """9618_w25_41:1(a) MP1-MP2: 30 nulls and top -1."""
    assert sol.Stack == [None] * 30 and sol.TopOfStack == -1


def test_1b_capacity_and_boolean(sol):
    """9618_w25_41:1(b) MP1-MP4: 30 pushes, increment before storing, full -> False."""
    for i in range(30):
        assert sol.Push(i * 7) is True
        assert sol.TopOfStack == i and sol.Stack[i] == i * 7
    before = sol.Stack.copy()
    assert sol.Push(999) is False
    assert sol.TopOfStack == 29 and sol.Stack == before


def test_1c_pop_lifo_empty_reuse(sol):
    """9618_w25_41:1(c) MP1-MP4: LIFO, decrement, -999 on empty."""
    assert sol.Pop() == -999 and sol.TopOfStack == -1
    for n in [0, 54, 1000]:
        sol.Push(n)
    assert [sol.Pop() for _ in range(3)] == [1000, 54, 0]
    assert sol.TopOfStack == -1 and sol.Pop() == -999
    assert sol.Push(45) is True and sol.Pop() == 45


@pytest.mark.parametrize('data', [[5], [0, 1000, 8, 20], [24, 8, 25, 10], [7, 7, 7]])
def test_1e_find_values_uses_pop(sol, monkeypatch, capsys, data):
    """9618_w25_41:1(e) MP1-MP4: exhaust Pop, output actual extrema, never sentinel."""
    for n in data:
        sol.Push(n)
    original = sol.Pop
    calls = []

    def spy():
        value = original()
        calls.append(value)
        return value

    monkeypatch.setattr(sol, 'Pop', spy)
    sol.FindValues()
    out = capsys.readouterr().out
    assert calls[:len(data)] == list(reversed(data))
    assert len(data) <= len(calls) <= len(data) + 1
    assert sol.TopOfStack == -1
    assert sorted(int(n) for n in re.findall(r'-?\d+', out)) == sorted([min(data), max(data)])
    assert re.search(r'[A-Za-z]', out), 'extrema require an explanatory message'


def run_seeded(candidate_path, tmp_path, seed):
    data = tmp_path / f'calls_{seed}.json'
    wrapper = tmp_path / f'seeded_{seed}.py'
    wrapper.write_text(
        'import json, random, runpy, sys\n'
        f'random.seed({seed})\n'
        'pushed = []\n'
        'def trace(frame, event, arg):\n'
        '    if event == "call" and frame.f_code.co_name == "Push":\n'
        '        pushed.append(frame.f_locals[frame.f_code.co_varnames[0]])\n'
        '    return trace\n'
        'sys.settrace(trace)\n'
        'try:\n'
        f'    runpy.run_path({str(candidate_path)!r}, run_name="__main__")\n'
        'finally:\n'
        '    sys.settrace(None)\n'
        f'    open({str(data)!r}, "w").write(json.dumps(pushed))\n'
    )
    result = run_script(wrapper)
    return result, json.loads(data.read_text())


def test_1f_ii_screenshot_stack_full_and_extrema(candidate_path, tmp_path):
    """9618_w25_41:1(d) MP2-MP4; 1(f)(i) whole; 1(f)(ii) whole."""
    runs = []
    for seed in [7, 29]:
        result, pushed = run_seeded(candidate_path, tmp_path, seed)
        assert result.returncode == 0, result.stderr
        assert len(pushed) == 31, 'stop immediately after the first failed push'
        assert all(isinstance(v, int) and 0 <= v <= 1000 for v in pushed)
        assert result.stdout.count('Stack full') == 1
        assert sorted(int(n) for n in re.findall(r'-?\d+', result.stdout)) == sorted([min(pushed[:30]), max(pushed[:30])])
        runs.append(pushed)
    assert runs[0] != runs[1], 'random generation must vary with the seed'
