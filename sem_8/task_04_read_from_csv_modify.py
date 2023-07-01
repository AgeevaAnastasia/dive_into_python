"""
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
"""
import csv
import json


def func(f_csv, f_json):
    with(
        open(f_csv, 'r', encoding='utf-8', newline='') as f_csv,
        open(f_json, 'w', encoding='utf-8') as f_json
    ):
        file = [*csv.reader(f_csv)]
        header_id, header_name, header_level = file[0]
        lst = []
        for id_, name, level in file[1:]:
            lst.append({header_id: id_, header_name: name, header_level: level, 'hash': hash(name + id_)})

        json.dump(lst, f_json, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    file_csv = 'csv_users_levels.csv'
    file_json = 'users_new_id.json'
    func(file_csv, file_json)
