# Input data
INPUT = ['срок депозита (лет)', 'процент депозита (годовой)', 'сумму депозита']
RUBLI = ['рубль', 'рубля', 'рублей']
COINS = ['копейка', 'копейки', 'копеек']
period, percent, amount = [int(input(f'Введите {INPUT[i]}:\n')) for i in range(3)]


# The function of setting the correct ending of words
def vvod(tom, value):
    if tom == 'rub':
        t = RUBLI
    else:
        t = COINS

    if value % 10 == 1 and value != 11:
        return f'{value} {t[0]}'
    elif value % 10 in [2, 3, 4] and value not in [12, 13, 14]:
        return f'{value} {t[1]}'
    else:
        return f'{value} {t[2]}'
    
    
# Calculation of the final amount
mon_perc = percent / 1200
mon_peri = int(period * 12)
for _ in range(mon_peri):
    amount *= (1 + mon_perc)
x = int(amount // 1)
y = int(100*(round(amount % 1, 2)))


print(f'Сумма вашего депозита на конец срока составит {vvod("rub", x)} и {vvod("coin", y)}.')


