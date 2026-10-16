"""Focused tests for label reapplication and preservation of original evidence."""
import json
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from apply_tags import apply, field_spans, loads, merge_line


TAG = dict(id='paper:1', primary='P1-IR-01', cross=[], confidence='high', note='')


def evidence_tokens(line):
    spans, _ = field_spans(line)
    return {k: line[a:b] for k, (a, b) in spans.items()
            if k not in ('types', 'tag_confidence', 'tag_note')}


def test_preserve_literal_evidence_and_idempotence():
    original = ' {"id" : "paper:1", "stem":"\\u4e2d \\"x\\"", "marks":1e0, "nested": {"x": [1, 2]}}\r\n'
    updated = merge_line(original, TAG)
    assert evidence_tokens(updated) == evidence_tokens(original)
    assert updated.endswith('\r\n')
    assert merge_line(updated, TAG) == updated
    assert loads(updated)['types'] == dict(primary='P1-IR-01', cross=[])


def test_replace_existing_tags_anywhere_without_changing_other_bytes():
    original = '{"types" : {"primary":null,"cross":[]}, "stem":"a,}b", "tag_note":"old", "id":"paper:1", "tag_confidence":"low"}\n'
    updated = merge_line(original, TAG)
    assert evidence_tokens(updated) == evidence_tokens(original)
    assert loads(updated)['tag_confidence'] == 'high'
    assert '"stem":"a,}b"' in updated


@pytest.fixture
def corpus(tmp_path):
    for folder in ('pipeline/tag', 'corpus/rows/p1', 'papers/p1'):
        (tmp_path / folder).mkdir(parents=True)
    (tmp_path / 'papers/p1/taxonomy.json').write_text(json.dumps({'types': [{'code':'P1-IR-01'}]}))
    path = tmp_path / 'corpus/rows/p1/paper.jsonl'
    path.write_text('{"id":"paper:1","paper":"paper","component":1,"equivalent_of":null}\n')
    tags = tmp_path / 'pipeline/tag/p1_tags.jsonl'
    tags.write_text(json.dumps(TAG)+'\n')
    return tmp_path, path, tags


def test_apply_and_read_only_check(corpus):
    root, path, _ = corpus
    before = path.read_bytes()
    with pytest.raises(ValueError, match='need tag updates'):
        apply(root, check=True)
    assert path.read_bytes() == before
    assert apply(root) == (1, 1)
    assert apply(root) == (1, 0)
    assert apply(root, check=True) == (1, 0)


@pytest.mark.parametrize('change', [
    {'primary':None}, {'primary':'P1-XX-00'}, {'cross':['P1-IR-01']},
    {'cross':['P1-XX-00']}, {'cross':[None]}, {'cross':'P1-IR-01'},
    {'confidence':'maybe'}, {'confidence':'low', 'note':' '}, {'note':None},
    {'id':'paper:2'},
])
def test_invalid_tags_leave_corpus_untouched(corpus, change):
    root, path, tags = corpus
    before = path.read_bytes()
    tags.write_text(json.dumps(TAG | change)+'\n')
    with pytest.raises(ValueError):
        apply(root)
    assert path.read_bytes() == before


def test_all_files_validated_before_writing(corpus):
    root, first, tags = corpus
    second = first.parent / 'z.jsonl'
    second.write_text('{"id":"z:1","paper":"z","component":1,"equivalent_of":"paper:1"}\n')
    tags.write_text(json.dumps(TAG)+'\n'+json.dumps(TAG | {'id':'z:1','note':'different'})+'\n')
    before = {p:p.read_bytes() for p in (first, second)}
    with pytest.raises(ValueError, match='Equivalent tags differ'):
        apply(root)
    assert all(p.read_bytes() == b for p,b in before.items())


def test_missing_duplicate_extra_and_cyclic_ids(corpus):
    root, path, tags = corpus
    before = path.read_bytes()
    for records in ([], [TAG,TAG], [TAG,TAG | {'id':'extra:1'}]):
        tags.write_text(''.join(json.dumps(r)+'\n' for r in records))
        with pytest.raises(ValueError):
            apply(root)
        assert path.read_bytes() == before
    tags.write_text(json.dumps(TAG)+'\n')
    path.write_text(before.decode().replace('null','"paper:1"'))
    with pytest.raises(ValueError, match='Invalid equivalent_of chain'):
        apply(root)


def test_duplicate_json_keys_rejected(corpus):
    root, path, tags = corpus
    before = path.read_bytes()
    tags.write_text(json.dumps(TAG)[:-1]+',"primary":"P1-IR-01"}\n')
    with pytest.raises(ValueError, match='Duplicate JSON key'):
        apply(root)
    assert path.read_bytes() == before
