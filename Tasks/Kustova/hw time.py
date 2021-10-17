answ = input("Программа преобразует значение времени в текстовый формат. Хотите преобразовать текущее время(введите 1) или другое(введите 2)?\n")
while answ != "1" or answ != "2":
    if answ == "1":
        import datetime
        hourminute = datetime.datetime.now().time()
        time = hourminute.strftime('%H:%M')
        hourminute = time.split(":")
        hour, minute = hourminute[0], hourminute[1]
        break
    elif answ == "2":
        time = input("введите время в формате 'hh:mm' :\n")
        hourminute = time.split(":")
        hour, minute = hourminute[0], hourminute[1]
        if int(hour) < 24 and int(minute) < 60:
            break
        else:
            answ = input("Неверный формат данных. Начнем сначала.\nХотите преобразовать текущее время(введите 1) или другое(введите 2)?\n")
    else:
        answ = input('Вы ответили что-то другое, введите 1 или 2! ')

def zero (h_m):        #убираем 0 перед второй цифрой, если она есть (ибо unexpected token)
	if h_m[0] == '0':
		h_m=h_m[1]
		return h_m
	else:
		return h_m

def hour12 (x):         #делаем из 24:00 формата 12:00
	if x > 12:
		x = x - 12
	return x

def numb (minut):        #делим минуты на двe цифры, если она больше 19
    t = minut//10
    if t != 0 and t != 1:
        h = minut//10
        m = minut%10
        return [h, m]
    else:
        return [minut]

def minuta (m):           # правильное окончание в выводе
    if m[-1] == 1:
        an = 'минута';
    elif 2 <= m[-1] <= 4:
        an = 'минуты'
    else:
        an = 'минут'
    return an

def without (time, text):  # для вывода "без такого-то"
    if time == 52:
        x  = text[:-3]+'ьми'
        return x
    elif time == 56:
        x  = text+'х'
        return x
    elif time == 57:
        x  = text[:-1]+'ех'
        return x
    elif time == 58:
        x  = text[:-1]+'ух'
        return x
    elif time == 59:
        x  ='одной'
        return x
    else:
        x  = text[:-1]+'и'
        return x

hour = int(zero(hour))
hour = hour12(hour)
minute2 = int(zero(minute))
minute = (numb(minute2))

dict = {0:"первого", 1:"второго", 2:"третьего", 3:"четвертого", 4:"пятого", 5:"шестого", 6:"седьмого", 7:"восьмого", 8:"девятого", 9:"десятого", 10:"одиннадцатого", 11:"двенадцатого", 12:"первого"}
dict_hourminute = { 1:"час", 2:"два", 3:"три", 4:"четыре", 5:"пять", 6:"шесть", 7:"семь", 8:"восемь", 9:"девять", 10:"десять", 11:"одинадцать", 12:"двенадцать", 13:"тринадцать", 14:"четырнадцать", 15:"пятнадцать", 16:"шестнадцать", 17:"семнадцать", 18:"восемнадцать", 19:"девятнадцать"}
dict_minute1_2 = {1:"одна", 2:"две"}
dict_min_x0={2:"двадцать", 3:"тридцать", 4:"сорок"}

if minute[0] == 0:
    if hour == 0:
        print("ровно полночь")
    else:
        print('ровно', dict_hourminute[hour] )
elif minute2 == 30:
    print("половина", dict[hour])
elif minute2 < 45:
    if len(minute) == 1:
        print(f'{dict_minute1_2[minute[0]] if minute[0] == 1 or minute[0] == 2 else dict_hourminute[minute[0]]} {minuta(minute)} {dict[hour]}')
    elif minute[1] == 0:
            print(f'{dict_min_x0[minute[0]]} минут {dict[hour]}')
    else:
        print(f'{dict_min_x0[minute[0]]} {dict_minute1_2[minute[1]] if minute[1] == 1 or minute[1] == 2 else dict_hourminute[minute[1]]} {minuta(minute)} {dict[hour]}')
elif 45 <= minute2 <= 59:
    print('без', without(minute2, dict_hourminute[abs(minute2-60)]), 'минуты' if minute2 == 59 else 'минут' ,dict_hourminute[hour+1])

