import pytest
from testkit import feed_input, output_lines

@pytest.mark.parametrize(
    'name, row, seat, expected',
    [
        ('Mia', '12', '7', ['Your code is Mia-1207', 'Row 12, seat 7']),
        ('Bo', '3', '45', ['Your code is Bo-345', 'Row 3, seat 45']),
        ('Ann Lee', '1', '1', ['Your code is Ann Lee-101', 'Row 1, seat 1']),
        ('Zed', '99', '99', ['Your code is Zed-9999', 'Row 99, seat 99']),
    ],
)
def test_ticket_code(sol, monkeypatch, capsys, name, row, seat, expected):
    """B1-B4: conversion, arithmetic code and output."""
    feed_input(monkeypatch, name, row, seat)
    sol.ticket_code()
    assert output_lines(capsys.readouterr().out) == expected
