"""Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""
import unittest
from task_01_funk_del_symbols import clean_text


class TestCleanTest(unittest.TestCase):
    def testSameText(self):
        self.assertEqual(clean_text('the same text'), 'the same text', msg='Something is not OK')

    def testLowerCaseText(self):
        self.assertEqual(clean_text('MAKE THE TEXT LOWER'), 'make the text lower', msg='Something is not OK')

    def testPunctuationsDeleting(self):
        self.assertEqual(clean_text('deleting all the punctuations symbols !@#$%^&*()?<>,.'),
                         'deleting all the punctuations symbols ', msg='Something is not OK')

    def testOtherLanguageDeleting(self):
        self.assertEqual(clean_text('deleting all the russian text как дела'),
                         'deleting all the russian text  ', msg='Something is not OK')

    def testAllFunc(self):
        self.assertEqual(clean_text('Make ALL deletions from the text. '
                                    'И русский тоже удалить? Удаляй!'),
                         'make all deletions from the text     ', msg='Something is not OK')


if __name__ == "__main__":
    unittest.main(verbosity=2)
