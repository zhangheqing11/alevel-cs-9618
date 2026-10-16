"""Real-source regressions for observed extraction failures (read-only PDFs)."""
from pathlib import Path
import sys
import pytest

sys.path.insert(0, str(Path(__file__).parent))
from pdf_text import DEFAULT_SOURCE_ROOT, extract_pdf
from split_qp import split_question_paper
from parse_ms import parse_mark_scheme


def source(name):
    path = DEFAULT_SOURCE_ROOT / "pastpapers" / name
    if not path.exists():
        pytest.skip("read-only source corpus unavailable")
    return extract_pdf(path)


def qp(name, label):
    return next(q for q in split_question_paper(source(name)) if q.label_hint == label)


def ms(name, label):
    return next(m for m in parse_mark_scheme(source(name)) if m.label == label)


def test_register_bits_and_actual_start_page_survive():
    leaf = qp("9618_s22_qp_11.pdf", "6(c)(i)")
    assert leaf.page == 14
    assert "0    1    1    0    1    1    0    1" in leaf.text
    assert "Opcode" in leaf.context
    assert "AND #2" in leaf.text


def test_top_level_context_is_inherited_by_later_leaf():
    leaf = qp("9618_s21_qp_11.pdf", "1(c)(iii)")
    assert "#FC238A" in leaf.context
    assert "00100011" in leaf.text


def test_same_line_label_and_mark_are_not_dropped():
    leaf = qp("9618_s23_qp_32.pdf", "11(a)(ii)")
    assert leaf.marks == 5
    assert leaf.page == 13
    assert leaf.text.count("Complete the given pseudocode") == 1


def test_low_mark_box_is_not_treated_as_footer():
    leaf = qp("9618_s24_qp_13.pdf", "7(b)")
    assert leaf.marks == 3
    assert leaf.page == 13
    assert "Artificial Intelligence" in leaf.text


def test_rotated_mark_scheme_keeps_three_languages():
    block = ms("9618_s22_ms_41.pdf", "1(a)")
    assert block.marks == 2
    assert "Java" in block.text and "VB.NET" in block.text and "Python" in block.text


def test_headerless_mark_scheme_continuation_is_retained():
    block = ms("9618_s23_ms_42.pdf", "3(a)(i)")
    assert block.page == 23
    assert block.marks == 5
    assert "Java" in block.text and "VB.NET" in block.text and "Python" in block.text
    assert "class Employee" in block.text


def test_missing_printed_mark_stays_unknown():
    block = ms("9618_s25_ms_12.pdf", "7(b)(ii)")
    assert block.marks is None
    assert "0000 0011" in block.text


def test_ms_typographic_question_label_is_normalized():
    block = ms("9618_s22_ms_13.pdf", "5(b)(iii)")
    assert block.marks == 2
    assert "Validation" in block.text


def test_array_indices_are_not_mark_boxes():
    leaves = split_question_paper(source("9618_s25_qp_33.pdf"))
    assert sum(q.marks for q in leaves) == 75
    assert len(leaves) == 26
