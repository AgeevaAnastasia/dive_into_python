"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
строковое представление.
Функцию hex используйте для проверки своего результата.
"""
BASE_16 = 16


def convert_number(n: int, base: int) -> str:
    digits = '0123456789abcdefg'
    temp = []
    while n:
        temp.append(digits[n % base])
        n //= base
    temp.reverse()
    return ''.join(temp)


num = int(input('Введите число в десятичной системе исчисления: '))

print(f'Число {num} в шестнадцатеричной системе: {convert_number(num, BASE_16)}', end=' ')
print(f'(проверка: {hex(num)[2:]})')
