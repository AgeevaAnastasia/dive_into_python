"""
Создайте функцию генератор чисел Фибоначчи
"""
NUMBER_OF_NUMBERS = 30


def fib(n):
    count = 0
    yield 0
    yield 1
    num1 = 0
    num2 = 1
    while count < n - 1:
        num = num1 + num2
        yield num
        num1, num2 = num2, num
        count += 1


print(*fib(NUMBER_OF_NUMBERS), sep='\n')
