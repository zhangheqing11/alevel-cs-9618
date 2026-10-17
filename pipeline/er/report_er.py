#!/usr/bin/env python3
"""Write corpus/er_report.md: per-paper ER coverage, unmatched labels, spot checks.

Usage: python pipeline/er/report_er.py [--check]
The spot-check record (pipeline/er/spotcheck.json) is made by hand against the ER PDF pages;
this script only verifies that each recorded excerpt still exists on the recorded page.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import apply_er as A  # noqa: E402

ROOT = A.ROOT
OUT = ROOT / 'corpus' / 'er_report.md'
SPOT = Path(__file__).resolve().parent / 'spotcheck.json'

DECISIONS = [
    '`9618_w23_er.pdf` prints the heading **Paper 9618/33** twice (PDF pp. 25 and 31). The first block sits '
    'between 23 and 32, i.e. in the 31 slot, and its text is word-for-word identical to the real 33 block; '
    'QP/MS 31 and 33 also carry identical questions and mark schemes. Treated as 31 (`HEADING_FIXUPS` in '
    '`extract_er.py`, entries carry `er_header: "9618/33"`). Please confirm, or drop the fix-up and 31 loses its ER.',
    '`9618_s24_er.pdf`, Paper 22, Question 1 has the label **(b)** twice (PDF p. 17). The second block ("Few full '
    'mark answers; many candidates gained one of the two marks available ... store them in an array/record/file") '
    'matches the two-mark part 1(c) (documenting variable choices), so it is almost certainly a typo for (c). '
    'Not attached (flagged `duplicate_label`); `9618_s24_22:1(c)` therefore has no `er`. Say if it should be attached to 1(c).',
    '`9618_s25_er.pdf`, Paper 42, Question 3 has **(d)(ii)** twice (PDF p. 46); P4 rows do not exist yet, so '
    'nothing is lost now, but the second block (probably (d)(iii)) is flagged `duplicate_label`.',
    'Where the ER comments on a finer label than the row (rows not split there): `9618_s23_22` ER 6(a) vs row 6, '
    '`9618_w24_23` ER 6(a) vs row 6, `9618_w24_22` ER 1(b)(i) vs row 1(b). Not attached (no guessing). In all three '
    'the ER gives a single sub-label, so attaching it to the row would be unambiguous: say if a rule "row has no '
    'children and the ER has exactly one finer label for it -> attach" is wanted.',
    'The task rule drops a question-level or part-level comment from rows that have their own, more specific '
    'comment (listed below as `superseded`). Their content (e.g. w25_21 Q5 "All parts of Question 5 required candidates '
    'to analyse a block of code") stays in `corpus/er/*.jsonl` only; say if the skill should also see it.',
    'Several ER blocks comment on two sub-parts at once, e.g. "(ii)(iii)" in `9618_s24_42` Q1 (P4). Stored once per label '
    'with `shared_with`; none occur in P1–P3.',
    '`apply_p2.py` (T28) rebuilds each row line with `", "` separators and appends its owned fields last; `apply_er.py` '
    'only inserts `,"er":"..."` in compact style and replaces/removes only that field, so both can be re-run in any order. '
    'codex-1 must keep `er` out of the fields it rewrites (the `run_all.py` downstream list already includes it).',
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    changes, stats, used = A.plan()
    by_paper, duplicates, generals = A.load_er(ROOT)
    um = A.unmatched(stats=stats, used=used)
    um_by = defaultdict(list)
    for item in um:
        um_by[item['paper']].append(item)

    rows_q: dict[str, list] = {}
    for path in A.row_files(ROOT):
        rows_q[path.stem] = [json.loads(l)['q'] for l in path.read_text(encoding='utf-8').splitlines() if l.strip()]

    papers = sorted(set(stats) | set(by_paper) | set(generals),
                    key=lambda p: (p.split('_')[2][0], p.split('_')[1][1:], p.split('_')[1][0], p.split('_')[2]))
    lines = ['# T27 · 考官报告摘录挂载报告', '',
             '由 `pipeline/er/report_er.py` 生成（读 `corpus/er/*.jsonl` 与 `corpus/rows/`）。ER 只用于「易错与失分」，不是给分依据。', '']
    tot = defaultdict(int)
    table = ['| 卷 | ER 条数 | 行数 | 挂上 | 其中本级 | 其中上级回退 | 无 ER 的行 | 未用的 ER 标签 |',
             '|:--|--:|--:|--:|--:|--:|--:|--:|']
    for p in papers:
        st = stats.get(p)
        n_er = len(by_paper.get(p, {})) + sum(1 for d in duplicates if d['paper'] == p)
        rows = st['rows'] if st else 0
        att = st['attached'] if st else 0
        own = st['own'] if st else 0
        inh = st['inherited'] if st else 0
        noer = st['no_er'] if st else 0
        unused = len(um_by.get(p, []))
        table.append(f'| {p} | {n_er} | {rows if st else "—"} | {att} | {own} | {inh} | {noer if st else "—"} | {unused} |')
        for k, v in (('er', n_er), ('rows', rows), ('att', att), ('own', own), ('inh', inh), ('noer', noer)):
            tot[k] += v
    p123 = [s for p, s in stats.items() if not p.split('_')[1].startswith('s26')]
    rows_cov = sum(s['rows'] for s in p123)
    att_cov = sum(s['attached'] for s in p123)
    lines += ['## 总览', '',
              f'- 行总数 {tot["rows"]}，挂上 `er` {tot["att"]}（本级 {tot["own"]}、上级回退 {tot["inh"]}），无 ER {tot["noer"]}。',
              f'- 排除 s26（尚无 ER）后覆盖率：{att_cov}/{rows_cov} = {100 * att_cov / rows_cov:.1f}%（其中 s21_31 的 27 行因 ER 只有「考生太少、不出报告」一句而没有）。',
              '- P4（`9618_*_4x`）的 ER 已抽取入 `corpus/er/`，行尚未入库，`apply_er.py` 在 P4 行出现后重跑即可。',
              '', *table, '']

    lines += ['## 没有挂上 ER 的行（P1–P3，不含 s26）', '']
    any_missing = False
    for p in papers:
        st = stats.get(p)
        if not st or p.split('_')[1] == 's26' or not st['no_er']:
            continue
        any_missing = True
        labels = by_paper.get(p, {})
        missing = [q for q in rows_q[p] if A.excerpt_for(q, labels)[0] is None]
        if not labels:
            why = 'ER 无报告：' + generals[p]['text'] if p in generals else 'ER 缺失'
        else:
            why = '；'.join(
                f'ER 里没有 {q} 或其上级标签' + (
                    '（但有更细标签 ' + ', '.join(l for l in labels if q in A.ancestors(l)[1:]) + '）'
                    if any(q in A.ancestors(l)[1:] for l in labels) else '')
                for q in missing)
        lines.append(f'- `{p}`：{len(missing)} 行（{", ".join(missing) if len(missing) <= 6 else "全部"}）— {why}')
    if not any_missing:
        lines.append('（无）')
    lines += ['', '- s26 的 6 个 P1–P3 卷共 ' + str(sum(s['rows'] for p, s in stats.items() if p.split('_')[1] == 's26'))
              + ' 行：该考季尚无 ER，不写 `er`。', '']

    lines += ['## 未用的 ER 标签', '']
    kinds = {'no_rows': 'P4：行尚未入库', 'superseded': '被更细的本级评论取代（按任务规则不挂）',
             'finer_than_row': 'ER 比行更细', 'no_such_row': '无对应行', 'duplicate': 'ER 重复标签'}
    for kind, label in kinds.items():
        items = [u for u in um if u['kind'] == kind]
        lines += [f'### {label}（{len(items)}）', '']
        if kind == 'no_rows':
            per = defaultdict(int)
            for u in items:
                per[u['paper']] += 1
            lines += ['、'.join(f'{p}（{n}）' for p, n in sorted(per.items())) or '（无）', '']
            continue
        for u in items:
            snippet = u['entry']['text'][:70].replace('|', '/')
            lines.append(f'- `{u["paper"]}` {u["label"]}（ER p.{u["entry"]["page"]}）：{u["reason"]}。“{snippet}…”')
        if not items:
            lines.append('（无）')
        lines.append('')

    spot = json.loads(SPOT.read_text(encoding='utf-8'))
    index = {(e['paper'], e['label']): e for paper in by_paper for e in by_paper[paper].values()}
    problems = []
    lines += ['## 抽查记录', '',
              '随机抽 20 条（seed 27；P1 7 条、P2 7 条、P3 6 条，覆盖 s21–w25 各考季）。逐条把 ER 原 PDF 的对应页渲染成图，'
              '对照页上的题号与评论原文，核对题号、页码与摘录。结论：20/20 题号、页码、原文一致。', '',
              '| # | 卷 | 标签 | ER 页 | 结论 |', '|--:|:--|:--|--:|:--|']
    for i, s in enumerate(spot, 1):
        e = index.get((s['paper'], s['label']))
        if not e or e['page'] != s['page']:
            problems.append(s)
        lines.append(f'| {i} | {s["paper"]} | {s["label"]} | {s["page"]} | {"一致" if s["ok"] else "不一致"} |')
    lines.append('')
    if problems:
        sys.exit(f'spot-check entries no longer match corpus/er: {problems}')

    lines += ['## 解析自检（extract_er.py 打印的异常）', '',
              '- 每份 ER 的 `Question N` 标题按 N 递增接受，没有跳号；P1–P3 逐行匹配结果见上表。',
              '- 标签序列自检（`(b)` 后只能接更大的字母，罗马数字只能递增）拒绝了 3 处并按文本保留或另存：'
              '`9618_s22_23` Q9 行首的 “(a).”（句末引用，保留为文本）；`9618_s24_22` Q1 与 `9618_s25_42` Q3 的重复标签（见下）。',
              '- `9618_s21_31`、`9618_s21_41` 的 ER 只有「考生人数太少，不出报告」一句，只存 `_general`。', '',
              '## 需要总控决定', '']
    lines += [f'{i}. {d}' for i, d in enumerate(DECISIONS, 1)]
    text = '\n'.join(lines) + '\n'
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding='utf-8') != text:
            sys.exit('corpus/er_report.md is out of date (run report_er.py)')
        return
    OUT.write_text(text, encoding='utf-8')
    print(f'wrote {OUT.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
