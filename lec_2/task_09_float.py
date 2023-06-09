"""
Вещественные числа, функция float()

Числа с плавающей запятой представлены классом float. Для хранения таких чисел
ПК, а не только Python используют особый формат представления числа: мантисса и
порядок. Так число 23321.345 правильнее было бы представить как
2.3321345*10**-4.
Особенности подобного формата хранения чисел могут приводить к погрешностям
вычисления."""

print(0.1 + 0.2)

"""Вместо ожидаемого 0.3 получили 0.30000000000000004 При округлении это будет
тот же 0.3. Но когда пишешь код, ожидаешь получить верный результат сразу.
Вторая особенность вещественных чисел - ограничение на хранения информации.
Попробуем сохранить достаточно большое по количеству знаков число с
плавающей точкой."""

pi = 3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375
print(pi)

"""При выводе на печать, а если быть точным, то в момент сохранения объекта в
память в качестве вещественного числа произошло отбрасывание части цифр. В
итоге в памяти осталось 3.141592653589793. И, да, вы верно заметили.
Подчёркивание можно использовать для удобства чтения чисел любого типа.
В случае с математикой вещественных чисел в Python стоит ожидать подобных
погрешностей вычисления и округления. О том как их избежать узнает в конце
сегодняшней лекции. Пока же стоит понять, что float является компактным и
быстрым типом данных для математических операций с плавающей запятой, если
нам не требуется высокая точность результата.
"""