#!/usr/bin/env python3
"""Execute the handbook's exact 38 Python fences with explicit example contexts.

This checks teaching snippets, including partial snippets supplied with their
missing data/callees. It does not certify every input or replace exercise tests.
Run: ~/.venvs/alevel-cs/bin/python papers/p2/audit/run_python.py
"""
from contextlib import redirect_stdout
from datetime import date
import io
import json
import os
from pathlib import Path
import re
from tempfile import TemporaryDirectory
from types import SimpleNamespace as Record

ROOT = Path(__file__).resolve().parents[3]


def main():
    blocks = []
    paths = sorted((ROOT / "papers/p2/cards").glob("*.md"))
    paths += sorted((ROOT / "papers/p2/core").glob("*.md"))
    for path in paths:
        for match in re.finditer(r"^```python\n(.*?)^```", path.read_text(), re.M | re.S):
            blocks.append((str(path.relative_to(ROOT)), match[1]))
    assert len(blocks) == 38, "Snippet inventory changed: update the contexts explicitly"
    results = []

    def run(number, env=None, inputs=(), call=None, check=None, output=None):
        filename, code = blocks[number]
        namespace = dict(env or {})
        values = iter(inputs)
        namespace["input"] = lambda prompt="": str(next(values))
        stream = io.StringIO()
        with redirect_stdout(stream):
            exec(compile(code, filename, "exec"), namespace)
            value = call(namespace) if call else None
        if check:
            assert check(namespace, value), (number, filename, value, namespace)
        if output is not None:
            assert stream.getvalue() == output, (number, stream.getvalue(), output)
        results.append(dict(block=number, file=filename, status="pass"))

    # Cards: original data shapes and explicitly stated examples/boundaries.
    run(0, {"data": list(range(29)) + [-1]}, output="30\n")
    for number in (1, 18):
        states = iter([False, False, True])
        ports = []
        run(number, {"get_stat": lambda: next(states), "reset": ports.append},
            check=lambda n, v: ports == ([1, 2, 3] * 2 if number == 1 else [1, 1]))
    run(2, call=lambda n: n["Component"](),
        check=lambda n, v: (v.item_num, v.reject, v.stage, v.limit_1, v.limit_2) == (0, False, "", 0.0, 0.0))
    run(3, {"data": ["A"] * 3 + ["B"] * 147},
        call=lambda n: (n["too_many"]("A", 2), n["too_many"]("A", 3), n["too_many"]("C", 0)),
        check=lambda n, v: v == (True, False, False))
    run(4, {"loyalty": [[100001, 11], [100002, 1], [99999, 0]]},
        call=lambda n: n["points_report"](), output="100001\nThe average points of all the customers is 6.0\n")
    run(5, {"loan": [Record(student_id="A", on_loan=True), Record(student_id="A", on_loan=False),
                      Record(student_id="B", on_loan=True), Record(student_id="", on_loan=False)]},
        call=lambda n: n["count_loans"]("A"), output="Student has 1 books on loan\nand has returned 1 books\n")
    codes = list(range(500, 0, -1))
    text = [str(c) for c in codes]
    run(6, {"err_code": codes, "err_text": text}, call=lambda n: n["sort_arrays"](),
        check=lambda n, v: codes == list(range(1, 501)) and text == [str(c) for c in codes])
    previous = Path.cwd()
    with TemporaryDirectory(prefix="T26b-python-") as temporary:
        os.chdir(temporary)
        try:
            Path("empty.txt").write_text("")
            Path("nine.txt").write_text("X\n" * 9)
            Path("ten.txt").write_text("\n" + "X\n" * 9 + "Y")
            run(7, call=lambda n: tuple(n["check_file"](f) for f in ("empty.txt", "nine.txt", "ten.txt")),
                check=lambda n, v: v == (False, False, True))
            Path("source.txt").write_text("  A\n\n  //comment\n  B")
            Path("target.txt").write_text("OLD\n")
            run(8, {"delete_spaces": lambda s: s.lstrip(" "), "delete_comment": lambda s: s.split("//", 1)[0]},
                call=lambda n: n["stage_2"]("source.txt", "target.txt"),
                check=lambda n, v: Path("target.txt").read_text() == "OLD\nA\nB\n",
                output="2 blank lines were removed\n")
            Path("Result.txt").write_text("A\nB\nC\nD\nE")
            run(16, call=lambda n: (n["output_three"](2), n["output_three"](4)),
                check=lambda n, v: v == (True, False), output="B\nC\nD\nD\nE\n")
            run(25, {"file_name": "source.txt"}, check=lambda n, v: n["line"] == "  B")
            run(26, {"in_file": "source.txt", "out_file": "filtered.txt"},
                check=lambda n, v: Path("filtered.txt").read_text() == "  A\n  //comment\n  B\n")
            with open("Result.txt") as file:
                run(27, {"file": file}, check=lambda n, v: (n["line_x"], n["line_y"], n["line_z"]) == ("C", "D", "E"))
        finally:
            os.chdir(previous)
    run(9, call=lambda n: [n["push"](float(i)) for i in range(61)],
        check=lambda n, v: v == [True] * 60 + [False] and n["sp"] == n["on_stack"] == 60)
    run(10, {"my_switch": 3}, check=lambda n, v: n["this_char"] == "7")
    run(11, call=lambda n: (n["sub_a"]("Name", True), n["sub_b"](2.5)),
        check=lambda n, v: v == (True, 2.5))
    run(12, inputs=[1, 2, 4, 99], call=lambda n: n["count"](),
        output="Number of odd values: 1\nNumber of even values: 2\n")
    run(13, call=lambda n: [n["factorial"](i) for i in (-1, 0, 1, 5, 7)],
        check=lambda n, v: v == [-1, 1, 1, 120, 5040])
    run(14, call=lambda n: (n["replace"]("Aa A", "A", "x"), n["replace"]("", "a", "b")),
        check=lambda n, v: v == ("xa x", ""))
    run(15, call=lambda n: [n["adjust_clock"](y) for y in (2022, 2024, 2026)],
        check=lambda n, v: v == [20, 17, 15])
    # Core templates: provide the globals implied by each fragment's caption.
    run(17, {"data": ["A", ""] * 15}, output="A\n" * 15)
    run(19, inputs=[-1, 101, 75], check=lambda n, v: n["mark"] == 75)
    run(20, inputs=[2, 3, 0], output="Total: 5\n")
    run(21, {"data": list(range(1, 101))}, check=lambda n, v: n["total"] == 5050)
    run(22, {"err_code": list(range(500)), "err_num": 499}, check=lambda n, v: n["found_at"] == 499)
    run(23, {"loyalty": [[i, 11 if i == 0 else 0] for i in range(1000)],
             "sample": [[1] * 128 for _ in range(6)], "total": 0},
        check=lambda n, v: n["total"] == 768, output="0\n")
    run(24, {"loan": [Record(student_id="A", on_loan=True), Record(student_id="A", on_loan=False)],
             "this_id": "A", "count": 0}, check=lambda n, v: n["count"] == 1)
    run(28, {"head_pointer": 1, "lst": [Record(data="B", pointer=-1), Record(data="A", pointer=0)]}, output="A\nB\n")
    run(29, {"mark": 79}, check=lambda n, v: n["grade"] == "B")
    run(30, {"total": 0}, inputs=[1, 3, 99], check=lambda n, v: n["total"] == 4)
    run(31, inputs=[101, 0], check=lambda n, v: n["mark"] == 0)
    run(32, check=lambda n, v: (n["h"], n["m"]) == (2, 15))
    run(33, {"in_string": "Aa A", "char1": "A", "char2": "x"}, check=lambda n, v: n["new_string"] == "xa x")
    run(34, {"in_string": "12,13,451,22", "total": 0}, check=lambda n, v: n["total"] == 498)
    run(35, {"this_year": 2022, "last_visit": date.today(), "points": 10}, check=lambda n, v: n["points"] == 14)
    run(36, {"state": "S2", "event": "A2"}, check=lambda n, v: n["state"] == "S5", output="X4\n")
    run(37)
    assert {r["block"] for r in results} == set(range(38))
    print(json.dumps({"blocks": 38, "executed": len(results), "results": sorted(results, key=lambda r: r["block"])},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
