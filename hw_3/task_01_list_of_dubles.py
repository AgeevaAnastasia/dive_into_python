"""
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

my_list = [1, 6, 3, 7, 9, 8, 2, 4, 3, 2, 8, 1]

res_list = []
for item in my_list:
    if my_list.count(item) > 1:
        if item not in res_list:
            res_list.append(item)

print(f'В исходном списке {my_list} дублируются элементы: {res_list}')
