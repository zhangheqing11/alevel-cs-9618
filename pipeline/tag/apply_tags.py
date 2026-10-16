"""Validate the P1 label source, then replace only the three tag field values.

Usage: python pipeline/tag/apply_tags.py [--check]
--check validates coverage and fails if corpus tags need updating; it never writes.
No PDF, pilot, or extraction code is used by this reapplication step.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import tempfile

ROOT = Path(__file__).resolve().parents[2]
FIELDS = ('types', 'tag_confidence', 'tag_note')


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'Duplicate JSON key: {key}')
        result[key] = value
    return result


DECODER = json.JSONDecoder(object_pairs_hook=unique_object)


def loads(text):
    return json.loads(text, object_pairs_hook=unique_object)


def encode(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))


def field_spans(line):
    """Locate top-level values without reserializing any other field or whitespace."""
    def skip(index):
        while index < len(line) and line[index].isspace():
            index += 1
        return index

    index = skip(0)
    if index >= len(line) or line[index] != '{':
        raise ValueError('Corpus row must be a JSON object')
    index = skip(index + 1)
    spans = {}
    while index < len(line) and line[index] != '}':
        key, index = DECODER.raw_decode(line, index)
        if not isinstance(key, str) or key in spans:
            raise ValueError('Invalid or duplicate object key')
        index = skip(index)
        if line[index] != ':':
            raise ValueError('Expected colon')
        start = skip(index + 1)
        _, end = DECODER.raw_decode(line, start)
        spans[key] = (start, end)
        index = skip(end)
        if line[index] == '}':
            break
        if line[index] != ',':
            raise ValueError('Expected comma')
        index = skip(index + 1)
        if line[index] == '}':
            raise ValueError('Trailing comma')
    if index >= len(line) or line[index] != '}' or line[index + 1:].strip():
        raise ValueError('Invalid object ending')
    return spans, index


def merge_line(line, tag):
    spans, close = field_spans(line)
    values = {'types': {'primary': tag['primary'], 'cross': tag['cross']},
              'tag_confidence': tag['confidence'], 'tag_note': tag['note']}
    replacements = [(spans[key][0], spans[key][1], encode(value))
                    for key, value in values.items() if key in spans]
    missing = [key for key in FIELDS if key not in spans]
    if missing:
        addition = (',' if spans else '') + ','.join(
            encode(key) + ':' + encode(values[key]) for key in missing)
        replacements.append((close, close, addition))
    for start, end, value in sorted(replacements, reverse=True):
        line = line[:start] + value + line[end:]
    return line


def load_jsonl(path):
    records = []
    for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip():
            raise ValueError(f'{path}:{number}: blank JSONL record')
        value = loads(line)
        if not isinstance(value, dict):
            raise ValueError(f'{path}:{number}: expected object')
        records.append(value)
    return records


def prepare(root=ROOT):
    """Validate every input and prepare all files before the first write."""
    root = Path(root)
    valid = {t['code'] for t in loads((root / 'papers/p1/taxonomy.json').read_text())['types']}
    tags = {}
    for tag in load_jsonl(root / 'pipeline/tag/p1_tags.jsonl'):
        if set(tag) != {'id', 'primary', 'cross', 'confidence', 'note'}:
            raise ValueError(f'Invalid tag fields: {tag.get("id")}')
        row_id = tag['id']
        if not isinstance(row_id, str) or row_id in tags:
            raise ValueError(f'Invalid or duplicate tag id: {row_id}')
        cross = tag['cross']
        if not isinstance(tag['primary'], str) or tag['primary'] not in valid:
            raise ValueError(f'Unknown primary: {row_id}')
        if (not isinstance(cross, list) or len(cross) > 2
                or any(not isinstance(c, str) or c not in valid for c in cross)
                or len(set(cross)) != len(cross) or tag['primary'] in cross):
            raise ValueError(f'Invalid cross tags: {row_id}')
        if tag['confidence'] not in ('high', 'low') or not isinstance(tag['note'], str):
            raise ValueError(f'Invalid confidence/note: {row_id}')
        if tag['confidence'] == 'low' and not tag['note'].strip():
            raise ValueError(f'Low confidence needs a note: {row_id}')
        tags[row_id] = tag

    rows = {}
    files = {}
    for path in sorted((root / 'corpus/rows/p1').glob('*.jsonl')):
        # read_bytes/decode retains CRLF, literal escapes and Unicode exactly.
        raw = path.read_bytes().decode('utf-8')
        lines = raw.splitlines(keepends=True)
        files[path] = (raw, lines)
        for line in lines:
            row = loads(line)
            if row['id'] in rows:
                raise ValueError(f'Duplicate corpus id: {row["id"]}')
            if row.get('component') != 1 or row.get('paper') != path.stem:
                raise ValueError(f'Wrong corpus component/paper: {row["id"]}')
            rows[row['id']] = row
    if not rows or set(rows) != set(tags):
        raise ValueError(f'Tag coverage mismatch; missing={sorted(set(rows)-set(tags))}; '
                         f'extra={sorted(set(tags)-set(rows))}')
    for row_id, row in rows.items():
        ref = row.get('equivalent_of')
        visited = {row_id}
        while ref:
            if ref in visited or ref not in rows:
                raise ValueError(f'Invalid equivalent_of chain: {row_id}')
            visited.add(ref)
            if any(tags[row_id][key] != tags[ref][key]
                   for key in ('primary', 'cross', 'confidence', 'note')):
                raise ValueError(f'Equivalent tags differ: {row_id} -> {ref}')
            ref = rows[ref].get('equivalent_of')

    plans = {}
    for path, (raw, lines) in files.items():
        updated = ''.join(merge_line(line, tags[loads(line)['id']]) for line in lines)
        if updated != raw:
            plans[path] = updated.encode('utf-8')
    return plans, len(rows)


def apply(root=ROOT, check=False):
    plans, count = prepare(root)
    if check:
        if plans:
            raise ValueError(f'{len(plans)} corpus files need tag updates')
        return count, 0
    for path, data in plans.items():
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(dir=path.parent, prefix='.tags-', delete=False) as out:
                temporary = Path(out.name)
                out.write(data)
            os.chmod(temporary, path.stat().st_mode & 0o777)
            os.replace(temporary, path)
        finally:
            if temporary and temporary.exists():
                temporary.unlink()
    return count, len(plans)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    try:
        count, changed = apply(check=args.check)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(1, f'Tag application failed: {exc}\n')
    print(f'Validated {count} P1 rows; updated {changed} files')


if __name__ == '__main__':
    main()
