#!/usr/bin/env python3
"""Generate an after-exam marking kit using only the selected paper's corpus rows."""
from __future__ import annotations

import argparse
import csv
import html
import json
import os
from pathlib import Path
import re
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[2]
SOURCES = Path('/Users/zhangheqing/Desktop/alevel cs/sources')
FIELDS = ['row_id', 'marks_available', 'marks_awarded', 'lost_skills', 'note']
# Official 2027–2029 syllabus p.11; also checked against s26 QP cover pages.
MINUTES = {1: 90, 2: 120, 3: 90, 4: 150}
ER_NOTICE = '仅供易错参考，不是给分依据'


def load_paper(paper: str, root: Path = ROOT) -> tuple[dict, list[dict]]:
    if not re.fullmatch(r'9618_[sw]\d{2}_[1-4][1-3]', paper):
        raise ValueError(f'无效卷 id：{paper}')
    with (root / 'corpus/inventory.csv').open(encoding='utf-8-sig', newline='') as f:
        entries = [r for r in csv.DictReader(f) if r['paper'] == paper]
    if len(entries) != 1:
        raise ValueError(f'资料清单没有唯一匹配：{paper}')
    info = entries[0]
    if not info['qp'] or not info['ms']:
        raise ValueError('缺少本卷 QP / MS 配对')
    prefix, component = paper.rsplit('_', 1)
    for kind in ('qp', 'ms'):
        if info[kind] != f'{prefix}_{kind}_{component}.pdf':
            raise ValueError(f'{kind} 不是同季同年同 variant 的配对')
    path = root / f'corpus/rows/p{component[0]}/{paper}.jsonl'
    rows = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]
    if not rows or len({r['id'] for r in rows}) != len(rows):
        raise ValueError('小问为空或 id 重复')
    if any(r['paper'] != paper or not r['id'].startswith(paper + ':') for r in rows):
        raise ValueError('小问行与本卷不一致')
    if sum(r['marks'] for r in rows) != int(info['total_marks']):
        raise ValueError('小问分值合计与 inventory 不一致')
    if any(not r['ms_text'].strip() for r in rows):
        raise ValueError('小问缺少 MS 原文，不能生成批改包')
    return info, rows


def fenced(text: str) -> str:
    longest = max((len(s) for s in re.findall(r'`+', text)), default=0)
    fence = '`' * max(3, longest + 1)
    return f'{fence}text\n{text}\n{fence}'


def table_cell(text: str) -> str:
    return html.escape(text).replace('|', '&#124;').replace('\n', '<br>')


def card_link(row: dict, output_dir: Path, root: Path) -> tuple[str, str]:
    primary = row.get('types', {}).get('primary')
    if not primary:
        return '未标注', '未标注'
    n = row['component']
    target = root / f'output/p{n}/P{n}题型手册.html'
    href = quote(Path(os.path.relpath(target, output_dir)).as_posix(), safe='/') + '#' + primary
    return f'[{primary}]({href})', f'<a href="{html.escape(href, quote=True)}">{primary}</a>'


