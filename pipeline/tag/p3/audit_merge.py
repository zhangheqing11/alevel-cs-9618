"""Check unowned field values and literal JSON key/value spans against the base."""
import argparse
import json
import subprocess

from apply_p3 import OWNED, ROOT


def evidence(line):
    decoder = json.JSONDecoder()
    position = line.index('{') + 1
    result = {}
    while True:
        while line[position].isspace() or line[position] == ',':
            position += 1
        if line[position] == '}':
            return result
        start = position
        key, position = decoder.raw_decode(line, position)
        while line[position].isspace() or line[position] == ':':
            position += 1
        _, end = decoder.raw_decode(line, position)
        if key not in OWNED:
            result[key] = line[start:end]
        position = end


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', default='origin/main')
    args = parser.parse_args()
    count = 0
    for path in sorted((ROOT/'corpus/rows/p3').glob('*.jsonl')):
        original = subprocess.check_output(['git', 'show', f'{args.base}:{path.relative_to(ROOT)}'], cwd=ROOT, text=True)
        before = {json.loads(line)['id']: evidence(line) for line in original.splitlines()}
        after = {json.loads(line)['id']: evidence(line) for line in path.read_text().splitlines()}
        assert before == after, ('unowned evidence changed', path.name)
        count += len(before)
    print(f'{count} rows: every unowned JSON field literal matches {args.base}')


if __name__ == '__main__':
    main()
