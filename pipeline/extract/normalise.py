"""Exact Symbol/Wingdings substitutions approved in DECISIONS D26/D29.

Keep this after parsing and deduplication: glyph substitution must not change
question boundaries, marks, flags or duplicate decisions. Unknown PUA stays put.
"""
D26 = dict(zip(map(chr, (0xF0AC, 0xF0DF, 0xF0B7, 0xF09F, 0xF0FC, 0xF050,
                        0xF0B1, 0xF0B4, 0xF0A1, 0xF03C, 0xF03E, 0xF02D, 0xF020)),
               ('←', '←', '•', '•', '✓', '✓', '±', '×', '○', '<', '>', '−', ' ')))
# D29 extends the approved D26 table after source-page adjudication.
D26.update({'\uf0f0': '⇨', '\uf0a5': '∞'})
TRANSLATION = str.maketrans(D26)
TEXT_FIELDS = ('stem', 'stem_ctx', 'ms_text')


def normalise_text(text):
    return text.translate(TRANSLATION)


def normalise_row(row):
    for field in TEXT_FIELDS:
        if field in row:
            row[field] = normalise_text(row[field])
    for point in row.get('markpoints', []):
        point['text'] = normalise_text(point['text'])
    return row


def main():
    """Normalize markpoint truth text before reapplying annotation mergers."""
    import argparse
    import json
    from pathlib import Path
    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument('--markpoints', type=Path, required=True)
    args = parser.parse_args()
    before = args.markpoints.read_text(encoding='utf-8')
    lines = []
    changed = 0
    for line in before.splitlines():
        row = json.loads(line)
        old = json.dumps(row, ensure_ascii=False)
        normalise_row(row)
        if json.dumps(row, ensure_ascii=False) != old:
            line = json.dumps(row, ensure_ascii=False, separators=(',', ':'))
            changed += 1
        lines.append(line)
    args.markpoints.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'{changed} markpoint truth records normalized')


if __name__ == '__main__':
    main()
