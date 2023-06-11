"""
✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа"""

my_tuple = {'hi', 'hello', 1, 3, 5.3, 2.1, (1, 4,), (10, 3.5,)}

'''
set_keys = set()
for item in my_tuple:
    set_keys.add(type(item))

my_dict = dict.fromkeys(set_keys, 0)

for key in my_dict.keys():
    temp_lst = []
    for item in my_tuple:
        if type(item) == key:
            temp_lst.append(item)
            my_dict[key] = temp_lst'''

my_dict = {}

'''for item in my_tuple:
    res = type(item)
    if res in my_dict:
        my_dict[res].append(item) # здесь к уже существующему списку добавляем элемент
    else:
        my_dict[res] = [item] # здесь создаем не просто переменную, а сразу список в []'''

for item in my_tuple:
    my_dict.setdefault(type(item), []).append(item)
    # my_dict[type(item)] = my_dict.get(type(item), []) + [item]

print(my_dict)
