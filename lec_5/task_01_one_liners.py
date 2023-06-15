"""
Полезные однострочники
Рассмотрим несколько примеров кода в одну строку, которые упрощают жизнь.

● Обмен значения переменных
Начнём с классического обмена значений переменных.

a, b = b, a

Мы поменяли местами содержимое переменных без создания дополнительных, в
одну строку.

● Распаковка коллекции
Рассмотрим другие варианты упаковки и распаковки значений."""

a, b, c = input("Три символа: ")
print(f'{a=} {b=} {c=}')

"""Как вы помните функция input возвращает строку str. Указав не одну переменную, а
три мы распаковываем строку из 3-х символов в три отдельные переменные."""

a, b, c = ("один", "два", "три",)
print(f'{a=} {b=} {c=}')

"""Аналогичным образом можно распаковать кортеж из трёх элементов в три
переменные. Со списком list, множеством set и прочими коллекциями будет
работать аналогично."""

a, b, c = {"один", "два", "три", "четыре", "пять"}
print(f'{a=} {b=} {c=}') # ValueError: too many values to unpack (expected 3)

"""Если количество переменных слева от равенства не совпадает с количеством
элементов последовательности Python вернёт ошибку.

● Распаковка коллекции с упаковкой “лишнего”, упаковка со звёздочкой
Для упаковки может применяться символ “звёздочка” перед именем переменной.
Такая переменная превратиться в список и соберёт в себя все значения, не
поместившиеся в остальные переменные."""

data = ["один", "два", "три", "четыре", "пять", "шесть", "семь",]
a, b, c, *d = data
print(f'{a=} {b=} {c=} {d=}')
a, b, *c, d = data
print(f'{a=} {b=} {c=} {d=}')
a, *b, c, d = data
print(f'{a=} {b=} {c=} {d=}')
*a, b, c, d = data
print(f'{a=} {b=} {c=} {d=}')

"""Элементы коллекции попадают в переменные в зависимости от того, какая из
переменных отмечена звёздочкой.

🔥 Важно! Звёздочкой можно отметить только одну переменную из
перечня.

Если нам нужна часть данных в переменных, а упакованный список в дальнейших
расчётах не участвует, в качестве переменной используют подчеркивание."""

link = 'https://docs.python.org/3/faq/programming.html#how-can-i-pass-optional-or-keyword-parameters-from-one-function-to-another'
prefix, *_, suffix = link.split('/')

""""● Распаковка со звёздочкой
Ещё один способ применения звёздочки — распаковка элементов коллекции.
Длинный вариант вывода элементов последовательности в одну строку с
разделителем табуляцией:"""

data = [2, 4, 6, 8, 10, ]
for item in data:
    print(item, end='\t')

"""И аналогичная операция в одну строку с распаковкой:"""

data = [2, 4, 6, 8, 10, ]
print(*data, sep='\t')

"""● Множественное присваивание
Если несколько переменных должны получить одинаковые значение, можно
объединить несколько строк в одну."""

a = b = c = 0
a += 42
print(f'{a=} {b=} {c=}')

"""Подобная запись допустима только с неизменяемыми типами данных. В противном
случае изменение одной переменной приведёт к изменению и других."""

a = b = c = {1, 2, 3}
a.add(42)
print(f'{a=} {b=} {c=}')

"""Другой вариант множественного присваивания похож на обмен переменных местами."""

a, b, c = 1, 2, 3
print(f'{a=} {b=} {c=}')

"""Число элементов в левой части должно совпадать с числом элементов справа от равно.
А если в левой части указать лишь одну переменную, получим кортеж."""

t = 1, 2, 3
print(f'{t=}, {type(t)}')

"""🔥 Важно! Тип объектов может отличаться. Не только целые числа, как в
примерах. Строки, любые коллекции. Ошибки это не вызовет. Но для
повышения читаемости рекомендуется не смешивать разные типы данных при
присваивании одной строкой.

● Множественное сравнение
Аналогично присваиванию можно сравнить несколько переменных внутри
конструкции if."""

a = b = c = 42
# if a == b and b == c:
if a == b == c:
    print('Полное совпадение')

"""Запись становится короче, т.к. исключается команда and внутри сравнения.
Работает подобная запись не только с проверкой на равенство, но и с другими
операциями."""

if a < b < c:
    print('b больше a и меньше c')

"""Проверяем, что b больше a и b меньше c."""