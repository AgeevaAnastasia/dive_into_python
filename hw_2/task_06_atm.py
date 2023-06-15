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
MULTIPLE_SUM = 50
MINIMUM_COMMISSION = 30 #total
COMMISSION = 0.015 #percent
MAXIMUM_COMMISSION = 600 #total
LUXURY_COMMISSION = 0.1 #percent
LUXURY_SUM = 5_000_000
COUNT_FOR_PREMIUM = 3
PREMIUM_FOR_OPERATIONS = 0.03 #percent

count_transactions = 0
account = START_SUM


def deposit_money(acc, count):
    amount = int(input(f'Введите сумму, кратную {MULTIPLE_SUM}, которую хотите внести: '))
    if amount % {MULTIPLE_SUM} == 0 and amount > 0:
        acc += amount
        count += 1
    else:
        print(f'Некорректный ввод. Сумма должна быть кратна {MULTIPLE_SUM} и быть больше 0.')
    if count % COUNT_FOR_PREMIUM == 0:
        acc += acc * PREMIUM_FOR_OPERATIONS
    return acc


def withdraw_money(acc, count):
    amount = int(input(f'Введите сумму, кратную {MULTIPLE_SUM}, которую хотите снять: '))
    if amount > acc:
        print('Нельзя снять больше, чем есть на счете')
    else:
        if amount % MULTIPLE_SUM == 0 and amount > 0:
            acc -= amount
            if amount * COMMISSION < MINIMUM_COMMISSION:
                acc -= MINIMUM_COMMISSION
                print(f'комиссия за операцию {MINIMUM_COMMISSION}')
            elif MINIMUM_COMMISSION <= amount * COMMISSION <= MAXIMUM_COMMISSION:
                acc -= acc * COMMISSION
                print(f'комиссия за операцию {COMMISSION * 100}%: {amount * COMMISSION}')
            else:
                acc -= MAXIMUM_COMMISSION
                print(f'комиссия за операцию {MAXIMUM_COMMISSION}')
            count += 1
        else:
            print(f'Некорректный ввод. Сумма должна быть кратна {MULTIPLE_SUM} и быть больше 0.')
    if count % COUNT_FOR_PREMIUM == 0:
        acc += acc * PREMIUM_FOR_OPERATIONS
    return acc


while True:
    print('''
    Выберите действие:
    1 - положить деньги
    2 - снять деньги
    3 - выйти''')
    choice = input('>>> ')
    if account > LUXURY_SUM:
        print(f'налог на роскошь - {LUXURY_COMMISSION * 100}% от суммы счета: {account * LUXURY_COMMISSION}')
        account = account - account * LUXURY_COMMISSION
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
