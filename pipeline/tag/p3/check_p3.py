#!/usr/bin/env python3
"""Validate P3 annotation sources without reading pilot inputs."""
import importlib.util
import json
from pathlib import Path


def _load_sibling(name):
    """Load a sibling when this file is executed as a standalone script.

    Pytest's importlib mode keeps test modules isolated, but the repository's
    pipeline scripts are also run directly (``python pipeline/.../check_p3.py``).
    A unique module name avoids the three component-local ``workbench.py``
    files competing in ``sys.modules`` during a root pytest run.
    """
    path = Path(__file__).with_name(name + ".py")
    spec = importlib.util.spec_from_file_location(f"_p3_check_{name}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


try:
    from .workbench import HERE, ROOT, rows, records, duplicates, norm
    from .apply_p3 import index_records
except ImportError:
    _workbench = _load_sibling("workbench")
    _apply_p3 = _load_sibling("apply_p3")
    HERE, ROOT = _workbench.HERE, _workbench.ROOT
    rows, records = _workbench.rows, _workbench.records
    duplicates, norm = _workbench.duplicates, _workbench.norm
    index_records = _apply_p3.index_records

ALWAYS = {'DR-03', 'DR-05', 'CT-02', 'CT-03', 'CT-06', 'CT-07', 'FP-06', 'FP-10'}
CONDITIONAL = {'CT-08', 'CT-09', 'FP-05'}
FORBIDDEN = {'translate-pseudocode', 'exception-handling', 'p4-identifiers'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(data, tags, points, inherited, type_codes, skills, exemptions):
    require(set(tags) == set(data), 'tag coverage must equal corpus ids')
    require(set(points) <= set(data), 'unknown markpoint ids')
    candidates = {rid for rid, row in data.items() if row['marks'] >= 4
                  and tags[rid]['primary'][3:] in ALWAYS | CONDITIONAL}
    require(set(points) <= candidates, 'split outside guide section 8.1')
    require(set(exemptions) == candidates - set(points), 'split coverage or exemptions incomplete')
    for rid, item in exemptions.items():
        require(tags[rid]['primary'][3:] in CONDITIONAL and bool(item.get('reason')),
                f'{rid}: invalid exemption for always-split type')
    for rid, tag in tags.items():
        require(set(tag) == {'id', 'primary', 'cross', 'confidence', 'note'}, f'{rid}: tag fields')
        require(tag['primary'] in type_codes and set(tag['cross']) <= type_codes, f'{rid}: type code')
        require(len(set(tag['cross'])) == len(tag['cross']) <= 2
                and tag['primary'] not in tag['cross'], f'{rid}: cross types')
        require(tag['confidence'] in {'high', 'low'} and
                (tag['confidence'] != 'low' or bool(tag['note'])), f'{rid}: confidence/note')
    for rid, item in points.items():
        require(set(item) == {'id', 'ms_max', 'markpoints'}, f'{rid}: point set fields')
        require(bool(item['markpoints']), f'{rid}: empty split')
        total = 0
        for n, point in enumerate(item['markpoints'], 1):
            require(set(point) == {'n', 'text', 'marks', 'skills'} and point['n'] == n,
                    f'{rid}: point fields/sequence')
            require(bool(point['text']) and norm(point['text']) in norm(data[rid]['ms_text']),
                    f'{rid}: non-verbatim text {point["text"]!r}')
            require(type(point['marks']) is int and point['marks'] >= 1, f'{rid}: point marks')
            require(1 <= len(point['skills']) <= 3 and len(set(point['skills'])) == len(point['skills'])
                    and set(point['skills']) <= skills and not set(point['skills']) & FORBIDDEN,
                    f'{rid}: invalid skills {point["skills"]}')
            total += point['marks']
        cap = item['ms_max']
        require((cap is None and total == data[rid]['marks']) or
                (cap == data[rid]['marks'] and total > cap), f'{rid}: point total/cap mismatch')
    for rid, parent in inherited.items():
        require({k: v for k, v in tags[rid].items() if k != 'id'} ==
                {k: v for k, v in tags[parent].items() if k != 'id'}, f'{rid}: inherited tags differ')
        require((rid in points) == (parent in points), f'{rid}: inherited split missing')
        if rid in points:
            require({k: v for k, v in points[rid].items() if k != 'id'} ==
                    {k: v for k, v in points[parent].items() if k != 'id'}, f'{rid}: inherited points differ')


def load_skills(path):
    vocabulary = json.loads(path.read_text(encoding='utf-8'))
    result = {item['tag'] for item in vocabulary['tags']}
    if vocabulary.get('extends'):
        result |= load_skills(ROOT / vocabulary['extends'])
    return result


def main():
    data = rows()
    tags = index_records(records(HERE / 'p3_tags.jsonl'))
    points = index_records(records(HERE / 'p3_markpoints.jsonl'))
    exemptions = index_records(records(HERE / 'split_exemptions.jsonl'))
    types = {item['code'] for item in json.loads((ROOT / 'papers/p3/taxonomy.json').read_text())['types']}
    validate(data, tags, points, duplicates(data), types,
             load_skills(ROOT / 'papers/p3/skill_tags.json'), exemptions)
    require(len(data) == 858, 'expected 858 P3 rows')
    low = sum(t['confidence'] == 'low' for t in tags.values())
    require(low < 0.1 * len(data), 'low confidence exceeds 10%')
    print(f'{len(tags)}/{len(data)} tags; {len(points)} split rows; '
          f'{sum(len(p["markpoints"]) for p in points.values())} points; '
          f'{len(exemptions)} justified exclusions; {low} low; validation passed')


if __name__ == '__main__':
    main()
