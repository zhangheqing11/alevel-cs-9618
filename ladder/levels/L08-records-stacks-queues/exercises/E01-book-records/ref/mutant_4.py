# M4: intentional fault from spec.md.
class Book:
    """Record type Book."""

    def __init__(self) -> None:
        self.title = ""
        self.author = ""
        self.year = 0
        self.on_loan = False


def make_book(title: str, author: str, year: int) -> Book:
    book = Book()
    book.title = title
    book.author = author
    book.year = year
    book.on_loan = False
    return book


def count_on_loan(books: list[Book]) -> int:
    count = 0
    for book in books:
        if book.on_loan == "TRUE":
            count = count + 1
    return count


def titles_before(books: list[Book], year: int) -> list[str]:
    titles = []
    for book in books:
        if book.year < year:
            titles.append(book.title)
    return titles
