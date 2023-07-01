"""Доработайте прошлую задачу добавив декоратор wraps в
каждый из декораторов.
"""
import os
import json
from random import randint
from functools import wraps


def param(count):
    def deco(func):
        res_list = []

        @wraps(func)
        def wrapper(*args):
            for i in range(count):
                res = func(*args)
                res_list.append(res)
            print(res_list)
            return res

        return wrapper

    return deco


def deco_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        file = func.__name__ + '.json'
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as f:
                lst = json.load(f)
        else:
            lst = []

        result = func(*args, **kwargs)
        lst.append({
            'params': (*args, *kwargs),
            'result': result
        })

        with open(file, 'w', encoding='utf-8') as f:
            json.dump(lst, f, indent=1)

    return wrapper


def deco_control(func):
    @wraps(func)
    def wrapper(num, attempt):
        if not 1 <= num <= 100:
            print(f'Параметр {num = } не в диапазоне, будет задан случайно')
            num = randint(1, 101)
        if not 1 <= attempt <= 10:
            print(f'Параметр {attempt = } не в диапазоне, будет задан случайно')
            attempt = randint(1, 11)
        func(num, attempt)

    return wrapper


@param(2)
@deco_json
@deco_control
def guess_number(num, attempt):
    '''
    Игра угадай число
    '''
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
    number = 20
    attempts = 4
    guess_number(number, attempts)
    print(f'{guess_number.__name__ = }')
    help(guess_number)
