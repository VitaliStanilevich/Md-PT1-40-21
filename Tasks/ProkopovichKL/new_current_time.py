# Это доработанное решение с использованием f-строки и немного меньшими словарями.
# Циклы/функции не использовал, т.к пока плохо ими владею. 

hh = {0:'первого', 00:'первого', 1:'второго', 2:'третьего', 3:'четвёртого', 4:'пятого', 
5:'шестого', 6:'седьмого', 7:'восьмого', 8:'девятого', 9:'десятого', 
10:'одиннадцатого', 11:'двенадцатого'}

mm = {0:'ноль', 00:'ноль', 1:'одна', 2:'две', 3:'три', 4:'четыре', 5:'пять', 6:'шесть', 7:'семь', 
8:'восемь', 9:'девять', 10:'десять', 11:'одиннадцать', 12:'двенадцать', 13:'тринадцать',
14:'четырнадцать', 15:'пятнадцать', 16:'шестнадцать', 17:'семнадцать', 18:'восемнадцать',
19:'девятнадцать', 20:'двадцать', 30:'тридцать', 40:'сорок'}

mmm = {59:'одной', 58:'двух', 57:'трёх', 56:'четырёх', 55:'пяти', 
54:'шести', 53:'семи', 52:'восьми', 51:'девяти', 50:'десяти',
49:'одиннадцати', 48:'двенадцати', 47:'тринадцати', 46:'четырнадцати', 45:'пятнадцати'}

mc = {1:'минут', 2:'минута', 3:'минуты'}

# Далее описано решение 1-го условия задачи - текстовый вывод текущего времени.

import datetime
current_date_time = datetime.datetime.now() # Получаем дату и время.
current_time = current_date_time.strftime('%H:%M') # Вычленяем время в нужном виде.
print('Текущее время -', current_time)
h = int(current_date_time.strftime('%H'))
m = int(current_date_time.strftime('%M'))
a = 'без'   # Добавляем пару переменных для f-строки
b = 'половина'
t = 'Текстовый формат времени -'

if h >= 12:
    h -= 12
else:
    h = h
if m == 0:
    text_time = f'{t} {mm[m]} {mc[1]} {hh[h]}'
    print(text_time)
elif m == 1:
    text_time = f'{t} {mm[m]} {mc[2]} {hh[h]}'
    print(text_time)
elif m >= 2 and m < 5:
    text_time = f'{t} {mm[m]} {mc[3]} {hh[h]}'
    print(text_time)
elif m >= 5 and m < 21:
    text_time = f'{t} {mm[m]} {mc[1]} {hh[h]}'
    print(text_time)
elif m == 21:
    text_time = f'{t} {mm[m-1]} {mm[1]} {mc[2]} {hh[h]}'
    print(text_time)
elif m >= 22 and m < 25:
    text_time = f'{t} {mm[m-(m-20)]} {mm[m-20]} {mc[3]} {hh[h]}'
    print(text_time)
elif m >= 25 and m < 30:
    text_time = f'{t} {mm[m-(m-20)]} {mm[m-20]} {mc[1]} {hh[h]}'
    print(text_time)
elif m == 30:
    text_time = f'{t} {b} {hh[h]}'
    print(text_time)
elif m == 31:
    text_time = f'{t} {mm[m-1]} {mm[1]} {mc[2]} {hh[h]}'
    print(text_time)
elif m >= 32 and m < 35:
    text_time = f'{t} {mm[m-(m-30)]} {mm[m-30]} {mc[3]} {hh[h]}'
    print(text_time)
elif m >= 35 and m < 40:
    text_time = f'{t} {mm[m-(m-30)]} {mm[m-30]} {mc[1]} {hh[h]}'
    print(text_time)
elif m == 40:
    text_time = f'{t} {mm[m]} {mc[1]} {hh[h]}'
    print(text_time)
elif m == 41:
    text_time = f'{t} {mm[m-1]} {mm[1]} {mc[2]} {hh[h]}'
    print(text_time)
elif m >= 42 and m < 45:
    text_time = f'{t} {mm[m-(m-40)]} {mm[m-40]} {mc[3]} {hh[h]}'
    print(text_time)
elif m >= 45 and m < 59:
    text_time = f'{t} {a} {mmm[m]} {mc[1]} {hh[h]}'
    print(text_time)
elif m == 59:
    text_time = f'{t} {a} {mmm[m]} {mc[3]} {hh[h]}'
    print(text_time)
else:
    print('В земных сутках такой комбинации времени не существует!')

# С 86 строки описано решение 2-го условия задачи - текстовый вывод 
# времени, введённого с консоли (hh:mm).

manual_time = input('\nВведите время числами строго в формате(hh:mm): ').split(':')
h = int(manual_time[0])
m = int(manual_time[1])
a = 'без'
b = 'половина'
t = 'Текстовый формат времени -'

if h < 0 or h > 23:
    print('Такого отображения часа не существует!')
    print('Повторите ввод!')
else:
    h = h
if m < 0 or m > 59:
    print('Такого отображения минут не существует!')
    print('Повторите ввод!')
else:
    m = m
if h >= 12:
    h -= 12
else:
    h = h
if m == 0:
    text_time = f'{t} {mm[m]} {mc[1]} {hh[h]}'
    print(text_time)
elif m == 1:
    text_time = f'{t} {mm[m]} {mc[2]} {hh[h]}'
    print(text_time)
elif m >= 2 and m < 5:
    text_time = f'{t} {mm[m]} {mc[3]} {hh[h]}'
    print(text_time)
elif m >= 5 and m < 21:
    text_time = f'{t} {mm[m]} {mc[1]} {hh[h]}'
    print(text_time)
elif m == 21:
    text_time = f'{t} {mm[m-1]} {mm[1]} {mc[2]} {hh[h]}'
    print(text_time)
elif m >= 22 and m < 25:
    text_time = f'{t} {mm[m-(m-20)]} {mm[m-20]} {mc[3]} {hh[h]}'
    print(text_time)
elif m >= 25 and m < 30:
    text_time = f'{t} {mm[m-(m-20)]} {mm[m-20]} {mc[1]} {hh[h]}'
    print(text_time)
elif m == 30:
    text_time = f'{t} {b} {hh[h]}'
    print(text_time)
elif m == 31:
    text_time = f'{t} {mm[m-1]} {mm[1]} {mc[2]} {hh[h]}'
    print(text_time)
elif m >= 32 and m < 35:
    text_time = f'{t} {mm[m-(m-30)]} {mm[m-30]} {mc[3]} {hh[h]}'
    print(text_time)
elif m >= 35 and m < 40:
    text_time = f'{t} {mm[m-(m-30)]} {mm[m-30]} {mc[1]} {hh[h]}'
    print(text_time)
elif m == 40:
    text_time = f'{t} {mm[m]} {mc[1]} {hh[h]}'
    print(text_time)
elif m == 41:
    text_time = f'{t} {mm[m-1]} {mm[1]} {mc[2]} {hh[h]}'
    print(text_time)
elif m >= 42 and m < 45:
    text_time = f'{t} {mm[m-(m-40)]} {mm[m-40]} {mc[3]} {hh[h]}'
    print(text_time)
elif m >= 45 and m < 59:
    text_time = f'{t} {a} {mmm[m]} {mc[1]} {hh[h]}'
    print(text_time)
else:
    text_time = f'{t} {a} {mmm[m]} {mc[3]} {hh[h]}'
    print(text_time)