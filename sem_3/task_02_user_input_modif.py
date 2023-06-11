"""
Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях
"""

user_input = input('Введите что-либо: ')

if user_input.isdecimal():
    res = int(user_input)
elif user_input.replace('.', '').replace(',', '').replace('-', '').replace(' ', '').isdecimal() \
        and ((user_input.count('.') == 1 or user_input.count(',') == 1) \
        or (user_input.count('-') <= 1 and user_input[1:].count('-')) == 0):
    res = float(user_input.replace(',', '.').replace(' ', ''))
elif user_input.islower():
    res = user_input
else:
    res = user_input.upper()

print(res, type(res))
