"""Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""
from random import randint


def main(number, attempt):
    def guess_number():
        print(f'Угадайте число от 1 до 1000. У вас {attempt} попыток.')
        for count in range(1, attempt + 1):
            guess = int(input(f'Попытка {count}. Ваше предположение: '))
            if guess == number:
                print(f'Поздравляем! Вы угадали число {number} за {attempt} попыток!')
                return True
            elif guess < number:
                print('Загаданное число больше')
            else:
                print('Загаданное число меньше')

        print(f'К сожалению, у вас закончились попытки. Загаданное число: {number}')
        return False

    return guess_number()


if __name__ == '__main__':
    number = 1000
    attempts = 10
    res = main(number, attempts)
    res()
