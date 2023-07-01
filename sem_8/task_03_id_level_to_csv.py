"""Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV"""
import json
import csv
import os.path


"""def func(file_json):
    if os.path.isfile(file_json):
        with (
            open(file_json, 'r', encoding='utf-8') as f,
            open('csv_users_levels.csv', 'w', encoding='utf-8', newline='') as f_csv
        ):
            dct = json.load(f)
            rows = []
            for level, in_dict in dct.items():
                for id_, name in in_dict.items():
                    rows.append({'id': id_, 'level': int(level), 'name': name})

            print(rows)

            csv_write = csv.DictWriter(f_csv, fieldnames=["id", "level", "name"])
            csv_write.writeheader()
            csv_write.writerows(rows)
    else:
        print('Такого файла нет')
        return"""


def func(file_json):
    if os.path.isfile(file_json):
        with (
            open(file_json, 'r', encoding='utf-8') as f,
            open('csv_users_levels1.csv', 'w', encoding='utf-8', newline='') as f_csv
        ):
            dct = json.load(f)
            my_list = [['id', 'name', 'level']]
            for level, inner_dct in dct.items():
                for id_, name in inner_dct.items():
                    my_list.append([id_, name, level])

            csv_write = csv.writer(f_csv)
            csv_write.writerows(my_list)
    else:
        print('Такого файла нет')
        return


if __name__ == '__main__':
    file = 'users_levels.json'
    func(file)
