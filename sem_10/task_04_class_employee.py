"""Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь"""
from random import randint
from task_03_class_person import Human


class Employee(Human):
    ID_MAKER = 7
    LEN_ID = 6

    def __init__(self, id_num, *args, **kwargs):
        self.id_num = self.get_id_num(id_num)
        self.level = self.level_gen()
        super().__init__(*args, **kwargs)

    def level_gen(self):
        return sum(map(int, str(self.id_num))) % self.ID_MAKER

    def get_id_num(self, id_num):
        if len(str(id_num)) != self.LEN_ID:
            return randint(100000, 999999)
        return id_num

    def get_id(self):
        return self.id_num


if __name__ == '__main__':
    person1 = Employee(1234, 'Иванов', 'Иван', 'Иванович', 45)
    print(person1.id_num, person1.level, person1.full_name(), person1.get_age())
