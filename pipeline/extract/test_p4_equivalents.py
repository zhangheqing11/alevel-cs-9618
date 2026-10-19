"""Guard D42 ③ / D41 ⑤ against false links, chains and unrelated field changes."""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
from p4_equivalents import candidates, verify_line


def pair(paper='9618_s22_43', q='1(a)'):
    base = {'component': 4, 'q': q, 'marks': 2, 'stem': 'same text', 'stem_ctx': 'given',
            'ms_text': 'own MS', 'equivalent_of': None}
    target = dict(base, id=f'9618_s22_41:{q}', paper='9618_s22_41')
    other = dict(base, id=f'{paper}:{q}', paper=paper)
    return {r['id']: r for r in (target, other)}


@pytest.mark.parametrize('field', ['stem', 'stem_ctx', 'ms_text'])
def test_rejects_any_text_field_difference(field):
    rows = pair()
    rows['9618_s22_43:1(a)'][field] += ' changed'
    assert candidates(rows) == []


def test_ignores_whitespace_and_respects_existing_links_and_chains():
    rows = pair()
    rows['9618_s22_43:1(a)']['stem'] = ' same\n text '
    assert len(candidates(rows)) == 1
    rows['9618_s22_41:1(a)']['equivalent_of'] = '9618_s21_41:1(a)'   # target is itself a link: no chain
    assert candidates(rows) == []
    rows['9618_s22_41:1(a)']['equivalent_of'] = None
    rows['9618_s22_43:1(a)']['equivalent_of'] = '9618_s22_41:1(a)'
    assert candidates(rows) == []


def test_only_component_4_non_41_rows_and_same_session_twin():
    rows = pair(paper='9618_s23_43')           # twin must be same session/year
    assert candidates(rows) == []
    rows = pair(paper='9618_s22_42')
    assert len(candidates(rows)) == 1
    assert all(r['paper'] != '9618_s22_41' for r, _ in candidates(rows))


def test_d41_extra_pair_is_a_candidate_despite_stem_difference():
    base = {'component': 3, 'marks': 5, 'q': '10(b)', 'stem': 'a', 'stem_ctx': 'c', 'ms_text': 'm', 'equivalent_of': None}
    rows = {'9618_s24_31:10(b)': dict(base, id='9618_s24_31:10(b)', paper='9618_s24_31'),
            '9618_s24_33:10(b)': dict(base, id='9618_s24_33:10(b)', paper='9618_s24_33', stem='a ←')}
    assert [r['id'] for r, _ in candidates(rows)] == ['9618_s24_33:10(b)']


def test_verify_line_allows_only_declared_changes():
    row = {'id': 'x:1', 'paper': 'x', 'equivalent_of': None, 'tag_note': 'old', 'er': 'comment'}
    before = json.dumps(row)
    linked = dict(row, equivalent_of='y:1')
    assert verify_line(before, json.dumps(linked), {'equivalent_of': 'y:1'})
    with pytest.raises(ValueError, match='unrelated field'):
        verify_line(before, json.dumps(linked), {})
    with pytest.raises(ValueError, match='unrelated field'):
        verify_line(before, json.dumps(dict(linked, er='changed')), {'equivalent_of': 'y:1'})
    with pytest.raises(ValueError, match='literal value changed'):
        verify_line(before, json.dumps(linked).replace('comment', '\\u0063omment'), {'equivalent_of': 'y:1'})
    retagged = dict(row, tag_note='new')
    assert verify_line(before, json.dumps(retagged), {'tag_note': 'new'})
