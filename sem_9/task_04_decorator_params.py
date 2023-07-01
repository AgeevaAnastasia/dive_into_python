"""Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
"""


def param(count):
    def deco(func):
        res_list = []

        def wrapper(*args):
            for _ in range(count):
                res_list.append(func(args))
            print(res_list)

        return wrapper

    return deco


@param(3)
def my_func(*args):
    print(*args)
    return args


if __name__ == '__main__':
    my_func('Hello, world!')
