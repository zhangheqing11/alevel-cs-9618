import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import apply_p4  # noqa: E402
import check_p4  # noqa: E402

LINE = ('{"id":"P:1(a)","marks":2,"stem":"caf\\u00e9 \\"x\\"","er":"keep – me",'
        '"equivalent_of":null,"types":{"primary":"P4-AR-01","cross":[]},"tag_note":"old"}')
TAGS = {"P:1(a)": {"id": "P:1(a)", "primary": "P4-SQ-02", "cross": ["P4-AR-03"], "confidence": "high", "note": ""}}
POINTS = {"P:1(a)": {"id": "P:1(a)", "ms_max": None, "markpoints": [
    {"n": 1, "text": "a", "marks": 1, "skills": ["queue-array"]},
    {"n": 2, "text": "b", "marks": 1, "skills": ["module-header"]}]}}


def test_preserves_non_owned_bytes_and_replaces_stale_annotations():
    out = apply_p4.annotated_line(LINE, TAGS, POINTS)
    assert out.startswith('{"id":"P:1(a)","marks":2,"stem":"caf\\u00e9 \\"x\\"","er":"keep – me",'
                          '"equivalent_of":null,')
    row = json.loads(out)
    assert row["types"] == {"primary": "P4-SQ-02", "cross": ["P4-AR-03"]}
    assert row["tag_note"] == "" and row["er"] == "keep – me"
    assert "ms_max" not in row and len(row["markpoints"]) == 2
    assert apply_p4.annotated_line(out, TAGS, POINTS) == out  # idempotent


def test_duplicate_annotation_ids_rejected():
    with pytest.raises(ValueError):
        apply_p4.index_records([{"id": "x"}, {"id": "x"}])


def _data():
    return {"P:1(a)": {"marks": 2, "ms_text": "1 mark each\n • a\n • b"},
            "Q:1(a)": {"marks": 2, "ms_text": "1 mark each\n • a\n • b"}}


def test_validator_accepts_consistent_sources_and_inherited_copy():
    tags = dict(TAGS, **{"Q:1(a)": dict(TAGS["P:1(a)"], id="Q:1(a)")})
    points = dict(POINTS, **{"Q:1(a)": dict(POINTS["P:1(a)"], id="Q:1(a)")})
    check_p4.validate(_data(), tags, points, {"Q:1(a)": "P:1(a)"}, {"P4-SQ-02", "P4-AR-03"},
                      {"queue-array", "module-header"})


@pytest.mark.parametrize("mutate", [
    lambda t, p: p["P:1(a)"]["markpoints"][0].update(text="not in ms"),
    lambda t, p: p["P:1(a)"]["markpoints"][0].update(skills=["unknown-tag"]),
    lambda t, p: p["P:1(a)"]["markpoints"].pop(),
    lambda t, p: t["Q:1(a)"].update(primary="P4-AR-03"),
    lambda t, p: p.pop("Q:1(a)"),
])
def test_validator_rejects_bad_sources(mutate):
    import copy
    tags = {"P:1(a)": copy.deepcopy(TAGS["P:1(a)"]), "Q:1(a)": dict(copy.deepcopy(TAGS["P:1(a)"]), id="Q:1(a)")}
    points = {"P:1(a)": copy.deepcopy(POINTS["P:1(a)"]),
              "Q:1(a)": dict(copy.deepcopy(POINTS["P:1(a)"]), id="Q:1(a)")}
    mutate(tags, points)
    with pytest.raises(ValueError):
        check_p4.validate(_data(), tags, points, {"Q:1(a)": "P:1(a)"}, {"P4-SQ-02", "P4-AR-03"},
                          {"queue-array", "module-header"})
