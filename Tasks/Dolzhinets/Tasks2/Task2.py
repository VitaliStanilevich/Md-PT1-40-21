#Реализовать:
#1.текстовый вывод текущего времени
#2.текстовый вывод времени, введённого с консоли (hh:mm).
#Для получения текущего времени использовать модуль datetime.
#min < 30: столько-то минут следующего часа
#min == 30: половина такого-то
#min > 30 and min < 45 столько-то минут следующего часа
#min >= 45 без min такого-то

import datetime #импортируем модуль
time_ = input("Введите время ч:м или введите 'Y' для текущего времени: ")
if time_ == 'Y':
    time_today = datetime.datetime.today().strftime("%H:%M")  #присваиваем объекту сегоднешнюю дату и время и возвращаем строку с количеством часов в 24 часовом формате и количество минут  
    hour = int(datetime.datetime.today().strftime("%I")) #переводим в целое число часы
    minute = int(datetime.datetime.today().strftime("%M")) #переводим в целое число минуты
else:
    date = time_.split(':') #режем строку на список по ":"
    hour_1 = int(date[0]) #присваиваем первый элемент списка объекту (час)
    minute = int(date[1]) #присваиваем второй элемент списка объекту (минуты)
    time_today = time_
    if hour_1 > 12: #условие если часов больше 12
        hour = hour_1 - 12
    else:
        hour = hour_1
hours_1= {0:'полночь', 1:'час', 2:'два', 3:'три', 4:'четыре', 5:'пять', 6:'шесть', 7:'семь', 8:'восемь', 9:'девять',
10:'десять', 11:'одиннадцать', 12:'двенадцать'}
min = {1:'одна минута', 2:'две минуты', 3:'три минуты', 4:'четыре минуты', 5:'пять минут',
6:'шесть минут', 7:'семь минут', 8:'восемь минут', 9:'девять минут', 10:'десять минут', 
11:'одиннадцать минут', 12:'двенадцать минут', 13:'тринадцать минут', 14:'четырнадцать минут',
15:'пятнадцать минут', 16:'шестнадцать минут', 17:'семьнадцать минут', 18:'восемнадцать минут',
19:'девятнадцать минут', 20:'двадцать минут', 21:'двадцать одна минута', 22:'двадцать две', 
23:'двадцать три минуты', 24:'двадцать четыре минуты', 25:'двадцать пять минут', 26:'двадцать шесть минут',
27:'двадцать семь минут', 28:'двадцать восемь минут', 29:'двадцать девять минут', 30:'половина', 
31:'тридцать одна минута', 32:'тридцать две минуты', 33:'тридцать три минуты', 
34:'тридцать четыре минуты', 35:'тридцать пять минут', 36:'тридцать шесть минут', 
37:'тридцать семь минут', 38:'тридцать восемь минут', 39:'тридцать девять минут', 
40:'сорок минут', 41:'сорок одна минута', 42:'сорок две минуты', 43:'сорок три минуты',
44:'сорок четыре минуты', 45:'без пятнадцати минут', 46:'без четырнадцати минут', 47:'без тринадцати минут',
48:'без двенадцати минут', 49:'без одиннадцати минут', 50:'без десяти минут', 51:'без девяти минут', 
52:'без восьми минут', 53:'без семи минут', 54:'без шести минут', 55:'без пяти минут', 
56:'без четырех минут', 57:'без трех минут', 58:'без двух минут', 59:'без одной минуты'} 
hours = {0:'первого', 1:'второго', 2:'третьего', 3:'четвертого', 4:'пятого', 5:'шестого', 
6:'седьмого', 7:'восьмого', 8:'девятого', 9:'десятого', 10:'одиннадцатого', 11:'двенадцатого', 12:'первого'}

#условия для минут и часов в различных диапазонах
if minute == 0 and 1 < hour < 5: 
    print(hours_1[hour], 'часа')
elif minute == 0 and 4 < hour < 13: 
    print(hours_1[hour], 'часов')
elif minute == 0 and hour == 1: 
    print(hours_1[hour])          
elif minute >= 45 and hour != 12:      
    print(min[minute], hours_1[hour + 1])
elif minute >= 45 and hour == 12:      
    print(min[minute], 'час')    
else:
    print(min[minute], hours[hour])