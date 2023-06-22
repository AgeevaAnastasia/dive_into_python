"""
Создайте функцию генератор чисел Фибоначчи
"""
NUMBER_OF_NUMBERS = 30


def fib(n): # это генератор первых n чисел Фибоначчи, а не ВСЕХ!
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


def fibonacci_generator(): # это генератор ВСЕХ чисел Фибоначчи. Если нужно их 5, то вызывать 5 раз
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print(*fib(NUMBER_OF_NUMBERS), sep='\n')
