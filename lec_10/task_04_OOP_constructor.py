"""Конструктор экземпляра

При создании класса обычно используют функцию конструктор __init__."""


class Person:
    max_up = 3
    def __init__(self):
        self.level = 1
        self.health = 100


p1 = Person()
p2 = Person()

print(f'{p1.max_up = }, {p1.level = }, {p1.health = }')
print(f'{p2.max_up = }, {p2.level = }, {p2.health = }')
#print(f'{Person.max_up = }, {Person.level = }, {Person.health = }')
# AttributeError: type object 'Person' has no attribute 'level'

Person.level = 100
print(f'{Person.level = }, {p1.level = }, {p2.level = }')

"""Внутри класса создаём функцию __init__. Два символа подчёркивания до и после
имени говорят о том, что это “магическое имя”. Подобные имена нужны для
добавления новых возможностей в работе класса и его экземпляров.
Внутри функции заданы две переменные level и health. Это атрибуты экземпляров.
Любой экземпляр получает заранее присвоенные значения. При этом сам класс не
имеет доступа к заданным атрибутам.

Также при попытке определить свойства level у класса мы не меняем значения
экземпляров. Это разные объекты, находящиеся в разных локальных областях
видимости.

● Параметр self
Ещё раз посмотрим на код конструктора:

def __init__(self):
self.level = 1
self.health = 100

В качестве параметра указана переменная self. Далее мы не просто присваиваем
значения переменным, а указываем self с точечной нотацией. В работе с классами
self является указателем на тот экземпляр класса, к которому происходит
обращение. Например для p1 это p1.level = 1. Какое бы имя вы не дали экземпляру,
self подставляет его на своё место.

💡 PEP-8! Имя self не является зарезервированным. Вместо него можно
использовать любое. Но соглашение о написании кода требует писать
self. Так ваш код поймут другие разработчики, а IDE верно его
проанализируют.

В некоторых языках при написании кода используется запись this.name. При
некотором допущении можно считать, что Python использует вместо this слово self с
той же логикой.

● Передача аргументов в экземпляр
При создании экземпляра можно передать значения в конструктор и тем самым
добавить свойства, характерные для конкретного экземпляра."""


class Person1:
    max_up = 3
    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100


p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')
print(f'{p1.name = }, {p1.race = }')
print(f'{p2.name = }, {p2.race = }')
print(f'{p3.name = }, {p3.race = }')


"""У __init__ определено три параметра. При этом первый параметр всегда self и он не
учитывается при передаче аргументов. Вызывая класс ожидаются два параметра,
при этом второй имеет значение по умолчанию. За исключением self логика такая
же как и при создании обычной функции. Все изученные в теме функции знания
применимы и к функциям класса."""
