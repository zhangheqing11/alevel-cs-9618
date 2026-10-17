"""Reproduce D35 candidates, render QP evidence, and verify link-only changes.

scan --base REV writes a review draft outside the repository; human verdicts
are never inferred from a failed pixel comparison. apply consumes the reviewed
manifest and writes overrides only. verify proves corpus field preservation.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess

from compare_pua import field_spans
from pdf_text import extract_pdf, source_path
from split_qp import split_question_paper, visual_lines, _label

ROOT = Path(__file__).resolve().parents[2]
REVIEW = ROOT / 'pipeline/extract/p3_equivalents_review.json'
FIELDS = ('stem', 'stem_ctx', 'ms_text')
CLIP = [35, 55, 570, 795]


def git_text(base, name):
    return subprocess.check_output(['git', 'show', f'{base}:{name}'], cwd=ROOT, text=True)


def baseline_rows(base):
    paths = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', base, 'corpus/rows/p3'], cwd=ROOT, text=True).splitlines()
    return {r['id']: r for name in paths for line in git_text(base, name).splitlines() for r in [json.loads(line)]}


def candidates(rows):
    result = []
    for row in sorted(rows.values(), key=lambda r: r['id']):
        target = rows.get(row['paper'][:-2] + '31:' + row['q'])
        if row['paper'].endswith('_31') or row['equivalent_of'] is not None or target is None:
            continue
        if all(' '.join(row[k].split()) == ' '.join(target[k].split()) for k in FIELDS):
            if row['marks'] != target['marks']:
                raise ValueError(f"{row['id']}: same text but different marks")
            result.append((row, target))
    return result


def question_starts(data):
    """Use the QP parser's labels to include ancestor diagrams before a leaf."""
    starts = {}
    number = letter = None
    for pn, words in enumerate(data['word_pages'], 1):
        if pn == 1:
            continue
        for group in visual_lines(words):
            text = ' '.join(w['text'] for w in group)
            if min(w['y0'] for w in group) < 55 or min(w['y0'] for w in group) > 795:
                continue
            if any(t in text for t in ('©', 'UCLES', '9618/', '[Turn', 'BLANK PAGE', 'Ĭ', 'ĥ')) or any(ord(c) < 32 for c in text):
                continue
            info = _label(group, number, letter)
            if info:
                label = info[0]
                m = re.match(r'(\d+)(\([a-z]\))?', label)
                number, letter = m[1], m[2]
                starts.setdefault(number, pn)
    return starts


def scan(base):
    import pymupdf
    rows = baseline_rows(base)
    documents, segments, starts, rasters, digests = {}, {}, {}, {}, {}

    def load(paper):
        if paper not in documents:
            path = source_path(paper[:-2] + 'qp_' + paper[-2:] + '.pdf')
            documents[paper] = pymupdf.open(path)
            digests[paper] = hashlib.sha256(path.read_bytes()).hexdigest()
            data = extract_pdf(path)
            segments[paper] = {s.label_hint: s for s in split_question_paper(data)}
            starts[paper] = question_starts(data)

    def raster(paper, page):
        key = paper, page
        if key not in rasters:
            pix = documents[paper][page - 1].get_pixmap(matrix=pymupdf.Matrix(2, 2),
                clip=pymupdf.Rect(CLIP), colorspace=pymupdf.csGRAY, alpha=False)
            rasters[key] = {'shape': [pix.width, pix.height], 'pixel_sha256': hashlib.sha256(pix.samples).hexdigest()}
        return rasters[key]

    records = []
    for row, target in candidates(rows):
        paper, other = row['paper'], target['paper']
        load(paper); load(other)
        a, b = segments[paper][row['q']], segments[other][target['q']]
        # Include all pages from the top-level question's start through this
        # leaf's end. Later sibling questions cannot affect this leaf's figure.
        ap = list(range(starts[paper][str(row['qn'])], a.end_page + 1))
        bp = list(range(starts[other][str(target['qn'])], b.end_page + 1))
        pairs = [{'page': x, 'target_page': y, 'source': raster(paper, x), 'target': raster(other, y)}
                 for x, y in zip(ap, bp)]
        equal = len(ap) == len(bp) and all(p['source'] == p['target'] for p in pairs)
        records.append({'id': row['id'], 'target': target['id'], 'has_figure': row['has_figure'],
            'qp_pages': ap, 'target_pages': bp, 'qp_sha256': digests[paper], 'target_qp_sha256': digests[other],
            'page_pairs': pairs, 'pixel_equal': equal, 'result': 'same' if equal else 'unreviewed',
            'method': 'pixel-sha256' if equal else 'pending-visual',
            'observation': '含父级图示的 QP 正文区域逐像素相同。' if equal else '像素不同，不自动判断图形相同。'})
    return {'base': base, 'renderer': f'PyMuPDF {pymupdf.VersionBind}', 'scale': 2, 'colorspace': 'GRAY',
            'clip_pt': CLIP, 'records': records}


