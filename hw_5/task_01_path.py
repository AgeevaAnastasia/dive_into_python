"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""


def path_file(path_file):
    *path, name, extension = path_file.replace('.', "\\").split('\\')
    return '\\'.join(path), name, extension


# print(path_file(input('Введите абсолютный путь до файла: ')))
print(path_file('C:\Program Files\Zip\zip.exe'))
