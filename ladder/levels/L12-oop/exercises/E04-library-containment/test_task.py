def build_library(sol):
    library = sol.Library()
    for title in ["Dune", "Emma", "Ubik", "Kim", "Ulysses"]:
        assert library.AddBook(sol.Book(title)) is True
    return library


def test_book(sol):
    """B1: book title/loan getters, reject lending twice, return book resets its loan status."""
    book = sol.Book("Dune")
    assert book.GetTitle() == "Dune"
    assert book.GetOnLoan() is False
    assert book.LendOut() is True
    assert book.LendOut() is False
    book.ReturnBook()
    assert book.GetOnLoan() is False


def test_library_storage(sol):
    """B2: private fixed array of five distinct Book objects, only used entries searched."""
    library = sol.Library()
    assert set(vars(library)) == {"_Library__Books", "_Library__NumberBooks"}
    books = vars(library)["_Library__Books"]
    assert type(books) is list
    assert len(books) == 5
    assert all(isinstance(book, sol.Book) for book in books)
    assert len({id(book) for book in books}) == 5
    assert all(book.GetTitle() == "" for book in books)
    assert library.FindBook("") == -1


def test_capacity_and_search(sol):
    """B3-B4: store five books, reject sixth, find first/interior/last or report not found."""
    library = build_library(sol)
    assert library.AddBook(sol.Book("Extra")) is False
    assert library.FindBook("Emma") == 1
    assert library.FindBook("Ulysses") == 4
    assert library.FindBook("Nope") == -1


def test_lending_and_count(sol):
    """B5-B6: delegate lending, reject repeat/absent title and count exactly one loan."""
    library = build_library(sol)
    assert library.LendBook("Emma") is True
    assert library.LendBook("Emma") is False
    assert library.LendBook("Nope") is False
    assert library.CountOnLoan() == 1


def test_containment(sol):
    """B7: Library contains books and does not inherit from Book."""
    assert not issubclass(sol.Library, sol.Book)


def test_find_first_duplicate(sol):
    """English task: FindBook returns the first added book with a matching title."""
    library = sol.Library()
    for title in ["Dune", "Emma", "Dune"]:
        assert library.AddBook(sol.Book(title)) is True
    assert library.FindBook("Dune") == 0
