"""
Логические конструкции, or, and, not
В Python доступны три логических оператора:
● and — логическое умножение «И»;
● or — логическое сложение «ИЛИ»;
● not — логическое отрицание «НЕ».
Логика их работы представлена в таблице
first   second  first and second    first or second not first
True    True    True                True            False
False   True    False               True            True
True    False   False               True            -
False   False   False               False           -

А теперь пример кода на Python чтобы разобраться в правильном синтаксисе
построения логических выражений. Вычислим високосный год в Григорианском
календаре поэтапно:"""

year = int(input('Введите год в формате yyyy: '))
if year % 4 != 0:
    print("Обычный")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Високосный")

"""А теперь выберем все случаи, когда год обычный и запишем их в одну строку:"""
if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
    print("Обычный")
else:
    print("Високосный")

"""Python последовательно слева направо проверяет логическое выражение,
формируя финальный ответ — True или False.
"""



"""
Ленивый if
Ещё раз посмотрим на прошлый пример кода.

if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:

В Python как и в некоторых других языках программирования if "ленивый". Если в
логическом выражении есть оператор or и первое значение то есть левое вернуло
истину, дальнейшая проверка не происходит, возвращается True. Если в
логическом выражении есть оператор and и левая половина вернула ложь, то
возвращается False без проверки правой половины выражения.
"""