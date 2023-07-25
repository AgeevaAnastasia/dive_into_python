"""Команда finally

Ещё одна команда для обработки исключений — finally. Она срабатывает во всех
случаях. И если была ошибка, и отработал блок except. И если ошибки не было."""


def get(text: str = None) -> int:
    num = None
    try:
        num = int(input(text))
    except ValueError as e:
        print(f'Ваш ввод привёл к ошибке ValueError: {e}')
    finally:
        return num if isinstance(num, int) else 1


if __name__ == '__main__':
    number = get('Введите целый делитель: ')
    try:
        print(f'100 / {number} = {100 / number}')
    except ZeroDivisionError as e:
        print(f'На ноль делить нельзя. Получим {e}')


"""Даём пользователю одну попытку на ввод числа. Независимо от результата
сработает блок finally. Он вернёт либо целое число, либо единицу, если получить
целое не удалось. Обработку деления на ноль вынесли в основной код.
Обычно finally используют для действий, которые обязательны независимо от того
была ошибка или нет.


Блок finally без except

Вполне допустимо использовать только связку try-finally. Например мы хотим
прочитать информацию из файла. И независимо от результат чтения закрыть его."""


file = open('text.txt', 'r', encoding='utf-8')
try:
    data = file.read().split()
    print(data[len(data)])
finally:
    print('Закрываю файл')
    file.close()


"""Открываем файл для чтения, скачиваем его и сохраняем каждую строку в
отдельную ячейку списка. Но внезапно “забываем”, что нумерация начинается с
нуля, а для доступа к последнему элементу можно использовать индекс -1. В
результате попытка прочитать информацию из ячейки, следующей за последней
выдаёт ошибку IndexError: list index out of range. Но блок finally закрывает файл
раньше, чем программа завершит свою работу.


🔥 Важно! Для ситуации выше правильным будет использовать менеджер
контекста для гарантированного закрытия файла.
Как вы можете видеть комбинации try-except-else-finally дают большой простор для
отлова исключений и изменения логика кода в зависимости от ситуаций.
"""