from decimal import Decimal

x0=input("Введите начальную сумму депозита BYN: ")   #начальная сумма
x0=int(x0)
dep=input("Введите процентную ставку %: ")       #процент
dep=int(dep)
year=input("Введите срок депозита лет: ")        #срок депозита
year=int(year)
mounth=12                                        #число месяцев в году
cap=0                                            #начальная капитализация
n=0                                              #номер начального месяца

while n<=year*mounth:                            #ограничитель итераций

    Sum=x0+Decimal(cap)
    cap+=((Sum*dep/100)/mounth)                  #размер капитализаци  
    n+=1                                         #счетчик итераций
    
print("Сумма на счету в конце срока с учетом ежемесячной капитализации" , round(Sum,2) , end="")
  
    






