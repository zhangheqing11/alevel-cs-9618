from testkit import run_script


def test_top_scorer(candidate_path, exercise_dir):
    """format example: numeric comparison, ties keep the first"""
    result = run_script(candidate_path, files_dir=exercise_dir / "files")
    assert result.returncode == 0, result.stderr
    assert result.lines == ["Top: Bo 10"]
