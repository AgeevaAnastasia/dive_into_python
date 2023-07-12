"""Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа. Внутри класса создайте экземпляр на основе
переданного типа и верните его из класса-фабрики."""

from class_animal import Fish, Bird, Mammal


class Factory:
    def __init__(self, class_animal, *args):
        self.animal = class_animal(*args)
        self.args = args


if __name__ == '__main__':
    one = Factory(Mammal, 'зебра', False, 7)
    print(f'{one.animal.common()}, {one.animal.specific()}')
    two = Factory(Bird, 'беркут', 2)
    print(f'{two.animal.common()}, {two.animal.specific()}')
    three = Factory(Fish, 'ёрш', False, 2)
    print(f'{three.animal.common()}, {three.animal.specific()}')
