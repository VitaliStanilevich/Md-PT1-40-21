

#вычислить сумму на счете в конце указанного срока
percent_year = 15 # годовой процент %
amount = 20000 #начальная сумма в BYN
deposit_term = 5  #срок депозита (лет)
sum_score =  amount * (1 + percent_year / 100.0 / 12) ** (deposit_term * 12 ) # вычисляем сумму счета через 5 лет
print (round (sum_score, 2)) # выводим и округляем до рублей и копеек
