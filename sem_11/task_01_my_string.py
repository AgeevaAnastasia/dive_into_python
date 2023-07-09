"""Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)

Добавьте к задачам 1 и 2 строки документации для классов.
"""
from datetime import datetime


class MyString(str):
    """Добавляет к стандартной строке свойства имя автора и дата создания"""

    def __new__(cls, value, name):
        """Инициализация экземпляра"""
        instance_ = super().__new__(cls, value)
        instance_.value = value
        instance_.name = name
        instance_.time = datetime.now()
        return instance_

    def __repr__(self):
        """Вывод на печать для разработчика"""
        return f'MyString("{self.value}", "{self.name}")'

    def __str__(self):
        """Вывод на печать для пользователя"""
        return f'Строка "{self.value}" имеет автора "{self.name}" и создана {self.time}'


data = MyString('Строка 1', 'Автор')

print(data.upper())
print(data.name)
print(data.time)
print(repr(data))
print(data)
