"""Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""
import string


def clean_text(text: str) -> str:
    """
    Deleting symbols from text, except latin alphabet characters and whitespaces.
    :return: string in lower register.
    >>> clean_text('the same text')
    'the same text'
    >>> clean_text('MAKE THE TEXT LOWER')
    'make the text lower'
    >>> clean_text('deleting all the punctuations symbols !@#$%^&*()?<>,.')
    'deleting all the punctuations symbols '
    >>> clean_text('deleting all the russian text как дела')
    'deleting all the russian text  '
    >>> clean_text('Make ALL deletions from the text. И русский тоже удалить? Удаляй!')
    'make all deletions from the text     '
    """
    text = ([item if item in string.ascii_letters or item in string.whitespace else '' for item in text])
    return ''.join(text).lower()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)