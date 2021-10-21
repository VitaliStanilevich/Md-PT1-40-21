#Депозит:
#начальная сумма - 20000 BYN
#срок - 5 лет
#процент (годовой) - 15%
#ежемесячная капитализация
start_sum = 20000
period_years = 5
percent = 0.15

sum_money = start_sum*((1+percent/12)**(period_years*12)) #нашёл формулу на сайтах по финансам
print(round(sum_money, 2))

i = 0
sum = start_sum
month = int(period_years * 12)
while i < month :
   i = i + 1
   sum = sum + sum * (percent/12)
print(round(sum, 2))

