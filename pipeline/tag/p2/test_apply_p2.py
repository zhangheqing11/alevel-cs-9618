"""Regression tests for preserving extraction evidence during annotation merges."""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from apply_p2 import OWNED, annotated_line, index_records


TAG = {'id': 'x', 'primary': 'P2-DT-05', 'cross': [], 'confidence': 'high', 'note': '中文'}
POINT = {'id': 'x', 'ms_max': 4, 'markpoints': [{'n': 1, 'text': 'Quote', 'marks': 1, 'skills': ['array-index']}]}


def test_preserves_literal_evidence_and_nested_values():
    line = r'{"id":"x", "stem" : "\u4e2d\nQuote \"[a,b]\"", "marks":4, "flags" : ["a", {"n":1e2}], "other":null}'
    result = annotated_line(line, {'x': TAG}, {'x': POINT})
    for literal in [r'"stem" : "\u4e2d\nQuote \"[a,b]\""', '"flags" : ["a", {"n":1e2}]', '"other":null']:
        assert literal in result
    assert {k: v for k, v in json.loads(result).items() if k not in OWNED} == json.loads(line)


@pytest.mark.parametrize('points', [{}, {'x': POINT}, {'x': dict(POINT, ms_max=None)}])
def test_idempotence_and_removal_of_obsolete_owned_fields(points):
    line = '{"id":"x", "ms_text":"Quote", "types":{}, "ms_max":99, "markpoints":[]}'
    result = annotated_line(line, {'x': TAG}, points)
    assert annotated_line(result, {'x': TAG}, points) == result
    row = json.loads(result)
    assert ('markpoints' in row) == bool(points)
    assert ('ms_max' in row) == (bool(points) and points['x']['ms_max'] is not None)
    assert row['types'] == {'primary': TAG['primary'], 'cross': []}


def test_duplicate_annotations_are_rejected():
    with pytest.raises(ValueError, match='duplicate annotation'):
        index_records([TAG, TAG])


def test_missing_annotation_is_rejected():
    with pytest.raises(KeyError):
        annotated_line('{"id":"missing"}', {'x': TAG}, {})
