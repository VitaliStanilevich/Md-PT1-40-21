depo=int(input('Введите сумму депозита:\n'))
years=int(input('Введите количество лет:\n'))
rate=int(input('Введите размер процентной ставки (годовая):\n'))

#вариант 1
new_depo=depo*(1+rate/100/12)**(years*12)
print('Сумма к выплате:',round(new_depo, 2),'BYN')

#вариант 2
months=[31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(years):
    for j in months:
        depo+=depo*(rate/100/365*j)
print('Сумма к выплате:',round(depo, 2),'BYN')
