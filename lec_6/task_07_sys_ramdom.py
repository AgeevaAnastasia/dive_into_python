"""
Некоторые модули “из коробки”

Рассмотрим несколько модулей из стандартной библиотеки Python. Точнее даже не
модули целиком, а некоторые функции из модулей.

Модуль sys
С модулем sys мы уже познакомились. Он относится к группе служебных в Python.
Модуль sys обеспечивает доступ к некоторым переменным, используемым или
поддерживаемым интерпретатором, а также к функциям, тесно
взаимодействующим с интерпретатором. Изучать все переменные и функции не
имеет смысла. Даже опытные разработчики не пользуются всеми, а их в модуле
около сотни. При необходимости вы всегда сможете найти описание той или иной
функции или переменной в официальной документации. Рассмотрим лишь одну
переменную модуля — argv.

Запуск скрипта с параметрами
Python позволяет запускать скрипты с параметрами. Для этого после имени
исполняемого файла указываются ключи и/или значения через пробел.
Например создадим файл script.py со следующим кодом."""

print('start')
print('stop')

"""Открываем консоль операционный системы и вводим команду на запуск.
python3 script.py

🔥 Важно! Для UNIX ОС используем команду python3. В Windows — python.

🔥 Важно! Не перепутайте консоль ОС и терминал интерпретатора Python.
Терминал выдаёт в начале строки приветствие на ввод — тройную стрелку >>>.
Скрипт вывел текст в консоль и завершил работу. Научим его принимать значения
из командной строки."""

from sys import argv
print('start')
print(argv)
print('stop')

"""Переменная argv содержит список. В нулевой ячейке имя запускаемого скрипта. В
последующих ячейках переданные значения.
Например при запуске следующей строки:

python script.py -d 42 -s "Hello world!" -k 100

получим следующий список:

['script.py', '-d', '42', '-s', 'Hello world!', '-k', '100']


Обратите внимание, что все значения переданы как строки даже числовые. Строка
“Hello world!” передана как один объект, потому что при вызове скрипта была
заключена в двойные кавычки.

Переменная argv позволяет решать простые задачи работы с командной строкой.
Если ваш будущий проект будет требовать более сложной обработки переданных в
скрипт параметров, обратите внимание на встроенный в Python модуль argparse.




Модуль random
Модуль используется для генерации псевдослучайных чисел. Почти все функции
модуля зависят от работы функции random(), которая генерирует псевдослучайные
числа в диапазоне от нуля включительно до единицы исключительно — [0, 1).

🔥 Важно! Генераторы псевдослучайных чисел модуля не должны
использоваться в целях безопасности. Для обеспечения безопасности или
криптографии необходимо использовать модуль secrets.

Для управления состоянием используют следующие 3 функции:
● seed(a=None, version=2) — инициализирует генератор. Если значение a не
указано, для инициализации используется текущее время ПК. Версия 2
используется со времён Python 3.2 как основная. Не стоит менять её.
● getstate() — возвращает объект с текущим состоянием генератора.
● setstate(state) — устанавливает новое состоянии генератора, принимая на
вход объект, возвращаемый функцией getstate.
Рассмотрим несколько часто используемых функции генерации чисел.
● randint(a, b) — генерация случайного целого числа в диапазоне от a
включительно до b включительно — [a, b].
● uniform(a, b) — генерация случайного вещественного числа в диапазоне от a
до b. Правая граница может как входить, так и не входить в возвращаемый
диапазон. Зависит от способа округления.
● choice(seq) — возвращает случайный элемент из непустой
последовательности.
● randrange(stop) или randrange(start, stop[, step]) работает как вложение
функции range в функцию choice, т.е. choice(range(start, stop, step)).
Возвращает случайное число от start до stop с шагом step.
● shuffle(x) — перемешивает случайным образом изменяемую
последовательность in place, т.е. не создавая новую.
● sample(population, k, *, counts=None) — выбирает k уникальных элементов из
последовательности population и возвращает их в новой последовательности.
Параметр counts позволяет указать количество повторов элемента.
Все описанные функции представлены в листинге ниже."""

import random as rnd

START = -100
STOP = 1_000
STEP = 10
data = [2, 4, 6, 8, 42, 73]
print(rnd.random())
rnd.seed(42)
state = rnd.getstate()
print(rnd.random())
rnd.setstate(state)
print(rnd.random())
print(rnd.randint(START, STOP))
print(rnd.uniform(START, STOP))
print(rnd.choice(data))
print(rnd.randrange(START, STOP, STEP))
print(data)
rnd.shuffle(data)
print(data)
print(rnd.sample(data, 2))
print(rnd.sample(data, 2, counts=[1, 1, 1, 1, 1, 100]))
