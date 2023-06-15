"""
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка."""


def sum_between(nums, ind_1, ind_2):
    if ind_2 < ind_1:
        ind_1, ind_2 = ind_2, ind_1
    if ind_1 < 0:
        ind_1 = 0
    if ind_2 > len(nums):
        ind_2 = len(nums) - 1
    sum_nums = 0
    for i in range(ind_1, ind_2 + 1):
        sum_nums += nums[i]
    return sum_nums


nums_user = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum_between(nums_user, -6, 3))
