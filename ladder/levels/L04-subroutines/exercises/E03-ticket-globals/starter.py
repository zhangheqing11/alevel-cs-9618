next_number = 1   # global: the number of the next ticket
issued = 0        # global: how many tickets have been issued


def take_ticket() -> int:
    """Return the current next_number, then add 1 to next_number and to issued."""
    raise NotImplementedError


def reset_tickets(start: int) -> None:
    """Set next_number to start and issued to 0."""
    raise NotImplementedError
