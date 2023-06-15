"""
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают или не совпадают в ваших решениях.
"""

# user_text = input("Введите строку текста: ")
user_text = "sdf jwijasdf jadfjlkjh sd"

dict_count1 = {}
for item in user_text:
    dict_count1[item] = dict_count1.get(item, 0) + 1

dict_count2 = {}
for item in set(user_text):
    dict_count2[item] = user_text.count(item))

print(dict_count1)
print(dict_count2)
