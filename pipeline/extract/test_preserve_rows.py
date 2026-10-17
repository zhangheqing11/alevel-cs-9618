"""Extraction reruns must preserve downstream annotation values and literals."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from run_all import write_jsonl


def test_rerun_preserves_all_downstream_literals_and_only_changes_link(tmp_path):
    path = tmp_path / 'paper.jsonl'
    before = ('{ "id":"paper:1", "stem":"same", "equivalent_of":null, '
              '"er":"\\u4e2d  \\nquote", "types": {"primary":"P3-X-01","cross":[]}, '
              '"tag_confidence":"low", "tag_note":"history", '
              '"markpoints":[{"n":1,"text":"x","marks":1,"skills":["assign-value"]}], '
              '"ms_max":1 }\n')
    path.write_text(before)
    write_jsonl(path, [{'id': 'paper:1', 'stem': 'same', 'equivalent_of': 'other:1'}])
    assert path.read_text() == before.replace('"equivalent_of":null', '"equivalent_of":"other:1"')
    write_jsonl(path, [{'id': 'paper:1', 'stem': 'same', 'equivalent_of': 'other:1'}])
    assert path.read_text() == before.replace('"equivalent_of":null', '"equivalent_of":"other:1"')


def test_rerun_updates_extracted_text_without_reverting_or_dropping_er(tmp_path):
    path = tmp_path / 'paper.jsonl'
    before = '{"id":"p:1","stem":"old","er":"comment"}\n'
    path.write_text(before)
    write_jsonl(path, [{'id': 'p:1', 'stem': 'new'}])
    assert path.read_text() == before.replace('"old"', '"new"')
