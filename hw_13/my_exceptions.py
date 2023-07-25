class MyException(Exception):
    pass


class SideException(MyException):
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Обе стороны прямоугольника ({self.a}, {self.b}) должны быть больше нуля'


class NameException(MyException):
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        return f'Каждое слово в имени "{self.name}" должно начинаться с большой буквы ' \
               f'и иметь в составе только буквы'


class RangeException(MyException):
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __str__(self):
        return f'Ошибка задания значения. Вы должны попасть в диапазон ' \
               f'от {self.min_value} до {self.max_value}'
