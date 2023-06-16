"""
Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление."""


def get_dict_params(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        if value.__hash__:
            my_dict[value] = key
        else:
            my_dict[", ".join(map(str, value))] = key
    return my_dict


print(get_dict_params(a=5, b='hi', c=[1, 2], d=(3, 4)))
