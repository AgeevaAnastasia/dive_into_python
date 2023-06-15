"""
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию."""


def unicode_text(text):
    set_text = set(text)
    res_text = []
    for item in set_text:
        res_text.append(ord(item))
    res_text = sorted(res_text, reverse=True)
    return res_text


print(unicode_text("help"))
