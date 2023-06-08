"""
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""

START_SUM = 0
count_transactions = 0

def deposit_money(acc, count):
    amount = int(input('Введите сумму, кратную 50: '))
    if amount % 50 == 0 and amount > 0:
        acc += amount
        count += 1
    else:
        print('Некорректный ввод. Сумма должна быть кратна 50 и быть больше 0.')
    print(f'У вас на счету: {acc}')
    return acc


def withdraw_money(acc):
    pass
    print(f'У вас на счету: {acc}')


def exit_atm(acc):
    print(f'У вас на счету: {acc}')


account = START_SUM
while True:
    print('''
    Выберите действие:
    1 - положить деньги
    2 - снять деньги
    3 - выйти''')
    choice = input()
    match choice:
        case '1':
            deposit_money(account)
        case '2':
            withdraw_money(account)
        case '3':
            exit_atm(account)