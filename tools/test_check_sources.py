"""Regression tests for the optional first-run source diagnostic."""
from pathlib import Path

from check_sources import configured_root, diagnose


def make_source_tree(root: Path) -> None:
    for relative, _ in (
        ("pastpapers", ""),
        ("official", ""),
        ("official/support", ""),
        ("official/specimen", ""),
    ):
        (root / relative).mkdir(parents=True, exist_ok=True)
    for relative, _ in (
        ("official/9618_syllabus_2027-2029.pdf", ""),
        ("official/9618_syllabus_update_2027-2029.pdf", ""),
        ("official/9618_pseudocode_guide_2027-2029.pdf", ""),
        ("pastpapers/9618_s24_qp_11.pdf", ""),
        ("pastpapers/9618_s24_ms_11.pdf", ""),
    ):
        (root / relative).write_bytes(b"placeholder")


def test_configured_root_preserves_default_and_env_override(monkeypatch, tmp_path):
    default, source = configured_root(env={})
    assert default.name == "sources"
    assert source == "documented default"

    custom = tmp_path / "my sources"
    selected, source = configured_root(env={"ALEVEL_CS_SOURCES": str(custom)})
    assert selected == custom
    assert source == "ALEVEL_CS_SOURCES"


def test_diagnose_missing_root_is_concise(tmp_path):
    issues = diagnose(tmp_path / "does-not-exist")
    assert issues == [f"sources root does not exist: {tmp_path / 'does-not-exist'}"]


def test_diagnose_reports_missing_core_inputs(tmp_path):
    (tmp_path / "pastpapers").mkdir()
    issues = diagnose(tmp_path)
    assert any("missing directory" in issue and "official" in issue for issue in issues)
    assert any("missing file" in issue and "pseudocode" in issue for issue in issues)
    assert any("no normalized question paper" in issue for issue in issues)


def test_diagnose_accepts_a_complete_minimal_tree(tmp_path):
    make_source_tree(tmp_path)
    assert diagnose(tmp_path) == []


def test_diagnose_rejects_a_file_as_root(tmp_path):
    root = tmp_path / "sources"
    root.write_text("not a directory", encoding="utf-8")
    assert diagnose(root) == [f"sources root is not a directory: {root}"]
