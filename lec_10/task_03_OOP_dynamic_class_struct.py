"""Динамическая структура класса

Класс и экземпляр являются динамическими объектами. Мы можем добавлять
атрибуты в процессе работы, а не только в момент создания класса."""


class Person:
    max_up = 3


p1 = Person()
p2 = Person()
Person.level = 1
print(f'{Person.level = }, {p1.level = }, {p2.level = }')

#p1.health = 100
#print(f'{Person.health = }, {p1.health = }, {p2.health = }')
# AttributeError: type object 'Person' has no attribute 'health'

#print(f'{p1.health = }, {p2.health = }')
# AttributeError: 'Person' object has no attribute 'health'

#print(f'{p1.health = }')

"""Добавление свойства level для класса позволяет обращаться к нему и из
экземпляров.
Когда же мы добавляем свойство health для экземпляра p1, получаем ошибку
AttributeError. Ни класс, ни экземпляр p2 не могут получить доступ к данному
атрибуту.
Возможность динамически изменять класс может быть использована как аналог
работы со словарями dict."""


class Person1:
    pass


p1 = Person1()
p1.level = 1
#p1.health = 100
dict_p1 = {}
dict_p1['level'] = 1
dict_p1['health'] = 100

#print(f'{p1.health = }')
print(f'{dict_p1["health"] = }')

"""Если в словаре мы указываем строковой ключ в квадратных скобках, в экземпляре
достаточно точечной нотации без лишних скобок и кавычек.
"""
