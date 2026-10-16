def fields(book):
    return book.title, book.author, book.year, book.on_loan


def make_library(sol):
    books = [sol.make_book(*values) for values in [
        ("Dune", "Herbert", 1965), ("Emma", "Austen", 1815),
        ("Ubik", "Dick", 1969), ("Kim", "Kipling", 1901),
    ]]
    books[1].on_loan = True
    books[2].on_loan = True
    return books


def test_book_defaults(sol):
    """B1: a new record has all four initial field values."""
    book = sol.Book()
    assert fields(book) == ("", "", 0, False)
    assert book.on_loan is False


def test_make_book(sol):
    """B2: construct a Book with correct title/author/year and Boolean loan field."""
    book = sol.make_book("Dune", "Herbert", 1965)
    assert isinstance(book, sol.Book)
    assert fields(book) == ("Dune", "Herbert", 1965, False)
    assert book.on_loan is False


def test_independent_records(sol):
    """B3: changing fields of one Book leaves a second Book unchanged."""
    first, second = sol.Book(), sol.Book()
    first.title, first.author, first.year, first.on_loan = "One", "Writer", 2000, True
    assert fields(second) == ("", "", 0, False)


def test_library_queries(sol):
    """B4-B7: count Boolean loans, filter strictly before year, preserve order and records."""
    books = make_library(sol)
    original = [fields(book) for book in books]
    assert sol.count_on_loan(books) == 2
    assert sol.count_on_loan([]) == 0
    assert sol.titles_before(books, 1966) == ["Dune", "Emma", "Kim"]
    assert sol.titles_before(books, 1965) == ["Emma", "Kim"]
    assert sol.titles_before(books, 1800) == []
    assert [fields(book) for book in books] == original
