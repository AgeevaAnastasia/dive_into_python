"""
Ещё раз про import

Мы уже использовали зарезервированное слово import для добавление в
собственный код расширенного функционала. Разберём import подробнее.

💡 PEP-8! Строки импорта рекомендуется писать в самом начале файла,
оставляя 1-2 пустые строки после него."""

import sys
print(sys)
print(sys.builtin_module_names)
print(*sys.path, sep='\n')

"""Мы импортировали модуль sys из стандартной библиотеки Python. Механизм
импорта выполняет поиск указанного имени (в нашем примере — “sys”) в
нескольких местах. В первую очередь проверяется список встроенных модулей,
который хранится в sys.builtin_module_names. Если имя модуля не найдено,
проверка ведётся в каталогах файловой системы, которые перечислены в sys.path.

🔥 Важно! Обычно (но не всегда) имя модуля заканчивается расширением
.py. При импорте расширение не указывается.

В результате импорта имя sys было добавлено в текущую, глобальную область
видимости. Для того, чтобы получить доступ к переменным, функциям, классам и
т.п. содержимому модуля используется точечная нотация:
имя_модуля<точка>имя_объекта.

Обратиться к объекту внутри модуля напрямую при “обычном” импорте не
получится. Подобный подход защищает от конфликта имён. Если и в вашем файле и
в импортируемом модуле есть функция func(), конфликта имён не будет. Свою
функцию вызываете как func(), а функцию из модуля как module_name.func()

● Переменная sys.path
Содержимое переменной sys.path формируется динамически. В качестве первого
адреса указывается путь до основного файла. Например если вы используете Unix
подобную ОС и ваш скрипт расположен по адресу /home/user/project, именно этот
путь будет первым в списке поиска модулей.

Далее в sys.path перечислены пути из PYTHONPATH и пути, указанные при
установке Python и создании виртуального окружения. Таким образом Python ищет
импортируемый модуль практически во всех местах, где этот модуль мог быть
установлен.

🔥 Важно! Если создать собственный файл с именем аналогичным имени
модуля, Python импортирует ваш файл, а не модуль. Строго не рекомендуется
использовать для своих файлов имена встроенных модулей. В редких
исключительных ситуациях стоит добавлять символ подчёркивания в конце
имени, чтобы избежать двойного именования.


● Антипримеры импорта
Взгляните на антипример. Мы создали файл random.py со следующим кодом."""
def randint(*args):
    return 'Не то, что вы искали!'

"""Импортируем модуль random в основном файле проекта и попробуем
сгенерировать случайное число от 1 до 6."""

import random
print(random.randint(1, 6))

"""В результате работы получим “Не то, что вы искали!”. Подробнее о модуле для
генерации случайных чисел поговорим далее в этом уроке.

💡 PEP-8! При импорте нескольких модулей каждый указывается с новой
строки.

Правильно:
import sys
import random

Неправильно:
import sys, random
"""