#!/usr/bin/env python3
"""Validate filled score sheets and print a paste-ready learning-record summary."""
from __future__ import annotations

import argparse
from collections import Counter
import csv
from pathlib import Path
import re

if __package__ in (None, ''):
    from make_mock import FIELDS, ROOT, load_paper
else:
    from .make_mock import FIELDS, ROOT, load_paper


def integer(value: str, label: str) -> int:
    if not re.fullmatch(r'\d+', value.strip()):
        raise ValueError(f'{label} 必须填非负整数（未得分填 0；空白不能视为 0）')
    return int(value)


def known_skills(root: Path) -> set[str]:
    import json
    return {t['tag'] for path in (root / 'papers').glob('p*/skill_tags.json')
            for t in json.loads(path.read_text(encoding='utf-8')).get('tags', [])}


def score_sheet(path: Path, root: Path = ROOT) -> dict:
    with path.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != FIELDS:
            raise ValueError(f'CSV 列应为：{",".join(FIELDS)}')
        scores = list(reader)
    if not scores or any(None in s or any(v is None for v in s.values()) for s in scores):
        raise ValueError('CSV 为空或列数不完整')
    papers = {s['row_id'].split(':')[0] for s in scores}
    if len(papers) != 1:
        raise ValueError('每个 score.csv 必须只含一份卷')
    paper = papers.pop()
    _, corpus = load_paper(paper, root)
    expected = {r['id']: r for r in corpus}
    ids = [s['row_id'] for s in scores]
    if len(ids) != len(set(ids)) or set(ids) != set(expected):
        raise ValueError('小问行缺失、重复或不属于本卷')
    types, skills = Counter(), Counter()
    awarded = 0
    vocabulary = known_skills(root)
    notes = []
    for score in scores:
        row = expected[score['row_id']]
        label = row['id']
        if integer(score['marks_available'], label + ' marks_available') != row['marks']:
            raise ValueError(f'{label} 分值被修改，应为 {row["marks"]}')
        mark = integer(score['marks_awarded'], label + ' marks_awarded')
        if mark > min(row['marks'], row.get('ms_max', row['marks'])):
            raise ValueError(f'{label} 得分超过小问分值或 MS 上限')
        lost = row['marks'] - mark
        awarded += mark
        types[row.get('types', {}).get('primary') or '未标注'] += lost
        allocations = {}
        for entry in score['lost_skills'].split(';'):
            if not entry.strip():
                continue
            match = re.fullmatch(r'\s*([a-z0-9]+(?:-[a-z0-9]+)*)\s*=\s*(\d+)\s*', entry)
            if not match or match[1] not in vocabulary:
                raise ValueError(f'{label} lost_skills 须写已知 tag=失分数，以分号分隔')
            tag, count = match[1], int(match[2])
            if tag in allocations or count <= 0:
                raise ValueError(f'{label} 技能重复或失分数不是正整数')
            allocations[tag] = count
        if sum(allocations.values()) > lost:
            raise ValueError(f'{label} 技能归因分数超过实际失分 {lost}')
        skills.update(allocations)
        skills['未归因'] += lost - sum(allocations.values())
        if score['note'].strip():
            notes.append(f'{row["q"]}：{score["note"].strip()}')
    return {'paper': paper, 'available': sum(r['marks'] for r in corpus),
            'awarded': awarded, 'types': dict(types), 'skills': dict(skills), 'notes': notes}


def read_thresholds(folder: Path, filename: str) -> list[dict]:
    path = folder / filename
    if not path.exists():
        return []
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def latest(rows: list[dict]) -> tuple[str, list[dict]]:
    def key(row):
        return int(row['year']), {'s': 0, 'w': 1}[row['session']]
    newest = max(key(r) for r in rows)
    found = [r for r in rows if key(r) == newest]
    return f'{found[0]["session"]}{found[0]["year"]}', found


def no_grade(reason: str) -> dict:
    return {'grade': None, 'reason': reason}


def grade_at(score: int, row: dict, grades: list[str]) -> str:
    limits = [integer(row[g], f'{g} 分数线') for g in grades]
    if limits != sorted(limits, reverse=True):
        raise ValueError('分数线等级顺序有误')
    return next((g for g, limit in zip(grades, limits) if score >= limit), 'U')


