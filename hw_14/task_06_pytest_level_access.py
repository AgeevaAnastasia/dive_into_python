"""На семинаре 13 был создан проект по работе с
пользователями (имя, id, уровень).
Напишите 3-7 тестов pytest для данного проекта.
Используйте фикстуры."""
import pytest
from project_id_level_access import Project, User, AccessException, LevelException

"""Файл как и путь до него может быть отдельной фикстурой, 
данные который после тестов удаляются. 
Используйте встроенную фикстуру tmp_path. Подробнее тут
https://habr.com/ru/companies/tinkoff/articles/745994/"""

@pytest.fixture
def data():
    file = 'users.json'
    return Project.load(file)


def test_create(data):
    assert isinstance(data, Project), 'Something is wrong'


def test_login(data):
    data.login('001', 'Вася')
    assert User('001', 'Вася') in data.users and data.admin.name == 'Вася', 'User logged off'


def test_login_error(data):
    with pytest.raises(AccessException):
        data.login('100', 'Фываолдж')


def test_add_user(data):
    data.login('001', 'Вася') # назначение админа с нужным уровнем доступа
    data.add_user('010', 'Андрей', '6')
    assert User('010', 'Андрей', '6') in data.users, "User wasn't add"


def test_del_user(data):
    user1 = User('006', 'Люся', '4')
    data.del_user(user1)
    assert user1 not in data.users, "User wasn't delete"


if __name__ == '__main__':
    pytest.main(['-v'])
