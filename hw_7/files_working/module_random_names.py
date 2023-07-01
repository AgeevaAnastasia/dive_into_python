"""
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""
from random import shuffle, randint, sample

MIN_LETTERS = 4
MAX_LETTERS = 7
VOWELS = 'аеёиоуыэюя'
LITERALS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
NOT_FIRST = 'йъыь'



def gen_pseudonyms(count, filename):
   with open (filename, 'a', encoding='utf-8') as f:
        for _ in range(count):
            name = sample(LITERALS, randint(MIN_LETTERS, MAX_LETTERS))
            if not set(name) & set(VOWELS):
                half = len(name) // 2
                name = name[:half] + sample(VOWELS, half)
                shuffle(name)
            while True:
                if name[0] in NOT_FIRST:
                    print(name)
                    shuffle(name)
                else:
                    break
            name = ''. join(name).capitalize()
            f.write(f'{name}\n')

if __name__ == '__main__':
#    nums_to_file(int(input('Введите количество имен, которые нужно сгенерировать: ')), input('Введите имя файла: '))
    gen_pseudonyms(10, 'names.txt')