def estimate_component(component: str, score: int, maximum: int,
                       folder: Path = ROOT / 'corpus/thresholds') -> dict:
    rows = read_thresholds(folder, 'components.csv')
    if not rows:
        return no_grade('待 T40 components.csv 合并；当前仅汇总原始分')
    season, recent = latest(rows)
    matches = [r for r in recent if r['component'] == component]
    if len(matches) != 1:
        return no_grade(f'{season} 无唯一 component {component} 分数线，不借用其他 variant')
    row = matches[0]
    if int(row['max_raw']) != maximum:
        return no_grade('试卷满分与分数线表不符')
    grade = grade_at(score, row, list('ABCDE'))
    return {'grade': grade, 'season': season, 'component': component,
            'source': str(folder / 'components.csv'),
            'pdf': f'9618_{season[0]}{season[-2:]}_gt.pdf'}


def estimate_option(results: list[dict], folder: Path = ROOT / 'corpus/thresholds',
                    option: str | None = None) -> dict:
    components = [r['paper'].rsplit('_', 1)[1] for r in results]
    if len(results) != 4 or {c[0] for c in components} != set('1234'):
        return no_grade('全 A Level 估分需要 P1–P4 各一份；不混用重复 component')
    rows = read_thresholds(folder, 'options.csv')
    if not rows:
        return no_grade('待 T40 options.csv 合并；当前仅汇总四卷原始分')
    season, recent = latest(rows)
    matches = [r for r in recent if sorted(r['components'].split(';')) == sorted(components)
               and (option is None or r['option'] == option)]
    if len(matches) != 1:
        return no_grade(f'{season} 无唯一匹配 option（{";".join(components)}）；必要时指定 --option')
    row = matches[0]
    # Four equal 75-mark papers each contribute 25%: syllabus 2027–2029 p.11.
    # Only the direct four-paper, 300-mark route is supported, not carry-forward.
    if any(r['available'] != 75 for r in results) or int(row['max_weighted']) != 300:
        return no_grade('加权未确认：仅支持四份 75 分卷对应满分 300 的直接四卷 option')
    score = sum(r['awarded'] for r in results)
    return {'grade': grade_at(score, row, ['A*', *'ABCDE']), 'season': season,
            'option': row['option'], 'weighted': score,
            'source': str(folder / 'options.csv'),
            'pdf': f'9618_{season[0]}{season[-2:]}_gt.pdf'}


def describe(estimate: dict) -> str:
    if estimate['grade'] is None:
        return f'等级占位：{estimate["reason"]}'
    route = estimate.get('option') or estimate['component']
    return (f'参考等级 {estimate["grade"]}（{estimate["season"]}，{route}；'
            f'{estimate["source"]}；原件 {estimate["pdf"]}）。'
            '仅按历史分数线估计，不是本次考试正式等级。')


def summarize(results: list[dict], folder: Path = ROOT / 'corpus/thresholds',
              option: str | None = None) -> str:
    papers = [r['paper'] for r in results]
    if len(papers) != len(set(papers)):
        raise ValueError('不能重复提交同一份卷')
    types, skills = Counter(), Counter()
    lines = ['模考批改摘要（可贴入学习记录）', '']
    for result in results:
        component = result['paper'].rsplit('_', 1)[1]
        estimate = estimate_component(component, result['awarded'], result['available'], folder)
        lines += [f"- {result['paper']}：{result['awarded']}/{result['available']}，"
                  f"失分 {result['available'] - result['awarded']}。{describe(estimate)}"]
        types.update(result['types'])
        skills.update(result['skills'])
    if len(results) > 1 or option:
        lines += ['', f"合计：{sum(r['awarded'] for r in results)}/{sum(r['available'] for r in results)}。"
                  + describe(estimate_option(results, folder, option))]
    for label, counts in [('按主题型失分', types), ('按技能失分', skills)]:
        detail = '；'.join(f'{tag} {count} 分' for tag, count in counts.most_common() if count)
        lines += ['', label + '：' + (detail or '无失分') + '。']
    lines += ['', '技能失分仅统计手填 tag=分数；未归因不自动分摊；每个失分只归入一个技能。'
              '主题型仅计 primary，不重复累计副题型。']
    notes = [f'{r["paper"]} {note}' for r in results for note in r['notes']]
    if notes:
        lines += ['', '批改备注：', *[f'- {note}' for note in notes]]
    return '\n'.join(lines) + '\n'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('scores', nargs='+', type=Path, help='一份或四份已填 score.csv')
    parser.add_argument('--thresholds', type=Path, default=ROOT / 'corpus/thresholds')
    parser.add_argument('--option', help='四卷组合对应 option；默认按 components 精确匹配')
    args = parser.parse_args()
    try:
        print(summarize([score_sheet(p) for p in args.scores], args.thresholds, args.option), end='')
    except (ValueError, OSError, KeyError) as exc:
        parser.exit(2, f'错误：{exc}\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
