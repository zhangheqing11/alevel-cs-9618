"""Tests for ER label parsing, upward fallback, and the only-`er` row rewrite."""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import apply_er as A  # noqa: E402
import extract_er as E  # noqa: E402


def body(*lines, page=1):
    return [(page, line) for line in lines]


def labels(entries):
    return {tuple(e['labels']): E.join_lines(e['lines']) for e in entries}


def parse(*lines):
    anomalies = []
    return E.parse_question_body(6, body(*lines), anomalies, 'p'), anomalies


# ---------------------------------------------------------------- label parsing

def test_spaced_unspaced_and_inline_labels():
    entries, _ = parse('(a)', 'First.', '(b) (i)', 'Second.', '(ii)', 'Third.',
                       '(c)(i)', 'Fourth.', '(iii)  Fifth inline.')
    got = labels(entries)
    assert got[('6(a)',)] == 'First.'
    assert got[('6(b)(i)',)] == 'Second.'
    assert got[('6(b)(ii)',)] == 'Third.'
    assert got[('6(c)(i)',)] == 'Fourth.'
    assert got[('6(c)(iii)',)] == 'Fifth inline.'


def test_question_level_preamble_gets_the_bare_question_label():
    entries, _ = parse('Whole-question remark.', 'Still the remark.', '(a)', 'Part.')
    got = labels(entries)
    assert got[('6',)] == 'Whole-question remark. Still the remark.'
    assert got[('6(a)',)] == 'Part.'


def test_combined_roman_comment_is_stored_for_both_labels():
    entries, anomalies = parse('(a)', 'x', '(ii)(iii) Both parts were fine.')
    both = [e for e in entries if len(e['labels']) == 2][0]
    assert both['labels'] == ['6(a)(ii)', '6(a)(iii)']
    assert anomalies


def test_out_of_sequence_brackets_stay_text():
    entries, anomalies = parse('(c)', 'See the rule in', '(a).', 'again.', '(d)', 'Last.')
    got = labels(entries)
    assert got[('6(c)',)] == 'See the rule in (a). again.'
    assert ('6(d)',) in got
    assert any('(a).' in a for a in anomalies)


def test_repeated_label_is_kept_apart_and_flagged():
    entries, anomalies = parse('(b)', 'One.', '(b)', 'Two.')
    dup = [e for e in entries if e.get('duplicate')]
    assert len(dup) == 1 and dup[0]['labels'] == ['6(b)']
    assert labels([e for e in entries if not e.get('duplicate')])[('6(b)',)] == 'One.'
    assert E.join_lines(dup[0]['lines']) == 'Two.'
    assert any('printed twice' in a for a in anomalies)


def test_roman_before_any_letter_is_text():
    entries, _ = parse('(ii) is mentioned first.', '(a)', 'x')
    assert labels(entries)[('6',)] == '(ii) is mentioned first.'


# ---------------------------------------------------------------- text normalisation

def test_join_lines_merges_whitespace_and_hyphen_wraps():
    assert E.join_lines(['a  b ', '', 'many-to-', 'many link', 'end -', 'x']) == 'a b many-to-many link end - x'


def test_private_use_glyphs_follow_d26_d29_and_unknown_ones_fail():
    assert E.normalise('x  1 ') == 'x ← 1 ∞'
    with pytest.raises(E.ERError):
        E.normalise('')


class FakePage:
    def __init__(self, text):
        self.text = text

    def get_text(self):
        return self.text


HEADER = ('Cambridge International Advanced Subsidiary and Advanced Level \n9618 Computer Science June 2024 \n'
          'Principal Examiner Report for Teachers \n \n© 2024 \n')


