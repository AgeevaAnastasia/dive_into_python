"""Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""
import pytest
from task_01_funk_del_symbols import clean_text


def test_same_text():
    assert clean_text('the same text') == 'the same text', 'Something is not OK'


def test_lower_case_text():
    assert clean_text('MAKE THE TEXT LOWER') == 'make the text lower', 'Something is not OK'


def test_punctuations_deleting():
    assert clean_text('deleting all the punctuations '
                      'symbols !@#$%^&*()?<>,.') == 'deleting all the punctuations symbols ', \
        'Something is not OK'


def test_other_language_deleting():
    assert clean_text('deleting all the russian text как дела') == 'deleting all the russian text  ', \
        'Something is not OK'


def test_all_func():
    assert clean_text('Make ALL deletions from the text. И русский тоже удалить? '
                      'Удаляй!') == 'make all deletions from the text     ', \
        'Something is not OK'


if __name__ == "__main__":
    # ['-v'] -  для подробных выводов
    if __name__ == '__main__':
        pytest.main(['-v'])
