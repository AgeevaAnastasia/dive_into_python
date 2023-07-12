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
    def __init__(self, name):
        self.name = name

    def common(self):
        return f'Название: {self.name}'


class Fish(Animal):

    def __init__(self, name, freshwater, deep):
        self.freshwater = freshwater
        self.deep = deep
        super().__init__(name)

    def specific(self):
        res = 'особенности: '
        if self.freshwater:
            res += 'пресноводная, '
        res += 'морская, '
        if self.deep < 3:
            res += 'мелководная'
        else:
            res += 'глубоководная'
        return res


class Bird(Animal):
    def __init__(self, name, wingspan):
        self.wingspan = wingspan
        super().__init__(name)

    def specific(self):
        res = 'особенности: '
        wing_length = self.wingspan * 0.45
        res += f'длина крыла равна {wing_length}'
        return res


class Mammal(Animal):
    ZONE = {1: 'арктические пустыни',
            2: 'тундра',
            3: 'тайга',
            4: 'смешанные леса и широколиственные леса',
            5: 'степи',
            6: 'пустыни',
            7: 'субтропики'}

    def __init__(self, name, hibernate, zone):
        self.hibernate = hibernate
        self.zone = zone
        super().__init__(name)

    def specific(self):
        res = 'особенности: '
        if self.hibernate:
            res += 'впадает в спячку, '
        else:
            res += 'не впадает в спячку, '
        res += 'обитает в зоне: ' + self.ZONE[self.zone]
        return res


if __name__ == '__main__':
    mammal = Mammal('зебра', False, 7)
    print(f'{mammal.common()}, {mammal.specific()}')

    fish = Fish('ёрш', False, 2)
    print(f'{fish.common()}, {fish.specific()}')

    bird = Bird('беркут', 2)
    print(f'{bird.common()}, {bird.specific()}')
