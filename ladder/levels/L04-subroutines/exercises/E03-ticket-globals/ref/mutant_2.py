# M2: intentional fault from spec.md.
next_number = 1
issued = 0


def take_ticket() -> int:
    next_number = 1
    issued = 0
    this_number = next_number
    next_number = next_number + 1
    issued = issued + 1
    return this_number


def reset_tickets(start: int) -> None:
    global next_number, issued
    next_number = start
    issued = 0
