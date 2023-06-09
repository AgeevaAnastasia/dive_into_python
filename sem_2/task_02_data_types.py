"""
Создайте в переменной data список значений разных типов перечислив их
через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
* порядковый номер начиная с единицы
* значение
* адрес в памяти
* размер в памяти
* хэш объекта
* результат проверки на целое число только если он положительный
* результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты.
"""

data = [1, 5.23, 'hello', 15, True, 4.8, 'hello', 1]

count = 1
for num, i in enumerate(data):
    print(f'Порядковый номер: {count};', end=' ')
    print(f'Значение: {i};', end=' ')
    print(f'Адрес в памяти: {id(i)};', end=' ')
    print(f'Размер в памяти: {i.__sizeof__()};', end=' ')
    print(f'Хэш объекта: {hash(i)};', end=' ')
    if isinstance(i, int):
        print(f'Элемент {i} является целым числом.', end=' ')
    if isinstance(i, str):
        print(f'Элемент {i} является строкой.', end=' ')
    count += 1
    print('\n')
