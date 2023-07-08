"""Возьмите любую из задач с прошлых семинаров (например сериализация данных),
которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
Задачи должны решаться через вызов методов экземпляра."""

import json
import pickle


class Serialize:
    def __init__(self, file, file1='file.pickle'):
        self.file = file
        self.file1 = file1

    def json_to_pickle(self):
        with (
            open(self.file, 'r', encoding='utf-8') as f,
            open(self.file1, 'wb') as f_p
        ):
            pickle.dump(json.load(f), f_p)


if __name__ == '__main__':
    e = Serialize('file.json')
    e.json_to_pickle()
