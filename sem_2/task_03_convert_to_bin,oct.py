"""
Напишите программу, которая получает целое число и возвращает
его двоичное, восьмеричное строковое представление.
* Функции bin и oct используйте для проверки своего
результата, а не для решения.
Дополнительно:
* Попробуйте избежать дублирования кода
в преобразованиях к разным системам счисления
* Избегайте магических чисел
* Добавьте аннотацию типов где это возможно
"""
BASE_2 = 2
BASE_8 = 8

"""
def convert_number(n: int, base: int) -> str:
    temp = ''
    while n:
        temp = temp + str(n % base)
        n = n // base
    return temp[::-1]


num = int(input('Введите число в десятичной системе исчисления: '))

print(f'Число {num} в двоичной системе: {convert_number(num, BASE_2)}')
print(f'Проверка перевода в двоичную систему: {bin(num)[2::]}')

print(f'Число {num} в восьмеричной системе: {convert_number(num, BASE_8)}')
print(f'Проверка перевода в восьмеричную систему: {oct(num)[2::]}')


"""


def convert_number(n: int, base: int) -> str:
    temp = []
    while n:
        temp.append(str(n % base))
        n = n // base
    temp.reverse()
    return ''.join(temp)


def convert(b, c):
    l = []
    if b == 0:
        return l
    dig = b % c
    l.append(dig)
    convert(b // c, c)
    return l


num = int(input('Введите число в десятичной системе исчисления: '))

print(f'Число {num} в двоичной системе: {convert_number(num, BASE_2)}')
print(f'Проверка перевода в двоичную систему: {bin(num)[2::]}')

print(f'Число {num} в восьмеричной системе: {convert_number(num, BASE_8)}')
print(f'Проверка перевода в восьмеричную систему: {oct(num)[2::]}')
