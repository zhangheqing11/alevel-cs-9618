import pytest
from testkit import run_script


def test_program(candidate_path, exercise_dir):
    """B1: run complete program with supplied file and compare evidence output."""
    result = run_script(candidate_path, files_dir=exercise_dir / "files")
    assert result.returncode == 0
    assert result.lines == ["Pen: 1.20", "Notebook: 2.50", "Ruler: 0.80", "Total: 4.50"]


def test_missing_file(candidate_path):
    """B2: missing source is handled and the main program reports no products."""
    result = run_script(candidate_path)
    assert result.returncode == 0
    assert result.lines == ["File not found", "No products"]


def test_empty_file(candidate_path, tmp_path):
    """B3: empty Products.txt produces only No products."""
    (tmp_path / "Products.txt").write_bytes(b"")
    result = run_script(candidate_path, files_dir=tmp_path)
    assert result.returncode == 0
    assert result.lines == ["No products"]


def test_read_products(sol):
    """B4: populate parallel arrays with float prices and retain unused initial slots."""
    sol.ReadProducts("Products.txt")
    assert sol.NumberProducts == 3
    assert sol.ProductName == ["Pen", "Notebook", "Ruler"] + [""] * 7
    assert sol.ProductPrice[:3] == pytest.approx([1.2, 2.5, 0.8], abs=1e-9)
    assert all(type(value) is float for value in sol.ProductPrice[:3])
    assert sol.ProductPrice[3:] == [0.0] * 7


def test_initial_state(sol, capsys):
    """B5: real arrays with specified defaults, no main execution or output on import."""
    assert sol.ProductName == [""] * 10
    assert sol.ProductPrice == [0.0] * 10
    assert sol.NumberProducts == 0
    assert capsys.readouterr().out == ""
