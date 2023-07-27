"""Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
Например, отлавливаем ошибку деления на ноль.
"""

import logging

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" в строке {lineno:03d} ' \
         '\nфункция "{funcName}()" в {created} {msg}'

logging.basicConfig(format=FORMAT, style='{', filename='log.log', filemode='a', encoding='utf-8', level=logging.ERROR)

logger = logging.getLogger(__name__)


def division(a, b):
    try:
        return  a/ b
    except ZeroDivisionError as e:
        logger.error('Ошибка! Делить на ноль нельзя.\n')

    return a / b


division(4, 0)
