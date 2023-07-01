"""Напишите следующие функции:
+Нахождение корней квадратного уравнения
+Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой
тройкой чисел из csv файла.
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""
from random import randint
import os
import csv
import json

LINES_IN_CSV = 100


def run(func):
    def wrapper():
        file = 'csv_trees.csv'
        with open(file, 'r', newline='') as f:
            csv_file = csv.reader(f)
            for line in csv_file:
                a, b, c = line
                func(a, b, c)

    return wrapper


def deco_json(func):
    def wrapper(a, b, c):
        file = func.__name__ + '.json'
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as f:
                lst = json.load(f)
        else:
            lst = []

        result = func(a, b, c)
        lst.append({
            'a': a,
            'b': b,
            'c': c,
            'result': result
        })

        with open(file, 'w', encoding='utf-8') as f:
            json.dump(lst, f, indent=1)

    return wrapper


def gen_csv_threes():
    file = 'csv_trees.csv'
    data = []
    for _ in range(LINES_IN_CSV):
        a = randint(1, 99)
        b = randint(1, 99)
        c = randint(1, 99)
        data.append((a, b, c))
    with open(file, 'w', encoding='utf-8', newline='') as f:
        csv_write = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        csv_write.writerows(data)


@run
@deco_json
def quadratic_equation(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    d = (b ** 2) - (4 * a * c)
    print(d)
    if d < 0:
        return 'no roots'
    elif d == 0:
        x = -b / (2 * a)
        return f'{x = }'
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return f'{x1 = }, {x2 = }'


if __name__ == '__main__':
    gen_csv_threes()
    quadratic_equation()
