"""Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""


class Human:
    def __init__(self, last_name, name, father_name, age):
        self.last_name = last_name
        self.name = name
        self.father_name = father_name
        self.__age = age

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age

    def full_name(self):
        return f'{self.last_name} {self.name} {self.father_name}'


if __name__ == '__main__':
    person1 = Human('Иванов', 'Иван', 'Иванович', 45)

    print(person1.full_name(), person1.get_age())
    person1.birthday()
    print(person1.get_age())
