"""
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
"""
from random import randint


def deco(func):
    def wrapper(num, attempt):
        if not 1 <= num <= 100:
            print(f'Параметр {num = } не в диапазоне, будет задан случайно')
            num = randint(1, 101)
        if not 1 <= attempt <= 10:
            print(f'Параметр {attempt = } не в диапазоне, будет задан случайно')
            attempt = randint(1, 11)
        func(num, attempt)

    return wrapper


def guess_number(num, attempt):
    print(f'Угадайте число от 1 до 100. У вас {attempt} попыток.')
    for count in range(1, attempt + 1):
        guess = int(input(f'Попытка {count}. Ваше предположение: '))
        if guess == num:
            print(f'Поздравляем! Вы угадали число {num} за {attempt} попыток!')
            return True
        elif guess < num:
            print('Загаданное число больше')
        else:
            print('Загаданное число меньше')

    print(f'К сожалению, у вас закончились попытки. Загаданное число: {num}')
    return False


if __name__ == '__main__':
    number = 2000
    attempts = 20
    print(guess_number.__name__)
    control = deco(guess_number)
    print((control.__name__))
    control(number, attempts)
