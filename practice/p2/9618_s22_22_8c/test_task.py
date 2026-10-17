import pytest
import itertools
from pathlib import Path
from testkit import output_lines, feed_input
from practice.p2._test_support import watch_open, no_shortcuts

def test_format_and_unique_characters(sol, monkeypatch):
    """9618_s22_22:8(c) MP1–MP6: reject duplicates and form 3 groups without requiring a fixed output."""
    sequence = itertools.cycle("aaAbBcCdDeEfF0123456789ghijklmnopqrstuvwxyzGHIJKLMNOPQRSTUVWXYZ")
    monkeypatch.setattr(sol, "RandomChar", lambda: next(sequence))
    result = sol.GeneratePassword()
    assert isinstance(result, str)
    assert len(result) == 14
    groups = result.split("-")
    assert [len(group) for group in groups] == [4, 4, 4]
    chars = "".join(groups)
    assert chars.isascii() and chars.isalnum() and len(set(chars)) == 12


def test_fresh_password_each_call(sol, monkeypatch):
    """9618_s22_22:8(c) MP1,MP2,MP5: reset result on each call; no fixed random output."""
    for _ in range(2):
        sequence = iter("0123456789ab")
        monkeypatch.setattr(sol, "RandomChar", lambda: next(sequence))
        result = sol.GeneratePassword()
        assert len(result) == 14 and len(set(result.replace("-", ""))) == 12
