"""
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке
"""

for i in range(2, 10):
    for j in range(2, 6):
        print(j, '*', i, '=', i * j, end='\t\t')
    print()
print('\n')
for i in range(2, 10):
    for j in range(6, 10):
        print(j, '*', i, '=', i * j, end='\t\t')
    print()
