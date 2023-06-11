"""
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировке Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.
"""

user_text = input("Введите строку текста: ")
# user_text = "Hi, hi, hi! What an amazing meet!"

text = user_text.split(' ')
sort_test_list = sorted(text)
spaces = len(max(sort_test_list, key=len))
print(spaces)

print('Ваша строка в отсортированном списке: ')
for num, item in enumerate(sort_test_list, 1):
    print(f'{num} {item: >{spaces}}')
