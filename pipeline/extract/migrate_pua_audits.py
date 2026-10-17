"""Migrate existing audit hashes only after proving the exact D26 row change.

This preserves original PDF excerpts, reviewer and date; it is not a new review.
    python pipeline/extract/migrate_pua_audits.py --base <pre-D26-commit>
"""
import argparse
import json
from pathlib import Path
import subprocess

from compare_pua import verify_line
from normalise import normalise_row
from run_all import row_hash

ROOT = Path(__file__).resolve().parents[2]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', required=True)
    args = parser.parse_args()
    originals = {}
    for path in sorted((ROOT / 'corpus/rows').glob('p*/*.jsonl')):
        name = path.relative_to(ROOT)
        before = subprocess.check_output(['git', 'show', f'{args.base}:{name}'], cwd=ROOT, text=True).splitlines()
        after = path.read_text().splitlines()
        if len(before) != len(after):
            raise ValueError(f'{name}: row count changed')
        for old, new in zip(before, after):
            verify_line(old, new)
            row = json.loads(old)
            originals[row['id']] = row
    prepared = []
    for path in sorted((ROOT / 'pipeline/extract').glob('audit_p*.json')):
        records = json.loads(path.read_text())
        for record in records:
            row = originals[record['id']]
            if record['row_sha256'] != row_hash(row):
                raise ValueError(f"{record['id']}: baseline audit hash mismatch")
            normalise_row(row)
            if record['row_sha256'] != row_hash(row):
                record['row_sha256'] = row_hash(row)
                record['normalisation'] = ('D26 mechanical substitutions only; baseline field comparison verified; '
                                           'original PDF review date unchanged')
        prepared.append((path, json.dumps(records, ensure_ascii=False, indent=2) + '\n'))
    for path, content in prepared:
        path.write_text(content)


if __name__ == '__main__':
    main()
