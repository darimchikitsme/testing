money = int(input('Введите сумму вклада: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a = per_cent.get('ТКБ')
BankA = money*a/100
b = per_cent.get('СКБ')
BankB = money*b/100
c = per_cent.get('ВТБ')
BankC = money*c/100
d = per_cent.get('СБЕР')
BankD = money*d/100
deposit = [BankA, BankB, BankC, BankD]
print(list(map(float,deposit)))
print('Максимальная сумма, которую вы можете заработать - ', max(deposit))
