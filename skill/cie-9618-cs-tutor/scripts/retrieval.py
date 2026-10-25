#!/usr/bin/env python3
"""Pick and audit the short retrieval questions used at lesson openings.

The bank is hand-authored Markdown in ``references/retrieval/P<N>.md``.  This
script deliberately uses only the standard library so the tutor can run it in
the same environment as ``ledger.py``.

Examples::

    retrieval.py pick P1 --n 3
    retrieval.py pick P1 --types P1-HW-06,P1-IR-05
    retrieval.py show P1-IR-05-R1
    retrieval.py check
"""

from __future__ import annotations

import argparse
import ast
import datetime as dt
import json
import pathlib
import random
import re
import sys
from collections import defaultdict
from typing import Iterable

try:
    from ledger import find_root, ledger_path, read_ledger
except ImportError:  # pragma: no cover - useful when imported from another cwd
    _SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
    if str(_SCRIPT_DIR) not in sys.path:
        sys.path.insert(0, str(_SCRIPT_DIR))
    from ledger import find_root, ledger_path, read_ledger


PAPERS = ("P1", "P2", "P3", "P4")
STAR_TARGETS = {"★★★": (2, True), "★★☆": (1, False)}
TYPE_RE = re.compile(r"^P[1-4]-[A-Z]{2,3}-\d{2}$")
ITEM_RE = re.compile(
    r"^- \*\*(?P<id>(P[1-4]-[A-Z]{2,3}-\d{2})-R\d+)\*\*"
    r"\s*[　 ]+〔(?P<label>原情境|换情境)〕\s*$"
)
TYPE_HEADING_RE = re.compile(
    r"^###\s+(?P<code>P[1-4]-[A-Z]{2,3}-\d{2})\s*[　 ]+(?P<name>.+?)\s*$"
)
CHAPTER_HEADING_RE = re.compile(r"^##\s+(?P<code>[A-Z]{2,3})\s*[　 ]+(?P<name>.+?)\s*$")
Q_RE = re.compile(r"^\s{2}- Q:\s*(?P<value>.*)$")
A_RE = re.compile(r"^\s{2}- A:\s*(?P<value>.*)$")
MEASURE_RE = re.compile(r"^\s{2}- 测：\s*(?P<value>.*)$")
ROW_RE = re.compile(r"⟦(?P<row>[^⟧\s]+)⟧")
QUOTE_RE = re.compile(r"「(?P<quote>[^」]+)」\s*⟦(?P<row>[^⟧\s]+)⟧")

# Retrieval items for these types should make the learner write a short,
# executable step.  The bank checker uses this list to prevent a whole paper
# of prose-only prompts from passing coverage checks.
CODE_TYPES = {
    # P2: pseudocode modules, file/ADT operations, traces and amendments.
    "P2-DT-05", "P2-DT-06", "P2-DT-07", "P2-DT-09", "P2-DT-10", "P2-DT-16",
    "P2-PG-09", "P2-PG-10", "P2-PG-11",
    "P2-SD-06", "P2-SD-07", "P2-SD-08", "P2-SD-12",
    # P3: algorithms, stack/ADT work, assembly and file pseudocode.
    "P3-CT-02", "P3-CT-06", "P3-FP-03", "P3-FP-10",
    # P4 practical programming: all active P4 retrieval types.
    "P4-PR-01", "P4-PR-03", "P4-AR-01", "P4-AR-04", "P4-AR-05",
    "P4-FL-01", "P4-FL-02", "P4-SR-01", "P4-SR-02", "P4-SR-03", "P4-SR-04",
    "P4-SQ-01", "P4-SQ-02", "P4-SQ-03", "P4-SQ-04", "P4-LT-02", "P4-LT-03",
    "P4-OP-01", "P4-OP-02", "P4-OP-03", "P4-OP-06", "P4-OP-07",
    "P4-MP-01", "P4-MP-02", "P4-MP-03",
}
FORBIDDEN_Q_PHRASES = (
    "state one required step",
    "in a new situation",
    "in a different",
)
GENERIC_MEASURE = "只测这一题型的一个关键得分点。"
CODE_FENCE_RE = re.compile(r"```(?P<lang>[A-Za-z0-9_-]*)\n(?P<body>.*?)```", re.S)
MARKING_PHRASE_RE = re.compile(r"\b(mark(?:s)?|accept|reject|allow|do not|correct)\b", re.I)
PSEUDO_OPENERS = {
    "IF": "ENDIF", "WHILE": "ENDWHILE", "FOR": "NEXT", "REPEAT": "UNTIL",
    "CASE": "ENDCASE", "FUNCTION": "ENDFUNCTION", "PROCEDURE": "ENDPROCEDURE",
    "CLASS": "ENDCLASS",
}


