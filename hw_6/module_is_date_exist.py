"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.

В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""
import sys

__all__ = ['is_valid_date']


def _is_leap_year(year):
    return year % 400 == 0 or year % 100 != 0 and year % 4 == 0 # вернет истину, если високосный


def is_valid_date(date_str):
    m_30 = [4, 6, 9, 11]
    m_31 = [1, 3, 5, 7, 8, 10, 12]
    day, month, year = map(int, date_str[0].split('.'))
    if 1 <= year <= 9999:
        if 1 <= month <= 12:
            if month == 2:
                if _is_leap_year(year):
                    if 1 <= day<= 29:
                        return True
                elif 1 <= day <= 28:
                    return True
            if month in m_30 and 1 <= day <= 30:
                return True
            if month in m_31 and 1 <= day <= 31:
                return True
    return False


if __name__ == '__main__':
    _, *params = sys.argv
    print(is_valid_date(params))
