# Реализовать:
# 1.текстовый вывод текущего времени
# 2.текстовый вывод времени, введённого с консоли (hh:mm).
#
# Для получения текущего времени использовать модуль datetime.
#
# min < 30: столько-то минут следующего часа
# min == 30: половина такого-то
# min > 30 and min < 45 столько-то минут следующего часа
# min >= 45 без min такого-то
#
#
# 21:16
# шестнадцать минут десятого
#
# test
import datetime
hours_type_1 = {
    1: "час", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять",
    11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать",
    17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать", 20: "двадцать", 21: "двадцать один", 22: "двадцать два",
    23: "двадцать три", 24: "двадцать четыре"
}
hours_type_2 = {
    1: "первого", 2: "второго", 3: "третьего", 4: "четвёртого", 5: "пятого", 6: "шестого", 7: "седьмого", 8: "восьмого",
    9: "девятого", 10: "десятого", 11: "одиннадцатого", 12: "двенадцатого", 13: "первого", 14: "второго",
    15: "третьего", 16: "четвёртого", 17: "пятого", 18: "шестого", 19: "седьмого", 20: "восьмого", 21: "девятого",
    22: "десятого", 23: "одиннадцатого", 24: "двенадцатого"
}
minutes_type_1 = {
    1: "одна", 2: "две", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь",
    9: "девять", 10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать",
    15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать", 20: "двадцать",
    21: "двадцать одна", 22: "двадцать две", 23: "двадцать три", 24: "двадцать четыре", 25: "двадцать пять",
    26: "двадцать шесть", 27: "двадцать семь", 28: "двадцать восемь	",
    29: "двадцать девять", 30: "половина"
}
minutes_type_2 = {
    31: "двадцати девяти", 32: "двадцати восьми", 33: "двадцати семи", 34: "двадцати шести", 35: "двадцати пяти",
    36: "двадцати четырёх", 37: "двадцати трёх", 38: "двадцати двух", 39: "двадцати одной", 40: "двадцати",
    41: "девятнадцати", 42: "восемнадцати", 43: "семнадцати", 44: "шестнадцати", 45: "пятнадцати", 46: "четырнадцати",
    47: "тринадцати", 48: "двенадцати", 49: "одиннадцати", 50: "десяти", 51: "девяти", 52: "восьми", 53: "семи",
    54: "шести", 55: "пяти", 56: "четырёх", 57: "трёх", 58: "двух", 59: "одной"
}
current_hours = int(datetime.datetime.now().strftime("%H"))
current_minutes = int(datetime.datetime.now().strftime("%M"))
if current_hours % 12 != 0:
    current_hours = current_hours - 11
else:
    current_hours = current_hours + 1

if current_minutes < 60 or current_hours < 24:
    if current_minutes == 00:
        proposal_minute_form = "ровно"
    elif 30 < current_minutes < 60:
        proposal_minute_form = "минут"
        minutes = minutes_type_2[current_minutes]
        hours = hours_type_1[current_hours]
        print("Без", minutes, proposal_minute_form, hours)
    elif current_minutes % 10 == 1 and current_minutes != 11:
        proposal_minute_form = "минута"
        minutes = minutes_type_1[current_minutes]
        hours = hours_type_2[current_hours]
        print(minutes, proposal_minute_form, hours)
    elif 1 < current_minutes % 10 < 5 and 10 < current_minutes < 20:
        proposal_minute_form = "минуты"
        minutes = minutes_type_1[current_minutes]
        hours = hours_type_2[current_hours]
        print(minutes, proposal_minute_form, hours)
    else:
        proposal_minute_form = "минут"
        minutes = minutes_type_1[current_minutes]
        hours = hours_type_2[current_hours]
        print(minutes, proposal_minute_form, hours)
else:
    print("Ошибка")


user_time = input("Введите текущее время в формате 'HH':'MM': ")
user_current_hours = int(user_time.split(":")[0])
user_current_minutes = int(user_time.split(":")[1])

if (user_current_hours // 12) != 0:
    user_current_hours = user_current_hours - 11
else:
    user_current_hours = user_current_hours + 1

if user_current_minutes < 60 or user_current_hours < 24:
    if user_current_minutes == 00:
        proposal_minute_form = "ровно"
    elif 30 < user_current_minutes < 60:
        proposal_minute_form = "минут"
        minutes = minutes_type_2[user_current_minutes]
        hours = hours_type_1[user_current_hours]
        print("Без", minutes, proposal_minute_form, hours)
    elif user_current_minutes % 10 == 1 and user_current_minutes != 11:
        proposal_minute_form = "минута"
        minutes = minutes_type_1[user_current_minutes]
        hours = hours_type_2[user_current_hours]
        print(minutes, proposal_minute_form, hours)
    elif 1 < user_current_minutes % 10 < 5 and 10 < current_minutes < 20:
        proposal_minute_form = "минуты"
        minutes = minutes_type_1[user_current_minutes]
        hours = hours_type_2[user_current_hours]
        print(minutes, proposal_minute_form, hours)
    else:
        proposal_minute_form = "минут"
        minutes = minutes_type_1[user_current_minutes]
        hours = hours_type_2[user_current_hours]
        print(minutes, proposal_minute_form, hours)
else:
    print("Ошибка")