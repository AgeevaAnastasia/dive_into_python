"""
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.
"""
import typing


def read_per_line(file_obj: typing.TextIO):
    line = file_obj.read()
    if line == '':
        file_obj.seek(0)
        line = file_obj.read()
    return line[:-1]


def mult(names, numbers, result):
    with(
        open(names, 'r', encoding='utf-8') as f1,
        open(numbers, 'r', encoding='utf-8') as f2,
        open(result, 'w', encoding='utf-8') as f3
    ):
        len_names = sum(True for _ in f1)
        len_numbers = sum(True for _ in f2)
        for _ in range(max(len_numbers, len_names)):
            name = read_per_line(f1)
            num_line = read_per_line(f2)
            a, b = map(float, num_line.replace('\n', '').split(' | '))
            if a * b < 0:
                print(name.lower(), abs(a * b), f3)
            else:
                print(name.upper(), round(a * b))


"""
def mult(names, numbers):
    result = 'result.txt'
    with(
        open(names, 'r', encoding='utf-8') as f1,
        open(numbers, 'r', encoding='utf-8') as f2,
        open(result, 'w', encoding='utf-8') as f3
    ):
        res_mult = []
        for line in f2:
            a, b = map(float, line.strip().split(' | '))
            res_mult.append(a * b)
        size_f2 = len(res_mult)
        list_names = []
        for line in f1:
            list_names.append(line.strip())
        size_f1 = len(list_names)
        if list_names > res_mult:
            for name in list_names:"""

if __name__ == '__main__':
    names = 'names.txt'
    numbers = 'numbers.txt'
    result = 'result.txt'
    mult(names, numbers, result)
