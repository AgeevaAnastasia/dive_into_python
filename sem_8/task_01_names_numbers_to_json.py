"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдоименами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""

import json


def create_json_file(input_file, output_file):
    data = []

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            name, mult = line.strip().split(' ')
            name = name.title()
            mult = float(mult)
            data.append({'name': name, 'mult': mult})

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


def write_json(name):
    with (
        open(name, 'r', encoding='UTF-8') as res,
        open('output.json', 'w', encoding='UTF-8') as j
    ):
        dict_res = {}
        for item in res:
            key, value = item.replace('\n', '').split((' '))
            dict_res[key.capitalize()] = value
            json.dump(dict_res, j, ensure_ascii=False, indent=3)


if __name__ == '__main__':
    create_json_file('result.txt', 'result.json')
    write_json('result.txt')
