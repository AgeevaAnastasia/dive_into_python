"""
Синтаксический сахар Python, @
В языке Python есть более элегантная возможность создания декораторов —
синтаксический сахар. Для этого используется символ “@” слитно с именем
декоратора. Строка кода пишется непосредственно над определением функции или
метода."""

import time
from typing import Callable


def main(func: Callable):
    def wrapper(*args, **kwargs):
        print(f'Запуск функции {func.__name__} в {time.time()}')
        result = func(*args, **kwargs)
        print(f'Результат функции {func.__name__}: {result}')
        print(f'Завершение функции {func.__name__} в{time.time()}')
        return result
    return wrapper


@main
def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(1000) = }')


"""Добавили декоратор @main к функции factorial. Необходимость в присваивании
значения новой переменной отпала. Несколько нижних строк кода из старого
примера удалили за ненадобностью. Кроме того мы сохранили старое имя функции.

🔥 Важно! Функция декоратор должна быть определена в коде раньше, чем
использована. В противном случае получим ошибку NameError

Синтаксический сахар упрощает написание кода, но не является обязательным к
применению. Однако в случае с передачей функции в замыкание использование
символа @ считается нормой. Связано это с тем, что присваивание переменной
нового значения происходит очень часто в коде. И понять создаём мы замыкание
функции или присваиваем что-то другое сложно. Когда же речь идёт о
присваивании через @, сразу ясно что используется декоратор
"""