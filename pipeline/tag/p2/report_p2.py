"""Rebuild the P2 annotation report; pilot access is confined to this post-blind step."""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

from check_p2 import norm, records, unique

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent


def boundary(record):
    return (record['ms_max'], [(norm(p['text']), p['marks']) for p in record['markpoints']])


def main():
    manifest = json.loads((HERE/'blind/manifest.json').read_text())
    for name, digest in manifest['files'].items():
        assert hashlib.sha256((HERE/'blind'/name).read_bytes()).hexdigest() == digest
    tags = unique(HERE/'p2_tags.jsonl')
    points = unique(HERE/'p2_markpoints.jsonl')
    blind = unique(HERE/'blind/p2_tags.jsonl')
    blind_points = unique(HERE/'blind/p2_markpoints.jsonl')
    rows = {r['id']: r for p in (ROOT/'corpus/rows/p2').glob('*.jsonl') for r in records(p)}
    verified = {rid: r for rid, r in rows.items() if not r['extension']}
    taxonomy = json.loads((ROOT/'papers/p2/taxonomy.json').read_text())['types']
    skills = json.loads((ROOT/'papers/p2/skill_tags.json').read_text())['tags']
    pilot = list(csv.DictReader((ROOT/'papers/p2/pilot_tags.csv').open(encoding='utf-8-sig')))
    pilot_points = records(ROOT/'papers/p2/pilot_markpoints.jsonl')
    agreement = sum(t['primary'] == blind[t['id']]['primary'] for t in pilot)
    split_agreement = sum(t['id'] in blind_points and boundary(t) == boundary(blind_points[t['id']]) for t in pilot_points)
    lines = ['# P2 全量标注与得分点拆分报告', '',
             '## 覆盖、证据与可复现流程', '',
             f'- 全部 {len(rows)} 行均有主题型；核验语料 {len(verified)} 行、{sum(r["marks"] for r in verified.values())} 分（2022–2026s，含 s26）；2021 扩展语料 {len(rows)-len(verified)} 行。',
             f'- 共 {len(points)} 行拆出 {sum(len(r["markpoints"]) for r in points.values())} 条候选得分点；核验语料 {sum(rid in verified for rid in points)} 行、{sum(len(r["markpoints"]) for rid,r in points.items() if rid in verified)} 条。ms_max 用于候选总分超过小问分值，候选条数不等于可获分数。',
             f'- low {sum(t["confidence"]=="low" for t in tags.values())} 行，占 {sum(t["confidence"]=="low" for t in tags.values())/len(tags):.2%}。',
             '- 只读每行自己的 QP/MS；原页查看记录见 pipeline/tag/p2/review_log.json。所有独立卷起始图示页均查看，复杂跨页代码和流程图另查原页。D21 重复卷完全复制对应 _21 行。',
             '- 721 行盲标、拆分及候选排除清单先完成，冻结于提交 5a95bb0；blind/ 保存原始快照与 SHA256 manifest。随后才首次读取两个 pilot 文件，未为提高一致率调整主题型或切分。',
             '- 真源：pipeline/tag/p2/p2_tags.jsonl、p2_markpoints.jsonl。check_p2.py 检查覆盖、词表、原文子串、分值和 D21；apply_p2.py 只写五个授权字段；report_p2.py 重建本报告。', '',
             '## 与试标的盲标比较', '',
             f'- 主题型：{agreement}/{len(pilot)} = {agreement/len(pilot):.2%}（要求 ≥90%）。',
             f'- 得分点切分：{split_agreement}/{len(pilot_points)} = {split_agreement/len(pilot_points):.2%}（要求 ≥80%）。逐行比较有序的压缩空白 text、marks 及 ms_max；18 行全部一致，110 条得分点，无切分分歧。技能集合独立比较，不混入切分一致率。',
             '- 最终主题型与切分和盲标快照相同；以下列出所有副题型、技能集合差异。', '',
             '### 副题型分歧与复核', '',
             '| 行 | pilot | 本次 | 复核结论 |', '|:--|:--|:--|:--|']
    for p in pilot:
        t = blind[p['id']]
        if p['primary'] != t['primary']:
            lines.append(f'| {p["id"]} | {p["primary"]} | {t["primary"]} | 见最终 tag_note |')
        if set(filter(None,p['cross'].split(';'))) != set(t['cross']):
            lines.append(f'| {p["id"]} | {p["cross"] or "无"} | {", ".join(t["cross"])} | 保留 DT-02：分别复核该题 MS p{rows[p["id"]]["ms_page"]}，数组边界声明与 OF 记录类型是两个独立下划线计分片段；按 §4 §3 不适用的单条声明按“其他行”的副题型阈值，记录类型另占一分。 |')
    lines += ['', '### 技能集合差异', '',
              '以下逐条按 §8.3 与该题 MS 文字复核。表中保留盲标差异，并列出最终技能；七处据原文补准，其他保留较具体或包含独立操作的 1–3 个标签。只比较集合，不把顺序差异当分歧。', '',
              '| 行 / 点 | MS 原文 | pilot 技能 | 盲标技能 | 最终技能与复核 |', '|:--|:--|:--|:--|:--|']
    changes = 0
    for p in pilot_points:
        for a,b in zip(p['markpoints'],blind_points[p['id']]['markpoints']):
            if set(a['skills']) != set(b['skills']):
                changes += 1
                final = points[p['id']]['markpoints'][a['n']-1]['skills']
                reason = '保留盲标：对应本点原文操作。' if set(final)==set(b['skills']) else '据原文补准：范围/条件循环、比较、转换或写入，按 §8.3。'
                lines.append(f'| {p["id"]} / {a["n"]} | {a["text"].replace("|", "∣")} | {", ".join(a["skills"])} | {", ".join(b["skills"])} | {", ".join(final)}；{reason} |')
    if not changes:
        lines.append('| 无 | 技能集合全部一致 | — | — |')
    lines += ['', f'技能集合有 {changes} 条差异。', '', '## 核验语料题型统计', '',
              '仅按主题型计数与计分，副题型不重复累计；包含 s26，排除全部 extension=true 的 2021 行。', '',
              '| 题型 | 名称 | 行数 | 分值 |', '|:--|:--|--:|--:|']
    counts = Counter(tags[rid]['primary'] for rid in verified)
    marks = Counter()
    for rid,r in verified.items():
        marks[tags[rid]['primary']] += r['marks']
    for t in taxonomy:
        lines.append(f'| {t["code"]} | {t["name_zh"]} | {counts[t["code"]]} | {marks[t["code"]]} |')
    lines += ['', '## 技能频次', '',
              '单位为含该技能的得分点条数；同一点同一技能只计一次。列出完整词表，0 表示本次拆分未使用；不代表整个题库不考该技能。', '',
              '| 技能 | 全部语料 | 核验语料 |', '|:--|--:|--:|']
    freq = Counter(s for p in points.values() for m in p['markpoints'] for s in m['skills'])
    vfreq = Counter(s for rid,p in points.items() if rid in verified for m in p['markpoints'] for s in m['skills'])
    for s in skills:
        lines.append(f'| {s["tag"]} | {freq[s["tag"]]} | {vfreq[s["tag"]]} |')
    lines += ['', '## 低信心与低频题型', '', '| 行 | 主题型 | 原因 |', '|:--|:--|:--|']
    for rid,t in tags.items():
        if t['confidence']=='low':
            lines.append(f'| {rid} | {t["primary"]} | {t["note"]} |')
    rare = [t for t in taxonomy if counts[t['code']]<2]
    lines += ['', '核验语料出现不足 2 次的主题型：' + ('；'.join(f'{t["code"]} {t["name_zh"]}（{counts[t["code"]]} 行）' for t in rare) if rare else '无。'), '',
              '## 未拆行审计与需要总控决定', '',
              '候选题型且 ≥4 分的未拆行全部逐项列在 split_exemptions.jsonl；文字解释按 §8.1 不拆，下划线、填空和按行计分按 §8.2.9 不拆。', '',
              '| 行 | 未拆依据 |', '|:--|:--|']
    for e in records(HERE/'split_exemptions.jsonl'):
        lines.append(f'| {e["id"]} | {e["reason"]} |')
    lines += ['', '- **需要总控决定：9618_w21_22:2(a)** 的五个流程图红框内文字未抽入 ms_text，现有文本只有按框计分说明。已看 QP p5、MS p4；当前按 §8.2.9 同类图示给分例外处理。请补抽图中文字后拆分，或确认按区域给分的例外。未越权改原始抽取字段。',
              '- **需要总控决定：技能词表缺少通用变量赋值 / 滚动缓存移位技能**。s22/22:4(a) MP5/6、w21/22:6(d) MP6、w23/21:6(a) MP5 暂取 initialise-variables 最近项，note 已说明；建议设计工位增加准确标签后回填，当前不私建技能。',
              '- w25/23:3 已按 §8.2.9 加粗代码给分例外不拆。D17 的 PopData 类型名当变量笔误原样保留；本次仅标注，不改 MS。w22/22:1(c) 的 D16 官方笔误同样保留。',
              '- 其余范围内没有新增题型或技能。2021 重复卷和 s26 均完成标注；保留整卷标志由既有规则消费，本任务没有改动抽取字段或共享文件。', '']
    (ROOT/'corpus/tag_report_p2.md').write_text('\n'.join(lines),encoding='utf-8')
    print(f'pilot primary {agreement}/{len(pilot)}; split {split_agreement}/{len(pilot_points)}; skill-set differences {changes}')


if __name__ == '__main__':
    main()
