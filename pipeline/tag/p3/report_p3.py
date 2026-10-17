#!/usr/bin/env python3
"""Rebuild the P3 report; only this post-freeze step reads pilot inputs."""
import csv
import hashlib
import json
from collections import Counter
from workbench import ROOT, HERE, rows, records, duplicates, norm
from apply_p3 import index_records
from check_p3 import load_skills


def boundary(record):
    return record['ms_max'], [(norm(p['text']), p['marks']) for p in record['markpoints']]


def cell(value):
    return str(value).replace('|', '∣').replace('\n', ' ')


def main():
    manifest = json.loads((HERE / 'blind/manifest.json').read_text())
    for name, digest in manifest['sha256'].items():
        if hashlib.sha256((HERE / 'blind' / name).read_bytes()).hexdigest() != digest:
            raise ValueError('blind snapshot changed: ' + name)
    data = rows()
    inherited = duplicates(data)
    verified = {rid: r for rid, r in data.items() if not r['extension'] and rid not in inherited}
    tags = index_records(records(HERE / 'p3_tags.jsonl'))
    points = index_records(records(HERE / 'p3_markpoints.jsonl'))
    blind = index_records(records(HERE / 'blind/p3_tags.jsonl'))
    blind_points = index_records(records(HERE / 'blind/p3_markpoints.jsonl'))
    pilot = list(csv.DictReader((ROOT / 'papers/p3/pilot_tags.csv').open(encoding='utf-8-sig')))
    pilot_points = records(ROOT / 'papers/p3/pilot_markpoints.jsonl')
    reviews = json.loads((HERE / 'pilot_review.json').read_text())
    decisions = {(r['id'], r['n']): r for r in reviews['skill_decisions']}
    agreement = sum(t['primary'] == blind[t['id']]['primary'] for t in pilot)
    crosses = sum(set(filter(None, t['cross'].split(';'))) == set(blind[t['id']]['cross']) for t in pilot)
    split_agreement = sum(boundary(t) == boundary(blind_points[t['id']]) for t in pilot_points)
    low = [t for t in tags.values() if t['confidence'] == 'low']
    if tags != blind:
        raise ValueError('post-pilot type changes must be separately reviewed')
    for rid, p in points.items():
        if boundary(p) != boundary(blind_points[rid]):
            raise ValueError('post-pilot split changed: ' + rid)
    counts = Counter(tags[rid]['primary'] for rid in verified)
    marks = Counter()
    for rid, row in verified.items():
        marks[tags[rid]['primary']] += row['marks']
    taxonomy = json.loads((ROOT / 'papers/p3/taxonomy.json').read_text())['types']
    split_unique = [rid for rid in points if rid not in inherited]
    vpoints = {rid: p for rid, p in points.items() if rid in verified}
    freq = Counter(s for p in points.values() for m in p['markpoints'] for s in m['skills'])
    vf = Counter(s for p in vpoints.values() for m in p['markpoints'] for s in m['skills'])
    lines = ['# P3 全量标注与得分点拆分报告', '', '## 覆盖与证据', '',
             f'- 全部 {len(data)} 行均有主题型；独立行 {len(data)-len(inherited)}，D35/equivalent_of 继承行 {len(inherited)}。',
             f'- 统计口径：2022–2026s 核验语料、包含 s26、排除 extension=true 与全部继承行；共 {len(verified)} 行、{sum(r["marks"] for r in verified.values())} 分。题型计数只按 primary，cross 不重复计分。',
             f'- 拆分 {len(points)} 行、{sum(len(p["markpoints"]) for p in points.values())} 条；去除继承后 {len(split_unique)} 行；核验去重 {len(vpoints)} 行、{sum(len(p["markpoints"]) for p in vpoints.values())} 条。ms_max 限制候选得分点总分，条数不等于可获分数。',
             f'- low {len(low)} 行（{len(low)/len(data):.2%}），均为一题及其重复行；核验去重语料无 low。',
             '- 盲标快照先于任何 pilot 读取冻结并提交（f8ea20a）；blind/manifest.json 记录两个真源 SHA256、输入文件散列及源版本，report_p3.py 会拒绝被改过的快照。最终主题型、cross、切分、text、marks、ms_max 均与盲标相同，仅复核了 skills。',
             '- 只读对应行自己的 QP/MS；独立 has_figure 行的 QP 起始页，以及全部 BL 与拆分候选的 MS 原页均已目视核对。页单见 render_manifest_*.json 与 review_log.json；9618_s21_31:8(b) 的 QP p.11 及 9618_w25_32:10 的 QP p.11 另查续页。',
             '- 真源为 p3_tags.jsonl / p3_markpoints.jsonl；compile_tags.py 与 compile_markpoints.py 可由人工判定与原文映射重建。check_p3.py 检查覆盖、题型、词表、分值、原文子串、豁免与继承；apply_p3.py 只合并五个授权字段，audit_merge.py 对比其余字段的原始 JSON 字节。', '',
             '## 与 pilot 的盲标比较', '',
             f'- 主题型 {agreement}/{len(pilot)} = {agreement/len(pilot):.2%}；cross 集合 {crosses}/{len(pilot)} = {crosses/len(pilot):.2%}。无主题型或副题型分歧。',
             f'- 得分点切分 {split_agreement}/{len(pilot_points)} = {split_agreement/len(pilot_points):.2%}，覆盖 {sum(len(p["markpoints"]) for p in pilot_points)} 条。比较有序的压缩空白 text、marks 与 ms_max，无切分分歧。',
             '- 技能比较按集合进行，标签顺序差异不算分歧。下表逐条列出全部分歧、原页复核结论与最终技能。', '',
             '| 行 / MP | pilot 技能 | 盲标技能 | 最终技能 | 原页复核 |', '|:--|:--|:--|:--|:--|']
    diffs = 0
    for p in pilot_points:
        for a, b in zip(p['markpoints'], blind_points[p['id']]['markpoints']):
            if set(a['skills']) == set(b['skills']):
                continue
            diffs += 1
            decision = decisions[(p['id'], a['n'])]
            final = points[p['id']]['markpoints'][a['n'] - 1]['skills']
            lines.append('| ' + ' | '.join(map(cell, [f'{p["id"]} / {a["n"]}', ', '.join(a['skills']), ', '.join(b['skills']), ', '.join(final), f'MS p.{decision["page"]}：{decision["decision"]}'])) + ' |')
    lines += ['', f'共 {diffs} 条技能集合分歧；skill_decisions 与同构项一致性修订见 pilot_review.json。',
              '同构修订：9618_s21_31:2(c) MP2、9618_s23_32:6(a) MP2 补 record-type；9618_s21_31:8(b) 与 9618_s26_31:10(a) 的内层循环补 nested-loops，下标更新使用 array-index，避免误当累计计数。继承行同步更新。', '',
              '## 核验语料题型统计（去重）', '', '| 题型 | 名称 | 行数 | 分值 |', '|:--|:--|--:|--:|']
    for t in taxonomy:
        lines.append(f'| {t["code"]} | {t["name_zh"]} | {counts[t["code"]]} | {marks[t["code"]]} |')
    lines += ['', f'合计：{sum(counts.values())} 行、{sum(marks.values())} 分。', '', '## 技能频次', '',
              '单位为使用该技能的得分点条数；全部语料列含扩展与继承，核验去重列排除扩展与继承。0 仅表示本次拆分未使用。', '',
              '| 技能 | 全部语料 | 核验去重 |', '|:--|--:|--:|']
    for skill in sorted(load_skills(ROOT / 'papers/p3/skill_tags.json')):
        lines.append(f'| {skill} | {freq[skill]} | {vf[skill]} |')
    lines += ['', '## low 清单', '', '| 行 | 主题型 | 理由 |', '|:--|:--|:--|']
    for t in low:
        lines.append(f'| {t["id"]} | {t["primary"]} | {t["note"]} |')
    lines += ['', '## 核验语料不足两次的题型', '', '| 题型 | 名称 | 去重行数 |', '|:--|:--|--:|']
    for t in taxonomy:
        if counts[t['code']] < 2:
            lines.append(f'| {t["code"]} | {t["name_zh"]} | {counts[t["code"]]} |')
    lines += ['', '## 拆分豁免与边界记录', '', '| 行 | 依据 |', '|:--|:--|']
    for e in records(HERE / 'split_exemptions.jsonl'):
        lines.append(f'| {e["id"]} | {e["reason"]} |')
    lines += ['', '- 9618_s22_32:8(a)：MS p.8 只列四条填空片段，并未给完整代码。与 QP p.11 四个留空行一一对应，按原文片段拆四点，不补出 MS 不存在的整行。指南 §8.2 B 未明确覆盖这种简写，已在 tag_note 说明。',
              '- 9618_w23_32:12(b)：SEEK 行有两处空，MS 按 blank 给分，合并为 2 分；9618_s24_31:10(b) 与 9618_s24_33:10(b) 的 WHILE 两处空按 completed line 合并为 1 分。',
              '- 9618_s24_33:10(b) 虽不属于 D35 的逐字重复行，但本卷 QP/MS 独立核验后，五条对应答案与 _31 相同；仅复用内容完全相同的映射。',
              '- 布尔表达式上划线只用于原页判型，不改抽取原文；所有得分点 text 仍是该行 ms_text 压缩空白后的子串。', '',
              '## 需要总控决定', '',
              '- 9618_s21_31:3(a)（及重复行）：SY-04 与 SY-03 各占两条连线，SY-02 占一条。暂取 SY-04，cross 为 SY-03、SY-02，low；请裁决并补清 §7.18 的同票规则。',
              '- 9618_s22_32:1(b)(iii)：DR-02 summary 把枚举字段赋值收入，但 DR-04 summary/not 与指南 §7.4 又将字段赋值归 DR-04。此处按直接产出取 DR-04，建议统一 taxonomy 边界措辞。',
              '- 9618_s22_32:8(a)：建议 §8.2 B 明确“MS 仅提供填空答案片段”可按 QP 留空行逐一映射且保留片段，不强行拼出非 MS 子串的整行。',
              '- 无建议新增的题型或技能标签；P3 词表 extends P2 已满足本次标注需要。共享文件及 P2 apply 未改。', '']
    (ROOT / 'corpus/tag_report_p3.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f'primary {agreement}/{len(pilot)}; split {split_agreement}/{len(pilot_points)}; '
          f'skill differences {diffs}; verified unique {len(verified)} rows')


if __name__ == '__main__':
    main()
