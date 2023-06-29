"""Простой декоратор без параметров
Передача функции в качестве аргумента

До этого момента наш код возвращал функции, но не принимал их. Исправим
ситуацию на примере самописной функции нахождения факториала. Напомним, что
факториал числа - произведение чисел от единицы до заданного числа."""
import time
from typing import Callable


def main(func: Callable):
    def wrapper(*args, **kwargs):
        print(f'Запуск функции {func.__name__} в {time.time()}')
        result = func(*args, **kwargs)
        print(f'Результат функции {func.__name__}: {result}')
        print(f'Завершение функции {func.__name__} в {time.time()}')
        return result
    return wrapper


def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(1000) = }')
control = main(factorial)
print(f'{control.__name__ = }')
print(f'{control(1000) = }')


"""
● Функция main принимает на вход другую функцию. Внутри функции
определена функция wrapper, которая возвращается функцией main.
● Функция wrapper принимает пару параметров *args и **kwargs. С ними вы уже
знакомы. Подобная запись позволяет принять любое число позиционных
аргументов и сохранить их в кортеже args, а также любое число ключевых
аргументов с сохранением в словаре kwargs.
Обязательной строкой внутри wrapper является result = func(*args, **kwargs).
Переданная в качестве аргумента функция func вызывается со всеми
аргументами, которые были переданы. Дополнительно выводим информацию
о времени запуска, результатах и времени завершения работы функции. Не
забываем вернуть результат работы func из wrapper.
● Функция factorial вычисляет факториал для заданного числа.
● В нижней части кода запускаем поиск факториала, проверяем
работоспособность. Далее мы создаём функцию control в которую
помещается wrapper с замкнутой внутри функций func — нашей функцией
factorial. При вызове контрольной функции помимо результата поиска
факториала получаем вывод прописанный внутри wrapper.

Замыкание переданной в качестве аргумента функции внутри другой функции
называется декорированием функции. В нашем примере main — декоратор,
которым мы декорировали функцию factorial"""