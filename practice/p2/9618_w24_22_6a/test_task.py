from random import Random
import re
from testkit import output_lines


def test_skip_holes_different_fillings_and_last_slots(sol,monkeypatch,capsys):
    """9618_w24_22:6(a) MP1-MP7: valid random selection and formatted output."""
    sol.Filling=['']*35
    sol.Filling[0]='Cheese'
    sol.Filling[34]='Onion'
    sol.Bread=['']*10
    sol.Bread[9]='Brown'
    rng=Random(42)
    monkeypatch.setattr(sol,'RAND',lambda limit:rng.random()*limit)
    for _ in range(20):
        sol.Special()
        lines=output_lines(capsys.readouterr().out)
        assert len(lines)==1
        match=re.fullmatch(r'The daily special is (Cheese|Onion) and (Cheese|Onion) on Brown bread\.',lines[0])
        assert match and match[1]!=match[2]


def test_qp_example_values(sol,monkeypatch,capsys):
    """9618_w24_22:6(a) MP1-MP7: QP arrays, no empty or duplicate fillings."""
    rng=Random(2024)
    monkeypatch.setattr(sol,'RAND',lambda limit:rng.random()*limit)
    valid_fillings=set(sol.Filling)-{''}
    valid_bread=set(sol.Bread)-{''}
    for _ in range(10):
        sol.Special()
        lines=output_lines(capsys.readouterr().out)
        assert len(lines)==1
        match=re.fullmatch(r'The daily special is (.+) and (.+) on (.+) bread\.',lines[0])
        assert match
        assert match[1] in valid_fillings and match[2] in valid_fillings
        assert match[1]!=match[2] and match[3] in valid_bread
