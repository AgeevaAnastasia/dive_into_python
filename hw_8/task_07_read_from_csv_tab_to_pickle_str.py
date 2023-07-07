"""Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Распечатайте его как pickle строку
"""
import csv
import pickle

with open('file.csv', 'r', encoding='utf-8') as f:
    file = [*csv.reader(f)]
    header_name, header_mult = file[0][0].split('\t')

    lst = []
    for i in range(1, len(file)):
        name, mult = file[i][0].split('\t')
        lst.append({header_name: name, header_mult: mult})

    print(pickle.dumps(lst))
