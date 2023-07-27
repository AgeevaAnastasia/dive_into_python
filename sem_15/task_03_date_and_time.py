"""Функция получает на вход текст вида: “1-й четверг ноября”, “3-
я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату.
"""

import logging
import argparse
from datetime import datetime

YEAR = datetime.now().year

FORMAT = '{levelname:<8} - {asctime}: \n{msg}'

logging.basicConfig(format=FORMAT, style='{', filename='log2.log', filemode='a', encoding='utf-8', level=logging.INFO)

logger = logging.getLogger(__name__)


def format_date(txt: str):
    days = {'понедельник': 0, 'вторник': 1, 'среда': 2, 'четверг': 3, 'пятница': 4,
            'суббота': 5, 'воскресенье': 6}
    months = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
              'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}
    """days = {'понедельник': 1, 'вторник': 2, 'среда': 3, 'четверг': 4, 'пятница': 5,
            'суббота': 6, 'воскресение': 7},
    months = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
              'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}"""
    """try:
        num_week, day_week, month = txt.split()
        num_week = int(num_week[0])
        for day in range(1, 31 + 1):
            date_res = datetime.datetime(year=YEAR, month=months[month], day=day)
            if date_res.weekday() == days[day_week]:
                return date_res
    except Exception as e:
        logger.error('Ошибка! Неверно указан формат даты.\n')
        print(f'Произошла ошибка {e}')"""

    try:
        a, b, c = txt.split()
        a = int(a[0])
        weekday = days[b]
        month = months[c]
        count = 0
        for day in range(1, 32):
            date_res = datetime(month=month, day=day, year=datetime.now().year)
            if date_res.weekday() == weekday:
                count += 1
                if count == a:
                    return date_res
    except Exception as e:
        logger.error(f"Ошибочка вышла:{e}")


days_reverse = {0: 'понедельник', 1: 'вторник', 2: 'среда', 3: 'четверг', 4: 'пятница',
                5: 'суббота', 6: 'воскресенье'}

months_reverse = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня',
              7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}

# print(format_date("1-й четверг ноября"))
# print(format_date("3-я среда мая"))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Парсит введенную в командной строке дату')
    parser.add_argument('-d', metavar='d', help='enter number of day', default="1-й")
    parser.add_argument('-dw', metavar='dw', help='enter day of a week', default=days_reverse[datetime.now().weekday()])
    parser.add_argument('-m', metavar='m', help='enter month', default=months_reverse[datetime.now().month])
    args = parser.parse_args()
    print(format_date(f'{args.d} {args.dw} {args.m}'))
