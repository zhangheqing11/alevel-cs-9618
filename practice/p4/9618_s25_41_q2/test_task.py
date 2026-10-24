"""s25/41 Q2: exact MS pp.18–29, official source bytes and QP data model."""
from pathlib import Path

import pytest
from testkit import feed_input, run_script, use_files

COLOURS = ("Red", "Green", "Blue", "Orange", "Yellow", "Pink")


def expected_groups(lines):
    result = {colour + ".txt": [] for colour in COLOURS}
    for line in lines:
        number, colour = line.split(",")
        result[colour.title() + ".txt"].append(int(number))
    return result


def test_2a_read_official_file(sol, monkeypatch, tmp_path, exercise_dir):
    """9618_s25_41:2(a) MP2, MP4–MP7: read all lines, strip line breaks, return array."""
    use_files(monkeypatch, tmp_path, exercise_dir / "files")
    expected = Path("TheData.txt").read_text().splitlines()
    prompts = []
    def answer(prompt=""):
        prompts.append(prompt)
        return "TheData.txt"
    monkeypatch.setattr("builtins.input", answer)
    assert sol.ReadData() == expected
    assert len(expected) == 72
    assert len(prompts) == 1 and prompts[0].strip(), "input() needs an appropriate prompt"


@pytest.mark.parametrize("count,ending", [(0, ""), (1, ""), (105, "\n")])
def test_2a_unknown_line_count(sol, monkeypatch, tmp_path, exercise_dir, count, ending):
    """9618_s25_41:2(a) MP4–MP7: EOF rather than hard-coded 72; final line with/without newline."""
    use_files(monkeypatch, tmp_path, exercise_dir / "files")
    lines = [str(i) + ",red" for i in range(count)]
    Path("Other.txt").write_bytes(("\r\n".join(lines) + ending).encode())
    feed_input(monkeypatch, "Other.txt")
    assert sol.ReadData() == lines


def test_2a_missing_file(sol, monkeypatch, tmp_path, exercise_dir, capsys):
    """9618_s25_41:2(a) MP8: handle missing input file and output a message."""
    use_files(monkeypatch, tmp_path, exercise_dir / "files")
    feed_input(monkeypatch, "missing.txt")
    sol.ReadData()
    assert capsys.readouterr().out.strip()


def test_2b_d_split_six_integer_arrays(sol, monkeypatch):
    """9618_s25_41:2(b) MP2–MP6; 2(d) MP1–MP2: six arrays, comma split, integer values, six correct filenames."""
    lines = ["10,red", "-7,green", "0,blue", "12,orange", "19,yellow", "4,pink", "30,red"]
    captured = []
    def store(data, filename):
        assert isinstance(data, list), "each colour needs a 1D array"
        assert all(isinstance(value, int) for value in data), "QP stores integers, not strings"
        captured.append((filename, list(data)))
    monkeypatch.setattr(sol, "StoreData", store)
    sol.SplitData(lines)
    assert len(captured) == 6
    assert dict(captured) == expected_groups(lines)


def test_2b_d_split_official_and_empty_groups(sol, monkeypatch, tmp_path, exercise_dir):
    """9618_s25_41:2(b) MP2–MP6; 2(d) MP1–MP2: all 72 items and all six (possibly empty) groups."""
    use_files(monkeypatch, tmp_path, exercise_dir / "files")
    for lines in (Path("TheData.txt").read_text().splitlines(), ["5,red"]):
        captured = []
        monkeypatch.setattr(sol, "StoreData", lambda data, filename: captured.append((filename, list(data))))
        sol.SplitData(lines)
        assert len(captured) == 6
        assert dict(captured) == expected_groups(lines)


def test_2c_append_new_lines(sol, monkeypatch, tmp_path, exercise_dir):
    """9618_s25_41:2(c) MP1–MP4: append integers to new lines, preserving existing data across calls."""
    use_files(monkeypatch, tmp_path, exercise_dir / "files")
    Path("Output.txt").write_text("91\n")
    sol.StoreData([10, 0, -4], "Output.txt")
    assert Path("Output.txt").read_text().splitlines() == ["91", "10", "0", "-4"]
    sol.StoreData([6], "Output.txt")
    assert Path("Output.txt").read_text().splitlines() == ["91", "10", "0", "-4", "6"]


def test_2c_open_error(sol, monkeypatch, tmp_path, exercise_dir, capsys):
    """9618_s25_41:2(c) MP5: catch failure while opening the output file."""
    use_files(monkeypatch, tmp_path, exercise_dir / "files")
    sol.StoreData([1], "absent/Output.txt")
    assert capsys.readouterr().out.strip()


def test_2c_write_error(sol, monkeypatch, capsys):
    """9618_s25_41:2(c) MP5: exception handling also surrounds writing, not just opening."""
    class BrokenFile:
        def __enter__(self):
            return self
        def __exit__(self, *args):
            return False
        def write(self, value):
            raise OSError("write failed")
        def close(self):
            pass
    monkeypatch.setattr("builtins.open", lambda *args, **kwargs: BrokenFile())
    sol.StoreData([1], "Output.txt")
    assert capsys.readouterr().out.strip()


def test_2ei_eii_screenshot_files(candidate_path, exercise_dir):
    """9618_s25_41:2(e)(i) MP1–MP3; 2(e)(ii) MP1–MP2: input filename prompt, red file and whole-program split."""
    res = run_script(candidate_path, stdin="TheData.txt\n", files_dir=exercise_dir / "files")
    assert res.returncode == 0, res.stderr
    assert res.stdout.strip(), "the filename prompt must be visible"
    expected = expected_groups((exercise_dir / "files/TheData.txt").read_text().splitlines())
    for filename, values in expected.items():
        assert res.read(filename).splitlines() == [str(v) for v in values]


def test_2d_2ei_traced_main(candidate_path, exercise_dir, tmp_path):
    """9618_s25_41:2(d) MP1–2; 2(e)(i) MP1–3; MS pp.28–29."""
    import shutil
    from testkit import run_script_traced
    files = tmp_path / "files"
    shutil.copytree(exercise_dir / "files", files)
    for filename, lines in (("TheData.txt", (files / "TheData.txt").read_text().splitlines()),
                            ("Other.txt", ["17,red", "6,blue", "99,red"])):
        (files / filename).write_text("\n".join(lines))
        r = run_script_traced(candidate_path, stdin=filename + "\n", files_dir=files)
        assert r.error is None
        positions = {id(call): index for index, call in enumerate(r.calls)}
        reads, splits, stores = r.called("ReadData"), r.called("SplitData"), r.called("StoreData")
        assert reads and splits and len(stores) == 6
        assert reads[0].result == lines
        assert splits[0].args["DataArray"] == reads[0].result
        assert positions[id(reads[0])] < positions[id(splits[0])] < positions[id(stores[0])]
        assert {c.args["FileName"]: c.args["DataToStore"] for c in stores} == expected_groups(lines)
        for name, values in expected_groups(lines).items():
            assert (r.workdir / name).read_text().splitlines() == [str(x) for x in values]
