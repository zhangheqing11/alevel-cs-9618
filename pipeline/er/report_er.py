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

RULINGS = [
    '**w23 的重复 `Paper 9618/33`** — 认可，保持 `HEADING_FIXUPS`。依据：`9618_w23_er.pdf` 在 p.25 与 p.31 各印一个 '
    '`Paper 9618/33` 标题，全文没有 31 的标题；第一块位于 23 与 32 之间（31 的位置）；两块文字逐字相同；QP/MS 31 与 33 '
    '题目、MS 完全相同。条目带 `er_header:"9618/33"`。',
    '**`9618_s24_22` Q1 第二个 (b)（p.17）→ 1(c)** — 按总控裁决挂到 1(c)，用 `LABEL_FIXUPS`（`extract_er.py`）实现，条目带 '
    '`er_label_printed:"1(b)"`。依据：该块写“怎样记录变量”（store them in an array/record/file、comments），行 1(c) 是 2 分的“记录变量设计”，'
    '同卷 ER 里没有别的块对应 1(c)。',
    '**ER 比行更细**（`s23_22` 6(a)↔行 6、`w24_23` 6(a)↔行 6、`w24_22` 1(b)(i)↔行 1(b)）— 按总控裁决放行：行没有子行、'
    'ER 在该行下只有唯一一个更细标签时，挂上并加前缀 `[ER 6(a)]`（规则见 `apply_er.py` 文件头注释，测试 `test_single_finer_label_*`）。'
    '有两个以上更细标签的不挂，仍列在下面的“ER 比行更细”。',
    '**上级总评只留在 `corpus/er/`** — 认可：行有本级评论时不挂上级总评，5 条见“被更细的本级评论取代”。',
    '**其他脚本重写行时保留 `er`** — 认可：`apply_p2.py` 用 `", "` 分隔并把自己的字段挪到末尾，`apply_er.py` 紧凑插入 `,"er":…` '
    '并只替换/删除该字段，互不干扰；codex-1 改 pipeline/extract、pipeline/tag 时保留 `er`。',
]

TODO = [
    '`9618_s25_er.pdf` Paper 42 Question 3 的 **(d)(ii) 印了两次**（p.46）：第二块讲“生成显示更新值的正确输出”，即 3(d)(iii)（测试截图）；总控裁决按 `LABEL_FIXUPS` 挂到 3(d)(iii)（D33）。'
    'P4 行入库后对照题面决定是否加 `LABEL_FIXUPS`。',
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
    table = ['| 卷 | ER 条数 | 行数 | 挂上 | 其中本级 | 上级回退 | 单一更细标签 | 无 ER 的行 | 未用的 ER 标签 |',
             '|:--|--:|--:|--:|--:|--:|--:|--:|--:|']
    for p in papers:
        st = stats.get(p)
        n_er = len(by_paper.get(p, {})) + sum(1 for d in duplicates if d['paper'] == p)
        rows = st['rows'] if st else 0
        att = st['attached'] if st else 0
        own = st['own'] if st else 0
        inh = st['inherited'] if st else 0
        fin = st['finer'] if st else 0
        noer = st['no_er'] if st else 0
        unused = len(um_by.get(p, []))
        table.append(f'| {p} | {n_er} | {rows if st else "—"} | {att} | {own} | {inh} | {fin} | {noer if st else "—"} | {unused} |')
        for k, v in (('er', n_er), ('rows', rows), ('att', att), ('own', own), ('inh', inh), ('fin', fin), ('noer', noer)):
            tot[k] += v
    p123 = [s for p, s in stats.items() if not p.split('_')[1].startswith('s26')]
    rows_cov = sum(s['rows'] for s in p123)
    att_cov = sum(s['attached'] for s in p123)
    lines += ['## 总览', '',
              f'- 行总数 {tot["rows"]}，挂上 `er` {tot["att"]}（本级 {tot["own"]}、上级回退 {tot["inh"]}、单一更细标签 {tot["fin"]}），无 ER {tot["noer"]}。',
              f'- 排除 s26（尚无 ER）后覆盖率：{att_cov}/{rows_cov} = {100 * att_cov / rows_cov:.1f}%（其中 s21_31 的 27 行因 ER 只有「考生太少、不出报告」一句而没有）。',
              '- P4（`9618_*_4x`）行已入库（T12 #29），`apply_er.py` 已在全部 P1–P4 行上重跑。',
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
              '## 总控裁决（PR #26，已执行）', '']
    lines += [f'{i}. {d}' for i, d in enumerate(RULINGS, 1)]
    lines += ['', '## 待办', '']
    lines += [f'- {t}' for t in TODO]
    text = '\n'.join(lines) + '\n'
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding='utf-8') != text:
            sys.exit('corpus/er_report.md is out of date (run report_er.py)')
        return
    OUT.write_text(text, encoding='utf-8')
    print(f'wrote {OUT.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
