def bank (x, month):

    P=int(15)

    for i in range (month):

        x = x + ((x/100*P)/12)

    return (x)

result = round( bank (float(input("Сумма вклада: ")),
 int(input("Число месяцв: "))))

print(result) 