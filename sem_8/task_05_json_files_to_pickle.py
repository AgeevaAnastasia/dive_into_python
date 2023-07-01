"""Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
"""
import json
import pickle
import os


def func(dir_):
    json_files = [i for i in os.listdir(dir_) if i.endswith('.json')]
    for file in json_files:
        file1 = file.split('.')[0] + '.pickle'
        with (
            open(os.path.join(dir_, file), 'r', encoding='utf-8') as f,
            open(os.path.join(dir_, file1), 'wb') as f_p
        ):
            pickle.dump(json.load(f), f_p)


if __name__ == '__main__':
    """dir_name = os.getcwd()"""
    func(os.getcwd())
