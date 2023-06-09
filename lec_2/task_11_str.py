"""
Строки, функция str()

В Python нет типа данных символ. Есть только класс str. В нём можно хранить как
один символ, аналог char в си-подобных языках, так и любое большее количество
символов. Почему символы, а не буквы? Для хранения используется кодировка
utf-8, т.е. в строке могут быть не только буквы, цифры, знаки препинания, но и
иероглифы, смайлики и всё то, что хранится в кодировке Unicode.

При работе со строками стоит помнить, что это неизменяемый тип данных. При этом
str можно представить как коллекцию символов — массив. Выходит, что строка
является коллекцией? Верно.

На этой лекции рассмотрим несколько приёмов работы со строками как с
неизменяемыми объектами. А на следующей поговорим о строке как о коллекции
символов.

Способы записи строк
Python допускает одинарные или двойные кавычки для записи строки. Одни
кавычки могут включать другие, но они не должны смешиваться."""

txt = 'Книга называется "Война и мир".'

"""Тройный двойные кавычки позволяют писать текст в несколько строк. Если такой текст не
присвоить переменной, он превращается в многострочный комментарий. Подобные
комментарии используют для создания документации к коду. Например так:"""
class str(object):
    """
    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str
    ...
    """

"""Ещё один способ записать строки, перечислить их последовательно друг за другом."""

text = 'Привет.' 'Как ты, друг?' 'Рад тебя видеть.'
print(text)

"""Такой приём работает, но считается плохим стилем. Плюс, а точнее минус, строки
соединились без пробелов.
На этом способы записи строк не заканчиваются. Посмотрите на этот код:"""

very_long_text = 'Lorem ipsum dolor sit amet, consectetur \
adipisicing elit. A ab alias animi assumenda at aut ' \
'commodi, consequatur cumque ea harum, hic id \
illum ipsam itaque laboriosam magnam minus nam nulla ' \
'numquam obcaecati officia officiis porro \
possimus praesentium quaerat temporibus ullam veniam? '


"""Как вы помните, PEP8 рекомендует не писать более 120 символов в одной строке.
Обратный слеш “\” позволяет писать продолжение с новой строки. Требования в 120
символов выполняются. А Python воспринимает несколько строк как одну.

🔥 Важно! Подобный приём с обратным слешем работает не только для строк
текста, но и для кода. Очень длинную строку можно разделить записать в несколько.
Но помните, что зачастую такие строки трудно читать. Возможно не стоит лепить
решение в одну мега строчку, а разбить его на более читаемый вариант.



Конкатенация строк
Отдельный способ создания строк — конкатенация. Или говоря проще, сложение.
Разберём на примере и обсудим все его нюансы:"""
LIMIT = 120
ATTENTION = 'Внимание!'
name = input('Твоё имя? ')
age = int(input('Твой возраст? '))
text = ATTENTION + ' Хоть тебе и осталось ' + str(100 - age) +\
" до ста лет, но длинна строки не должна превышать " + str(LIMIT) + ' символов.'
print(text)

"""Переменная text получилась в результате сложения нескольких строк. При этом:
● Все элементы должны быть строками. Иначе получим ошибку вида: TypeError:
can only concatenate str (not "int") to str Именно для этого мы обернули
переменные с числами, такие как LIMIT, функцией str()
● Если в переменной хранится строковое значение, оборачивать её в str() не
нужно. Получится масло масляное.
● Складывать можно строки в одинарных, двойных и даже в трех двойных
кавычках. Но лучше выбрать единый стиль записи строк и придерживаться
его во всём проекте.
● Если код не влазит в 120 символов строки, не стесняемся использовать
обратный слеш для его разделения на несколько строк.
Конкатенация строк затратна по памяти и по времени. Для простых задач допустим
подобный подход. В реальных проектах конкатенация используется для
формирования констант. В остальных случаях используют способы форматирования
строк. О них поговорим на следующей лекции.
Кстати, рекомендации Google по стилю кода, которые являются продвинутой
версией PEP-8 с дополнительными требования запрещают программистам
использовать конкатенацию строк, особенно если она происходит внутри цикла.
Почему? Поговорим о размере строки в памяти.

Размер строки в памяти
Строки как объекты тратят память на служебную информацию, а как массивы на
хранение текста. В 64-х разрядной версии Python служебная информация занимает
48 байт. Разберём пример кода:"""

