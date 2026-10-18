"""D42 ③ / D41 ⑤: link duplicated P4 rows (and one P3 row) to their `_41` / `_31` twin.

Mirrors p3_equivalents.py (T12e) without changing it.

  scan   --base REV   find candidates, render QP evidence, write a review *draft*
                      outside the repository (human verdicts are never inferred
                      from a failed pixel comparison)
  apply               consume the reviewed manifest, write overrides.json only
  verify              prove that only approved links (and the approved P3
                      adjudication write-back) changed, byte for byte

Candidates: P4 rows whose paper is not `_41`, with no equivalent_of, whose
stem / stem_ctx / ms_text equal (whitespace-insensitive) those of the same
question in the same session's `_41` paper.  EXTRA_PAIRS adds the single P3
row of D41 ⑤ whose stem differs only in where the extraction placed `←`.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

from compare_pua import field_spans
from p3_equivalents import CLIP, FIELDS, git_text, question_starts
from pdf_text import extract_pdf, source_path
from split_qp import split_question_paper

ROOT = Path(__file__).resolve().parents[2]
REVIEW = ROOT / 'pipeline/extract/p4_equivalents_review.json'
SF_MANIFEST = ROOT / 'pipeline/extract/source_files_p4.json'
SOURCES = Path('/Users/zhangheqing/Desktop/alevel cs/sources/pastpapers')
EXTRA_PAIRS = {'9618_s24_33:10(b)': '9618_s24_31:10(b)'}
# D41 ④: the five P3 tag rows whose confidence/note were written back.
P3_TAG_ROWS = ['9618_s21_31:3(a)', '9618_s21_32:3(a)', '9618_s21_33:3(a)',
               '9618_s22_32:1(b)(iii)', '9618_s22_32:8(a)']
TAG_FIELDS = ('tag_confidence', 'tag_note')


def baseline_rows(base):
    names = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', base, 'corpus/rows/p3', 'corpus/rows/p4'],
                                    cwd=ROOT, text=True).splitlines()
    return {r['id']: r for name in names for line in git_text(base, name).splitlines() for r in [json.loads(line)]}


def candidates(rows):
    """Return [(row, target)] for D42 ③ plus EXTRA_PAIRS."""
    result = []
    for row in sorted(rows.values(), key=lambda r: r['id']):
        if row['id'] in EXTRA_PAIRS:
            target = rows[EXTRA_PAIRS[row['id']]]
            if row['equivalent_of'] is None and row['marks'] == target['marks']:
                result.append((row, target))
            continue
        if row['component'] != 4 or row['paper'].endswith('_41') or row['equivalent_of'] is not None:
            continue
        target = rows.get(row['paper'][:-2] + '41:' + row['q'])
        if target is None or target['equivalent_of'] is not None:
            continue
        if all(' '.join(row[k].split()) == ' '.join(target[k].split()) for k in FIELDS):
            if row['marks'] != target['marks']:
                raise ValueError(f"{row['id']}: same text but different marks")
            result.append((row, target))
    return result


def evidence_text(paper):
    """Text of the evidence template with the paper number masked (macOS textutil)."""
    d = SOURCES / f'{paper[:8]}_sf_{paper[-2:]}'
    docs = sorted(d.rglob('evidence.doc*'))
    if not docs:
        return None
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / 'e.txt'
        subprocess.run(['textutil', '-convert', 'txt', '-output', str(out), str(docs[0])], check=True)
        text = out.read_text(errors='replace')
    text = re.sub(r'9618[ /]*(Paper )?4[123]', '9618 Paper 4X', text)
    return re.sub(r'\s+', ' ', text).strip()


def source_comparison(papers):
    """Per paper: data files (non-evidence) identical to its `_41` twin; evidence text mask-equal."""
    manifest = {e['paper']: e for e in json.loads(SF_MANIFEST.read_text())}

    def data(paper):
        # Instruction PDFs are compared by content only (file names differ between years).
        names = [(f['path'].rsplit('/', 1)[-1], f['sha256']) for f in manifest[paper]['files']]
        return sorted((('*.pdf' if n.lower().endswith('.pdf') else n), h) for n, h in names if not n.startswith('evidence'))
    result = {}
    for paper in sorted(papers):
        twin = paper[:-2] + '41'
        a, b = evidence_text(paper), evidence_text(twin)
        result[paper] = {'target': twin, 'data_files_identical': data(paper) == data(twin),
                         'data_files': [n for n, _ in data(paper)],
                         'evidence_text_identical_after_masking_paper_number': a == b}
        if a != b:
            import difflib
            sm = difflib.SequenceMatcher(None, a or '', b or '', autojunk=False)
            result[paper]['evidence_text_differences'] = [
                [(a or '')[i1 - 12:i2 + 12], (b or '')[j1 - 12:j2 + 12]] for t, i1, i2, j1, j2 in sm.get_opcodes() if t != 'equal']
    return result


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
    pairs_found = candidates(rows)
    for row, target in pairs_found:
        paper, other = row['paper'], target['paper']
        load(paper); load(other)
        a, b = segments[paper][row['q']], segments[other][target['q']]
        # All pages from the top-level question's start through this leaf's end,
        # so a parent scenario / code box before the leaf is part of the evidence.
        ap = list(range(starts[paper][str(row['qn'])], a.end_page + 1))
        bp = list(range(starts[other][str(target['qn'])], b.end_page + 1))
        pairs = [{'page': x, 'target_page': y, 'source': raster(paper, x), 'target': raster(other, y)}
                 for x, y in zip(ap, bp)]
        equal = len(ap) == len(bp) and all(p['source'] == p['target'] for p in pairs)
        records.append({'id': row['id'], 'target': target['id'], 'has_figure': row['has_figure'],
            'qp_pages': ap, 'target_pages': bp, 'qp_sha256': digests[paper], 'target_qp_sha256': digests[other],
            'page_pairs': pairs, 'pixel_equal': equal, 'result': 'same' if equal else 'unreviewed',
            'method': 'pixel-sha256' if equal else 'pending-visual',
            'observation': '含父级情景的 QP 正文区域逐像素相同。' if equal else '像素不同，不自动判断图形相同。'})
    p4_papers = {r['id'].split(':')[0] for r in records if r['id'] not in EXTRA_PAIRS}
    return {'base': base, 'renderer': f'PyMuPDF {pymupdf.VersionBind}', 'scale': 2, 'colorspace': 'GRAY',
            'clip_pt': CLIP, 'source_files': source_comparison(p4_papers), 'records': records}


def checked_review():
    review = json.loads(REVIEW.read_text())
    fresh = scan(review['base'])
    keep = lambda d: {k: v for k, v in d.items() if k != 'records'}
    if keep(fresh) != keep(review):
        raise ValueError('review configuration or source-file comparison changed')
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


def link_reason(entry):
    if entry['id'] in EXTRA_PAIRS:
        return ('D41 ⑤：MS 逐字相同，题干只差 `←` 的抽取位置；QP 原页核对图形相同。'
                f"{entry['observation']} 证据见 p4_equivalents_review.json。")
    return (f"D42 ③：题干、上下文、同题 MS 压缩空白相同；QP 图形已核验（{entry['method']}）；"
            f"源文件目录数据文件相同。{entry['observation']} 证据见 p4_equivalents_review.json。")


def apply(review):
    path = ROOT / 'pipeline/extract/overrides.json'
    overrides = json.loads(path.read_text())
    for entry in review['records']:
        if entry['result'] != 'same':
            continue
        sf = review['source_files'].get(entry['id'].split(':')[0])
        if sf is not None and not sf['data_files_identical']:
            raise ValueError(f"{entry['id']}: source data files differ from {sf['target']}")
        old = overrides.get(entry['id'], {'fields': {}})
        if old['fields'].get('equivalent_of', entry['target']) != entry['target']:
            raise ValueError(f"{entry['id']}: conflicting existing override")
        old['fields']['equivalent_of'] = entry['target']
        old['reason'] = link_reason(entry)
        overrides[entry['id']] = old
    path.write_text(json.dumps(overrides, ensure_ascii=False, indent=2) + '\n')


def verify_line(before, after, changes):
    """`changes` maps field -> new value; nothing else may differ, even in bytes."""
    old, new = json.loads(before), json.loads(after)
    expected = dict(old)
    expected.update(changes)
    if new != expected:
        raise ValueError(f"{old['id']}: unrelated field change")
    a, _ = field_spans(before)
    b, _ = field_spans(after)
    for key in old:
        if key not in changes and before[slice(*a[key])] != after[slice(*b[key])]:
            raise ValueError(f"{old['id']}: literal value changed: {key}")
    # Everything outside the changed values (whitespace, key order) is identical.
    def blank(text, spans, keys):
        out, last = [], 0
        for s, e in sorted(spans[k] for k in keys):
            out.append(text[last:s]); last = e
        return ''.join(out) + text[last:]
    keys = [k for k in changes if old.get(k) != new.get(k)]
    if blank(before, a, keys) != blank(after, b, keys):
        raise ValueError(f"{old['id']}: bytes outside changed fields changed")
    return bool(keys)


def verify(review):
    links = {e['id']: e['target'] for e in review['records'] if e['result'] == 'same'}
    tags = {json.loads(l)['id']: json.loads(l) for l in (ROOT / 'pipeline/tag/p3/p3_tags.jsonl').read_text().splitlines()}
    base = review['base']
    names = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', base, 'corpus/rows'], cwd=ROOT, text=True).splitlines()
    current = sorted(str(p.relative_to(ROOT)) for p in (ROOT / 'corpus/rows').glob('p*/*.jsonl'))
    if names != current:
        raise ValueError('paper set changed')
    link_papers, tag_rows, unchanged_files, total = Counter(), 0, 0, 0
    preserved = Counter()
    for name in names:
        before_text = git_text(base, name)
        after_text = (ROOT / name).read_text()
        if before_text == after_text:
            unchanged_files += 1
        before, after = before_text.splitlines(keepends=True), after_text.splitlines(keepends=True)
        if len(before) != len(after):
            raise ValueError(f'{name}: row count changed')
        for old, new in zip(before, after):
            rid = json.loads(old)['id']
            changes = {}
            if rid in links:
                changes['equivalent_of'] = links[rid]
            if rid in P3_TAG_ROWS:
                changes['tag_confidence'] = tags[rid]['confidence']
                changes['tag_note'] = tags[rid]['note']
            if verify_line(old, new, changes):
                if 'equivalent_of' in changes and json.loads(old)['equivalent_of'] != links[rid]:
                    link_papers[json.loads(old)['paper']] += 1
                if rid in P3_TAG_ROWS:
                    tag_rows += 1
            total += 1
            for k in ('types', 'tag_confidence', 'tag_note', 'markpoints', 'ms_max', 'er'):
                preserved[k] += k in json.loads(old)
    if sum(link_papers.values()) != len(links):
        raise ValueError('approved links not all changed')
    if tag_rows != len(P3_TAG_ROWS):
        raise ValueError(f'expected {len(P3_TAG_ROWS)} P3 tag rows changed, got {tag_rows}')
    return {'base': base, 'papers': len(names), 'rows': total, 'files_byte_identical': unchanged_files,
            'links_changed': sum(link_papers.values()), 'per_paper': dict(sorted(link_papers.items())),
            'p3_tag_rows_changed': tag_rows, 'preserved_field_counts': dict(preserved)}


def migrate_audits(review):
    """Refresh row hashes of audit records whose row only changed by a link (D42 / D41 ⑤)."""
    from run_all import row_hash
    originals = baseline_rows(review['base'])
    current = {r['id']: r for p in (ROOT / 'corpus/rows').glob('p[34]/*.jsonl') for s in p.read_text().splitlines() for r in [json.loads(s)]}
    total = 0
    for name in ('audit_p3.json', 'audit_p4.json'):
        path = ROOT / 'pipeline/extract' / name
        records = json.loads(path.read_text())
        for record in records:
            old, new = originals[record['id']], current[record['id']]
            if record['row_sha256'] not in {row_hash(old), row_hash(new)}:
                raise ValueError(f"{record['id']}: invalid baseline audit hash")
            if row_hash(old) != row_hash(new):
                record['row_sha256'] = row_hash(new)
                record['equivalence_update'] = {'decision': 'D41 ⑤' if record['id'] in EXTRA_PAIRS else 'D42 ③',
                    'baseline_row_sha256': row_hash(old), 'equivalent_of': new['equivalent_of'],
                    'note': 'Link-only change verified; original PDF excerpts and review date unchanged.'}
                total += 1
        path.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    return total


def report_section(rows_by_paper):
    review = json.loads(REVIEW.read_text())
    records = review['records']
    rows = {r['id']: r for data in rows_by_paper.values() for r in data}
    p4 = [e for e in records if e['id'] not in EXTRA_PAIRS]
    n_pixel = sum(e['pixel_equal'] for e in records)
    lines = ['', '## D42 ③ / D41 ⑤ / T12f · P4 重复行补链与 P3 裁决回写', '',
        f"候选基线 `{review['base']}`。P4：非 `_41`、原 equivalent_of 为空，stem/stem_ctx/ms_text 压缩空白后与同季 `_41` 同题号完全相同，共 {len(p4)} 行；另 D41 ⑤ 的 P3 行 `9618_s24_33:10(b)` 1 行（题干只差 `←` 的抽取位置，MS 逐字相同）。",
        f"所有候选渲染对应 QP 正文区域（144 dpi 灰度、clip={review['clip_pt']} pt，从大题起始页至本叶子结束页）。{n_pixel} 行区域逐像素 SHA-256 相同，其余 {len(records) - n_pixel} 行经并排目视（见逐行证据）。",
        '源文件目录核对（`source_files` 字段）：每个被补链的 P4 卷与其 `_41` 的数据文件逐字节相同；evidence.doc 模板文字在遮去卷号后相同（w21_42 仅一处逗号差异，见 review）。',
        '逐行页码、源 PDF SHA-256、渲染像素 SHA-256 与人工所见在 `pipeline/extract/p4_equivalents_review.json`；可用 p4_equivalents.py scan 重现。仅将已确认项写入 overrides.json，再由 run_all.py 重出 rows，未手改 JSONL。', '',
        '| 卷 | 候选 | 补链 | 跳过 | 原因 |', '|---|---:|---:|---:|---|']
    for paper in sorted({e['id'].split(':')[0] for e in records}):
        selected = [e for e in records if e['id'].split(':')[0] == paper]
        linked = sum(rows.get(e['id'], {}).get('equivalent_of') == e['target'] for e in selected)
        skipped = [e for e in selected if e['result'] != 'same']
        lines.append(f"| {paper} | {len(selected)} | {linked} | {len(skipped)} | " +
                     ('；'.join(f"`{e['id']}` {e['observation']}" for e in skipped) if skipped else '均已确认图形相同') + ' |')
    lines += ['', '不变性验证（`p4_equivalents.py verify`，对 `' + review['base'][:7] + '` 逐字节比对全部 rows）见 `pipeline/extract/p4_equivalents_diff.json`：仅已批准的 equivalent_of 值变化；P3 五行（D41 ④）只有 tag_confidence、tag_note 变化；types、markpoints、ms_max、er 等下游字段与字段外 JSON 字节原样保留，P1/P2 及其他卷字节不变。',
        '原抽查记录先验证基线哈希，再机械更新受 equivalent_of 影响的哈希并注明 D42 ③ / D41 ⑤；保留原页摘录、审阅者和日期，不冒充新做的随机抽查。', '',
        '### P3 裁决回写（D41 ④）', '',
        '`papers/p3/adjudication.csv` 的 5 行写回 `pipeline/tag/p3/p3_tags.jsonl`，主/次题型与表一致（未变），置信度改 high，`tag_note` 引用裁决规则 C1 / C2 / C3，再由 `apply_p3.py` 合并进 rows：',
        '', *[f"- `{rid}`" for rid in P3_TAG_ROWS],
        '', '### 逐行 QP 图形证据', '', '| 行 | 指向 | QP 页 / 目标页 | 方法 | 结论 |', '|---|---|---|---|---|']
    for e in records:
        pages = ','.join(map(str, e['qp_pages'])) + ' / ' + ','.join(map(str, e['target_pages']))
        observation = e['observation'].replace('|', r'\|')
        lines.append(f"| `{e['id']}` | `{e['target']}` | {pages} | {e['method']} | {observation} |")
    pending = [e for e in records if e['result'] != 'same']
    lines += ['', '### 需要总控决定', '']
    lines += [f"- `{e['id']}`：{e['observation']}（未补链）。" for e in pending] or [f'- 无。本批 {len(records)} 个候选均已确认相同，补链 {len(records)}，跳过 0。']
    return lines


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('action', choices=['scan', 'apply', 'verify'])
    parser.add_argument('--base')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--migrate-audits', action='store_true')
    args = parser.parse_args()
    if args.action == 'scan':
        if not args.base or not args.output:
            parser.error('scan requires --base and --output (write the draft outside the repo)')
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
    out = args.output or ROOT / 'pipeline/extract/p4_equivalents_diff.json'
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
