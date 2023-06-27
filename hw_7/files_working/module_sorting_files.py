"""
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
import os

DCT = {'Video': ('mkv', 'avi', 'mp4'),
       'Pictures': ('png', 'jpg', 'jpeg', 'png', 'gif'),
       'Audio': ('wav', 'mp3', 'odd', 'flac'),
       'Documents': ('txt', 'doc', 'docx', 'tiff', 'err', 'log', 'ttf', 'text',
                     'pdf', 'pps', 'ppsm', 'pptx', 'pub', 'xls', 'xlsm', 'xps'),
       'Books': ('epub', 'fb2', 'ibooks', 'mobi')}


def group_files(dir_):
    files = [file for file in os.listdir(dir_) if os.path.isfile(file)]
    for fold, ext in DCT.items():
        if not os.path.isdir(fold):
            os.mkdir(fold)
        for file in files:
            if file.split('.')[1] in ext:
                os.replace(file, os.path.join(dir_, fold, file))


if __name__ == '__main__':
    group_files(os.getcwd())
