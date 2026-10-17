"""Prove D26 is the only corpus change, including literal JSON field tokens.

Run after extraction and both annotation mergers:
    python pipeline/extract/compare_pua.py --base origin/main
The checked baseline is a Git revision, never a rewritten local snapshot.
"""
import argparse
from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys

from normalise import D26, TEXT_FIELDS, normalise_row

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'pipeline/tag'))
from apply_tags import field_spans


def verify_line(before, after):
    original, actual = json.loads(before), json.loads(after)
    expected = normalise_row(deepcopy(original))
    if actual != expected:
        different = sorted(k for k in original.keys() | actual.keys() if actual.get(k) != expected.get(k))
        raise ValueError(f"{original['id']}: unexpected field changes: {different}")
    old_spans, _ = field_spans(before)
    new_spans, _ = field_spans(after)
    # JSON whitespace between fields may be formatted by the existing P2 merger;
    # each unchanged value token must still be byte-for-byte identical.
    for key in original:
        if actual[key] == original[key]:
            a, b = old_spans[key], new_spans[key]
            if before[a[0]:a[1]] != after[b[0]:b[1]]:
                raise ValueError(f"{original['id']}: literal value changed: {key}")
    counts = Counter()
    unknown = []
    fields = [(k, original[k], actual[k]) for k in TEXT_FIELDS]
    fields += [(f'markpoints[{i}].text', p['text'], actual['markpoints'][i]['text'])
               for i, p in enumerate(original.get('markpoints', []))]
    for field, old, new in fields:
        counts[field.split('[')[0]] += sum(c in D26 for c in old)
        for code in sorted(set(c for c in new if '\ue000' <= c <= '\uf8ff')):
            unknown.append((original['id'], field, f'U+{ord(code):04X}', new.count(code)))
    return counts, unknown


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', required=True)
    parser.add_argument('--report', default='pipeline/extract/pua_report.md')
    args = parser.parse_args()
    revision = subprocess.check_output(['git', 'rev-parse', args.base], cwd=ROOT, text=True).strip()
    names = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', revision, 'corpus/rows'], cwd=ROOT, text=True).splitlines()
    current = sorted(str(p.relative_to(ROOT)) for p in (ROOT / 'corpus/rows').glob('p*/*.jsonl'))
    if names != current:
        raise ValueError('paper set differs from baseline')
    report = ['# T12c · D26 私用区归一对比', '', f'基线：`{revision}`。', '',
              '逐行确认：仅 stem、stem_ctx、ms_text 和 markpoints[].text 按 D26 精确替换；其他字段值及未变化字段的 JSON 值字节完全一致。P2 合并器会重排字段间空白，未将这类排版视作字段变化。', '',
              '| 卷 | stem | stem_ctx | ms_text | markpoints.text | 合计 |', '|---|---:|---:|---:|---:|---:|']
    unknown = []
    total = Counter()
    nrows = 0
    for name in names:
        before = subprocess.check_output(['git', 'show', f'{revision}:{name}'], cwd=ROOT, text=True).splitlines()
        after = (ROOT / name).read_text().splitlines()
        if len(before) != len(after):
            raise ValueError(f'{name}: row count changed')
        counts = Counter()
        for a, b in zip(before, after):
            changes, remaining = verify_line(a, b)
            counts.update(changes)
            unknown.extend(remaining)
            nrows += 1
        total.update(counts)
        report.append('| ' + Path(name).stem + ' | ' + ' | '.join(str(counts[k]) for k in (*TEXT_FIELDS, 'markpoints')) + f' | {sum(counts.values())} |')
    report += ['', f'共 {len(names)} 卷 / {nrows} 行，替换 {sum(total.values())} 处（含重复出现在题干情景和得分点的字符）。', '', '## 表外私用区字符', '', '| 行 | 字段 | 字符 | 次数 |', '|---|---|---|---:|']
    report += ['| ' + ' | '.join(map(str, u)) + ' |' for u in unknown] or ['| 无 | — | — | 0 |']
    report += ['', '表外字符原样保留，未推断其含义。历史审计摘录不作为新的原页核验；原有内容哈希如发生机械替换，应从基线验证后迁移。', '']
    (ROOT / args.report).write_text('\n'.join(report))
    print(f'{nrows} rows verified; {sum(total.values())} substitutions; {len(unknown)} unknown locations')


if __name__ == '__main__':
    main()
