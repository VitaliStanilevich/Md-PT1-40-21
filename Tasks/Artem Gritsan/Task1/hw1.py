from decimal import Decimal as dl
dep = int(input('Введите сумму депозита:\n'))
date = dl(input('Введите срок(в месяцах):\n'))
p = dl(input('Введите процент(годовой):\n'))
n = dl(1 / 11)
g = ((dep * (1 + (p / 100))) / dep)**n 
S = dep * pow(g, date - 1)
print(round(S, 0))
