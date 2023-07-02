"""Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""
import pickle
import csv


def pickle_to_csv(p_file, c_file):
    with (
        open(p_file, 'rb') as p_f,
        open(c_file, 'w', encoding='utf-8', newline='') as c_f
    ):
        dct = pickle.load(p_f)
        headers = [key for key in dct[0].keys()]
        csv_write = csv.DictWriter(c_f, fieldnames=headers,
                                   dialect='excel-tab',
                                   quoting=csv.QUOTE_MINIMAL)
        csv_write.writeheader()
        res = []
        for i in range(1, len(dct)):
            res.append(dct[i])
        print(res)
        csv_write.writerows(res)


if __name__ == '__main__':
    pickle_file = 'file.pickle'
    csv_file = 'file.csv'
    pickle_to_csv(pickle_file, csv_file)
