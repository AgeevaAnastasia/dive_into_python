"""Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Ключевые и позиционные параменты сохраняются под ключом 'params'
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции."""
import os
import json


def deco(func):
    def wrapper(num, *args, **kwargs):
        file = func.__name__ + '.json'
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as f:
                lst = json.load(f)
        else:
            lst = []

        result = func(num, *args, **kwargs)
        lst.append({
            'params': (num, *args, *kwargs),
            'result': result
        })

        with open(file, 'w', encoding='utf-8') as f:
            json.dump(lst, f, indent=1)

    return wrapper


@deco
def get_any(num, *args, **kwargs):
    return num


if __name__ == '__main__':
    get_any(12, 45, 'think', [1, 2], g=3)
