"""w25/41 Q3: hashed records with ten collision slots per bucket."""
from testkit import output_lines, run_script, use_files


def test_3a_public_record_constructor(sol):
    """9618_w25_41:3(a) MP2: two constructor arguments stored in public fields."""
    record = sol.Record(528, 'permission')
    assert record.Key == 528 and record.Data == 'permission'


def empty(record):
    return record is None or (record.Key in (-1, None) and record.Data in ('', '-1', None))


def test_3b_initialise_all_cells(sol):
    """9618_w25_41:3(b) MP1-MP2: real 100x10 table; Initialise resets every slot."""
    assert isinstance(sol.HashTable, list) and len(sol.HashTable) == 100
    sol.InitialiseHashTable()
    assert len(sol.HashTable) == 100 and all(len(row) == 10 for row in sol.HashTable)
    assert all(empty(record) for row in sol.HashTable for record in row)
    sol.InsertData(sol.Record(999, 'last bucket'))
    sol.InitialiseHashTable()
    assert all(empty(record) for row in sol.HashTable for record in row)


def test_3c_hash_modulo(sol):
    """9618_w25_41:3(c) MP1-MP2: return key MOD 100 including first/last bucket."""
    for value in [0, 1, 99, 100, 199, 528, 1128, 1828, 9999]:
        assert sol.Hash(value) == value % 100


def test_3d_insert_collision_slots_once(sol, monkeypatch):
    """9618_w25_41:3(d) MP2-MP4: calls Hash and fills only next slot, through index 9."""
    sol.InitialiseHashTable()
    calls = []
    original = sol.Hash

    def spy(key):
        calls.append(key)
        return original(key)

    monkeypatch.setattr(sol, 'Hash', spy)
    for i in range(10):
        key = 28 + 100 * i
        sol.InsertData(sol.Record(key, 'value' + str(i)))
        assert [(r.Key, r.Data) for r in sol.HashTable[28][:i + 1]] == [(28 + 100 * j, 'value' + str(j)) for j in range(i + 1)]
        assert all(empty(r) for r in sol.HashTable[28][i + 1:])
    assert calls == [28 + 100 * i for i in range(10)]
    assert all(empty(r) for r in sol.HashTable[27] + sol.HashTable[29])


def test_3e_reads_official_records(sol, monkeypatch, tmp_path, exercise_dir):
    """9618_w25_41:3(e) MP2-MP5: every line becomes a typed Record passed to InsertData."""
    work = use_files(monkeypatch, tmp_path, exercise_dir / 'files')
    expected = [(int(k), v) for k, v in (line.split(',', 1) for line in (work / 'HashTableData.txt').read_text().splitlines())]
    sol.InitialiseHashTable()
    calls = []
    original = sol.InsertData

    def spy(record):
        assert isinstance(record, sol.Record)
        calls.append((record.Key, record.Data))
        original(record)

    monkeypatch.setattr(sol, 'InsertData', spy)
    sol.ReadData()
    assert calls == expected
    for k, data in expected:
        assert sol.GetRecord(k) == data


def test_3e_missing_file_handled(sol, monkeypatch, tmp_path, capsys):
    """9618_w25_41:3(e) MP6: exception produces a message, not a crash."""
    monkeypatch.chdir(tmp_path)
    sol.InitialiseHashTable()
    sol.ReadData()
    assert capsys.readouterr().out.strip()


def test_3f_getrecord_last_collision_and_missing(sol, monkeypatch):
    """9618_w25_41:3(f) MP1-MP5: Hash call, scan whole bucket, string or Not found."""
    sol.InitialiseHashTable()
    for i in range(10):
        sol.InsertData(sol.Record(i * 100 + 99, 'data ' + str(i)))
    called = []
    original = sol.Hash

    def spy(key):
        called.append(key)
        return original(key)

    monkeypatch.setattr(sol, 'Hash', spy)
    assert sol.GetRecord(999) == 'data 9'
    assert sol.GetRecord(1099) == 'Not found'
    assert sol.GetRecord(21) == 'Not found'
    assert called == [999, 1099, 21]


def test_3g_ii_screenshot_words(candidate_path, exercise_dir):
    """9618_w25_41:3(g)(i) MP1-MP3; 3(g)(ii) MP1-MP2: official five searches."""
    result = run_script(candidate_path, stdin='528\n1128\n1828\n1062\n39\n', files_dir=exercise_dir / 'files')
    assert result.returncode == 0, result.stderr
    lines = output_lines(result.stdout)
    index = 0
    for word in ['permission', 'peace', 'precedent', 'up', 'Not found']:
        while index < len(lines) and not lines[index].rstrip().endswith(word):
            index += 1
        assert index < len(lines), f'missing ordered result {word}'
        index += 1
