import datetime

def two_digit_min (a):
    if a > 20 and a%10 != 0:
        min_10 = (a//10)*10
        min_1 = a%10
        return f"{minutes[min_10][0]} {minutes[min_1][0]}"
    else:
        return minutes[a][0]
 
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
        if mm == 1:
            print(f"без {minutes[mm][1]} минуты {hours[hh+1][0]}")
        else:
            print(f"без {minutes[mm][1]} минут {hours[hh+1][0]}")

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
12:['двенадцать','двенадцатого'], 
}

minutes = {
1:['одна','одной'],
2:['две','двух'],
3:['три','трех'],
4:['четыре','четырех'],
5:['пять', 'пяти'],
6:['шесть','шести'],
7:['семь','семи'],
8:['восемь','восьми'],
9:['девять','девяти'],
10:['десять','десяти'],
11:['одиннадцать','одиннадцати'],
12:['двенадцать','двенадцати'],
13:['тринадцать','тринадцати'],
14:['четырнадцать','четырнадцати'],
15:['пятнадцать','пятнадцати'],
16:['шестнадцать'],
17:['семнадцать'],
18:['восемнадцать'],
19:['девятнадцать'],
20:['двадцать'],
30:['тридцать'],
40:['сорок']
}

t = str(datetime.datetime.now().time())
hm = t.split(':')
h, m = int(hm[0]), int(hm[1])
h = simple_hour(h)

time(h, m)

hm = input('Enter your time(hh:mm)\n').split(':')
h, m = int(hm[0]), int(hm[1])
h = simple_hour(h)

time(h, m)