class RetrievalError(Exception):
    """A user-facing bank or command error."""


def paper_number(paper: str) -> int:
    if paper not in PAPERS:
        raise RetrievalError(f"unknown paper {paper!r}; use P1, P2, P3 or P4")
    return int(paper[1])


def bank_path(root: pathlib.Path, paper: str) -> pathlib.Path:
    return root / "skill" / "cie-9618-cs-tutor" / "references" / "retrieval" / f"{paper}.md"


def index_path(root: pathlib.Path, paper: str) -> pathlib.Path:
    return root / "output" / f"p{paper_number(paper)}" / "index.json"


def load_index(root: pathlib.Path, paper: str) -> dict:
    path = index_path(root, paper)
    if not path.exists():
        raise RetrievalError(
            f"{path.relative_to(root)} is missing; run `python3 build/build.py all` first"
        )
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RetrievalError(f"invalid {path.relative_to(root)}: {exc}") from exc
    if not isinstance(data, dict) or not isinstance(data.get("types"), dict):
        raise RetrievalError(f"{path.relative_to(root)} has no usable types index")
    return data


def _finish_item(items: list[dict], current: dict | None) -> None:
    if current is None:
        return
    current["answer"] = "\n".join(current.pop("_answer_lines", []))
    items.append(current)


def parse_bank(path: pathlib.Path, paper: str) -> tuple[list[dict], list[str]]:
    """Parse one bank while retaining the answer block exactly as authored."""
    if not path.exists():
        raise RetrievalError(f"missing bank file: {path}")
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    items: list[dict] = []
    current: dict | None = None
    chapter: str | None = None
    current_type: str | None = None
    answer_mode = False

    if not lines or lines[0].strip() != f"# {paper} 开场检索题库":
        errors.append("first line must be `# P<N> 开场检索题库`")

    for lineno, line in enumerate(lines, 1):
        chapter_match = CHAPTER_HEADING_RE.match(line)
        type_match = TYPE_HEADING_RE.match(line)
        item_match = ITEM_RE.match(line)
        if chapter_match:
            _finish_item(items, current)
            current = None
            answer_mode = False
            chapter = chapter_match.group("code")
            current_type = None
            continue
        if type_match:
            _finish_item(items, current)
            current = None
            answer_mode = False
            current_type = type_match.group("code")
            continue
        if item_match:
            _finish_item(items, current)
            current = {
                "id": item_match.group("id"),
                "type": item_match.group(2),
                "label": item_match.group("label"),
                "chapter": chapter,
                "heading_type": current_type,
                "line": lineno,
                "q": "",
                "measure": "",
                "_answer_lines": [],
            }
            answer_mode = False
            continue
        if current is None:
            continue
        q_match = Q_RE.match(line)
        if q_match:
            current["q"] = q_match.group("value")
            answer_mode = False
            continue
        a_match = A_RE.match(line)
        if a_match:
            current["_answer_lines"] = [a_match.group("value")]
            answer_mode = True
            continue
        measure_match = MEASURE_RE.match(line)
        if measure_match:
            current["measure"] = measure_match.group("value")
            answer_mode = False
            continue
        # A code fence, an indented code line, or an indented evidence line is
        # part of A. Blank lines are retained so ``show`` remains faithful.
        if answer_mode:
            if line.startswith("  - ") or line.startswith("### ") or line.startswith("## "):
                answer_mode = False
            else:
                current["_answer_lines"].append(line[4:] if line.startswith("    ") else line)

    _finish_item(items, current)
    for item in items:
        if item["heading_type"] != item["type"]:
            errors.append(
                f"line {item['line']}: {item['id']} is under {item['heading_type'] or 'no type heading'}"
            )
    return items, errors


def load_bank(root: pathlib.Path, paper: str) -> list[dict]:
    items, errors = parse_bank(bank_path(root, paper), paper)
    if errors:
        raise RetrievalError(f"{bank_path(root, paper).relative_to(root)}: " + "; ".join(errors))
    return items


