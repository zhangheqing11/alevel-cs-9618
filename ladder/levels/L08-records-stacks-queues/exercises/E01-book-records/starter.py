class Book:
    """Record type Book."""

    def __init__(self) -> None:
        raise NotImplementedError   # set title, author, year, on_loan to their initial values


def make_book(title: str, author: str, year: int) -> Book:
    """Return a new Book with the given fields; on_loan is False."""
    raise NotImplementedError


def count_on_loan(books: list[Book]) -> int:
    """Return how many books are on loan."""
    raise NotImplementedError


def titles_before(books: list[Book], year: int) -> list[str]:
    """Return the titles of books published before year, in list order."""
    raise NotImplementedError
