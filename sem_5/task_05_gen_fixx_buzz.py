"""
✔ Напишите программу, которая выводит
на экран числа от 1 до 100.
✔ При этом вместо чисел, кратных трем,
программа должна выводить слово «Fizz»
✔ Вместо чисел, кратных пяти — слово «Buzz».
✔ Если число кратно и 3, и 5, то программа
должна выводить слово «FizzBuzz».
✔ *Превратите решение в генераторное выражение.

for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz', end=' ')
    elif i % 3 == 0:
        print('Fizz', end=' ')
    elif i % 5 == 0:
        print('Buzz', end=' ')
    else:
        print(i, end=' ')"""


def gen_fizzbuzz(min_n, max_n):
    for i in range(min_n, max_n + 1):
        if i % 15 == 0:
            yield 'FizzBuzz'
        elif i % 3 == 0:
            yield 'Fizz'
        elif i % 5 == 0:
            yield 'Buzz'
        else:
            yield i


print(*gen_fizzbuzz(1, 100), sep='\n')
print()

gen_oneliner_fizzbuzz = ('FizzBuzz' if i % 15 == 0 else
                         'Buzz' if i % 5 == 0 else
                         'Fizz' if i % 3 == 0
                         else i for i in range(1, 101))
print(*gen_oneliner_fizzbuzz, sep='\n')
