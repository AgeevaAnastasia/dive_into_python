"""
Напишите функцию для транспонирования матрицы"""


def matrix_transposition(matrix):
    matrix_res = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix_res)):
        for j in range(len(matrix_res[0])):
            matrix_res[i][j] = matrix[j][i]
    return matrix_res


matrix_user = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(matrix_user)
print(matrix_transposition(matrix_user))
