"""Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и
значение по умолчанию.
При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
Реализуйте работу через обработку исключений.
"""


def func(dct, key, default='no such key in dict'):
    try:
        return dct[key]
    except KeyError:
        print(f'Ошибка: ключа {key} нет в словаре. Возвращаем дефолтное значение "{default}"')
        return default


if __name__ == '__main__':
    dct = {
        1: 'a',
        2: 'b',
        3: 'c',
        4: 'd'
    }

    print(func(dct, 5))
