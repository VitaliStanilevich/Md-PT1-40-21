import datetime
ecual_hour = {0: "полночь", 1: "один час", 2: "два часа", 3: "три часа", 4: "четыре часа", 5: "пять часа", 6: "шесть чаов", 7: "семь часов",
8: "восемь часов", 9: "девать часов", 10: "десять часов", 11: "одиннадцать часов", 12: "полдень"}
half_hour = {0: "первого", 1: "второго", 2: "третьего", 3: "четвёртого", 4: "пятого", 5: "шестого", 6: "седьмого", 7: "восьмого",
8: "девятого", 9: "десятого", 10: "одиннадцотого", 11: "двенадцатого"}
half_past_hour = {0: "час", 1: "два", 3: "три", 3: "четыре", 4: "пять", 5: "шесть", 6: "семь", 7: "восемь", 8: "девять", 9: "десять", 
10: "одиннадцать", 11: "двенадцать"}
first_minutes = {1: "одна", 2: "две", 3: "три", 4: "чеыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь",
9: "девять", 10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцатьь", 15: "пятнадцать", 16: "шестнадцать",
17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать", 20: "двадцать", 21: "двадцать одна", 22: "двадцать две", 23: "двадцать три", 
24: "двадцать четыре", 25: "двадцать пять", 26: "двадцать шесть", 27: "двадцать семь", 28: "двадцать восемь", 29: "двадцать девять",
31: "тридцать одна", 32: "тридцать две", 33: "тридцать три", 34: "тридцать четыре", 35: "тридцать пять", 36: "тридцать шесть", 37: "тридцать семь",
38: "тридцать восемь", 39: "тридцать девять", 40: "сорок", 41: "сорок одна", 42: "сорок две", 43: "сорок три", 44: "сорок четыре",}
second_minutes = {45: "пятнадцати", 46: "четырнадцати", 47: "тринадцати", 48: "двенадцати", 49: "одиннадцати", 50: "десяти", 51: "девяти", 
52: "восьми", 53: "семи", 54: "шести", 55: "пяти", 56: "четырёх", 57: "трёх", 58: "двух", 59: "одной"}

today_time = input("Введите время в формате HH:MM:\n").split(":")
h1 = int(today_time[0])
m = int(today_time[1])
if h1 > 12:
    h = h1-12
else:
    h = h1

if m == 0:
    print(ecual_hour[h])
elif m == 30:
    print("Половина", half_hour[h])
elif m == 1 or m == 21 or m == 31 or m == 41:
    print(first_minutes[m], "минута", half_hour[h])
elif m in range (2, 4+1) or m in range (21, 24+1) or m in range (32, 34+1) or m in range (41, 44+1):
    print(first_minutes[m], "минуты", half_hour[h])
elif m in range (5, 20+1) or m in range (25, 29+1) or m in range (35, 40+1):
    print(first_minutes[m], "минут", half_hour[h])
elif m == 59:
    print("Без", second_minutes[m], "минуты", half_hour[h])
elif m >= 45:
    print("Без", second_minutes[m], "минут", half_hour[h])