"""Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат."""


class Rectangle:
    def __init__(self, a, b=0):
        self.a = a
        if b == 0:
            self.b = a
        else:
            self.b = b

    def perimeter(self):
        return (self.a + self.b) * 2

    def area(self):
        return self.a * self.b


rect1 = Rectangle(2, 3)
rect2 = Rectangle(6)

print(f'P = {rect1.perimeter()}, S = {rect1.area()}')
print(f'P = {rect2.perimeter()}, S = {rect2.area()}')