def all_items(root: pathlib.Path, papers: Iterable[str] = PAPERS) -> dict[str, dict]:
    found: dict[str, dict] = {}
    for paper in papers:
        for item in load_bank(root, paper):
            if item["id"] in found:
                raise RetrievalError(f"duplicate retrieval id {item['id']}")
            found[item["id"]] = item
    return found


def _date_key(value: str, fallback: str = "9999-99-99") -> str:
    try:
        dt.date.fromisoformat(value)
    except (TypeError, ValueError):
        return fallback
    return value


def _choose_item(items: list[dict], code: str, avoid: set[str], rng: random.Random) -> dict:
    choices = [item for item in items if item["type"] == code and item["id"] not in avoid]
    if not choices:
        choices = [item for item in items if item["type"] == code]
    if not choices:
        raise RetrievalError(f"no retrieval questions found for {code}")
    migration = [item for item in choices if item["label"] == "换情境"]
    pool = migration or choices
    return rng.choice(pool)


def _code_blocks(answer: str) -> list[tuple[str, str]]:
    return [(m.group("lang").lower(), m.group("body")) for m in CODE_FENCE_RE.finditer(answer)]


def _pseudo_structure_errors(body: str) -> list[str]:
    """Check the small 1–3 line pseudocode snippets used in retrieval answers."""
    stack: list[str] = []
    errors: list[str] = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line == "..." or line.startswith("//"):
            continue
        upper = line.upper()
        # An ELSE/ELSEIF belongs to the currently open IF; it does not close it.
        if upper.startswith("ELSEIF") or upper == "ELSE":
            if not stack or stack[-1] != "ENDIF":
                errors.append(f"unexpected {line}")
            continue
        matched_end = None
        for opener, closer in PSEUDO_OPENERS.items():
            if upper.startswith(opener + " ") or upper == opener or upper.startswith(opener + "("):
                stack.append(closer)
                break
            if upper == closer or upper.startswith(closer + " "):
                matched_end = closer
                break
        if matched_end:
            if not stack or stack[-1] != matched_end:
                errors.append(f"unexpected {line}")
            else:
                stack.pop()
    errors.extend(f"missing {closer}" for closer in reversed(stack))
    return errors


def _answer_structure_errors(item: dict) -> list[str]:
    errors: list[str] = []
    answer = item["answer"]
    for lang, body in _code_blocks(answer):
        if lang in {"python", "py"}:
            try:
                ast.parse(body)
            except SyntaxError as exc:
                errors.append(f"Python answer does not parse: {exc.msg}")
        elif lang in {"pseudocode", "pseudo", "text", ""}:
            errors.extend(_pseudo_structure_errors(body))
    return errors


def pick(args: argparse.Namespace, root: pathlib.Path) -> int:
    paper = args.paper
    items = load_bank(root, paper)
    by_type: dict[str, list[dict]] = defaultdict(list)
    for item in items:
        by_type[item["type"]].append(item)
    requested = [x.strip() for x in (args.types or "").split(",") if x.strip()]
    rng = random.Random(args.seed)
    avoid = {x.strip() for x in (args.avoid or "").split(",") if x.strip()}

    if requested:
        unknown = [code for code in requested if code not in by_type]
        if unknown:
            print("Unknown or empty retrieval type: " + ", ".join(unknown), file=sys.stderr)
            return 2
        codes = requested
    else:
        ledger_file = pathlib.Path(args.ledger) if args.ledger else ledger_path(root, paper)
        if not ledger_file.is_absolute():
            ledger_file = (pathlib.Path.cwd() / ledger_file).resolve()
        if not ledger_file.exists():
            print(f"No ledger found at {ledger_file}; pass --types or --ledger.")
            return 0
        try:
            ledger_rows, _ = read_ledger(ledger_file)
        except Exception as exc:  # ledger.py provides the detailed schema error
            print(f"Cannot read ledger {ledger_file}: {exc}", file=sys.stderr)
            return 2
        today = dt.date.today().isoformat()
        learning = [row for row in ledger_rows if row.get("状态") == "学习中" and row.get("类型") in by_type]
        mastered = [row for row in ledger_rows if row.get("状态") == "已掌握" and row.get("类型") in by_type]

        def learning_key(row: dict) -> tuple[int, str, str]:
            due = _date_key(row.get("复测日期", ""))
            expired = 0 if due != "9999-99-99" and due <= today else 1
            return (expired, due, _date_key(row.get("日期", "")))

        learning.sort(key=learning_key)
        mastered.sort(key=lambda row: _date_key(row.get("日期", "")))
        rows = learning + mastered
        codes = []
        for row in rows:
            code = row["类型"]
            if code not in codes:
                codes.append(code)
            if len(codes) >= max(0, args.n):
                break
        if not codes:
            print(f"No retrievable types for {paper}: no matching 学习中 or 已掌握 ledger rows.")
            return 0

    n = args.n if not requested else min(args.n, len(codes))
    if requested:
        codes = codes[:n]
    for code in codes[:n]:
        item = _choose_item(items, code, avoid, rng)
        print(f"{item['id']}: {item['q']}")
    return 0


