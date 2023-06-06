"""
Напишите программу, которая запрашивает год и проверяет его на високосность.
Распишите все возможные проверки в цепочке elif
Откажитесь от магических чисел
Обязательно учтите год ввода Григорианского календаря
В коде должны быть один input и один print
"""
GREGORIAN_CALENDAR = 1582


def is_leap_year(year):
    if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
        return 'не високосный'
    else:
        return 'високосный'


while True:
    year_user = int(input('Введите год: '))
    if year_user < GREGORIAN_CALENDAR:
        print('Вы ввели год до введения Григорианского календаря. Введите год после 1582.')
    else:
        break

print('Этот год', is_leap_year(year_user))
