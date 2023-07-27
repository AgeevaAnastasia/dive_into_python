"""Добавьте возможность запуска из командной строки.
При этом значение любого параметра можно опустить. В
этом случае берётся первый в месяце день недели, текущий
день недели и/или текущий месяц.
*Научите функцию распознавать не только текстовое
названия дня недели и месяца, но и числовые,
т.е не мая, а 5."""

from task_03_date_and_time import format_date
import argparse
from datetime import datetime


def pars_date():
    parser = argparse.ArgumentParser(prog='Парсит введенную в командной строке дату')
    parser.add_argument('-d', metavar='d',help='enter number of day', default="1")
    parser.add_argument('-dw', metavar='dw', help='enter day of a week', default="1")
    parser.add_argument('-m', metavar='m', help='enter month', default=datetime.now().month)
    args = parser.parse_args()
