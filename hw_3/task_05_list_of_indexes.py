"""
✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.
"""

my_list = [2, 4, 6, 1, 3, 6, 7, 3, 8, 4, 8, 7, 3, 1, 6]

list_of_indexes_odd = []
for i in range(len(my_list)):
    if my_list[i] % 2 == 1:
        list_of_indexes_odd.append(i + 1)

print(f'порядковые номера нечетных чисел в списке {my_list}:', end=' ')
print(*list_of_indexes_odd)