def show(args, root: pathlib.Path) -> int:
    wanted = args.ids
    items = all_items(root)
    missing = [item_id for item_id in wanted if item_id not in items]
    if missing:
        print("Unknown retrieval id: " + ", ".join(missing), file=sys.stderr)
        return 2
    for pos, item_id in enumerate(wanted):
        if pos:
            print()
        item = items[item_id]
        print(f"{item['id']} 〔{item['label']}〕")
        print(f"Q: {item['q']}")
        print("A: " + item["answer"].replace("\n", "\n   "))
        print("测：" + item["measure"])
    return 0


def check_paper(root: pathlib.Path, paper: str) -> tuple[list[str], int, int]:
    errors: list[str] = []
    path = bank_path(root, paper)
    try:
        index = load_index(root, paper)
    except RetrievalError as exc:
        return [str(exc)], 0, 0
    items, parse_errors = parse_bank(path, paper)
    errors.extend(f"{path.relative_to(root)}: {msg}" for msg in parse_errors)
    type_index = index["types"]
    seen: set[str] = set()
    by_type: dict[str, list[dict]] = defaultdict(list)
    measures: dict[str, str] = {}
    switched = 0
    for item in items:
        item_id = item["id"]
        if item_id in seen:
            errors.append(f"{path.relative_to(root)} line {item['line']}: duplicate id {item_id}")
        seen.add(item_id)
        by_type[item["type"]].append(item)
        if item["type"] not in type_index:
            errors.append(f"{path.relative_to(root)} line {item['line']}: {item['type']} is not in taxonomy index")
        if not item["q"].strip():
            errors.append(f"{path.relative_to(root)} line {item['line']}: missing Q")
        if not item["measure"].strip():
            errors.append(f"{path.relative_to(root)} line {item['line']}: missing 测")
        measure = item["measure"].strip()
        if measure == GENERIC_MEASURE:
            errors.append(f"{path.relative_to(root)} line {item['line']}: generic 测 line")
        if measure.endswith(("……", "...", "…")):
            errors.append(f"{path.relative_to(root)} line {item['line']}: 测 line is truncated")
        if len(measure) > 40:
            errors.append(f"{path.relative_to(root)} line {item['line']}: 测 line exceeds 40 characters")
        if measure in measures:
            errors.append(
                f"{path.relative_to(root)} line {item['line']}: 测 duplicates {measures[measure]} in {paper}"
            )
        else:
            measures[measure] = item_id
        question_lower = item["q"].lower()
        for phrase in FORBIDDEN_Q_PHRASES:
            if phrase in question_lower:
                errors.append(f"{path.relative_to(root)} line {item['line']}: template Q phrase {phrase!r}")
        type_info = type_index.get(item["type"], {})
        name_en = str(type_info.get("name_en", "")).strip().lower()
        if len(name_en.split()) >= 3 and name_en in question_lower:
            errors.append(f"{path.relative_to(root)} line {item['line']}: Q repeats name_en {name_en!r}")
        answer = item["answer"]
        if not answer.strip():
            errors.append(f"{path.relative_to(root)} line {item['line']}: missing A")
        if "⟦" not in answer and "非 MS 原文" not in answer:
            errors.append(f"{path.relative_to(root)} line {item['line']}: A needs ⟦row id⟧ or （非 MS 原文）")
        if "非 MS 原文" not in answer:
            quoted = " ".join(m.group("quote") for m in QUOTE_RE.finditer(answer))
            if MARKING_PHRASE_RE.search(quoted):
                errors.append(f"{path.relative_to(root)} line {item['line']}: A quotes marking/commentary text directly")
        for structure_error in _answer_structure_errors(item):
            errors.append(f"{path.relative_to(root)} line {item['line']}: {structure_error}")
        row_ids = ROW_RE.findall(answer)
        if any("s26" in row_id for row_id in row_ids) or "9618_s26_" in answer:
            errors.append(f"{path.relative_to(root)} line {item['line']}: s26 evidence is reserved and forbidden")
        if "「" in answer:
            for match in QUOTE_RE.finditer(answer):
                if not match.group("quote").strip():
                    errors.append(f"{path.relative_to(root)} line {item['line']}: empty quoted evidence")
        if item["label"] == "换情境":
            switched += 1

    expected = {code: data for code, data in type_index.items() if data.get("stars") in STAR_TARGETS}
    for code, data in expected.items():
        entries = by_type.get(code, [])
        required, need_migration = STAR_TARGETS[data["stars"]]
        if len(entries) < required:
            errors.append(f"{path.relative_to(root)}: {code} ({data['stars']}) has {len(entries)} questions; needs {required}")
        if need_migration and not any(item["label"] == "换情境" for item in entries):
            errors.append(f"{path.relative_to(root)}: {code} (★★★) needs at least one 〔换情境〕 question")
        if code in CODE_TYPES:
            code_items = [item for item in entries if "```" in item["answer"] and "非 MS 原文" in item["answer"]]
            required_code = (len(entries) + 1) // 2
            if len(code_items) < required_code:
                errors.append(
                    f"{path.relative_to(root)}: {code} has {len(code_items)}/{len(entries)} code answers; "
                    f"needs at least {required_code}"
                )
        if sum(1 for item in entries if item["label"] == "换情境") > 1:
            answers = [item["answer"] for item in entries if item["label"] == "换情境"]
            if len(answers) != len(set(answers)):
                errors.append(f"{path.relative_to(root)}: {code} has duplicate 〔换情境〕 answers")
        if len(entries) > 1:
            answers = [item["answer"] for item in entries]
            if len(answers) != len(set(answers)):
                errors.append(f"{path.relative_to(root)}: {code} has duplicate answers")
    for code in by_type:
        if code not in expected:
            star = type_index.get(code, {}).get("stars", "unknown")
            errors.append(f"{path.relative_to(root)}: {code} is outside retrieval scope ({star})")
    return errors, len(items), switched


