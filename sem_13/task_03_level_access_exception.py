"""Создайте класс с базовым исключением и дочерние классыисключения:
○ ошибка уровня,
○ ошибка доступа.

Доработайте классы исключения так, чтобы они выдали
подробную информацию об ошибках.
Передавайте необходимые данные из основного кода
проекта.
"""


class MyException(Exception):
    pass


class LevelException(BaseException):
    def __init__(self, level, name):
        self.level = level
        self.name = name
    def __str__(self):
        return f'Level {self.level} incorrect for user {self.name}!'


class AccessException(BaseException):
    def __init__(self, user_id):
        self.user_id = user_id
    def __str__(self):
        return f'Access for {self.user_id} denied!'
