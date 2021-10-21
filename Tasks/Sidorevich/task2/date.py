from datetime import datetime

hours = {
    1: {'form1': 'час', 'form2': 'первого'},
    2: {'form1': 'два', 'form2': 'второго'},
    3: {'form1': 'три', 'form2': 'третьего'},
    4: {'form1': 'четыре', 'form2': 'четвёртого'},
    5: {'form1': 'пять', 'form2': 'пятого'},
    6: {'form1': 'шесть', 'form2': 'шестого'},
    7: {'form1': 'семь', 'form2': 'седьмого'},
    8: {'form1': 'восемь', 'form2': 'восьмого'},
    9: {'form1': 'девять', 'form2': 'девятого'},
    10: {'form1': 'десять', 'form2': 'десятого'},
    11: {'form1': 'одиннадцать', 'form2': 'одиннадцатого'},
    12: {'form1': 'двенадцать', 'form2': 'двенадцатого'}
}

minutes = {
    1: {'form1': 'одна', 'form2': 'одной'},
    2: {'form1': 'две', 'form2': 'двух'},
    3: {'form1': 'три', 'form2': 'трёх'},
    4: {'form1': 'четыре', 'form2': 'четырёх'},
    5: {'form1': 'пять', 'form2': 'пяти'},
    6: {'form1': 'шесть', 'form2': 'шести'},
    7: {'form1': 'семь', 'form2': 'семи'},
    8: {'form1': 'восемь', 'form2': 'восьми'},
    9: {'form1': 'девять', 'form2': 'девяти'},
    10: {'form1': 'десять', 'form2': 'десяти'},
    11: {'form1': 'одиннадцать', 'form2': 'одиннадцати'},
    12: {'form1': 'двенадцать', 'form2': 'двенадцати'},
    13: {'form1': 'тринадцать', 'form2': 'тринадцати'},
    14: {'form1': 'четырнадцать', 'form2': 'четырнадцати'},
    15: {'form1': 'пятнадцать', 'form2': 'пятнадцати'},
    16: {'form1': 'шестнадцать'},
    17: {'form1': 'семнадцать'},
    18: {'form1': 'восемнадцать'},
    19: {'form1': 'девятнадцать'},
    20: {'form1': 'двадцать'},
    30: {'form1': 'тридцать'},
    40: {'form1': 'сорок'},
    50: {'form1': 'пятьдесят'},
}


def proc(h, m):
    """
    Преобразование времени формата hh:mm в текстовый формат.
    """
    H = h % 24
    h %= 12
    m %= 60

    if m == 0:
        if H == 12:
            return "полдень"
        elif H == 0 or H == 24:
            return "полночь"
        else:
            # Значение для часов
            body = "один" if h == 1 else hours[h]['form1']

            # Суффикс для часов
            suff = 'ов'
            if h == 1:
                suff = ''
            elif h in (2, 3, 4):
                suff = 'а'
            return f"{body} час{suff}"
    elif m == 30:
        return f"половина {hours[h+1]['form2']}"
    elif 0 < m < 45:
        # Значение для минут
        body = ''
        if m > 20 and m != 30 and m != 40 and m != 50:
            body = f"{minutes[m//10*10]['form1']} {minutes[m%10]['form1']}"
        else:
            body = minutes[m]['form1']

        # Суффикс для минут
        suff = ''
        if m in (11, 12, 13, 14):
            pass
        elif m % 10 == 1:
            suff = 'а'
        elif m % 10 in (2, 3, 4):
            suff = 'ы'

        return f"{body} минут{suff} {hours[h+1]['form2']}"
    else:
        # Значение для минут
        body = f"{minutes[60-m]['form2']}"

        # Суффикс для минут
        suff = 'ы' if 60-m == 1 else ''

        return f"без {body} минут{suff} {hours[h+1]['form1']}"


# Текущее время
h, m = datetime.now().hour, datetime.now().minute

print(f"Сейчас {h:>02}:{m:>02}")

# Заданное время
t = input("Введите время в формате 'hh:mm':\n").split(':')
h, m = int(t[0]), int(t[1])

if 0 <= h <= 24 and 0 <= m < 60:
    print(proc(h, m))
else:
    print("Неправильный формат")

# Проверка
# file = open("log.txt", 'w')

# for h in range(0, 25):
#     for m in range(0, 60):
#         msg = f"h={h}, m={m}: {proc(h, m)}"
#         file.write(msg + '\n')
#         file.flush()

# file.close()
