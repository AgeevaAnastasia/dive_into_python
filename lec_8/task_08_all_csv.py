"""CSV
CSV (от англ. Comma-Separated Values — значения, разделённые запятыми) —
текстовый формат, предназначенный для представления табличных данных. Строка
таблицы соответствует строке текста, которая содержит одно или несколько полей,
разделенных запятыми.

CSV часто используют там, где удобно хранить информацию в таблицах. Выгрузки
из баз данных, из электронных таблиц для анализа данных.


Формат CSV
При работе с CSV стоит помнить о том, что формат не до конца стандартизирован.
Например запятая как символ разделитель может являться частью текста. Чтобы не
учитывать такие запятые, можно использовать кавычки. Но тогда кавычки не могут
быть частью строки. Кроме того десятичная запятая используется для записи
вещественных чисел в некоторых странах. Все эти особенности необходимо
учитывать при работе с CSV файлами.

Рассмотрим тестовый CSV файл biostats.csv:

"Name","Sex","Age","Height (in)","Weight (lbs)"
"Alex","M",41,74,170
"Bert","M",42,68,166
"Carl","M",32,70,155
"Dave","M",39,72,167
"Elly","F",30,66,124
"Fran","F",33,66,115
"Gwen","F",26,64,121
"Hank","M",30,71,158
"Ivan","M",53,72,175
"Jake","M",32,69,143
"Kate","F",47,69,139
"Luke","M",34,72,163
"Myra","F",23,62,98
"Neil","M",36,75,160
"Omar","M",38,70,145
"Page","F",31,67,135
"Quin","M",29,71,176
"Ruth","F",28,65,131

В первой строке могут содержаться заголовки столбцов как в нашем случае. Строки
со второй и до конца файла представляют записи. Одна строка — одна запись.
Текстовая информация заключена в кавычки, а числа указаны без них.
Подобные текстовые CSV файлы легко получить выгрузив данные из Excel или
другой электронной таблицы указав нужный формат. По сути CSV является
промежуточным файлом между Excel и Python.


Модуль CSV
Для работы с форматом в Python есть встроенный модуль csv. Для его
использования достаточно импорта в начале файла:
import csv

Рассмотрим основные функции модуля.
● Чтение CSV
Функция csv.reader принимает на вход файловый дескриптор и построчно читает
информацию."""

import csv

with open('biostats.csv', 'r', newline='') as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        print(line)
        print(type(line))


"""🔥 Важно! При работе с CSV необходимо указывать параметр newline=’’ во
время открытия файла.

Кроме файлового дескриптора можно передать любой объект поддерживающий
итерацию и возвращающий строки. Также функция reader может принимать
диалект отличный от заданного по умолчанию — “excel”. А при необходимости и
дополнительные параметры форматирования, если файл имеет свои особенности.

Файл biostats_tab_bad.csv хранит те же данные, что и файл выше, но вместо разделителя
используется символ табуляции. По сути это разновидность TSV — файл с
разделителем табуляцией:

"Name"  "Sex"   "Age"   "Height (in)"   "Weight (lbs)"
"Alex"  "M" 41  74  170
"Bert"  "M" 42  68  166
"Carl"  "M" 32  70  155
"Dave"  "M" 39  72  167
"Elly"  "F" 30  66  124
"Fran"  "F" 33  66  115
"Gwen"  "F" 26  64  121
"Hank"  "M" 30  71  158
"Ivan"  "M" 53  72  175
"Jake"  "M" 32  69  143
"Kate"  "F" 47  69  139
"Luke"  "M" 34  72  163
"Myra"  "F" 23  62  98
"Neil"  "M" 36  75  160
"Omar"  "M" 38  70  145
"Page"  "F" 31  67  135
"Quin"  "M" 29  71  176
"Ruth"  "F" 28  65  131


Добавим несколько параметров для его чтения"""

import csv

with open('biostats_tab_bad.csv', 'r', newline='') as f:
    csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(line)
        print(type(line))


"""
➢ dialect='excel-tab' — указали диалект с табуляцией в качестве разделителя
➢ quoting=csv.QUOTE_NONNUMERIC — передали встроенную константу,
указывающую функции, что числа без кавычек необходимо преобразовать к
типу float.



● Запись CSV
Для записи данных в файл используют функцию writer, которая возвращает объект
конвертирующий данные в формат CSV. Функция writer принимает файловый
дескриптор и дополнительные параметры записи аналогичные параметрам
функции reader. При этом данные в файл не записываются пока у возвращённого
объекта не будет вызван метод writerow для записи одной строки или writerows для
записи нескольких строк.
Рассмотри на примере."""

