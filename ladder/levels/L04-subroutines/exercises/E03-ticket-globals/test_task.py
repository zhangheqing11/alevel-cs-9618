def test_initial_state(sol):
    """B1: fresh module starts at ticket 1 and zero issued tickets."""
    assert (sol.next_number, sol.issued) == (1, 0)


def test_take_three(sol):
    """B2, B5: return successive integers and update both global counters."""
    values = [sol.take_ticket() for _ in range(3)]
    assert values == [1, 2, 3]
    assert all(type(value) is int for value in values)
    assert (sol.next_number, sol.issued) == (4, 3)


def test_reset(sol):
    """B3: reset changes the start and resets the issued counter."""
    sol.reset_tickets(100)
    assert [sol.take_ticket(), sol.take_ticket()] == [100, 101]
    assert (sol.next_number, sol.issued) == (102, 2)


def test_reset_zero(sol):
    """B4: reset to zero after issuing a ticket, without retaining old counts."""
    sol.take_ticket()
    sol.reset_tickets(0)
    assert sol.take_ticket() == 0
    assert sol.issued == 1