def generate(paper: str, out: Path | None = None, root: Path = ROOT,
             sources: Path | None = None) -> Path:
    info, rows = load_paper(paper, root)
    directory = (out if out is not None else root / 'output/mock') / paper
    source_root = sources or Path(os.environ.get('ALEVEL_CS_SOURCES', SOURCES))
    for protected in (source_root, SOURCES, root / 'sources'):
        if directory.resolve().is_relative_to(protected.resolve()):
            raise ValueError('sources/ 为只读，不能作为输出目录')
    if (directory / 'score.csv').exists():
        raise FileExistsError(f'{directory}/score.csv 已存在；保留批改记录，请指定新的 --out')
    source_dir = source_root / 'pastpapers'
    n = int(info['component'])
    title = f'{paper} 整卷模考批改包'
    md = [f'# {title}', '',
          f"考试时长：{MINUTES[n]} 分钟；总分：{info['total_marks']} 分。", '',
          '本包仅在完成限时模考后打开。给分只认本卷对应小问的 MS；不根据 ER 给分。', '',
          '## 材料与批改步骤', '']
    body = [f'<h1>{title}</h1>', f'<p>考试时长：{MINUTES[n]} 分钟；总分：{info["total_marks"]} 分。</p>',
            '<p>本包仅在完成限时模考后打开。给分只认本卷对应小问的 MS；不根据 ER 给分。</p>',
            '<h2>材料与批改步骤</h2>', '<ul>']
    for key, label in [('qp', 'QP 原卷'), ('ms', 'MS 本卷评分方案'), ('in', 'P2 插页'), ('sf', 'P4 源文件目录')]:
        if info.get(key):
            path = source_dir / info[key]
            md.append(f'- {label}：`{path}`')
            body.append(f'<li>{label}：<code>{html.escape(str(path))}</code></li>')
    steps = ('先按 MS 逐点核对；有图、表或代码排版时回看原始 PDF，抽取文本不能替代原页。'
             '勾选表仅作记录，按 MS 的 Max / 或选关系计算，不机械相加；总分不得超过小问分值。'
             '在 score.csv 填 marks_awarded（未得分填 0，空白表示未批改）；'
             'lost_skills 可填 tag=失分数，以分号分隔；不确定的技能留空，记入未归因。')
    md += ['', steps, '', 'MS 页码和 QP 页码均为 PDF 页码（从 1 起）。手册链接仅用于批改后复习；先运行 make build。', '']
    body += ['</ul>', f'<p>{steps}</p>', '<p>MS / QP 页码均从 PDF 第 1 页起算。手册链接用于批改后复习；先运行 make build。</p>']
    for row in rows:
        link_md, link_html = card_link(row, directory, root)
        heading = f"{row['q']} · {row['marks']} 分"
        md += [f'## {heading}', '', f'主题型：{link_md}', '', f"本题 MS：`{source_dir / info['ms']}` p.{row['ms_page']}", '']
        body += [f'<section><h2>{heading}</h2>', f'<p>主题型：{link_html}</p>',
                 f'<p>本题 MS：<code>{html.escape(str(source_dir / info["ms"]))}</code> p.{row["ms_page"]}</p>']
        if row['has_figure']:
            warning = f"对照 QP p.{row['qp_page']}（图、表或代码）；同时核对 MS 原页的图形与排版。"
            md += [warning, '']
            body.append(f'<p class="notice">{warning}</p>')
        if row.get('flags'):
            warning = '语料核对标记：' + ', '.join(row['flags']) + '；有疑问以原页为准。'
            md += [warning, '']
            body.append(f'<p>{html.escape(warning)}</p>')
        md += ['### 本题 MS 原文（给分依据）', '', fenced(row['ms_text']), '']
        body += ['<h3>本题 MS 原文（给分依据）</h3>', f'<pre>{html.escape(row["ms_text"])}</pre>']
        if row.get('markpoints'):
            md += ['### 得分点勾选表', '', '| MP | MS 原文 | 分值 | 技能标签 | ✓✗ |', '| :-- | :-- | --: | :-- | :-- |']
            body += ['<h3>得分点勾选表</h3><table><thead><tr><th>MP</th><th>MS 原文</th><th>分值</th><th>技能标签</th><th>✓✗</th></tr></thead><tbody>']
            for point in row['markpoints']:
                skills = '; '.join(point['skills'])
                md.append(f"| MP{point['n']} | {table_cell(point['text'])} | {point['marks']} | {skills} | |")
                body.append(f'<tr><td>MP{point["n"]}</td><td><pre>{html.escape(point["text"])}</pre></td><td>{point["marks"]}</td><td>{skills}</td><td> </td></tr>')
            md.append('')
            body.append('</tbody></table>')
        else:
            md += ['未拆得分点：请按上方本题 MS 原文逐点批改。', '']
            body.append('<p>未拆得分点：请按上方本题 MS 原文逐点批改。</p>')
        if row.get('ms_max') is not None:
            cap = f"MS 上限：{row['ms_max']} 分；还须遵守本题 MS 中的分组上限及或选规则。"
            md += [cap, '']
            body.append(f'<p class="notice">{cap}</p>')
        if row.get('er'):
            md += [f'### 考官报告（{ER_NOTICE}）', '', f"来源：`{source_dir / info['er']}`；摘录范围按语料原样保留。", '', fenced(row['er']), '']
            body += [f'<aside><h3>考官报告（{ER_NOTICE}）</h3>',
                     f'<p>来源：<code>{html.escape(str(source_dir / info["er"]))}</code>；摘录范围按语料原样保留。</p>',
                     f'<pre>{html.escape(row["er"])}</pre></aside>']
        else:
            md += ['本小问无 ER 摘录。', '']
            body.append('<p>本小问无 ER 摘录。</p>')
        body.append('</section>')
    css = ('body{max-width:1100px;margin:2rem auto;padding:0 1rem;font:17px/1.6 system-ui,sans-serif;color:#17212b}'
           'pre{white-space:pre-wrap;overflow-wrap:anywhere;font:14px/1.5 ui-monospace,monospace;background:#f3f5f7;padding:1rem}'
           'table{width:100%;border-collapse:collapse}td,th{border:1px solid #bbc3cb;padding:.45rem;text-align:left;vertical-align:top}'
           'td pre{padding:0;margin:0;background:none}code{overflow-wrap:anywhere}.notice,aside{border-left:4px solid #bf7c13;padding-left:1rem}'
           'section{border-top:1px solid #bbc3cb;margin-top:2rem}@media print{body{font-size:11pt}h2,h3{break-after:avoid}tr{break-inside:avoid}}')
    document = f'<!doctype html>\n<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><style>{css}</style></head><body>' + '\n'.join(body) + '</body></html>\n'
    directory.mkdir(parents=True, exist_ok=True)
    # Exclusive creation protects a student's existing score, including concurrent runs.
    with (directory / 'score.csv').open('x', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(FIELDS)
        writer.writerows([r['id'], r['marks'], '', '', ''] for r in rows)
    (directory / 'marking.md').write_text('\n'.join(md), encoding='utf-8')
    (directory / 'marking.html').write_text(document, encoding='utf-8')
    return directory


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('paper', help='例如 9618_s26_22')
    parser.add_argument('--out', type=Path, help='输出父目录（其下创建卷 id 文件夹）')
    args = parser.parse_args()
    try:
        print(generate(args.paper, args.out))
    except (ValueError, OSError) as exc:
        parser.exit(2, f'错误：{exc}\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
