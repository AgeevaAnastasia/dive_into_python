"""
Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
*Строки нумеруются начиная с единицы.
*Слова выводятся отсортированными согласно кодировки Unicode.
* Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.
"""


def print_words_list(text):
    example = text.split()
    example.sort()
    max_len = len(max(example, key=len))
    for num, item in enumerate(example, 1):
        print(f'{num}: {item:>{max_len}}')


print_words_list("Sdfj  slkdjf ejejej ghsdjfs skdjfkjs")
