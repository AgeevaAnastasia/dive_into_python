"""
Программа загадывает число от 0 до 1000.
Необходимо угадать число за 10 попыток.
Программа должна подсказывать «больше» или «меньше» после каждой попытки.
"""
from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPT_NUMBER = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

attempt = ATTEMPT_NUMBER
while attempt > 0:
    guess_user = int(input('Введите число: '))
    if num == guess_user:
        print('Вы угадали! Поздравляем!')
        break
    elif num < guess_user:
        print('Загаданное число меньше.')
    elif num > guess_user:
        print('Загаданное число больше.')
    attempt -= 1
    if attempt > 0:
        print('Осталось попыток:', attempt)
    else:
        print('Попытки закончились, увы, вы не угадали! Было загадано число', num)
