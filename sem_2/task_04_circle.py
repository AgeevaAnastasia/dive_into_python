"""
Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.
"""

import decimal
from math import pi

while True:
    diam = int(input('Введите диаметр окружности (от 1 до 1000): '))
    if 0 < diam <= 1000:
        break

decimal.getcontext().prec = 42
square = decimal.Decimal(pi * ((diam / 2) ** 2))
circumference = decimal.Decimal(pi * diam)

print(f'Длина окружности равна {circumference} \nПлощадь круга равна {square}')
