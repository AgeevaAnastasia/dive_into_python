"""
Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его
за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь
"""
__all__ = ['guess_number']
from random import randint
import sys

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPTS = 10


def guess_number(min_num=0, max_num=100, guess_nums=10):
    num = randint(min_num, max_num + 1)
    count = 0
    print(f'Угадайте число от {min_num} до {max_num}. У вас {guess_nums} попыток.')
    for attempt in range(1, guess_nums + 1):
        guess = int(input(f'Попытка {attempt}. Ваше предположение: '))

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
    _, *params = sys.argv
    guess_number(*map(int, params))











"""
    while count < guess_nums:
        attempt = int(input(f'Попытка {guess_nums - count}. Введите число: '))
        count += 1
        if attempt < num:
            print('Загаданное число больше')
        elif attempt > num:
            print('Загаданное число меньше')
        elif attempt == num:
            print('Ура, вы угадали!')
            return True
        if count == guess_nums:
            print(f'У вас кончились попытки. Загаданное число: {num}')
            return False
"""
