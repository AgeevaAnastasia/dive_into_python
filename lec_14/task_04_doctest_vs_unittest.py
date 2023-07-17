"""Сравнение тестов doctest и unittest


Возьмём уже знакомую функцию проверки числа на простоту и реализуем
написанные ранее в doctest тесты используя unittest.
Файл prime.py без тестов doctest


def is_prime(p: int) -> bool:
    if not isinstance(p, int):
        raise TypeError('The number P must be an integer type')
    elif p < 2:
        raise ValueError('The number P must be greater than one')
    elif p > 100_000_000:
        print('If the number P is prime, the check may take a long time. Working...')
    for i in range(2, p):
        if p % i == 0:
            return False
    return True


Ничего нового в коде функции нет.


А так будет выглядет файл test_prime.py

import io
import unittest
from unittest.mock import patch
from prime import is_prime


class TestPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(42))
        self.assertTrue(is_prime(73))
    def test_type(self):
        self.assertRaises(TypeError, is_prime, 3.14)
    def test_value(self):
        with self.assertRaises(ValueError):
            is_prime(-100)
            is_prime(1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_warning_false(self, mock_stdout):
        self.assertFalse(is_prime(100_000_001))
        self.assertEqual(mock_stdout.getvalue(), 'If the number P is prime, '
                                                 'the check may take a long time. Working...\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_warning_true(self, mock_stdout):
        self.assertTrue(is_prime(100_000_007))
        self.assertEqual(mock_stdout.getvalue(), 'If the number P is prime, '
                                                 'the check may take a long time. Working...\n')


if __name__ == '__main__':
    unittest.main()


Разберём каждый из тестов внутри класса:

➢ Кейс test_is_prime
Проверяем базовую работу функции. Утверждение assertFalse ожидает получить
ложь в качестве аргумента. В нашем случае в качестве результата вызова функции.
Аналогично assertTrue ожидает получить истину.

➢ Кейс test_type
Утверждение assertRaises ожидает ошибку типа (аргумент один) если вызвать
функцию is_prime (аргумент два) и передать ей число 3.14 (аргумент три).

➢ Кейс test_value
Используем менеджер контекста для утверждения ошибки и внутри контекста
дважды запускаем функцию. assertRaises во всех случаях будет ожидать ошибку
значения

➢ Кейсы test_warning_false и test_warning_true


🔥 Внимание! Оба примера выходят за рамки основ unittest. Это скорее
пример на будущее для самых любознательных.

Используя декоратор patch из модуля mock перенаправляем стандартный поток
вывода sys.stdout обращаясь к StringIO модуля ввода-вывода io. Результат попадает
в параметр mock_stdout. Внутри метода делаем стандартную проверку на ложь или
истину для большого числа. А далее проверяем, что стандартный вывод получил
значение, совпадающее с ожидаемым текстом предупреждения.

🔥 Внимание! Разбор Mock объектов выходит за рамки лекции. Самые
любознательные могут обратиться к стандартной документации языка.
https://docs.python.org/3.11/library/unittest.mock.html


Запуск тестов doctest из unittest

А что если тесты уже написаны в doctest? В этом случае можно создать функцию
test_loader и добавить тесты doctest в перечень для тестирования. Изучите пример."""

import doctest
import unittest
import prime


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(prime))
    tests.addTests(doctest.DocFileSuite('prime.md'))
    return tests


if __name__ == '__main__':
    unittest.main()


"""Объект tests используя метод addTests добавляет импортированный модуль prime.
Для этого используется класс DocTestSuite из модуля doctest. А если необходимо
тестировать документацию, используется класс DocFileSuite. Теперь функция
unittest.main соберёт написанные раннее тесты doctest и запустит их.
"""