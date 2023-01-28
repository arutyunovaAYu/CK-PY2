class Book:
    """ Базовый класс книги. """
    def init(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError('Значение name должно соответствовать типу str')
        self._name = name
        if not isinstance(author, str):
            raise TypeError('Значение author должно соответствовать типу str')
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def str(self):
        return f"Книга: {self._name}. Автор: {self._author}"

    def repr(self):
        return f"{self.class.name}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """ Дочерний класс книги. """
    def init(self, name: str, author: str, pages: int):
        super().init(name, author)
        if not isinstance(pages, int):
            raise TypeError('Значение pages должно соответствовать типу int')
        if not pages > 0:
            raise ValueError('Значение pages должно быть положительным числом')
        self.pages = pages

    def str(self):
        return f"Книга: {self._name}. Автор: {self._author}. Количество страниц: {self.pages}"

    def repr(self):
        super_repr = super().repr()
        return f"{super_repr}"


class AudioBook(Book):
    """ Дочерний класс книги. """
    def init(self, name: str, author: str, duration: float):
        super().init(name, author)
        if not isinstance(duration, float):
            raise TypeError('Значение duration должно соответствовать типу float')
        if not duration > 0:
            raise ValueError('duration должно быть положительным числом')
        self.duration = duration

    def str(self):
        return f"Книга: {self._name}. Автор: {self._author}. Продолжительность: {self.duration}"

    def repr(self):
        super_repr = super().repr()
        return f"{super_repr}"