def checked_review():
    review = json.loads(REVIEW.read_text())
    fresh = scan(review['base'])
    if {k: v for k, v in fresh.items() if k != 'records'} != {k: v for k, v in review.items() if k != 'records'}:
        raise ValueError('review configuration changed')
    if len(fresh['records']) != len(review['records']):
        raise ValueError('review candidate count changed')
    for actual, saved in zip(fresh['records'], review['records']):
        for key in actual.keys() - {'result', 'method', 'observation'}:
            if actual[key] != saved[key]:
                raise ValueError(f"{actual['id']}: evidence changed: {key}")
        if saved['result'] == 'same' and not actual['pixel_equal']:
            if saved['method'] != 'visual' or not saved['observation'].strip():
                raise ValueError(f"{saved['id']}: no human visual verdict")
        if saved['result'] not in {'same', 'different', 'uncertain'}:
            raise ValueError(f"{saved['id']}: unfinished review")
    return review


def apply(review):
    path = ROOT / 'pipeline/extract/overrides.json'
    overrides = json.loads(path.read_text())
    for entry in review['records']:
        if entry['result'] != 'same':
            continue
        old = overrides.get(entry['id'], {'fields': {}})
        if old['fields'].get('equivalent_of', entry['target']) != entry['target']:
            raise ValueError(f"{entry['id']}: conflicting existing override")
        old['fields']['equivalent_of'] = entry['target']
        old['reason'] = f"D35：题干、上下文、同题 MS 压缩空白相同；QP 图形已核验（{entry['method']}）。{entry['observation']} 证据见 p3_equivalents_review.json。"
        overrides[entry['id']] = old
    path.write_text(json.dumps(overrides, ensure_ascii=False, indent=2) + '\n')


def verify_line(before, after, links):
    old, new = json.loads(before), json.loads(after)
    expected = dict(old)
    if old['id'] in links:
        expected['equivalent_of'] = links[old['id']]
    if new != expected:
        raise ValueError(f"{old['id']}: unrelated field change")
    a, _ = field_spans(before)
    b, _ = field_spans(after)
    for key in old:
        if old[key] == new[key] and before[slice(*a[key])] != after[slice(*b[key])]:
            raise ValueError(f"{old['id']}: literal value changed: {key}")
    # A stronger guarantee: even the surrounding JSON whitespace is unchanged.
    av, bv = a['equivalent_of'], b['equivalent_of']
    if before[:av[0]] + before[av[1]:] != after[:bv[0]] + after[bv[1]:]:
        raise ValueError(f"{old['id']}: bytes outside equivalent_of changed")
    return old['equivalent_of'] != new['equivalent_of']


def verify(review):
    links = {e['id']: e['target'] for e in review['records'] if e['result'] == 'same'}
    base = review['base']
    names = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', base, 'corpus/rows'], cwd=ROOT, text=True).splitlines()
    current = sorted(str(p.relative_to(ROOT)) for p in (ROOT/'corpus/rows').glob('p*/*.jsonl'))
    if names != current:
        raise ValueError('paper set changed')
    counts = Counter()
    total, annotations = 0, Counter()
    for name in names:
        before = git_text(base, name).splitlines(keepends=True)
        after = (ROOT/name).read_text().splitlines(keepends=True)
        if len(before) != len(after):
            raise ValueError(f'{name}: row count changed')
        for old, new in zip(before, after):
            if verify_line(old, new, links):
                counts[json.loads(old)['paper']] += 1
            total += 1
            for k in ('types', 'tag_confidence', 'tag_note', 'markpoints', 'ms_max', 'er'):
                annotations[k] += k in json.loads(old)
    if sum(counts.values()) != len(links):
        raise ValueError('approved links not all changed')
    return {'base': base, 'papers': len(names), 'rows': total, 'changed': sum(counts.values()),
            'per_paper': dict(sorted(counts.items())), 'preserved_field_counts': dict(annotations)}


