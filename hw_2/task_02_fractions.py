"""
Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму и *произведение дробей.
Для проверки своего кода используйте модуль fractions
"""
import fractions
from math import gcd, lcm


def sum_fractions(num1, denom1, num2, denom2):
    denom = lcm(denom1, denom2)
    num1 = num1 * denom / denom1
    num2 = num2 * denom / denom2
    num = int(num1 + num2)
    if gcd(num, denom):
        divider = gcd(num, denom)
        num = int(num / divider)
        denom = int(denom / divider)
    return num, denom


def mult_fractions(num1, denom1, num2, denom2):
    num = num1 * num2
    denom = denom1 * denom2
    if gcd(num, denom):
        divider = gcd(num, denom)
        num = int(num / divider)
        denom = int(denom / divider)
    return num, denom


a, b = map(int, input('Введите первую дробь вида a/b: ').split('/'))
c, d = map(int, input('Введите первую дробь вида a/b: ').split('/'))

numerator1, denominator1 = sum_fractions(a, b, c, d)
numerator2, denominator2 = mult_fractions(a, b, c, d)

f1 = fractions.Fraction(a, b)
f2 = fractions.Fraction(c, d)

if numerator1 == denominator1:
    print(f'{a}/{b} + {c}/{d} = {numerator1} (проверка: {f1 + f2})')
else:
    print(f'{a}/{b} + {c}/{d} = {numerator1}/{denominator1} (проверка: {f1 + f2})')

if numerator2 == denominator2:
    print(f'{a}/{b} * {c}/{d} = {numerator2} (проверка: {f1 + f2})')
else:
    print(f'{a}/{b} * {c}/{d} = {numerator2}/{denominator2} (проверка: {f1 * f2})')
