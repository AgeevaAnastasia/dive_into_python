"""
Функция — фрагмент программного кода, к которому можно обратиться из другого
места программы. Функцию стоит представлять как чёрный ящик. В ящик попадают
данные, обрабатываются внутри (для пользователя функции не важно как они
обрабатываются) и ящик возвращает готовый результат. Подобные функции
обеспечивают простоту использования и возможности переносимости и
переиспользования в других частях проекта и даже в других проектах.
В Python можно создавать свои функции, использовать встроенные функции
интерпретатора, а также работать с функциями из модулей и пакетов стандартной
библиотеки и из устанавливаемых дополнений. На этой лекции подробно
поговорим про самописные функции и функции “из коробки”.

Создание своих функции
Как и всё в Python функция является объектом. Можно сказать, что питоновская
функция это функция высшего порядка. Она может работать с другими функциями,
либо принимая их в виде параметров, либо возвращая их. Проще говоря, функцией
высшего порядка называется такая функция, которая принимает функцию-объект
как аргумент или возвращает функцию-объект в виде выходного значения.
Разберёмся в понятиях “вызываем” и “передаём” на уже знакомом примере кода.
"""

a = 42
print(type(a), id(a))
print(type(id))

"""
Функция print вызывается с двумя аргументами - функциями. Каждая из
переданных в качестве аргументов функций: type и id так же вызываются с
переменной a в качестве аргумента.
Во втором случае функция type вызывается с функцией id в качестве аргумента.
При этом у id отсутствуют круглые скобки после имени. Мы не вызываем её, а
передаём как объект.
Ещё один пример передачи функции ниже."""

very_bad_programming_style = sum
print(very_bad_programming_style([1, 2, 3]))

"""
Передали в переменную встроенную функцию sum. Теперь переменную можно
вызывать как функцию суммирования.
Итого. Наличие круглых скобок после имени функции с аргументами или без них
внутри скобок — вызов функции. Имя функции без скобок — передача функции как
объекта.

Для определения собственной функции используется зарезервированное слово def.
Далее указывается имя функции, круглые скобки с параметрами при
необходимости и двоеточием. Со следующей строки описывается тело функции как
вложенный блок, т.е. с 4 отступами для каждой строки тела."""

def my_func():
    pass

"""Определили функцию под именем my_func, которая не принимает аргументы и
ничего не делает.

🔥 PEP-8! Имена функций записываются в стиле snake_case как и имена
переменных

Что такое pass
Похоже мы впервые встретили слово pass. Это зарезервированное слово, которое
ничего не делает. Используется в тех местах, где должен быть код для верной
работы программы, но его пока нет. Например мы не можем создать функцию без
тела. Нужна как минимум одна строка. В ней мы и написали pass.

🔥 Внимание! Не злоупотребляйте использованием pass. Делать десятки
заготовок функций и классов с pass на будущее - не лучшая привычка.
Создавайте код по мере того как он вам нужен.

И сразу пару антипримеров использования pass которые выдают в программисте
новичка, радостно вставляющего новое слово повсюду в коде.
Плохо:"""

if a != 5:
    pass
else:
    a += 1

"""Уже лучше:"""

if a == 5:
    a += 1
else:
    pass

"""Отлично. Ничего лишнего:"""
if a == 5:
    a += 1


