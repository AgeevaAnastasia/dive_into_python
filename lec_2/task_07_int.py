"""
Целые числа, функция int()
Целое число имеет тип int. Для преобразования строки к числу используется
одноименная функция."""

x = '2'
int(x, base=10)

"""Первый аргумент — объект, который мы хотим преобразовать в число. Обычно это
другое число и или числовая строка. Второй аргумент указывает на основание
системы счисления. По умолчанию используется десятичная система, её можно не
указывать. Для base допустимы значения от 2 до 36, т.е. от двоичной до тридцати
шестиричной системы счисления. Примеры использования."""

x = int("42")
y = int(3.1415)
z = int("hello", base=30)
print(x, y, z, sep='\n')

"""Мы преобразовали десятичное число из строки в число, отбросили у вещественного
числа дробную часть и преобразовали строковую запись числа в тридцатиричной
системе счисления в её десятичный числовой аналог.

🔥 PEP-8! При указании значений для ключевых аргументов функции
пробелы вокруг знака равенства не ставятся.

У целый в Python есть одна полезная особенность. Объект изменяет свои размеры в
зависимости от длины целого числа. Переполнения регистра не происходит. В
Python "резиновый инт". При этом вы должны понимать, что любой объект хранит в
себе "служебную информацию", которая также занимает место в памяти.
Воспользуемся функцией getsizeof() из модуля sys, чтобы посмотреть на затраты
памяти под целым числом."""

import sys

STEP = 2 ** 16
num = 1
for _ in range(30):
    print(sys.getsizeof(num), num)
    num *= STEP

"""🔥 PEP-8! После импорта модулей ставится пустая строка.

Для хранения "единицы" в 64-х разрядной версии Python тратится 28(!) байт
памяти. Это объект со своей служебной информацией и несколькими байтами под
само число.
При этом мы можем хранить огромные числа, превышающие long integer на много
порядков без проблем и лишних приёмов программирования. Число Гугол, т.е. 10 в
степени 100 займет всего лишь 72 байта."""

print(sys.getsizeof(10 ** 100))


"""
Формат представления числа. Снова о "_".
Ещё одна особенность, которая упрощает чтение больших чисел появилась в Python
3.6. Это символ подчеркивания в качестве разделителя групп цифр. Да, снова он. И
не в последний раз."""

num = 7_901_123_456_789

"""Интерпретатор опускает символ подчеркивания. Они нужны лишь для
программиста, читающего код.

🔥 Внимание! Кроме того, обратите внимание на цикл из примера кода о
"резиновом инт".

for _ in range(30):
    
Конструкция цикла for in ожидает, что после for указывается переменная для
приёма значений, которые берутся из итератора указанного после in. Но если
внутри цикла значения не нужны, в качестве имени переменной используют
подчеркивание "_". Важно понимать, что использование подчеркивания в теле
цикла неверно. Скорее всего вам нужна переменная i, item или другая подобная.
Если подчёркиваем, то только один раз."""