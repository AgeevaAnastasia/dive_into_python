"""
Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список.
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
global list_of_operations
list_of_operations = []


def deposit_money(acc, count):
    amount = int(input(f'Введите сумму, кратную {MULTIPLE_SUM}, которую хотите внести: '))
    if amount % MULTIPLE_SUM == 0 and amount > 0:
        string = 'Внесение средств: ' + str(acc) + ' + ' + str(amount) + \
                 ' = ' + str(acc + amount)
        list_of_operations.append(string)
        acc += amount
        count += 1
    else:
        print(f'Некорректный ввод. Сумма должна быть кратна {MULTIPLE_SUM} и быть больше 0.')
    if count % COUNT_FOR_PREMIUM == 0:
        string = 'Премия за каждую 3-ю операцию: ' + str(acc) + ' + ' + str(acc * PREMIUM_FOR_OPERATIONS) + \
                 ' = ' + str(acc + acc * PREMIUM_FOR_OPERATIONS)
        list_of_operations.append(string)
        acc += acc * PREMIUM_FOR_OPERATIONS
    return acc


def withdraw_money(acc, count):
    amount = int(input(f'Введите сумму, кратную {MULTIPLE_SUM}, которую хотите снять: '))
    if amount > acc:
        print('Нельзя снять больше, чем есть на счете')
    else:
        if amount % MULTIPLE_SUM == 0 and amount > 0:
            string = 'Снятие средств: ' + str(acc) + ' - ' + str(amount) + \
                     ' = ' + str(acc - amount)
            list_of_operations.append(string)
            acc -= amount
            if amount * COMMISSION < MINIMUM_COMMISSION:
                string = 'Минимальная комиссия за снятие: ' + str(acc) + ' - ' + str(MINIMUM_COMMISSION) + \
                         ' = ' + str(acc - MINIMUM_COMMISSION)
                list_of_operations.append(string)
                acc -= MINIMUM_COMMISSION
                print(f'комиссия за операцию {MINIMUM_COMMISSION}')
            elif MINIMUM_COMMISSION <= amount * COMMISSION <= MAXIMUM_COMMISSION:
                string = 'Комиссия за снятие: ' + str(acc) + ' - ' + str(acc * COMMISSION) + \
                         ' = ' + str(acc - acc * COMMISSION)
                list_of_operations.append(string)
                acc -= acc * COMMISSION
                print(f'комиссия за операцию {COMMISSION * 100}%: {amount * COMMISSION}')
            else:
                string = 'Максимальная комиссия за снятие: ' + str(acc) + ' - ' + str(MAXIMUM_COMMISSION) + \
                         ' = ' + str(acc - MAXIMUM_COMMISSION)
                list_of_operations.append(string)
                acc -= MAXIMUM_COMMISSION
                print(f'комиссия за операцию {MAXIMUM_COMMISSION}')
            count += 1
        else:
            print(f'Некорректный ввод. Сумма должна быть кратна {MULTIPLE_SUM} и быть больше 0.')
    if count % COUNT_FOR_PREMIUM == 0:
        string = 'Премия за каждую 3-ю операцию: ' + str(acc) + ' + ' + str(acc * PREMIUM_FOR_OPERATIONS) + \
                 ' = ' + str(acc + acc * PREMIUM_FOR_OPERATIONS)
        list_of_operations.append(string)
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
        print(f'налог на роскошь - {LUXURY_COMMISSION * 100}% от суммы счета, превышающий 5000000: '
              f'{(account - 5000000) * LUXURY_COMMISSION}')
        string = 'Налог на роскошь 10% от суммы свыше 5000000: ' + str(account) + \
                 ' - ' + str((account - 5000000) * LUXURY_COMMISSION) + \
                 ' = ' + str(account - (account - 5000000) * LUXURY_COMMISSION)
        list_of_operations.append(string)
        account = account - (account - 5000000) * LUXURY_COMMISSION
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

for item in list_of_operations:
    print(item)
