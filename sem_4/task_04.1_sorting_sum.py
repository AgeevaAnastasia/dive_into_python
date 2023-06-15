"""
✔ Функция получает на вход список чисел.
✔ Отсортируйте список по убыванию суммы цифр"""


def get_sum_num(num):
    return sum(map(int, str(num)))


def get_dict(nums):
    dict_nums = {}
    for item in nums:
        dict_nums[item] = get_sum_num(item) # либо sum(map(int, str(item)))
    res = dict(sorted(dict_nums.items(), key=lambda x: x[1],  reverse=True))
    return res

    #return dict(sorted((zip(map(nums, get_sum_num), nums)), key=lambda x: -x[0]))


input_data = [2, 23, 91, 33, 49, 47, 73, 14, 58, 9] #input('Введите числа: ').split()
print(input_data)
#print(sorted(input_data, key=get_sum_num, reverse=True))
print(get_dict(input_data))
