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
account = START_SUM


def deposit_money(acc, count):
    amount = int(input('Введите сумму, кратную 50, которую хотите внести: '))
    if amount % 50 == 0 and amount > 0:
        acc += amount
        if amount * 0.15 < 30:
            acc -= 30
            print('комиссия за операцию 30')
        elif 30 <= amount * 0.15 <= 600:
            acc -= acc * 0.15
            print(f'комиссия за операцию 1.5%: {amount * 0.15}')
        else:
            acc -= 600
            print('комиссия за операцию 600')
        count += 1
    else:
        print('Некорректный ввод. Сумма должна быть кратна 50 и быть больше 0.')
    if count % 3 == 0:
        acc += acc * 0.03
    return acc


def withdraw_money(acc, count):
    amount = int(input('Введите сумму, кратную 50, которую хотите снять: '))
    if amount > acc:
        print('Нельзя снять больше, чем есть на счете')
    else:
        if amount % 50 == 0 and amount > 0:
            acc -= amount
            if amount * 0.15 < 30:
                acc -= 30
                print('комиссия за операцию 30')
            elif 30 <= amount * 0.15 <= 600:
                acc -= acc * 0.15
                print(f'комиссия за операцию 1.5%: {amount * 0.15}')
            else:
                acc -= 600
                print('комиссия за операцию 600')
            count += 1
        else:
            print('Некорректный ввод. Сумма должна быть кратна 50 и быть больше 0.')
    if count % 3 == 0:
        acc += acc * 0.03
    return acc


while True:
    print('''
    Выберите действие:
    1 - положить деньги
    2 - снять деньги
    3 - выйти''')
    choice = input('>>> ')
    if account > 5_000_000:
        print(f'налог на роскошь - 10% от суммы счета: {account * 0.1}')
        account = account - account * 0.1
    match choice:
        case '1':
            account = deposit_money(account, count_transactions)
            print(f'У вас на счете: {account}')
        case '2':
            account = withdraw_money(account, count_transactions)
            print(f'У вас на счете: {account}')
        case '3':
            print(f'У вас на счете: {account}')
            break
