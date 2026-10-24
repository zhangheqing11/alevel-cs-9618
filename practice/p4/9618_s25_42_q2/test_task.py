"""9618_s25_42 Q2 hash table; expected screenshot values read from own MS p.32."""
from pathlib import Path
import re
import pytest
from testkit import run_script, use_files

MS_SPARE = [915,136,415,55,349,775,846,469,246,752,8,889,695,292,417,181,810,972,781,46,120,95,378,433,994,946,586,365,615,580,128,944,2,689,962,704,948,435,195,981,320,658,831,408,947,830,88,362,629,986,31,823,527,141,905,965,697,15,24,977,88]


def field(obj, name):
    return getattr(obj, name) if hasattr(obj, name) else getattr(obj, 'Get' + name)()


def values(obj):
    return tuple(field(obj, n) for n in ['Key', 'Item1', 'Item2'])


def test_2a_record_fields(sol):
    """9618_s25_42:2(a) MP2: supplementary field-value check; declaration/types remain manual."""
    assert values(sol.NewRecord(646, 12, 568)) == (646, 12, 568)


def test_2b_arrays_and_initialise(sol):
    """9618_s25_42:2(b)(i) whole; 2(b)(ii) MP1-MP2: 200/100 records, all fields -1."""
    assert isinstance(sol.HashTable, list) and len(sol.HashTable) == 200
    assert isinstance(sol.Spare, list) and len(sol.Spare) == 100
    sol.Initialise()
    assert [values(x) for x in sol.HashTable] == [(-1, -1, -1)] * 200
    assert [values(x) for x in sol.Spare] == [(-1, -1, -1)] * 100


@pytest.mark.parametrize('key,expected', [(0, 0), (199, 199), (200, 0), (646, 46), (999, 199)])
def test_2c_hash(sol, key, expected):
    """9618_s25_42:2(c) MP1-MP2: return key modulo 200."""
    assert sol.CalculateHash(key) == expected


def test_2d_insert_and_collisions(sol, monkeypatch):
    """9618_s25_42:2(d) MP2-MP6: hash call, collision at same index, one overflow slot only."""
    sol.Initialise(); calls = []; original = sol.CalculateHash
    def spy(key):
        calls.append(key); return original(key)
    monkeypatch.setattr(sol, 'CalculateHash', spy)
    data = [(646, 12, 568), (846, 3, 9), (1046, 8, 2), (199, 7, 1)]
    for row in data:
        sol.InsertIntoHash(sol.NewRecord(*row))
    assert calls == [646, 846, 1046, 199]
    assert values(sol.HashTable[46]) == data[0] and values(sol.HashTable[199]) == data[3]
    assert [values(x) for x in sol.Spare[:2]] == data[1:3]
    assert all(field(x, 'Key') == -1 for x in sol.Spare[2:])


def test_2d_last_spare_slot(sol):
    """9618_s25_42:2(d) MP5-MP6: all 100 overflow slots available, including index99."""
    sol.Initialise()
    for i in range(101):
        sol.InsertIntoHash(sol.NewRecord(i * 200, i, i + 1))
    assert values(sol.Spare[99]) == (20000, 100, 101)


def test_2e_create_from_official_data(sol, monkeypatch, tmp_path, exercise_dir):
    """9618_s25_42:2(e) MP2-MP5: every CSV line converted to record and passed to InsertIntoHash."""
    use_files(monkeypatch, tmp_path, exercise_dir / 'files')
    sol.Initialise(); calls = []; original = sol.InsertIntoHash
    def spy(obj):
        calls.append(values(obj)); return original(obj)
    monkeypatch.setattr(sol, 'InsertIntoHash', spy)
    expected = [tuple(map(int, line.split(','))) for line in Path('HashData.txt').read_text().splitlines()]
    sol.CreateHashTable()
    assert calls == expected
    table = [(-1, -1, -1)] * 200; overflow = []
    for row in expected:
        index = row[0] % 200
        if table[index][0] == -1:
            table[index] = row
        else:
            overflow.append(row)
    assert [values(x) for x in sol.HashTable] == table
    assert [values(x) for x in sol.Spare[:len(overflow)]] == overflow


def test_2e_missing_file(sol, monkeypatch, tmp_path, capsys):
    """9618_s25_42:2(e) MP6 optional: exception handling and output."""
    use_files(monkeypatch, tmp_path, tmp_path / 'no-fixtures')
    sol.Initialise(); sol.CreateHashTable()
    assert capsys.readouterr().out.strip()


@pytest.mark.parametrize('count', [0, 3, 100])
def test_2f_printspare_empty_partial_full(sol, capsys, count):
    """9618_s25_42:2(f)(i) MP1-MP2: each occupied key, no empty -1s, full array safe."""
    sol.Initialise()
    for i in range(count):
        sol.Spare[i] = sol.NewRecord(i + 1, 99, 88)
    sol.PrintSpare()
    assert [int(x) for x in re.findall(r'-?\d+', capsys.readouterr().out)] == list(range(1, count + 1))


def test_2f_screenshot(candidate_path, exercise_dir):
    """9618_s25_42:2(f)(ii) whole; 2(f)(iii) whole: 61 keys in exact own-MS screenshot order."""
    r = run_script(candidate_path, files_dir=exercise_dir / 'files')
    assert r.returncode == 0, r.stderr
    assert [int(x) for x in re.findall(r'-?\d+', r.stdout)] == MS_SPARE


def test_2b_no_algorithm_shortcuts(candidate_path):
    """9618_s25_42:2(b)(i) MPwhole (D10): required algorithm cannot be delegated to built-ins."""
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
