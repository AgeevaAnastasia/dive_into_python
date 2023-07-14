"""Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
загрузка данных (функция из задания 4)
вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
"""
import json
from task_03_level_access_exception import AccessException, LevelException

from task_04_id_level_access import User


class Project:
    def __init__(self, users, filename):
        self.users = users
        self.admin = None
        self.filename = filename

    @classmethod
    def load(cls, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                users_dict = json.load(f)
        except Exception as e:
            print(f'При открытии файла {filename} возникла ошибка {e}. ')
        else:
            # print(f'{users_dict = }')
            users = []
            for level, user in users_dict.items():
                for user_id, name in user.items():
                    users.append(User(user_id, name, level))
            return Project(users, filename)

    def __str__(self):
        return str(self.users)

    def __enter__(self):
        pass

    # * метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера
    def __exit__(self, exc_type, exc_val, exc_tb):
        # print(self.filename)
        users_dict = {}
        for user in self.users:
            if user.level not in users_dict.keys():
                users_dict.update({user.level: {}})
            users_dict[user.level].update({user.user_id: user.name})
        # print(f'{users_dict = }')
        with open(self.filename, "w", encoding="utf-8") as f_json:
            # записываем словарь в json-файл с отступом=1
            json.dump(users_dict, f_json, indent=1, ensure_ascii=False)
            print(f'Записал список пользователей {users_dict = } в файл {self.filename}')

    # * метод удаления пользователя из списка пользователей проекта
    def del_user(self, user_del):
        for user in self.users:
            if user == user_del:
                print(f'{user} удаляется из проекта')
                self.users.remove(user)

    # вход в систему
    def login(self, user_id, name):
        user_new = User(user_id, name)
        if user_new not in self.users:
            raise AccessException(user_id)
        for user in self.users:
            if user_new == user:
                self.admin = user

    # добавление пользователя
    def add_user(self, user_id, name, level):
        if int(self.admin.level) >= int(level):
            raise LevelException(level, name)
        self.users.append(User(user_id, name, level))


if __name__ == '__main__':
    file = 'users.json'
    project = Project.load(file)
    # print(project)
    with project:
        project.login('006', 'Люся')
        print(f'Admin --- > {project.admin}')
        project.add_user('010', 'Мустафа', '7')
        print(*project.users)
        user_delete = User('010', 'Мустафа', '7')
        project.del_user(user_delete)