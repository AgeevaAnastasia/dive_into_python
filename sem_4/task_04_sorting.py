"""
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
"""


def my_bubble_sort(numbs):
    for i, item_i in enumerate(numbs):
        for j in range(i, len(numbs)):
            if item_i > numbs[j]:
                numbs[i], numbs[j] = numbs[j], numbs[i]
    return numbs


data = [1, 5, 6, 2, 8, 4, 2, 8, 4, 0, 9, 5] #input('Введите числа: ').split()
print(data)
print(my_bubble_sort(data))