def test_paper_with_question_continued_on_next_page():
    doc = [FakePage(HEADER + 'COMPUTER SCIENCE\nPaper 9618/21\nFundamental\nKey messages\nBe precise.\n'
                    'General comments\nRead the question.\nComments on specific questions\n'
                    'Question 1\n(a)\nGood.\n(b) (i)\nStarts here\n'),
           FakePage(HEADER + 'and continues here.\n(ii)\nOK.\nQuestion 2\nAll fine.\n'),
           FakePage(HEADER + 'COMPUTER SCIENCE\nPaper 9618/22\nKey messages\nOther.\nQuestion 1\nWhole.\n')]
    papers = E.split_papers(E.page_lines(doc))
    assert [p for (p, _), _ in papers] == ['9618/21', '9618/22']
    anomalies = []
    out = E.parse_paper('9618/21', papers[0][1], '9618_s24_21', anomalies)
    by = {e['label']: e for e in out}
    assert by['1(b)(i)']['text'] == 'Starts here and continues here.' and by['1(b)(i)']['page'] == 1
    assert by['1(b)(ii)']['page'] == 2 and by['2']['text'] == 'All fine.'
    assert by['_general']['text'].startswith('Key messages Be precise. General comments Read the question.')
    assert not anomalies
    assert all('COMPUTER SCIENCE' not in e['text'] for e in out)


def test_misprinted_paper_heading_is_fixed_up_by_table():
    assert E.HEADING_FIXUPS[('w23', '9618/33', 1)] == '9618/31'


# ---------------------------------------------------------------- matching

def test_nearest_enclosing_label_with_scope_prefix():
    labels_ = {'6(c)': dict(text='Parent.'), '6(c)(ii)': dict(text='Own.'), '7': dict(text='Q.')}
    assert A.excerpt_for('6(c)(ii)', labels_) == ('Own.', '6(c)(ii)')
    assert A.excerpt_for('6(c)(i)', labels_) == ('[Q6(c)] Parent.', '6(c)')
    assert A.excerpt_for('7(a)(i)', labels_) == ('[Q7] Q.', '7')
    assert A.excerpt_for('8', labels_) == (None, None)
    assert A.excerpt_for('6(d)', labels_) == (None, None)


def test_single_finer_label_is_attached_with_er_prefix():
    rows = {'6', '7(a)', '7(b)'}
    one = {'6(a)': dict(text='Only part.')}
    assert A.excerpt_for('6', one, rows) == ('[ER 6(a)] Only part.', '6(a)')
    two = {'6(a)': dict(text='A.'), '6(b)': dict(text='B.')}
    assert A.excerpt_for('6', two, rows) == (None, None)             # ambiguous: never guessed
    assert A.excerpt_for('6', one, {'6', '6(a)(i)'}) == (None, None)  # row has sub-rows: no rule
    assert A.excerpt_for('7(a)', one, rows) == (None, None)


def test_label_fixup_relabels_second_block_and_keeps_printed_label():
    anomalies = []
    lines = [(1, 'Question 1'), (1, '(a)'), (1, 'A.'), (1, '(b)'), (1, 'B.'), (2, '(b)'), (2, 'C.')]
    key = ('9618_s24_22', '1(b)')
    E.LABEL_FIXUPS[key] = '1(c)'
    try:
        out = E.parse_paper('9618/22', [(1, 'Key messages'), (1, 'k')] + lines, '9618_s24_22', anomalies)
    finally:
        del E.LABEL_FIXUPS[key]
    by = {e['label']: e for e in out}
    assert by['1(c)']['text'] == 'C.' and by['1(c)']['er_label_printed'] == '1(b)'
    assert by['1(b)']['text'] == 'B.' and 'duplicate_label' not in by['1(c)']


# ---------------------------------------------------------------- row rewriting

def test_merge_line_only_touches_er_and_keeps_every_other_byte():
    original = ' {"id" : "p:1", "stem":"\\u4e2d \\"x\\"", "marks":1e0, "nested": {"x": [1, 2]}}\r\n'
    added = A.merge_line(original, 'T "q" é')
    assert A.merge_line(added, None) == original
    assert added.endswith('}\r\n') and '"stem":"\\u4e2d \\"x\\""' in added
    assert A.merge_line(added, 'T "q" é') == added          # idempotent
    changed = A.merge_line(added, 'new')
    assert json.loads(changed)['er'] == 'new'
    assert changed.replace('"er":"new"', '"er":"T \\"q\\" é"') == added


