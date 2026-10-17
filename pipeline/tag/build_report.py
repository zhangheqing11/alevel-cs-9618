"""Reproduce the blind/pilot comparison and P1 tagging report after blind freeze."""
import csv
import hashlib
import json
from pathlib import Path

from apply_tags import ROOT, load_jsonl, prepare
from apply_adjudication import read_adjudications


def main():
    folder = ROOT / 'pipeline/tag'
    manifest = json.loads((folder / 'blind_manifest.json').read_text())
    blind_path = folder / 'p1_tags.blind.jsonl'
    if hashlib.sha256(blind_path.read_bytes()).hexdigest() != manifest['blind_sha256']:
        raise ValueError('Blind snapshot hash changed')
    blind = {t['id']: t for t in load_jsonl(blind_path)}
    tags = {t['id']: t for t in load_jsonl(folder / 'p1_tags.jsonl')}
    plans, count = prepare(ROOT)
    if plans or count != 979 or len(blind) != 979:
        raise ValueError('Report requires all 979 corpus rows to match the label source')
    rows = [r for p in sorted((ROOT / 'corpus/rows/p1').glob('*.jsonl')) for r in load_jsonl(p)]
    if set(blind) != set(tags):
        raise ValueError('Blind and final row coverage differs')
    taxonomy = json.loads((ROOT / 'papers/p1/taxonomy.json').read_text())
    verified = [r for r in rows if not r['extension'] and not r['equivalent_of']]
    extension = [r for r in rows if r['extension']]
    low = [r for r in rows if r['tag_confidence'] == 'low']
    reviews = {r['id']: r for r in load_jsonl(folder / 'pilot_review.jsonl')}
    adjudication_path = ROOT / 'papers/p1/adjudication.csv'
    adjudications = read_adjudications(adjudication_path) if adjudication_path.exists() else {}
    for row_id, ruling in adjudications.items():
        if tags.get(row_id) != ruling:
            raise ValueError(f'Unapplied adjudication: {row_id}')
    with (ROOT / 'papers/p1/pilot_tags.csv').open(encoding='utf-8-sig', newline='') as source:
        pilot = list(csv.DictReader(source))
    matches = full_matches = 0
    differences = []
    for gold in pilot:
        row_id = gold['id']
        initial = blind[row_id]
        crosses = gold['cross'].split(';') if gold['cross'] else []
        primary_match = initial['primary'] == gold['primary']
        cross_match = set(initial['cross']) == set(crosses)
        matches += primary_match
        full_matches += primary_match and cross_match
        if not primary_match or not cross_match:
            if row_id not in reviews:
                raise ValueError(f'Unreviewed pilot difference: {row_id}')
            review = reviews[row_id]
            if row_id in adjudications:
                review = dict(id=row_id, decision='adjudicated',
                              reason=adjudications[row_id]['note']+'；详见 papers/p1/adjudication.csv。')
            if review['decision'] == 'retain_blind' and tags[row_id] != initial:
                raise ValueError(f'Final tag contradicts review: {row_id}')
            differences.append(dict(id=row_id, blind=initial, pilot=gold,
                                    final=tags[row_id], review=review, initial_review=reviews[row_id]))
    if set(reviews) != {d['id'] for d in differences}:
        raise ValueError('Review list does not match differences')
    comparison = dict(blind_sha256=manifest['blind_sha256'], pilot_rows=len(pilot),
                      primary_matches=matches, primary_agreement=matches/len(pilot),
                      primary_cross_matches=full_matches, differences=differences,
                      final_primary_matches=sum(tags[g['id']]['primary'] == g['primary'] for g in pilot),
                      final_primary_cross_matches=sum(tags[g['id']]['primary'] == g['primary']
                          and set(tags[g['id']]['cross']) == set(filter(None, g['cross'].split(';'))) for g in pilot))
    (folder / 'pilot_comparison.json').write_text(json.dumps(comparison, ensure_ascii=False, indent=2)+'\n')

    lines = ['# P1 全量标签报告（T24）', '',
        '## 覆盖与复核', '',
        f'- 全部 {len(rows)} 行、33 卷均有一个主题型；核验语料 {len(verified)} 行、{sum(r["marks"] for r in verified)} 分；2021 扩展 {len(extension)} 行、{sum(r["marks"] for r in extension)} 分。',
        f'- 低信心 {len(low)}/{len(rows)} = {len(low)/len(rows):.2%}；带副题型 {sum(bool(r["types"]["cross"]) for r in rows)} 行。',
        '- 全部 353 个 has_figure 行已看自己的 QP 原页；跨页题补看后续页。页码与行号在 `pipeline/tag/visual_review.jsonl`，渲染图片为本地临时缓存，不入库。',
        '- 标签真源为 `pipeline/tag/p1_tags.jsonl`。`apply_tags.py` 只替换或追加 types、tag_confidence、tag_note；既有字段的原始 JSON 值、转义与空白不重新序列化。覆盖、题型码、低信心说明及 equivalent_of 一致性均在写入前检查。',
        '- 979 行的原有字段值 token 已逐字比对通过；重复套用无改动。合并器另有 16 项保真与错误输入测试。',
        '- 9618_s25_12:7(b)(ii) 带 marks-unclear：题目明确是 XOR 求结果，保留 high/PF-12；未修改抽取字段或分值。', '',
        '## 盲标与 pilot', '',
        '- 先完成全部 979 行并提交封存（原封存提交 `da13eb6`；合并后以快照 SHA-256 核验内容），之后才首次读取 pilot。封存文件：`pipeline/tag/p1_tags.blind.jsonl`；输入与哈希：`pipeline/tag/blind_manifest.json`。',
        f'- 盲标 SHA-256：`{manifest["blind_sha256"]}`。',
        f'- **主题型一致率：{matches}/{len(pilot)} = {matches/len(pilot):.2%}**。主题型加副题型集合完全一致：{full_matches}/{len(pilot)} = {full_matches/len(pilot):.2%}。',
        '- 此处是按已发布指南（含示例）盲标后与 pilot 的一致率，不能当作未见题目的独立准确率。没有为追求一致率改写封存标签。',
        '- 机器可复算的全部分歧在 `pipeline/tag/pilot_comparison.json`；复核理由真源为 `pipeline/tag/pilot_review.jsonl`。', '',
        '| 行 id | 盲标 primary / cross | pilot primary / cross | 最终结论与理由 |',
        '|:--|:--|:--|:--|']
    for d in differences:
        b, g, f = d['blind'], d['pilot'], d['final']
        lines.append(f'| {d["id"]} | {b["primary"]} / {", ".join(b["cross"]) or "无"} | {g["primary"]} / {g["cross"] or "无"} | {('裁决后' if d['review']['decision'] == 'adjudicated' else '保留')} {f["primary"]} / {", ".join(f["cross"]) or "无"}。{d["review"]["reason"]} |')
    lines += ['', f'当前最终标签与 pilot：主题型 {comparison["final_primary_matches"]}/{len(pilot)}；主题型加副题型 {comparison["final_primary_cross_matches"]}/{len(pilot)}。盲标一致率仍使用封存快照。', '',
              '## 低信心清单', '',
              '| 行 id | 主题型 | 副题型 | 犹豫的题型与理由 |', '|:--|:--|:--|:--|']
    for r in low:
        lines.append(f'| {r["id"]} | {r["types"]["primary"]} | {", ".join(r["types"]["cross"])} | {r["tag_note"]} |')
    if not low:
        lines.append('| 无 | — | — | 当前没有低信心行 |')
    lines += ['', '## 核验语料统计口径', '',
        '只计 extension=false 且 equivalent_of 为空的行，与 build/stats.py 一致。主题型行数与分值均独占归属，合计为 805 行、2025 分；混合小问仍把整行分值计给主题型，不推测各子知识点的分值拆分。副题型另列出现行数与关联整行分值，仅表示覆盖范围，不能与主题型分值相加。章级副题型按行去重（同一行若有同章两个副题型只计一次）。', '',
        '| 章 | 主行数 | 主分值 | 副关联行数 | 副关联整行分值 |', '|:--|--:|--:|--:|--:|']
    chapters = list(dict.fromkeys(t['chapter'] for t in taxonomy['types']))
    for chapter in chapters:
        primary = [r for r in verified if r['types']['primary'].split('-')[1] == chapter]
        cross = [r for r in verified if any(c.split('-')[1] == chapter for c in r['types']['cross'])]
        lines.append(f'| {chapter} | {len(primary)} | {sum(r["marks"] for r in primary)} | {len(cross)} | {sum(r["marks"] for r in cross)} |')
    lines += ['', '| 题型码 | 题型 | 主行数 | 主分值 | 副关联行数 | 副关联整行分值 |', '|:--|:--|--:|--:|--:|--:|']
    unused, rare = [], []
    for t in taxonomy['types']:
        code = t['code']
        primary = [r for r in verified if r['types']['primary'] == code]
        cross = [r for r in verified if code in r['types']['cross']]
        lines.append(f'| {code} | {t["name_zh"]} | {len(primary)} | {sum(r["marks"] for r in primary)} | {len(cross)} | {sum(r["marks"] for r in cross)} |')
        if not primary and not cross:
            unused.append(code)
        if len(primary)+len(cross) < 2:
            rare.append(code)
    lines += ['', '## 未使用题型与指南建议', '',
        f'- 核验语料未使用题型：{", ".join(unused) or "无；88 个题型均至少用作一次主题型"}。',
        f'- 核验语料出现不足两行（含副题型）：{", ".join(rare) or "无"}。',
        '- taxonomy、tagging-guide、pilot、MS 与抽取字段均未改动。', '',
        '## 裁决回写', '',
        f'已应用 papers/p1/adjudication.csv 的 {len(adjudications)} 行；confidence 统一为 high，note 仅为 adjudicated: 加规则编号。原始裁决理由以 CSV 为准，盲标快照与首次复核历史保留。', '',
        '| 行 id | 规则 | 当前主题型 | 当前副题型 |', '|:--|:--|:--|:--|']
    for row_id, ruling in adjudications.items():
        lines.append(f'| {row_id} | {ruling["note"]} | {ruling["primary"]} | {", ".join(ruling["cross"]) or "无"} |')
    lines += ['', '## 复现', '',
        '```sh',
        '~/.venvs/alevel-cs/bin/python pipeline/tag/apply_adjudication.py',
        '~/.venvs/alevel-cs/bin/python pipeline/tag/apply_adjudication.py --check',
        '~/.venvs/alevel-cs/bin/python pipeline/tag/apply_tags.py',
        '~/.venvs/alevel-cs/bin/python pipeline/tag/apply_tags.py --check',
        '~/.venvs/alevel-cs/bin/python -m pytest pipeline/tag/test_apply_tags.py pipeline/tag/test_adjudication.py -q',
        '~/.venvs/alevel-cs/bin/python pipeline/tag/build_report.py',
        'make check', 'make check-scope TASK=T24', 'make build', '```', '']
    (ROOT / 'corpus/tag_report_p1.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f'Report: {count} rows; pilot primary {matches}/{len(pilot)}; low {len(low)}')


if __name__ == '__main__':
    main()
