"""
Напишите программу, которая решает
квадратные уравнения даже если
дискриминант отрицательный.
✔ Используйте комплексные числа
для извлечения квадратного корня.
"""
# чтобы ввести коэффициенты
# a, b, c = map(int, input('Введите a, b, c: ').split())
a = 1
b = -2
c = 5

d = b ** 2 - 4 * a * c

x1 = (-b + complex(d ** 0.5)) / (2 * a)
x2 = (-b - complex(d ** 0.5)) / (2 * a)

print(f'Дискриминант d = {d}; \nпервый корень Х1 = {x1}; \nвторой корень Х2 = {x2}')
