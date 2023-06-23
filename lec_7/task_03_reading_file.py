"""
Чтение файла: целиком, через генератор
Рассмотрим подробнее варианты чтения информации из файла.

● Чтение в список"""

with open('text_data.txt', 'r', encoding='utf-8') as f:
    print(list(f))


"""Мы уже использовали приём чтения всего файла построчно в ячейки списка.
Медленная по времени и затратная по памяти операция. Но обратите внимание на
окончание каждой строки. Символ “\n” означает перенос строки. Разные ОС для
обозначения переноса строки используют “\n”, “\r\n” или даже “\r”. Python берёт
работу по конвертации символа окончания строки на себя. При чтении любое
окончание заменяется на “\n”. А при записи текстового файла окончание “\n”
заменяется на окончание для вашей ОС.

● Чтение методом read
Ещё один вариант чтения файла — метод read().
read(n=-1) — читает n символов или n байт информации из файла. Если n
отрицательное или не указана, читает весь файл. Попытка чтения будет даже в том
случае, когда файл больше оперативной памяти."""

with open('text_data.txt', 'r', encoding='utf-8') as f:
    res = f.read()
    print(f'Читаем первый раз\n{res}')
    res = f.read()
    print(f'Читаем второй раз\n{res}')


"""Если прочитать файл до конца, повторные попытки чтения не будут вызывать
ошибку. Метод будет возвращать пустую строку.
Также при чтении через read не добавляются символы переноса строки. Точнее мы
не видим “\n”, а видим перенос строки на новую строчку."""

SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.read(SIZE):
        print(res)

"""При чтении файла блоками фиксированного размера можно воспользоваться
циклом while. Дочитав до конца в переменную попадёт пустая строка, которая в
цикле будет интерпретирована как ложь и завершит тело цикла.

● Чтение методом readline
Для чтения текстового файла построчно используют метод readline."""

with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline():
        print(res)


"""Обратите внимание на вывод информации. Между строками остаётся по пустой
строке. При чтении readline возвращает строку с символом переноса на конце.
Функция print выводит их на печать и автоматически добавляет переход на
следующую строку. Получаем пару “\n\n”."""

SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline(SIZE):
        print(res)


"""Передача положительного числа в качестве аргумента задаёт границу для длины
строки. Если строка короче границы, она возвращается целиком. А если больше, то
возвращается часть строки заданного размера. При этом следующий вызов метода
вернёт продолжение строки снова фиксированного размера или остаток до конца,
если она короче.

● Чтение циклом for
Вместо метода readline без аргумента можно использовать более короткую запись с
циклом for"""

with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')


"""Файл построчно попадает в переменную line. А для того чтобы избавиться от пустых
строк отключили перенос строки в функции print.

🔥 Важно! Символ переноса строки сохранился в конце каждой строки.

Если вам необходимо обработать строку без переносов, можно использовать
срезы line[:-1] или метод замены line.replace('\n', '')"""

SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line[:-1])
        print(line.replace('\n', ''))