def migrate_audits(review):
    from run_all import row_hash
    originals = baseline_rows(review['base'])
    current = {r['id']: r for p in (ROOT/'corpus/rows/p3').glob('*.jsonl') for s in p.read_text().splitlines() for r in [json.loads(s)]}
    path = ROOT/'pipeline/extract/audit_p3.json'
    records = json.loads(path.read_text())
    migrated = 0
    for record in records:
        old, new = originals[record['id']], current[record['id']]
        if record['row_sha256'] not in {row_hash(old), row_hash(new)}:
            raise ValueError(f"{record['id']}: invalid baseline audit hash")
        if row_hash(old) != row_hash(new):
            record['row_sha256'] = row_hash(new)
            record['equivalence_update'] = {'decision': 'D35', 'baseline_row_sha256': row_hash(old),
                'equivalent_of': new['equivalent_of'], 'note': 'Link-only change verified; original PDF excerpts and review date unchanged.'}
            migrated += 1
    path.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    return migrated


def report_section(rows_by_paper):
    review = json.loads(REVIEW.read_text())
    records = review['records']
    rows = {r['id']: r for data in rows_by_paper.values() for r in data}
    lines = ['', '## D35 / T12e · P3 重复行补链', '',
        f"候选基线 `{review['base']}`；非 _31、原 equivalent_of 为空，stem/stem_ctx/ms_text 压缩空白后与同季 _31 同题号完全相同，共 {len(records)} 行。全部 has_figure。",
        '所有候选均渲染对应 QP 正文区域：144 dpi 灰度、clip=[35,55,570,795] pt，从大题起始页至本叶子结束页，覆盖父级情景图。107 行区域逐像素 SHA-256 相同；另 12 行（s24_33）并排查看原页，确认图形、数值、连线和标注相同，条码与竖直排版不同。',
        '逐行页码、源 PDF SHA-256、渲染像素 SHA-256 与人工所见在 `pipeline/extract/p3_equivalents_review.json`；可用 p3_equivalents.py scan 重现。仅将已确认项写入 overrides.json，再由 run_all.py 重出 rows，未手改 JSONL。', '',
        '| 卷 | 候选 | 补链 | 跳过 | 原因 |', '|---|---:|---:|---:|---|']
    for paper in sorted({e['id'].split(':')[0] for e in records}):
        selected = [e for e in records if e['id'].split(':')[0] == paper]
        linked = sum(rows.get(e['id'], {}).get('equivalent_of') == e['target'] for e in selected)
        skipped = [e for e in selected if e['result'] != 'same']
        lines.append(f"| {paper} | {len(selected)} | {linked} | {len(skipped)} | " + ('；'.join(e['observation'] for e in skipped) if skipped else '均已确认图形相同') + ' |')
    lines += ['', '严格对比结果见 `pipeline/extract/p3_equivalents_diff.json`：仅已批准的 equivalent_of 值变化，其余字段与字段外 JSON 字节不变；types、tag_confidence、tag_note、markpoints、ms_max、er 原样保留，P1/P2 及其他卷字节不变。',
        '原抽查记录先验证基线哈希，再机械更新受 equivalent_of 影响的哈希并注明 D35；保留原页摘录、审阅者和日期，不冒充新做的随机抽查。', '',
        '### 逐行 QP 图形证据', '', '| 行 | 指向 | QP 页 / 目标页 | 方法 | 结论 |', '|---|---|---|---|---|']
    for e in records:
        pages = ','.join(map(str, e['qp_pages'])) + ' / ' + ','.join(map(str, e['target_pages']))
        observation = e['observation'].replace('|', r'\|')
        lines.append(f"| `{e['id']}` | `{e['target']}` | {pages} | {e['method']} | {observation} |")
    pending = [e for e in records if e['result'] != 'same']
    lines += ['', '### 需要总控决定', '']
    lines += [f"- `{e['id']}`：{e['observation']}（未补链）。" for e in pending] or ['- 无。本批 119 个候选均已确认相同，补链 119，跳过 0。']
    return lines


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['scan', 'apply', 'verify'])
    parser.add_argument('--base')
    parser.add_argument('--output', type=Path, default=Path('/tmp/t12e-review-draft.json'))
    parser.add_argument('--migrate-audits', action='store_true')
    args = parser.parse_args()
    if args.action == 'scan':
        if not args.base:
            parser.error('scan requires --base')
        base = subprocess.check_output(['git', 'rev-parse', args.base], cwd=ROOT, text=True).strip()
        result = scan(base)
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
        print(Counter(e['method'] for e in result['records']))
        return
    review = checked_review()
    if args.action == 'apply':
        apply(review)
        return
    result = verify(review)
    if args.migrate_audits:
        result['audit_hashes_migrated'] = migrate_audits(review)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
