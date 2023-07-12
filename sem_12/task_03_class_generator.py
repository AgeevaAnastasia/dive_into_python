"""Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1"""
from math import factorial


class Factorial:
    def __init__(self, start, stop=None, step=None):
        self.start = start
        self.stop = stop
        self.step = step
        if self.step is None:
            self.step = 1
        if self.stop is None:
            self.stop = self.start
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.stop:
            res = factorial(self.start)
            self.start += self.step
            return res
        raise StopIteration


if __name__ == '__main__':
    gen = Factorial(2, 10, 3)
    for num in gen:
        print(num)