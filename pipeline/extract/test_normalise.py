"""D26 substitutions must be exact, idempotent and narrowly scoped."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from normalise import normalise_text, normalise_row


def test_exact_d26_mapping_and_unknown_preservation():
    source = '\uf0ac\uf0df\uf0b7\uf09f\uf0fc\uf050\uf0b1\uf0b4\uf0a1\uf03c\uf03e\uf02d\uf020\ue001'
    expected = '←←••✓✓±×○<>− \ue001'
    assert normalise_text(source) == expected
    assert normalise_text(expected) == expected


def test_only_authorized_fields_are_normalised():
    row = {'stem': '\uf0ac', 'stem_ctx': '\uf020', 'ms_text': '\uf050',
           'tag_note': '\uf0ac', 'markpoints': [{'text': '\uf0ac', 'note': '\uf0ac'}]}
    normalise_row(row)
    assert row == {'stem': '←', 'stem_ctx': ' ', 'ms_text': '✓',
                   'tag_note': '\uf0ac', 'markpoints': [{'text': '←', 'note': '\uf0ac'}]}


def test_comparison_rejects_unrelated_changes():
    import json
    import pytest
    from compare_pua import verify_line
    row = {'id': 'paper:1', 'stem': '\uf0ac', 'stem_ctx': '', 'ms_text': 'x', 'marks': 1}
    before = json.dumps(row, ensure_ascii=False)
    after = json.dumps(normalise_row(dict(row)), ensure_ascii=False)
    assert sum(verify_line(before, after)[0].values()) == 1
    with pytest.raises(ValueError, match='unexpected field'):
        verify_line(before, after.replace('"marks": 1', '"marks": 2'))
    with pytest.raises(ValueError, match='literal value'):
        verify_line(before, after.replace('"x"', '"\\u0078"'))


def test_d29_adjudicated_step_arrow_and_infinity():
    assert normalise_text('Step 1\uf0f0Step 2; distance=\uf0a5') == 'Step 1⇨Step 2; distance=∞'
    assert normalise_text('\ue001') == '\ue001'
