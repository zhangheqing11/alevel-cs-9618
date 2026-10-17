"""Guard D35 against false duplicate links and unrelated annotation changes."""
from copy import deepcopy
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
from p3_equivalents import candidates, verify_line


def pair():
    target = {'id': '9618_s24_31:1', 'paper': '9618_s24_31', 'q': '1',
              'marks': 2, 'stem': 'same text', 'stem_ctx': 'given diagram',
              'ms_text': 'own MS', 'equivalent_of': None}
    other = dict(target, id='9618_s24_33:1', paper='9618_s24_33')
    return {r['id']: r for r in (target, other)}


@pytest.mark.parametrize('field', ['stem', 'stem_ctx', 'ms_text'])
def test_d35_rejects_any_text_field_difference(field):
    rows = pair()
    rows['9618_s24_33:1'][field] += ' changed'
    assert candidates(rows) == []


def test_d35_ignores_whitespace_but_keeps_existing_links():
    rows = pair()
    rows['9618_s24_33:1']['stem'] = ' same\n text '
    assert len(candidates(rows)) == 1
    rows['9618_s24_33:1']['equivalent_of'] = '9618_s23_31:1'
    assert candidates(rows) == []


def test_strict_comparison_rejects_unapproved_links_and_er_rewrites():
    row = dict(pair()['9618_s24_33:1'], er='comment')
    before = json.dumps(row)
    updated = dict(row, equivalent_of='9618_s24_31:1')
    links = {row['id']: updated['equivalent_of']}
    assert verify_line(before, json.dumps(updated), links)
    with pytest.raises(ValueError, match='unrelated field'):
        verify_line(before, json.dumps(updated), {})
    with pytest.raises(ValueError, match='unrelated field'):
        verify_line(before, json.dumps(dict(updated, er='changed')), links)
    with pytest.raises(ValueError, match='literal value changed'):
        verify_line(before, json.dumps(updated).replace('comment', '\\u0063omment'), links)
