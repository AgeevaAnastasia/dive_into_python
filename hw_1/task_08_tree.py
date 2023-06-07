"""
Нарисовать в консоли ёлку спросив
у пользователя количество рядов
"""


def print_tree(n):
    count = 1
    while n > 0:
        print(' ' * (n - 1), '*' * count)
        n -= 1
        count += 2


while True:
    n_user = int(input('Введите количество рядов ёлки от 1 до 10: '))
    if n_user < 1:
        print('Вы ввели число меньше 1.')
    elif n_user > 10:
        print('Вы ввели число больше 10.')
    else:
        break

print_tree(n_user)
