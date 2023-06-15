"""
Хэш hash() как проверка на неизменяемость
Второй вариант убедиться в изменяемости или неизменяемости — проверка
на хеширование.

Хеш — это криптографическая функция хеширования, которую обычно
называют просто хэшем. Хеш-функция представляет собой алгоритм,
который может преобразовать произвольный массив данных в набор бит
фиксированной длины.

В Python для получения хеша используется функция hash(). Если объект
является неизменяемым, функция возвращает число — хеш-сумму.
Изменяемые объекты хешировать нельзя исходя из самого определения
хеш-функции. Если массив данных может меняться, значит будет меняться и
хеш-сумма. Подобное поведение нарушало бы логику кода. Рассмотрим на
примере."""

x = 42
y = 'text'
z = 3.1415
print(hash(x), hash(y), hash(z))
my_list = [x, y, z]
print(hash(my_list)) # получим ошибку, т.к. list изменяемый

"""Как видите нижняя строка кода вызывает ошибку TypeError: unhashable type:
'list' Если вдруг забыли изменяемый объект или нет, просто попробуйте
получить его хеш.
"""