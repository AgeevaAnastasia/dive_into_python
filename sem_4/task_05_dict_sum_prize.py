"""
✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии. """


def get_sum(names, salaries, bonus):
    #sum_money = [i[0] * float(i[1].strip('%')) / 100 for i in zip(salaries, bonus)]
    #return dict(zip(names, sum_money))
    salary_dict = {}
    for name, salary, bonus in zip(names, salaries, bonus):
        salary_dict[name] = salary * float(bonus[:-1]) / 100
    return salary_dict


names_user = ["Иванов", "Петров", "Сидоров"]
salaries_user = [20000, 25000, 30000]
bonus_user = ['10.25%', '11%', '11.5%']

print(get_sum(names_user, salaries_user, bonus_user))
