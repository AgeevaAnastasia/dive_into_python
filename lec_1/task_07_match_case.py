"""
Выбор из вариантов, match и case
В Python версии 3.10, т.е. совсем недавно появилась новая возможность
множественного сравнения. Это конструкция match и case. После match указываем
23
переменную для сравнения. Далее идёт блок из множества case с вариантами
сравнения. Рассмотрим работу кода на примере.
🔥 Важно! Если у вас стоит Python версии 3.9 и ниже, код не будет работать."""

color = input('Твой любимый цвет: ')
match color:
    case 'красный' | 'оранжевый':
        print('Любитель яркого')
    case 'зелёный':
        print('Ты не охотник?')
    case 'синий' | 'голубой':
        print('Ха, классика!')
    case _:
        print('Тебя не понять')

"""
Данный код аналогичен прошлому варианту с elif. Добавлена возможность
проверить несколько цветов. Например для красного и оранжевого будет один
вывод. Вертикальная черта играет роль оператора "или". Уточню что пользователь
вводит один единственный цвет.
Вместо слова else в данной конструкции используется сочетание case _ На этом
курсе мы ещё несколько раз будет встречаться с подчеркиванием. И каждый раз он
имеет разные эффект в зависимости от применения."""
