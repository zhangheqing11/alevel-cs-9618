#!/usr/bin/env python3
"""Build corpus/tag_report_p4.md from the annotation sources, the corpus rows and the pilot comparison."""
import json
from collections import Counter, defaultdict

from workbench import HERE, ROOT, rows, records, duplicates
import pilot_compare

from report_notes import NARRATIVE


def main():
    data = rows()
    dups = duplicates(data)
    tags = {t["id"]: t for t in records(HERE / "p4_tags.jsonl")}
    points = {p["id"]: p for p in records(HERE / "p4_markpoints.jsonl")}
    tax = json.loads((ROOT / "papers/p4/taxonomy.json").read_text(encoding="utf-8"))
    names = {t["code"]: t["name_zh"] for t in tax["types"]}
    core = [r for r, row in data.items() if not row["extension"] and r not in dups]
    uniq = [r for r in data if r not in dups]
    low = [r for r in data if tags[r]["confidence"] == "low"]

    out = ["# P4 打标签报告（T34）", "",
           "> 由 `pipeline/tag/p4/report_p4.py` 生成。核验语料 = 2022–2026s 全部 variant（不含 2021 扩展），"
           "按 `equivalent_of` 去重（T12f 后 205 行重复行全部带链）。", ""]
    out += ["## 1. 总览", "",
            "| 项 | 全部 744 行 | 去重后（独立行） | 核验语料去重 |", "|:--|--:|--:|--:|",
            f"| 行数 | {len(data)} | {len(uniq)} | {len(core)} |",
            f"| 拆得分点的行 | {len(points)} | {sum(r in points for r in uniq)} | {sum(r in points for r in core)} |",
            f"| 得分点条数 | {sum(len(p['markpoints']) for p in points.values())} | "
            f"{sum(len(points[r]['markpoints']) for r in uniq if r in points)} | "
            f"{sum(len(points[r]['markpoints']) for r in core if r in points)} |",
            f"| 带 ms_max 的行 | {sum(p['ms_max'] is not None for p in points.values())} | "
            f"{sum(points[r]['ms_max'] is not None for r in uniq if r in points)} | "
            f"{sum(points[r]['ms_max'] is not None for r in core if r in points)} |",
            f"| 带副题型的行 | {sum(bool(tags[r]['cross']) for r in data)} | {sum(bool(tags[r]['cross']) for r in uniq)} | "
            f"{sum(bool(tags[r]['cross']) for r in core)} |",
            f"| low 行 | {len(low)}（{len(low) / len(data):.1%}） | {sum(r in low for r in uniq)} | {sum(r in low for r in core)} |",
            "", f"所有 2 分及以上的行（{sum(data[r]['marks'] >= 2 for r in data)} 行）都有计分清单，全部拆分；"
            "不拆的只有 1 分行。", ""]

    out += ["## 2. 每题型行数与分值（核验语料，去重）", "",
            "| 题型 | 名称 | 主题型行数 | 分值 | 作副题型 |", "|:--|:--|--:|--:|--:|"]
    prim, marks, cross = Counter(), Counter(), Counter()
    for r in core:
        prim[tags[r]["primary"]] += 1
        marks[tags[r]["primary"]] += data[r]["marks"]
        for c in tags[r]["cross"]:
            cross[c] += 1
    for t in tax["types"]:
        c = t["code"]
        out.append(f"| {c} | {names[c]} | {prim[c]} | {marks[c]} | {cross[c]} |")
    out += [f"| 合计 | | {sum(prim.values())} | {sum(marks.values())} | {sum(cross.values())} |", ""]
    rare = [c for c in names if prim[c] < 2]
    out += ["### 核验语料出现 < 2 次的题型（主题型计）", ""]
    out += [f"- {c} {names[c]}：{prim[c]} 次" + (f"（另作副题型 {cross[c]} 次）" if cross[c] else "") for c in rare] or ["- 无"]
    out.append("")

    out += ["## 3. 技能标签出现次数（去重后全部独立行的得分点）", ""]
    skills = Counter(s for r in uniq if r in points for m in points[r]["markpoints"] for s in m["skills"])
    p4new = {t["tag"] for t in json.loads((ROOT / "papers/p4/skill_tags.json").read_text(encoding="utf-8"))["tags"]}
    out += ["| 标签 | 次数 | P4 新标签 |", "|:--|--:|:--:|"]
    out += [f"| {s} | {n} | {'✓' if s in p4new else ''} |" for s, n in skills.most_common()]
    unused = sorted(p4new - set(skills))
    out += ["", f"共用到 {len(skills)} 个标签；P4 新标签未用到的：{', '.join(unused) or '无'}。", ""]

    out += ["## 4. low 清单", ""]
    if low:
        out += ["| 行 | 主题型 | 原因 |", "|:--|:--|:--|"]
        out += [f"| {r} | {tags[r]['primary']} | {tags[r]['note']} |" for r in low]
    else:
        out.append("无（原 low 的 3 个独立判定及其 2 行重复已按 D43 ⑤ 定案为 high，见第 9 节）。")
    out.append("")

    c = pilot_compare.compare()
    n = c["rows"]
    out += ["## 5. 与 pilot 的一致率", "",
            "盲标快照 `pipeline/tag/p4/blind/`（提交于读取 pilot 之前，散列见 `blind/manifest.json`，"
            "`pilot_compare.py` 先校验散列）与 `papers/p4/pilot_tags.csv`、`papers/p4/pilot_markpoints.jsonl` 比较：", "",
            "| 指标 | 一致 | 比例 | 完成标准 |", "|:--|--:|--:|:--|",
            f"| 主题型 | {n - len(c['primary_diff'])}/{n} | {(n - len(c['primary_diff'])) / n:.1%} | ≥ 90% |",
            f"| 副题型（集合相同） | {n - len(c['cross_diff'])}/{n} | {(n - len(c['cross_diff'])) / n:.1%} | — |",
            f"| 得分点切分（条数、逐条文本、分值、ms_max 全同） | {c['split_rows'] - len(c['split_diff'])}/{c['split_rows']} | "
            f"{(c['split_rows'] - len(c['split_diff'])) / c['split_rows']:.1%} | ≥ 80% |",
            f"| 技能集合逐条完全相同 | {c['skill_exact']}/{c['skill_points']} | {c['skill_exact'] / c['skill_points']:.1%} | — |",
            f"| 技能集合平均 Jaccard | | {c['skill_jaccard']:.2f} | — |", ""]
    out += ["### 主题型分歧", "", "| 行 | 盲标 | pilot | pilot 说明 | 复核结论 |", "|:--|:--|:--|:--|:--|"]
    for r in c["primary_diff"]:
        out.append(f"| {r} | {c['btags'][r]['primary']} | {c['ptags'][r]['primary']} | {c['ptags'][r]['note']} | "
                   f"终稿 {tags[r]['primary']}：{tags[r]['note']} |")
    out.append("")
    diff_types = Counter()
    for r, _, a, b in c["skill_rows"]:
        for s in set(a) - set(b):
            diff_types["盲标多 " + s] += 1
        for s in set(b) - set(a):
            diff_types["pilot 多 " + s] += 1
    out += ["### 技能标签差异（只在切分一致的行上比）", "",
            "差异集中在次要标签，最常见的：" + "、".join(f"{k}（{v}）" for k, v in diff_types.most_common(10)) + "。"
            "技能不在完成标准内，终稿保留盲标的技能。", ""]
    out.append(NARRATIVE)
    (ROOT / "corpus/tag_report_p4.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("wrote corpus/tag_report_p4.md")


if __name__ == "__main__":
    main()
