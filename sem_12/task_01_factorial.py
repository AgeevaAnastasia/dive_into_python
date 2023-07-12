"""Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.

Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.

И вот эту задачу тоже, пожалуйста, посмотрите у меня.
Почему-то он при повторном вычислении факториала от числа,
вычисленного ранее, не повторяет вычисление или не записывает его
в историю. При этом из словаря ключ и значение удалены!
Но снова почему-то не вычисляются. Не могу догадаться, что тут не так.
"""
import json
from collections import defaultdict
from math import factorial


class Factorial1:

    def __init__(self, k):
        self._k = k
        self._storage = defaultdict(int)
        self._history = []
        self.file = 'file.json'

    def __str__(self):
        if len(self._storage) > self._k:
            self._storage.pop(self._history[0])
            self._history = self._history[1:]

        print(self._history)
        print(self._storage)

        txt = '\n'.join((f'{k}: {v}' for k, v in self._storage.items()))
        return f'Список последних {self._k} вычисленных факториалов:\n{txt}'

    def __call__(self, value):
        key = str(value) + "!"
        self._history.append(key)
        self._storage[key] = factorial(value)
        return f'{value}! = {factorial(value)}'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(self._storage, f, indent=1)
        return self.file


class Factorial:

    def __init__(self, k):
        self._k = k
        self._history = []

    def __call__(self, num):
        m = 1
        for n in range(1, num):
            m *= n
        self._history.append({num: m})
        if len(self._history) > self._k:
            self.history = self._history[-self._k:]
        return m

    def get_history(self):
        return self._history


if __name__ == "__main__":
    """calk_fact = Factorial1(5)
    print(calk_fact(2))  # 1
    print(calk_fact(6))  # 2
    print(calk_fact(10))  # 3
    print(calk_fact(5))  # 4
    print(calk_fact(7))  # 5
    print(calk_fact(2))  # 6
    print(calk_fact(11))  # 7
    print(calk_fact)

    c = Factorial(5)
    # for i in range(3, 9):
    # print(c(i))

    print(c(2))  # 1
    print(c(6))  # 2
    print(c(10))  # 3
    print(c(5))  # 4
    print(c(7))  # 5
    print(c(2))  # 6
    print(c(11))  # 7

    print(c.get_history())"""
    calk_fact = Factorial1(4)
    with calk_fact as cf:
        print(cf(2))
        print(cf(6))
        print(cf(10))
        print(cf(5))
        print(cf(2))
        print(cf(11))
        print(cf)
