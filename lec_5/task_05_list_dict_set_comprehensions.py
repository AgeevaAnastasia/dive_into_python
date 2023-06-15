"""
Допустимые размеры односточника

PEP-8! Ограничение в 80 (120) символов на строку касается и генераторов. Если
ваш код выходит за границу, попробуйте его упростить. Если упрощение
невозможно, стоит перейти от однострочного генераторного выражения к функции
генератору. Их мы рассмотрим далее на уроке.
Аналогичные ограничения касаются и рассматриваемых далее генераторов
списков, множеств и словарей.


List comprehensions
Что будет, если генераторное выражение записать не в круглых скобках, а в
квадратных? Получим list comprehensions. Другие названия: list comp, генератор
списков, списковое включение. И нет, это не генераторное выражение. Генератор
списков полностью формирует список с элементами до его присваивания
переменной слева от знака равно."""


my_listcomp = [chr(i) for i in range(97, 123)]
print(my_listcomp) # ['a', 'b', 'c', 'd', ..., z]
for char in my_listcomp:
    print(char)

"""Как и генераторные выражения списковые включения поддерживаю несколько
циклов и логические проверки для каждого из циклов. Можно воспринимать их как
синтаксический сахар, более короткую запись. Например выбираем все чётные
числа из исходного списка и складываем их в результирующий.
Длинный код:"""

data = [2, 5, 1, 42, 65, 76, 24, 77]
res = []
for item in data:
    if item % 2 == 0:
        res.append(item)
print(f'{res = }')

"""Аналогичное решение, но с использованием синтаксического сахара listcomp:"""

data = [2, 5, 1, 42, 65, 76, 24, 77]
res = [item for item in data if item % 2 == 0]
print(f'{res = }')

"""
1. Не создаём пустой список в начале.
2. Не пишем двоеточия после цикла и логической проверки.
3. Исключаем метод append.
Итого вместо 4 строк кода получаем одну.



Генераторные выражения или генерация списка
В примере из раздела “генераторные выражения” мы обернули генератор
функцией list, чтобы сохранить значения в список. Можно воспринимать это как
антипример кода. Какой же пример является верным? Если на выходе нужен
готовый список, оптимальным будет следующий код:"""

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = [i + j for i in x if i % 2 != 0 for j in y if j != 1]
print(f'{len(res)=}\n{res}')

"""А если нам не нужны все элементы разом. Например мы в дальнейшем хотим
перебирать значения по одному в цикле. В этом случае подойдет генераторное
выражение без преобразования в список."""

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
for item in mult:
    print(f'{item = }')

"""🔥 Важно! При написании кода заранее решите нужна вам сгенерированная
коллекция целиком или нет. Не стоит тратить память на хранение всех
элементов, если вы ими не пользуетесь одновременно.



Set comprehensions
Кроме синтаксического сахара для генерации списков можно создавать множества
в одну строку. Синтаксис аналогичен примерам выше. Изменяются лишь скобки.
Для множеств используются фигурные."""

my_setcomp = {chr(i) for i in range(97, 123)}
print(my_setcomp) # {'f', 'g', 'b', 'j', 'e',... }
for char in my_setcomp:
    print(char)

"""Мы также перебираем элементы в цикле. Также можно использовать вложенные
циклы. Также для каждого цикла может быть проверка на включение элемента в
множество.

Стоит обратить внимание на следующие особенности:
● порядок элементов внутри множества может не совпадать с порядком
добавления элементов.
● множество хранит только уникальные значения"""

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = {i + j for i in x if i % 2 != 0 for j in y if j != 1}
print(f'{len(res)=}\n{res}')

"""Как и в примерах выше для генерации множества перебрали все возможные
комбинации пар x и y списков. Но в итоге осталось не 25 элементов, а 19
уникальных. 6 дублирующих элементов не были добавлены в множество, но время
на их обработку было затрачено. Асимптотика не улучшилась.



Dict comprehensions
Ещё один вариант синтаксического сахара — генерация словаря."""

my_dictcomp = {i: chr(i) for i in range(97, 123)}
print(my_dictcomp) # {97: 'a', 98: 'b', 99: 'c',... }
for number, char in my_dictcomp.items():
    print(f'dict[{number}] = {char}')

"""Запись похожа на создание множества, но в качестве выражения для добавления
указываются две переменные через двоеточие: key: value. Благодаря такой записи
Python понимает, что надо создать словарь.

🔥 Важно! Стоит помнить, что ключи словаря должны быть объектами неизменяемого типа.

Во всём остальном для генерации словарей в одну строку действуют те же правила,
что и для других типов данных.
"""