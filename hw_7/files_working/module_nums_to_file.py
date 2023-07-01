"""
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""
__all__ = ['nums_to_file']

from random import randint, uniform
MIN_NUM = -1000
MAX_NUM = 1000


def nums_to_file(nums_str, filename):
    with open (filename, 'a', encoding='utf-8') as f:
        for _ in range(nums_str):
            f. write(f'{(randint(MIN_NUM, MAX_NUM + 1)): 5} | '
                     f'{(round(uniform(MIN_NUM, MAX_NUM + 1), 2)): 7}\n')


if __name__ == '__main__':
#    nums_to_file(int(input('Введите количество строк: ')), input('Введите имя файла: '))
    nums_to_file(7, 'numbers.txt')
