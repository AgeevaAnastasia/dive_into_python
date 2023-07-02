"""Напишите функцию, которая получает на вход директорию
и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах,
а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий."""
import json
import csv
import pickle
import os


def dir_walk(dir_):
    data = []

    sizes = dict()
    for root, dirs, files in os.walk(dir_, topdown=False):
        size = sum(os.path.getsize(os.path.join(root, f)) for f in files)
        size += sum(sizes[os.path.join(root, d)] for d in dirs)
        sizes[root] = size

    for path, *_ in os.walk(dir_):
        parent_dir = os.path.basename(path)
        for item in os.listdir(path):
            path_ = os.path.join(path, item)
            if os.path.isdir(path_):
                type_item = 'directory'
                size = sizes[path_]
            else:
                type_item = 'file'
                size = os.path.getsize(path_)

            data.append({'name': item, 'parent directory': parent_dir, 'type': type_item, 'size': size})

    file = 'file_tree'
    with (open(file + '.json', 'w', encoding='utf-8') as j_f,
          open(file + '.csv', 'w', encoding='utf-8', newline='') as c_f,
          open(file + '.pickle', 'wb') as p_f):
        json.dump(data, j_f, indent=1)
        pickle.dump(data, p_f)
        writer = csv.DictWriter(c_f, fieldnames=data[0])
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    # dir_walk('Введите адрес директории: ')
    dir_walk('.')
