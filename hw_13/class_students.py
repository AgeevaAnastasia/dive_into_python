"""Создайте класс студента.
Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Названия предметов должны загружаться из файла CSV при создании экземпляра.
Другие предметы в экземпляре недопустимы.
Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
Также экземпляр должен сообщать средний балл по тестам для каждого предмета и
по оценкам всех предметов вместе взятых."""
import csv
import json
from statistics import mean
from my_exceptions import NameException, RangeException

MARK_MAX = 5
MARK_MIN = 2
TEST_MAX = 100
TEST_MIN = 0


class Check:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if isinstance(value, str):
            if not value.replace(' ', '').isalpha() or not value.istitle():
                raise NameException(value)
        elif isinstance(value, int):
            if (self.min_value is not None and value < self.min_value) or (self.max_value is not None and value >= self.max_value):
                raise RangeException(self.min_value, self.max_value - 1)
        else:
            raise TypeError(f'Неверные данные {value}.')


class Student:
    name = Check()
    mark = Check(MARK_MIN, MARK_MAX + 1)
    test_result = Check(TEST_MIN, TEST_MAX + 1)

    def __init__(self, name, file='subjects.csv'):
        self.name = name
        self._subjects = {}
        with open(file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for line in reader:
                self._subjects[line[0]] = {'mark': None, 'tests': []}

    def __str__(self):
        return f'Студент {self.name}: \n' \
               f'{self._subjects} \n'

    def is_subject(self, subject):
        if subject not in self._subjects.keys():
            raise ValueError(f'Предмета {subject} нет в расписании текущего семестра')

    def put_mark(self, subject):
        self.is_subject(subject)
        avg = mean(self._subjects[subject]['tests'])
        if avg >= 85:
            mark = 5
        elif 65 < avg < 85:
            mark = 4
        elif 45 < avg <= 65:
            mark = 3
        else:
            mark = 2
        self._subjects[subject]['mark'] = mark

    def put_test_result(self, subject, test_result):
        self.test_result = test_result
        self.is_subject(subject)
        self._subjects[subject]['tests'].append(self.test_result)

    def average_tests(self):
        result = {subject: mean(self._subjects[subject]['tests']) for subject in self._subjects.keys()}
        return f'Средняя оценка по тестам по предметам студента {self.name}: \n' \
               f'{result} \n'

    def average_marks(self):
        data = []
        for key in self._subjects.keys():
            if self._subjects[key]['mark'] is not None:
                data.append(self._subjects[key]['mark'])
        return f'Средняя балл за семестр студента {self.name}: {mean(data)} \n'

    def student_to_csv(self):
        file = self.name + '.csv'
        with open(file, 'w', newline='', encoding='utf-8') as f:
            csv_write = csv.writer(f)
            for key, value in self._subjects.items():
                csv_write.writerow([key, value])

    def student_to_json(self):
        file = self.name + '.json'
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(self._subjects, f, indent=2)


if __name__ == '__main__':
    student1 = Student('Иванов Иван')
    student1.put_test_result('math', 94)
    student1.put_test_result('math', 90)
    student1.put_test_result('math', 98)
    student1.put_test_result('history', 67)
    student1.put_test_result('history', 80)
    student1.put_test_result('history', 45)
    student1.put_test_result('literature', 89)
    student1.put_test_result('literature', 45)
    student1.put_test_result('literature', 67)
    student1.put_test_result('native_language', 67)
    student1.put_test_result('native_language', 86)
    student1.put_test_result('native_language', 75)
    student1.put_test_result('foreign_language', 45)
    student1.put_test_result('foreign_language', 56)
    student1.put_test_result('foreign_language', 67)
    student1.put_test_result('physics', 92)
    student1.put_test_result('physics', 78)
    student1.put_test_result('physics', 88)
    student1.put_test_result('chemistry', 67)
    student1.put_test_result('chemistry', 86)
    student1.put_test_result('chemistry', 93)
    student1.put_test_result('biology', 55)
    student1.put_test_result('biology', 57)
    student1.put_test_result('biology', 68)

    student1.put_mark('math')
    student1.put_mark('history')
    student1.put_mark('literature')
    student1.put_mark('native_language')
    student1.put_mark('foreign_language')
    student1.put_mark('physics')
    student1.put_mark('chemistry')
    student1.put_mark('biology')

    print(student1)

    print(student1.average_tests())

    print(student1.average_marks())

    student1.student_to_csv()

    student1.student_to_json()

    student2 = Student('Петров петр')
    student3 = Student('Сидорова Екатерина')
    student3.put_test_result('math', 124)
