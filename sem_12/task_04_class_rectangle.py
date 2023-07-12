"""Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств

Доработаем прямоугольник и добавим экономию памяти
для хранения свойств экземпляра без словаря __dict__.

Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.
"""


class Rectangle:
    """Класс для вывода площади и периметра прямоугольника,
    для вычитания и сложения периметров прямоугольников,
    для сравнения площадей прямоугольников"""

    def __init__(self, a, b=0):
        """Инициализация экземпляра"""
        __slots__ = ('_a', '_b')
        self._a = a
        self._b = b
        if b == 0:
            self._b = a

    @property
    def length(self):
        return self._a

    @property
    def height(self):
        return self._b

    @length.setter
    def length(self, value):
        if value > 0:
            self._a = value
        else:
            raise ValueError(f'Длина стороны прямоугольника должна быть больше нуля')

    @height.setter
    def height(self, value):
        if value > 0:
            self._b = value
        else:
            raise ValueError(f'Длина стороны прямоугольника должна быть больше нуля')

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

    rect1.height = 4
    rect1.length = 4

    print(rect1)
