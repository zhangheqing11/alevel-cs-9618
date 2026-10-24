import re
"""9618_s23_41 Q3: two stacks and restoring an unmatched item."""
from pathlib import Path
import pytest
from testkit import output_lines, run_script, run_script_traced, use_files


def test_3a_declarations(sol):
    """9618_s23_41:3(a) MP1-MP3: two real arrays and zero pointers (D10)."""
    assert isinstance(sol.Animal, list) and len(sol.Animal) == 20
    assert isinstance(sol.Colour, list) and len(sol.Colour) == 10
    assert (sol.AnimalTopPointer, sol.ColourTopPointer) == (0, 0)


@pytest.mark.parametrize('kind,size', [('Animal', 20), ('Colour', 10)])
def test_3b_stack_capacity_lifo_and_reuse(sol, kind, size):
    """9618_s23_41:3(b)(i) MP1-MP3; 3(b)(ii) MP1-MP3; 3(b)(iv) MP1-MP2."""
    push = getattr(sol, 'Push' + kind); pop = getattr(sol, 'Pop' + kind)
    pointer = kind + 'TopPointer'
    assert pop() == ''
    for i in range(size):
        assert push(str(i)) is True
        assert getattr(sol, pointer) == i + 1
    assert push('overflow') is False and getattr(sol, pointer) == size
    for i in range(size - 1, -1, -1):
        assert pop() == str(i) and getattr(sol, pointer) == i
    assert pop() == ''
    assert push('reused') is True and pop() == 'reused'


def test_3b_read_files(sol, monkeypatch, tmp_path, exercise_dir):
    """9618_s23_41:3(b)(iii) MP1-MP3; 3(b)(v) MP1-MP2: all lines via Push operations."""
    use_files(monkeypatch, tmp_path, exercise_dir / 'files')
    seen = {'Animal': [], 'Colour': []}
    for kind in seen:
        original = getattr(sol, 'Push' + kind)
        def spy(value, kind=kind, original=original):
            seen[kind].append(value.rstrip('\r\n'))
            return original(value)
        monkeypatch.setattr(sol, 'Push' + kind, spy)
    sol.ReadData()
    for kind in seen:
        expected = Path(kind + 'Data.txt').read_text().splitlines()
        assert seen[kind] == expected
        assert getattr(sol, kind + 'TopPointer') == len(expected)
        assert [getattr(sol, kind)[i].rstrip('\r\n') for i in range(len(expected))] == expected


@pytest.mark.parametrize('missing', ['AnimalData.txt', 'ColourData.txt'])
def test_3b_missing_file(sol, monkeypatch, tmp_path, exercise_dir, capsys, missing):
    """9618_s23_41:3(b)(iii) MP5; 3(b)(v) MP1: missing-file handling and message."""
    use_files(monkeypatch, tmp_path, exercise_dir / 'files')
    Path(missing).unlink()
    sol.ReadData()
    assert capsys.readouterr().out.strip()


def test_3c_output_pair(sol, capsys, monkeypatch):
    """9618_s23_41:3(c) MP1: pop both stacks and output colour/animal on one line."""
    sol.PushAnimal('horse'); sol.PushColour('black')
    calls = []
    for name in ['PopAnimal', 'PopColour']:
        original = getattr(sol, name)
        def spy(name=name, original=original):
            calls.append(name); return original()
        monkeypatch.setattr(sol, name, spy)
    sol.OutputItem()
    assert calls.count('PopAnimal') == calls.count('PopColour') == 1
    lines = output_lines(capsys.readouterr().out)
    assert any('black horse' in line for line in lines)
    assert (sol.AnimalTopPointer, sol.ColourTopPointer) == (0, 0)


@pytest.mark.parametrize('kind,message', [('Animal', 'No colour'), ('Colour', 'No animal')])
def test_3c_restores_unmatched_item(sol, capsys, kind, message):
    """9618_s23_41:3(c) MP2-MP5: no-match message; surviving item restored to its stack."""
    getattr(sol, 'Push' + kind)('saved')
    sol.OutputItem()
    assert message in capsys.readouterr().out
    assert getattr(sol, kind + 'TopPointer') == 1
    assert getattr(sol, 'Pop' + kind)() == 'saved'


def test_3c_both_empty_does_not_create_item(sol, capsys):
    """9618_s23_41:3(c) MP3/MP5: restore only an item actually removed (QP; D31)."""
    sol.OutputItem()
    assert (sol.AnimalTopPointer, sol.ColourTopPointer) == (0, 0)
    assert capsys.readouterr().out.strip()


def test_3d_screenshot(candidate_path, exercise_dir):
    """9618_s23_41:3(d)(i) whole; 3(d)(ii) whole: exact own-MS image p.38 pairs."""
    r = run_script(candidate_path, files_dir=exercise_dir / 'files')
    assert r.returncode == 0, r.stderr
    lines = [' '.join(x.split()) for x in output_lines(r.stdout)]
    expected = ['pink hamster', 'blue elephant', 'white eagle', 'yellow rabbit']
    position = 0
    for pair in expected:
        while position < len(lines) and pair not in lines[position]:
            position += 1
        assert position < len(lines), pair
        position += 1


def test_3b_no_algorithm_shortcuts(candidate_path):
    """9618_s23_41:3(b)(i) MP1 (D10): required algorithm cannot be delegated to built-ins."""
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


def test_3d_main_call_chain(candidate_path, exercise_dir):
    """9618_s23_41:3(d)(i) whole (MS p.38): ReadData and OutputItem four times."""
    data = ''
    completed = run_script(candidate_path, stdin=data, files_dir=exercise_dir / 'files', timeout=5.0)
    assert completed.returncode == 0, completed.stderr
    r = run_script_traced(candidate_path, stdin=data, files_dir=exercise_dir / 'files')
    assert r.error is None, r.error
    names = [c.name for c in r.calls if c.name in ('ReadData', 'OutputItem')]
    assert names == ['ReadData'] + ['OutputItem'] * 4
    for name in ('PopAnimal', 'PopColour'):
        assert len(r.called(name)) == 4
    expected = ['pink hamster', 'blue elephant', 'white eagle', 'yellow rabbit']
    position = 0
    for pair in expected:
        position = r.stdout.index(pair, position) + len(pair)