import csv

with (
    open('biostats_tab_bad.csv', 'r', newline='') as f_read,
    open('new_biostats.csv', 'w', newline='', encoding='utf-8') as f_write
):
    csv_read = csv.reader(f_read, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    csv_write = csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    all_data = []
    for i, line in enumerate(csv_read):
        if i == 0:
            csv_write.writerow(line)
        else:
            line[2] += 1
            for j in range(2, 4 + 1):
                line[j] = int(line[j])
            all_data.append(line)
    csv_write.writerows(all_data)


"""
1. Используя менеджер контекста with открыли два файла. Из первого читаем
информацию, а второй создаём для записи.
2. Функция reader возвращает объект csv_read для чтения как в пример выше.
3. Функция writer возвращает объект csv_write для записи. Мы указали:
    a. диалект “excel”
    b. в качестве разделителя столбцов будем использовать пробел
    c. если символ разделитель (пробел) есть в данных, экранируем их
вертикальной чертой
    d. символ экранирования используем по минимум, только там где он
необходим для разрешения конфликта с разделителем
4. В цикле читаем все строки из исходного файл. При этом строку с заголовком
сразу записываем методом writerow.
5. Для остальных строк увеличиваем возраст на единицу, преобразуем
вещественные числа в целые и сохраняем список в матрицу all_data
6. Одним запросом writerows(all_data) сохраняем матрицу в файл.



● Чтение в словарь
Помимо сохранения таблицы в список можно использовать для хранения словарь.
Ключи словаря — названия столбцов, значения — очередная строка файла CSV.
Прочитаем файл biostats_tab_bad.csv из примера выше, но не в список, а в словарь.
Воспользуемся классом DictReader."""

import csv

with open('biostats_tab_bad.csv', 'r', newline='') as f:
    csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", "height", "weight", "office"],
                              restkey="new", restval="Main Office", dialect='excel-tab',
                              quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(f'{line = }')
        print(f'{line["name"] = }\t{line["age"] = }')



"""Если передать список строк в параметр fieldnames, они будут использоваться для
ключей словаря, а не первая строка файла. В нашем примере передан “лишний”
ключ count. Т.к. в таблице нет шестого столбца, ему было присвоено значение из
параметра restval."""

import csv

with open('biostats_tab_bad.csv', 'r', newline='') as f:
    csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", ],
                              restkey="new", restval="Main Office",
                              dialect='excel-tab',
                              quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(f'{line = }')
        print(f'{line["name"] = }\t{line["age"] = }')

"""
Если количество ключей оказывается меньше, чем столбцов, недостающий ключ
берётся из параметра restkey. При этом все столбцы без ключа сохраняются как
элементы списка в restkey ключ.



● Запись из словаря
Для записи содержимого словаря в CSV используют класс DictWriter. Его параметры
схожи с рассмотренными выше параметрами DictReader."""

import csv
from typing import Iterator

with (
    open('biostats_tab_bad.csv', 'r', newline='') as f_read,
    open('biostats_new.csv', 'w', newline='', encoding='utf-8') as f_write
):
    csv_read: Iterator[dict] = csv.DictReader(f_read, fieldnames=["name", "sex", "age", "height", "weight", "office"],
                                              restval="Main Office",
                                              dialect='excel-tab',
                                              quoting=csv.QUOTE_NONNUMERIC)
    csv_write = csv.DictWriter(f_write, fieldnames=["id", "name", "office", "sex", "age", "height", "weight"],
                               dialect='excel-tab',
                               quoting=csv.QUOTE_ALL)
    csv_write.writeheader()
    all_data = []
    for i, dict_row in enumerate(csv_read):
        if i != 0:
            dict_row['id'] = i
            dict_row['age'] += 1
            all_data.append(dict_row)
    csv_write.writerows(all_data)



"""Класс DictWriter получил список полей для записи, где добавлено новое поле id. В
качестве диалекта выбран excel с табуляцией. В параметре quoting указали, что все
значения стоит заключать в кавычки.
Новый для нас метод writeheader сохранил первую строку с заголовками в том
порядке, в котором мы их перечислили в параметре fieldnames. Далее мы работаем
с элементами словаря и формируем список словарей для одноразовой записи в
файл.

🔥 Важно! Обратите внимание на импорт объекта Iterator из модуля typing.
При написании кода IDE подсвечивала возможные ошибки, так как не
понимала что за объект csv_read. Запись csv_read: Iterator[dict] = … сообщает,
что мы используем объект итератор, который возвращает словари. После
уточнения типа IDE исключила подсветку “ошибок”.
"""