"""Создайте класс Матрица. Добавьте методы для:
- вывода на печать,
- сравнения,
- сложения,
- *умножения матриц"""


class Matrix:
    """Класс для вывода, сравнения, сложения, умножения двух матриц"""

    def __init__(self, matrix):
        """Инициализация экземпляра класса"""
        self.matrix = matrix

    def __str__(self):
        """Вывод матрицы на печать в консоль"""
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix) + '\n'

    def __eq__(self, other):
        """Проверка двух матриц на равенство"""
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return False
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    def __ne__(self, other):
        """Проверка матриц на неравенство"""
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return True
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return True
        return False

    def __gt__(self, other):
        """Сравнение матриц: первая матрица больше второй"""
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return False
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] > other.matrix[i][j]:
                    return True
        return False

    def __ge__(self, other):
        """Сравнение матриц: первая матрица больше или равна второй"""
        if self.__eq__(other) or self.__gt__(other):
            return True
        return False

    def __lt__(self, other):
        """Сравнение матриц: первая матрица меньше второй"""
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return False
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] < other.matrix[i][j]:
                    return True
        return False

    def __le__(self, other):
        """Сравнение матриц: первая матрица меньше или равна второй"""
        if self.__eq__(other) or self.__lt__(other):
            return True
        return False

    def __add__(self, other):
        """Сложение двух матриц"""
        return [[self.matrix[i][j] + other.matrix[i][j]
                 for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]

    def __mul__(self, other):
        """Умножение двух матриц"""
        if not len(self.matrix) == len(other.matrix[0]):
            return 'Матрицы не согласованы, умножение невозможно'

        result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0])))
                   for j in range(len(other.matrix[0]))] for i in range(len(self.matrix))]
        return result


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m1)
print(m2)
print()

print(f'm1 = m2 is {m1 == m2}')
print(f'm1 != m2 is {m1 != m2}')
print(f'm1 > m2 is {m1 > m2}')
print(f'm1 >= m2 is {m1 >= m2}')
print(f'm1 < m2 is {m1 < m2}')
print(f'm1 <= m2 is {m1 <= m2}')
print(f'm1 + m2 = {m1 + m2}')
print(f'm1 * m2 = {m1 * m2}')
