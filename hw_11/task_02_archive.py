"""Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков-архивов
list-архивы также являются свойствами экземпляра

Добавьте к задачам 1 и 2 строки документации для классов.

Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя.
"""


class Archive:
    """Принимает у экземпляра число и строку и хранит в архиве все данные
    ранее введённых экземпляров"""

    archive_nums = []
    archive_strings = []

    def __init__(self, num, string):
        """Инициализация экземпляра класса"""
        self.num = num
        self.string = string
        self.archive_nums.append(num)
        self.archive_strings.append(string)

    def __str__(self):
        """Вывод на печать для пользователя"""
        return f'num = {self.num}, string = {self.string}, \n' \
               f'archive_nums = {self.archive_nums}, \n' \
               f'archive_strings = {self.archive_strings}'

    def __repr__(self):
        """Вывод на печать для разработчика"""
        return f'Archive({self.num}, "{self.string}")'


data1 = Archive(12, 'fff')
print(data1.archive_nums, data1.archive_strings)
data2 = Archive(141, 'aaaaa')
print(data2.archive_nums, data2.archive_strings)
print(data1.archive_nums, data1.archive_strings)
print()
print(data1)
print(repr(data2))
