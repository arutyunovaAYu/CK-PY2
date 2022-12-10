# TODO Написать 3 класса с документацией и аннотацией типов

#if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    #pass

class Cat:
    def __init__(self, color: str, count_paws, breed: str):
        if not isinstance(color, str):
            raise TypeError('Цвет кошки должен быть типа str')
        self.color = color
        if count_paws <= 0:
            raise TypeError('Точно ли это кошка?')
        self.count_paws = count_paws
        if not isinstance(breed, str):
            raise TypeError('Порода кошки должна быть типа str')
        self.breed = breed


class Fridge:
    def __init__(self, brand: str, count_chambers: int, article: str):
        if not isinstance(brand, str):
            raise TypeError('Бренд холодильника должен быть типа str')
        self.brand = brand
        if not count_chambers > 1:
            raise ValueError('Это не холодильник')
        self.count_chambers = count_chambers
        if not isinstance(article, str):
            raise TypeError('Артикул холодильника должен быть типа str')
        self.article = article

        def broken(self):
            print('Холодильник не работает')
            self.health = 0


class Garland:
    def __init__(self, brand: str, light: str, length: int):
        if not isinstance(brand, str):
            raise TypeError('Бренд гирлянды должен быть типа str')
        self.brand = brand
        if not isinstance(light, str):
            raise TypeError('Свет гирлянды должен быть типа str')
        self.light = light
        if length <= 0:
            raise ValueError('У Вас нет гирлянды')
        self.length = length


if __name__ == "__main__":
    Cat_1 = Cat('Черный', 4, 'Сибирская')
    Fridge_1 = Fridge('Атлант', 3, 'ATF23O9FG')
    Garland_1 = Garland('Радость ёлки', 'жёлтый', 2)
    import doctest

    doctest.testmod()
    pass