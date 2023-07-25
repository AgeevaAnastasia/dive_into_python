"""Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.

Доработайте задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
"""
from my_exceptions import SideException


class Rectangle:
    """Класс для вывода площади и периметра прямоугольника,
    для вычитания и сложения периметров прямоугольников,
    для сравнения площадей прямоугольников"""

    def __init__(self, a, b=0):
        """Инициализация экземпляра"""
        self.a = a
        self.b = b
        if b == 0:
            b = a
            self.b = a
        if a <= 0 or b <= 0:
            raise SideException(a, b)

    def perimeter(self):
        """Вычисление периметра прямоугольника"""
        return (self.a + self.b) * 2

    def area(self):
        """Вычисление площади прямоугольника"""
        return self.a * self.b

    def __str__(self):
        """Вывод на печать для пользователя"""
        return f'Rectangle({self.a}, {self.b})'

    def __add__(self, other):
        """Сложение периметров прямоугольников"""
        p = self.perimeter() + other.perimeter()
        a = self.a + other.a
        b = p // 2 - a
        return Rectangle(a, b)

    def __sub__(self, other):
        """Вычитание периметров прямоугольников"""
        if self.perimeter() == other.perimeter():
            return 'Прямоугольники равны'
        elif self.perimeter() > other.perimeter():
            p = self.perimeter() - other.perimeter()
            a = p // 2 // 2
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


rect1 = Rectangle(3)
rect2 = Rectangle(2, 6)
rect3 = Rectangle(-3, 5)

print(f'P = {rect1.perimeter()}, S = {rect1.area()}')
print(f'P = {rect2.perimeter()}, S = {rect2.area()}')

print()

print(rect1 - rect2)
print(rect2 - rect1)
print(rect1 + rect2)

print()

print(f'S(rect1) > S(rect2) = {rect1 > rect2}')
print(f'S(rect1) < S(rect2) = {rect1 < rect2}')
print(f'S(rect1) = S(rect2) = {rect1 == rect2}')
print(f'S(rect1) >= S(rect2) = {rect1 >= rect2}')
print(f'S(rect1) <= S(rect2) = {rect1 <= rect2}')
print(f'S(rect1) != S(rect2) = {rect1 != rect2}')
