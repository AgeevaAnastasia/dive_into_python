"""
Антипаттерн "магические числа"
В прошлом примере мы использовали антипаттерн — плохой стиль для написания
кода. Число 18 используется в коде коде без пояснений. Такой антипаттерн
называется "магическое число". Рекомендуется помещать числа в константы,
которые храняться в начале файла."""

ADULT = 18
age = float(input('Ваш возраст: '))
how_old = age - ADULT
print(how_old, "лет назад ты стал совершеннолетним")

"""Плюсом такого подхода является возможность легко корректировать большие
проекты. Представьте, что в вашем коде несколько тысяч строк, а число 18
использовалось несколько десятков раз.
● При развертывании проекта в стране, где совершеннолетием считается 21
год вы будете перечитывать весь код в поисках магических "18" и править их
на "21". В случае с константой изменить число нужно в одном месте.
● Дополнительный сложности могут возникнуть, если в коде будет 18 как
возраст совершеннолетия и 18 как коэффициент для рассчёт чего-либо.
Теперь править кода ещё сложнее, ведь возраст изменился, а коэффициент
-нет. В случае с сохранением значений в константы мы снова меняем число в
одном месте.
"""