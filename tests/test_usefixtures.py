import pytest


@pytest.fixture
def clear_books_database() -> None:
    print("[FIXTURES] Удаляем все данные из БД")


@pytest.fixture
def fill_books_database() -> None:
    print("[FIXTURES] Создаём новые данные в БД")


@pytest.mark.usefixtures("fill_books_database")
def test_read_all_books_in_library():
    print("Reading all books in library")


@pytest.mark.usefixtures("clear_books_database", "fill_books_database")
# Важен порядок, если 1 поставили очистку БД, то она и выполнится первой
class TestLibrary:
    def test_read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...