def test_remove_er_in_the_middle_or_at_the_start():
    assert A.merge_line('{"a":1, "er": "x", "b":2}\n', None) == '{"a":1, "b":2}\n'
    assert A.merge_line('{"er":"x","b":2}\n', None) == '{"b":2}\n'
    assert A.merge_line('{"a":1}\n', None) == '{"a":1}\n'


@pytest.fixture
def corpus(tmp_path):
    (tmp_path / 'corpus/er').mkdir(parents=True)
    (tmp_path / 'corpus/rows/p2').mkdir(parents=True)
    er = [dict(paper='9618_s24_22', label='_general', text='G', page=1),
          dict(paper='9618_s24_22', label='1(a)', text='A.', page=2),
          dict(paper='9618_s24_22', label='2', text='Whole two.', page=2),
          dict(paper='9618_s24_22', label='2(a)(i)', text='Finer.', page=3),
          dict(paper='9618_s24_22', label='3', text='Dup.', page=3),
          dict(paper='9618_s24_22', label='3', text='Dup 2.', page=3, duplicate_label=True)]
    (tmp_path / 'corpus/er/s24.jsonl').write_text(''.join(json.dumps(e) + '\n' for e in er), encoding='utf-8')
    rows = [dict(id='9618_s24_22:1(a)', paper='9618_s24_22', q='1(a)', stem='é'),
            dict(id='9618_s24_22:2(a)', paper='9618_s24_22', q='2(a)', stem='x'),
            dict(id='9618_s24_22:2(b)', paper='9618_s24_22', q='2(b)', stem='y', er='stale'),
            dict(id='9618_s24_22:4', paper='9618_s24_22', q='4', stem='z', er='stale too')]
    (tmp_path / 'corpus/rows/p2/9618_s24_22.jsonl').write_text(
        ''.join(json.dumps(r, ensure_ascii=False, separators=(',', ':')) + '\n' for r in rows), encoding='utf-8')
    (tmp_path / 'corpus/rows/p2/9618_s26_22.jsonl').write_text(
        json.dumps(dict(id='9618_s26_22:1', paper='9618_s26_22', q='1')) + '\n', encoding='utf-8')
    return tmp_path


def test_apply_on_fixture_is_exact_idempotent_and_reports_unmatched(corpus):
    changes, stats, used = A.apply(corpus)
    path = corpus / 'corpus/rows/p2/9618_s24_22.jsonl'
    rows = [json.loads(l) for l in path.read_text(encoding='utf-8').splitlines()]
    assert [r.get('er') for r in rows] == ['A.', '[Q2] Whole two.', '[Q2] Whole two.', None]
    other = (corpus / 'corpus/rows/p2/9618_s26_22.jsonl').read_text().splitlines()
    assert all('er' not in json.loads(l) for l in other)
    assert stats['9618_s24_22']['inherited'] == 2 and stats['9618_s24_22']['no_er'] == 1
    again, _, _ = A.apply(corpus, check=True)
    assert again == {}
    kinds = {(u['label'], u['kind']) for u in A.unmatched(corpus)}
    assert ('2(a)(i)', 'finer_than_row') in kinds and ('3', 'no_such_row') in kinds and ('3', 'duplicate') in kinds


def test_check_mode_never_writes(corpus):
    before = (corpus / 'corpus/rows/p2/9618_s24_22.jsonl').read_bytes()
    changes, _, _ = A.apply(corpus, check=True)
    assert changes and (corpus / 'corpus/rows/p2/9618_s24_22.jsonl').read_bytes() == before


def test_real_corpus_is_current():
    changes, _, _ = A.apply(A.ROOT, check=True)
    assert changes == {}
