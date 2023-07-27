"""Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК. Соберите информацию о содержимом в виде объектов namedtuple.

Каждый объект хранит:
* имя файла без расширения или название каталога,
* расширение, если это файл,
* флаг каталога,
* название родительского каталога.

В процессе сбора сохраните данные в текстовый файл используя логирование.
"""

from collections import namedtuple
import argparse
import logging
import os


def my_parser():
    parser = argparse.ArgumentParser(description='Parse folder')
    parser.add_argument('folder', metavar='f', type=str, nargs='*', help='Please, enter the folder path: ')
    args = parser.parse_args()
    dir_walk(args.folder[0])


def log_object(obj):
    FORMAT = '{levelname:<6} - {asctime}: \n{msg}'
    logging.basicConfig(format=FORMAT, style='{', filename='objects.log', filemode='a', encoding='utf-8',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info(f'{obj}')


def dir_walk(dir_):
    Obj = namedtuple('Obj', ['name', 'extension', 'type', 'parent'])
    list_objects = []

    for path, *_ in os.walk(dir_):
        parent = os.path.basename(path)
        for item in os.listdir(path):
            path_ = os.path.join(path, item)
            if os.path.isdir(path_):
                type_item = 'directory'
            else:
                type_item = 'file'
            try:
                name, extension = item.rsplit('.', 1)
            except ValueError:
                name = item
                extension = None

            o = Obj(name, extension, type_item, parent)
            list_objects.append(o)
            log_object(o)


if __name__ == '__main__':
    my_parser()