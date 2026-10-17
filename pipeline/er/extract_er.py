#!/usr/bin/env python3
"""Parse the Principal Examiner Reports (ER) into per-label excerpts.

Usage: python pipeline/er/extract_er.py [--sources DIR] [--out DIR] [--check]

Reads <sources>/pastpapers/9618_<季><yy>_er.pdf (ALEVEL_CS_SOURCES, default
/Users/zhangheqing/Desktop/alevel cs/sources) and writes corpus/er/<季><yy>.jsonl:
  {"paper": "9618_s24_31", "label": "6(c)(ii)", "text": "...", "page": 31}
plus one {"label": "_general"} entry per paper (Key messages + General comments).

Text is the ER's own words: line breaks and runs of whitespace are merged, private-use
glyphs are normalised by the D26/D29 table, nothing is paraphrased. A comment that the ER
writes for two sub-parts at once ("(ii)(iii) ...") is stored once per label with
"shared_with" naming the other label(s). Anything the parser had to guess about
is collected in `anomalies` and printed (and written next to the output with --out).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SOURCES = '/Users/zhangheqing/Desktop/alevel cs/sources'

# D26 / D29: Symbol / Wingdings glyphs left in the Private Use Area by PDF extraction.
PUA_MAP = {
    '': '←', '': '←', '': '•', '': '•', '': '✓', '': '✓',
    '': '±', '': '×', '': '○', '': '<', '': '>', '': '−',
    '': ' ', '': '⇨', '': '∞',
}
PUA_TABLE = str.maketrans(PUA_MAP)

ROMANS = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']
ROMAN_VALUE = {r: n for n, r in enumerate(ROMANS, 1)}

HEADER_LINES = (
    re.compile(r'^Cambridge International Advanced Subsidiary and Advanced Level$'),
    re.compile(r'^9618 Computer Science (June|November) 20\d\d$'),
    re.compile(r'^Principal Examiner Report for Teachers$'),
    re.compile(r'^© 20\d\d$'),
    re.compile(r'^COMPUTER SCIENCE$'),  # title block of the next paper, printed before its "Paper" line
)
PAPER_RE = re.compile(r'^Paper (9618/\d\d)$')
QUESTION_RE = re.compile(r'^Question (\d+)$')
LABEL_RE = re.compile(r'^((?:\(\s*[a-z]{1,4}\s*\)\s*)+)(.*)$')
GROUP_RE = re.compile(r'\(\s*([a-z]{1,4})\s*\)')
SPECIFIC = 'Comments on specific questions'

# The ER itself mislabels a section: w23's first "Paper 9618/33" block sits between 23 and 32 and is
# word-for-word the same as the real 33 block (QP/MS 31 and 33 have identical questions and
# mark schemes). Keyed by (season, heading as printed, 1-based occurrence of that heading).
# Reported under "需要总控决定" in corpus/er_report.md; entries carry "er_header".
HEADING_FIXUPS = {('w23', '9618/33', 1): '9618/31'}

# A label the ER prints twice in one question where the second block plainly belongs to another
# part. Keyed by (paper, printed label of the repeated block); the repeated (second) block gets the
# corrected label and carries "er_label_printed". Decision: 总控 on PR #26 (T27).
# 9618_s24_22 Q1: the second "(b)" (PDF p.17) is about how to record the variable choices
# ("store them in an array/record/file", "comments") = part 1(c), the only 2-mark part left uncommented;
# the ER has no other block for 1(c).
LABEL_FIXUPS = {('9618_s24_22', '1(b)'): '1(c)'}


class ERError(Exception):
    pass


def normalise(text: str) -> str:
    unknown = {c for c in text if 0xE000 <= ord(c) <= 0xF8FF and c not in PUA_MAP}
    if unknown:
        raise ERError('private-use character(s) outside the D26/D29 table: '
                      + ', '.join(f'U+{ord(c):04X}' for c in sorted(unknown)))
    return text.translate(PUA_TABLE)


def join_lines(lines: list[str]) -> str:
    """Merge wrapped lines; a hyphen that ends a line is kept and the break is dropped."""
    out = ''
    for line in lines:
        line = re.sub(r'\s+', ' ', line).strip()
        if not line:
            continue
        if out and out.endswith('-') and len(out) > 1 and out[-2].isalpha() and line[0].islower():
            out += line
        else:
            out = f'{out} {line}' if out else line
    return out


def page_lines(doc) -> list[tuple[int, str]]:
    """(page, line) pairs with the running page header removed."""
    result = []
    for number, page in enumerate(doc, 1):
        for raw in normalise(page.get_text()).split('\n'):
            line = raw.strip()
            if not line or any(rx.match(line) for rx in HEADER_LINES):
                continue
            result.append((number, line))
    return result


def split_papers(lines):
    """[(paper_suffix like '9618/31', [(page, line)...])] in document order."""
    papers = []
    counts: dict[str, int] = {}
    for number, line in lines:
        match = PAPER_RE.match(line)
        if match:
            printed = match.group(1)
            counts[printed] = counts.get(printed, 0) + 1
            papers.append(((printed, counts[printed]), []))
        elif papers:
            papers[-1][1].append((number, line))
    return papers


def parse_label(line: str):
    """Return (tokens, rest) if the line starts with label groups such as '(b) (i)'."""
    match = LABEL_RE.match(line)
    if not match:
        return None
    tokens = GROUP_RE.findall(match.group(1))
    return tokens, match.group(2).strip()


def classify(tokens):
    """-> ('letter'|'roman'|'letter_roman'|'romans', values) or None when not a label shape."""
    if len(tokens) == 1:
        t = tokens[0]
        if t in ROMAN_VALUE:
            return 'roman', [t]
        if len(t) == 1:
            return 'letter', [t]
        return None
    if len(tokens) == 2:
        a, b = tokens
        if len(a) == 1 and a not in ROMAN_VALUE and b in ROMAN_VALUE:
            return 'letter_roman', [a, b]
        if a in ROMAN_VALUE and b in ROMAN_VALUE and ROMAN_VALUE[b] == ROMAN_VALUE[a] + 1:
            return 'romans', [a, b]
        if len(a) == 1 and a == 'i' and b in ROMAN_VALUE:
            return None
    if len(tokens) == 3:
        a, b, c = tokens
        if (all(t in ROMAN_VALUE for t in tokens)
                and ROMAN_VALUE[b] == ROMAN_VALUE[a] + 1 and ROMAN_VALUE[c] == ROMAN_VALUE[b] + 1):
            return 'romans', [a, b, c]
    return None


def repeated_label(qn, kind, vals, letter, roman, current):
    """The label this line names when it only repeats the label already open, else None."""
    if kind == 'letter':
        candidate = f'{qn}({vals[0]})'
        if vals[0] == letter and roman is None and current['labels'] == [candidate]:
            return candidate
    elif kind == 'roman':
        candidate = f'{qn}({letter})({vals[0]})'
        if letter is not None and vals[0] == roman and current['labels'] == [candidate]:
            return candidate
    elif kind == 'letter_roman':
        candidate = f'{qn}({vals[0]})({vals[1]})'
        if vals[0] == letter and vals[1] == roman and current['labels'] == [candidate]:
            return candidate
    return None


def parse_question_body(qn: int, body, anomalies, context):
    """body: [(page, line)] after 'Question N'. -> list of entry dicts (no paper yet)."""
    entries = []  # each: {'labels': [label,...], 'page': p, 'lines': []}
    letter = None
    roman = None
    current = {'labels': [str(qn)], 'page': body[0][0] if body else 0, 'lines': []}
    entries.append(current)

    def start(labels, page):
        nonlocal current
        current = {'labels': labels, 'page': page, 'lines': []}
        entries.append(current)

    for page, line in body:
        parsed = parse_label(line)
        shape = classify(parsed[0]) if parsed else None
        accepted = False
        if shape:
            kind, vals = shape
            rest = parsed[1]
            duplicate = repeated_label(qn, kind, vals, letter, roman, current)
            if duplicate and re.search(r'[A-Za-z]', rest) or duplicate and not rest:
                anomalies.append(f'{context}: label {duplicate} printed twice in the ER; second block kept '
                                 f'separately (duplicate_label), not attached to any row')
                start([duplicate], page)
                current['duplicate'] = True
                if rest:
                    current['lines'].append(rest)
                continue
            if kind == 'letter' and (letter is None or vals[0] > letter):
                letter, roman = vals[0], None
                start([f'{qn}({letter})'], page)
                accepted = True
            elif kind == 'roman' and letter is not None and (
                    roman is None or ROMAN_VALUE[vals[0]] > ROMAN_VALUE[roman]):
                roman = vals[0]
                start([f'{qn}({letter})({roman})'], page)
                accepted = True
            elif kind == 'letter_roman' and (
                    letter is None or vals[0] > letter
                    or (vals[0] == letter and (roman is None or ROMAN_VALUE[vals[1]] > ROMAN_VALUE[roman]))):
                letter, roman = vals
                start([f'{qn}({letter})({roman})'], page)
                accepted = True
            elif kind == 'romans' and letter is not None and (
                    roman is None or ROMAN_VALUE[vals[0]] > ROMAN_VALUE[roman]):
                roman = vals[-1]
                start([f'{qn}({letter})({r})' for r in vals], page)
                accepted = True
                anomalies.append(f'{context} Q{qn}: one comment for {"/".join(f"({r})" for r in vals)} '
                                 f'stored under each label (shared_with)')
            if accepted:
                if rest:
                    if rest[0].islower():
                        anomalies.append(f'{context} Q{qn}: label {current["labels"][0]} followed by lower-case '
                                         f'text on the same line ({rest[:40]!r}); check')
                    current['lines'].append(rest)
                continue
            anomalies.append(f'{context} Q{qn}: line looks like a label but breaks the sequence, '
                             f'kept as text: {line[:60]!r}')
        elif parsed and not shape:
            anomalies.append(f'{context} Q{qn}: line begins with brackets, kept as text: {line[:60]!r}')
        current['lines'].append(line)
    return entries


def parse_paper(suffix: str, lines, paper_id: str, anomalies):
    context = paper_id
    # headings
    key_idx = next((i for i, (_, l) in enumerate(lines) if l == 'Key messages'), None)
    spec_idx = next((i for i, (_, l) in enumerate(lines) if l == SPECIFIC), None)
    if key_idx is None:
        text = join_lines([l for _, l in lines])
        if len(text) > 300 or not re.search(r'too few candidates', text):
            raise ERError(f'{paper_id}: no "Key messages" heading')
        text = re.search(r'There were too few[^.]*\.', text).group(0)
        anomalies.append(f'{context}: ER has no report ({text!r}); stored as _general only')
        return [{'label': '_general', 'text': text, 'page': lines[0][0]}]
    # question headings: monotonic, only after the specific-comments heading when there is one
    first = spec_idx + 1 if spec_idx is not None else key_idx + 1
    q_positions = []
    last = 0
    for i in range(first, len(lines)):
        m = QUESTION_RE.match(lines[i][1])
        if not m:
            continue
        n = int(m.group(1))
        if n <= last:
            anomalies.append(f'{context}: line "Question {n}" after Question {last}, kept as text')
            continue
        if n != last + 1:
            anomalies.append(f'{context}: ER jumps from Question {last} to Question {n}')
        q_positions.append((n, i))
        last = n
    if not q_positions:
        raise ERError(f'{paper_id}: no Question headings')
    general_end = spec_idx if spec_idx is not None else q_positions[0][1]
    general_lines = lines[key_idx:general_end]
    # an ER with no "Comments on specific questions" heading: general text stops at Question 1
    out = [{'label': '_general', 'text': join_lines([l for _, l in general_lines]),
            'page': lines[key_idx][0]}]
    bounds = [(n, i) for n, i in q_positions] + [(None, len(lines))]
    for (n, i), (_, j) in zip(bounds, bounds[1:]):
        body = lines[i + 1:j]
        if not body:
            anomalies.append(f'{context}: Question {n} has no text')
            continue
        for entry in parse_question_body(n, body, anomalies, context):
            text = join_lines(entry['lines'])
            if not text:
                if len(entry['labels']) == 1 and entry['labels'][0] == str(n):
                    continue  # no question-level preamble
                anomalies.append(f'{context}: label {entry["labels"][0]} has no text')
                continue
            for label in entry['labels']:
                item = {'label': label, 'text': text, 'page': entry['page']}
                others = [x for x in entry['labels'] if x != label]
                if others:
                    item['shared_with'] = others
                if entry.get('duplicate'):
                    fixed = LABEL_FIXUPS.get((paper_id, label))
                    if fixed:
                        item['label'] = fixed
                        item['er_label_printed'] = label
                        anomalies.append(f'{context}: second block printed as {label} stored as {fixed} (LABEL_FIXUPS)')
                    else:
                        item['duplicate_label'] = True
                out.append(item)
    return out


def extract_pdf(path: Path, season: str):
    import pymupdf  # imported late so the pure parsing helpers can be tested without it
    doc = pymupdf.open(str(path))
    anomalies: list[str] = []
    entries = []
    seen = set()
    for (printed, occurrence), lines in split_papers(page_lines(doc)):
        suffix = HEADING_FIXUPS.get((season, printed, occurrence), printed)
        paper_id = f'9618_{season}_{suffix.split("/")[1]}'
        if suffix != printed:
            anomalies.append(f'{paper_id}: heading printed as Paper {printed} (occurrence {occurrence}); '
                             f'treated as {suffix}')
        if paper_id in seen:
            raise ERError(f'{paper_id}: Paper heading appears twice in {path.name}')
        seen.add(paper_id)
        for item in parse_paper(suffix, lines, paper_id, anomalies):
            if suffix != printed:
                item['er_header'] = f'9618/{printed.split("/")[1]}'
            entries.append({'paper': paper_id, **item})
    return entries, anomalies


def dump(entries) -> str:
    return ''.join(json.dumps(e, ensure_ascii=False, separators=(',', ':')) + '\n' for e in entries)


def sources_dir(arg=None) -> Path:
    return Path(arg or os.environ.get('ALEVEL_CS_SOURCES') or DEFAULT_SOURCES)


def season_files(src: Path):
    files = sorted((src / 'pastpapers').glob('9618_*_er.pdf'))
    return [(re.match(r'9618_([sw]\d\d)_er\.pdf$', f.name).group(1), f) for f in files]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sources')
    parser.add_argument('--out', default=str(ROOT / 'corpus' / 'er'))
    parser.add_argument('--check', action='store_true', help='fail if corpus/er would change; never writes')
    args = parser.parse_args()
    src = sources_dir(args.sources)
    out_dir = Path(args.out)
    changed = []
    all_anomalies = []
    for season, pdf in season_files(src):
        try:
            entries, anomalies = extract_pdf(pdf, season)
        except ERError as exc:
            sys.exit(f'ER extraction failed: {exc}')
        target = out_dir / f'{season}.jsonl'
        data = dump(entries)
        if not target.exists() or target.read_text(encoding='utf-8') != data:
            changed.append(target.name)
            if not args.check:
                out_dir.mkdir(parents=True, exist_ok=True)
                target.write_text(data, encoding='utf-8')
        all_anomalies += [f'{season}: {a}' for a in anomalies]
        print(f'{season}: {len(entries)} entries, {len(anomalies)} anomalies')
    for a in all_anomalies:
        print('  ! ' + a)
    if args.check and changed:
        sys.exit(f'corpus/er out of date: {changed}')


if __name__ == '__main__':
    main()
