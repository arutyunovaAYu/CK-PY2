from typing import Union


class Animal:
    """
    Базовый класс Animal
    :param color: цвет животного, str
    :param model: название животного, str
    :param weight: вес животного, int or float
    :raise: TypeError, неправильный типу
    :raise: ValueError,  значение нереальное
    """
    def __init__(self, model: str, color: str, weight: Union[int, float]):
        """ Валидация атрибутов объекта класса Animal """
        if not isinstance(model, str):
            raise TypeError("The model should be a string")
        self._model = model

        if not isinstance(color, str):
            raise TypeError("The color should be a string")
        self._color = color

        if not isinstance(weight, tuple([int, float])):
            raise TypeError("The weight should be an int or float")
        if weight <= 0:
            raise ValueError("The weight should be positive")
        self._weight = weight

    def __str__(self) -> str:
        return f'Animal {self._color} {self._model}. Масса: {self._weight} кг.'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}модель={self._model!r}, (цвет={self._color!r}, масса={self._fly_weight})'

    # Защищаем базовые аргументы и даём возможность перезаписи
    # Модель, как в примере с автором книги, менять запрещаем.
    @property
    def model(self) -> str:
        """ получаем модель животного """
        return self._model

    @property
    def color(self) -> str:
        """ получаем цвет животного """
        return self._color

    @color.setter
    def color(self, new_color: str) -> None:
        """ дадим новый цвет """
        if not isinstance(new_color, str):
            raise TypeError("The color should be a string")
        self._color = new_color

    @property
    def weight(self) -> int or float:
        """ установим массу """
        return self._weight

    @weight.setter
    def weight(self, new_weight: Union[int, float]) -> None:
        """ новая масса """
        if not isinstance(new_weight, tuple([int, float])):
            raise TypeError("The weight should be an int or float")
        if new_weight <= 0:
            raise ValueError("The weight should be positive")
        self._weight = new_weight


    def need_food(self) -> float:
        """
        необходимое количество еды для животного.
        Наследуется в неизменном виде дочерними классами.
        """
        return (self._weight * 25)

    def activity(self) -> float:
        """
        расход энергии ккал/час
        Этот метод может быть переопределен в дочерних классах для расчета расхода калорий
        иным образом.
        """
        return None

    def need_love(self, max_weight: Union[int, float]) -> float:
        """
        сколько любви требуется животному
        вес животного, умноженный на обратную активность
        :param max_weight: максимально допустимая масса в кг, int or float
        """
        # Параметр max_weight указан здесь, а не в __init__, чтобы передавать его только тогда, когда нужно
        if not isinstance(max_weight, tuple([int, float])):
            raise TypeError("The max weight should be an int or float")
        if max_weight <= 0:
            raise ValueError("The max weight should be positive")
        self.max_weight = max_weight
        return self.max_weight - self._weight


class Bird(Animal):
    """
    Дочерний класс птица
    :param count_wings: количество крыльев, int
    """
    def __init__(self, model, color, weight, count_wings: int):  # аннотацию типов убрала, т.к. она выше
        super().__init__(model, color, weight)  # вызываем конструктор родительского класса для его расширения
        if not isinstance(count_wings, int):
            raise TypeError("The count_wings should be a int")
        self.count_wings = count_wings

    def __str__(self) -> str:
        return f'{super().__str__()} count wings: {self.count_wings}.'  # наследуем и дополняем __str__

    def __repr__(self) -> str:  # а вот метод __repr__ придется перегружать
        return f'{self.__class__.__name__}(модель={self._model!r}, цвет={self._color!r}, вес={self._weight}, количество крыльев={self.count_wings!r})'

    def need_love(self, max_weight: Union[int, float]) -> float:
        """ Допустим, для более легких животных любви нужно больше """
        super(Bird, self).need_love(max_weight)
        return (self.max_weight - self._weight) * 1000


class Cat(Animal):
    """
    Дочерний класс кошки
    :param moustache: возможность добавить усы ( да или нет), bool
    """
    def __init__(self, color, model, weight, moustache: bool):
        super().__init__(color, model, weight)
        if not isinstance(moustache, bool):
            raise TypeError("The moustache availability should be a string")
        self.moustache = moustache

    def __str__(self) -> str:
        return f'{super().__str__()} Возможность добавить усы: {self.moustache}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(цвет={self._color!r}, модель={self._model!r}, вес={self._weight}, усы={self.moustache})'

    def need_love(self, max_weight: Union[int, float]) -> float:
        super(Cat, self).need_love(max_weight)
        return self.max_weight - self._weight / 2


if __name__ == "__main__":
    animal = Animal('Поли', 'коричневый', 100)
    print(animal)

    bird = Bird('Летучка', 'черный', 1, 2)
    print(bird)
    print("need_love:", bird.need_love(10), "вениамины")

    cat = Cat('Васька', 'белый', 3, True)
    print(cat)
    print("need_food:", cat.need_food())  # наследуемый метод
    print("need_love:", cat.need_love(15))  # перегружаемый метод