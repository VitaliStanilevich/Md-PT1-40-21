def bank (a, month):

    Pers=int(15)

    for i in range (month):

        a = a + ((a/100*Pers)/12)

    return (a)

result = round( bank (float(input("Введите сумму вклада: ")), int(input("Введите количество месяцев: "))))

print(result)