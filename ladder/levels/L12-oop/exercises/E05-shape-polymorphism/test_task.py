import math
import pytest


def test_subclass_areas(sol):
    """B1: overridden methods return rectangle and full-precision circle areas."""
    assert sol.Rectangle(3, 4).GetArea() == pytest.approx(12, abs=1e-9)
    assert sol.Circle(1).GetArea() == pytest.approx(math.pi, abs=1e-9)


def test_base_shape(sol):
    """B2: the base class has zero area and correctly formatted description."""
    assert sol.Shape("Blob").GetArea() == pytest.approx(0.0, abs=1e-9)
    assert sol.Shape("Blob").Describe() == "Blob: 0.00"


def test_polymorphic_description(sol):
    """B3: inherited Describe dispatches GetArea on each subclass and formats two decimals."""
    assert sol.Circle(2).Describe() == "Circle: 12.57"
    assert sol.Rectangle(2.5, 4).Describe() == "Rectangle: 10.00"


def test_parent_initialisation(sol):
    """B4: constructors initialise the inherited name through the parent."""
    assert sol.Rectangle(3, 4).GetName() == "Rectangle"
    assert sol.Circle(1).GetName() == "Circle"


def test_total_area(sol):
    """B5: sum mixed shape objects uniformly, including empty list."""
    shapes = [sol.Rectangle(3, 4), sol.Circle(1), sol.Shape("Blob")]
    assert sol.TotalArea(shapes) == pytest.approx(12 + math.pi, abs=1e-9)
    assert sol.TotalArea([]) == pytest.approx(0.0, abs=1e-9)


def test_inheritance_and_single_description(sol):
    """B6: both classes inherit Shape; Describe is implemented only by the parent."""
    assert "Describe" not in sol.Rectangle.__dict__
    assert "Describe" not in sol.Circle.__dict__
    assert issubclass(sol.Rectangle, sol.Shape)
    assert issubclass(sol.Circle, sol.Shape)
