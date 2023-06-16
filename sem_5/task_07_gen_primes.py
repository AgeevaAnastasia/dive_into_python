"""
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""
from math import sqrt

N = 5


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def gen_primes(n):
    count = 0
    yield 2
    number = 3
    while count < n - 1:
        if is_prime(number):
            yield number
            count += 1
        number += 2


print(*gen_primes(N))
