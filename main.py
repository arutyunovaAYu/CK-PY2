from pydantic import BaseModel
from typing import List

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book():
    def __init__(self, id_:int, name:str, pages:int):
         """
         Создание и подготовка к работе объекта "Book"
         :param id_: id книги
         :param name: название книги
         :param pages: количество страниц
         Примеры:
         >>> Book_1 = Book(0, 'Ada', 394) #инициализация экземпляра класса
         """
        if not isinstance(id_, int):
            raise TypeError('id_ должно быть типа int')
        if id_ < 0:
            raise ValueError('id_ должно быть положительным числом')
        self.id_ = id_
        if not isinstance(name, str):
            raise TypeError('name должно быть типа str')
        self.name = name
        if not isinstance(pages, int):
            raise TypeError('pages должно быть типа int')
        if pages < 0:
            raise ValueError('pages должно быть положительным числом')
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})"




# TODO написать класс Library
class Library:
    def __init__(self, books: list[Book] = None):
         """
         Создание и подготовка к работе объекта "Library"
         :param books: список книг
         """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self, id_: int):
         """
         Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
         :return: Если книг в библиотеке нет, то вернуть 1. Если книги есть, то вернуть идентификатор последней книги увеличенный на 1.
         """
        if len(self.books) == 0:
            return 1
        return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_: int):
        for i, books in enumerate(self.books):
            if books.id_ == id_:
                return i
        if not self.books:
               raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id(0))  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id(1))  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1