empty_str = ''
en_str = 'Text'
ru_str = 'Текст'
unicode_str = '😀😍😉🙃'
print(empty_str.__sizeof__())
print(en_str.__sizeof__())
print(ru_str.__sizeof__())
print(unicode_str.__sizeof__())

"""Во-первых обратите внимание на магический метод __sizeof__(). Он работает
аналогично sys.getsizeof и возвращает количество байт занятых объектом. Почему
же пустая строка заняла 49 байт, если служебная информация использует 48? Один
байт - символ конца строки.
Теперь посмотрим на текст. Английские буквы тратят по одному байту на символ.
Если же речь идёт о русском языке или любых других символах, кодирование
занимает 2 или 4 байта. Это особенность хранения информации в кодировке UTF-8
и фишка языка Python для доступа к букве по индексу.
А теперь зная, что строка тратит много памяти, что строка неизменяемый тип
данных и что при конкатенации строк создаются новые объекты, которые занимают
дополнительную память вы сами можете сделать вывод почему сложение строк не
приветствуется.

Методы проверки строк
Ряд методов анализируют строку текста и возвращают истину или ложь в
зависимости от содержимого строки. Часто используемые методы перечислены в
таблице:
str.isalnum() - Возвращает True, если все символы в строке
                буквенно-цифровые. Символ является
                буквенно-цифровым, если одно из следующих
                значений возвращает True: c.isalpha(), c.isdecimal(),
                c.isdigit()или c.isnumeric().
                
str.isalpha() - Возвращает True, если все символы в строке являются
                буквенными. Алфавитные символы — это символы,
                определенные в базе данных символов Юникода как
                «буква»

str.isdecimal() - Возвращает True, если все символы в строке являются
                  десятичными символами

str.isdigit() - Возвращает True, если все символы в строке являются
                цифрами. Цифры включают десятичные символы и
                цифры, требующие специальной обработки, например
                цифры надстрочного индекса совместимости.

str.isnumeric() - Возвращает True, если все символы в строке являются
                  числовыми символами. Числовые символы включают
                  цифровые символы и все символы, которые имеют
                  свойство числового значения Unicode
str.isalnum() - Возвращает True, если все символы в строке
                буквенно-цифровые. Символ является
                буквенно-цифровым, если одно из следующих
                значений возвращает True: c.isalpha(), c.isdecimal(),
                c.isdigit()или c.isnumeric().

str.isascii() - Возвращает True, если строка пуста или все символы в
                строке ASCII

str.islower() - Возвращает True, если все символы в строке в нижнем
                регистре

str.istitle() - Возвращает True, если строка является строкой с
                заглавным регистром и содержит хотя бы один символ

str.isupper() - Возвращает True, если все символы в строке в
                верхнем регистре

str.isprintable() - Возвращает True, если все символы в строке доступны
                    для печати или строка пуста. Непечатаемые символы
                    — это символы, определенные в базе данных
                    символов Unicode как «Другие» или «Разделители», за
                    исключением пробела ASCII (0x20), который считается
                    печатаемым.
                    
str.isspace() - Возвращает True, если в строке есть только
                пробельные символы


🔥 Внимание! Обратите внимание, что методы начинаются с приставки is.
Подобный приём часто используется в программировании. Если переменная
содержит логическое значение или функция/метод возвращает логическое
значение, в начале добавляют приставку is — намёк на истину или ложь в
качестве результата.
"""