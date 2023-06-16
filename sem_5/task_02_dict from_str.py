"""
✔ Самостоятельно сохраните в переменной строку текста.
✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
✔ Напишите преобразование в одну строку.
"""
my_dict = {item: ord(item) for item in set('jxiekglz;bkjwnbdjks')}
#my_dict = {item: ord(item) for item in set(input('Введите строку: '))}
print(my_dict)
