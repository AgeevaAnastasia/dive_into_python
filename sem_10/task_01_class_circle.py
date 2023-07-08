"""Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def len_circle(self):
        return math.pi * 2 * self.radius

    def area_circle(self):
        return math.pi * (self.radius ** 2)


my_circle = Circle(4)
print(my_circle.len_circle())
print(my_circle.area_circle())
