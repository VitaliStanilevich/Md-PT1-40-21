import datetime

def two_digit_min (a):
    if a > 20 and a%10 != 0:
        min_10 = (a//10)*10
        min_1 = a%10
        return f"{minutes[min_10]} {minutes[min_1]}"
    else:
        return minutes[a]
 
def simple_hour(b):
    if b >= 12:
        return b - 12
    else:
        return b

def time(hh, mm):
    if mm == 0:
        if hh == 1:
            print(f"ровно {hours[hh][0]}")
        elif 2 <= hh <= 4:
            print(f"{hours[hh][0]} часа")
        else:
            print(f"{hours[hh][0]} часов")
    elif 0 < mm < 45:
        if mm == 30:
            print(f"половина {hours[hh+1][1]}")
        elif mm%10 == 1:
            print(f"{two_digit_min(mm)} минута {hours[hh+1][1]}")
        elif 2 <= mm%20 <= 4:
            print (f"{two_digit_min(mm)} минуты {hours[hh+1][1]}")
        else:
            print (f"{two_digit_min(mm)} минут {hours[hh+1][1]}")
    else:
        mm = 60 - mm
        n = len(minutes[mm])-1
        if mm == 1:
            print(f"без {minutes[mm][:n]}ой минуты {hours[hh+1][0]}")
        elif mm == 2:
            print(f"без {minutes[mm][:n]}ух минут {hours[hh+1][0]}")
        elif 3 <= mm <= 4:
            print(f"без {minutes[mm][:n]}ех минут {hours[hh+1][0]}")
        elif mm == 8:
            print(f"без {minutes[mm][:3]}ьми минут {hours[hh+1][0]}")
        else:
            print(f"без {minutes[mm][:n]}и минут {hours[hh+1][0]}")

hours = {
    00:['двенадцать','двеннадцатого'],
    1:['час', 'первого'],
    2:['два', 'второго'],
    3:['три', 'третьего'], 
    4:['четыре','четвертого'],
    5:['пять','пятого'],
    6:['шесть','шестого'],
    7:['семь','седьмого'],
    8:['восемь','восьмого'], 
    9:['девять','девятого'],
    10:['десять','десятого'],
    11:['одиннадцать','одиннадцатого'],
    12:['двенадцать','двеннадцатого']
}

minutes = {
    1:'одна',
    2:'две',
    3:'три',
    4:'четыре',
    5:'пять',
    6:'шесть',
    7:'семь',
    8:'восемь',
    9:'девять',
    10:'десять',
    11:'одиннадцать',
    12:'двенадцать',
    13:'тринадцать',
    14:'четырнадцать',
    15:'пятнадцать',
    16:'шестнадцать',
    17:'семнадцать',
    18:'восемнадцать',
    19:'девятнадцать',
    20:'двадцать',
    30:'тридцать',
    40:'сорок'
}

t = str(datetime.datetime.now().time())
hm = t.split(':')
h, m = int(hm[0]), int(hm[1])
h = simple_hour(h)
time(h, m)

hm = input('Enter your time(hh:mm)\n').split(':')
h, m = int(hm[0]), int(hm[1])
h = simple_hour(h)
if 0 <= h <= 12 and 0 <= m < 60:
    time(h, m)
else:
    print('Вы ввели неверный формат')












