"""Apply exactly the four skill adjudications in DECISIONS D30, repeatably."""
from copy import deepcopy
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
TARGETS = {
    ('9618_w21_22:6(d)', 6): 'assign-value',
    ('9618_w23_21:6(a)', 5): 'assign-value',
    ('9618_s22_22:4(a)', 5): 'shift-values',
    ('9618_s22_22:4(a)', 6): 'shift-values',
}
KEYWORDS = re.compile(r'assign|shuffl|shift|mov(?:e|ing)\s+(?:up|down)|rotat', re.I)


def prepare(text):
    seen, lines, changed = set(), [], 0
    for line in text.splitlines():
        row = json.loads(line)
        before = deepcopy(row)
        for point in row['markpoints']:
            key = row['id'], point['n']
            if key not in TARGETS:
                continue
            if key in seen:
                raise ValueError(f'duplicate D30 point: {key}')
            seen.add(key)
            new = TARGETS[key]
            if point['skills'] == [new]:
                continue
            if point['skills'] != ['initialise-variables']:
                raise ValueError(f'unexpected prior skills for {key}: {point["skills"]}')
            point['skills'] = [new]
            changed += 1
        lines.append(line if row == before else json.dumps(row, ensure_ascii=False))
    if seen != set(TARGETS):
        raise ValueError(f'missing D30 points: {set(TARGETS) - seen}')
    return '\n'.join(lines) + '\n', changed


def candidates(records):
    """Broad keyword hits only; no automatic skill decisions."""
    return [(row['id'], point) for row in records for point in row['markpoints']
            if (row['id'], point['n']) not in TARGETS and KEYWORDS.search(point['text'])]


def main():
    path = HERE / 'p2_markpoints.jsonl'
    before = path.read_text(encoding='utf-8')
    after, changed = prepare(before)
    if before != after:
        path.write_text(after, encoding='utf-8')
    print(f'D30: {changed} skill replacements')


if __name__ == '__main__':
    main()
