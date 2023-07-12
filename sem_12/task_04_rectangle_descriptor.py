"""Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.
"""


class Range:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f'Сторона должна быть больше 0')
        setattr(instance, self.param_name, value)


class Rectangle:
    """Класс для вывода площади и периметра прямоугольника,
    для вычитания и сложения периметров прямоугольников,
    для сравнения площадей прямоугольников"""
    __slots__ = ('_a', '_b')

    a = Range()
    b = Range()

    def __init__(self, a, b=None):
        """Инициализация экземпляра"""

        self._a = a
        self._b = b
        if b is None:
            self._b = a

    def perimeter(self):
        """Вычисление периметра прямоугольника"""
        return (self._a + self._b) * 2

    def area(self):
        """Вычисление площади прямоугольника"""
        return self._a * self._b

    def __str__(self):
        """Вывод на печать для пользователя"""
        return f'Rectangle({self._a}, {self._b})'

    def __add__(self, other):
        """Сложение периметров прямоугольников"""
        p = self.perimeter() + other.perimeter()
        a = self._a + other._a
        b = p // 2 - a
        return Rectangle(a, b)

    def __sub__(self, other):
        """Вычитание периметров прямоугольников"""
        if self.perimeter() == other.perimeter():
            return 'Прямоугольники равны'
        elif self.perimeter() > other.perimeter():
            p = self.perimeter() - other.perimeter()
            a = (p // 2) // 2
            if a == 0:
                a += 1
            b = (p // 2) - a
            return Rectangle(a, b)
        else:
            return 'Нельзя вычесть больший прямоугольник из меньшего'

    def __eq__(self, other):
        """Сравнение площадей прямоугольников: площади прямоугольников равны"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Сравнение площадей прямоугольников: площади прямоугольников не равны"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Сравнение площадей прямоугольников: площадь первого прямоугольника больше площади второго"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Сравнение площадей прямоугольников: площадь первого прямоугольника меньше или равна площади второго"""
        return self.area() <= other.area()

    def __lt__(self, other):
        """Сравнение площадей прямоугольников: площадь первого прямоугольника меньше площади второго"""
        return self.area() < other.area()

    def __le__(self, other):
        """Сравнение площадей прямоугольников: площадь первого прямоугольника больше или равна площади второго"""
        return self.area() >= other.area()


if __name__ == '__main__':
    rect1 = Rectangle(3)
    rect2 = Rectangle(2, 6)

    print(rect1)
    print(rect2)

    rect1.a = 4
    rect1.b = 4

    print(rect1)

    rect2.a = 12
    rect2.b = 0

    print(rect2)
