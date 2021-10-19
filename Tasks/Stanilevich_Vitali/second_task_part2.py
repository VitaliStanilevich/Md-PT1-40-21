import datetime

full_hour = {0: "полноч", 1: "один час", 2: "два часа", 3: "три часа", 4: "четыре часа", 5: "пять часов", 6: "шесть часов", 7: "семь часов",
            8: "восемь часов", 9:"девять часов", 10: "десять часов", 11:"одинадцать часов", 12:"двенадцать часов",}
next_hour = {0: "первого", 1: "второго", 2: "третьего", 3: "четвертого", 4: "пятого", 5: "шестого", 6: "седьмого", 7: "восьмого", 8: "девятого", 9:"десятого", 10: "одинадцатого", 11:"двенадцатого", 12: "первого"}
end_of_hour = {0:"час", 1:"два", 2:"три", 3:"четыре", 4:"пять", 5:"шесть", 6:"семь", 7:"восемь", 8:"девять", 9:"десять", 10:"одинадцать", 11:"двенадцать", 12:"час"}

minutes = {1: "одна минута", 2: "две минуты", 3: "три минуты", 4: "четыре минуты", 5: "пять минут", 6: "шесть минут", 7: "семь минут", 8: "восемь минут",
         9: "девять минут", 10:"десять минут", 11: "одинадцать минут", 12:"двенадцать минут", 13: "тренадцать минут", 14: "четырнадцать минут", 
         15: "пятнадцать минут", 16: "шестнадцать минут", 17: "семнадцать минут", 18: "восемнадцать минут", 19: "девятнадцать минут",
         20: "двадцать ", 30: "тридцать" , 40:"сорок "}

wt_minutes = {45:"пятнадцати", 46:"четырнадцати", 47:"тренадцати", 48:"двенадцати", 49:"одинадцати", 50:"десяти", 51:"девяти", 52:"восьми", 53:"семи", 54:"шести", 55:"пяти",
        56:"четырёх", 57:"трёх", 58:"двух",59:"одной"}        

a = input("Введите время в формате HH:MM : ").split(":")
h = int(a[0])
m = int(a[1])

if m == 0 and h <= 12:
    print(full_hour[h])
elif m == 0 and h > 12:
    h = h - 12
    print(full_hour[h])

elif m == 20 and h <= 12 :
    print (minutes[m] + "минут" , next_hour[h]) 

elif m == 20 and h > 12 :
    h = h - 12
    print (minutes[m] + "минут" , next_hour[h])  

elif m == 40 and h <= 12 :
    print (minutes[m] + "минут" , next_hour[h]) 

elif m == 40 and h > 12 :
    h = h - 12
    print (minutes[m] + "минут" , next_hour[h]) 

elif m == 30 and h <= 12:
    print ("половина" ,next_hour[h])
elif m == 30 and h > 12:
    h = h - 12
    print ("половина" ,next_hour[h])



elif m > 20 and m < 45 and h <= 12 and m != 30 and m != 40:
     m = str(m)
     m1 = int(m[0])
     m2 = int(m[1])
     m1 = m1 * 10
     print (minutes[m1], minutes[m2], next_hour[h])

elif m > 20 and m < 45 and h > 12 and m != 30 and m != 40:
     m = str(m)
     m1 = int(m[0])
     m2 = int(m[1])
     m1 = m1 * 10
     h = h - 12
     print (minutes[m1], minutes[m2], next_hour[h])


elif m >= 45 and h <= 12:
    print ("без", wt_minutes[m], end_of_hour[h])

elif m >= 45 and h > 12:
    h = h - 12
    print ("без", wt_minutes[m], end_of_hour[h])

elif m <= 19 and h <= 12:
    print (minutes[m], next_hour[h])
elif m <= 19 and h > 12:
    h = h - 12
    print (minutes[m], next_hour[h])



today = datetime.datetime.today()
time = ( today.strftime("%H:%M") )
print ("Сейчас", time,)
time =time.split(":")

h = int(time[0])
m = int(time[1])

if m == 0 and h <= 12:
    print(full_hour[h])
elif m == 0 and h > 12:
    h = h - 12
    print(full_hour[h])

elif m == 20 and h <= 12 :
    print (minutes[m] + "минут" , next_hour[h]) 

elif m == 20 and h > 12 :
    h = h - 12
    print (minutes[m] + "минут" , next_hour[h])  

elif m == 40 and h <= 12 :
    print (minutes[m] + "минут" , next_hour[h]) 

elif m == 40 and h > 12 :
    h = h - 12
    print (minutes[m] + "минут" , next_hour[h]) 

elif m == 30 and h <= 12:
    print ("половина" ,next_hour[h])
elif m == 30 and h > 12:
    h = h - 12
    print ("половина" ,next_hour[h])



elif m > 20 and m < 45 and h <= 12 and m != 30 and m != 40:
     m = str(m)
     m1 = int(m[0])
     m2 = int(m[1])
     m1 = m1 * 10
     print (minutes[m1], minutes[m2], next_hour[h])

elif m > 20 and m < 45 and h > 12 and m != 30 and m != 40:
     m = str(m)
     m1 = int(m[0])
     m2 = int(m[1])
     m1 = m1 * 10
     h = h - 12
     print (minutes[m1], minutes[m2], next_hour[h])


elif m >= 45 and h <= 12:
    print ("без", wt_minutes[m], end_of_hour[h])

elif m >= 45 and h > 12:
    h = h - 12
    print ("без", wt_minutes[m], end_of_hour[h])

elif m <= 19 and h <= 12:
    print (minutes[m], next_hour[h])
elif m <= 19 and h > 12:
    h = h - 12
    print (minutes[m], next_hour[h])