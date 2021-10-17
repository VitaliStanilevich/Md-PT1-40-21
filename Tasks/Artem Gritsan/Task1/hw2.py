from datetime import datetime as dt
hours = {
    '12': {'dft': 'первого', 'ex': 'двенадцать'},
    '1': {'dft': 'второго', 'ex': 'час'},
    '2': {'dft': 'третьего', 'ex': 'два'},
    '3': {'dft': 'четвертого', 'ex': 'три'},
    '4': {'dft': 'пятого', 'ex': 'четыре'},
    '5': {'dft': 'шестого', 'ex': 'пять'},
    '6': {'dft': 'седьмого', 'ex': 'шесть'},
    '7': {'dft': 'восьмого', 'ex': 'семь'},
    '8': {'dft': 'девятого', 'ex': 'восемь'},
    '9': {'dft': 'десятого', 'ex': 'девять'},
    '10': {'dft': 'одиннадцатого', 'ex': 'десять'},
    '11': {'dft': 'двенадцатого', 'ex': 'одиннадцать'},
}

minutes_def = {
    '1': {'most': 'одна', 'few': 'минуты'},
    '2': {'most': 'две', 'few': 'двух'},
    '3': {'most': 'три', 'few': 'трех'},
    '4': {'most': 'четыре', 'few': 'четырех'},
    '5': {'most': 'пять', 'few': 'пяти'},
    '6': {'most': 'шесть', 'few': 'шести'},
    '7': {'most': 'семь', 'few': 'семи'},
    '8': {'most': 'восемь', 'few': 'восьми'},
    '9': {'most': 'девять', 'few': 'девяти'},
    '11': {'most': 'одиннацдать', 'few': 'одиннацдати'},
    '12': {'most': 'двенадцать', 'few': 'двенадцати'},
    '13': {'most': 'тринадцать', 'few': 'тринадцати'},
    '14': {'most': 'четырнадцать', 'few': 'четырнадцати'},
    '15': {'most': 'пятнадцать', 'few': 'пятнадцати'},
    '16': {'most': 'шестнадцать'},
    '17': {'most': 'семнадцать'},
    '18': {'most': 'восемнадцать'},
    '19': {'most': 'девятнадцать'},

}
minutes_ten = {
    '1': 'десять',
    '2': 'двадцать',
    '3': 'тридцать',
    '4': 'сорок',
    '5': 'пятьдесят',

}
time = input('Введите время по типу "21:15", либо введите "now" для вывода текущего времени:\n')
if time == 'now':
    n = dt.now().strftime('%H:%M')
    t = n.split(':')
else:
    t = time.split(':')
if int(t[0]) > 12:
    t[0] = str(int(t[0]) - 12)
if t[1] == '00':
    if t[0] == '12':
        print('Полдень')
    elif t[0] == '0':
        print('Полночь')
    else:
        if t[0] == '1':
            print(f"{hours[t[0]]['ex'].capitalize()} ровно")
        elif int(t[0]) < 5:
            print(f"{hours[t[0]]['ex'].capitalize()} часа ровно")
        else:
            print(f"{hours[t[0]]['ex'].capitalize()} часов ровно")
elif t[1] == '30':
    print(f"Половина {hours[t[0]]['dft']}")
elif int(t[1]) < 45:
    if t[1] == '01':
        print(f"{minutes_def['1']['most'].capitalize()} минута {hours[t[0]]['dft']}")
    elif int(t[1]) < 5:
        print(f"{minutes_def[t[1][1]]['most'].capitalize()} минуты {hours[t[0]]['dft']}")
    else:
        if int(t[1][1]) == 0:
            print(f"{minutes_ten[t[1][0]].capitalize()} минут {hours[t[0]]['dft']}")
        elif int(t[1]) < 10:
            print(f"{minutes_def[t[1][1]]['most'].capitalize()} минут {hours[t[0]]['dft']}")
        elif int(t[1]) < 20:
            print(f"{minutes_def[t[1]]['most'].capitalize()} минут {hours[t[0]]['dft']}")
        else:
            if int(t[1][1]) == 1:
                print(f"{minutes_ten[t[1][0]].capitalize()} {minutes_def[t[1][1]]['most']} минута {hours[t[0]]['dft']}")
            elif int(t[1][1]) < 5:
                print(f"{minutes_ten[t[1][0]].capitalize()} {minutes_def[t[1][1]]['most']} минуты {hours[t[0]]['dft']}")
            else:
                print(f"{minutes_ten[t[1][0]].capitalize()} {minutes_def[t[1][1]]['most']} минут {hours[t[0]]['dft']}")
else:
    t[1] = str(60 - int(t[1]))
    t[0] = str(int(t[0]) + 1)
    print(f"Без {minutes_def[t[1]]['few']} {hours[t[0]]['ex']} ")






