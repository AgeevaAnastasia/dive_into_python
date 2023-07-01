"""
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона

✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.

✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""
__all__ = ['create_files', 'create_some_types_files']

import os
import random as rnd
import string


def create_files(dir_, extension, min_len_name=6, max_len_name=30, min_bytes=256, max_bytes=4096, num_of_files=2):
    if not os.path.isdir(dir_):
        os.mkdir(dir_)
    for _ in range(num_of_files):
        name_len = rnd.randint(min_len_name, max_len_name + 1)
        file_name = dir_ + '\\' + ''.join(rnd.choices(string.ascii_letters, k=name_len)) + '.' + extension
        file_size = rnd.randint(min_bytes, max_bytes + 1)
        # random_bytes = os.urandom(file_size)
        random_bytes = ''.join(rnd.choices(string.ascii_letters, k=file_size)).encode('utf-8')

        if not os.path.isfile(file_name):
            with open(file_name, 'wb') as file:
                file.write(random_bytes)


def create_some_types_files(dir_, **kwargs):
    for ext, num in kwargs.items():
        create_files(dir_, ext, num_of_files=num)


if __name__ == '__main__':
    # user_dir = input('Введите папку, в которую нужно сгенерировать файлы: ')
    user_dir = os.getcwd() + '\\my_dir'
    create_some_types_files(user_dir, txt=2, bin=1, png=3)
