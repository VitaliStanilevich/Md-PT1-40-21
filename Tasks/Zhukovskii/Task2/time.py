import datetime
x = input("Напишите время в формате ЧЧ:ММ или введите NOW для текущего времени: ")
if x == 'NOW':
    t = datetime.datetime.today().strftime("%H:%M")
    h = int(datetime.datetime.today().strftime("%I"))
    m = int(datetime.datetime.today().strftime("%M"))
else:
    a = x.split(':')
    h1 =int(a[0])
    m = int(a[1])
    t = x
    if h1 > 12:
        h = h1-12
    else:
        h = h1
print(t)
dh1 = { 1: "один", 2: "два", 3: "три", 4:"четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одинадцать", 12: "двенадцать", 0: "ноль"}
dh30 = {0: "первого", 1: "второго", 2: "третьего", 3: "четвертого", 4: "пятого", 5: "шестого", 6: "седьмого", 7: "восьмого", 8: "девятого", 9: "десятого", 10: "одинадцатаго", 11: "двенадцатого", 12: "первого"}
dm = {0: "ноль", 1: "одна", 2: "две", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одинадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать", 16: "шестьнадцать", 17: "семьнадцать", 18: "восемьнадцать", 19: "девятнадцать", 20: "двадцать", 30: "тридцать", 40: "сорок", 45: "пятнадцати", 46: "четырнадцати", 47: "тринадцати", 48: "двенадцати", 49: "одиннадцати", 50: "десяти", 51: "девяти", 52: "восьми", 53: "семи", 54: "шести", 55: "пяти", 56: "четырех", 57: "трех", 58: "двух", 59: "одной"}
dH = {1: "час", 2: "часа", 3: "часов"}
dM = {1: "минут", 2: "минуты", 3: "минута"}
m1 = m%10
m2 = m-m1
if m1 > 4:
    M = 2
elif m1 == 1:
    M = 3
else:
    M = 2

if m == 0:
    if h == 1:
        H = 1
    elif h > 4:
        H = 3
    elif h < 1:
        H = 3
    else:
        H = 2
    print(dh1[h], dH[H])
elif m < 20:
    print(dm[m], dM[M], dh30[h])
elif m ==30:
    print("половина", dh30[h])
elif m > 44:
    if m1 == 1:
        M = 2
    else:
        M = 1
    print("без", dm[m], dM[M], dh1[h])
else:
    if m1 == 0:
        print(dm[m2], dM[M], dh30[h])
    else:
        print(dm[m2], dm[m1], dM[M], dh30[h])
        