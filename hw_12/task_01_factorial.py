"""
Данил, а можете, пожалуйста, посмотреть у меня эту задачу с семинара.
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
        return f'{value}! = {self._storage[key]}'

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
    calk_fact = Factorial1(4)
    with calk_fact as cf:
        print(cf(2))
        print(cf(6))
        print(cf(10))
        print(cf(5))
        print(cf(2))
        print(cf(11))
        print(calk_fact)
