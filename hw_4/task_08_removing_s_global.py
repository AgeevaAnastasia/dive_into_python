"""
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""


def change_global():
    global glob
    glob = globals()
    my_dict = {}
    for key, value in glob.items():
        if key != 's' and key.endswith('s'):
            my_dict[key[:-1]] = value
            glob[key] = None
    glob |= my_dict


names = ['Петя', 'Вася', 'Аня']
numbers = [12, 24, 35, 198]
five = 5
man = 'Гена'

change_global()
print(f'names: {names}, \nname: {name}, \nnumbers: {numbers}: \nnumber: {number}, \nfive: {five}, \nman: {man}')
