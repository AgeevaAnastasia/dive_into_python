"""Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.


Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
"""


class Animal:
    def __init__(self, name, tail):
        self.name = name
        self.tail = tail

    def common(self):
        return f'Название: {self.name}, хвост: {self.tail}'


class Fish(Animal):

    def __init__(self, name, tail, freshwater, deep):
        self.freshwater = freshwater
        self.deep = deep
        super().__init__(name, tail)

    def specific(self):
        res = ''
        if self.freshwater:
            res += 'пресноводная, '
        res += 'морская, '
        if self.deep < 3:
            res += 'мелководная'
        res += 'глубоководная'
        return res


class Bird(Animal):
    def __init__(self, name, tail, wingspan):
        self.wingspan = wingspan
        super().__init__(name, tail)

    def specific(self):
        wing_length = self.wingspan * 0.45
        return f'длина крыла равна {wing_length}'


class Mammal(Animal):
    ZONE = {1: 'арктические пустыни',
            2: 'тундра',
            3: 'тайга',
            4: 'смешанные леса и широколиственные леса',
            5: 'степи',
            6: 'пустыни',
            7: 'субтропики'}

    def __init__(self, name, tail, hibernate, zone):
        self.hibernate = hibernate
        self.zone = zone
        super().__init__(name, tail)

    def specific(self):
        res = ''
        if self.hibernate:
            res += 'впадает в спячку, '
        res += 'не впадает в спячку, '
        res += 'обитает в зоне: ' + self.ZONE[self.zone]
        return res


mammal = Mammal('Лев', True, False, 7)
print(f'{mammal.common()}, особые свойства: {mammal.specific()}')

fish = Fish('Рыба', True, False, 4)
print(f'{fish.common()}, особые свойства: {fish.specific()}')

bird = Bird('Птица', True, 4)
print(f'{fish.common()}, особые свойства: {bird.specific()}')
