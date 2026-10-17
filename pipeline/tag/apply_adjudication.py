"""Write design-agent CSV rulings back to the P1 label source.

Run this whenever T22 appends adjudication rows, then run apply_tags.py and
build_report.py. --check verifies the label source without writing. The CSV and
blind snapshot remain read-only. CSV reasons must start with a rule ID, for
example '裁决规则 B1（...）：...'; tag notes contain only 'adjudicated: B1'.
"""
import argparse
import csv
import os
from pathlib import Path
import re
import tempfile

from apply_tags import ROOT, encode, load_jsonl, prepare


def read_adjudications(path):
    rulings = {}
    with Path(path).open(encoding='utf-8-sig', newline='') as source:
        reader = csv.DictReader(source, strict=True)
        if reader.fieldnames != ['id', 'primary', 'cross', 'reason']:
            raise ValueError('Adjudication CSV must have id,primary,cross,reason columns')
        for row in reader:
            if None in row or any(value is None for value in row.values()):
                raise ValueError('Malformed adjudication CSV row')
            row = {key: value.strip() for key, value in row.items()}
            row_id = row['id']
            if not row_id or row_id in rulings:
                raise ValueError(f'Empty or duplicate adjudication id: {row_id}')
            match = re.match(r'^裁决规则\s+([A-Z]+\d+(?:[.-]\d+)*)\b', row['reason'])
            if not match:
                raise ValueError(f'Missing rule number in adjudication reason: {row_id}')
            cross = [code.strip() for code in row['cross'].split(';')] if row['cross'] else []
            rulings[row_id] = dict(id=row_id, primary=row['primary'], cross=cross,
                                   confidence='high', note='adjudicated: '+match[1])
    return rulings


def adjudicated_tags(root=ROOT):
    """Resolve equivalent groups and validate the entire candidate before writing."""
    root = Path(root)
    prepare(root)
    tags = load_jsonl(root/'pipeline/tag/p1_tags.jsonl')
    by_id = {t['id']: t for t in tags}
    rows = {r['id']:r for path in sorted((root/'corpus/rows/p1').glob('*.jsonl'))
            for r in load_jsonl(path)}
    rulings = read_adjudications(root/'papers/p1/adjudication.csv')

    def canonical(row_id):
        while rows[row_id].get('equivalent_of'):
            row_id = rows[row_id]['equivalent_of']
        return row_id

    groups = {}
    for row_id, ruling in rulings.items():
        if row_id not in by_id:
            raise ValueError(f'Adjudication id not in P1 corpus: {row_id}')
        key = canonical(row_id)
        value = {k:v for k,v in ruling.items() if k != 'id'}
        if key in groups and groups[key] != value:
            raise ValueError(f'Conflicting equivalent adjudications: {row_id}')
        groups[key] = value
    updated = [tag | groups.get(canonical(tag['id']), {}) for tag in tags]
    prepare(root, tag_records=updated)
    return updated, len(rulings)


def apply_adjudications(root=ROOT, check=False):
    root = Path(root)
    updated, count = adjudicated_tags(root)
    path = root/'pipeline/tag/p1_tags.jsonl'
    original = path.read_bytes().decode('utf-8').splitlines(keepends=True)
    before = load_jsonl(path)
    changed = sum(old != new for old, new in zip(before, updated))
    if check and changed:
        raise ValueError(f'{changed} labels need adjudication updates')
    if changed and not check:
        data = ''.join(raw if old == new else encode(new)+('\r\n' if raw.endswith('\r\n') else '\n')
                       for raw, old, new in zip(original, before, updated)).encode('utf-8')
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(dir=path.parent, prefix='.adjudication-', delete=False) as out:
                temporary = Path(out.name)
                out.write(data)
            os.chmod(temporary, path.stat().st_mode & 0o777)
            os.replace(temporary, path)
        finally:
            if temporary and temporary.exists():
                temporary.unlink()
    return count, changed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    try:
        count, changed = apply_adjudications(check=args.check)
    except (ValueError, KeyError, TypeError, OSError, csv.Error) as exc:
        parser.exit(1, f'Adjudication failed: {exc}\n')
    print(f'Validated {count} adjudications; updated {changed} labels')


if __name__ == '__main__':
    main()
