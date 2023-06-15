"""
Словарь, dict
В Python есть изменяемый тип данных словарь. В других языках аналогичная
структура данных может называться отображение, mapping, именованный массив,
ассоциативный массив, сопоставление и т.п. Словарь представляет набор пар
ключ-значение. Ключ — любой неизменяемый тип данных. Значение - любой тип
данных. Обращаясь к ключу словаря получают доступ к значению.

🔥 Важно! Ключ выступает источником для вычисления хеша. Полученный
хеш играет роль числового индекса и указывает на ячейку со значением. В
Python вычисление хеша возможно лишь у неизменяемых типов данных.
Следовательно, ключ словаря обязан быть неизменяемым объектом. Обычно
это строка, целое число (вещественные лучше не использовать, вы же помните
о точности округления), либо кортеж или неизменяемое множество.

Способы создания словаря
Для создания словаря есть несколько способов. Например:
● передать набор пар ключ-значение в фигурных скобках,
● использовать знак равенства между ключом и значением,
● передать любую последовательность, каждый элемент который пара ключ и
значение"""

a = {'one': 42, 'two': 3.14, 'ten': 'Hello world!'}
b = dict(one=42, two=3.14, ten='Hello world!')
c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello world!')])
print(a == b == c)

"""Все три способа создают одинаковые словари.

🔥 Важно! Вариант b не допускает использования зарезервированных слов.
При этом ключи указываются без кавычек, но в словаре становятся ключами
типа str.


Добавление нового ключа
Для добавления в существующий словарь новой пары ключ-значение можно
использовать обычную операцию присваивания."""

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
my_dict['ten'] = 10
print(my_dict)

"""Доступ к значению словаря
Доступ через квадратные скобки []
Для получения доступа к значению необходимо указать ключ в квадратных скобках
после или переменной."""

TEN = 'ten'
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict['two'])
print(my_dict[TEN])
print(my_dict[1]) # KeyError: 1


"""Ключ может быть указан явно или передам как содержимое переменной,
константы. При попытке обратиться к несуществующему ключу получаем ошибку:
KeyError.
Доступ к ключу позволяет изменять значения. Для этого используем операцию
присваивания как и в случае с добавлением новой пары ключ-значение.

🔥 Важно! Получить доступ к ключу по значению невозможно.



Доступ через метод get
Если ли мы хотим гарантировать отсутствие ошибки KeyError при обращении к
элементу словаря, можно обратиться к значению через метод get, а не квадратные
скобки."""

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.get('two'))
print(my_dict.get('five'))
print(my_dict.get('five', 5))
print(my_dict.get('ten', 5))

"""При обращении к существующему ключу метод get работает аналогично доступу к
через квадратные скобки. Если обратиться к несуществующему ключу, get
возвращает None. Метод get принимает второй аргумент, значение по умолчанию.
Если ключ отсутствует в словаре, вместо None будет возвращено указанное
значение.


Часто используемые методы словарей
Разберем некоторые методы работы со словарями.

Метод setdefault
Метод setdefault похож не get, но отсутствующий ключ добавляется в словарь."""

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.setdefault('five')
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.setdefault('six', 6)
print(f'{eggs = }\t{my_dict=}')
new_spam = my_dict.setdefault('two')
print(f'{new_spam=}\t{my_dict=}')
new_eggs = my_dict.setdefault('one', 1_000)
print(f'{new_eggs=}\t{my_dict=}')

"""При вызове метода с одним аргументом отсутствующий ключ добавляется в
словарь. В качестве значения передаётся None. Если указать два аргумента и ключ
отсутствует, второй аргумент становится значением ключа и также добавляется в
словарь. При обращении к существующему ключу, словарь не изменяется
независимо от того указанные один или два аргумента.


Метод keys
Метод keys возвращает объект-итератор dict_keys."""

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.keys())
for key in my_dict.keys():
    print(key)

"""
Обычно объект не используют напрямую. Метод keys применяется в связке с
циклом for для перебора ключей словаря.

🔥 Важно! Запись цикла for key in my_dict: отработает аналогично. По
умолчанию словарь возвращает ключи для итерации в цикле.

💡 Внимание! В отличии от списков, кортежей и строк доступ к
элементу-значению осуществляется не по индексу, а по ключу. При этом
начиная с версии Python 3.7 словарь сохраняет порядок добавления ключей. В
каком порядке ключи были добавлены, в том порядке они будут возвращены в
случае итерации по словарю.


Метод values
Метод values похож на keys, но возвращает значения в виде объекта итератора
dict_values, а не ключи."""

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.values())
for value in my_dict.values():
    print(value)


"""Метод items
Если в цикле необходимо работать одновременно с ключами и значениями, как с
парами, используют метод items."""

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.items())
for tuple_data in my_dict.items():
    print(tuple_data)
for key, value in my_dict.items():
    print(f'{key = } value before 100 - {100 - value}')

"""Метод возвращает объект итератор dict_items. Если создать цикл for с одной
переменной между for и in, получим кортеж из пар элементов — ключа и значения.
Обычной используют две переменные в цикле: первая принимает ключ, а вторая
значение. Такой подход облегчает чтение кода и позволяют использовать ключ и
значение по-отдельности.



Метод popitem
Для удаления пары ключ значение из словаря используют метод popitem."""

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.popitem()
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.popitem()
print(f'{eggs = }\t{my_dict=}')

"""Так как словари сохраняют порядок добавления ключей, удаление происходит
справа налево, по методу LIFO. Элементы удаляются в обратном добавлению
порядке.

🔥 Важно! Если измените значение у существующего ключа, положение
ключа в очереди не меняется, он не считается последним добавленным.


Метод pop
Метод pop удаляет пару ключ-значение по переданному ключу."""

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.pop('two')
print(f'{spam = }\t{my_dict=}')
err = my_dict.pop('six') # KeyError: 'six'
err = my_dict.pop() # TypeError: pop expected at least 1 argument, got 0

"""Если указать несуществующий ключ, получим ошибку KeyError. В отличии от метода
pop у списков list, dict.pop вызовет ошибку TypeError. Для удаление последнего
элемента нужен метод popitem.


Метод update
Для расширение словаря новыми значениями используют метод update."""

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
my_dict.update(dict(six=6))
print(my_dict)
my_dict.update(dict([('five', 5), ('two', 42)]))
print(my_dict)

"""На вход метод получает другой словарь в любой из вариаций создания словаря.
Если передать существующий ключ, значение будет заменено новым.
Ещё один способ создать словари из нескольких других, который появился в новой
версии Python — вертикальная черта."""

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
new_dict = my_dict | {'five': 5, 'two': 42} | dict(six=6)
print(new_dict)

"""При перезаписи совпадающих ключей приоритет отдаётся словарю,
расположенному правее.
"""