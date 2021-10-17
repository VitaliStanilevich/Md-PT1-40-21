# p = 20000
# t = 5
# r = 15/100
# n = 12

# x = p * (1 + r / n)**(n*t)

# print (round(x, 2),'BYN')


p = int(input ("Сумма депозита "))
t = int(input ("Срок депозита "))
r = int(input ("Процент(годовой) "))
N = str(input("С ежемесячной капитализацией?(да или нет) "))
if N == "да":

    n = 12
    r = r / 100
    f = n * t
    x =(1 + r / n)**f * p
    print (round(x, 2),'BYN')
else:
    N == "Нет"
    n = 12
    r = r / 100
    f = n * t
    x = (p * r *  f) / n
    x = x + p
    print (round(x, 2),'BYN')

