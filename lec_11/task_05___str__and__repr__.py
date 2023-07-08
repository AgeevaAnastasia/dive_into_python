"""Представления экземпляра
При работе с классами, а точнее с их экземплярами бывает необходимо вывести их
содержимое в консоль. С этим отлично справляется функция print, но есть одно но.
Попробуем “запринтить” класс из примера выше."""


class User1:
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()


user1 = User1('Спенглер1')
print(user1)

"""В результат получили строку вида <__main__.User object at 0x000001C1B4FA6B60>
Число в конце — адрес объекта в оперативной памяти. Он может быть разным для
разных ПК и даже при разных запусках программы. Но пользы от этой информации
немного. Для получения читаемого описания необходимо переопределить как
минимум один из дандер методов: __str__ или __repr__.



Представление для пользователя, __str__

Дандер метод __str__ используется для получения удобного пользователю
описания экземпляра."""


class User2:
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()

    def __str__(self):
        return f'Экземпляр класса User с именем "{self.name}"'


user2 = User2('Спенглер2')
print(user2)

"""Метод __str__ обязан вернуть строку str. Обычно это строка содержит информацию
о свойствах класса для понимания что за экземпляр перед нами. Упор делается на
удобство чтения. Но и о краткости забывать не стоит.



Представление для создания экземпляра, __repr__

Дандер метод __repr__ аналогичен __str__, но возвращает максимально близкое к
созданию экземпляра класса представление."""


class User3:
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()

    def __repr__(self):
        return f'User({self.name})'


user3 = User3('Спенглер3')
print(user3)

"""Если скопировать вывод метода repr и присвоить его переменной, должен
получится ещё один экземпляр класса. Рассмотрим более сложный класс и его
метод __repr__."""


class User4:
    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3

    def __repr__(self):
        return f'User({self.name}, {self.equipment})'


user4 = User4('Венкман1', ['протонный ускоритель', 'ловушка'])
print(user4)

"""Мы снова получили строку, которую можно скопировать и создать экземпляр без
внесения правок. При этом свойство life опущено в выводе, т.к. не влияет на
создание экземпляра.




Приоритет методов

Добавим классу из примера выше метод __str__ и посмотрим какой из них
сработает."""


class User5:

    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3

    def __str__(self):
        eq = 'оборудованием: ' + ', '.join(self.equipment) if self.equipment else 'пустыми руками'
        return f'Перед нами {self.name} с {eq}. Количество жизней - {self.life}'

    def __repr__(self):
        return f'User({self.name}, {self.equipment})'


user5 = User5('Венкман2', ['протонный ускоритель', 'ловушка'])
print(user5)

"""При вызове функции print сработал метод __str__. Как же получить вывод от
__repr__ при наличии двух методов? Есть несколько способов вывода на печать:"""

# class User:
# ...
user5_1 = User5('Венкман3', ['протонный ускоритель', 'ловушка'])
print(user5_1)
print(f'{user5_1}')
print(repr(user5_1))
print(f'{user5_1 = }')

"""В первых двух вариантах срабатывает дандер __str__. Далее мы явно передаём в
print результат встроенной функции repr, которая обращается к одноимённому
методу. Так же при использовании f-строк символ равенства выводит имя
переменной слева от знака равно и repr справа от него.



Печать коллекций

Однако метод __repr__ оказывается более приоритетным, если на печать выводится
не один элемент, а коллекция элементов."""


class User:
    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3

    def __str__(self):
        eq = 'оборудованием: ' + ', '.join(self.equipment) if self.equipment else 'пустыми руками'
        return f'Перед нами {self.name} с {eq}. Количество жизней - {self.life}'

    def __repr__(self):
        return f'User({self.name}, {self.equipment})'


u_1 = User('Спенглер4')
u_2 = User('Венкман4', ['протонный ускоритель', 'ловушка'])
u_3 = User(equipment=['ловушка', 'прибор ночного видения'], name='Стэнц')

ghostbusters = [u_1, u_2, u_3]
print(ghostbusters)
print(f'{ghostbusters}')
print(repr(ghostbusters))
print(f'{ghostbusters = }')
print(*ghostbusters, sep='\n')

"""В приведённом примере список из трёх экземпляров при печати возвращает repr
представление во всех четырёх рассмотренных способах. И только при распаковке
списка через звёздочку функция print получает экземпляры напрямую и вызывает
их дандер __str__."""
