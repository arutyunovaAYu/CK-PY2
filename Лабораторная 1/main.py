# TODO Написать 3 класса с документацией и аннотацией типов

#if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    #pass
import doctest

class Cat:
    def __init__(self, color: str, count_paws, breed: str):
        """
        Создание и подготовка к работе объекта "Cat"

        :param color: цвет кота
        :param count_paws: число лап
        :param breed: порода кота

        Примеры:
        >>> Cat_1 = Cat('Черный', 4, 'Сибирская') #инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError('Цвет кошки должен быть типа str')
        self.color = color
        if count_paws <= 0:
            raise TypeError('Точно ли это кошка?')
        self.count_paws = count_paws
        if not isinstance(breed, str):
            raise TypeError('Порода кошки должна быть типа str')
        self.breed = breed

    def is_cat_exist(self) -> bool:
        """
        Функция, которая проверяет существует ли кот

        :return: Существует ли кот

        Примеры:
        >>> Cat_1 = Cat('Черный', 4, 'Сибирская')
        >>> Cat_1.is_cat_exist()
        """
        ...

    def touch_cat(self, cat: int) -> None:
        """
        Функция, которая гладит кота

        :param cat: Наличие кота

        :raise ValueError: Кота нет

        Примеры:
        >>> Cat_1 = Cat('Черный', 4, 'Сибирская')
        >>> Cat_1.touch_cat(1)
        """

        if not isinstance(cat, int):
            raise TypeError("Число котов должно быть типа int")
        if cat <= 0:
            raise ValueError("Кот должен существовать")
        ...

    def feed_cat(self, food:str) -> None:
        """
        Функция, которая кормит кота

        :param food: Наличие еды

        :raise ValueError: Еды нет

        Примеры:
        >>> Cat_1 = Cat('Черный', 4, 'Сибирская')
        >>> Cat_1.touch_cat(5)
        """

        if not isinstance(food, int):
            raise TypeError("Количество еды должно быть типа int")
        if food <= 0:
            raise ValueError("Еда должна быть")
        ...


class Fridge:
    def __init__(self, brand: str, count_chambers: int, article: str):
        """
        Создание и подготовка к работе объекта "Fridge"

        :param brand: фирма холодильника
        :param count_chambers: число камер
        :param article: артикул холодильника

        Примеры:
        >>> Fridge_1 = Fridge('Атлант', 3, 'ATF23O9FG') #инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError('Бренд холодильника должен быть типа str')
        self.brand = brand
        if not count_chambers > 1:
            raise ValueError('Это не холодильник')
        self.count_chambers = count_chambers
        if not isinstance(article, str):
            raise TypeError('Артикул холодильника должен быть типа str')
        self.article = article

        def open_chamber(self, chamber: str) -> None:
            """
            Функция, которая открывает камеру холодильника

            :param chamber: Наличие камеры

            :raise ValueError: Камеры нет

            Примеры:
            >>> Fridge_1 = Fridge('Атлант', 3, 'ATF23O9FG')
            >>> Fridge_1.open_chamber(1)
            """

            if not isinstance(chamber, int):
                raise TypeError("Количество камер должно быть типа int")
            if chamber <= 0:
                raise ValueError("Должна быть хотя бы одна камера")
            ...

        def wash_fridge(self, fridge: str) -> None:
            """
            Функция, которая моет холодильник

            :param fridge: Наличие холодильника

            :raise ValueError: Холодильника нет

            Примеры:
            >>> Fridge_1 = Fridge('Атлант', 3, 'ATF23O9FG')
            >>> Fridge_1.wash_fridge(1)
            """

            if not isinstance(fridge, int):
                raise TypeError("Количество олодильников должно быть типа int")
            if fridge <= 0:
                raise ValueError("Должен быть хотя бы один холодильник")
            ...


class Garland:
    def __init__(self, brand: str, light: str, length: int):
        """
        Создание и подготовка к работе объекта "Garland"

        :param brand: фирма гирлянды
        :param light: цвет гирлянды
        :param length: длина гирлянды

        Примеры:
        >>> Garland_1 = Garland('Радость ёлки', 'жёлтый', 2) #инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError('Бренд гирлянды должен быть типа str')
        self.brand = brand
        if not isinstance(light, str):
            raise TypeError('Свет гирлянды должен быть типа str')
        self.light = light
        if length <= 0:
            raise ValueError('У Вас нет гирлянды')
        self.length = length

        def on_garland(self, garland: int) -> None:
            """
            Функция, которая включает гирлянду

            :param garland: Наличие гирлянды

            :raise ValueError: Гирлянды нет

            Примеры:
            >>> Garland_1 = Garland('Радость ёлки', 'жёлтый', 2)
            >>> Garland_1.on_garland(1)
            """

            if not isinstance(garland, int):
                raise TypeError("Количество гирлянд должно быть типа int")
            if garland <= 0:
                raise ValueError("Должна быть хотя бы одна гирлянда")
            ...

        def hang_garland(self, wall: int) -> None:
            """
            Функция, которая вешает гирлянду

            :param wall: Наличие стены

            :raise ValueError: Стены нет

            Примеры:
            >>> Garland_1 = Garland('Радость ёлки', 'жёлтый', 2)
            >>> Garland_1.hang_garland(1)
            """

            if not isinstance(wall, int):
                raise TypeError("Количество стен должно быть типа int")
            if wall <= 0:
                raise ValueError("Должна быть хотя бы одна стена")
            ...


if __name__ == "__main__":
    doctest.testmod()
    pass