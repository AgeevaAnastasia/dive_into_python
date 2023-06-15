"""
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — его порядковый
номер из диапазона, границами которого являются
введенные числа.
✔ Границы диапазона учитывать.
"""


def dict_unicode_list(str_numbers):
    lim1, lim2 = map(int, str_numbers.split())
    dict_numbers = {}
    if lim1 < lim2:
        for i in range(lim1, lim2 + 1):
            dict_numbers[chr(i)] = i
    else:
        for i in range(lim2, lim1 + 1):
            dict_numbers[chr(i)] = i
    return dict_numbers


input_data = '1067 1093' # input('Введите границы диапазона через пробел: ')
print(dict_unicode_list(input_data))
