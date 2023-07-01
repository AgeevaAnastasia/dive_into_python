"""
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключом для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.
"""
import json
import os.path

LEVELS = 7

"""
def id_name_level(file_json):
    if os.path.isfile(file_json):
        with open(file_json, 'r', encoding='utf-8') as f:
            dct = json.load(f)
    else:
        dct = {str(i): {} for i in range(1, LEVELS + 1)}

    while True:
        data = input('Введите через пробел имя, id и уровень доступа, для выхода нажмите enter: ')
        if not data:
            print(dct)
            break
        user_input, id_, level = data.split()
        for value in dct.values():
            for key in value.keys():
                print(key)
                if key == id_:
                    print('Такой id уже существует, повторите ввод.')
                else:
                    print('сработало условие)')
                    dct[int(level)][id_] = user_input
                    print(dct)
        print('мы здесь')
        
    with open(file_json, 'w', encoding='utf-8') as f:
        json.dump(dct, f, ensure_ascii=False)
"""
def func(file_json):
    if os.path.isfile(file_json):
        with open(file_json, 'r', encoding='utf-8') as f:
            dct = json.load(f)
    else:
        dct = {str(i): {} for i in range(1, LEVELS + 1)}

    while True:
        data = input('Введите через пробел имя, id и уровень доступа, для выхода нажмите enter: ')
        if not data:
            print(dct)
            break
        user_input, id_, level = data.split()
        if id_ not in dct[level]:
            dct.setdefault(level, {id_: user_input})[id_] = user_input # как бы повторили ввод
                                                                       # в случае, если данные совпали
        else:
            print('Такой id на этом уровне доступа уже существует, повторите ввод.')

    with open(file_json, 'w', encoding='utf-8') as f:
        json.dump(dct, f, ensure_ascii=False)


if __name__ == '__main__':
    file_name = 'users_levels.json'
    func(file_name)
