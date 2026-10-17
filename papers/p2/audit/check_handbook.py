#!/usr/bin/env python3
"""Reproduce T26b mechanical checks; PDF packets are temporary, not audit verdicts.

Run with the repository venv. Output goes to --out (default /tmp/T26b-evidence).
Source PDFs are only read. Semantic findings remain a separate manual report.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter
import json
import os
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
SOURCES = Path(os.environ.get("ALEVEL_CS_SOURCES", "/Users/zhangheqing/Desktop/alevel cs/sources"))
REF = r"9618_[sw]\d{2}_2[123]:\d+(?:\([a-z0-9]+\))*"


def collect():
    rows = {}
    for path in sorted((ROOT / "corpus/rows/p2").glob("*.jsonl")):
        for line in path.read_text().splitlines():
            row = json.loads(line)
            rows[row["id"]] = row
    cards = []
    for path in sorted((ROOT / "papers/p2/cards").glob("*.md")):
        text = path.read_text()
        headings = list(re.finditer(r"^### (P2-[A-Z]+-\d+).*", text, re.M))
        for i, heading in enumerate(headings):
            end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
            body = text[heading.start():end]
            rep = re.search(r"#### 代表题精讲[^\n]*?(" + REF + r")", body)
            var = re.search(r"\*\*下一道变式\*\*[^\n]*?(" + REF + r")", body)
            cards.append(dict(card=heading[1], file=str(path.relative_to(ROOT)),
                              line=text[:heading.start()].count("\n") + 1,
                              representative=rep[1] if rep else None,
                              variation=var[1] if var else None, body=body))
    return rows, cards


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path("/tmp/T26b-evidence"))
    parser.add_argument("--pdf-packets", action="store_true")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    rows, cards = collect()
    manual_maps = json.loads(Path(__file__).with_name("manual_map_memberships.json").read_text())
    results = {"cards": [], "pick_failures": [], "maps": [], "map_columns": [], "python_ast": [],
               "pseudocode_candidates": [], "page_references": []}
    for card in cards:
        entry = {key: value for key, value in card.items() if key != "body"}
        for role in ("representative", "variation"):
            row = rows[card[role]]
            entry[role + "_pages"] = {"qp": row["qp_page"], "ms": row["ms_page"]}
            reasons = []
            if not 2022 <= row["year"] <= 2025:
                reasons.append("outside 2022-25")
            if row["types"]["primary"] != card["card"]:
                reasons.append("not primary")
            if row.get("equivalent_of"):
                reasons.append("equivalent_of=" + row["equivalent_of"])
            if reasons:
                results["pick_failures"].append(dict(card=card["card"], role=role, row=row["id"], reasons=reasons))
        if rows[card["representative"]]["paper"] == rows[card["variation"]]["paper"]:
            results["pick_failures"].append(dict(card=card["card"], reasons=["same paper"]))
        results["cards"].append(entry)
        # Counts are per distinct leaf, not per MP. Include s26, exclude extension/duplicates,
        # except the AD-05 map explicitly includes its w21/21 extension.
        sample = [r for r in rows.values() if r["types"]["primary"] == card["card"]
                  and r.get("markpoints") and not r.get("equivalent_of")
                  and (2022 <= r["year"] <= 2026 or
                       (card["card"] == "P2-AD-05" and r["id"] == "9618_w21_21:2(b)") or
                       (card["card"] == "P2-DT-08" and r["id"] == "9618_s21_21:5"))]
        skill_counts = Counter()
        for row in sample:
            skill_counts.update({s for mp in row["markpoints"] for s in mp["skills"]})
        if "得分点地图" in card["body"]:
            results["maps"].append(dict(card=card["card"], split_rows=len(sample),
                                        skills=dict(sorted(skill_counts.items())), rows=[r["id"] for r in sample]))
            section = card["body"].split("**得分点地图**", 1)[1].split("**易错", 1)[0]
            column_index = 0
            for line in section.splitlines():
                column = re.match(r"\| (.*?) \| (\d+) \| (.*?) \|", line)
                if not column:
                    continue
                label, reported, tags = column.groups()
                method = "skill union per leaf"
                if card["card"] in manual_maps:
                    manual = manual_maps[card["card"]]
                    members = manual["columns"][column_index]
                    group_by_paper = manual.get("group_by") == "paper"
                    actual = len({rid.split(":")[0] if group_by_paper else rid for rid in members})
                    method = "manual MS memberships" + (" grouped by paper" if group_by_paper else "")
                else:
                    # PG-10 explicitly counts return-value=7 and separately notes boolean-return=2.
                    if card["card"] == "P2-PG-10" and label.startswith("各种情况"):
                        tags = "`return-value`"
                    skills = set(re.findall(r"`([^`]+)`", tags))
                    members = [r["id"] for r in sample if skills &
                               {s for mp in r["markpoints"] for s in mp["skills"]}]
                    actual = len(members)
                results["map_columns"].append(dict(card=card["card"], label=label,
                    reported=int(reported), recounted=actual, delta=actual-int(reported),
                    method=method, supporting_rows=members))
                column_index += 1
    paths = sorted((ROOT / "papers/p2/cards").glob("*.md")) + sorted((ROOT / "papers/p2/core").glob("*.md"))
    paths += [ROOT / "papers/p2/front.md", ROOT / "papers/p2/back.md"]
    for path in paths:
        text = path.read_text()
        for match in re.finditer(r"^```(python|pseudocode)\n(.*?)^```", text, re.M | re.S):
            lang, code = match[1], match[2]
            line = text[:match.start()].count("\n") + 2
            record = dict(file=str(path.relative_to(ROOT)), line=line)
            if lang == "python":
                try:
                    ast.parse(code)
                    record["status"] = "parsed"
                except SyntaxError as exc:
                    record.update(status="syntax-error", detail=str(exc))
                results["python_ast"].append(record)
            else:
                # Lexical candidates only: never infer marking from a lint match.
                for offset, code_line in enumerate(code.splitlines()):
                    statement = code_line.split("//", 1)[0]
                    if re.search(r"\b(?:ELSIF|ELSEIF|ENDFOR|BREAK|CONTINUE|def|len)\b|==|!=|\+=|\[[^\]]*\]\[", statement):
                        results["pseudocode_candidates"].append(dict(**record, offset=offset, text=code_line))
        for match in re.finditer(r"QP p\.(\d+)", text):
            results["page_references"].append(dict(file=str(path.relative_to(ROOT)),
                line=text[:match.start()].count("\n") + 1, page=int(match[1]),
                context=text[max(0, match.start()-160):match.end()+80]))
    (args.out / "mechanical.json").write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n")
    if args.pdf_packets:
        import pymupdf
        docs = {}
        for card in cards:
            packet = card["body"] + "\n\n=== ORIGINAL PDF PAGES (not corpus ms_text) ===\n"
            # Include every referenced QP/MS page, including quote context, in each packet.
            for rid in dict.fromkeys(re.findall(REF, card["body"])):
                row = rows[rid]
                packet += "\nROW " + rid + "\n"
                for kind in ("qp", "ms"):
                    filename = re.sub(r"_(2[123])$", "_" + kind + r"_\1.pdf", row["paper"])
                    if filename not in docs:
                        docs[filename] = pymupdf.open(SOURCES / "pastpapers" / filename)
                    pages = row[kind + "_page"]
                    if isinstance(pages, int):
                        pages = [pages]
                    for number in pages:
                        packet += f"\n{filename} p.{number}\n" + docs[filename][number-1].get_text(sort=True)
            (args.out / (card["card"] + ".txt")).write_text(packet)
        for doc in docs.values():
            doc.close()
    print(json.dumps(dict(cards=len(cards), pick_failures=results["pick_failures"],
        python_blocks=len(results["python_ast"]), ast_failures=[r for r in results["python_ast"] if r["status"] != "parsed"],
        pseudocode_candidates=results["pseudocode_candidates"],
        map_columns=len(results["map_columns"]),
        map_differences_ge_2=[r for r in results["map_columns"] if abs(r["delta"]) >= 2],
        out=str(args.out)), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
