"""
Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различные случайные варианты и выведите 4 успешных расстановки.
*Выведите все успешные варианты расстановок
"""
N = 8  # размер доски и количество ферзей


def checkmate_queens(x):
    global solutions, matrix
    if x < N:
        for matrix[x] in range(N):
            for y in range(x - 1, -1, -1):
                if matrix[x] == matrix[y] or abs(matrix[x] - matrix[y]) == (x - y):
                    break
            else:
                checkmate_queens(x + 1)
    elif N > 0:
        solutions += 1
        for i in range(N - 1):
            print(f'{chr(i + 65)}{matrix[i] + 1}', end=' ') # замена первой цифру на букву
        else:
            print(f'{chr(N + 64)}{matrix[N - 1] + 1}')


# создание матрицы, заполненной нулями, для того, чтобы не было выхода за пределы при переборе
matrix = [[0 for j in range(2)] for i in range(8)]
solutions = 0
checkmate_queens(0)
print(f'Всего решений: {solutions}')
