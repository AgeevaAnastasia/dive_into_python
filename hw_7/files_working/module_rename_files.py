"""
Напишите функцию группового переименования файлов. Она должна:
* принимать в качестве аргумента желаемое конечное имя файлов.
* При переименовании в конце имени добавляется порядковый номер.
* принимать в качестве аргумента расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
* принимать в качестве аргумента расширение конечного файла.
Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extension>
"""
import os


def rename_files(ext_, final_name_, final_ext_):
    files = [file for file in os.listdir() if os.path.isfile(file) and file.split('.')[1] == ext_]
    for num, file in enumerate(files, 1):
        new_file = file.split('.')[0] + '_' + final_name_ + '_' + str(num) + '.' + final_ext_
        os.replace(file, new_file)


if __name__ == '__main__':
    ext = 'jpeg'
    final_name = '2023_06_24'
    final_ext = 'jpg'
    rename_files(ext, final_name, final_ext)
