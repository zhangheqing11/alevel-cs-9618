next_number = 1
issued = 0


def take_ticket() -> int:
    global next_number, issued
    this_number = next_number
    next_number = next_number + 1
    issued = issued + 1
    return this_number


def reset_tickets(start: int) -> None:
    global next_number, issued
    next_number = start
    issued = 0
