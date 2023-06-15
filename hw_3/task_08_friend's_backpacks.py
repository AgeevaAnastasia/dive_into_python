"""
✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""

backpacks = {'Alex': ('thing_1', 'thing_2', 'thing_3', 'thing_4'),
             'Dan': ('thing_2', 'thing_4', 'thing_5', 'thing_6'),
             'Ann': ('thing_1', 'thing_5', 'thing_7', 'thing_8', 'thing_9', 'thing_10')}
friends = list(backpacks.keys())
res_all = set()
for i in range(len(friends)):
    res_all = res_all | set(backpacks[friends[i]])
print(f'У всех друзей во всех рюкзаках есть такие вещи: \n{res_all}', end='\n\n')

for i in range(len(friends)):
    temp_set = set(backpacks[friends[i]])
    for j in range(len(backpacks)):
        if j == i:
            continue
        temp_set = temp_set - set(backpacks[friends[j]])
    print(f'Только у {friends[i]} есть {temp_set}')
print()

for i in range(len(friends)):
    temp_set = set()
    temp_list = []
    for j in range(len(backpacks)):
        if j == i:
            continue
        temp_set = temp_set | set(backpacks[friends[j]])
    for item in temp_set:
        if item not in set(backpacks[friends[i]]):
            temp_list.append(item)
    print(f'Только у {friends[i]} нет {temp_list}')
