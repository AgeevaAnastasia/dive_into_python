"""
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого
отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется
больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""


def is_triangle(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False


def is_isosceles(a, b, c):
    if a == b or b == c or a == c:
        return True
    else:
        return False


def is_equilateral(a, b, c):
    if a == b and b == c:
        return True
    else:
        return False


a_user = float(input('Введите сторону a: '))
b_user = float(input('Введите сторону b: '))
c_user = float(input('Введите сторону c: '))

if is_triangle(a_user, b_user, c_user):
    if is_isosceles(a_user, b_user, c_user):
        if is_equilateral(a_user, b_user, c_user):
            print('Это равносторонний треугольник')
        else:
            print('Это равнобедренный треугольник')
    else:
        print('Такой треугольник существует')
else:
    print('Такой треугольник не существует')