def check(args, root: pathlib.Path) -> int:
    papers = [args.paper] if args.paper else list(PAPERS)
    all_ids: set[str] = set()
    total_errors: list[str] = []
    for paper in papers:
        errors, count, switched = check_paper(root, paper)
        total_errors.extend(errors)
        try:
            items = load_bank(root, paper)
            for item in items:
                if item["id"] in all_ids:
                    total_errors.append(f"duplicate retrieval id across papers: {item['id']}")
                all_ids.add(item["id"])
        except RetrievalError:
            pass
        ratio = (switched / count * 100) if count else 0.0
        print(f"{paper}: {count} questions; {switched} 〔换情境〕 ({ratio:.1f}%)")
    if total_errors:
        print("Retrieval bank check failed:")
        for error in total_errors:
            print(f"  - {error}")
        return 1
    print(f"✓ retrieval bank: {len(all_ids)} questions across {len(papers)} paper(s)")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    pick_parser = sub.add_parser("pick", help="pick question faces from a ledger or explicit types")
    pick_parser.add_argument("paper", choices=PAPERS)
    pick_parser.add_argument("--n", type=int, default=3)
    pick_parser.add_argument("--types", help="comma-separated type codes")
    pick_parser.add_argument("--avoid", help="comma-separated retrieval ids to avoid")
    pick_parser.add_argument("--ledger", help="ledger path (use a temporary copy for experiments)")
    pick_parser.add_argument("--seed", type=int, help="seed deterministic tie selection")

    show_parser = sub.add_parser("show", help="show faces and answers")
    show_parser.add_argument("ids", nargs="+", help="retrieval ids such as P1-IR-05-R1")

    check_parser = sub.add_parser("check", help="audit format and star-level coverage")
    check_parser.add_argument("paper", nargs="?", choices=PAPERS)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        root = find_root(None)
        if args.command == "pick":
            return pick(args, root)
        if args.command == "show":
            return show(args, root)
        if args.command == "check":
            return check(args, root)
    except RetrievalError as exc:
        print(f"retrieval.py: {exc}", file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
