"""
✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили.
Сохраните его итераторатор.
✔ Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
"""
my_dict = {item: ord(item) for item in set('jxiekglz;bkjwnbdjks')}
iter_dict = iter(my_dict.items())
for _ in range(5):
    print(next(iter_dict))
